"taking input from file"

text_file = open("input.txt", "r")
coins = text_file.read().split()
coins = list(map(int, coins))


def Coinchange(n, c_a, c_o):
    if sum(c_o) == n:
        yield c_o
    elif sum(c_o) > n:
        pass
    elif not c_a:
        pass
    else:
        for c in Coinchange(n, c_a[:], c_o + [c_a[0]]):
            yield c
        for c in Coinchange(n, c_a[1:], c_o):
            yield c


n = int(input("Enter the coin to be paid : "))
solution = [s for s in Coinchange(n, coins, [])]
print("Ways:",len(solution))

print("Ways can be like this: ")
for s in solution:
    print(s)
