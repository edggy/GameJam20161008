
from character import Character
from background import Background

class Story:
    def __init__(self, filename):
        
        commands = {'assign': self.assign, 'scene': self.scene, 'load': self.load, 'say': self.say, 'options': self.options, 'add':self.add, 'sub':self.sub}
        
        self.startScene = None
        self.startBackground = None
        self.curScene = ''
        self.storyScenes = {}
        self.characters = {'None':None}
        self.backgrounds = {}        

        self.state = None
        
        with open(filename, 'r') as f:
            self.f = f
            done = False
            while not done:
                line = f.readline().strip()
                line = line.split('#', maxsplit=1)[0]
                if line.strip() == '':
                    continue
                
                if self.state is None:
                    command, data = line.split(maxsplit=1)
                    commands[command](data)
                elif self.state == 'options':
                    optionList = []
                    for i in range(numLines):
                        optionList.append(self.parseOptionLine(self.f.readline().strip()))
                    self.storyScenes[self.curScene].append(('opts', optionList))                    
                
                
    def assign(self, data):
        command, name, filename = data.split(maxsplit=2)
        if command == 'character':
            self.characters[name] = Character(filename)
        elif command == 'background':
            self.backgrounds[name] = Background(filename)
        
    
    def scene(self, data):
        data = data.strip()
        if self.startScene is None:
            self.startScene = data

        self.curScene = data
        self.storyScenes[self.curScene] = []
    
    def load(self, data):
        command, name = data.split(maxsplit=1)
        if command == 'character':
            name, location = name.split(maxsplit=1)
            self.storyScenes[self.curScene].append(('loadC', self.characters[name], int(location)))
        elif command == 'background':
            if self.startBackground is None:
                self.startBackground = self.backgrounds[name]
            self.storyScenes[self.curScene].append(('loadB', self.backgrounds[name]))
        
    
    def say(self, data):
        name, data = data.split(maxsplit=1)
        self.storyScenes[self.curScene].append(('say', name, data))
        
    def add(self, data):
        self.storyScenes[self.curScene].append(('add', data.strip()))
        
    def sub(self, data):
        self.storyScenes[self.curScene].append(('sub', data.strip()))
        
    def options(self, data):
        numLines = int(data.strip())
        self.state = 'options'
            
    def parseOptionLine(self, line):
        parts = [i for i in filter(None, line.split('\t'))]
    
    def __getitem__(self, key):
        for line in self.storyScenes[key]:
            yield line
    
        
if __name__ == '__main__':
    s = Story('story.txt')
    for line in s['0']:
        print(line)