import os
import re
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

input = open('input/3.txt', 'r')

def calculateMuls(muls):
    result = 0
    for mul in muls:
        nums = re.findall(r'\d{1,3}', mul)
        result += int(nums[0]) * int(nums[1])
    return result

finalResult = 0

for line in input:
    mulsInLine = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
    finalResult += calculateMuls(mulsInLine)
print(finalResult)
