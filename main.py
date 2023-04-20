dict_ = {}
tot_ = {}

with open('1.txt', encoding='utf-8') as f1:
    list1 = f1.readlines()
    dict_['1.txt'] = list1
    tot_[len(list1)] = '1.txt'

with open('2.txt', encoding='utf-8') as f2:
    list2 = f2.readlines()
    dict_['2.txt'] = list2
    tot_[len(list2)] = '2.txt'

with open('3.txt', encoding='utf-8') as f3:
    list3 = f3.readlines()
    dict_['3.txt'] = list3
    tot_[len(list3)] = '3.txt'


sort_ = dict(sorted(tot_.items(), key=lambda item: item[0]))

with open('4.txt', 'w') as file:
    for key, value in sort_.items():
        put = str(value) + '\n' + str(key) + '\n' + "".join(dict_.get(value)) + '\n'
        file.write(put)



