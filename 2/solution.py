with open("input", "r") as f:
    lines = f.read().split("\n")

sample = """A Y
B X
C Z"""

# lines = sample.split("\n")

# a/x = rock
# b/y = paper
# c/z = scissor

draw = {
            "r": "r",
            "p": "p",
            "s": "s"
    }

win = {
            "r": "s",
            "p": "r",
            "s": "p"
    }

loose = {
            "r": "p",
            "p": "s",
            "s": "r"
    }

points = {
            "r": 1,
            "p": 2,
            "s": 3
    }

def calcPoints(elve, my):
    if draw[my] == elve: return points[my] + 3
    elif win[my] == elve: return points[my] + 6
    else: return points[my]

def normalize(i):
    if i in "AX": return "r"
    if i in "BY": return "p"
    if i in "CZ": return "s"

def calcPointsTwo(elve, my):
#    print("=====")
#    print("Combo:", elve, my)

    # r means we wanna loose 
    # p means we need a draw 
    # s means a win 
    if my == "r":
#        print("Loosing. Points:", points[win[elve]], "+ 0. Chose", win[elve])
        return points[win[elve]]
    if my == "p":
#        print("Draw. Points:", points[draw[elve]], "+ 3. Chose", draw[elve])
        return 3 + points[draw[elve]]
    if my == "s":
#        print("Win. Points:", points[win[elve]], "+ 6. Chose", loose[elve])
        return 6 + points[loose[elve]]

totalPointsOne = 0
totalPointsTwo = 0
for i in lines:
    if not i: continue
    elveSign = normalize(i.split()[0])
    mySign = normalize(i.split()[1])

    p2 = calcPointsTwo(elveSign, mySign)
    p1 = calcPoints(elveSign, mySign)

    totalPointsOne+=p1
    totalPointsTwo+=p2
    
print("Answer 1:", totalPointsOne)
print("Answer 2:", totalPointsTwo)
