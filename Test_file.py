import sys
import json


# files given
STOP_FILE = './data/tramstops.json'
LINE_FILE = './data/tramlines.txt'

def build_tram_lines(lines):
    linedict = {}
    timedict = {}
    temp_timedict = {}
    stops = []
    with open(lines, 'r',encoding="utf-8") as file:
        opened_file = file.readlines()
        A = True
        for i in range(len(opened_file)):
            while A:
                stops = []
                times = {}
                if i[0].isdigit():
                    tramline = i.strip('\n').replace(":","")
                    linedict.setdefault(tramline,stops)
                if i[0].isalpha():
                    i = i.strip('\n').split()
                    name = i[:-1]
                    time = i[-1]
                    if len(name) != 1:
                        name = " ".join(name)
                    else: name = name[0]
                    linedict[tramline].append(name)
                    temp_timedict[tramline].setdefault(name,time)
                if i[0] in ['\n', ' ']:
                    A = False
                '''for tramline in temp_timedict:
                    stops = list(temp_timedict[tramline].keys())
                for i in range(len(stops)-1):
                    current_stop = stops[i]
                    next_stop = stops[i+1]
                    current_time = int(temp_timedict[tramline][current_stop].replace(':',''))
                    next_time = int(temp_timedict[tramline][next_stop].replace(':',''))
                    diff_time = next_time - current_time 
                    diff_dict = {}
                    timedict.setdefault(current_stop,diff_dict)
                    timedict[current_stop].setdefault(next_stop,diff_time)'''

    return linedict, timedict
print(build_tram_lines(LINE_FILE))
#build_tram_lines(LINE_FILE)


