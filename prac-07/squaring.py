from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder


class SquareNumberApp(App):

    def build(self):
        Window.size = (200, 100)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        try:
            result = int(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = ""


SquareNumberApp().run()
