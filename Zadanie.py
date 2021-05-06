from pprint import pprint
with open("Receips.txt",encoding='utf-8') as file:
    cook_book = {}
    lines = file.readlines()
    omlete_list = []
    omlete_ele = []
    pekin_list = []
    pekin_ele = []
    baked_ele = []
    baked_list = []
    fachitos_ele = []
    fachitos_list = []
    for r in range(2, (2+int(lines[1]))):
        omlete_ele += [lines[r].strip().split(" | ")]
    for i in range(int(lines[1])):
        omlets_in = {}
        omlets_in["ingredients_name"] = omlete_ele[i][0]
        omlets_in["quantity"] = omlete_ele[i][1]
        omlets_in["measure"] = omlete_ele[i][2]
        omlete_list.append(omlets_in)
    cook_book[lines[0].strip()] = omlete_list
    for r in range(8, (8+int(lines[7]))):
        pekin_ele += [lines[r].strip().split(" | ")]
    for n in range(int(lines[7])):
        pekin_in = {}
        pekin_in["ingredients_name"] = pekin_ele[n][0]
        pekin_in["quantity"] = pekin_ele[n][1]
        pekin_in["measure"] = pekin_ele[n][2]
        pekin_list.append(pekin_in)
    cook_book.update({lines[6].strip() : pekin_list})
    for r in range(15, (15+int(lines[14]))):
        baked_ele += [lines[r].strip().split(" | ")]
    for b in range(int(lines[14])):
        baked_in ={}
        baked_in["ingredients_name"] = baked_ele[b][0]
        baked_in["quantity"] = baked_ele[b][1]
        baked_in["measure"] = baked_ele[b][2]
        baked_list.append(baked_in)
    cook_book.update({lines[13].strip() : baked_list})
    for r in range(21, (21+int(lines[20]))):
        fachitos_ele += [lines[r].strip().split(" | ")]
    for f in range(int(lines[20])):
        fachitos_in = {}
        fachitos_in["ingredients_name"] = fachitos_ele[f][0]
        fachitos_in["quantity"] = fachitos_ele[f][1]
        fachitos_in["measure"] = fachitos_ele[f][2]
        fachitos_list.append(fachitos_in)
    cook_book.update({lines[19].strip(): fachitos_list})

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for dish_names, ingredients in cook_book.items():
            for ingredient in ingredients:
                if dish in dish_names:
                    new_shop = dict(ingredient)
                    new_shop['quantity'] = float(new_shop['quantity'])
                    new_shop['quantity'] *= person_count
                    if new_shop['ingredients_name'] not in shop_list:
                        keys = ['measure', 'quantity' ]
                        shop_list[new_shop['ingredients_name']] = {x:new_shop[x] for x in keys}
                    else:
                        shop_list[new_shop['ingredients_name']]['quantity'] += new_shop['quantity']
    pprint(shop_list)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 5)
pprint(cook_book)