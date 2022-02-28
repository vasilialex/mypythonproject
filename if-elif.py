a = 30
if a == 25:
    print('best age 25')
elif a < 10:
    print('betw 1 - 10')
elif (a >= 10) and (a <= 20):
    print('betwn 10-20')
else:
    print ('you are noob')


all_cars = ['BMW', 'AUDI', 'MAZDA', 'SEAT', 'FORD']
my_cars = ['BMW', 'AUDI']

for i in all_cars:
    if i in my_cars:
        print( i + " ""my_cars" )
    else: print(i + " " "dont have car")

