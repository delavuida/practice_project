# Chapter06_01
# 파이썬 클래스
# OOP(객체 지향 프로그래밍), self, 인스턴스 메소드, 인스턴스 변수

# 클래스 and 인스턴스 차이 이해
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 접근 가능, 하나를 공유
# 인스턴스 변수 : 객체마다 별도 존재

# 예제1

class Dog: #object 상속
    # 클래스 속성
    species = 'firstdog' # 클래스 변수

    # 초기화/인스턴스 속성
    def __init__(self, name, age): # 인스턴스 변수
        self.name = name
        self.age = age

# 클래스 정보
print(Dog)

# 인스턴스화
a = Dog("mikky", 2)
b = Dog("baby", 3)

# 비교
print(a == b, id(a), id(b))

print()

# 네임스페이스

print('dog1', a.__dict__)
print('dog2', b.__dict__)
        
# 인스턴스 속성 확인
print('{} is {} and {} is {}'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print('{0} is a {1}'.format(a.name, a.species))

print()

print(Dog.species)
print(a.species)
print(b.species)

print()

# 예제2
# self의 이해
class selfTest:
    def func1():
        print('Func1 called')
    def func2(self):
        print(id(self))
        print('Func2 called')


f = selfTest()

# print(dir(f))
print(id(f))
# f.func1() # 예외
f.func2()

selfTest.func1()
#selfTest.func2() # 예외
selfTest.func2(f)

print()

# 예제3
# 클래스 변수, 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0 # 재고

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name
        Warehouse.stock_num += 1
    
    def __del__(self):
        Warehouse.stock_num -= 1


user1 = Warehouse("Lee")
user2 = Warehouse("Cho")

print(Warehouse.stock_num)
# Warehouse.stock_num = 50
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before', Warehouse.__dict__)

print('>>>', user1.stock_num)

print()

del user1
print('after', Warehouse.__dict__)

print()

# 예제4
class Dog: #object 상속
    # 클래스 속성
    species = 'firstdog' # 클래스 변수

    # 초기화/인스턴스 속성
    def __init__(self, name, age): # 인스턴스 변수
        self.name = name
        self.age = age

    def info(self):
        return '{} is {} years old'.format(self.name, self.age)
    
    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성

C = Dog('july', 4)
d = Dog('Marry', 10)

# 메소드 호출
print(C.info())
print(d.info())

# 메소드 호출
print(C.speak('WAL WAL!'))
print(d.speak('Mung Mung!'))