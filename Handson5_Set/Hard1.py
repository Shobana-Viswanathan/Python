words = input("Enter words : ").split(",")
grp = {}
for word in words:
    key = ''.join(sorted(word.replace(" ", "")))
    if key not in grp:
        grp[key] = set()
    grp[key].add(word)
print(list(grp.values()))