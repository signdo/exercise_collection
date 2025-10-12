use adw::{gtk, gio, glib};
use adw::subclass::prelude::*;
use adw::prelude::*;

use tracing::{debug, warn};

use crate::application::ExampleApplication;
use crate::config::{APP_ID, PROFILE};

mod imp {
    use std::cell::RefCell;

    use super::*;

    #[derive(Debug, gtk::CompositeTemplate)]
    #[template(resource = "/io/github/signdo/ExerciseCollection/ui/window.ui")]
    pub struct ExampleApplicationWindow {
        #[template_child]
        pub open_save_btn: TemplateChild<gtk::Button>,
        #[template_child]
        pub toast_overlay: TemplateChild<adw::ToastOverlay>,
        #[template_child]
        pub text_buffer: TemplateChild<gtk::TextBuffer>,

        pub settings: gio::Settings,
        pub filename: RefCell<Option<glib::GString>>,
    }

    impl Default for ExampleApplicationWindow {
        fn default() -> Self {
            Self {
                open_save_btn: TemplateChild::default(),
                toast_overlay: TemplateChild::default(),
                text_buffer: TemplateChild::default(),

                settings: gio::Settings::new(APP_ID),
                filename: RefCell::default(),
            }
        }
    }

    #[glib::object_subclass]
    impl ObjectSubclass for ExampleApplicationWindow {
        const NAME: &'static str = "ExampleApplicationWindow";
        type Type = super::ExampleApplicationWindow;
        type ParentType = adw::ApplicationWindow;

        fn class_init(klass: &mut Self::Class) {
            klass.bind_template();
        }

        // You must call `Widget`'s `init_template()` within `instance_init()`.
        fn instance_init(obj: &glib::subclass::InitializingObject<Self>) {
            obj.init_template();
        }
    }

    impl ObjectImpl for ExampleApplicationWindow {
        fn constructed(&self) {
            self.parent_constructed();
            let obj = self.obj();

            // Devel Profile
            if PROFILE == "Devel" {
                obj.add_css_class("devel");
            }

            // Load latest window state
            obj.load_window_size();

            obj.callback_textbuffer_modify_stat_changed();
            obj.callback_open_save_btn();
        }
    }

    impl WidgetImpl for ExampleApplicationWindow {}
    impl WindowImpl for ExampleApplicationWindow {
        // Save window state on delete event
        fn close_request(&self) -> glib::Propagation {
            if let Err(err) = self.obj().save_window_size() {
                tracing::warn!("Failed to save window state, {}", &err);
            }

            // Pass close request on to the parent
            self.parent_close_request()
        }
    }

    impl ApplicationWindowImpl for ExampleApplicationWindow {}
    impl AdwApplicationWindowImpl for ExampleApplicationWindow {}
}

glib::wrapper! {
    pub struct ExampleApplicationWindow(ObjectSubclass<imp::ExampleApplicationWindow>)
        @extends gtk::Widget, gtk::Window, gtk::ApplicationWindow, adw::ApplicationWindow,
        @implements gio::ActionMap, gio::ActionGroup,
                    gtk::Root, gtk::Native, gtk::ShortcutManager,
                    gtk::Accessible, gtk::Buildable, gtk::ConstraintTarget;
}

impl ExampleApplicationWindow {
    pub fn new(app: &ExampleApplication) -> Self {
        glib::Object::builder().property("application", app).build()
    }

    fn save_window_size(&self) -> Result<(), glib::BoolError> {
        let imp = self.imp();

        let (width, height) = self.default_size();

        imp.settings.set_int("window-width", width)?;
        imp.settings.set_int("window-height", height)?;

        imp.settings
            .set_boolean("is-maximized", self.is_maximized())?;

        Ok(())
    }

    fn load_window_size(&self) {
        let imp = self.imp();

        let width = imp.settings.int("window-width");
        let height = imp.settings.int("window-height");
        let is_maximized = imp.settings.boolean("is-maximized");

        self.set_default_size(width, height);

        if is_maximized {
            self.maximize();
        }
    }

    fn callback_textbuffer_modify_stat_changed(&self) {
        self.imp().text_buffer.connect_modified_changed(glib::clone!(
            #[weak(rename_to = app_window)] self,
            move |_| {
                debug!("Text buffer modify state changed...");

            if app_window.imp().text_buffer.is_modified() {
                app_window.imp().open_save_btn.set_label("Save");
                app_window.imp().open_save_btn.set_css_classes(&["destructive-action"]);
            } else {
                app_window.imp().open_save_btn.set_label("Open");
                app_window.imp().open_save_btn.set_css_classes(&["suggested-action"]);
            }
        }));
    }

    fn callback_open_save_btn(&self) {
        self.imp().open_save_btn.connect_clicked(glib::clone!(
            #[weak(rename_to = app_window)] self,
            move |_| {
                if app_window.imp().text_buffer.is_modified() == false {
                    // for clean data
                    debug!("Text buffer is clean...");

                    let file_dialog = gtk::FileDialog::builder()
                        .title("Open File:")
                        .accept_label("Open")
                        .build();

                    file_dialog.open(
                        Some(app_window.root().unwrap().downcast_ref::<gtk::ApplicationWindow>().unwrap()),
                        gio::Cancellable::NONE,
                        move |result | {
                            if let Ok(file) = result {
                                // Another method:
                                //
                                // let filepath = file.path().unwrap();
                                // debug!("File path = {}", filepath.to_str().unwrap());
                                //
                                let filename = file.parse_name();
                                debug!("File name = {}", filename);

                                if let Ok(content) = std::fs::read_to_string(filename.clone()) {
                                    debug!("File content = {}", content);
                                    app_window.imp().text_buffer.set_text(&content);

                                    // Update text_buffer will change modify state
                                    app_window.imp().text_buffer.set_modified(false);
                                    *app_window.imp().filename.borrow_mut() = Some(filename.clone());

                                } else {
                                    let warn_info = format!("Cannot open file: {}", filename);
                                    warn!(warn_info);

                                    let toast = adw::Toast::builder()
                                        .title(warn_info)
                                        .timeout(2)
                                        .build();
                                    app_window.imp().toast_overlay.add_toast(toast);
                                };
                            } else {
                                warn!("No file selected.");
                            }
                        }
                    );
                } else {
                    // for dirt data
                    debug!("Text buffer is dirt...");

                    let text_buffer = app_window.imp().text_buffer.text(
                        &app_window.imp().text_buffer.start_iter(),
                        &app_window.imp().text_buffer.end_iter(),
                        true
                    );

                    if let Some(filename) = &(*app_window.imp().filename.borrow()) {
                        // If file from user open
                        if let Err(err) = std::fs::write(filename, text_buffer) {
                            let warn_info = format!("Cannot save file: {}", err);
                            warn!(warn_info);

                            let toast = adw::Toast::builder()
                                .title(warn_info)
                                .timeout(2)
                                .build();
                            app_window.imp().toast_overlay.add_toast(toast);
                        } else {
                            debug!("File saved.");

                            // Set buffer state to clean
                            app_window.imp().text_buffer.set_modified(false);
                        };
                    } else {
                        // If new file
                        let file_dialog = gtk::FileDialog::builder()
                            .title("Save File:")
                            .accept_label("Save")
                            .initial_name("Untitled.txt")
                            .build();

                        file_dialog.save(
                            Some(app_window.root().unwrap().downcast_ref::<gtk::ApplicationWindow>().unwrap()),
                            gio::Cancellable::NONE,
                            move |result | {
                                if let Ok(file) = result {
                                    let filename = file.parse_name();
                                    debug!("File name = {}", filename);

                                    if let Err(err) = std::fs::write(filename.clone(), text_buffer) {
                                        let warn_info = format!("Cannot save file: {}", err);
                                        warn!(warn_info);

                                        let toast = adw::Toast::builder()
                                            .title(warn_info)
                                            .timeout(2)
                                            .build();
                                        app_window.imp().toast_overlay.add_toast(toast);
                                    } else {
                                        debug!("File saved.");

                                        // Set buffer state to clean
                                        app_window.imp().text_buffer.set_modified(false);
                                        *app_window.imp().filename.borrow_mut() = Some(filename.clone());
                                    };

                                } else {
                                    warn!("No file selected.");
                                }
                            }
                        );

                    }

                }

            }
        ));
    }
}
