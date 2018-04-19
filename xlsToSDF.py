import xlrd
import pandas
import numpy

sdfFile = open("Assym.sdf", "r")
outSdfFile = open("AssymData.sdf", "w")
dataFile = xlrd.open_workbook("AssymBase.xls", on_demand=True)

workSheet = dataFile.sheet_by_name("Лист1")
rawEbindLaList = workSheet.col_values(7)
rawEbindNdList = workSheet.col_values(10)
rawEbindEuList = workSheet.col_values(8)
rawEbindLuList = workSheet.col_values(9)
rawEHomo = workSheet.col_values(11)
rawDipMom = workSheet.col_values(12)
rawETotalLaList = workSheet.col_values(3)
rawETotalEuList = workSheet.col_values(4)
rawETotalLuList = workSheet.col_values(5)
rawETotalLigandList = workSheet.col_values(6)


DF = pandas.DataFrame()
DF = DF.assign(EbindLa = rawEbindLaList[4:])
DF = DF.assign(EbindNd = rawEbindNdList[4:])
DF = DF.assign(EbindEu = rawEbindEuList[4:])
DF = DF.assign(EbindLu = rawEbindLuList[4:])
DF = DF.assign(EHomo = rawEHomo[4:])
DF = DF.assign(DipMom = rawDipMom[4:])
DF = DF.assign(ETotalLa = rawETotalLaList[4:])
DF = DF.assign(ETotalEu = rawETotalEuList[4:])
DF = DF.assign(ETotalLu = rawETotalLuList[4:])
DF = DF.assign(ETotalLig = rawETotalLigandList[4:])
DataList = sdfFile.readlines()
linesAm = len(DataList)
q = 0
i = 0
while i < len(DataList):
    if str(DataList[i]).startswith("M  "):
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, DF.get_value(q, "EbindLu"))
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, ">  <EbindLu>")
        DataList.insert(i + 1, "\n")

        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, DF.get_value(q, "EbindEu"))
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, ">  <EbindEu>")
        DataList.insert(i + 1, "\n")

        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, DF.get_value(q, "EbindNd"))
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, ">  <EbindNd>")
        DataList.insert(i + 1, "\n")

        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, DF.get_value(q, "EbindLa"))
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, ">  <EbindLa>")
        DataList.insert(i + 1, "\n")

        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, DF.get_value(q, "EHomo"))
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, ">  <EHomo>")
        DataList.insert(i + 1, "\n")

        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, DF.get_value(q, "DipMom"))
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, ">  <DipMom>")
        DataList.insert(i + 1, "\n")

        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, DF.get_value(q, "ETotalLig"))
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, ">  <ETotalLig>")
        DataList.insert(i + 1, "\n")

        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, DF.get_value(q, "ETotalLu"))
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, ">  <ETotalLu>")
        DataList.insert(i + 1, "\n")

        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, DF.get_value(q, "ETotalEu"))
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, ">  <ETotalEu>")
        DataList.insert(i + 1, "\n")

        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, DF.get_value(q, "ETotalLa"))
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, "\n")
        DataList.insert(i + 1, ">  <ETotalLa>")
        DataList.insert(i + 1, "\n")
        q = q + 1
    i = i + 1

for line in DataList:
    outSdfFile.write(str(line))
