import kivy
from kivy.app import App
from kivy.uix.widget import Widget

class kivyStudiesWidget(Widget):
    pass

class kivystudiesApp(App):
    def build(self):
        return kivyStudiesWidget()

if __name__ == '__main__':
    kivystudiesApp().run()