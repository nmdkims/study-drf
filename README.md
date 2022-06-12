# 6/10 세번째 과제 설명 - WIP
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


