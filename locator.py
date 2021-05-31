import sys
import datetime
THD_COL = 4
YEAR_COL = 7
MONTH_COL = 8
TIME_COL = 0


def locateFunction(filename, year, month, strike, callPut, time_input):
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
                    colon = y.split(':')
                    value1 = colon[0]
                    value2 = colon[1]
                    value3 = colon[2]
                    value4 = colon[3]
                    value5 = colon[4]
                    value6 = colon[5]
                    value7 = colon[6]
                    value8 = colon[7]
                    value9 = colon[8]
                    value10 = colon[9]
                    value11 = colon[10]
                    value12 = colon[11]
                    value13 = colon[12]
                    value14 = colon[13]
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
                    disect = y.split(':')
                    value1 = disect[0]
                    value2 = disect[1]
                    value3 = disect[2]
                    value4 = disect[3]
                    value5 = disect[4]
                    value6 = disect[5]
                    value7 = disect[6]
                    value8 = disect[7]
                    value9 = disect[8]
                    value10 = disect[9]
                    value11 = disect[10]
                    value12 = disect[11]
                    value13 = disect[12]
                    value14 = disect[13]
                    break
            if found:
                break
    general.close()
    return value2

def main():
    if len(sys.argv) < 6:
        print("Usage: ", sys.argv[0], "Year Month Strike Call/Put Time")
        exit(-1)
    filename = sys.argv[1]
    year = sys.argv[2]
    month = sys.argv[3]
    strike = sys.argv[4]
    callPut = sys.argv[5]
    time_input = sys.argv[6]
    date_time_obj = datetime.datetime.strptime(time_input, '%H:%M:%S')
    answer = locateFunction(filename, year, month, strike, callPut, time_input)
    print(answer)
if __name__ == "__main__":
    main()
