def get_summ(one, two, delimiter='&'):
    #str1 = str(one)
    #str2 = str(two)
    #deli = str(delimiter)
    string = str(one) + str(two) + str(delimiter)
    return string.upper()

a=get_summ('a', 'df')
print(a)