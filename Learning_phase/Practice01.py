print("Hello,World!")

x=10
y="alice"
pi=3.14
is_actice=True

# type casting 

x=int("10")
print(x)
y=str(124)
print(y)

# dynammic typing
x=10
print(f"x is of type {type(x)}")

x="Now I am string"
print(f"x is now type {type(x)}")

# conditionals

x=10

if x>5:
    print("x is great")
elif x==5:
    print("x is 5")
else:
    print("x is less than 5")

# loops

for i in range(1,11):
    print(i)

fruit = ["apple","banana","cherry"]

for fru in fruit:
    print(fru)

# even number 

for i in range(2,21,2):
    print(i)

text="Python"
for char in text:
    print(char)


numbers = [1,2,3,4,5]
total=0
for num in numbers:
    total+=num
print("Sum:",total)

fruits = ["app","bana","dev"]

for fru in fruit:
    print(fru)

# factorial 

num = 5
factorial=1

for i in range(1,num+1):
    factorial*=i
print("Factorial:",factorial)

# reverse a string

# text="Hello"
# reverse_text=""
# for char in text:
#     reverse_text=char+reverse_text
# print("Reverse String:",reverse_text)

# multiplication table

# n=5
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

# count vowels in string

# text="Python Programming"
# vowels="aeiouAEIOU"
# count=0
# for char in vowels:
#     if char in vowels:
#         count+=1
# print("Number of vowels: ",count)


# while loop

# i=1
# while i<=10:
#     print(i)
#     i+=1

# sum the numbers

# n=5
# sum=0
# i=1
# while i<= n:
#     sum+=i
#     i+=1
# print("Sum: ",sum)

# reverse a number

# num=12345
# reverse_num=0
# while num>0:
#     digit=num%10
#     reverse_num=reverse_num*10+digit
#     num//=10
# print("Reverse:", reverse_num)

# # print element of a list

# fruit=["apple","banana","cherry"]

# i=0
# while i<len(fruit):
#     print(fruit[i])
#     i+=1

# # infinite loop 

# while True:
#     print("This is a infinite loop")

# guess the number game 

secret_number = 7

guess = None
while guess !=secret_number:
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
print("congratlation!")
    

