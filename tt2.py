a = []
b = a

print('Before')
print(a)
print(b)

if a is b:
    print('It is the same thing')

a.append('new thing')

print('After')
print(a)
print(b)