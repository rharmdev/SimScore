from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
import sports

screen_helper = """
ScreenManager:
    LandingScreen:
    FootballScreen:
    TennisScreen:
    MenuScreen:

<LandingScreen>:
    name: 'land'
    MDLabel:
        text: 'SimScore'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.925}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
    MDIconButton:
        halign: "center"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        icon: "soccer-field"
        user_font_size: "150sp"
        on_press: root.manager.current = 'menu'
    MDLabel:
        text: 'Created by Rharm Manju'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.3}
        theme_text_color: "Hint"




<MenuScreen>:
    name: 'menu'
    MDLabel:
        text: 'SimScore'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.925}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
    MDRoundFlatButton:
        text: 'Football'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'football'
    MDRoundFlatButton:
        text: 'Tennis'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'tennis'
    MDLabel:
        text: 'Menu'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H4'
    MDIconButton:
        halign: "center"
        pos_hint: {'center_x':0.8,'center_y':0.5}
        icon: "tennis"
        user_font_size: "120sp"
        on_press: root.manager.current = 'tennis'
    MDIconButton:
        halign: "center"
        pos_hint: {'center_x':0.2,'center_y':0.5}
        icon: "soccer"
        user_font_size: "120sp"
        on_press: root.manager.current = 'football'
 
 
<FootballScreen>:
    name: 'football'
    MDLabel:
        text: 'SimScore'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.925}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
    MDLabel:
        text: 'All Football scores are in format X-X = Goals.'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.825}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H6'
    MDLabel:
        text:   app.footballtext
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Hint"
        text_color: 1, 1, 1, 1
        font_style: 'Body1'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
    
    
    

    

<TennisScreen>:
    name: 'tennis'
    MDLabel:
        text: 'SimScore'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.925}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
    MDLabel:
        text: 'All Tennis scores are in format X-X = Sets.'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.825}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H6'
    MDLabel:
        text:   app.tennistext
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.55}
        theme_text_color: "Hint"
        text_color: 1, 1, 1, 1
        font_style: 'Body1'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

"""


class MenuScreen(Screen):
    pass


class FootballScreen(Screen):
    pass


class TennisScreen(Screen):
    pass


class LandingScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(FootballScreen(name='football'))
sm.add_widget(TennisScreen(name='tennis'))
sm.add_widget(LandingScreen(name='land'))


class AppApp(MDApp):
    tennismatches = sports.get_sport(sports.TENNIS)
    tennistext = str(tennismatches)
    all_matches = sports.all_matches()
    footballmatches = all_matches['soccer']
    footballtext = str(footballmatches)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(screen_helper)
        return self.screen


AppApp().run()
