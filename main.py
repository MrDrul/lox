# MemesPedia (Backend + Frontend)

# First Import The Modules!!
import requests
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.label import Label


# build the class App
class MemesPedia(App):

    # define the build function and design the layout
    def build(self):
        # run a try-except to notify if the connection is active
        try:

            f1 = FloatLayout()
            self.img = None

            self.label2 = Label(text="An unknown error occurred! Please check your connection and try again later!")

            # add exit button
            btn = Button(text="Exit!",
                         font_size="35sp",
                         background_color=(1, 0, 1, 1),
                         color=(1, 1, 1, 1),
                         size_hint=(.11, .1),
                         pos_hint={'x': .0, 'y': 0})
            btn.bind(on_press=self.callback1)
            f1.add_widget(btn)

            # add new meme button
            self.btn1 = Button(text='Next!',
                               font_size="35sp",
                               background_color=(0, 0, 1, 1),
                               color=(1, 1, 1, 1),
                               size_hint=(.11, .1),
                               pos_hint={'right': 1, 'y': 0})
            self.btn1.bind(on_press=self.get_meme)
            f1.add_widget(self.btn1)

            Clock.schedule_once(self.get_meme)

            # return the UI:
            return f1
        except:
            self.root.add_widget(self.label2)
            self.root.remove_widget(self.btn1)

    # define a function that generates new meme whenever the button is clicked
    def get_meme(self, *args):
        try:
            if self.img:
                self.root.remove_widget(self.img)

            # request the content from the url
            response = requests.get("https://meme-api.herokuapp.com/gimme")
            # extract the main meme url from json file and print it
            pass_times = response.json()['url']

            # identify the image from that meme url
            image_url = pass_times
            r = requests.get(image_url)
            # convert the image variable (r) to string
            r = str(requests.get(image_url))

            self.img = AsyncImage(source=pass_times)

            self.img.size_hint_x = 1
            self.img.size_hint_y = 1

            self.root.add_widget(self.img, index=2)

        except:
            self.root.add_widget(self.label2)
            self.root.remove_widget(self.btn1)

    # callback function foe exit button
    def callback1(self, event):
        exit()

    # callback function for next button
    def callback(self, event):
        try:
            return self.get_meme()
        except:
            self.root.add_widget(self.label2)
            self.root.remove_widget(self.btn1)


root = MemesPedia()
root.run()
