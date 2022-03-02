
   
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

## 사용한 버전
python==3.9
Django==3.2.9


## 개발서버 테스트시 노드가 설치되어 있어야하고 urlencode 설치되어 있어야함
```
    npm install urlencode
```

## 개발서버 테스트시 개발서버와 영상 스트리밍 서버(node) 두개 켜있어야함
```  
    node stream_server.js
    python manage.py runserver  
``` 
###### # node_django_video_stream_-
