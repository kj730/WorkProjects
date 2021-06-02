import sys
import datetime
THD_COL = 4
YEAR_COL = 7
MONTH_COL = 8
TIME_COL = 0

OUTPUT_KIND_IDX=0
OUTPUT_STK_IDX=1



def locateFunction(filename, year, month, strike, callPut, time_input):
    answer = ""
    thd_Arr = []
    try:
        general = open(filename, "r")
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
    if callPut == "C":
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
    elif callPut == "P":
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

def format_output(data):
    disect = data.split(':')
    print("Kind=" + disect[OUTPUT_KIND_IDX])
    print("Strike=" + disect[OUTPUT_STK_IDX])
    print("Value3=" + disect[2])
    print("Value4=" + disect[3])
    print("Value5=" + disect[4])
    print("Value6=" + disect[5])
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


def main():
    if len(sys.argv) < 6:
        print("Usage: ", sys.argv[0], "Filename Year Month Strike Call/Put Time")
        exit(-1)
    filename = sys.argv[1]
    year = sys.argv[2]
    month = sys.argv[3]
    strike = sys.argv[4]
    callPut = sys.argv[5]
    time_input = sys.argv[6]
    date_time_obj = datetime.datetime.strptime(time_input, '%H:%M:%S')
    answer = locateFunction(filename, year, month, strike, callPut, time_input)
    print("Answer is " + answer)
    if len(answer) > 3:
        format_output(answer)
    else:
        print("data not found")
if __name__ == "__main__":
    main()
