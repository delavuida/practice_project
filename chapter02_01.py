# Chapter02_01
# 파이썬 기초
# 파이썬 기본 출력
# 참초 : https://www.python-course.eu/python3_formatted_output.php

print('python start!')
print("python start!")
print('''python start!''')
print("""python start!""")

print()


# separator 옵션
print('p', 'y', 't', 'h', 'o', 'n', sep='')
print('010','7777','1234', sep='-')
print('python', 'google.com', sep='@')

print()

# end 옵션

print('Welcome to', end=' ')
print('IT News', end=' ')
print('Web Site')

# file 옵션
import sys


print('Learn Python', file = sys.stdout)
print()

# format 사용(d, s, f) / digit, string, float
print('%s %s' % ('one', 'two'))
print('{} {}'.format('one', 'two'))
print('{1} {0}'.format('one', 'two'))

print()

# %s
print('%10s' % ('nice'))
print('{:>10}'.format('nice'))
print('%-10s' % ('nice'))
print('{:10}'.format('nice'))


print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s' % ('nice'))
print('%.5s' % ('pythong study'))
print('{:10.5}'.format('python study')) # 5개만 출력

print()

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

print()

# %f

print('%f' % (3.1421513512))
print('{:f}'.format(3.1421513512))


print('%06.2f' % (3.141592653589793))
print('{:06.2f}'.format(3.141592653589793))

# 1