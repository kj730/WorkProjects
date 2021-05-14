import os
import time
import sys
THD_COL = 4
YEAR_COL = 7
MONTH_COL = 8
thd_Arr = []
def locateFunction(year, month, strike, callPut):
    try:
        general = open("FBQNGM1.General.20210503.log", "r")
    except OSError as err:
        print("Unable to open General File. OS error: {0}".format(err))
        return -1
    except:
        print("Unable to open General File")
        return -1
    for line in general:
        split = line.split('|')
        thdStr = split[THD_COL]
        if thdStr == "THD":
            thd_Arr.append(line)
    for x in thd_Arr:
        splitter = x.split('|')
        yearStr = splitter[YEAR_COL]
        monthStr = splitter[MONTH_COL]
    thd_Arr.reverse()
    if callPut == "call":
        for x in thd_Arr:
            cutter = x.split('|')
            for y in cutter:
               if y[0:6] == "C:" + strike:
                   print(y)
    elif callPut == "put":
        for x in thd_Arr:
            split = x.split('|')
            for y in split:
               if y[0:6] == "P:" + strike:
                   print(y)
    general.close()
def main():
    if len(sys.argv) < 5:
        print("Usage: ", sys.argv[0], "Year Month Strike Call/Put")
        exit(-1)
    year = sys.argv[1]
    month = sys.argv[2]
    strike = sys.argv[3]
    callPut = sys.argv[4]
    answer = locateFunction(year, month, strike, callPut)
    exit(answer)