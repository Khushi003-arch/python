'''
dictionary are used to store data in key: value pair
unorder
mutable
don't allow duplicate keys
in dictionary list is not used as key.

'''

dict={
    'name':'khushi',
    'CGPA':8.05,
    'marks':[10,20,30],
    'is_adult':True
}

print(dict)
print(type(dict))
print(dict['name'])
print(dict['CGPA'])


# change the value of it :

dict['CGPA']=9.00

print('CGPA')