import random
class value:
    def __init__(self,t,d):
        self.times=t
        self.date=set([d])
with open('C:/Users/Tongji511/Desktop/distribute system/tb_call_201202_random-revise.txt', 'r') as f:
    f3 = f.read().split('\n')
    f3 = [i.split('\t') for i in f3]
    f3 = random.sample(f3,k=5000)
    name_dict={}
#print(name_dict[f3[0][1]])
    for j in f3:
        if j[1] in name_dict:
            v = name_dict[j[1]]
            v.times+=1
            v.date.add(j[0])
            name_dict[j[1]]=v
        else:
            v = value(1,j[0])
            name_dict[j[1]]=v
