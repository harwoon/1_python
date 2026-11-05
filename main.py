# main.py

import fruit
#from fruits import apple_info, banana_info, func1 #init에 func1 추가해서
#from fruits.apple import func1 #fruit패키지 내 apple의 func1
from fruits import *

fruit.print_fruit("사과")

result = fruit.add_quantity(10, 5)
print(result)

apple = fruit.Fruit("사과", 10)
apple.print_info()

print("*" * 30)
print(apple_info())
print(banana_info())
print(func1())