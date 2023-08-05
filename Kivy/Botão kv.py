from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        return Button()

    def on_press_button(self):
        print('Você apertou o botão!')

if __name__ == '__main__':
    app = ButtonApp()
    app.run()