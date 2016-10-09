from story import Story

'''
State is the hidden variables that keep track of things
'''

class State:
    def __init__(self, filename):
        keys = ['storyFile', 'dataFile']
        
        with open(filename, 'r') as f:
            for line in f:
                key, value = line.split(maxsplit=1)
                if key in keys:
                    setattr(self, key.strip(), value.strip())
        
        self.story = Story(self.storyFile)
        self.background = self.story.startBackground
        self.speaker = ''
        self.text = ''
        self.options = []
        
    def action(self, actionNumber):
        for data in self.story[actionNumber]:
            pass
        
    def next(self):
        pass
    
    

if __name__ == '__main__':
    pass



