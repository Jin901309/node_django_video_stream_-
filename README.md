
   
<p align="center"><img src="main.png" 너비="400"></p>
<p align="center"><img src="detail.png" 너비="400"></p>
<p align="center"><img src="channel.png" 너비="400"></p>
<p align="center"><img src="login.png" 너비="400"></p>
<p align="center"><img src="video.png" 너비="400"></p>


## django-youtube 비슷하게 만들어 본  사이트

-django<br>
-tailwind.css<br>
-html<br>
-node.js<br>
-axios.js<br>
-alpine.js<br>
-video.js<br>
-postgresql<br>

## 배포
-라즈베리파이(라즈베리파이에는 기본 방화벽이없음-> ufw,fail2ban사용)<br>
-nginx (node, django)<br>
-Django GUNICORN사용<br>
-node forever사용<br>
-부팅시 자동 서버 시작

## 구현 기능 
-좋아요.<br>
-댓글(crd)<br>
-영상 재생(node.js)<br>
-영상 업로드(crud)<br>
(대용량 파일 업로드 구현 할 생각이 없어서 chunk 사용안함.(라즈베리파이에 올려볼 목적))
-구독<br>
-채널<br>
-조회수<br>
-카카오로그인(외 로그인 로그아웃(이메일인증))<br>
-라즈베리파이 배포<br>
사용자 구현시 Abstract상속 말고 AbstractBaseUser사용해서 username제거함.<br>
-관리자페이지 <br>
액션 기능:<br>
	비밀번호초기화(사용자)<br>
	활성화 비활성화(사용자)등등<br>

## <a href="https://github.com/Jin901309/node_django_video_stream_-/tree/main/admin_page_image">관리자 페이지 구현한 일부 이미지</a>


## 사용한 버전
python==3.9<br>
Django==3.2.9<br>


## 개발서버 사용시 노드가 설치되어 있어야하고 urlencode 설치되어 있어야함
```
    npm install urlencode
```

## 개발서버 사용시 개발서버와 영상 스트리밍 서버(node) 두개 켜있어야함
```  
    node stream_server.js
    python manage.py runserver  
```


 
###### # node_django_video_stream_-
