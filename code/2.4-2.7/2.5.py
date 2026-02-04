#2.5
#learn
import json
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

#从提供的数据集中抽取了一些有意思的数据来进行练习
#嘻嘻

l1 = ["\ufeff90", "\u0000", "\u001F", " ", "\t\n\r"]
l2 = ["１２０", "８０.５", "７９", "100.0"]
l3 = ["0x50", "0b1010000", "0o120", "80"]
#l4 = [null, true, false, "NaN", "Infinity", "-Infinity", "undefined", "null"]
