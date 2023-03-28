# Chapter02_01
# 파이썬 기초
# 파이썬 기본 출력 (2023년 추가)
# 파이썬 3가지 print formatting


"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\000 : 널 문자

"""

### 3가지 format practices

x = 50
y = 100
text = 308276567
n = 'Lee'

# 예제1 출력1
ex1 = 'n = %s, s = %s, sum = %d' %(n, text, (x + y))
print(ex1)

print()

# 예제2 출력2
ex2 = 'n = {n}, s = {s}, sum = {sum}'.format(n = n, s = text, sum = x + y)
print(ex2)

print()

# 예제3 출력3
ex3 = f'n = {n}, s = {text}, sum = {x + y}'
print(ex3)

print()

# 구분기호
# 예제4

m = 100000000

print(f'm : {m:,}')

print()

# 정렬 ^ : 가운데 정렬, < : 왼쪽 정렬, > 오른쪽 정렬
# 예제5

t = 20

print(f"t : {t:10}")
print(f"t center : {t:^10}")
print(f"t left : {t:<10}")
print(f"t right : {t:>10}")

print()

print(f"t center : {t:-^10}")
print(f"t center : {t:#<10}")