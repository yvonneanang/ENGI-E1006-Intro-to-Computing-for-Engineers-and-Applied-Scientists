#sumbitted by Yvonne Naa Ardua Anang (uni: yna2103)

li = [5, 2]
k = 3
new_li =[]
count = 0

while count < len(li):
    smallest_index = 0
    smallest_value = li[smallest_index]
    for x in li:
        if smallest_value == None:
            smallest_value = x
            smallest_index = li.index(x)
        if x != None and  x < smallest_value :
            smallest_value = x
            smallest_index = li.index(x)
    new_li.append(smallest_value)
    li[smallest_index] = None
    count += 1

print (new_li[0:k])
