# Chapter 03_04
# 파이썬 튜플
# 튜플 자료형(순서, 중복 o, 수정, 삭제 x) #불변

# 선언

a = ()
b = (1,)
c = (11, 12, 13, 14)
d = (100, 10000, 'Ace', 'Base', 'Captain')
e = (100, 10000, ('Ace', 'Base', 'Captain'))

# 인덱싱
print('>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

print()

# 수정 x

# d[0] = 1500 에러

# 슬라이싱 ~
print('>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

print()

# 튜플 연산
print('>>>>>>')
print('c + d =', c + d)
print('c * 3 =', c * 3)

print()

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a -', a)
print('a -', a.index(3))
print('a -', a.count(2))

print()

# 팩킹 & 언팩킹 (packing, unpacking)

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

print()

# 언팩킹 - 1
(x1, x2, x3, x4) = t


print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)

print()

# 팩킹, 언팩킹
t2 = 1, 2, 3
t3 = (4,)
x1, x2, x3 = t2
x4, x5, x6 = 4, 5, 6
print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)
