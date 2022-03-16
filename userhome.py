from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang.builder import Builder
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivymd.uix.snackbar import Snackbar
import requests
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker
from kivy.uix.colorpicker import ColorPicker
from kivymd.uix.picker import MDThemePicker

config = {
  "apiKey": "AIzaSyB2BZjMWxuuWGCxYiy39nM2QW6YNaEYejM",
 " authDomain": "isaifirst-434b9.firebaseapp.com",
  "databaseURL": "https://isaifirst-434b9-default-rtdb.firebaseio.com/",
  "projectId": "isaifirst-434b9",
  "storageBucket": "isaifirst-434b9.appspot.com",
  "messagingSenderId": "577271030988",
  "appId": "1:577271030988:web:bc9f35c4b8c6501b248e69",
  "measurementId": "G-K8KL14RGJG",
 "serviceAccount":"serviceAccount.json"

}
Window.size = (250, 500)


class WelcomeScreen(MDApp):
    pass


class SignupScreen(Screen):
    pass


class Home(MDApp):
    def screen(self, screen):
        sm = ScreenManager()  # screenmanager
        screens = {}  # screenmanager


class SecondScreen():
    def on_pre_enter(self):
        self.ids.scr4.text = "Second Screen Updated"

    """def __init__(self, *kwargs):
        super(Home, self).__init__()
          """


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class services(MDApp):
    def __init__(self):
        super(services, self).__init__()
        pass


class NavigationDrawer(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_file('userhome.kv')
        return self.screen

    def show_date_picker(self):
        date_dialog = MDDatePicker(mode="range")
        date_dialog.open()

    def color_theme_callback(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def userinput(self, phone, email, name, location, issue):
        if len(phone) != 10:
            err = Snackbar(text="invalid phone number", md_bg_color=[0, 0.3, 0, 1])
            err.open()
        else:
            if len(phone) == 10:
                err = Snackbar(text="Success")
                err.open()
        # def userinput(self, phone, email, name):

        # def userinput(self, phone, email, name):
        '''if len(name) == len(phone) == "":
            err = Snackbar(text="invalid information")
            err.open()
        else:
            if len(phone) == 10 and len(name) >= 1:
                err = Snackbar(text="success")
                err.open()'''
        if len(name) == "":
            err = Snackbar(text="must me more than 5 characters ")
            err.open()
        else:
            if len(name) > 5:
                err = Snackbar(text=" success")
                err.open()

            # valid=re.search("r^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$",email)
            # SUBMITTING data to database.
            url = "https://isaifirst-434b9-default-rtdb.firebaseio.com/.json"
            JSON = {"phoneNum": f"{phone}", "useremail": f"{email}", "username": f"{name}", "location": f"{location}",
                    "issue": f"{issue}"}
            res = requests.post(url=url, json=JSON)
    def send_comment(self,*args):
        pass

    def view_information(self, view_information):
        url = "https://isaifirst-434b9-default-rtdb.firebaseio.com/.json"
        self.auth_key = 'bTwFAO5zo89eyXpTu30B4C3Fh2hsw3p3JBDZOgYA'
        from_database = requests.get(url=url + '?auth=' + self.auth_key)
        # for data in database.json():
        print(from_database.json())
        new_label = self.root.ids.view_information
        new_label.text = from_database.text


NavigationDrawer().run()
