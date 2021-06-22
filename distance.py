import sys
filekj = open(sys.argv[1], "r")
max = 0.000000
#find a file with "TICK" in it and finds the max distance
for line in filekj:
    if line.find("TICK") != -1:
        pos = line.find("distance=")
        if pos != -1:
            if max < float(line[pos + 9:line.find(" ", pos)]):
                max = float(line[pos + 9:line.find(" ", pos)])
print(max)

