'''
202195057 손패택
컴퓨터학부
'''
# 문자열
name = '김지연'     # 문자열을 변수에 저장.

# 리스트
city = ['서울시', 800, '부산시', 400]   # 리스트 생성.

# 튜플
num = (100, 200, 300, 400)  # 튜플 생성.

'''
1. 인덱싱(indexing)
    순차적인 자료구조에 인덱스(첨자) 값을 가지고 접근할 수 있는 기능
    인덱스는 0번지부터 시작한다.
[i] => i번지 값.
'''
# 문자열에서 첫 번째 문자를 변수에 저장.
surName = name[0]
print("name[0] : ", surName)

# 리스트의 마지막에서 두 번째 요소 출력.
print("city[-2] : ", city[-2])

# 리스트의 마지막에서 네 번째 요소의 값을 변경.
# 서울시 -> 서울특별시 변경 => 변수에 값을 새로 저장.
city[-4] = '서울특별시'
print("city : ", city)

# 튜플의 여섯 번째 요소(5번지) 값 출력
# IndexError: tuple index out of range
# 5번지 값은 없어서 오류가 발생한다.
#print("num[5] : ", num[5])

'''
2. 슬라이싱(slicing)
    시퀀스 자료형애에서 일부를 잘라내어 동일한 자료형으로 반환하는 기능.
[start : stop : step] 
    => start에서 시작해서 stop 이전까지 step 간격으로 추출
'''
# name 변수에 있는 문자열의 1번지부터 2번지까지 잘라서 변수에 저장.
giveName = name[1:3]
print("name[1:3] : ", giveName)  # 성 빼고 이름만 출력된다.

# city 리스트의 세 번째 요소부터 끝까지 출력
print("city[2:] :", city[2:])

# num 튜플의 두 번째 요소부터 세 번째 요소까지 출력.
print("num[1:3] :", num[1:3])

# num 튜플의 처음부터 끝까지 2씩 증가하면서 슬라이싱하여 출력.
print("num[::2] :", num[::2])

# 인덱스 범위가 벗어나도 가능한 값만 자동 슬라이싱 된다.
print("num[-10:10] :", num[-10:10])

'''
3. 연결 
    + 연산자를 사용하여 두 개의 자료를 연결하여 샐운 시퀀스 자료형을 만드는 기능
자료형 + 자료형
'''
text1 = 'I Like '
text2 = text1 + 'Python Language'
print("text1 + 문자열 = ", text2)

num1 = (1,2,3,4,5)
num2 = (6,7,8,9)
num = num1 + num2   # 두 개의 튜플을 합쳐서 새로운 자료 생성.
print("num1 + num2 = ", num)

# TypeError: can only concatenate tuple (not "list") to tuple
# 서로 다른 자료형은 연결 할 수 없다.
#result = num1 + city        # 튜플 + 리스트
#print("num1 + city = ", result)

'''
4. 반복
    * 연산자를 사용하여 시퀀스 자료형을 원하는 만큼 반복하는 기능.
자료형 * 반복 횟수
'''
language = ('C', 'JAVA', 'Python')  # 튜플 생성.
languages = language * 3       # language를 3번 반복하여 변수에 저장.
print("languages = ", languages)

feel = 'happy. ' * 10   # 문자열 10번 반복하여 변수에 저장.
print("feel = ", feel)

contury = ['대한민국'] * 10   # 리스트의 내용을 10번 반복하여 변수에 저장.
print("contury = ", contury)

'''
5. 멤버 유무 검사
    시퀀스 자료형에서 특정 자료가 있는지 알려주는 기능
자료 in 자료형
'''
# 색상 리스트 생성.
color = ['red', 'green', 'blue', 'yellow']
print("리스트에 'black'이 있나요? ", 'black' in color)
print("리스트에 'red'가 있나요? ", 'red' in color)

text3 = 'Python'
print("문자열에 't'가 있나요? ", 't' in text3)
print("문자열에 소문자 'p'가 있나요? ", 'p' in text3)
print("문자열에 대문자 'P'가 있나요? ", 'P' in text3)

# in 연산자는 for 반복문에서 효율적으로 사용할 수 있다.
for i in text3 :   # text3안에 있는 문자열을 하나씩 i 변수에 넣어서 반복.
    print(i)
    
'''
6. 길이 정보
    len() 내장함수를 이용하여 시퀀스 자료형의 길이를 알 수 있다.
len(자료형)
'''
# 문자열 text2의 길이 => 띄어쓰기도 길이에 포함.
print("문자열 text2의 길이 : ", len(text2))

# 리스트 city의 길이
print("리스트 city의 길이 : ", len(city))