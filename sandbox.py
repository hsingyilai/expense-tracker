expense = ["a", "b", "c", "d"]
flag = [False, True]

for i in range(len(expense)):
    if i >= len(flag):
        flag.append(False)

print(flag)
