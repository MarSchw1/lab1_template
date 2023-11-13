import sys
import json
import math


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

def build_tram_lines(FILE):
    line_dict = {}
    time_dict = {}
    with open(FILE, 'r',encoding="utf-8") as file:
        opened_file = file.readlines()
        for line in opened_file:
            stops = []
            if line[0].isdigit():
                tramline = line.strip('\n').replace(":","")
                line_dict.setdefault(tramline,stops)
                prev_station = None
            if line[0].isalpha():
                line = line.strip('\n').split()
                stop_name = line[:-1]
                if len(stop_name) != 1:
                    stop_name = " ".join(stop_name)
                else: stop_name = stop_name[0]
                line_dict[tramline].append(stop_name)
                
                time = int((line[-1]).replace(':',''))
                #if prev_station == None:
                    #prev_station, prev_time = stop_name, time

                if stop_name not in time_dict.get(prev_station, {}) and prev_station not in time_dict.get(stop_name, {}):
                    time_diff = time - prev_time
                    if time_diff >= 0:
                        time_dict.setdefault(prev_station,{}).setdefault(stop_name, time_diff)
                prev_station, prev_time = stop_name, time 

                         
        return line_dict, time_dict

#print(build_tram_lines(LINE_FILE))
#build_tram_lines(LINE_FILE)

def build_tram_network(stopfile, linefile):
    stops = build_tram_stops(STOP_FILE)
    line, times = build_tram_lines(LINE_FILE)

    data = {"stops": stops, "line":line, "times":times}

    with open("tramnetwork.json" , 'w',encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)
    #bprint('Done')

    
#build_tram_network(STOP_FILE,LINE_FILE)

def lines_via_stop(line_dict, stop): # (linedict, stop)
    stops = []
    for line in line_dict:
        if stop in line_dict.get(line):
            stops.append(line)
    if len(stops) == 0:
        return False
    else: return stops

'''with open('./tramnetwork.json',encoding='utf-8') as file:
        data = json.load(file)'''
def lines_between_stops(line_dict,stop1, stop2): #(linedict, stop1, stop2)
    stops = []
    for line in line_dict:
        if stop1 in line_dict.get(line) and stop2 in line_dict.get(line):
            stops.append(line)
    if len(stops) == 0:
        return False
    else: return stops
#lines_between_stops(data['line'],"Lackarebäck","Korsvägen")


def time_between_stops(linedict, timedict, line, stop1, stop2):
    if line in linedict:
        if stop1 in linedict[line] and stop2 in linedict[line]:
            stops = linedict[line]
            index1, index2 = stops.index(stop1), stops.index(stop2)
            route = stops[min(index1,index2):max(index1,index2) +1]
            time = 0
            for i in range(len(route)-1):
                if route[i+1] not in timedict[route[i]]: 
                    time += timedict[route[i+1]][route[i]]
                else:
                    time += timedict[route[i]][route[i+1]]
            return time
        else: return False
    else: return False
#print(time_between_stops("1", "Östra Sjukhuset", "Härlanda"))

def distance_between_stops(stopdict, stop1, stop2):
    if stop1 in stopdict and stop2 in stopdict:
        R = 6371.009
        lat1, long1 = float(stopdict[stop1]["lat"]),float(stopdict[stop1]["long"])
        lat2, long2 = float(stopdict[stop2]["lat"]),float(stopdict[stop2]["long"])
        diff_lat, diff_long = ((lat1) - (lat2))*(math.pi/180), ((long1) - (long2))*(math.pi/180)
        lat_mean = ((lat1 + lat2) / 2)*(math.pi/180)
        D = R * math.sqrt(diff_lat**2 + (math.cos(lat_mean)*diff_long)**2)
        return round(D,3)
    else: return False

#print(distance_between_stops(build_tram_stops(STOP_FILE), "Rymdtorget Spårvagn", "Hagakyrkan"))


def answer_query(tramdict, query):
    question = query.strip().split()
    if question[0] == 'via':
        stop = ' '.join(question[1:])
        answer = lines_via_stop(tramdict['line'], stop)
    
    elif question[0] == 'between':
        pos_and = question.index('and')
        stop1,stop2 = ' '.join(question[1:pos_and]), ' '.join(question[pos_and+1:])
        answer = lines_between_stops(tramdict['line'],stop1,stop2)

    elif question[0] == 'time':
        line = question[2]
        pos_to, pos_from = question.index('to'),question.index('from')
        stop1, stop2 = ' '.join(question[pos_from +1 :pos_to]), ' '.join(question[pos_to +1:])
        answer = time_between_stops(tramdict['line'],tramdict['times'],line, stop1, stop2)
        
    elif question[0] == 'distance':
        pos_to, pos_from = question.index('to'),question.index('from')
        stop1, stop2 = ' '.join(question[pos_from+1:pos_to]), ' '.join(question[pos_to+1:])
        answer = distance_between_stops(tramdict['stops'],stop1,stop2)

    else: answer = None

    return answer
        

def dialogue(tramfile=TRAM_FILE):
    with open(tramfile,encoding='utf-8') as file:
        data = json.load(file)
    while True:
        prompt = input('>')
        if prompt == 'quit': break
        answer = answer_query(data, prompt)
        if answer == None:
            print('sorry, try again')
        elif answer == False:
            print('unknown argument')
        else:
            print(answer)
            break


if __name__ == '__main__':
    if sys.argv[1:] == ['init']:
        build_tram_network(STOP_FILE,LINE_FILE)
    else:
        dialogue()

