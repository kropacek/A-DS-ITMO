def prefix(string: str) -> int:
    pi = [0] * len(string)
    i, j = 1, 0
    while i < len(string):
        if string[i] == string[j]:
            pi[i] = j+1
            i += 1; j += 1
        elif j == 0:
            pi[i] = 0
            i += 1
        else:
            j = pi[j-1]
    return pi

print(prefix('14'))