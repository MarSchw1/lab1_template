import sys
import json


# files given
STOP_FILE = './data/tramstops.json'
LINE_FILE = './data/tramlines.txt'

def build_tram_lines(lines):
    tram_lines = {}
    with open(lines) as f:
        opened_file = f.readlines()
        for line in opened_file:
            line = line.strip('\n')
        while line != ' ':
            stops = []
            if line[0].isdigit():
                number = line.replace(':','')
            if line[0].isalpha():
                lines = lines.strip('\n').split()
                name = lines[:-1]
                if len(name) == 2:
                    name = " ".join(name)
                else: name = name[0]
                stops.append(name)
            tram_lines.setdefault(number,stops)
        return tram_lines
print(build_tram_lines(LINE_FILE))

# Detta är ett äldre försök som inte fungerar som det ska. Vissa delar gör dock det.
'''tram_lines = {}
    
    with open(lines) as file:
        opened_file = file.readlines()
        while opened_file != '\n':
            stops = []
            for i in opened_file:
                if i[0].isdigit():
                    tramline = i.strip('\n').replace(":","")
                if i[0].isalpha():
                    i = i.strip('\n').split()
                    name = i[:-1]
                    if len(name) == 2:
                        name = " ".join(name)
                    else: name = name[0]
                    stops.append(name)
            tram_lines.setdefault(tramline,stops)
        return tram_lines'''




