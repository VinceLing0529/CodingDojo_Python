
def change(str1):
    str1 = str1.strip().split()
    expected1 =""
    for i in str1:
        expected1 += i[0].upper()
    print(expected1)

str1 = " there's no free lunch - gotta pay yer way. ";
str2 = "Live from New York, it's Saturday Night!";
change(str1)
change(str2)





x = "abcdefg"

rev = ""
for i in range(len(x), 0, -1):
    rev += x[i-1]
print(rev)



