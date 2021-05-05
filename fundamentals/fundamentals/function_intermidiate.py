x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#update value:
x[1][0]=15
print(x)
students[0]["last_name"]="Bryant"
sports_directory["soccer"][0]="Andres"
z[0]["y"]=30
print(students)
print(sports_directory)
print(z)


#iterate 
def iterateDictionary(dic):
    for i in students:
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students)

def iterateDictionary2(key,dic):
    for i in dic:
        print(i[key])

iterateDictionary2('first_name', students)

def printInfo(dic):
    for key in dojo:
        print(len(dojo[key]),key)
        for i in dojo[key]:
            print(i)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
