from kivy.app import App
from kivy.uix.button import Button

class myapp(App):
    def bulid(self):
        return Button(text='hello,kivy!')
    
if __name__ == '__main__':
    myapp().run()
    myapp.show(self)
    block=True