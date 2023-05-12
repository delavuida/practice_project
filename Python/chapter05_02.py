# Chapter05_02
# 파이썬 사용자 입력
# input 사용법
# 기본 타입(str)

# 예제1
name = input("Enter your Name :")
grade = input("Enter your Grade :")
company = input("Enter your Company Name :")

print(name, grade, company)

print()

# 예제2
number = input("Enter Number :")
name = input("Enter Name :")

print("Type of number", type(number))
print("Type of name", type(name))

print()

# 예제3 (계산)
first_number = int(input("Enter number :"))
second_number = int(input("Enter number2 :"))

total = first_number + second_number
print("first_number + second_ number =", total)

print()

# 예제4
float_number = float(input("Enter float number :"))

print("input float :", float_number)
print("input type : ", type(float_number))

print()

# 예제5
print("FisrtName - {0}, LastName - {1}".format(input("Enter first name :"), input("Enter second name :")))

print()
