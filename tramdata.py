import sys
import json


# files given
STOP_FILE = './data/tramstops.json'
LINE_FILE = './data/tramlines.txt'

# file to give
TRAM_FILE = './tramnetwork.json'

def build_tram_stops(jsonobject):
    ## YOUR CODE HERE
    pass

def build_tram_lines(lines):
    tram_lines = {}
    
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