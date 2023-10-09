from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '400')  # 16:9
Config.set('graphics', 'resizable', False)  # ウインドウリサイズ禁止

# 起動時の解像度の設定

class Test(BoxLayout):
    def __init__(self, **kwargs):
        super(Test, self).__init__(**kwargs)

        self.count = 0
        #デフォルトは"horizontal"水平方向に配置されます。
        self.orientation = "horizontal"
        #self.orientation = "vertical"

        btn = Button(text='Hello World', on_press=self.click)
        self.add_widget(btn)
        lbl = Label(text='label')
        self.add_widget(lbl)
        lbl.markup = True
        lbl.text += '[color=#FF00CC]color text[/color]\n'
        lbl.size = (20, 100)
        lbl.font_size = 20
    def click(self,btn):
        print(type(self),type(btn))
        self.count += 1
        self.add_widget(Button(text="{}".format(self.count),on_press=self.dismiss,on_release=self.on_release ))

    def dismiss(self,a):
        print(type(self),type(a))
        self.remove_widget(a)
        
    def on_release(self,a):
        pass
        
class Sample(App):
    def build(self):
        return Test()
    
    def on_stop(self):
        print('on_stop:アプリケーションを終了します')
        try:
            pass 
        finally:
            pass
            quit() 
            
if __name__ == '__main__':
    Sample().run()