
   
<p align="center"><img src="main.png" 너비="400"></p>
<p align="center"><img src="detail.png" 너비="400"></p>
<p align="center"><img src="channel.png" 너비="400"></p>





## django-youtube 비슷하게 만들어 본  사이트

-django
-tailwind.css
-html
-node.js
-axios.js
-alpine.js
-video.js

#####테스트시 노드가 설치되어 있어야하고 urlencode 설치되어 있어야함
```
    npm install urlencode
```

######테스트시 개발서버와 영상 스트리밍 서버(node) 두개 켜있어야함
```  
    node stream_server.js
    python manage.py runserver  
``` 
###배포  
-라즈베리파이
-nginx (node, django)
-Django GUNICORN사용
-node forever사용
###### # node_django_video_stream_-
