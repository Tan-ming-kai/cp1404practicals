from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Constructs main app"""
        super().__init__(**kwargs)
        self.names = ["bob", "bobby", "hobby", "jobby"]

    def build(self):
        """kivy GUI"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """creates a label for each name in names"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

    def clear_all(self):
        """Clear all widgets with the (main) id"""
        self.root.ids.main.clear_widgets()


DynamicLabelsApp().run()