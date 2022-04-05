# 숫자
student_number = 2214
age = 18
height = 165.4

# 문자
name = '임정훈'

print(f'학번 : {student_number}\n이름 : {name}\n나이 : {age}\n키 : {height}')  # 학번 : 2214


print(type(student_number))  # <class 'int'>
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(height))  # <class 'float'>
print(type(10.27))  # <class 'int'>
print(type('1027'))  # <class 'str'>
print(10 / 27)  # java : 0, python : 0.37037037037037035
print(27 / 10)  # java : 2, python : 2.7
print(27 // 10)  # python : 나눈 몫 : 2
print(27 % 10)  # python : 나눈 몫 : 7
print(type(10 / 27))  # <class 'float'>
print(type(27//5))   # <class 'int'>
print(type(27 % 10))   # <class 'int'>
print(20 / 10)   # python : 나눈 몫 : 2.0
print(type(20 / 10))   # <class 'float'>

#변수 이름 규칙, 자료형변환
#my_mbti, my_function(), MyClass #myMbti : camel-case, my_mbti : snake-case

my_mbti = 'INTP'

print(f'My MBTI : {my_mbti}')

#print('My MBTI'+my_mbti+'age : '+age)   #java : String.toString(age); python: str(age)
print('My MBTI'+my_mbti+', age : '+str(age))
height = '165.2'
print(float(height) + 10)   #java : Float.parseFloat(height);, python : float(height)

#str(), int(), float(): 자료형변환 함수
#+연산자 : 숫자 숫자 : 덧셈, 문자+문자 => 문자문자
print(18 + 2)   #20
print('18'+'2') #'182'
print(18 * 2)   #36
print('2' * 3)  #'2222'

#짝을 10번 출력
print('짝'*10)
#print('짝'*'10')

print(18 ** 3)

