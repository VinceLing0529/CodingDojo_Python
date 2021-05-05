def countdown(number):
    new_list=[]
    for i in range(number+1):
        new_list.append(number)
        number -=1
    return new_list 

print(countdown(5))

def printandreturn(li):
    print(li[0])
    return(li[1])

def firstpluelength(li):
    x= li[0]+len(li)
    return x

print(firstpluelength([1,2,3,4,5]))

def vgs(li):
    new_list=[]
    if len(li)<2:
        return False
    for i in range(len(li)):
        if li[i-1]<li[i]:
            new_list.append(li[i])
    return new_list

print(vgs([5,2,3,2,1,4]))
print(vgs([3]))

def lv(length,value):
    new_list=[]
    for i in range(length):
        new_list.append(value)
    return new_list
print(lv(4,7))
print(lv(6,2))