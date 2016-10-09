import tkinter as tk
from PIL import ImageTk

'''
Scene is the top half of the window that shows the background and has slots to place chacters.
'''


class Scene(tk.Frame):
    def __init__(self, master = None, initBackground = None, scale=0.5):
        tk.Frame.__init__(self, master)
        self.scale = scale
        self.scene = tk.Canvas(self, width=self.scale*1920, height=self.scale*1080)
        self.scene.pack(fill=tk.BOTH, expand=tk.YES)
        self.background = initBackground
        self.scene.pack(side=tk.TOP)
        self.characters = [(None, 0)] * len(self.background)
        self.draw()
    
    def changeBackground(self, newBackground, draw = True):
        '''
        Takes a background image and replaces the current background
        '''
        self.background = newBackground
        self.characters = [(None, 0)] * len(self.background)
        if draw: 
            self.draw()
    
    def changeCharacter(self, newCharacter = None, location = 0, imgNum = 0, draw = True):
        '''
        Takes a person and puts them in the scene at the specified location
        '''
        self.characters[location] = (newCharacter, imgNum)
        if draw:
            self.draw()
    
    def draw(self):
        self.background.draw(self)
        for location, character in enumerate(self.characters):
            if character[0] is not None:
                character[0].draw(self, self.background[location], character[1])
        
        
        
if __name__ == "__main__":
    import os
    
    from background import Background
    from character import Character
    
    root = tk.Tk()
    bg = Background(os.path.join('assets', 'Pumpkin patch-night.data'))
    char = Character(os.path.join('assets', 'tmpC1.data.txt'))
    
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.pack()
            self.create_widgets()
    
        def create_widgets(self):
            self.hi_there = Scene(self, bg, scale=0.5)
            self.hi_there.changeCharacter(char, 1)
            self.hi_there.pack(side="top")
            
            self.hidden = False
            self.hide = tk.Button(self, text="HIDE", fg="red", command=self.hide)
            self.hide.pack(side="bottom")            
            
            self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
            self.quit.pack(side="bottom")
    
        def hide(self):
            if not self.hidden:
                self.hidden = True
                self.hi_there.changeCharacter(None, 1)
            else:
                self.hidden = False
                self.hi_there.changeCharacter(char, 1)
                
            
        

    app = Application(master=root)
    app.mainloop()

