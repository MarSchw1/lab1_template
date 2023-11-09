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

print(build_tram_lines(LINE_FILE))
#build_lines(LINE_FILE)       

#Denna funktion fick vi inte ha eftersom vi tekniskt sett läser datan 2 gånger när vi skapar temp_timedict.
'''def build_tram_lines(lines):
    linedict = {}
    timedict = {}
    temp_timedict = {}
    with open(lines, 'r',encoding="utf-8") as file:
        opened_file = file.readlines()
        A = True
        while A:
            for lines in opened_file:
                stops = []
                times = {}
                if lines[0].isdigit():
                    tramline = lines.strip('\n').replace(":","")
                    linedict.setdefault(tramline,stops)
                    temp_timedict.setdefault(tramline,times)
                if lines[0].isalpha():
                    lines = lines.strip('\n').split()
                    name = lines[:-1]
                    time = lines[-1]
                    if len(name) != 1:
                        name = " ".join(name)
                    else: name = name[0]
                    linedict[tramline].append(name)
                    temp_timedict[tramline].setdefault(name,time)
                if lines[0] in ['\n', ' ']:
                    A = False
                for tramline in temp_timedict:
                    stops = list(temp_timedict[tramline].keys())
                for i in range(len(stops)-1):
                    current_stop = stops[i]
                    next_stop = stops[i+1]
                    current_time = int(temp_timedict[tramline][current_stop].replace(':',''))
                    next_time = int(temp_timedict[tramline][next_stop].replace(':',''))
                    diff_time = next_time - current_time 
                    diff_dict = {}
                    timedict.setdefault(current_stop,diff_dict)
                    timedict[current_stop].setdefault(next_stop,diff_time)

    return timedict'''


'''   linedict, timedict = build_tram_lines(LINE_FILE)
    if stop1 in linedict[line] and stop2 in linedict[line]:
        total_time = 0
        count_time = False
        prev_stop = None
        for stop in linedict.get(line):
            if stop == stop1:
                count_time = True
                prev_stop = stop
            if stop stop1:
                continue
            while count_time == True:
                time = timedict.get(prev_stop).get(stop)
                total_time += time
        return total_time'''
