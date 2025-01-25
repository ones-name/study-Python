magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")


number=[1,2,3,4]
for numbers in number:
    print(numbers)
    b = numbers + 2
    print(b)
print(100)

pizzas=["chess pizza","chicken pizza","beef pizza" ]
for pizza in pizzas:
    print(pizza)
    print(f"i like {pizza}")
print(f'i really love {pizza}')
animals=["chicken","duck","goose"]
for animal in animals:
    print(f"A {animal} would make a great pet")
print("Any of these animals are birds!")
print(animals)
nums=range(1,5)
for i in nums:
    print(i)
even_numbers = list(range(2, 11, 3))
print(even_numbers)
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)
for ber in range(1,21):
    print(ber)
we=list(range(1,100))
print(min(we))
print(max(we))
print(sum(we))
# our=[]
# for i in range(1,100):
#     our.append(i)
# print(our)
n=list(range(1,20,2))
for m in n:
    print(m)
v=list(range(3,30,3))
for j in v:
    print(j)
time=list(range(1,10))

ko=[i**3 for i in range(1,10)]
print(ko)
he=[]
for ke in range(1,10):
    e=ke**3
    he.append(e)
print(he)
players = ['charles', 'martina', 'michael', 'florence', 'eli']
x=players[:]
print(x)
dimensions = (200, 50)
print(dimensions)
dimensions = (400, 100)
print(dimensions)
for i in range(1,21):
    if i == 10:
        print("this is 55")
        print("this is 10")