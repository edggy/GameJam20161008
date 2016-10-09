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
        
        self.imgNames = []
        self.imgs = []
        
        with open(filename, 'r') as f:
            numArt = int(f.readline())
            for i in range(numArt):
                filename = os.path.join(cwd, f.readline().strip())
                center = tuple(map(int, f.readline().split()))
                self.imgNames.append((filename, center))
        
        for filename, center in self.imgNames:
            img = Image.open(filename)
            ratio = 540 / img.size[1]
            
            newSize = tuple(map(lambda x: int(x*ratio), img.size))
            img = img.resize(newSize, self.scalingMethod)
            
            center = tuple(map(lambda x: int(x*ratio), center))
            
            self.imgs.append((img, center))
        
        
    def draw(self, scene, location, imgNum):
        img, center = self.imgs[imgNum]
        newSize = int(img.size[0] * scene.scale), int(img.size[1] * scene.scale)
        self.imgTk = ImageTk.PhotoImage(img.resize(newSize, self.scalingMethod), size = newSize)
        scene.scene.create_image(tuple(map(lambda x: x * scene.scale, (location[0] - center[0], location[1] - center[1]))), image=self.imgTk, anchor=tk.NW)
        

if __name__ == "__main__":
    pass


