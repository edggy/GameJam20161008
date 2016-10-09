import re

from story import Story

'''
State is the hidden variables that keep track of things
'''

class State:
    def __init__(self, filename):
        keys = ['storyFile', 'dataFile']
        
        with open(filename, 'r') as f:
            for line in f:
                line = line.split('#', maxsplit=1)[0]
                if line.strip() == '':
                    continue                
                key, value = line.split(maxsplit=1)
                if key in keys:
                    setattr(self, key.strip(), value.strip())
        
        self.story = Story(self.storyFile)
        self.background = self.story.startBackground
        self.speaker = ''
        self.text = ''
        self.options = []
        self.optionResults = {}
        self.firstGrey = 0
        self.data = {}
        
        self.curScene = self.story[self.story.startScene]
        
    def action(self, actionNumber = None):
        if actionNumber is not None:
            self.curScene = self.story[self.optionResults[actionNumber]]
            
        while True:
            act = next(self.curScene)
            if act[0] == 'loadB':
                self.background = act[1]
                return (act[0], (act[1],))
            elif act[0] == 'loadC':
                return (act[0], (act[1],act[2]))
            elif act[0] == 'res':
                self.data[act[1]] = 0           
            elif act[0] == 'add':
                try:
                    self.data[act[1]] += 1
                except KeyError:
                    self.data[act[1]] = 1
            elif act[0] == 'sub':
                try:
                    self.data[act[1]] -= 1
                except KeyError:
                    self.data[act[1]] = -1
            elif act[0] == 'say':
                self.speaker = act[1]
                self.text = act[2]
                return act[0]
            elif act[0] == 'opts':
                optList = act[1]
                pattern = re.compile('|'.join(self.data.keys()))
                if len(self.data) > 0:
                    suball = lambda s: pattern.sub(lambda x: str(self.data[x.group()]), s)
                else:
                    suball = lambda s: s
                print([tuple(i) for i in filter(lambda x: eval(suball(x[0])), optList)])
                selectable = [tuple(i) for i in filter(lambda x: eval(suball(x[1])), optList)]
                viewable = [tuple(i) for i in filter(lambda x: eval(suball(x[0])), optList)]
                
                self.firstGrey = 0
                
                self.options = []
                for row in viewable:
                    if row in selectable:
                        self.options.insert(0, row)
                        self.firstGrey += 1
                    else:
                        self.options.append(row)
                        
                for i, row in enumerate(self.options):
                    self.optionResults[i] = row[3]
                    self.options[i] = row[2]
                return act[0]
        
    def next(self):
        pass
    
    

if __name__ == '__main__':
    s = State('settings.txt')
    for i in range(2):
        print(s.action())
    print(s.action(1))
    for i in range(9):
        act = s.action()    
        if act == 'opts':
            print(s.options)


