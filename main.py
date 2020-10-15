from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivy.core.window import Window
import sports

### Initializing the modules.

### Kv File and code.
screen_helper = """
ScreenManager:
    LandingScreen:
    PredictScreen:
    ScoresScreen:
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
        icon: "tennis"
        user_font_size: "120sp"
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
        text: 'Predict'
        pos_hint: {'center_x':0.2,'center_y':0.8}
        on_press: root.manager.current = 'Predict'
    MDRoundFlatButton:
        text: 'Scores'
        pos_hint: {'center_x':0.8,'center_y':0.8}
        on_press: root.manager.current = 'note'
    MDLabel:
        text: 'Menu'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H4'
    MDIconButton:
        halign: "center"
        pos_hint: {'center_x':0.5,'center_y':0.5}
        icon: "tennis"
        user_font_size: "120sp"
        on_press: 
 
<PredictScreen>:
    label_wid: label_field
    name: 'Predict'
    MDLabel:
        text: 'SimScore'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.925}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
    MDLabel:
        text: 'Predict'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H4'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.8}
        on_press: root.manager.current = 'menu'
    MDTextField:
        id: text_field
        multiline: True
        size_hint: (.95, None)
        hint_text: ''
        pos_hint: {'center_x':0.5,'center_y':0.5}
        font_size: '18'
    MDIconButton:
        icon: "tennis"
        user_font_size: "30sp"
        ripple_scale: .5
        pos_hint: {"center_y": .52}
        pos: text_field.width - self.width + dp(8), 0
        on_press: label_field.text = text_field.text
        on_release: text_field.text = '' 
        
    MDLabel:
        id: label_field
        text: ''
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.2}
        theme_text_color: "Hint"
     
    
    
    

    

<ScoresScreen>:
    name: 'note'
    MDLabel:
        text: 'SimScore'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.925}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H3'
    MDLabel:
        text: 'All scores are in format X-X = Sets.'
        halign: 'center'
        pos_hint: {'center_x':0.5,'center_y':0.825}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: 'H6'
    MDLabel:
        text:   app.text
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


class PredictScreen(Screen):
    pass


class ScoresScreen(Screen):
    pass


class LandingScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(PredictScreen(name='Predict'))
sm.add_widget(ScoresScreen(name='note'))
sm.add_widget(PredictScreen(name='land'))



### Main app class that calls the sports scores.
class AppApp(MDApp):
    matches = sports.get_sport(sports.TENNIS)
    text = str(matches)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.screen = Builder.load_string(screen_helper)
        return self.screen






AppApp().run()
