from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, BooleanProperty

class GridLayoutExample(GridLayout):
    text = StringProperty("Hello")
    count_enabled = BooleanProperty(True)
    post_text = StringProperty("")
    count = 0
    def on_toggle_button_state(self, widget):
        if widget.state == 'down':
            widget.text = 'ON'
            self.count_enabled = False
        else:
            widget.text = 'OFF'
            self.count_enabled = True

    def on_click(self):
        self.count += 1
        self.text = str(self.count)    


    def on_text_validate(self, widget):
        self.post_text = widget.text


class TheLabApp(App):
    pass

TheLabApp().run()