import json
with open("rawmovements.txt") as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
i=0
movements = {}
moveName = 'bravo'

for x in content:
    frame ={}
    x = x.replace("<","")
    x = x.replace(">", "")
    x = x.replace("=", " ")
    x = x.replace('"', '')
    angles = x.split(" ")
    #First angle value is at 4 Last one is at 21 in angles
    frame['right_titty'] = float(angles[4])
    frame['left_titty'] = float(angles[5])
    frame['right_shoulder'] = float(angles[6])
    frame['left_shoulder'] = float(angles[7])
    frame['right_hand'] = float(angles[8])
    frame['left_hand'] = float(angles[9])
    frame['right_ab'] = float(angles[10])
    frame['left_ab'] = float(angles[11])
    frame['right_ass'] = float(angles[12])
    frame['left_ass'] = float(angles[13])
    frame['right_hip'] = float(angles[14])
    frame['left_hip'] = float(angles[15])
    frame['right_knee'] = float(angles[16])
    frame['left_knee'] = float(angles[17])
    frame['right_ankle'] = float(angles[18])
    frame['left_ankle'] = float(angles[19])
    frame['right_foot'] = float(angles[20])
    frame['left_foot'] = float(angles[21])
    with open("output.txt", 'a+') as o:
        o.write("\n")
        o.write(moveName + "" + str(i) + " = ")
        json.dump(frame, o)
    movements[i] = frame
    i += 1
print(movements)
