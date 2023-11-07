import sys
import json


# files given
STOP_FILE = './data/tramstops.json'
LINE_FILE = './data/tramlines.txt'

# file to give
TRAM_FILE = './tramnetwork.json'

def build_tram_stops(jsonobject):
    stopdict = {}
    with open(jsonobject, 'r') as infile:
        stop_data = json.load(infile)
        for station in stop_data:
            lat, long = stop_data.get(station).get('position')
            stopdict[station] = {"lat": lat, "long": long}
        return stopdict
#print(build_tram_stops(STOP_FILE))

def build_tram_lines(lines):
    line_dict = {}
    time_dict = {}
    with open(lines, 'r',encoding="utf-8") as file:
        opened_file = file.readlines()
        A = True
        prev_station = None
        prev_time = None
        while A:
            for lines in opened_file:
                stops = []
                times = {}
                if lines[0].isdigit():
                    tramline = lines.strip('\n').replace(":","")
                    line_dict.setdefault(tramline,stops)
                if lines[0].isalpha():
                    lines = lines.strip('\n').split()
                    stop_name = lines[:-1]
                    if len(stop_name) != 1:
                        stop_name = " ".join(stop_name)
                    else: stop_name = stop_name[0]
                    line_dict[tramline].append(stop_name)

                    
                    time = int((lines[-1]).replace(':',''))
                    if prev_station is not None:
                        if prev_station not in time_dict.get(prev_station, {}) and prev_station:
                            time_diff = time - prev_time
                            time_dict.setdefault(prev_station,{}).setdefault(stop_name, time_diff)
                        prev_station, prev_time = stop_name, time
                    if prev_station is None:
                        prev_station, prev_time = stop_name, time
                if lines[0] in ['\n', ' ']:
                    A = False
                         
        return line_dict,time_dict

#print(build_tram_lines(LINE_FILE))
#build_tram_lines(LINE_FILE)

def build_tram_network(stopfile, linefile):
    stops = build_tram_stops(STOP_FILE)
    lines, times = build_tram_lines(LINE_FILE)

    data = {"stops": stops, "lines":lines, "times":times}

    with open("tramnetwork.json" , 'w') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

    
build_tram_network(STOP_FILE,LINE_FILE)

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