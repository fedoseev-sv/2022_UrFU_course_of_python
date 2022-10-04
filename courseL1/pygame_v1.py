"""
It's game from courses Python Skillfactory.
You have to choce number. It's all. 
"""

import numpy as np

number:int = np.random.randint(1, 101)
count:int = 0

while True:
    count += 1
    predict_number:int = int(input("Введие число: "))
    
    if number > predict_number:
        print("Число меньше загаданного.")
    elif number < predict_number:
        print("Число больше загаданного.")
    else:
        print(f"Вы угадали с {count} попытки.")
        break
