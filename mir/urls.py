"""mir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin

from study.views import tag_upload
from study.views import theme_upload
from study.views import study_upload
from study.views import region_upload
from study.views import country_upload
from study.views import quality_upload
from study.views import category_upload
from study.views import resource_upload
from study.views import sub_theme_upload
from study.views import sub_category_upload

from study.views import tag_upload_confirm
from study.views import theme_upload_confirm
from study.views import region_upload_confirm
from study.views import country_upload_confirm
from study.views import quality_upload_confirm
from study.views import category_upload_confirm
from study.views import resource_upload_confirm

urlpatterns = [
	
	#Category Links
	
	#Upload URLS
	path('admin/study/upload/', study_upload, name='study_upload'),
	
	#Tags URLS
	path('admin/study/tag/upload/', tag_upload, name='tag_upload'),
	path('admin/study/tag/upload/confirm/', tag_upload_confirm, name='tag_upload_confirm'),

	#Theme URLS
	path('admin/study/theme/upload/', theme_upload, name='theme_upload'),
	path('admin/study/theme/upload/confirm/', theme_upload_confirm, name='theme_upload_confirm'),
	
	#Region URLS
	path('admin/study/region/upload/', region_upload, name='region_upload'),
	path('admin/study/region/upload/confirm/', region_upload_confirm, name='region_upload_confirm'),
	
	#Country URLS
	path('admin/study/country/upload/', country_upload, name='country_upload'),
	path('admin/study/country/upload/confirm/', country_upload_confirm, name='country_upload_confirm'),

	#Quality URLS
	path('admin/study/quality/upload/', quality_upload, name='quality_upload'),
	path('admin/study/quality/upload/confirm/', quality_upload_confirm, name='quality_upload_confirm'),

	#category URLS
	path('admin/study/category/upload/', category_upload, name='category_upload'),
	path('admin/study/category/upload/confirm/', category_upload_confirm, name='category_upload_confirm'),

	#Resource URLS
	path('admin/study/resource/upload/', resource_upload, name='resource_upload'),	
	path('admin/study/resource/upload/confirm/', resource_upload_confirm, name='resource_upload_confirm'),

	path('admin/study/sub/theme/upload/', sub_theme_upload, name='sub_theme_upload'),	
	path('admin/study/sub/category/upload/', sub_category_upload, name='sub_category_upload'),	
	#path('admin/study/sub/category/upload/confirm/', sub_category_upload_confirm, name='sub_category_upload_confirm'),

	#Generic Admin Links
    path('admin/', admin.site.urls),
]
