from common import *

lines = []
with open("10k.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    for caseList in genCaseCombination(line):
        for subWord in getSubsitueCombintion(caseList):
            if checkHash(subWord):
                print("--------------------")
                print("Found!", subWord)
                print("--------------------")
                exit(0)
    print("Incorrect!", line)
print("Not found!")
