import unittest
from tramdata import *
from itertools import combinations

TRAM_FILE = './tramnetwork.json'
LINE_FILE = './data/tramlines.txt'

class TestTramData(unittest.TestCase):

    def setUp(self):
        with open(TRAM_FILE, encoding='utf-8') as trams:
            tramdict = json.loads(trams.read())
            self.stopdict = tramdict['stops']
            self.linedict = tramdict['line']

    def test_stops_exist(self):
        stopset = {stop for line in self.linedict for stop in self.linedict[line]}
        for stop in stopset:
            self.assertIn(stop, self.stopdict, msg = stop + ' not in stopdict')

    # add your own tests here
    def test_all_lines_included(self):
        with open(LINE_FILE,'r',encoding='utf-8') as FILE:
            line_list = [line.strip(':\n') for line in FILE.readlines() if line[0].isdigit()] 
        for line in line_list:
            self.assertIn(line, self.linedict.keys(), msg = line + ' not in linedict')
    
    def test_all_stops_included(self):
        with open(LINE_FILE,'r',encoding='utf-8') as FILE:
            pass

    def test_distances_feasible(self):
        all_stops = self.stopdict.keys()
        pairs = combinations(all_stops,2)
        for pair in pairs:
            stop1 , stop2 = pair
            self.assertLess(distance_between_stops(self.stopdict,stop1,stop2), 10, msg = f'(distance betwenne {stop1} and {stop2} is greater then 20km)')


        

if __name__ == '__main__':
    unittest.main()

