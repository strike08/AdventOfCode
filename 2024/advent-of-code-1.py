import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

input = open('input/1.txt', 'r')


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def difference(valueOne, valueTwo):
    return abs(valueOne-valueTwo)

listOne = []
listTwo = []

for line in input:
    listOne.append(int(line.split('   ')[0]))
    listTwo.append(int(line.split('   ')[1].split('\n')[0]))
bubble_sort(listOne)
bubble_sort(listTwo)

result = 0
for item in range(len(listOne)):
    result += difference(listOne[item], listTwo[item])

print(result)