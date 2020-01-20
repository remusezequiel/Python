course = 'Curso'
string = 'python'

result = '{} de {}'.format(course,string)
print(result)
result = '{a} de {b}'.format(a=course,b=string)
print(result)
result = result.lower()
print(result)
result = result.upper()
print(result)

#Busqueda
result = '{} de {}'.format(course,string)
print(result)
pos = result.find('Curso')
print(pos)
count = result.count('o')
print(count)
new_result = result.replace('o','a')
print(new_result)
new_result = result.split(' ')
print(new_result)
