# LOOPS 
# repeating something

print("today is on thursday")

# printing this 100 times 

# the types of loops
#while loops 
#for loops 

#while loops 

# while condition:
    #code

cake = 1 

while cake <= 9:
    print(cake)
    cake += 1

#for loops 
#reapeating sequence

for numbers in range(7):
    print(numbers)

for i in range(5):
    print(i)

    for i in range(0,12,2):
        print(i)

for i in range(1,6):
    print(i)

#LOOPING THROUGH STRINGS

for letters in "PYTHON":
    print(letters)

#BREAKS 
#stops the loop immediately
for i in range(1,11):
    if i == 6:
        break
    print(i)

#continue 
#skipps one interation

for i in range(1,11):
    if i == 5:
        continue
    print(i) 


    #PASSWORD CHECKER 
    password = "" 
    while password != "12345":
        password = input("Enter your password: ")

    print("WELCOME") 



