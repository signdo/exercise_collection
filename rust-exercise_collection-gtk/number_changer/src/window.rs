use adw::{gtk, gio, glib};
use adw::subclass::prelude::*;
use adw::prelude::*;
use tracing::{info, error};

use crate::application::ExampleApplication;
use crate::config::{APP_ID, PROFILE};

mod imp {
    use super::*;

    #[derive(Debug, gtk::CompositeTemplate)]
    #[template(resource = "/io/github/signdo/ExerciseCollection/ui/window.ui")]
    pub struct ExampleApplicationWindow {
        #[template_child]
        pub btn_plus: TemplateChild<gtk::Button>,
        #[template_child]
        pub btn_minus: TemplateChild<gtk::Button>,
        #[template_child]
        pub num_label: TemplateChild<gtk::Label>,

        pub settings: gio::Settings,
    }

    impl Default for ExampleApplicationWindow {
        fn default() -> Self {
            Self {
                btn_plus: TemplateChild::default(),
                btn_minus: TemplateChild::default(),
                num_label: TemplateChild::default(),
                settings: gio::Settings::new(APP_ID),
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

            // Enable button click event
            obj.setup_callbacks();

            // Load latest window state
            obj.load_window_size();
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

    fn setup_callbacks(&self) {
        // Minus Button
        self.imp().btn_minus.connect_clicked(glib::clone!(
            #[weak(rename_to = num_label)] self.imp().num_label,
            move |_| {
                let num: i32 = num_label.label().parse().unwrap_or_else(|e| {
                    let err_str = format!("Unable convert GString to i32: [{}] Set default value.", e);

                    error!(err_str);
                    let err_dialog = adw::AlertDialog::builder()
                        .title("ERROR")
                        .body(&err_str)
                        .build();
                    err_dialog.add_response("ok", "OK");
                    err_dialog.present(Some(&num_label));
                    0
                }) - 1;
                num_label.set_label(num.to_string().as_str());
                info!("Minus button clicked: number = {}", num_label.label());
            }
        ));

        // Plus Button
        self.imp().btn_plus.connect_clicked(glib::clone!(
            #[weak(rename_to = num_label)] self.imp().num_label,
            move |_| {
                let num: i32 = num_label.label().parse().unwrap_or_else(|e| {
                    let err_str = format!("Unable convert GString to i32: [{}] Set default value.", e);

                    error!(err_str);
                    let err_dialog = adw::AlertDialog::builder()
                        .title("ERROR")
                        .body(&err_str)
                        .build();
                    err_dialog.add_response("ok", "OK");
                    err_dialog.present(Some(&num_label));
                    0
                }) + 1;
                num_label.set_label(num.to_string().as_str());
                info!("Plus button clicked: number = {}", num_label.label());
            }
        ));
    }
}
