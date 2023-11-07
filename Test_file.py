import sys
import json


# files given
STOP_FILE = './data/tramstops.json'
LINE_FILE = './data/tramlines.txt'
def build_lines(linefile):
    linedict = {}
    timedict = {}
    with open(linefile, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n') 
        print(lines)


build_lines(LINE_FILE)
        




