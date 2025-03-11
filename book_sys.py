# 도서 정보를 저장할 딕셔너리 생성
library = {}

categories = ['인문', '과학', '예술', '기술']

while True:
    print("\n==== 도서 관리 시스템 ====")
    print("1. 도서 추가")
    print("2. 도서 찾기")
    print("3. 도서 삭제")
    print("4. 도서 수정")
    print("5. 도서 대출")
    print("6. 도서 반납")
    print("7. 도서 목록 출력")
    print("8. 종료")

    choice = input("원하는 작업을 선택하세요 (1-8): ")

    if choice == '1':  # 도서 추가
        title = input("도서 제목을 입력하세요: ")
        author = input("저자를 입력하세요: ")
        category = input("카테고리를 입력하세요 (인문/과학/예술/기술): ")
        if category not in categories:
            print("잘못된 카테고리입니다.")
        elif title in library:
            print("이미 존재하는 도서입니다.")
        else:
            library[title] = [author, category, True]
            print(f"도서 '{title}'가 추가되었습니다.")

    elif choice == '2':  # 도서 찾기
        title = input("찾을 도서 제목을 입력하세요: ")
        if title in library:
            author, category, available = library[title]
            status = "Available" if available else "Checked Out"
            print(f"제목: {title}, 저자: {author}, 카테고리: {category}, 상태: {status}")
        else:
            print("해당 도서를 찾을 수 없습니다.")

    elif choice == '3':  # 도서 삭제
        title = input("삭제할 도서 제목을 입력하세요: ")
        if title in library:
            del library[title]
            print(f"도서 '{title}'가 삭제되었습니다.")
        else:
            print("해당 도서를 찾을 수 없습니다.")

    elif choice == '4':  # 도서 수정
        title = input("수정할 도서 제목을 입력하세요: ")
        if title in library:
            new_author = input("새 저자를 입력하세요: ")
            new_category = input("새 카테고리를 입력하세요 (인문/과학/예술/기술): ")
            if new_category not in categories:
                print("잘못된 카테고리입니다.")
            else:
                library[title][0] = new_author
                library[title][1] = new_category
                print(f"도서 '{title}'가 수정되었습니다.")
        else:
            print("해당 도서를 찾을 수 없습니다.")

    elif choice == '5':  # 도서 대출
        title = input("대출할 도서 제목을 입력하세요: ")
        if title in library:
            if library[title][2]:
                library[title][2] = False
                print(f"도서 '{title}'가 대출되었습니다.")
            else:
                print("이미 대출된 도서입니다.")
        else:
            print("해당 도서를 찾을 수 없습니다.")

    elif choice == '6':  # 도서 반납
        title = input("반납할 도서 제목을 입력하세요: ")
        if title in library:
            if not library[title][2]:
                library[title][2] = True
                print(f"도서 '{title}'가 반납되었습니다.")
            else:
                print("이미 반납된 도서입니다.")
        else:
            print("해당 도서를 찾을 수 없습니다.")

    elif choice == '7':  # 도서 목록 출력
        if not library:
            print("등록된 도서가 없습니다.")
        else:
            for title, (author, category, available) in library.items():
                status = "Available" if available else "Checked Out"
                print(f"제목: '{title}', 저자: {author}, 카테고리: {category}, 상태: {status}")

    elif choice == '8':  # 종료
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못된 선택입니다. 다시 입력하세요.")
