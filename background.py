
import PIL as pil

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
    def __init__(self, master = None, filename = None):
        tk.Frame.__init__(self, master)
        with open(file, 'r') as f:
            self.img = f.readline()
            self.numLocs = int(f.readline())
            for i in range(self.numLocs):
                x, y = f.readline().split()
                self.locs.append((int(x), int(y)))
            
            