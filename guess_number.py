
'''number = 30


while True:
    i = int(input('Guess number in range 1-30 :'))
         
    if i == number:
        break
    if i < number:
        print ("Number more than :" )
    else:
        print("Number less than :" )

print('Congratulations ! You are WiN')
'''

'''x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("Perv")
elif x > 0 and y < 0:
    print("Chet")
elif x < 0:
    print("Vtoraya")
else:
    print("tretja")
'''

'''a = 1
while a <= n:
    print(a)
    a += 1
'''

'''x = 0
import turtle

turtle.shape('turtle')
turtle.width(10)
while x != 4 :
    turtle.forward(50)
    turtle.left(90)
    x = x + 1

x = 0
turtle.penup()
turtle.goto(70, -10)
turtle.pendown()
turtle.left(90)
turtle.forward(80)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)
turtle.left(90)
turtle.forward(90)    



x = 0
turtle.penup()
turtle.goto(100, -10)
turtle.pendown()

turtle.left(90)
turtle.forward(130)

turtle.left(90)
turtle.forward()
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(140)    



#while x != 4 :
 #   turtle.forward(100)
  #  turtle.left(90)
   # x = x + 1
'''


'''a = 0
while a < 10:
    a = a +1
    t.fd(60 + a*20)
    t.left(90)
    t.fd(60 + a*20)
    t.left(90)
    t.fd(60 + a*20)
    t.lt(90)
    t.fd(60 + a*20)
    t.lt(90)
 
    t.penup()
    t.goto(-a*10,-a*10)
    t.pendown()
'''

import turtle


a = 0
b = 10
turtle.shape('turtle')
while a < 12:
    turtle.forward(160)
    turtle.left(180)
    turtle.forward(160)
    turtle.left(b + 200)
    a = a + 1
    turtle.goto(0, 0 )

