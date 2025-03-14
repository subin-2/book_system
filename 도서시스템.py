import sys
import book_func as bf

# 도서 정보를 저장할 딕셔너리 생성 {책: [저자, 분류, 대출가능여부]}
# library = { 'apple' : ['헤밍웨이','인문',True], 
#            '이기적 유전자' : ['리처드 도킨스','과학',True], }

filename = 'book_sys.json'
library = bf.book_load(filename)

# 카테고리 목록 (도서 카테고리로 '인문', '과학', '예술', '기술'을 사용)
categories = ['인문', '과학', '예술', '기술']

# 메인 루프: 프로그램을 종료할 때까지 반복
while True:
    # 메뉴 출력
    print("\n==== 도서 관리 시스템 ====")
    print("1. 도서 추가")
    print("2. 도서 찾기")
    print("3. 도서 삭제")
    print("4. 도서 수정")
    print("5. 도서 대출")
    print("6. 도서 반납")
    print("7. 도서 목록 출력")
    print("8. 종료")

    # 사용자 입력 받기
    choice = input("원하는 작업을 선택하세요 (1-8): ")

    # 도서 찾기
    if choice == '2':
        bf.book_search(library)
    
    # 도서 추가
    elif choice == '1':
        bf.book_input(library, categories)
    
    # 도서 삭제
    elif choice == '3':
        bf.book_delete(library)

    # 도서 수정
    elif choice == '4':
        bf.book_update(library, categories)

    # 도서 대출
    elif choice == '5':
        bf.book_borrow(library)

    # 도서 반납
    elif choice == '6':
        bf.book_return(library)

    # 도서 목록 출력
    elif choice == '7':
        bf.book_list(library)

    elif choice == '8':  # 종료
        print("프로그램을 종료합니다.")
        bf.book_save(library,filename)
        break

    else:
        print("잘못된 선택입니다. 다시 입력하세요.")
        
