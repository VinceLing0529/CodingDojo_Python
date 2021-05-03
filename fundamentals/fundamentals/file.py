num1 = 42 #variable declaration-integer
num2 = 2.3 #variable declaration-floats
boolean = True #variable declaration-boolean
string = 'Hello World'#variable declaration-string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration-list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration-dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration-tuples
print(type(fruit))#tuples
print(pizza_toppings[1])#Sausage
pizza_toppings.append('Mushrooms')#add value
print(person['name']) #John
person['name'] = 'George' #change value
person['eye_color'] = 'blue' #add value
print(fruit[2])#access value


if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#if statement, will do lower
    
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#Just right!

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

#0 1 222 33 44 555
pizza_toppings.pop()#delete last
pizza_toppings.pop(1)#delete second

print(person)#show value
person.pop('eye_color')#delete key with value
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#After 1st if statement
    
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

#HelloHelloHelloHelloHelloHelloHelloHelloHelloHello
print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
#HelloHelloHelloHello

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
#HelloHelloHelloHelloHelloHelloHelloHelloHelloHello

#HelloHelloHelloHello

"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
