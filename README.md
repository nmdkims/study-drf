## 6/17 여섯번째 과제 설명 WIP
1. product 앱에서 <작성자, 썸네일, 상품 설명, 등록일자, 노출 종료 일자, 가격, 수정 일자, 활성화 여부>가 포함된 product 테이블을 생성해주세요
2. django serializer를 사용해 validate / create / update 하는 기능을 구현해주세요
    1. custom validation 기능을 사용해 노출 종료 일자가 현재보다 더 이전 시점이라면 상품을 등록할 수 없도록 해주세요
    2. custom creator 기능을 사용해 상품 설명의 마지막에 “<등록 일자>에 등록된 상품입니다.” 라는 문구를 추가해주세요
    3. custom update 기능을 사용해 상품이 update 됐을 때 상품 설명의 가장 첫줄에 “<수정 일자>에 수정되었습니다.” 라는 문구를 추가해주세요
3. product 앱에서 <작성자, 상품, 내용, 평점, 작성일>을 담고 있는 review 테이블을 만들어주세요
4. 현재 날짜를 기준으로, 노출 종료 날짜가 지나지 않았고 활성화 여부가 True이거나 로그인 한 사용자가 등록 한 상품들의 정보를 serializer를 사용해 리턴해주세요
5. 4번 상품 정보를 리턴 할 때 상품에 달린 review와 평균 점수를 함께 리턴해주세요
    1. 평균 점수는 (리뷰 평점의 합/리뷰 갯수)로 구해주세요
    2. 작성 된 리뷰는 모두 return하는 것이 아닌, 가장 최근 리뷰 1개만 리턴해주세요
6. 로그인 하지 않은 사용자는 상품 조회만 가능하고, 회원가입 이후 3일 이상 지난 사용자만 상품을 등록 할 수 있도록 권한을 설정해주세요

# 6/15 다섯번째 과제 설명 - WIP
1. product라는 앱을 새로 생성해주세요
2. product 앱에서 <제목, 썸네일, 설명, 등록일자, 노출 시작 일, 노출 종료일, 활성화 여부>가 포함된 event 테이블을 생성해주세요
<img width="711" alt="image" src="https://user-images.githubusercontent.com/89897944/174226253-4a379a1f-d7cd-4f16-b750-c909ef3245b0.png">

3. django serializer에서 기본적으로 제공하는 validate / create / update 기능을 사용해 event 테이블의 생성/수정 기능을 구현해주세요
    1. 전달 받은 데이터는 **kwargs를 사용해 입력해주세요
    2. postman으로 파일을 업로드 할 때는 raw 대신 form-data를 사용하고, Key type을 File로 설정해주세요
4. 등록된 이벤트 중 현재 시간이 노출 시작 일과 노출 종료 일의 사이에 있고, 활성화 여부가 True인 event 쿼리셋을 직렬화 해서 리턴해주는 serializer를 만들어주세요


# 역참조 - ( 6/13일 3번 문제 )
![image](https://user-images.githubusercontent.com/89897944/174224560-d941f9c3-115c-4250-97f3-df7177641194.png)
** 역참조를 할때 변수 이름 밑에는 "_set"이 들어가야한다.
그리고 () 안에 'many=True'를 설정하여 한명의 유저가 여러개의 comment를 가지고 있는 one to many 관계가 가능 하다는 것을 나타내 준다.


# Method 별로 권한 설정 다르게 하기 - ( 6/10일 13번 문제 )
![image](https://user-images.githubusercontent.com/89897944/174224236-c3662f08-8433-4364-8e17-51f59fe78450.png)
**def haspermission 밑에 if 분기를 만들어서 서로 다른 권한을 줄 수 있다.

# 6/13 네번째 과제 
1. blog 앱에 <게시글, 작성자, 작성 시간, 내용>이 포함된 comment라는 테이블을 추가해주세요
    게시글과 작성자는 fk 필드로 생성해주셔야 해요
<img width="704" alt="image" src="https://user-images.githubusercontent.com/89897944/173721755-ae5375eb-5730-43fd-abee-e9cf4f53576e.png">

    
2. Django Serializer 기능을 사용해 로그인 한 사용자의 기본 정보들을 response data에 넣어서 return 해주세요
3. 사용자가 작성 한 게시글을 로그인 한 (2번)User의 serializer data에 포함시켜서 같이 return해주세요
<img width="460" alt="image" src="https://user-images.githubusercontent.com/89897944/173725863-bf3ae2df-45ee-4284-92bc-c9cc32d3c596.png">

<img width="896" alt="image" src="https://user-images.githubusercontent.com/89897944/173725975-0c5fbb8b-e0c0-45d5-8377-278b99c01801.png">
*** 에러 수정 중입니다.

# 6/10 세번째 과제
새롭게 만든 앱 : blog, user(수정)

새롭게 추가된 API : /h3/user , /h3/blog

1. Django 프로젝트를 생성하고, user 라는 앱을 만들어서 settings.py 에 등록해보세요.
<img width="675" alt="image" src="https://user-images.githubusercontent.com/89897944/173239228-4fd104f7-c372-43c4-a5a9-3a1ac77e58df.png">

2. user/models.py에 `Custom user model`을 생성한 후 django에서 user table을 생성 한 모델로 사용할 수 있도록 설정해주세요
<img width="825" alt="image" src="https://user-images.githubusercontent.com/89897944/173239266-cfc0ffc1-f3cd-40e8-ba8d-efa69d1fe2f8.png">

3. user/models.py에 사용자의 상세 정보를 저장할 수 있는 `UserProfile` 이라는 모델을 생성해주세요
<img width="957" alt="image" src="https://user-images.githubusercontent.com/89897944/173239289-e2f942e7-8543-4ec1-92ca-2a5b1e03213e.png">

4. blog라는 앱을 만든 후 settings.py에 등록해주세요
<img width="576" alt="image" src="https://user-images.githubusercontent.com/89897944/173239377-b94f5b21-23dc-4309-9389-df3aecfce179.png">

5. blog/models.py에 <카테고리 이름, 설명>이 들어갈 수 있는 `Category`라는 모델을 만들어보세요.
6. blog/models.py에 <글 작성자, 글 제목, 카테고리, 글 내용>이 들어갈 수 있는 `Article` 이라는 모델을 만들어보세요.(카테고리는 2개 이상 선택할 수 있어야 해요)
7. Article 모델에서 외래 키를 활용해서 작성자와 카테고리의 관계를 맺어주세요
<img width="979" alt="image" src="https://user-images.githubusercontent.com/89897944/173239423-cc46a932-6952-4649-944c-71a691215c2e.png">

8. admin.py에 만들었던 모델들을 추가해 사용자와 게시글을 자유롭게 생성, 수정 할 수 있도록 설정해주세요
9. admin 페이지에서 사용자, 카테고리, 게시글을 자유롭게 추가해주세요
![image](https://user-images.githubusercontent.com/89897944/173239477-068612d2-5ebd-43cb-9496-5ffc53add3e1.png)

10. views.py에 username, password를 받아 로그인 할 수 있는 기능을 만들어주세요
    - 로그인 기능 구현이 처음이시라면 3일차 강의자료 5번 항목을 확인해주세요
![image](https://user-images.githubusercontent.com/89897944/173240036-82c7a498-9906-4ab5-a062-e289985a2f18.png)

11. views.py에 로그인 한 사용자의 정보, 게시글을 보여주는 기능을 만들어주세요
![image](https://user-images.githubusercontent.com/89897944/173241154-e8f9982b-348e-460a-8216-0b712b83608b.png)

13. views.py에 <글 제목, 카테고리, 글 내용>을 입력받아 게시글을 작성해주는 기능을 만들어주세요
    - 게시글은 계정 생성 후 3일 이상 지난 사용자만 생성할 수 있도록 권한을 설정해주세요
    - 테스트 코드에서는 계정 생성 후 3분 이상 지난 사용자는 게시글을 작성할 수 있도록 해주세요
![image](https://user-images.githubusercontent.com/89897944/173242748-438a03ad-d920-4bee-96e0-dd50c3388943.png)

----- 문제점 post와 get을 따로 분리하여 permission을 적용하는 방법을 생각해보는 중

    
# 6/8 두번째 과제 설명
새롭게 만든 앱 : user, actor

새롭게 추가된 API : /h2/user , /h2/actor

과제 1 : one to one, many to many 등 다양한 속성을 가진 필드를 사용해 모델링 해보기
- 강의에서 보여드린 user / userprofile / hobby의 관계가 아닌, 어디에 어떤 관계를 사용할 수 있을지 고민해보고 만들어 보면 좋을 것 같습니다!!
<img width="1500" alt="image" src="https://user-images.githubusercontent.com/89897944/172916099-052a0b4e-1f47-4748-8157-46bf75f79d94.png">


과제 2 : CBV를 사용해 views.py 구성해보기
<img width="1220" alt="image" src="https://user-images.githubusercontent.com/89897944/172915922-f015ba75-69ac-46d6-829d-f7e5024c85b9.png">


과제 3 : custom user permission을 활용해 내가 원하는 대로 권한 바꿔보기
<img width="1728" alt="image" src="https://user-images.githubusercontent.com/89897944/172915276-b0ee482c-7305-4e3c-ae08-74df461b19c6.png">
![image](https://user-images.githubusercontent.com/89897944/172915555-f13e6246-7af2-4f0d-bf69-beff397a99a0.png)


# 6/7 첫번째 과제 설명
새롭게 만든 앱 : message

새롭게 추가된 API : /message/basic

과제 1 : mutable과 immutable한 자료형에 대하여 학습하기
- https://dawnpast12.tistory.com/entry/3%EB%B6%84-CS%EC%A7%80%EC%8B%9D-Immutable%EA%B3%BC-Mutable

과제 2 : Get으로 message를 리턴 받을 수 있게 프로젝트 하나 만들어보기 (포스트맨 사용)
- 프로젝트의 이름은 myapi로 임의로 설정하였습니다.
- 해당 프로젝트의 앱에 message라는 앱을 생성하고 해당 앱에서 함수형 view로 get 호출이 가능하게 하였습니다.
- get으로 http://127.0.0.1:8000/message/basic 에 요청을 하게 되면 "GET 요청 완료" 를 반환하게 하였습니다.

![image](https://user-images.githubusercontent.com/89897944/172777346-3b8a86f6-72f3-494f-bc73-8488ba724d4b.png)


