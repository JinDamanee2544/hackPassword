from common import *
import time

LOOP_COUNT = 10
DISPLAY_FLOATING_DIGITS = 10

lines = []

with open("10k.txt", "r") as f:
    allWord = f.readlines()


def measureTime():
    rainbow = open("rainbow.txt", "w")
    start = time.time()
    for line in allWord:
        line = line.strip()
        for caseList in genCaseCombination(line):
            for subWord in getSubsitueCombintion(caseList):
                hashed = hash(subWord)
                rainbow.write(subWord + " : \t" + hashed + "\n")
    end = time.time()
    rainbow.close()
    return end - start


timeList = []
for i in range(LOOP_COUNT):
    currTime = measureTime()
    timeList.append(currTime)
    print("Loop ", i + 1, " finished with :", currTime, "seconds")
geometricMean = 1
for i in timeList:
    geometricMean *= i
geometricMean = geometricMean ** (1 / LOOP_COUNT)

with open("rainbow.txt", "r") as f:
    allRainbow = f.readlines()

hashGenerated = len(allRainbow)

print("-----------------")
print(
    "Generate all possible combination of cases and subsitued characters comes with :",
    hashGenerated,
    "passwords",
)
print(
    "Geometric mean creating Rainbow table is \t : ",
    round(geometricMean, DISPLAY_FLOATING_DIGITS),
    "seconds",
)
print(
    "Average time per passwords trying \t\t : ",
    round(geometricMean / hashGenerated, DISPLAY_FLOATING_DIGITS),
    "seconds",
)
