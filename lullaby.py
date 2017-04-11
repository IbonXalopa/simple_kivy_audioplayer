# -*-coding:utf8;-*-
# qpy:2
# qpy:kivy

from kivy.app import App

from kivy.core.audio import SoundLoader

from kivy.uix.button import Button


class myApp(App):
    def build(self):
        # display a button with the text.
        return Button(text="Goodnight <Your Baby's Name>")

    def on_pause(self):
        return True

# In soundLoader belwo, you will have to introduce a path to your audio file.
sound = SoundLoader.load('/storage/emulated/0/Music/utulanki.m4a')

if sound:
    print("Sound found at %s" % sound.source)
    print("Sound is %.3f seconds" % sound.length)
    sound.play()

if __name__ == '__main__':
    myApp().run()