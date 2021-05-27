import sys
import datetime
THD_COL = 4
YEAR_COL = 7
MONTH_COL = 8
TIME_COL = 0

#THIS IS A COMMENT

def locateFunction(year, month, strike, callPut, time_input):
    answer = ""
    thd_Arr = []
    try:
        general = open("FBQNGM1.General.20210503.log", "r")
    except OSError as err:
        print("Unable to open General File. OS error: {0}".format(err))
        return -1
    except:
        print("Unable to open General File")
        return -1
    for line in general:
        splitter = line.split('|')
        if len(splitter) < THD_COL + 1:
            continue
        thdStr = splitter[THD_COL]
        if thdStr == " THD ":
            thd_Arr.append(line)
    for x in thd_Arr:
        seperate = x.split('|')
        yearStr = seperate[YEAR_COL]
        monthStr = seperate[MONTH_COL]
    thd_Arr.reverse()
    if callPut == "call":
        found = False
        for x in thd_Arr:
            cutter = x.split('|')
            if time_input < cutter[TIME_COL]:
                continue
            for y in cutter:
                found = y.startswith("C:" + strike + ":")
                if found:
                    answer = y
                    break
            if found:
                break
    elif callPut == "put":
        found = False
        for x in thd_Arr:
            split = x.split('|')
            if time_input < split[TIME_COL]:
                continue
            for y in split:
                found = y.startswith("P:" + strike + ":")
                if found:
                    answer = y
                    break
            if found:
                break
    general.close()
    return answer

def main():
    if len(sys.argv) < 6:
        print("Usage: ", sys.argv[0], "Year Month Strike Call/Put Time")
        exit(-1)
    year = sys.argv[1]
    month = sys.argv[2]
    strike = sys.argv[3]
    callPut = sys.argv[4]
    time_input = sys.argv[5]
    date_time_obj = datetime.datetime.strptime(time_input, '%H:%M:%S')
    answer = locateFunction(year, month, strike, callPut, time_input)
    print(answer)
if __name__ == "__main__":
    
