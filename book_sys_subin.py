import sys

# 도서 정보를 저장할 딕셔너리 생성 {책: [저자, 분류, 대출가능여부]}
library = { '노인과 바다' : ['헤밍웨이','인문',True], 
           '이기적 유전자' : ['리처드 도킨스','과학',True], 
           '파이썬' : ['박응용','기술',True], 
           '깃허브' : ['박응용', '기술', True], 
           '자바' : ['박응용','기술',True]}

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
        print("\n==== 도서 찾기 ====")
        print("1. 제목으로 찾기")  # 제목으로 도서 검색 옵션
        print("2. 저자 이름으로 찾기")  # 저자 이름으로 도서 검색 옵션
        search_choice = input("검색 기준을 선택하세요 (1 또는 2): ")

        if search_choice == '1':  # 제목으로 검색
            title_1 = input("찾을 도서 제목을 입력하세요: ")
            # 도서 제목이 정확히 일치하는 도서를 찾음 (대소문자 구분하지 않음)
            found_books = [title for title in library if title.lower() == title_1.lower()]
            if found_books:
                for title in found_books:
                    author, category, available = library[title]
                    status = "Available" if available else "Checked Out"
                    print(f"제목: {title}, 저자: {author}, 카테고리: {category}, 상태: {status}") #그냥 다 목록이 나오는데?
            else:
                print("해당 제목을 가진 도서를 찾을 수 없습니다.")
        
        elif search_choice == '2':  # 저자 이름으로 검색
            author_name = input("찾을 저자 이름을 입력하세요: ")
            # 저자 이름이 포함된 도서 제목을 찾음 (대소문자 구분하지 않음)
            found_books = [title for title, (author, _, _) in library.items() if author_name.lower() in author.lower()]
            #리스트 컴프리헨션 사용
            if found_books:
                for title in found_books:
                    author, category, available = library[title]
                    status = "Available" if available else "Checked Out"
                    print(f"제목: {title}, 저자: {author}, 카테고리: {category}, 상태: {status}")
            else:
                print("해당 저자의 도서를 찾을 수 없습니다.")
        else:
            print("잘못된 선택입니다. 다시 시도해주세요.")
    
    # 도서 추가
    elif choice == '1':
        print("\n==== 도서 추가 ====")
        title = input("도서 제목을 입력하세요: ")
        author = input("저자를 입력하세요: ")
        category = input("카테고리를 입력하세요 (인문/과학/예술/기술): ")
        if category not in categories:
            print("잘못된 카테고리입니다.")  # 카테고리가 유효하지 않으면 오류 메시지 출력
        elif title in library:
            print("이미 존재하는 도서입니다.")  # 도서 제목이 이미 존재하면 오류 메시지 출력
        else:
            # 도서 제목을 키로 하고, [저자, 카테고리, 대출 가능 여부]를 값으로 저장
            library[title] = [author, category, True]
            print(f"도서 '{title}'가 추가되었습니다.")  # 도서가 정상적으로 추가되었음을 알림

    # 도서 삭제
    elif choice == '3':
        print("\n==== 도서 삭제 ====")
        title = input("삭제할 도서 제목을 입력하세요: ")
        if title in library:
            del library[title]  # 해당 도서를 삭제
            print(f"도서 '{title}'가 삭제되었습니다.")  # 도서 삭제 완료 메시지
        else:
            print("해당 도서를 찾을 수 없습니다.")  # 도서가 없으면 오류 메시지 출력

    # 도서 수정
    elif choice == '4':
        print("\n==== 도서 수정 ====")
        title = input("수정할 도서 제목을 입력하세요: ")
        if title in library:
            new_author = input("새 저자를 입력하세요: ")
            new_category = input("새 카테고리를 입력하세요 (인문/과학/예술/기술): ")
            if new_category not in categories:
                print("잘못된 카테고리입니다.")  # 잘못된 카테고리 입력 시 오류 메시지
            else:
                # 기존 도서 정보 수정
                library[title][0] = new_author
                library[title][1] = new_category
                print(f"도서 '{title}'가 수정되었습니다.")  # 도서 수정 완료 메시지
        else:
            print("해당 도서를 찾을 수 없습니다.")  # 도서가 없으면 오류 메시지 출력

    # 도서 대출
    elif choice == '5':
        print("\n==== 도서 대출 ====")
        title = input("대출할 도서 제목을 입력하세요: ")
        if title in library:
            if library[title][2]:  # 도서가 대출 가능하면
                library[title][2] = False  # 대출 상태로 변경
                print(f"도서 '{title}'가 대출되었습니다.")  # 대출 완료 메시지
            else:
                print("이미 대출된 도서입니다.")  # 이미 대출된 도서는 대출할 수 없음을 알림
        else:
            print("해당 도서를 찾을 수 없습니다.")  # 도서가 없으면 오류 메시지 출력

    # 도서 반납
    elif choice == '6':
        print("\n==== 도서 반납 ====")
        title = input("반납할 도서 제목을 입력하세요: ")
        if title in library:
            if not library[title][2]:  # 도서가 대출 중이면
                library[title][2] = True  # 반납 상태로 변경
                print(f"도서 '{title}'가 반납되었습니다.")  # 반납 완료 메시지
            else:
                print("이미 반납된 도서입니다.")  # 이미 반납된 도서는 다시 반납할 수 없음을 알림
        else:
            print("해당 도서를 찾을 수 없습니다.")  # 도서가 없으면 오류 메시지 출력

    # 도서 목록 출력
    elif choice == '7':
        print("\n==== 도서 목록 출력 ====")
        if not library:
            print("등록된 도서가 없습니다.")
        else:
            for title, (author, category, available) in library.items():
                status = "Available" if available else "Checked Out"
                print(f"\n제목: '{title}', 저자: {author}, 카테고리: {category}, 상태: {status}")

    elif choice == '8':  # 종료
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 선택입니다. 다시 입력하세요.")
        


