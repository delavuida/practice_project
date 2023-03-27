# Chapter04_03
# 파이썬 반복문
# While문 실습

# While <expr>:
#    <statement(s)>


# 예제1

n = 5

# while True: 무한 반복문

while n > 0:
    print(n)
    n = n - 1

print()

# 예제2
a = ['foo', 'bar', 'baz']

while a:
    print(a.pop())

print()

# 예제3
# break, continue

n = 5

while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop Ended')

print()

# 예제4
m = 5

while m > 0:
    m -= 1
    if m == 2:
        continue
    print(m)
print('Loop Ended')

print()

# if 중첩

# 예제5

i = 1

while i <= 10:
    print('i :',i)
    if i == 6:
        break
    i += 1

print()

# While - else 구문

# 예제6

n = 10

while n > 0:
    n -= 1
    print(n)
    if n == 5:
        continue
else:
    print('loop out')

print()

# 예제7
a = ['foo', 'bar', 'baz', 'qux']
s = 'kim'

i = 0

while i < len(a):
    if a[i] == s:
        break
    i += 1

else:
    print(s, 'not found in list')

print()

# 예제8
a = ['foo', 'bar', 'baz']

while True:
    if not a:
        break
    print(a.pop())
