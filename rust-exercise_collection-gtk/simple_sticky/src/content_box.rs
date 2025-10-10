use adw::{gtk, glib};
use adw::prelude::*;
use adw::subclass::prelude::*;

glib::wrapper! {
    pub struct ContentBox(ObjectSubclass<imp::ContentBox>)
        @extends gtk::Box, gtk::Widget,
        @implements gtk::Accessible, gtk::Buildable,
            gtk::ConstraintTarget, gtk::Orientable;
}

impl ContentBox {
    pub fn new() -> Self {
        glib::Object::builder().build()
    }
    pub fn text_buffer(&self) -> glib::GString {
        self.imp().textview_buffer.text(
            &self.imp().textview_buffer.start_iter(),
            &self.imp().textview_buffer.end_iter(),
            true
        )
    }
    pub fn set_text_buffer(&self, text: &str) {
        self.imp().textview_buffer.set_text(text);
    }
}

mod imp {
    use super::*;

    #[derive(Debug, gtk::CompositeTemplate)]
    #[template(resource = "/io/github/signdo/ExerciseCollection/ui/content_box.ui")]
    pub struct ContentBox {
        #[template_child]
        pub textview_buffer: TemplateChild<gtk::TextBuffer>,
    }

    impl Default for ContentBox {
        fn default() -> Self {
            Self {
                textview_buffer: TemplateChild::default(),
            }
        }
    }

    #[glib::object_subclass]
    impl ObjectSubclass for ContentBox {
        const NAME: &'static str = "ContentBox";
        type Type = super::ContentBox;
        type ParentType = gtk::Box;

        fn class_init(klass: &mut Self::Class) {
            klass.bind_template();
        }

        // You must call `Widget`'s `init_template()` within `instance_init()`.
        fn instance_init(obj: &glib::subclass::InitializingObject<Self>) {
            obj.init_template();
        }
    }

    impl ObjectImpl for ContentBox {
        fn constructed(&self) {
            self.parent_constructed();
        }
    }

    impl WidgetImpl for ContentBox {}
    impl BoxImpl for ContentBox {}
}
