from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self):
        super().__init__()
        self.names = ['Alice', 'Bob', 'Charlie', 'Dave']

    def build(self):
        main = BoxLayout(orientation='vertical')
        for name in self.names:
            label = Label(text=name)
            main.add_widget(label)
        return main

if __name__ == '__main__':
    DynamicLabelsApp().run()
