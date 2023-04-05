
ll = []
with open('./resources/History.txt', encoding='UTF-8') as f:
    for line in f.readlines():
        ll.append(line.strip('\n').split(',')[0])
print(ll)