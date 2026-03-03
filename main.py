from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList , OneLineListItem
from kivymd.uix.button import MDFlatButton , MDFloatingActionButton
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.label import MDLabel

import webbrowser
import AppOpener as ao
import speech_recognition as sr
import pyttsx3
import pywhatkit
import os

import sys
import os
from kivy.config import Config
Config.set('kivy', 'window_icon', 'icon.ico')

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))
        

class myApp(MDApp):
    def build(self):
        self.kv = Builder.load_file(os.path.join(base_path, "myui.kv"))
        return self.kv
    
    def on_start(self):
        
        cmd_list = self.kv.ids.cmd_list
        
        file_path_c = os.path.join(base_path, "text_commands.txt")

        with open(file_path_c, "r") as f:
            line_l = f.readlines()
            num = len(line_l)
                
            for i in range(num):
                item = OneLineListItem(text = line_l[(num-i)-1])
                cmd_list.add_widget(item)
                    
                
    
    #switch to dark theme
    
    def dark(self):
        app_bar = self.kv.ids.top_bar
        app_bar.right_action_items = [["white-balance-sunny",lambda x : self.light()]]
        self.theme_cls.theme_style = "Dark"
        
    #switch to light theme
    
    def light(self):
        app_bar = self.kv.ids.top_bar
        app_bar.right_action_items = [["moon-waning-crescent",lambda x : self.dark()]]
        self.theme_cls.theme_style = "Light"
    
    # alert dialogbox
    
    def dialog(self , text):
        self.btn = MDFlatButton(text = "close" , on_release = self.dialog_close)
        self.dialog = MDDialog(title = "Error" , text = text , size = (1,1) , buttons = [self.btn])
        self.dialog.open()
        
    #closing of dialogbox
    
    def dialog_close(self):
        self.dialog.dismiss()
        
    def change_voice(self):
        btn = self.kv.ids.voice_btn
        
        if(btn.text == "Male voice"):
            btn.text = "Female voice"
            MDSnackbar(
            MDLabel(
                text="Setted as male voice",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                ),
                duration=2  # disappears after 2 seconds
                ).open()
                 
            
        else :
            btn.text = "Male voice"
            MDSnackbar(
            MDLabel(
                text="Setted as female voice",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                ),
                duration=2  # disappears after 2 seconds
                ).open()
            
            
    def setting(self):
        set = self.kv.ids.card
        button = self.kv.ids.voice_btn
        if(set.opacity == 0):
            set.opacity = 1
            
        else :
            set.opacity = 0
    
    # by default male voice
    
    # def speak(self,words):
    #     engine = pyttsx3.init()
    #     engine.say(words)
    #     engine.runAndWait()
    
    
        
        
    # settings of voice

    def speak_male(self,text):
        engine1 = pyttsx3.init()
        voices1 = engine1.getProperty('voices')
        engine1.setProperty('voice', voices1[0].id)
        engine1.say(text)
        engine1.runAndWait()
        
        #female voice choice
        
    def speak_female(self,text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

            
        
        #processing texual input
    def process_cmd(self):
        
        command = self.kv.ids.input.text
        voice = self.kv.ids.voice_btn
        
        cmd = command.lower()
        try:
            if (("open" in cmd) and not(("web" or "google" or "browser") in cmd)):
                app = cmd[cmd.find(" "):len(cmd)]
                
                if(voice.text == "Male voice"):
                    self.speak_female(f"opening {app}")
                    
                elif(voice.text == "Female voice"):
                    self.speak_male(f"opening {app}")
            
                ao.open(app)
                
                if (("open" in cmd) and ("v" and "s" and "code" in cmd)):
                    ao.open("visual studio code")
                    
                elif((("c" or "d") and "drive" in cmd) or ("files" in cmd)):
                    ao.open("file explorer")
                    
                elif(("chrome" in cmd) or ("google" in cmd)):
                    ao.open("google chrome")
                    
                elif(("power point" in cmd) or ("ppt" in cmd) or ("microsoft power point" in cmd) or ("microsoft powerpoint"in cmd)):
                    ao.open("powerpoint")
                    
                
        
                
                
                
            elif ("open" in cmd) and (("web" or "google" or "browser" or "website") in cmd):
                web = cmd[cmd.find(" "):len(cmd)]
                
                if(voice.text == "Male voice"):
                    self.speak_female(f"opening {web}")
                    
                else:
                    self.speak_male(f"opening {web}")
                    
                    webbrowser.open(f"https://www.google.com/search?q={web}")
                
            elif(("play" in cmd) and (("song" or "music") in cmd)and (not("spotify" in cmd))):
                song_name = cmd[cmd.find(" "):len(cmd)]
                
                if(voice.text == "Male voice"):
                    self.speak_female(f"playing {video}")
                    
                else:
                    self.speak_male(f"playing {video}")
                    
                webbrowser.open(f"https://music.youtube.com/search?q={song_name}")
                
                
                
            elif ("play" in cmd) and ("spotify" in cmd):
                song = cmd[cmd.find(" "):len(cmd)]
                
                if(voice.text == "Male voice"):
                    self.speak_female(f"playing {song}")
                    
                else:
                    self.speak_male(f"playing  {song}")
                    
                webbrowser.open(f"https://open.spotify.com/search/{song}")
                    
                
            elif("play" in cmd) and ("video" or "movie" in cmd):
                video = cmd[cmd.find(" "):len(cmd)]
                
                if(voice.text == "Male voice"):
                    self.speak_female(f"playing {video} on youtube")
                    
                else:
                    self.speak_male(f"playing {video} on youtube")
                    
                pywhatkit.playonyt(video)
                
                
            elif("close" in cmd):
                window = cmd[cmd.find(" ") : len(cmd)]
                ao.close(window)
                
            elif(cmd == ""):
                
                if(voice.text == "Male voice"):
                    self.speak_female("give me any command........")
                    
                else:
                    self.speak_male("give me any command........")
                    
                
            else:
                webbrowser.open(f"https://www.bing.com/search?q={cmd}&form=ANNTH1&refig=698a0d08b9994ba38115441d2f74c764&pc=HCTS&pq=copilot&mturn=1")
            
            
            #file handling for history

            file_path = os.path.join(base_path, "text_commands.txt")
            with open(file_path, "a") as f:
                f.write(cmd +"\n")
                    
                
        
                
        
            
        except FileNotFoundError :
                print("file not found please enter valid name.")
                self.dialog("please check name of app and enter correct name")
                
        
        
        
        
        
#voice recognition and command processing
        
    def voice_command(self , cmd2):
        
        voice = self.kv.ids.voice_btn
        
        try:
            if (("open" in cmd2) and (("web" or "google" or "browser") not in cmd2)):
                app = cmd2[cmd2.find(" "):len(cmd2)]
                
                if(voice.text == "Male voice"):
                    self.speak_female(f"opening{app}")
                    
                elif(voice.text == "Female voice"):
                    self.speak_male(f"opening{app}")
                    
                ao.open(app)
                    
                
                if (("open" in cmd2) and ("v" and "s" and "code" in cmd2)):
                    ao.open("visual studio code")
                    
                elif((("c" or "d") and "drive" in cmd2) or ("files" in cmd2)):
                    ao.open("file explorer")
                    
                elif(("chrome" in cmd2) or ("google" in cmd2)):
                    ao.open("google chrome")
                    
                elif(("power point" in cmd2) or ("ppt" in cmd2) or ("microsoft power point" in cmd2) or ("microsoft powerpoint"in cmd2)):
                    ao.open("powerpoint")
                    
                
                
        
                
                
                
            elif ("open" in cmd2) and (("web" or "google" or "browser" or "website") in cmd2):
                web = cmd2[cmd2.find(" "):len(cmd2)]
                
                webbrowser.open(f"https://www.google.com/search?q={web}")
                
                if(voice.text == "Male voice"):
                    self.speak_female(f"opening{web}")
                    
                else:
                    self.speak_male(f"opening{web}")
                
                
            elif("play" in cmd2) and ("video" or "movie" in cmd2):
                video = cmd2[cmd2.find(" "):len(cmd2)]
                pywhatkit.playonyt(video)
                
                if(voice.text == "Male voice"):
                    self.speak_female(f"playing {video} on youtube")
                    
                else:
                    self.speak_male(f"playing {video} on youtube")
                    
                
            elif("play" in cmd2) and (("youtube" and "song") in cmd2):
                song = cmd2[cmd2.find(" "):len(cmd2)]
                pywhatkit.playonyt(song)
                
                if(voice.text == "Male voice"):
                    self.speak_female(f"playing {video} on youtube")
                    
                else:
                    self.speak_male(f"playing {video} on youtube")
                
            elif ("play" in cmd2) and ("spotify" in cmd2):
                name = cmd2[cmd2.find(" "):len(cmd2)]
                webbrowser.open(f"https://open.spotify.com/search/{name}")
                
                if(voice.text == "Male voice"):
                    self.speak_female(f"{name}")
                    
                else:
                    self.speak_male(f" {name}")
                
            elif("close" in cmd2):
                window = cmd2[cmd2.find(" ") : len(cmd2)]
                ao.close(window)
                
            elif(cmd2 == ""):
                if(voice.text == "Male voice"):
                    self.speak_female("give me any command.....")
                    
                else:
                    self.speak_male("give me eny command.....")
                
                
            elif(("what" or "when" or "who" or "why" or "whome" or "where") in cmd2):
                webbrowser.open(f"https://www.bing.com/search?q={cmd2}&form=ANNTH1&refig=698a0d08b9994ba38115441d2f74c764&pc=HCTS&pq=copilot&mturn=1")
                
                if(voice.text == "Male voice"):
                    self.speak_female("Answer of your query is searched on web ,it is in fornt of you...")
                    
                else:
                    self.speak_male("Answer of your query is searched on web ,it is in fornt of you...")
                    
                    
            # file handling for history

            file_path = os.path.join(base_path, "text_commands.txt")
            with open(file_path, "a") as f:
                f.write(cmd2 + "\n")
                    
                
                    
                
                    
            
                
        
            
        
                
        except Exception as e :
            self.dialog(f" {str(e)} /n Please try again" )
              
        
        
        
        
    def speech_recognition(self):
        

# Initialize recognizer
        voice_btn = self.kv.ids.voice_btn
        recognizer = sr.Recognizer()
       

        # Use microphone as input
        
        if(voice_btn.text == "Male voice"):
            self.speak_female("How can I help you.")
            
        else : 
            self.speak_male("How can I help you.")
        
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)  # reduce background noise
            audio = recognizer.listen(source, phrase_time_limit= 4.5)
            command2 = recognizer.recognize_google(audio)
            
        try:
                
            cmd3 = command2.lower()
            self.voice_command(cmd3)
            print("You said:", cmd3)
                    
                    

        except sr.UnknownValueError:
            self.dialog("Sorry, I could not understand the audio. please try again")

        except sr.RequestError:
            self.dialog("Could not request results. Check your internet connection.")
                
        except Exception as e :
            self.dialog(str(e))
                    
# Run App  
if __name__ == "__main__":
    myApp().run()