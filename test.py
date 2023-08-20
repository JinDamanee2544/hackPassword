from common import *

c = genCaseCombination("hello")
l = []
for i in c:
    w = getSubsitueCombintion(i)
    l = [*l, *w]
print(set(l))
print(len(set(l)))
