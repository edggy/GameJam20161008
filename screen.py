import tkinter as tk
import tkinter.ttk as ttk

import state
import scene
import copy
'''
Screen is the entire window
Has scene on top, options on bottom
'''

class Screen(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.currentState = state.State("settings.txt")
        self.currentScene = scene.Scene(self, self.currentState.background, .5)
        
        #text variables
        self.btnTextVars = [tk.StringVar() for i in range(5)]
        self.contBtnTxt = tk.StringVar()
        self.contBtnTxt.set('Start'.center(20, ' '))
        self.display = tk.StringVar()
        self.display.set("")
        
        #create the five necessary buttons for player choices and place them in buttonContainer
        self.buttonContainer = tk.Frame(self, background = "", height = 400, width=self.currentScene.scene.winfo_width() - 200)
        self.optionButtons = []            
        self.optionButtons.append(ttk.Button(self.buttonContainer, width = 100, textvariable = self.btnTextVars[0], command=lambda: self.buttonPress(0)))
        self.optionButtons.append(ttk.Button(self.buttonContainer, width = 100, textvariable = self.btnTextVars[1], command=lambda: self.buttonPress(1)))
        self.optionButtons.append(ttk.Button(self.buttonContainer, width = 100, textvariable = self.btnTextVars[2], command=lambda: self.buttonPress(2)))
        self.optionButtons.append(ttk.Button(self.buttonContainer, width = 100, textvariable = self.btnTextVars[3], command=lambda: self.buttonPress(3)))
        self.optionButtons.append(ttk.Button(self.buttonContainer, width = 100, textvariable = self.btnTextVars[4], command=lambda: self.buttonPress(4)))
            
        self.nextButton = ttk.Button(self, textvariable = self.contBtnTxt, command=self.continueGame)
        self.displayedText = tk.Label(self, textvariable = self.display)
        
        self.currentScene.pack(side = 'top')
        for button in self.optionButtons:
            button.disabledforeground = 'grey'            
            button.pack(side = 'top')
            
            
        self.buttonContainer.place(x = self.currentScene.scale*500, y = self.currentScene.scale*800)
        self.buttonContainer.lower()
        
        self.nextButton.place(x = self.currentScene.scale*1600, y = self.currentScene.scale*1000)
        self.nextButton.lift()
        self.nextButton.state(['!disabled'])
        
        self.displayedText.place(x = self.currentScene.scale*500, y=self.currentScene.scale*700)
        self.displayedText.lower()
        
    #called when an option select shows up
    def changeButtons(self, optionsList):
        for i,option in enumerate(optionsList):
            if i <= self.currentState.firstGrey:
                self.btnTextVars[i].set(option)
            else:
                self.btnTextVars[i].set(option)
                self.optionButtons[i].state(['disabled'])
                
        leftover = len(self.optionButtons) - len(optionsList)
        for x in range(leftover):
            self.optionButtons[len(optionsList)+x].lower()
            self.optionButtons[len(optionsList)+x].state(['disabled'])

    #only relevant on say or opts because those are when the player needs time to read and then select continue
    #called every time an action should step forward
    def continueGame(self):
        self.contBtnTxt.set("Continue")
        #call the next action and check what it is; call operations to match
        while True:
            actionName, keys = self.currentState.action()
            if actionName == 'opts':
                self.buttonContainer.lift()
                for button in self.optionButtons:
                    button.state(['!disabled'])
                    self.nextButton.state(['disabled'])
                    self.nextButton.lower()
                    
                self.changeButtons(self.currentState.options)
                break
            elif actionName == 'say':
                self.display.set(self.currentState.speaker + ':    ' + self.currentState.text)
                self.displayedText.lift()
                self.buttonContainer.lower()
                break
            elif actionName == 'loadB':
                self.currentScene.changeBackground(*keys)
            elif actionName == 'loadC':
                self.currentScene.changeCharacter(*keys)
        
        
    #method for option buttons
    def buttonPress(self, num):
        self.currentState.action(num)
        for button in self.optionButtons:
            button.state(['disabled'])
            button.lower()
            
        self.nextButton.state(['!disabled'])
        self.nextButton.lift()
        self.continueGame()
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = Screen(master=root)
    app.mainloop()