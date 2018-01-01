import random
class value:
    def __init__(self,t,d):
        self.times=t
        self.date=set([d])
with open('C:/Users/75799/Desktop/1111/tb_call_201202_random.txt', 'r') as f:
    row_data = f.read().split('\n')
    list_data = [i.split('\t') for i in row_data]
    part_list_data = random.sample(list_data,k=5000)
    name_dict={}
#print(name_dict[f3[0][1]])
    for j in part_list_data:
        if j[1] in name_dict:
            v = name_dict[j[1]]
            v.times+=1
            v.date.add(j[0])
            name_dict[j[1]]=v
        else:
            v = value(1,j[0])
            name_dict[j[1]]=v
    with open('C:/Users/75799/Desktop/1111/tb_call_201202_random_write.txt', 'w') as f1:
        for (k, v) in name_dict.iteritems():
            # print(k)#user
            date_length = len(v.date)
            average_times = v.times / date_length
            f1.write(k+','+str(average_times)+',' +'\n')