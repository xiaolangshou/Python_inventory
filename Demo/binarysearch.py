list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
target = 5
num = 0

def func(l,t):
    count = 0
    for i in l:
        if i == t:
            count += 1
    if count <= 0:
        print('no taget in list')
    else:
        global num
        num += 1
        midV = l[int(l.__len__()/2)]
        if t == midV:
            print('find target %s in step %s' %(midV, num))
        else:
            if t > midV:
                for i in l:
                    if i < midV:
                        l.remove(i)
                    elif i == midV:
                        print('find target %s in step %s' %(midV, num))
                        return
                    else:
                        pass
            else:
                for i in l:
                    if i > midV:
                        l.remove(i)
                    elif i == midV:
                        return
                    else:
                        pass

func(list,target)
