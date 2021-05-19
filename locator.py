import sys

THD_COL = 4
YEAR_COL = 7
MONTH_COL = 8



def locateFunction(year, month, strike, callPut):
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
            result = x.find("C:3230:")
            for y in cutter:
                if y[0:7] == "C:" + strike + ":":
                    answer = y
                    found = True
                    break
            if found:
                break
    elif callPut == "put":
        found = False
        for x in thd_Arr:
            split = x.split('|')
            for y in split:
                if y[0:6] == "P:" + strike + ":":
                    answer = y
                    found = True
                    break
            if found:
                break
    general.close()
    return answer

def main():
    if len(sys.argv) < 5:
        print("Usage: ", sys.argv[0], "Year Month Strike Call/Put")
        exit(-1)
    year = sys.argv[1]
    month = sys.argv[2]
    strike = sys.argv[3]
    callPut = sys.argv[4]
    answer = locateFunction(year, month, strike, callPut)
    print(answer)
if __name__ == "__main__":
    main()
