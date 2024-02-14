### File Owners


def group_by_owners(files):
    newDict = {}
    for v, k in files.items():
        if k in newDict:
            tmp = newDict.get(k)
            tmp.append(v)
            newDict[k] = tmp
        else:
            newDict[k] = [v]
    return newDict


def group_by_owners(files):
    owners = defaultdict(list)
    for file, owner in files.items():
        owners[owner].append(file)
    return owners


if __name__ == "__main__":
    files = {"Input.txt": "Randy", "Code.py": "Stan", "Output.txt": "Randy"}
    print(group_by_owners(files))
