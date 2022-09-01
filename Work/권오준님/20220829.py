import random  # random 모듈

def 판정(self, enemy): # 판정 함수 정의
    if self=='묵':
        if enemy=='묵':
            승패='비김'
        elif enemy=='찌':
            승패='이김'
        else:
            승패='짐'
        
    elif self=='찌':
        if enemy=='묵':
            승패='짐'
        elif enemy=='찌':
            승패='비김'
        else:
            승패='짐'
        
    elif self=='빠':
        if enemy=='묵':
            승패='이김'
        elif enemy=='찌':
            승패='짐'
        else:
            승패='짐'
     
    return 승패    # 승패는 '나'의 기준으로 작성됨 / 가위바위보 결과를 '승패'의 변수에 반환함.

승패 = '비김'
묵찌빠 = ['묵','찌','빠']

while 승패 == '비김':          # 비겼을 때 실행 / 이기거나 졌을 경우 실행 x
    print("\"가위바위보!\"\n") # 추가
    self = input('나 : ')
    if self not in 묵찌빠 :       # 가위바위보 잘못 했을 때 / 멤버쉽(포함?) 연산자 (in / not in)
        print("다시 하세요!")     # 비겼을 때 뿐 아니라 나머지 경우의 오류도 처리하기엔 너무복잡...
        print("-----------------------------------\n")
        continue
    enemy = random.choice(묵찌빠)  # '묵찌빠'의 요소들 중 하나를 무작위로 뽑음
    print("상대 :",enemy)
    승패 = 판정(self, enemy)
    if 승패 == '비김':
        print("가위바위보에서 비겼습니다.")
        print("-----------------------------------\n")


while 승패 != '비김':  # 이기거나 졌을 때 반복 실행
    
    if 승패 == '이김':        
        print("당신이 가위바위보에서 이겼습니다.")
        print("-----------------------------------\n")  # 추가
        print("\"가위바위보!\"\n")        
    else:
        print("상대가 가위바위보에서 졌습니다.")
        print("-----------------------------------\n")  # 추가
        print("\"가위바위보!\"\n") 
        
    전판 = 승패    # 가위바위보의 결과(이기거나 졌을 때)를 전판에 대입
        
    self = input('나 : ')
    enemy = random.choice(묵찌빠)
    print("상대 :",enemy)
    승패 = 판정(self, enemy)

if 전판 == '이김':  
    print("묵찌빠 게임을 이겼습니다.")
else: 
    print("묵찌빠 게임에서 졌습니다.")
    
    
