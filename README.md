# django
사용 ide = Visual Studio Code

## 환경 만들기
conda create -n (이름) python==3.8

시스템 속성 > 환경변수 > 변수탭 path> 아래 5개 로컬주소 추가

C:\Users\admin\anaconda3
C:\Users\admin\anaconda3\Library\mingw-w64\bin
C:\Users\admin\anaconda3\Library\usr\bin
C:\Users\admin\anaconda3\Library\bin
C:\Users\admin\anaconda3\Scripts

vscode에서 터미널 cmd > conda activate (이름)

## django 설치
pip install django==3.2

pip install django-allauth django-crispy-forms django-markdownx

## django project생성
django-admin startproject (프로젝트이름) . <!--콤마 꼭 한칸띄고 입력-->

## 명령어
<!-- models.py 변경후 저장 -->
python manage.py makemigrations
python manage.py migrate 

python manage.py createsuperuser

python manage.py startapp blog 
<!-- 페이지 생성후 setting.py installed_apps 저장-->

python manage.py runserver

## 페이지 생성후 project > urls.py

### blog, homepage

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    <!-- path가 '주소+/blog' 이면 blog 의 urls.py -->
    path('', include('homepage.urls')),
    <!-- path가 '주소+ ' 이면 hompage 의 urls.py -->
]