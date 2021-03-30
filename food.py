import random
#아래 전체를 반복
for i in range(1,4): 

    print("밥 무러 가자")
    print("메뉴는?")
    # 메뉴 변수 나열
    menulist = '쫄면', '육계장', '비빔밥'
    print("1.쫄면 2. 육계장 3. 비빔밥 4. 랜덤")   
    menu = input(str (i) +  ". 입력: ")    
    # 만약에 사용자가 입력값이 1과 같으면    
    if menu == '1' :
          print("학식 먹어라")
    if menu == '2' :
          print("분식 먹어라")
    if menu == '3' :
          print("중식 먹어라")
    if menu == '4' :
          print("내 마음 대로")
          print (random.choice(menulist))
    #랜덤을 고르면 위 메뉴중에서 아무꺼나
    # 여기까지 반복