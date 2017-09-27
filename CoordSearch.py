import gzip
import os
import math

outputFile = open("pythonOutput.csv", "w")

LanthAtom = b"C1 "

x_file = gzip.open(os.path.join('M0008', "output.gz"), 'r')
lines = x_file.readlines()
length = len(lines)
obsList = list()
bondList = list()
NeededAtoms = list()

for line in range(length):
    if lines[line].startswith(b"                     Cartesian Coordinates", 0): # ДОБЫВАЕМ НУЖНЫЕ КУСКИ OUTPUT'А
        i = line + 4
        while len(lines[i]) > 30:
            obsList.append(lines[i])
            i = i + 1
    if lines[line].startswith(b" Bond Orders              Mulliken", 0):
        j = line + 1
        while len(lines[j]) > 30:
            bondList.append(lines[j])
            j = j + 1


datList = list()                                                                 # НАХОДИМ ДЕКАРТОВЫЕ КООРДИНАТЫ АТОМА ЛАНТАНИДА
for line in bondList:
    if line.count(LanthAtom) > 0:
        datList.append(str(line.decode().split(" ")[11]))

lanthCoordList = list()
lanthCoord = str()
for line in obsList:
    if line.count(LanthAtom) > 0:
        lanthCoordList = line.decode().split(" ")
        print(lanthCoordList)
        lanthCoord = lanthCoordList[16] + " " + lanthCoordList[21] + " " +  lanthCoordList[25]
        print(lanthCoord)


lanthDekCoord = lanthCoord.split(" ")
print(lanthDekCoord)

atomCoord = [[0] * 3 for i in range(6)]             # i(0,4) j(0,2)

for i in range(3):
    atomCoord[0][i] = lanthDekCoord[i]

j = 0
print(datList)
for i in datList:
    for line in obsList:
        trashList = line.decode().split(" ")
        if trashList[5] == i:
            coordList = line.decode().split(" ")
            print(coordList)

            atomCoord[1 + j][0] = coordList[16]
            atomCoord[1 + j][1] = coordList[21]
            atomCoord[1 + j][2] = coordList[25]
            j = j + 1
        else:
            if trashList[4] == i:
                coordList = line.decode().split(" ")
                print(coordList)
                atomCoord[1 + j][0] = coordList[14]
                atomCoord[1 + j][1] = coordList[18]
                atomCoord[1 + j][2] = coordList[23]
                j = j + 1

            else:
                if trashList[3] == i:
                    coordList = line.decode().split(" ")
                    atomCoord[1 + j][0] = coordList[16]
                    atomCoord[1 + j][1] = coordList[18]
                    atomCoord[1 + j][2] = coordList[23]
                    j = j + 1

print(atomCoord)

coordDistList = list()
for i in range(len(atomCoord) - 1):
    coordDistList.append(math.sqrt((float(atomCoord[0][0]) - float(atomCoord[1 + i][0]))**2 + (float(atomCoord[0][1]) - float(atomCoord[1 + i][1]))**2 + (float(atomCoord[0][2]) - float(atomCoord[1 + i][2])**2)))
    print(coordDistList)

for i in coordDistList:
    outputFile.write(str(i) + "\n")



