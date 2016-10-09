import os
from PIL import Image
from PIL import ImageTk
import tkinter as tk

'''
A Character is a character in the game
Has a image associated with them

Character file format:
<img location>
'''

class Character:
    def __init__(self, filename):
        cwd = os.path.dirname(filename)
        with open(filename, 'r') as f:
            self.imgName = os.path.join(cwd, f.readline().strip())     
        self.img = Image.open(self.imgName)
        
    def draw(self, scene):
        newSize = self.img.size[0] * scene.scale, self.img.size[1] * scene.scale
        self.imgTk = ImageTk.PhotoImage(self.img.resize(newSize), size = newSize)
        scene.scene.create_image((0,0), image=self.imgTk, anchor=tk.CENTER)   
        

if __name__ == "__main__":
    pass


