import os
cook_book = {}
def cookbook():
    file_path = os.path.join(os.getcwd(), 'Receips.txt')
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            counter = int(f.readline())
            ing_list = list()
            for item in range(counter):
                ingredients = {}
                ingr = f.readline().strip()
                ingredients['ingredient_names'] = ingr.split('|')[0]
                ingredients['quantity'] = ingr.split('|')[1]
                ingredients['measure'] = ingr.split('|')[2]
                ingredients['quantity'] = int(ingredients['quantity'])
                ing_list.append(ingredients)
            f.readline()
            cook_book[dish_name] = ing_list
    return cook_book
cookbook()
print(cook_book)
#
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                new_shop = dict(ingredient)
                new_shop['quantity'] = float(new_shop['quantity'])
                new_shop['quantity'] *= person_count
                if new_shop['ingredient_names'] not in shop_list:
                    keys = ['measure', 'quantity' ]
                    shop_list[new_shop['ingredient_names']] = {x:new_shop[x] for x in keys}
                else:
                    shop_list[new_shop['ingredient_names']]['quantity'] += new_shop['quantity']
        else:
            print(dish, "=> Такого блюда нет")
    print(shop_list)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 5)
# pprint(cook_book)