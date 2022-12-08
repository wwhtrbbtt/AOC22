with open("input", "r") as f:
    lines = f.read().split("\n")

sample = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

partTwo = False

# lines = sample.split("\n")

def getAllSections(i):
    t = i.split("-")
    return [i for i in range(int(t[0]), int(t[1])+1)]

def isFullyContained(s1, s2, r=True):
    contain=True
    for i in s1:
        if i not in s2:
            contain=False
            if not partTwo: break
        elif partTwo: return True

    if contain: return True
    if r: return isFullyContained(s2, s1, r=False)
    

c = 0
for l in lines:
    if not l: continue
    sections = l.split(",")
    sec1 = getAllSections(sections[0])
    sec2 = getAllSections(sections[1])
    if isFullyContained(sec1, sec2): c += 1
    
print("Task 1:", c)
