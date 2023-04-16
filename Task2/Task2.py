# -*- coding: utf-8 -*-
import json

def write_order_to_json(item, quantity, price, buyer,date):
    order_data = {'item': item,
                  'quantity': quantity,
                  'price': price,
                  'buyer': buyer,
                  'date': date}
    with open('orders.json', 'w', encoding='utf-8') as f:
        json.dump(order_data, f, indent=4, ensure_ascii=False)

write_order_to_json('кофе', 'молоко', 'зерно', 'цветы', 'лето')



