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
        self.currentState = state.State("settings.txt")
        self.currentScene = scene.Scene(self,self.state.background, .75)
        
        #create the five necessary buttons for player choices and hide them
        self.optionButtons = [Button(self, text=currentState.options[i], command=lambda: self.buttonPress(i)) for i in range(5)]
        for button in optionButtons:
            button.lower(self.currentScene.background)
            
        self.nextButton = Button(self, text='Continue', command=self.continueGame)
        self.textBox = 
        
        self.currentScene.pack(side = 'top')
        for button in optionButtons:
            button.pack(side = 'top')
        
        
    def changeButtons(self, optionsList):
        for i,option in enumerate(optionsList):
            if i >= self.currentState.firstGrey:
                self.optionButtons[i].text = option

    #only relevant on say or opts because those are when the player needs time to read and then select continue
    def continueGame(self):
        if 'opt' == self.state.action():
            

        
    def buttonPress(self, num):
        pass
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Screen(master=root)
    app.mainloop()