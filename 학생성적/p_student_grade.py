title=["번호",'이름','국어','영어','수학','합계','평균']
Key=["no",'name','kor','eng','math','total','avg']
student=[]
sno=1
#------------------------------------------------------------------------

from p_func_page import *

title=["번호",'이름','국어','영어','수학','합계','평균']
Key=["no",'name','kor','eng','math','total','avg']
student=[]
sno=1


while True:
    main()
    # print("[학생 성적 프로그램]")
    # print("1.성적 입력")
    # print("2.성적 출력")
    # print("3.성적 수정")
    # print()
    choice=int(input("원하는 번호를 입력하세요>>  "))

    if choice==1:
        input()
        # while True:
        #     no=sno
        #     print("[ 학생 성적 입력 ]")
        #     no=input("번호 입력>>  ")
        #     name=input("이름 입력>>  ")
        #     kor=int(input("국어 점수>> "))
        #     eng=int(input("영어 점수>> "))
        #     math=int(input("수학 점수>> "))
        #     total=kor+eng+math
        #     avg=total/3

        #     student.append({"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":total,"agv":avg,})
        #     print("f{name} 학생의 성적이 저장되었습니다.")

    elif choice==2:
        output()
        # print("[학생 성적 출력]")
        # name=input("찾는 학생의 이름을 입력하세요>>  ")
        # print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t".format(*title))
        # if len(student)==0:
        #     print("데이터가 없습니다.")
        # else:
        #     for s in student:
        #         print(f"{s[no]}\t{s[name]}\t{s[kor]}\t{s[eng]}\t{s[math]}\t{s[total]}\t{s[avg]}\t")

    else:
        correction()
        print("[성적 수정]")
        name=input("찾는 학생의 이름을 입력하세요>>  ")
        temp=0
        for i,s in enumerate(student):
            if s['name']==name:
                print(f"찾으시는 {name} 학생의 데이터가 있습니다.")
                temp=1
                break
        if temp==0:
            print(f"{name}의 데이터가 없습니다.")
        elif temp==1:
            print("[수정 과목 선택]")
            print("1.국어   2.영어   3.수학")
            choice=int(input("과목을 선택하세요.>>  "))
            if choice==0:break
            elif choice==1:
                print("[국어 점수 변경]")
                print("현재 국어 점수: ")
            elif choice==2:
                print("[영어 점수 변경]")
                print("현재 영어 점수: ")
            elif choice==3:
                print("[수학 점수 변경]")
                print("현재 수학 점수: ")

    if temp==0:
        print(f"{'name'}의 데이터가 없습니다.")