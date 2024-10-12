from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

# Set the background color of the window
Window.clearcolor = (1, 0, 1, 1)  # RGBA for magenta

class MyApp(App):
    def build(self):
        # Create a label with text and font size
        label = Label(text='Learning Kivy', font_size='50sp')
        return label

# Run the app
if __name__ == '__main__':
    MyApp().run()