from django import template
from django.shortcuts import render
from django.http import HttpResponse

register = template.Library()

from study.models import Tag
from study.models import Study
from study.models import Theme
from study.models import Region
from study.models import Country
from study.models import Quality
from study.models import Category
from study.models import Resource
from study.models import SubTheme
from study.models import SubCategory

# Create your views here.

'''	Front End views '''

def home_page(request):	
	if request.method == 'POST':
		theme = request.POST.get('theme')
		region = request.POST.get('region')
		country = request.POST.get('country')
		keyword = request.POST.get('keyword')
		quality = request.POST.get('quality')
		category = request.POST.get('category')
		sub_theme = request.POST.get('sub_theme')
		sub_category = request.POST.get('sub_category')

		result = Study.objects.filter(title__icontains=keyword)
		context = {
			'result':result
		}
		return render(request, 'core/search_result.html', context)
	else:
		
		no_of_studies = []
		High = "High"
		study_data = Study.objects.all()
		theme_data = Theme.objects.all()
		region_data = Region.objects.all()
		country_data = Country.objects.all()
		quality_data = Quality.objects.all()
		category_data = Category.objects.all()	
		sub_theme_data = SubTheme.objects.all()
		sub_category_data = SubCategory.objects.all()
		#prac = practice(**kwargs)
		
		no_of_sub_categories = 1
		no_of_categories = Category.objects.count()
		x = 0
		#while x < no_of_categories:
			#no_of_sub_categories = SubCategory.objects.filter(category=category_data[0]).count()

		context = {
			'x':x,
			#'prac':prac,
			'High':High,
			'study_data':study_data,
			'theme_data':theme_data, 
			'region_data':region_data,
			'country_data':country_data,
			'quality_data':quality_data,
			'no_of_studies':no_of_studies,
			'category_data':category_data, 
			'sub_theme_data':sub_theme_data, 
			'no_of_categories':no_of_categories,
			'sub_category_data':sub_category_data,		
			'no_of_sub_categories':no_of_sub_categories,
		}

		return render(request, 'core/index.html', context)

def of_sub_categories():
	num = Category.objects.count()
	return num

#@register.filter
def sub_categories_in_category(cat):
	got_sub_cat = SubCategory.objects.filter(category=cat)
	return got_sub_cat

def practice(*args):
	return args