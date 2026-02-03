message1 = " Agent:007_Bond; Coords:(40,74); Items:gun,money,gun; Mission:2025-RESCUE-X "
info1 = {}
#for message1
#这里为了突出slice的用法

idx = message1.index("Mission")
start_idx = idx + len("Mission")
mission = message1.strip()[start_idx:]
info1["Mission"] = mission

T1 = message1.strip().split("; ")
for k in T1:
    T2 = k.split(":")
    if T2[0] == "Coords":
        location =T2[1].split('(')[1].split(')')[0].split(',')
        x,y = int(location[0]), int(location[1])
        coord = tuple((x,y))
        info1[T2[0]] = coord
        continue
    elif T2[0] == "Items":
        items = set(T2[1].split(','))
        info1[T2[0]] = items
        continue
    #也可以直接在分割里取
    # elif T2[0] == "Mission":
    #     mission = T2[1]
    #     info1[T2[0]] = mission
    else:
        info1[T2[0]] = T2[1]
print(info1)