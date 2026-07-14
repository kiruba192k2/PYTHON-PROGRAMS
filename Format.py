'''string1 = 'Student : {name} Marks : {marks}'
print(string1.format(name="Aarav", marks=95))
print('Student : {1} Marks : {0}'.format('88', 'Priya'))
print(f'{25:b}')
name = 'Rahul'
marks = 82
print(f'Student : {name} Marks : {marks}')
print(f'{7.89654:.2f}')
print(f'{45:5}')
print(f'{45:3}')
print(f'{45:04}')
print(f'{987654:,}')
print(f'{0.675:.2%}')'''

l=[1,4,5,6,2]
print(sorted(l))
print(max(l))
print(min(l))
print(list(filter(lambda x:x%2,l)))
print(list(map(lambda x:x**2,l)))
l2=[[1,2,3],[4,6,7],[5,8,9]]
print(list(zip(*l2)))
print(any(i%2==0 for i in [7,3,5]))
 