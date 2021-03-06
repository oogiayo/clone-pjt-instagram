# Clone-Project - Instagram*



## 1. 프로젝트 설명

> 2020.09.30~ 추석 연휴간, 그동안 학습한 Django 기능을 활용하여 인스타그램 웹사이트를 클론코딩 프로젝트를 진행

- Project 참여자 : `김동욱(Donguk Kim)` 



## 2. Instagram 기능 설명

---

#### [유저관련 기능]

---

1. 기본 인증 & 권한 기능 (로그인, 회원가입, 로그아웃, 회원탈퇴, 회원정보 수정 등)
2. 프로필 페이지
   - User 프로필 이미지
   - 자기소개
3. 팔로우



---

#### [포스팅 기능]

---

1. 이미지 업로드 (media)
2. 작성자
3. 좋아요 (M:N)
4. 해쉬태그(Hashtag) = 글내용 대체 (M:N)



---

#### [댓글 기능]

----

1. 댓글 작성
2. @멘션 기능 => Optional



---

#### [검색 기능]

---

1. 포스팅 검색 기능
2. 유저 검색 기능
3. 해쉬태그 검색 기능





## 3. 개발 과정

---

#### [개발 계획]

---

![image-20200930120643598](README.assets/image-20200930120643598.png)

- `Trello`의 칸반보드를 활용한 개발 Sprint 내용 수시 확인 및 점검 : https://trello.com/



---

#### [데이터베이스 모델링]

---

![image-20200930115445388](README.assets/image-20200930115445388.png)

- DB 모델링에 사용한 Tool : `erdcloud` (https://www.erdcloud.com/)





## 4. 구현 결과사진

---

#### [유저관련 기능]

---

1. 기본 인증 & 권한 기능 (로그인, 회원가입, 로그아웃, 회원탈퇴, 회원정보 수정 등)

   > 기본적으로 내비게이션 바에 기능을 구축해놓았으며, 프로필 페이지에서도 편집이 가능하다.

   - 회원가입 페이지

     ![image-20201003221506933](README.assets/image-20201003221506933.png)

     

   - 내비게이션 바의 회원정보 수정 & 프로필 이동 & 로그아웃 기능

     ![image-20201003221635011](README.assets/image-20201003221635011.png)

     

   

2. 프로필 페이지

   > User 프로필 이미지 & 자기소개 & 팔로우 기능

   ![image-20201003215608218](README.assets/image-20201003215608218.png)

   

   



---

#### [포스팅 기능]

---

0. 메인 화면

   ![image-20201003234610489](README.assets/image-20201003234610489.png)

   ![image-20201003233353644](README.assets/image-20201003233353644.png)



1. 이미지 업로드 (media)

   ![image-20201003213920031](README.assets/image-20201003213920031.png)

   

2. 게시물 세부 페이지 & 댓글 기능

   ![image-20201003235646033](README.assets/image-20201003235646033.png)



3. 게시글 수정 및 삭제 기능
   - 내 게시글에만 수정/삭제 가능!



---

#### [댓글 기능]

----

1. 댓글 작성 => 구현 OK
2. @멘션 기능 => Optional  __(NOT Yet)__



---

#### [검색 기능]

---

1. 검색 기능

   - 해쉬태그(#word)를 검색하여 관련 포스팅 모아보기

     > 내비게이션 바의 검색창에 # + 단어를 검색하면 해쉬태그 검색이 가능하며 관련 포스팅 목록을 펼쳐본다.

      ![image-20201003221258880](README.assets/image-20201003221258880.png)

     

   - 유저 검색

     > 내비게이션 바의 검색창에 #을 붙이지 않고 검색하면 유저 검색이 가능하며, 해당 유저의 프로필 페이지로 이동한다.

     ![image-20201003221140583](README.assets/image-20201003221140583.png)

     

   - 검색 실패 페이지

     ![image-20201003220710429](README.assets/image-20201003220710429.png)





## 6. 개선 및 추가개발 예정 기능

---

#### [하나의 게시글에 여러 이미지를 업로드하는 기능]

---

- 모델링 수정
  - 이미지 클래스를 하나 생성하고, 포스트(게시글) 클래스와 1:N 관계를 형성하는 것으로 계획중.





---

#### [Front-end 개선]

---

- 아직 기본적인 Bootstrap 기능들만 사용하느라 프론트에서 미숙한 부분이 많다. 특히 sizing 처리에서 어려움을 겪고 있으므로 조금 더 공부해서 개선할 계획.

- 인스타그램의 Clone으로 시작했으나 점차 디자인하고 바꿔나갈 계획.





---

#### [Direct Message 기능]

---









## 7. 새로 배운 것 & 어려웠던 점 + 해결 방법



---

#### [댓글 작성날짜 (ex. OO시간 전) 구현 과정 문제 해결]

---

> 처음에는 |timesince 사용해서 구현했다. 	ex) {{ comment.created_at|timesince }} 전 
>
> BUT )  1시간이 넘어가면 OO시간, OO분  => 이렇게 조금 지저분하게 나오는 문제가 있었다



#### #1 첫 번째 시도

-  template 내에서 필터를 2번 붙여서 사용할 수 있지 않을까??

  -  |date:'~~~'|timesince 이런식으로 섞어서 사용하고싶었는데, 원래 안되는지 내가 잘못했는지 잘 안됐다.

  



#### #2 두 번째 시도

- __Django 사용자 정의 필터(Custom Template Filter)__를 정의해서 구현성공!!!!!

  

1. Application 폴더(posts) 내부에 `templatetags` 패키지 폴더를 만든다.

   - Django가 패키지 폴더로 인식해야하므로 폴더 내부에 `__init.py__`의 빈파일을 만들어서 패키지로 명시한다.

   - 주의) `templatetags` 패키지를 추가하면 서버 재시작해야 적용됨

     

2. `templatetags` 폴더 내부에 원하는 이름의 .py 파일을 만든다.

   - 나는 `custom_filter.py`로 만들었다.

   - 해당 Application 폴더의 구조는 다음과 같다.

     ```
     # Application 폴더 구조
     posts/
         templatetags/
             __init__.py
             custom_filter.py
     ```

   - `custom_filter.py` 파일의 기본 형태는 다음과 같다.

     ```python
     from django import template
     
     register = template.Library()
     ```

   - 여기서 register는 유효한 tag library를 만들기 위한 모듈수준의 인스턴스 객체이다.

   

 3. 내가 원하는 함수를 정의해준다.

    - `@register.filter` 데코레이터를 함수에 붙여줘야 한다.

    - 내가 다루려고 하는 Difference of Datetime은 `datetime.timedelta` 타입의 데이터 형태이고, 현재 시각이 필요하므로 `timezone`  모듈을 불러와서 사용한다.

      ```python
      from django import template
      from django.utils import timezone
      
      register = template.Library()
      
      @register.filter
      def processed_timesince(value):
          dif = int((timezone.now() - value).seconds)
          unit = {'초': 60, '분': 60, '시간': 24, '일': 31, '달': 12}
          for key, val in unit.items():
              if dif//val == 0:
                  return str(dif) + key
              else:
                  dif //= val
          return str(dif) + '년'
      ```

    





- 앵커태그 활용 => (좋아요 누른 후 원하는 위치에 redirect)



- front

  ```
  Grid system
  ```

  ```
  Hover (마우스 오버 효과)
  
  Transition
  ```

  ```
  Django에서 static file (css,img 사용하기)
  
  django는 모듈화가 잘된건지. 웹개발에 최적화 된건지
  여하간, tomcat처럼 디렉토리에 이미지나 CSS를 넣는다고 찾아지지 않는다.
  
  (html) templates 처럼 특정 디렉토리를 생성하고 setting.py 파일에 지정해줘야 한다
  setting.py에서
  STATIC_URL = '/static/' 해주고
  
  각 app 디렉토리 밑에 /static이란 디렉토리를 만들어준다.
  사용할 때는 load staticfiles를 불러준후에 경로를 다음과 같이 지정해주면 된다.
  {% load staticfiles %}
  <img src="{% static "img/logo_nav.png" %}">
  
  출처: https://bcho.tistory.com/821 [조대협의 블로그]
  ```





- modeling

  ```
  imageField
  ```

  ```
  Hashtag?
  모델링은 M:N 했는데 구현이 어렵다
  ```

  ```
  처음에 설계를 제대로 안해놓으니까 구현방법이 왔다갔다? 
  a태그에 query string 넣고싶은데 => 그냥 함수 하나 더 만들었음...!
  ```

  



- `.json` 파일로 dumpdata할 때 이모티콘이 있으면 Error가 떴다. => 따로 인코딩 명령어 커스터마이징 필요

  ```
  CommandError: Unable to serialize database: 'cp949' codec can't encode character '\U0001f311' in position 24: illegal multibyte sequence
  Exception ignored in: <generator object cursor_iter at 0x00000267A0DFD248>
  Traceback (most recent call last):
    File "C:\Users\dongu\Desktop\clone-pjt\venv\lib\site-packages\django\db\models\sql\compiler.py", line 1602, in cursor_iter
      cursor.close()
  sqlite3.ProgrammingError: Cannot operate on a closed database.
  ```







