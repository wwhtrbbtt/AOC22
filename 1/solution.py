with open("input", "r") as f:
    lines = f.read().split("\n")

elves = [0 for _ in range(len(lines))]
c = 0
for l in lines:
    if not l:
        c+=1
    else:
        elves[c] += int(l)

print(f"Top elve: {max(elves)}")
#print(f"Top 3 elves together: {sum(sorted(zip(elves), reverse=True)[:3])}")
print(f"Top 3 elves: {sum([i[0] for i in sorted(zip(elves), reverse=True)[:3]])}")
