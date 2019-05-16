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
from django.conf import settings
from django.conf.urls.static import static

from core.views import search
from core.views import home_page
from core.views import view_study
from core.views import about_us_page
from core.views import view_bubble_study

from core.api.views import StudyListAPIView

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
from study.views import study_upload_confirm
from study.views import theme_upload_confirm
from study.views import region_upload_confirm
from study.views import country_upload_confirm
from study.views import quality_upload_confirm
from study.views import category_upload_confirm
from study.views import resource_upload_confirm
from study.views import sub_theme_upload_confirm
from study.views import sub_category_upload_confirm

from study.views import download_tags
from study.views import download_theme
from study.views import download_region
from study.views import download_country
from study.views import download_quality
from study.views import download_category
from study.views import download_resource
#from study.views import download_all_studies

from study.views import download_template
from study.views import download_all_studies
from study.views import download_study_related_template
from study.views import download_sub_theme_related_template
from study.views import download_sub_category_related_template


urlpatterns = [	   

	#Study URLS
	path('admin/study/upload/', study_upload, name='study_upload'),
	path('admin/study/upload/confirm/', study_upload_confirm, name='study_upload_confirm'),
	path('admin/study/studies/download/', download_all_studies, name='download_all_studies'),	
	path('admin/study/download/related/templates/', download_study_related_template, name='download_study_related_template'),	


	#Tags URLS
	path('admin/study/tag/upload/', tag_upload, name='tag_upload'),
	path('admin/study/tag/download/', download_tags, name='download_tags'),
	path('admin/study/tag/upload/confirm/', tag_upload_confirm, name='tag_upload_confirm'),
	

	#Theme URLS
	path('admin/study/theme/upload/', theme_upload, name='theme_upload'),
	path('admin/study/theme/download/', download_theme, name='download_theme'),
	path('admin/study/theme/upload/confirm/', theme_upload_confirm, name='theme_upload_confirm'),
	
	#Region URLS
	path('admin/study/region/upload/', region_upload, name='region_upload'),
	path('admin/study/region/download', download_region, name='download_region'),
	path('admin/study/region/upload/confirm/', region_upload_confirm, name='region_upload_confirm'),
	
	#Country URLS
	path('admin/study/country/upload/', country_upload, name='country_upload'),
	path('admin/study/country/download/', download_country, name='download_country'),
	path('admin/study/country/upload/confirm/', country_upload_confirm, name='country_upload_confirm'),

	#Quality URLS
	path('admin/study/quality/upload/', quality_upload, name='quality_upload'),
	path('admin/study/quality/download/', download_quality, name='download_quality'),
	path('admin/study/quality/upload/confirm/', quality_upload_confirm, name='quality_upload_confirm'),

	#category URLS
	
	path('admin/study/category/upload/', category_upload, name='category_upload'),
	path('admin/study/category/download', download_category, name='download_category'),	
	path('admin/study/category/upload/confirm/', category_upload_confirm, name='category_upload_confirm'),

	#Resource URLS
	path('admin/study/resource/upload/', resource_upload, name='resource_upload'),	
	path('admin/study/resource/download', download_resource, name='download_resource'),
	path('admin/study/resource/upload/confirm/', resource_upload_confirm, name='resource_upload_confirm'),

	#Sub Theme URLS
	path('admin/study/sub/theme/upload/', sub_theme_upload, name='sub_theme_upload'),	
	path('admin/study/sub/theme/upload/confirm/', sub_theme_upload_confirm, name='sub_theme_upload_confirm'),
	path('admin/study/sub/theme/download/related/templates/', download_sub_theme_related_template, name='download_sub_theme_related_template'),

	#Sub Category URLS
	path('admin/study/sub/category/upload/', sub_category_upload, name='sub_category_upload'),	
	path('admin/study/sub/category/upload/confirm/', sub_category_upload_confirm, name='sub_category_upload_confirm'),
	path('admin/study/sub/category/download/related/templates/', download_sub_category_related_template, name='download_sub_category_related_template'),

	#Generic URL to download Template files
	path('admin/study/download/<file_name>/', download_template, name='download_template'),
	
	#Generic Admin Links
    path('admin/', admin.site.urls),

    

    #Front End Page Links
    path('', home_page, name='home_page'),
    path('search', search, name='search'),
    path('about', about_us_page, name='about'),
    path('view/study/<study_id>/', view_study, name='view_study'),
    path('api/study/all', StudyListAPIView.as_view(), name='studies_json'),    
    path('view/bubble/<bubble_id>/', view_bubble_study, name='view_bubble_study'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)