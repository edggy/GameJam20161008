
from character import Character
from background import Background

import simpleaudio as sa

class Story:
    def __init__(self, filename):
        
        commands = {'assign': self.assign, 'scene': self.scene, 'load': self.load, 'say': self.say, 
            'options': self.options, 'add':self.add, 'sub':self.sub, 'res':self.res, 'sound':self.sound, 'goto':self.goto}
        
        self.startScene = None
        self.startBackground = None
        self.curScene = ''
        self.storyScenes = {}
        self.characters = {'None':None}
        self.backgrounds = {}
        self.sounds = {}

        self.state = None
        
        with open(filename, 'r') as f:
            for line in f:
                #line = f.readline().strip()
                line = line.split('#', maxsplit=1)[0]
                if line.strip() == '':
                    continue
                
                
                if self.state is not None and self.state['state'] == 'options':
                    if self.state['numLines'] > 0:
                        self.state['optionList'].append(self.parseOptionLine(line))
                        self.state['numLines'] -= 1
                    else:
                        self.storyScenes[self.curScene].append(('opts', self.state['optionList']))
                        self.state = None
                        
                if self.state is None:
                    command, data = map(lambda x: x.strip(), line.split(maxsplit=1))
                    commands[command](data)                        
                
                
    def assign(self, data):
        command, name, filename = map(lambda x: x.strip(), data.split(maxsplit=2))
        if command == 'character':
            self.characters[name] = Character(filename)
        elif command == 'background':
            self.backgrounds[name] = Background(filename)
        elif command == 'sound':
            self.sounds[name] = sa.WaveObject.from_wave_file(filename)
        
    
    def scene(self, data):
        data = data.strip()
        if self.startScene is None:
            self.startScene = data

        self.curScene = data
        self.storyScenes[self.curScene] = []
    
    def load(self, data):
        command, name = map(lambda x: x.strip(), data.split(maxsplit=1))
        if command == 'character':
            name, location, numImg = map(lambda x: x.strip(), name.split(maxsplit=2))
            self.storyScenes[self.curScene].append(('loadC', self.characters[name], int(location), int(numImg)))
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
        
    def res(self, data):
        self.storyScenes[self.curScene].append(('res', data.strip()))
        
    def sound(self, data):
        self.storyScenes[self.curScene].append(('sound', self.sounds[data.strip()]))
        
    def options(self, data):
        numLines = int(data.strip())
        self.state = {'state':'options', 'numLines':numLines, 'optionList':[]}
            
    def parseOptionLine(self, line):
        return [i.strip() for i in filter(None, line.split('\t'))]
    
    def goto(self, data):
        self.storyScenes[self.curScene].append(('goto', data.strip()))
    
    def __getitem__(self, key):
        for line in self.storyScenes[key]:
            yield line
    
        
if __name__ == '__main__':
    s = Story('story.test.txt')
    for line in s['0']:
        print(line)
    print()
    for line in s['1']:
        print(line)    