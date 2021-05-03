#Basic:
for x in range(151):
    print(x)
#Multiples of Five
for x in range(5,1001,5):
    print(x)
#Counting, the Dojo Way
for x in range(1,101):
    if x%5==0:
        if x%10==0:
            print("Coding Dojo")
        else:
            print("Coding")
    else:
        print(x)
#Whoa. That Sucker's Huge 
num = 0
for x in range(1,500000,2):
    num +=x
print(num)
#Countdown by Fours
for x in range(2018,0,-4):
    print(x)

#Flexible Counter
