import kivy
from kivy.app import App
from widgets.PingPongGame import *
from kivy.core.window import Window
Window.fullscreen = True
Window.maximize()
kivy.require('1.0.6')  # replace with your current kivy version !


class MyApp(App):

    def ___init__(self, **kwargs):
        return super().__init__(self, kwargs)

    def get_application_name(self) -> str:
        return 'Pong Game'

    def load_kv(self, filename=None):
        return super().load_kv("design/pongGameDesign.kv")

    def get_application_icon(self):
        return super().get_application_icon()

    def build(self):
        self.icon = 'assets/logo.jpg'
        return PongGameWidget()


if __name__ == '__main__':
    MyApp().run()
