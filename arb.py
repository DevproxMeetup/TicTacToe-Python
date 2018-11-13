def func(val1, name=None, age=None):
    print('The Value:', val1)
    print('Age and Name:', age, name)

func('v1', 'the name', 123)

value_list = ['The Value', 'The Name here', 444]

func(*value_list)