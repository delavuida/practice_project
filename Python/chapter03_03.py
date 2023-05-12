# chapter03_03
# 파이썬 리스트
# 리스트 자료형 (순서, 중복, 수정, 삭제 O)


# 선언
a = []
b = list()
c = [70, 75, 80, 85] #len
d = [1000, 10000, "Ace", "Bace", "Captain"]
e = [1000, 10000, ["Ace", "Bace", "Captain"]]
f = [21.42, "foobar", 3, 4, False, 3.141592]


# 인덱싱
print(">>>>>>")
print("d : ", type(d), d)
print("d : ", d[1])
print("d : ", d[0] + d[1] + d[1])
print("d : ", d[-1])
print("e : ", e[-1][1])
print("e : ", list(e[-1][1]))

print()

# 슬라이싱
print(">>>>>")
print("d : ", d[0:3])
print("d : ", d[2:])
print("e : ", e[-1][1:3])

print()

# 리스트 연산
print(">>>>>")
print("c + d", c + d)
print("c * 3", c * 3)
print("'Test' + c[0]", 'Test' + str(c[0]))

print()

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])

print()

# Identity(id)

temp = c
print(temp, c)
print(id(temp))
print(id(c))

print()

# 리스트 수정, 삭제
print(">>>>>>")
c[0] = 4
print("c : ", c)
print(len(c))

c[1:2] = [['a', 'b', 'c']]
print("c : ", c)
print(len(c))

c[1:2] = ['a', 'b', 'c']
print("c : ", c)
print(len(c))

c[1] = ['a', 'b', 'c']
print("c : ", c)
print(len(c))

c[1:3] = []
print("c : ", c)
print(len(c))

del c[2] # 삭제
print("c : ", c)
print(len(c))

print()

#리스트 함수
a = [5, 2, 3, 1, 4]

print("a : ", a)

a.append(10) # 원소 추가
print("a : ", a)

a.sort()
print("a : ", a) # 원소 정렬

a.reverse()
print("a : ", a) # 역 정렬

print("a : ", a.index(3), a[3]) # 지정 원소 호출

a.insert(2, 7) # 2번 인덱스에 7을 삽입
print("a : ", a)

a.reverse()
print("a : ", a) # 역 정렬

# del a[6]
# print("a : ", a)

a.remove(10)
print("a : ", a)

print("a : ", a.pop())
print("a : ", a)

print("a : ", a.pop(0))
print("a : ", a)

print("a : ", a.count(4)) # 4라는 값이 리스트안에 몇개가 있는지 확인하는 함수

ex = [8,9]
a.extend(ex)
print("a : ", a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    data = a.pop()
    print(data)
