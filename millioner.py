import random
import time

print("Enter your name")
name = str(input())
print("Enter your age")
age = int(input())


addage = int(random.randint(5, 10))

for i in range(5):
    print("Please waiting .... ")
    time.sleep(2)


print("Congratulation ! You will be millionare in ", age + addage, "years")



