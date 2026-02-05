#2.5
#learn
import json
import re

sum = [i**2 for i in range(10)]
print(sum)

iterable = ["张三","李四"]
students = list(map(lambda s:"".join(["QG_",s]),iterable))
print(students)

#practise

raw_data = ["85", "92", "ERROR", "1050", "78", "WARNING", "99", "120"]
def condition(s:str):
    try:
        #这里不用int(),s.isnumeric(),s.isdigit()
        #是因为他们只能处理证书，而float可以处理整数，小数，更加全面
        temp = float(s)
        if temp >= 80:
            return True
        else:
            return False
    except:
        return False
num_data = [float(num) for num in raw_data if condition(num)]
# 当然这里要用filter也可以
# num_data = list(map(float,filter(condition,raw_data)))
max_num = max(num_data)
min_num = min(num_data)
result = list(map(lambda x : (x-min_num)/(max_num-min_num),num_data))
output = ["核心过载" if x > 0.8 else "运转正常" for x in result]
print(output)
print("")



#从提供的数据集practise
#这里分界标准使用0.8
#类似85.5.5和85..5这种不确定清洗成啥的都置了None
def clean(s):
    if isinstance(s, dict):
        if s["value"]:
            ret = clean(s["value"])
        else:
            ret = clean(s["val"])
        return ret
    elif isinstance(s, list):
        ret = list(map(clean, s))
        return ret
    elif s is None or isinstance(s, bool) or s.strip() in ["null", "undefined", "NaN", "Infinity", "-Infinity"]:
        return None

    s = s.strip()
    if not s:
        return None

    cleaned = re.sub(r"[^\d\.\-+eEobx]", "", s)
    if not cleaned:
        return None
    if cleaned[2:] != "":
        if cleaned[:2] == "0x":
            return int(cleaned[2:], 16)
        elif cleaned[:2] == "0b":
            return int(cleaned[2:], 2)
        elif cleaned[:2] == "0o":
            return int(cleaned[2:], 10)

    try:
        ret = float(cleaned)
        return ret
    except:
        return None



def nom(data:list):
    maxx = max(data)
    minx = min(data)
    if maxx == minx:
        return [1]
    return list(map(lambda x : (x-minx)/(maxx-minx),data))

def flatten(items):
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(flatten(item))
        else :
            result.append(item)
    return result

print("以下数据源自energy_data.json")
with open("energy_data.json","r",encoding="utf-8") as f:
    data_all = json.load(f)

for  data in data_all:
    print("原来的数据:")
    print(data)
    print("输出:")
    cleaned1 = list(map(lambda x : clean(x),data))
    cleaned2 = flatten(cleaned1)
    print(cleaned2)
    temp = list(filter(lambda x:x is not None,cleaned2))
    if len(temp) != 0:
        result = nom(temp)
        if isinstance(result, float):
            output = "核心过载"
        else:
            output = ["核心过载" if x > 0.8 else "运转正常" for x in result]
        print(result)
        print(output)
        print("")
    else:
        print("空\n")
