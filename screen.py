import tkinter as tk

import state
import scene
'''
Screen is the entire window
Has scene on top, options on bottom
'''

class Screen(tk.Frame):
    def __init__(self, master = None, initBackground = None):
        tk.Frame.__init__(self, master)
        self.state = state.State("settings.txt")
        self.scene = scene.Scene(self,self.state.background, .75)
        self.buttons = [Button(self, text=state.options[i], command=lambda: self.state.action(i)) for i in range(5)]
        #self.button0 = Button(self, text=state.options[0], command=lambda: self.state.action(0))
        #
        
        self.scene.pack(side = 'top')
        for button in buttons:
            button.pack(side = 'top')
        
    def changeButtons():
        
        pass



if __name__ == "__main__":
    root = tk.Tk()
    app = Screen(master=root)
    app.mainloop()