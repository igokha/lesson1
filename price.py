def format_price(price):
    p=int(price)
    s = 'price: ' + str(p) + ' rub.'
    return s.capitalize()

print(format_price(586.43))