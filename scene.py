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
        self.characters = []
        self.draw()
    
    def changeBackground(self, newBackground):
        '''
        Takes a background image and replaces the current background
        '''
        self.background = newBackground
        self.characters = []
    
    def changeCharacter(self, newCharacter = None, location = 0):
        '''
        Takes a person and puts them in the scene at the specified location
        '''
        self.characters[location] = newCharacter
        self.draw()
    
    def draw(self):
        self.background.draw(self)
        for location, character in self.characters:
            if character is not None:
                character.draw(self.scene, self.background[location])
        
        
        
if __name__ == "__main__":
    import os
    
    from background import Background
    from character import Character
    
    root = tk.Tk()
    bg = Background(os.path.join('assets', 'tmpBG1.data.txt'))
    char = Character(os.path.join('assets', 'tmpC1.data.txt'))
    
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.pack()
            self.create_widgets()
    
        def create_widgets(self):
            self.hi_there = Scene(self, bg, scale=0.5)
            self.hi_there.pack(side="top")
    
            self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
            self.quit.pack(side="bottom")
    
        def say_hi(self):
            print("hi there, everyone!")

    app = Application(master=root)
    app.mainloop()

