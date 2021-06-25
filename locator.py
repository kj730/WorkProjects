import sys
import datetime
THD_COL = 4
YEAR_COL = 7
MONTH_COL = 8
TIME_COL = 0

OUTPUT_KIND_IDX=0
OUTPUT_STK_IDX=1


#finds the value of a strike at a given time
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
        #check to see if we are using the right line in the file
        if len(splitter) < THD_COL + 1:
            continue
        thdStr = splitter[THD_COL]
        if thdStr == " THD ":
            thd_Arr.append(line)
    for x in thd_Arr:
        seperate = x.split('|')
        yearStr = seperate[YEAR_COL]
        monthStr = seperate[MONTH_COL]
    #reverse the array so that we can find the most recent strike
    thd_Arr.reverse()
    if callPut == "C":
        found = False
        for x in thd_Arr:
            cutter = x.split('|')
            #makes sure that that the time in the file is before the time argument
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
            #makes sure that that the time in the file is before the time argument
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
#formarts the data to see each value in an easier way
def format_output(data):
    arr = data.split(':')
    if(len(data) == 0):
        print("Data not found for year = ", sys.argv[2], " month = ", sys.argv[3], " strike = ", sys.argv[4], " Call/Put = ", sys.argv[5], "time = ", sys.argv[6])
    else:
        print("Kind =" + arr[OUTPUT_KIND_IDX])
        print("Strike =" + arr[OUTPUT_STK_IDX])
        print("Value3 =" + arr[2])
        print("BidIn =" + arr[3])
        print("BidOut =" + arr[4])
        print("BidQty =" + arr[5])
        print("On/Off =" + arr[6])
        print("AskIn =" + arr[7])
        print("AskOut =" + arr[8])
        print("AskQty =" + arr[9])
        print("Value11=" + arr[10])
        print("Value12=" + arr[11])
        print("Value13=" + arr[12])
        print("Value14=" + arr[13])

def main():
    if len(sys.argv) < 6:
        print("Usage: ", sys.argv[0], "Filename Year Month Strike Call/Put(C or P) Time")
        exit(-1)
    filename = sys.argv[1]
    year = sys.argv[2]
    month = sys.argv[3]
    strike = sys.argv[4]
    callPut = sys.argv[5]
    time_input = sys.argv[6]
    #make a time object from the time argument
    date_time_obj = datetime.datetime.strptime(time_input, '%H:%M:%S')
    answer = locateFunction(filename, year, month, strike, callPut, time_input)
    print("Answer is " + answer)
    if len(answer) > 3:
        print("Time: ", date_time_obj)
        format_output(answer)
    else:
        print("data not found")
if __name__ == "__main__":
    main()
