#indicators/variables of internet freedom
from django import template
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

register = template.Library()

from study.models import Tag
from study.models import Study
from study.models import Theme
from study.models import Region
from study.models import Country
from study.models import Category
from study.models import Resource
from study.models import SubTheme
from study.models import SubCategory

# Create your views here.

'''	Front End views '''

def search(request):
	if request.method == 'POST':
		theme = request.POST.get('theme')
		region = request.POST.get('region')
		country = request.POST.get('country')
		keyword = request.POST.get('keyword')
		category = request.POST.get('category')

		study_data = Study.objects.all()
		theme_data = Theme.objects.all()
		region_data = Region.objects.all()
		country_data = Country.objects.all()
		category_data = Category.objects.all()

		#If no search parameters are input
		if theme=="" and category=="" and region=="" and country=="" and keyword=="":
			result = Study.objects.all()
		#If all parameters are input
		elif theme!="" and category!="" and region!="" and country!="" and keyword!="":
			result = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, region=region, country=country)
		#Keyword Seach with other parameters
		elif keyword!="" and theme=="" and category=="" and region=="" and country=="":
			result = Study.objects.filter(title__icontains=keyword)
		elif keyword!="" and theme!="" and category=="" and region=="" and country=="":
			result = Study.objects.filter(title__icontains=keyword, theme=theme)
		elif keyword!="" and theme=="" and category!="" and region=="" and country=="":
			result = Study.objects.filter(title__icontains=keyword, category=category)
		elif keyword!="" and theme=="" and category=="" and region!="" and country=="":
			result = Study.objects.filter(title__icontains=keyword, region=region)
		elif keyword!="" and theme=="" and category=="" and region=="" and country!="":
			result = Study.objects.filter(title__icontains=keyword, country=country)
		#Keyword and Theme Combination
		elif keyword!="" and theme!="" and category!="" and region=="" and country=="":
			result = Study.objects.filter(title__icontains=keyword, theme=theme, category=category)
		elif keyword!="" and theme!="" and category=="" and region!="" and country=="":
			result = Study.objects.filter(title__icontains=keyword, theme=theme, region=region)
		elif keyword!="" and theme!="" and category=="" and region=="" and country!="":
			result = Study.objects.filter(title__icontains=keyword, theme=theme, country=country)
		#Keyword and category Combination
		elif keyword!="" and theme=="" and category!="" and region!="" and country=="":
			result = Study.objects.filter(title__icontains=keyword, category=category, region=region)
		elif keyword!="" and theme=="" and category!="" and region=="" and country!="":
			result = Study.objects.filter(title__icontains=keyword, category=category, country=country)
		#Keyword and region combination
		elif keyword!="" and theme=="" and category=="" and region!="" and country!="":
			result = Study.objects.filter(title__icontains=keyword, region=region, country=country)
		#Theme Search
		elif keyword=="" and theme!="" and category=="" and region=="" and country=="":
			result = Study.objects.filter(theme=theme)
		elif keyword=="" and theme!="" and category!="" and region=="" and country=="":
			result = Study.objects.filter(theme=theme, category=category)
		elif keyword=="" and theme!="" and category=="" and region!="" and country=="":
			result = Study.objects.filter(theme=theme, region=region)
		elif keyword=="" and theme!="" and category=="" and region=="" and country!="":
			result = Study.objects.filter(theme=theme, country=country)
		#Theme and Category Search
		elif keyword=="" and theme!="" and category!="" and region=="" and country=="":
			result = Study.objects.filter(theme=theme, category=category)
		elif keyword=="" and theme!="" and category!="" and region!="" and country=="":
			result = Study.objects.filter(theme=theme, category=category, region=region)
		elif keyword=="" and theme!="" and category!="" and region=="" and country!="":
			result = Study.objects.filter(theme=theme, category=category, country=country)
		#Theme and region combination
		elif keyword=="" and theme!="" and category=="" and region!="" and country!="":
			result = Study.objects.filter(theme=theme, region=region, country=country)
		#Category search
		elif keyword=="" and theme=="" and category!="" and region=="" and country=="":
			result = Study.objects.filter(category=category)
		elif keyword=="" and theme=="" and category!="" and region!="" and country=="":
			result = Study.objects.filter(category=category, region=region)
		elif keyword=="" and theme=="" and category!="" and region=="" and country!="":
			result = Study.objects.filter(category=category, country=country)
		#Category region combination
		elif keyword=="" and theme=="" and category!="" and region!="" and country!="":
			result = Study.objects.filter(category=category, region=region, country=country)
		#Region Search
		elif keyword=="" and theme=="" and category=="" and region!="" and country=="":
			result = Study.objects.filter(region=region)		
		elif keyword=="" and theme=="" and category=="" and region!="" and country!="":
			result = Study.objects.filter(region=region, country=country)
		#Country Search
		elif keyword=="" and theme=="" and category=="" and region=="" and country!="":
			result = Study.objects.filter(country=country)

		context = {
		'result':result,
		'study_data':study_data,
		'theme_data':theme_data, 
		'region_data':region_data,
		'country_data':country_data,		
		'category_data':category_data,
		}

		return render(request, 'core/search_result.html', context)	
	else:
		return redirect('home_page')


def search_data(request):
	if request.method == 'POST':
		keyword = request.POST.get('keyword')
		theme_captured = request.POST.getlist('theme[]')
		region_captured = request.POST.getlist('region[]')
		country_captured = request.POST.getlist('country[]')
		category_captured = request.POST.getlist('category[]')
		
		study_data = Study.objects.all()
		theme_data = Theme.objects.all()
		region_data = Region.objects.all()
		country_data = Country.objects.all()
		category_data = Category.objects.all()	
		
		if theme_captured=="" and region_captured=="" and country_captured=="" and category_captured and keyword=="":
			result = Study.objects.all()
		elif theme_captured=="" and region_captured=="" and country_captured=="" and category_captured and keyword=="":
			pass

def search_one(request):
	if request.method == 'POST':
		theme = request.POST.get('theme')
		region = request.POST.get('region')
		country = request.POST.get('country')
		keyword = request.POST.get('keyword')
		#quality = request.POST.get('quality')
		category = request.POST.get('category')
		sub_theme = request.POST.get('sub_theme')
		sub_category = request.POST.get('sub_category')

		study_data = Study.objects.all()
		theme_data = Theme.objects.all()
		region_data = Region.objects.all()
		country_data = Country.objects.all()
		#quality_data = Quality.objects.all()
		category_data = Category.objects.all()	
		sub_theme_data = SubTheme.objects.all()
		sub_category_data = SubCategory.objects.all()

		#If no search parameters are input
		if theme=="" and category=="" and region=="" and country=="" and sub_theme=="" and sub_category =="" and keyword=="":
			result = Study.objects.all()
		#If all parameters are input
		elif theme!="" and category!="" and region!="" and country!="" and sub_theme!="" and sub_category!="" and keyword!="":
			result = Study.objects.filter(title__icontains=keyword, sub_theme__theme=theme, sub_category__category=category, region=region, country=country, sub_theme=sub_theme, sub_category=sub_category)
		#Keyword Seach with other parameters
		elif keyword!="" and theme=="" and category=="" and region=="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword)
		elif keyword!="" and theme!="" and category=="" and region=="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, sub_theme__theme=theme)
		elif keyword!="" and theme=="" and category!="" and region=="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, sub_category__category=category)
		elif keyword!="" and theme=="" and category=="" and region!="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, region=region)
		elif keyword!="" and theme=="" and category=="" and region=="" and country!="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, country=country)
		elif keyword!="" and theme=="" and category=="" and region=="" and country=="" and sub_theme!="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, sub_theme=sub_theme)
		elif keyword!="" and theme=="" and category=="" and region=="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, sub_category=sub_category)
		#Keyword and Theme Combination
		elif keyword!="" and theme!="" and category!="" and region=="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, sub_theme__theme=theme, sub_category__category=category)
		elif keyword!="" and theme!="" and category=="" and region!="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, sub_theme__theme=theme, region=region)
		elif keyword!="" and theme!="" and category=="" and region=="" and country!="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, sub_theme__theme=theme, country=country)
		elif keyword!="" and theme!="" and category=="" and region=="" and country=="" and sub_theme!="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, sub_theme__theme=theme, sub_theme=sub_theme)
		elif keyword!="" and theme!="" and category=="" and region=="" and country=="" and sub_theme=="" and sub_category !="":
			result = Study.objects.filter(title__icontains=keyword, sub_theme__theme=theme, sub_category=sub_category)
		#Keyword and category Combination
		elif keyword!="" and theme=="" and category!="" and region!="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, sub_category__category=category, region=region)
		elif keyword!="" and theme=="" and category!="" and region=="" and country!="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, sub_category__category=category, country=country)
		elif keyword!="" and theme=="" and category!="" and region=="" and country=="" and sub_theme!="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, sub_category__category=category, sub_theme=sub_theme)
		elif keyword!="" and theme=="" and category!="" and region=="" and country=="" and sub_theme=="" and sub_category !="":
			result = Study.objects.filter(title__icontains=keyword, sub_category__category=category, sub_category=sub_category)
		#Keyword and region combination
		elif keyword!="" and theme=="" and category=="" and region!="" and country!="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, region=region, country=country)
		elif keyword!="" and theme=="" and category=="" and region!="" and country=="" and sub_theme!="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, region=region, sub_theme=sub_theme)
		elif keyword!="" and theme=="" and category=="" and region!="" and country=="" and sub_theme=="" and sub_category !="":
			result = Study.objects.filter(title__icontains=keyword, region=region, sub_category=sub_category)
		#Keyword and Country Combination
		elif keyword!="" and theme=="" and category=="" and region=="" and country!="" and sub_theme!="" and sub_category =="":
			result = Study.objects.filter(title__icontains=keyword, country=country, sub_theme=sub_theme)
		elif keyword!="" and theme=="" and category=="" and region=="" and country!="" and sub_theme=="" and sub_category !="":
			result = Study.objects.filter(title__icontains=keyword, country=country, sub_category=sub_category)
		#Keyword and sub_category combination
		elif keyword!="" and theme=="" and category=="" and region=="" and country=="" and sub_theme!="" and sub_category !="":
			result = Study.objects.filter(title__icontains=keyword, sub_theme=sub_theme, sub_category=sub_category)
		#Theme Search
		elif keyword=="" and theme!="" and category=="" and region=="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(sub_theme__theme=theme)
		elif keyword=="" and theme!="" and category!="" and region=="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(sub_theme__theme=theme, sub_category__category=category)
		elif keyword=="" and theme!="" and category=="" and region!="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(sub_theme__theme=theme, region=region)
		elif keyword=="" and theme!="" and category=="" and region=="" and country!="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(sub_theme__theme=theme, country=country)
		elif keyword=="" and theme!="" and category=="" and region=="" and country=="" and sub_theme!="" and sub_category =="":
			result = Study.objects.filter(sub_theme__theme=theme, sub_theme=sub_theme)
		elif keyword=="" and theme!="" and category=="" and region=="" and country=="" and sub_theme=="" and sub_category !="":
			result = Study.objects.filter(sub_theme__theme=theme, sub_category=sub_category)
		#Theme and Category Search
		elif keyword=="" and theme!="" and category!="" and region=="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(sub_theme__theme=theme, sub_category__category=category)
		elif keyword=="" and theme!="" and category!="" and region!="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(sub_theme__theme=theme, sub_category__category=category, region=region)
		elif keyword=="" and theme!="" and category!="" and region=="" and country!="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(sub_theme__theme=theme, sub_category__category=category, country=country)
		elif keyword=="" and theme!="" and category!="" and region=="" and country=="" and sub_theme!="" and sub_category =="":
			result = Study.objects.filter(sub_theme__theme=theme, sub_category__category=category, sub_theme=sub_theme)
		elif keyword=="" and theme!="" and category!="" and region=="" and country=="" and sub_theme=="" and sub_category !="":
			result = Study.objects.filter(sub_theme__theme=theme, sub_category__category=category, sub_category=sub_category)
		#Theme and region combination
		elif keyword=="" and theme!="" and category=="" and region!="" and country!="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(sub_theme__theme=theme, region=region, country=country)
		elif keyword=="" and theme!="" and category=="" and region!="" and country=="" and sub_theme!="" and sub_category =="":
			result = Study.objects.filter(sub_theme__theme=theme, region=region, sub_theme=sub_theme)
		elif keyword=="" and theme!="" and category=="" and region!="" and country=="" and sub_theme=="" and sub_category !="":
			result = Study.objects.filter(sub_theme__theme=theme, region=region, sub_category=sub_category)
		#Theme and country combination
		elif keyword=="" and theme!="" and category=="" and region=="" and country!="" and sub_theme!="" and sub_category =="":
			result = Study.objects.filter(sub_theme__theme=theme, country=country, sub_theme=sub_theme)
		elif keyword=="" and theme!="" and category=="" and region!="" and country!="" and sub_theme=="" and sub_category !="":
			result = Study.objects.filter(sub_theme__theme=theme, region=region, sub_category=sub_category)
		#Theme and sub_theme		
		elif keyword=="" and theme!="" and category=="" and region!="" and country=="" and sub_theme!="" and sub_category !="":
			result = Study.objects.filter(sub_theme__theme=theme, sub_theme=sub_theme, sub_category=sub_category)
		#Category search
		elif keyword=="" and theme=="" and category!="" and region=="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(sub_category__category=category)
		elif keyword=="" and theme=="" and category!="" and region!="" and country=="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(sub_category__category=category, region=region)
		elif keyword=="" and theme=="" and category!="" and region=="" and country!="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(sub_category__category=category, country=country)
		elif keyword=="" and theme=="" and category!="" and region=="" and country=="" and sub_theme!="" and sub_category =="":
			result = Study.objects.filter(sub_category__category=category, sub_theme=sub_theme)
		elif keyword=="" and theme=="" and category!="" and region=="" and country=="" and sub_theme=="" and sub_category!="":
			result = Study.objects.filter(sub_category__category=category, sub_category=sub_category)
		#Category region combination
		elif keyword=="" and theme=="" and category!="" and region!="" and country!="" and sub_theme=="" and sub_category =="":
			result = Study.objects.filter(sub_category__category=category, region=region, country=country)
		elif keyword=="" and theme=="" and category!="" and region!="" and country=="" and sub_theme!="" and sub_category =="":
			result = Study.objects.filter(sub_category__category=category, region=region, sub_theme=sub_theme)
		elif keyword=="" and theme=="" and category!="" and region!="" and country=="" and sub_theme=="" and sub_category!="":
			result = Study.objects.filter(sub_category__category=category, region=region, sub_category=sub_category)
		#category country combination
		elif keyword=="" and theme=="" and category!="" and region=="" and country!="" and sub_theme!="" and sub_category =="":
			result = Study.objects.filter(sub_category__category=category, country=country, sub_theme=sub_theme)
		elif keyword=="" and theme=="" and category!="" and region=="" and country!="" and sub_theme=="" and sub_category!="":
			result = Study.objects.filter(sub_category__category=category, country=country, sub_category=sub_category)
		#Category sub_theme combination
		elif keyword=="" and theme=="" and category!="" and region=="" and country=="" and sub_theme!="" and sub_category!="":
			result = Study.objects.filter(sub_category__category=category, sub_theme=sub_theme, sub_category=sub_category)
		#Region Search
		elif keyword=="" and theme=="" and category=="" and region!="" and country=="" and sub_theme=="" and sub_category=="":
			result = Study.objects.filter(region=region)		
		elif keyword=="" and theme=="" and category=="" and region!="" and country!="" and sub_theme=="" and sub_category=="":
			result = Study.objects.filter(region=region, country=country)
		elif keyword=="" and theme=="" and category=="" and region!="" and country=="" and sub_theme!="" and sub_category=="":
			result = Study.objects.filter(region=region, sub_theme=sub_theme)
		elif keyword=="" and theme=="" and category=="" and region!="" and country=="" and sub_theme=="" and sub_category!="":
			result = Study.objects.filter(region=region, sub_category=sub_category)
		#region country combination
		elif keyword=="" and theme=="" and category=="" and region!="" and country!="" and sub_theme!="" and sub_category=="":
			result = Study.objects.filter(region=region, country=country, sub_theme=sub_theme)
		elif keyword=="" and theme=="" and category=="" and region!="" and country!="" and sub_theme=="" and sub_category!="":
			result = Study.objects.filter(region=region, country=country, sub_category=sub_category)
		#region sub_theme combination
		elif keyword=="" and theme=="" and category=="" and region!="" and country=="" and sub_theme!="" and sub_category!="":
			result = Study.objects.filter(region=region, sub_theme=sub_theme, sub_category=sub_category)
		#Country Search
		elif keyword=="" and theme=="" and category=="" and region=="" and country!="" and sub_theme=="" and sub_category=="":
			result = Study.objects.filter(country=country)
		elif keyword=="" and theme=="" and category=="" and region=="" and country!="" and sub_theme!="" and sub_category=="":
			result = Study.objects.filter(country=country, sub_theme=sub_theme)
		elif keyword=="" and theme=="" and category=="" and region=="" and country!="" and sub_theme=="" and sub_category!="":
			result = Study.objects.filter(country=country, sub_category=sub_category)
		#Country sub_theme combination
		elif keyword=="" and theme=="" and category=="" and region=="" and country!="" and sub_theme!="" and sub_category!="":
			result = Study.objects.filter(country=country, sub_theme=sub_theme, sub_category=sub_category)
		#Sub Theme search
		elif keyword=="" and theme=="" and category=="" and region=="" and country=="" and sub_theme!="" and sub_category=="":
			result = Study.objects.filter(sub_theme=sub_theme)
		elif keyword=="" and theme=="" and category=="" and region=="" and country=="" and sub_theme!="" and sub_category!="":
			result = Study.objects.filter(sub_theme=sub_theme, sub_category=sub_category)
		#Sub Category search
		elif keyword=="" and theme=="" and category=="" and region=="" and country=="" and sub_theme=="" and sub_category!="":
			result = Study.objects.filter(sub_category=sub_category)
		

		context = {
		'result':result,
		'study_data':study_data,
		'theme_data':theme_data, 
		'region_data':region_data,
		'country_data':country_data,
		'quality_data':quality_data,		
		'category_data':category_data, 
		'sub_theme_data':sub_theme_data,
		'sub_category_data':sub_category_data,
		}

		return render(request, 'core/search_result.html', context)	
	else:
		return redirect('home_page')


def home_page(request):	
	study_data = Study.objects.all()
	theme_data = Theme.objects.all()
	region_data = Region.objects.all()
	country_data = Country.objects.all()
	category_data = Category.objects.all()		
	
	context = {		
		'study_data':study_data,
		'theme_data':theme_data, 
		'region_data':region_data,
		'country_data':country_data,
		'category_data':category_data,	
	}

	return render(request, 'core/index.html', context)

def studies_json(request):
	queryset = Study.objects.all()
	study_data = serializers.serialize('json', queryset)
	return HttpResponse(queryset, content_type='application/json')

def view_study(request, study_id):
	study_data = Study.objects.filter(id=study_id)
	context = {
		'study_data': study_data,
	}

	return render(request, 'core/view_study.html', context)

