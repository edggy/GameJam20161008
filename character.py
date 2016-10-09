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
        self.scalingMethod = Image.LANCZOS
        
        cwd = os.path.dirname(filename)
        with open(filename, 'r') as f:
            self.imgName = os.path.join(cwd, f.readline().strip()) 
            self.center = tuple(map(int, f.readline().split()))
        self.img = Image.open(self.imgName)
        ratio = 540 / self.img.size[1]
        
        newSize = tuple(map(lambda x: int(x*ratio), self.img.size))
        self.img = self.img.resize(newSize, self.scalingMethod)
        
        self.center = tuple(map(lambda x: int(x*ratio), self.center))
        
        
    def draw(self, scene, location):
        newSize = int(self.img.size[0] * scene.scale), int(self.img.size[1] * scene.scale)
        self.imgTk = ImageTk.PhotoImage(self.img.resize(newSize, self.scalingMethod), size = newSize)
        scene.scene.create_image(tuple(map(lambda x: x * scene.scale, (location[0] - self.center[0], location[1] - self.center[1]))), image=self.imgTk, anchor=tk.NW)
        

if __name__ == "__main__":
    pass


