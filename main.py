import os
import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.core.clipboard import Clipboard


Window.size = (480, 500)  #620
Window.clearcolor = 238/255, 238/255, 238/255, 1  #(252/255, 89/255, 74/255, 1)

class StartScreen(Screen):
    def wait(self):
        self.label1.text = "Please wait..."
    def generator(self):
        file1 = open(self.firstInput.text, "r", encoding='cp437')
        file2 = open(self.secondInput.text, "r", encoding='cp437')
        file3 = open("UnfollowersList.txt", "w+", encoding='cp437')
        temp1 = []
        temp2 = []
        followingList = []
        followersList = []
        unfollowersList = []

        for data in file1:
            temp1.append(data)
        for data in temp1:
            if (data == "Verified\n"):
                temp1.remove(data)
        #print(len(temp1))

        for data in temp1:
            if (data.find("profile") > -1):
                i = temp1.index(data) + 1
                followingList.append(temp1[i])

        # print("i follow: ",followingList)
        #print("i follow: ", len(followingList))
        file1.close()

        for data in file2:
            temp2.append(data)
        for data in temp2:
            if (data == "Verified\n"):
                temp2.remove(data)
        # print(list2)
        for data in temp2:
            if (data.find("profile") > -1):
                i = temp2.index(data) + 1
                followersList.append(temp2[i])

        #print("follows me:", len(followersList))
        file2.close()

        setOne = set(followingList)
        setTwo = set(followersList)

        setThree = setOne - setTwo
        unfollowersList = []
        for data in setThree:
            unfollowersList.append(data)
            file3.write(data)




        str1 = str(len(unfollowersList)) + " people don't follow you back!"
        file3.write(".........................................\n")
        file3.write(str1 + "\n")

        os.startfile("UnfollowersList.txt")

        self.label1.text = str1

        file3.close()

class ScreenManagement(ScreenManager):
    pass



presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        self.title = "UnfollowersList"
        self.icon = "images/instagram1.png"
        return presentation

if __name__ == "__main__":
    MainApp().run()