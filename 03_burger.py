# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

# TODO здесь ваш код
import my_burger as mb

double_cheeseburger_recipe = []
mb.add_buns(double_cheeseburger_recipe)
mb.add_cheese(double_cheeseburger_recipe)
mb.add_beef(double_cheeseburger_recipe)
mb.add_cheese(double_cheeseburger_recipe)
mb.add_beef(double_cheeseburger_recipe)
mb.add_pickle(double_cheeseburger_recipe)
mb.add_tomato(double_cheeseburger_recipe)
mb.add_mayo(double_cheeseburger_recipe)

print(f"Рецепт двойного чизбургера:\n{', '.join(double_cheeseburger_recipe)}")

my_cheeseburger_recipe = []
mb.add_buns(my_cheeseburger_recipe)
mb.add_cheese(my_cheeseburger_recipe)
mb.add_beef(my_cheeseburger_recipe)
mb.add_cheese(my_cheeseburger_recipe)
mb.add_bacon(my_cheeseburger_recipe)
mb.add_onion(my_cheeseburger_recipe)
mb.add_tomato(my_cheeseburger_recipe)
mb.add_mayo(my_cheeseburger_recipe)

print(f"Рецепт моего чизбургера:\n{', '.join(my_cheeseburger_recipe)}")