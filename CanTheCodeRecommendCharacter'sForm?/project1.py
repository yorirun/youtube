
#DO NOT REUPLOAD OR CHANGE THIS CODE, IF YOU WANT TO DO SOMETHING WITH MY CODE,
  #PLEASE ASK TO ME!
#재배포혹은 코드의 수정은 허락하지않은 사항입니다, 이 코드를 사용해서 무언가 하고싶다면,
  #사전에 제게 허락을 받아주세요!


import random as rn #randrange!!! n+1 -- 난수 생성위해 불러온 모듈


#캐릭터의 스타일 파티션(역할) 분할 //Print random number
head1 = rn.randrange(1,4) #머리카락의 전반적인 길이 : hair1
head2 = rn.randrange(11,14) #머리카락 성질 (ex) 직모) :hair2
head3 = rn.randrange(14,25) #추가 스타일 : hair style3
#
eye = rn.randrange(25,35) #눈 스타일 :eye
#
stature = rn.randrange(36,39) #키 설정(외형) :stature(tall)
#
tribe = rn.randrange(41,49) #종족값설정 :form of tribe
#
sopum1 = rn.randrange(50,59) #외형적인 소품 ex)안경 등 :item1
sopum2 = rn.randrange(60,69) #옷 스타일 :item2
sopum3 = rn.randrange(70,79) #들고있는 소품 :item3
#
c0lor = rn.randrange(80,108)


#if구문으로 단어와 생성된 난수(random값) 대응하게 만들기 //Set random number to word

#head1
if head1 == 1:
    print("머리길이: 장발") #long hair
if head1 == 2:
    print("머리길이: 중발") #middle size(?) hair :(long + short)hair divide 2
if head1 == 3:
    print("머리길이: 단발") #short hair
#head2
if head2 == 11:
    print("머리형태: 직모") #straight
if head2 == 12:
    print("머리형태: 반곱슬") #half curly
if head2 == 13:
    print("머리형태: 곱슬머리") #culry
#head3
if head3 == 14:
    print("머리형태2: 가르마0") #hair part
if head3 == 15:
    print("머리형태2: 일자") #straight
if head3 == 16:
    print("머리형태2: 더벅머리") #messy hair
if head3 == 17:
    print("머리형태2: ^자 머리") #hair looks like ^
if head3 == 18:
    print("머리형태2: 깻잎머리") #hair part --> 7:3
if head3 == 19:
    print("머리형태2: 트윈테일") #twintail
if head3 == 20:
    print("머리형태2: 포니테일") #ponytail
if head3 == 21:
    print("머리형태2: 땋은 머리") #braid(hair)
if head3 == 22:
    print("머리형태2: 올 백") #combed back hair
if head3 == 23:
    print("머리형태2: 넘긴머리") #side swept hair
if head3 == 24:
    print("머리형태2: 투톤") #ombre hair
#eye
if eye == 25:
    print("눈 형태: 평범한 눈") #normal
if eye == 26:
    print("눈 형태: 올라간 눈") #little upper
if eye == 27:
    print("눈 형태: 처진 눈") #little down
if eye == 28:
    print("눈 형태: 실눈") #eye looks like - - or ^ ^
if eye == 29:
    print("눈 형태: 동태눈") #empty eye(?) --> vacuity
if eye == 30:
    print("눈 형태: 머리카락에 가려짐") #can't find eyes, because hair is too long
if eye == 31:
    print("눈 형태: 삼백안") #三白眼: three part is white(I didn't find word)
if eye == 32:
    print("눈 형태: 반쯤 감은 눈") #heavy lidded eyes
if eye == 33:
    print("눈 형태: 도끼눈") #An eye looks like STARING
if eye == 34:
    print("눈 형태: 고양이눈") #cay's eye --> (|).(|)
#stature
if stature == 36:
    print("외형: 어린이") #kid
if stature == 37:
    print("외형: 청소년") #teen-ager
if stature == 38:
    print("외형: 성인") #adult
#tribe
if tribe == 41:
    print("종족값: 사람") #human
if tribe == 42:
    print("종족값: 수인") #animal human
if tribe == 43:
    print("종족값: 용족") #draonoid
if tribe == 44:
    print("종족값: 언데드") #undead
if tribe == 45:
    print("종족값: 화인(꽃+인간)") #flower human
if tribe == 46:
    print("종족값: 흡혈귀") #vampire
if tribe == 47:
    print("종족값: 요정") #fairy
if tribe == 48:
    print("종족값: 마족") #devil
#sopum
'''1'''
if sopum1 == 50:
    print("소품: 오드아이(렌즈)") #odd eye
if sopum1 == 51:
    print("소품: 마법사의 모자") #magician's hat (sharp)
if sopum1 == 52:
    print("소품: 마술사의 모자") #magician's hat ( _ㅁ_ )
if sopum1 == 53:
    print("소품: 야구모자") #cap
if sopum1 == 54:
    print("소품: 검정색 안경") #glasses (black)
if sopum1 == 55:
    print("소품: 은색 안경") #glasses (white)
if sopum1 == 56:
    print("소품: 귀걸이") #earring
if sopum1 == 57:
    print("소품: 학사모") #Mortarboard
if sopum1 == 58:
    print("소품: 베레모") #beret

'''2'''
if sopum2 == 60:
    print("소품2: 파카") #parka
if sopum2 == 61:
    print("소품2: 티셔츠") #T-shirt
if sopum2 == 62:
    print("소품2: 터틀넥") #turtle neck
if sopum2 == 63:
    print("소품2: 맨투맨") #sweat shirt
if sopum2 == 64:
    print("소품2: 스웨터") #sweater
if sopum2 == 65:
    print("소품2: 나시") #tanktop
if sopum2 == 66:
    print("소품2: 코트") #coat
if sopum2 == 67:
    print("소품2: 더플코트") #duffle coat
if sopum2 == 68:
    print("소품2: 드레스") #dress

'''3'''
if sopum3 == 70:
    print("소품3: 시계") #watch (clock)
if sopum3 == 71:
    print("소품3: 연필") #pencil
if sopum3 == 72:
    print("소품3: 클라리넷") #clarinet
if sopum3 == 73:
    print("소품3: 책") #book
if sopum3 == 74:
    print("소품3: 손에드는 음식") #food that can hold
if sopum3 == 75:
    print("소품3: 마이크") #microphone
if sopum3 == 76:
    print("소품3: 휴대폰") #cellphone
if sopum3 == 77:
    print("소품3: 칼") #knife
if sopum3 == 78:
    print("소품3: 망치") #hammer
#c0lor (well.. if you want to know that color.. maybe copy the color.., it'll be the best way)
if c0lor == 80:
    print("기본색깔: 빨강")
if c0lor == 81:
    print("기본색깔: 주황")
if c0lor == 82:
    print("기본색깔: 연주황")
if c0lor == 83:
    print("기본색깔: 연갈색")
if c0lor == 84:
    print("기본색깔: 노란갈색")
if c0lor == 85:
    print("기본색깔: 어두운갈색")
if c0lor == 86:
    print("기본색깔: 갈색")
if c0lor == 87:
    print("기본색깔: 연귤색")
if c0lor == 88:
    print("기본색깔: 귤색")
if c0lor == 89:
    print("기본색깔: 노랑")
if c0lor == 90:
    print("기본색깔: 연노랑")
if c0lor == 91:
    print("기본색깔: 연초록")
if c0lor == 92:
    print("기본색깔: 어두운초록")
if c0lor == 93:
    print("기본색깔: 초록")
if c0lor == 94:
    print("기본색깔: 연청록")
if c0lor == 97:
    print("기본색깔: 군청색")
if c0lor == 98:
    print("기본색깔: 파랑")
if c0lor == 99:
    print("기본색깔: 연남색")
if c0lor == 100:
    print("기본색깔: 남색")
if c0lor == 101:
    print("기본색깔: 보라")
if c0lor == 102:
    print("기본색깔: 자주색")
if c0lor == 103:
    print("기본색깔: 연회색")
if c0lor == 104:
    print("기본색깔: 회색")
if c0lor == 105:
    print("기본색깔: 검정")
if c0lor == 106:
    print("기본색깔: 은색")
if c0lor == 107:
    print("기본색깔: 금색")
          #by chanpercent (developer account: yorirun)
