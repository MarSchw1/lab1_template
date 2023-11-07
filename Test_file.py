import sys
import json


# files given
STOP_FILE = './data/tramstops.json'
LINE_FILE = './data/tramlines.txt'
'''def build_lines(linefile):
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
                    linedict[tramNr].append(stopName)'''
def build_tram_lines(lines):
    line_dict = {}
    time_dict = {}
    with open(lines, 'r',encoding="utf-8") as file:
        opened_file = file.readlines()
        A = True
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
                        name = " ".join(stop_name)
                    else: stop_name = stop_name[0]
                    line_dict[tramline].append(stop_name)

                    prev_station = False
                    time = int((lines[-1]).replace(':',''))
                    if prev_station not in time_dict[prev_station] and prev_station:
                        time_diff = time - prev_time
                        time_dict.setdefault(prev_station,{}).setdefault(stop_name, time_diff)
                    prev_station, prev_time = stop_name, time

                if lines[0] in ['\n', ' ']:
                    A = False
                         
        return time_dict

print(build_tram_lines(LINE_FILE))
#build_lines(LINE_FILE)       




