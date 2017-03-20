# Paint App Sample
#from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.colorpicker import ColorPicker
from kivy.graphics import Color, Ellipse, Line

class ClearButton(Button):
    pass

class ColorChangeButton(Button):
    pass

class SaveButton(Button):
    pass        

class MyPopup(Popup):
    pass

class MyPaintWidget(Widget):
    color = [1, 1, 1, 1]
    def on_touch_down(self, touch):
        with self.canvas:
            Color(rgba=(self.color))
            d = 5
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(pos=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
    
    def clear_canvas(self,*args):
        self.canvas.clear()

    def save_canvas(self,*args):
        self.export_to_png("screenshot.png")
        
    def open_popup(self):
        popup = MyPopup()
        popup.open()

class MyPaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = MyPaintWidget(size=[800,600])
        clearbtn = ClearButton()
        colorbtn = ColorChangeButton()
        savebtn = SaveButton()
        parent.add_widget(self.painter)
        parent.add_widget(savebtn)
        parent.add_widget(colorbtn)
        parent.add_widget(clearbtn)
        return parent
    
if __name__ == '__main__':
    MyPaintApp().run()