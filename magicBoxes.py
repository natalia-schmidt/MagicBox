numberMagicBoxes = 42
magicBoxes = dict()
filename = "actions.txt"
fin = open(filename, "r")
lines = fin.readlines()
i = 0
fin.close()
error = False
while not error and i < len(lines):
    actor = lines[i].strip().split()[0]
    fruit = lines[i].strip().split()[3]
    if actor == "Bob":
        if fruit in magicBoxes.keys():
            magicBoxes[fruit] += 1
        else:
            if len(magicBoxes.keys()) >= numberMagicBoxes:
                print(f"ERROR: the object {fruit} cannot be stored.")
                error = True
            else:
                magicBoxes[fruit] = 1
    elif actor == "Carl":
        if fruit not in magicBoxes.keys():
            print(f"ERROR: The object {fruit} is not available.")
            error = True
        else:
            magicBoxes[fruit] -= 1
            if magicBoxes[fruit] == 0:
                magicBoxes.pop(fruit)

    i += 1