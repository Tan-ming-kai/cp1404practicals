
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETERS = 1.6

class MilesToKm(App):
    """kivy app to change miles to km"""
    message = StringProperty()
    """ MilesToKm App changes miles to kilometers """

    def build(self):
        """build kivy GUI"""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def converts_distance(self, value):
        """converts the distance from miles to KM"""
        try:
            result = float(value) / MILES_TO_KILOMETERS
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "0"

    def handles_output(self, message):
        """sets the output label to a string """
        self.root.ids.output_label.text = message

    def handle_increment(self, value):
        """either increase or decrease the user value by 1 based on up or down"""
        new_value = int(self.root.ids.miles_input.text) + value
        self.root.ids.miles_input.text = str(new_value)
        self.converts_distance(new_value)



MilesToKm().run()