import os
from PIL import Image
from PIL import ImageTk
import tkinter as tk

'''
Background class hold the image of the background and the data such as character locations

Background file format:
<img location>
<number of character positions>
<pos 1 x> <pos 1 y>
<pos 2 x> <pos 2 y>
...
<pos n x> <pos n y>
'''



class Background():
    def __init__(self, filename):
        cwd = os.path.dirname(filename)
        with open(filename, 'r') as f:
            self.imgName = os.path.join(cwd, f.readline().strip())
            self.numLocs = int(f.readline())
            self.locs = []
            for i in range(self.numLocs):
                x, y = f.readline().split()
                self.locs.append((int(x), int(y)))
        self.img = Image.open(self.imgName)
        #self.imgTk = ImageTk.PhotoImage(self.img)
                
    def __getitem__(self, index):
        return self.locs[index]
    
    def draw(self, scene):
        #newSize = scene.scene.winfo_reqwidth(), scene.scene.winfo_reqheight()
        newSize = int(self.img.size[0] * scene.scale), int(self.img.size[1] * scene.scale)
        self.imgTk = ImageTk.PhotoImage(self.img.resize(newSize), size = newSize)        
        scene.scene.create_image((0,0), image=self.imgTk, anchor=tk.NW)
        

