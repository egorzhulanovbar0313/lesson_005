# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код

from district.central_street.house1 import room1 as cs_h1_r1, room2 as cs_h1_r2
from district.central_street.house2 import room1 as cs_h2_r1, room2 as cs_h2_r2
from district.soviet_street.house1 import room1 as ss_h1_r1, room2 as ss_h1_r2
from district.soviet_street.house2 import room1 as ss_h2_r1, room2 as ss_h2_r2

rooms = [cs_h1_r1, cs_h1_r2, cs_h2_r1, cs_h2_r2, ss_h1_r1, ss_h1_r2, ss_h2_r1, ss_h2_r2]

all_folks = []
for room in rooms:
    all_folks += room.folks
    
print(f"На районе живут {', '.join(all_folks)}")


