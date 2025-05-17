#COMING SOON

s="aa"
p="a"
s_counter = 0

for i in range(len(p)):
    if p[i] == "*":
        while (p[i-1] == s[s_counter]) or (p[i-1] == "."):
            s_counter += 1

    elif p[i] == ".":
        s_counter += 1
    else:
        if s[s_counter] == p[i]:
            s_counter += 1
        elif i < len(p) and p[i+1] == "*":
            s_counter += 1
        else:
            print(False)