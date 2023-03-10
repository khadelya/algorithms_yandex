with open("input.txt", "r") as file:
    contents = file.read().split()
    ans = [0 for _ in range(len(contents))]
    dct = {}
    for i, word in enumerate(contents):
        if word not in dct:
            dct[word] = 0
        ans[i] = dct[word]
        dct[word] += 1
print(*ans)
