# 간단한 영상 사이트

### 노드
##### 노드가 설치되어 있어야하고 urlencode 설치되어 있어야함
```
    npm install urlencode
```

###### 개발서버와 영상 스트리밍 서버(node) 두개 켜있어야함
```  
    node stream_server.js
    python manage.py runserver  
``` 

###### .env 파일의 내용이 없으므로 이메일인증코드,카카오 로그인은 동작하지 않음 (admin page 사용자 만들기)