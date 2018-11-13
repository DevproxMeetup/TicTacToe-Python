minimum_to_buy_alc = 16

def age_check(age):
    return age > minimum_to_buy_alc

print('Hello World')
print('Good bye')
age = 21
if age_check(age):
    print('Alcohol sale allowed')
    shopper_name = input('Enter cust name: ')
    shopper = {
        'name': shopper_name,
        'age': age
    }
    print('Shopper {name} has age {age}:'.format(**shopper))
else:
    print('Sale not allowed to under aged drinkers')
print('Outside')


i = 3.333
print(str(i))