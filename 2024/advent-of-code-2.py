import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def validateReport(reportValues):
    if (reportValues[0] < reportValues[-1]):
        return validateIncreasing(reportValues)
    if (reportValues[0] > reportValues[-1]):
        return validateDecreasing(reportValues)
    return 0

def validateIncreasing(reportValues):
    for item in range(0, len(reportValues) - 1):
        difference = reportValues[item+1] - reportValues[item]
        if (difference == 0 or difference < 1 or difference > 3):
            return 0
    return 1

def validateDecreasing(reportValues):
    for item in range(0, len(reportValues) - 1):
        difference = reportValues[item] - reportValues[item+1]
        if (difference == 0 or difference < 1 or difference > 3):
            return 0
    return 1

input = open('input/2.txt', 'r')

safeReports = 0
for line in input:
    reportValues = list(map(int, line.split(' ')))
    safeReports += validateReport(reportValues)
print(safeReports)