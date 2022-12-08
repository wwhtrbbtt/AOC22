with open("input", "r") as f:
    lines = f.read().split("\n")

sample = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".split("\n")
# lines = sample

def getCompartments(i):
    l = int(len(i)/2)
    return i[:l], i[l:2*l]

def getCommonChars(comps):
    return list(dict.fromkeys([i for i in comps[1] if i in comps[0]]))

def smartOrd(char):
    if ord(char)>96: return ord(char)-96
    else: return ord(char)-38

s = 0
for l in lines:
    comps = getCompartments(l)
    common = getCommonChars(comps)
    s += sum([smartOrd(i) for i in common])

print("Task 1:", s)

group = 0
groups = [[]]
for c, l in enumerate(lines):
    if c % 3 == 0 and c != 0: 
        group+=1
        groups.append([])
    groups[group].append(l)

s = 0
for group in groups:
   if len(group) != 3: 
       continue
   c1 = getCommonChars((group[0], group[1]))
   common = getCommonChars((group[2], "".join(c1)))
   s += sum([smartOrd(i) for i in common])
print("Task 2:", s)
