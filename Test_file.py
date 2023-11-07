import sys
import json


# files given
STOP_FILE = './data/tramstops.json'
LINE_FILE = './data/tramlines.txt'
def build_lines(linefile):
    linedict = {}
    timedict = {}
    with open(linefile, 'r', encoding='utf-8') as file:
        tramlines = file.read().split('\n\n') 
        #print(len(tramlines))
        for line in tramlines:
            line = line.split('\n')
            stops = []
            for i,e in enumerate(line):
                if len(e) == 2 or len(e) == 3:
                    tramNr = e.strip(':')
                    linedict.setdefault(tramNr, stops)
                
                elif e is not None:
                    e = e.split()
                    stopName = ' '.join(e[:-1])
                    time = e[-1].replace(':','')
                    linedict[tramNr].append(stopName)


                    


                
        return linedict

print(build_lines(LINE_FILE))
#build_lines(LINE_FILE)       




