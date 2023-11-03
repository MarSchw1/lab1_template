import sys
import json


# files given
STOP_FILE = './data/tramstops.json'
LINE_FILE = './data/tramlines.txt'

# file to give
TRAM_FILE = './tramnetwork.json'

def build_tram_stops(jsonobject):
    dict_position = {}
    with open(jsonobject, 'r') as infile:
        stop_data = json.load(infile)
        for station in stop_data:
            lat, long = stop_data.get(station).get('position')
            dict_position[station] = {"lat": lat, "long": long}
        return dict_position
#print(build_tram_stops(STOP_FILE))

def build_tram_lines(lines):
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

    tram_lines = {}
    with open(lines, 'r') as file:
        opened_file = file.readlines()
        A = True
        while A:
            for lines in opened_file:
                stops = []
                if lines[0].isdigit():
                    tramline = lines.strip('\n').replace(":","")
                    tram_lines.setdefault(tramline,stops)
                '''if lines[0].isdigit() or lines[0:1].isdigit():
                    lines = lines.strip("\n")
                    lines = lines.replace(":", "")
                    if len(lines) == 1:
                        tramline = str(lines[0])
                    elif len(lines) == 2:
                        tramline = str(lines[0:2])
                    tram_lines.setdefault(tramline, stops)'''
                if lines[0].isalpha():
                    lines = lines.strip('\n').split()
                    name = lines[:-1]
                    if len(name) == 2:
                        name = " ".join(name)
                    else: name = name[0]
                    tram_lines[tramline].append(name)
                if lines[0] in ['\n', ' ']:
                    A = False
        return tram_lines
print(build_tram_lines(LINE_FILE))


def build_tram_network(stopfile, linefile):
    ## YOUR CODE HERE
    pass

def lines_via_stop(linedict, stop):
    ## YOUR CODE HERE
    pass

def lines_between_stops(linedict, stop1, stop2):
    ## YOUR CODE HERE
    pass

def time_between_stops(linedict, timedict, line, stop1, stop2):
    ## YOUR CODE HERE
    pass

def distance_between_stops(stopdict, stop1, stop2):
    ## YOUR CODE HERE
    pass

def answer_query(tramdict, query):
    ## YOUR CODE HERE
    pass

def dialogue(tramfile=TRAM_FILE):
    ## YOUR CODE HERE
    pass

if __name__ == '__main__':
    if sys.argv[1:] == ['init']:
        build_tram_network(STOP_FILE,LINE_FILE)
    else:
        dialogue()