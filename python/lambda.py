def square(x): return x*x
# x = int(input('Enter your name: '))
# square(x)

people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person: person['name'])
def f(person):
    return person['name']

# people.sort(key=f)

print(people)
