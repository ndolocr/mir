#indicators/variables of internet freedom
from django import template
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

#register = template.Library()

#from study.models import Tag
from study.models import Study
from study.models import Theme
from study.models import Region
from study.models import Country
from study.models import Category
from study.models import Resource
#from study.models import SubTheme
#from study.models import SubCategory

# Create your views here.

'''	Front End views '''

def studies_json(request):
	queryset = Study.objects.all()
	study_data = serializers.serialize('json', queryset)
	return HttpResponse(queryset, content_type='application/json')

def view_study(request, study_id):	
	theme_data = Theme.objects.all()
	region_data = Region.objects.all()
	country_data = Country.objects.all()
	category_data = Category.objects.all()
	study_data = Study.objects.get(id=study_id)
	
	context = {
		'theme_data':theme_data, 
		'study_data': study_data,		
		'region_data':region_data,
		'country_data':country_data,
		'category_data':category_data,
	}

	return render(request, 'core/view_study.html', context)

def view_bubble_study(request, bubble_id):
	theme_data = Theme.objects.all()
	region_data = Region.objects.all()
	country_data = Country.objects.all()
	category_data = Category.objects.all()

	if bubble_id=="one_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public").order_by('title')
	elif bubble_id=="one_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="one_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="two_low":
		Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public").order_by('title')
	elif bubble_id=="two_high":
		Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public").order_by('title')
	elif bubble_id=="two_medium":
		Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="three_low":
		Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public").order_by('title')
	elif bubble_id=="three_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="three_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="four_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public").order_by('title')
	elif bubble_id=="four_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="four_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="five_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public").order_by('title')
	elif bubble_id=="five_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public").order_by('title')
	elif bubble_id=="five_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public").order_by('title')	
	elif bubble_id=="six_low":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public").order_by('title')
	elif bubble_id=="six_high":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="six_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public").order_by('title')	
	elif bubble_id=="seven_low":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public").order_by('title')
	elif bubble_id=="seven_high":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public").order_by('title')
	elif bubble_id=="seven_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="eight_low":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public").order_by('title')	
	elif bubble_id=="eight_high":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public").order_by('title')
	elif bubble_id=="eight_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="nine_low":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public").order_by('title')	
	elif bubble_id=="nine_high":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public").order_by('title')
	elif bubble_id=="nine_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="ten_low":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public").order_by('title')
	elif bubble_id=="ten_high":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="ten_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="sixteen_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="sixteen_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="sixteen_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="seventeen_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="seventeen_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="seventeen_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="eighteen_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="eighteen_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="eighteen_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="nineteen_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="nineteen_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="nineteen_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="twenty_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="twenty_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="twenty_one_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_one_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_one_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_two_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="twenty_two_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_two_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="twenty_three_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="twenty_three_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_three_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_four_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_four_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="twenty_four_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_five_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_five_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="twenty_five_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="twenty_six_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_six_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_six_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_seven_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="twenty_seven_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_seven_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="twenty_eight_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="twenty_eight_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_eight_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_nine_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="twenty_nine_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="twenty_nine_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="thirty_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="thirty_one_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_one_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_one_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_two_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="thirty_two_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_two_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="thirty_three_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="thirty_three_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_three_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_four_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_four_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="thirty_four_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_five_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_five_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="thirty_five_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="thirty_six_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_six_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_six_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_seven_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="thirty_seven_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_seven_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public").order_by('title')
	elif bubble_id=="thirty_eight_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="thirty_eight_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_eight_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_nine_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="thirty_nine_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="thirty_nine_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="fourty_low":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')
	elif bubble_id=="fourty_high":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	
	elif bubble_id=="fourty_medium":
		study_data = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public").order_by('title')	


	context = {
		'theme_data':theme_data, 
		'study_data': study_data,		
		'region_data':region_data,
		'country_data':country_data,
		'category_data':category_data,
	}

	return render(request, 'core/view_bubble_study.html', context)

def about_us_page(request):
	theme_data = Theme.objects.all().filter().order_by('theme_name')
	region_data = Region.objects.all().filter().order_by('region_name')
	country_data = Country.objects.all().filter().order_by('country_name')
	category_data = Category.objects.all().filter().order_by('category_name')
	
	
	context = {
		'theme_data':theme_data,		
		'region_data':region_data,
		'country_data':country_data,
		'category_data':category_data,
	}

	return render(request, 'core/about.html', context)

def home_page(request):	
	theme_data = Theme.objects.all().filter().order_by('theme_name')
	region_data = Region.objects.all().filter().order_by('region_name')
	country_data = Country.objects.all().filter().order_by('country_name')
	category_data = Category.objects.all().filter().order_by('category_name')
	
	study_data = Study.objects.filter(publish="Public")
	#Row One
	cell_one_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
	cell_one_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
	cell_one_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

	cell_two_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
	cell_two_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
	cell_two_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

	cell_three_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
	cell_three_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
	cell_three_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

	cell_four_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
	cell_four_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
	cell_four_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

	cell_five_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
	cell_five_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
	cell_five_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


	#Row two
	cell_six_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
	cell_six_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
	cell_six_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

	cell_seven_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
	cell_seven_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
	cell_seven_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

	cell_eight_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
	cell_eight_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
	cell_eight_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

	cell_nine_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
	cell_nine_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
	cell_nine_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

	cell_ten_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
	cell_ten_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
	cell_ten_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

	#Row three
	cell_eleven_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
	cell_eleven_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
	cell_eleven_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

	cell_twelve_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
	cell_twelve_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
	cell_twelve_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

	cell_thirteen_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
	cell_thirteen_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
	cell_thirteen_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

	cell_fourteen_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
	cell_fourteen_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
	cell_fourteen_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

	cell_fifteen_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
	cell_fifteen_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
	cell_fifteen_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

	#Row four
	cell_sixteen_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
	cell_sixteen_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
	cell_sixteen_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

	cell_seventeen_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
	cell_seventeen_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
	cell_seventeen_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

	cell_eighteen_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
	cell_eighteen_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
	cell_eighteen_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

	cell_nineteen_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
	cell_nineteen_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
	cell_nineteen_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

	cell_twenty_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
	cell_twenty_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
	cell_twenty_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

	#Row five
	cell_twenty_one_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
	cell_twenty_one_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
	cell_twenty_one_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

	cell_twenty_two_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
	cell_twenty_two_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
	cell_twenty_two_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

	cell_twenty_three_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
	cell_twenty_three_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
	cell_twenty_three_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

	cell_twenty_four_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
	cell_twenty_four_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
	cell_twenty_four_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

	cell_twenty_five_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
	cell_twenty_five_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
	cell_twenty_five_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

	#Row six
	cell_twenty_six_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
	cell_twenty_six_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
	cell_twenty_six_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

	cell_twenty_seven_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
	cell_twenty_seven_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
	cell_twenty_seven_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

	cell_twenty_eight_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
	cell_twenty_eight_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
	cell_twenty_eight_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

	cell_twenty_nine_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
	cell_twenty_nine_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
	cell_twenty_nine_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

	cell_thirty_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
	cell_thirty_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
	cell_thirty_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

	#Row seven
	cell_thirty_one_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
	cell_thirty_one_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
	cell_thirty_one_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

	cell_thirty_two_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
	cell_thirty_two_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
	cell_thirty_two_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

	cell_thirty_three_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
	cell_thirty_three_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
	cell_thirty_three_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

	cell_thirty_four_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
	cell_thirty_four_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
	cell_thirty_four_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

	cell_thirty_five_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
	cell_thirty_five_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
	cell_thirty_five_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

	#Row eight
	cell_thirty_six_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
	cell_thirty_six_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
	cell_thirty_six_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

	cell_thirty_seven_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
	cell_thirty_seven_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
	cell_thirty_seven_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

	cell_thirty_eight_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
	cell_thirty_eight_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
	cell_thirty_eight_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

	cell_thirty_nine_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
	cell_thirty_nine_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
	cell_thirty_nine_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

	cell_fourty_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
	cell_fourty_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
	cell_fourty_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

	context = {		
		'study_data':study_data,
		'theme_data':theme_data, 
		'region_data':region_data,
		'country_data':country_data,
		'category_data':category_data,
		
		#Row one
		'cell_one_low':cell_one_low,
		'cell_one_high':cell_one_high,
		'cell_one_medium':cell_one_medium,

		'cell_two_low':cell_two_low,
		'cell_two_high':cell_two_high,
		'cell_two_medium':cell_two_medium,

		'cell_three_low':cell_three_low,
		'cell_three_high':cell_three_high,
		'cell_three_medium':cell_three_medium,

		'cell_four_low':cell_four_low,
		'cell_four_high':cell_four_high,
		'cell_four_medium':cell_four_medium,

		'cell_five_low':cell_five_low,
		'cell_five_high':cell_five_high,
		'cell_five_medium':cell_five_medium,

		#Row two
		'cell_six_low':cell_six_low,
		'cell_six_high':cell_six_high,
		'cell_six_medium':cell_six_medium,

		'cell_seven_low':cell_seven_low,
		'cell_seven_high':cell_seven_high,
		'cell_seven_medium':cell_seven_medium,

		'cell_eight_low':cell_eight_low,
		'cell_eight_high':cell_eight_high,
		'cell_eight_medium':cell_eight_medium,

		'cell_nine_low':cell_nine_low,
		'cell_nine_high':cell_nine_high,
		'cell_nine_medium':cell_nine_medium,

		'cell_ten_low':cell_ten_low,
		'cell_ten_high':cell_ten_high,
		'cell_ten_medium':cell_ten_medium,

		#Row three
		'cell_eleven_low':cell_eleven_low,
		'cell_eleven_high':cell_eleven_high,
		'cell_eleven_medium':cell_eleven_medium,

		'cell_twelve_low':cell_twelve_low,
		'cell_twelve_high':cell_twelve_high,
		'cell_twelve_medium':cell_twelve_medium,

		'cell_thirteen_low':cell_thirteen_low,
		'cell_thirteen_high':cell_thirteen_high,
		'cell_thirteen_medium':cell_thirteen_medium,

		'cell_fourteen_low':cell_fourteen_low,
		'cell_fourteen_high':cell_fourteen_high,
		'cell_fourteen_medium':cell_fourteen_medium,

		'cell_fifteen_low':cell_fifteen_low,
		'cell_fifteen_high':cell_fifteen_high,
		'cell_fifteen_medium':cell_fifteen_medium,

		#Row four
		'cell_sixteen_low':cell_sixteen_low,
		'cell_sixteen_high':cell_sixteen_high,
		'cell_sixteen_medium':cell_sixteen_medium,

		'cell_seventeen_low':cell_seventeen_low,
		'cell_seventeen_high':cell_seventeen_high,
		'cell_seventeen_medium':cell_seventeen_medium,

		'cell_eighteen_low':cell_eighteen_low,
		'cell_eighteen_high':cell_eighteen_high,
		'cell_eighteen_medium':cell_eighteen_medium,

		'cell_nineteen_low':cell_nineteen_low,
		'cell_nineteen_high':cell_nineteen_high,
		'cell_nineteen_medium':cell_nineteen_medium,

		'cell_twenty_low':cell_twenty_low,
		'cell_twenty_high':cell_twenty_high,
		'cell_twenty_medium':cell_twenty_medium,

		#Row five
		'cell_twenty_one_low':cell_twenty_one_low,
		'cell_twenty_one_high':cell_twenty_one_high,
		'cell_twenty_one_medium':cell_twenty_one_medium,

		'cell_twenty_two_low':cell_twenty_two_low,
		'cell_twenty_two_high':cell_twenty_two_high,
		'cell_twenty_two_medium':cell_twenty_two_medium,

		'cell_twenty_three_low':cell_twenty_three_low,
		'cell_twenty_three_high':cell_twenty_three_high,
		'cell_twenty_three_medium':cell_twenty_three_medium,

		'cell_twenty_four_low':cell_twenty_four_low,
		'cell_twenty_four_high':cell_twenty_four_high,
		'cell_twenty_four_medium':cell_twenty_four_medium,

		'cell_twenty_five_low':cell_twenty_five_low,
		'cell_twenty_five_high':cell_twenty_five_high,
		'cell_twenty_five_medium':cell_twenty_five_medium,

		#Row six
		'cell_twenty_six_low':cell_twenty_six_low,
		'cell_twenty_six_high':cell_twenty_six_high,
		'cell_twenty_six_medium':cell_twenty_six_medium,

		'cell_twenty_seven_low':cell_twenty_seven_low,
		'cell_twenty_seven_high':cell_twenty_seven_high,
		'cell_twenty_seven_medium':cell_twenty_seven_medium,

		'cell_twenty_eight_low':cell_twenty_eight_low,
		'cell_twenty_eight_high':cell_twenty_eight_high,
		'cell_twenty_eight_medium':cell_twenty_eight_medium,

		'cell_twenty_nine_low':cell_twenty_nine_low,
		'cell_twenty_nine_high':cell_twenty_nine_high,
		'cell_twenty_nine_medium':cell_twenty_nine_medium,

		'cell_thirty_low':cell_thirty_low,
		'cell_thirty_high':cell_thirty_high,
		'cell_thirty_medium':cell_thirty_medium,

		#Row seven
		'cell_thirty_one_low':cell_thirty_one_low,
		'cell_thirty_one_high':cell_thirty_one_high,
		'cell_thirty_one_medium':cell_thirty_one_medium,

		'cell_thirty_two_low':cell_thirty_two_low,
		'cell_thirty_two_high':cell_thirty_two_high,
		'cell_thirty_two_medium':cell_thirty_two_medium,

		'cell_thirty_three_low':cell_thirty_three_low,
		'cell_thirty_three_high':cell_thirty_three_high,
		'cell_thirty_three_medium':cell_thirty_three_medium,

		'cell_thirty_four_low':cell_thirty_four_low,
		'cell_thirty_four_high':cell_thirty_four_high,
		'cell_thirty_four_medium':cell_thirty_four_medium,

		'cell_thirty_five_low':cell_thirty_five_low,
		'cell_thirty_five_high':cell_thirty_five_high,
		'cell_thirty_five_medium':cell_thirty_five_medium,

		#Row eight
		'cell_thirty_six_low':cell_thirty_six_low,
		'cell_thirty_six_high':cell_thirty_six_high,
		'cell_thirty_six_medium':cell_thirty_six_medium,

		'cell_thirty_seven_low':cell_thirty_seven_low,
		'cell_thirty_seven_high':cell_thirty_seven_high,
		'cell_thirty_seven_medium':cell_thirty_seven_medium,

		'cell_thirty_eight_low':cell_thirty_eight_low,
		'cell_thirty_eight_high':cell_thirty_eight_high,
		'cell_thirty_eight_medium':cell_thirty_eight_medium,

		'cell_thirty_nine_low':cell_thirty_nine_low,
		'cell_thirty_nine_high':cell_thirty_nine_high,
		'cell_thirty_nine_medium':cell_thirty_nine_medium,


		'cell_fourty_low':cell_fourty_low,
		'cell_fourty_high':cell_fourty_high,
		'cell_fourty_medium':cell_fourty_medium,

	}

	return render(request, 'core/index.html', context)



def search(request):
	if request.method == 'POST':
		theme = request.POST.get('theme')
		region = request.POST.get('region')
		country = request.POST.get('country')
		keyword = request.POST.get('keyword')
		category = request.POST.get('category')

		theme_data = Theme.objects.all().filter().order_by('theme_name')
		region_data = Region.objects.all().filter().order_by('region_name')
		country_data = Country.objects.all().filter().order_by('country_name')
		category_data = Category.objects.all().filter().order_by('category_name')
		
		study_data = Study.objects.filter(publish="Public")

		#If no search parameters are input
		if theme=="" and category=="" and region=="" and country=="" and keyword=="":
			#Row 1
			cell_one_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		#If all parameters are input
		elif theme!="" and category!="" and region!="" and country!="" and keyword!="":
			#Row 1
			cell_one_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_one_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_one_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_two_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_two_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_two_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_three_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_three_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_three_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_four_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_four_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_four_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_five_low = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_five_high = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_five_medium = Study.objects.filter(theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_six_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_six_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_seven_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_seven_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_seven_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_eight_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_eight_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_eight_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_nine_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_nine_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_nine_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_ten_low = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_ten_high = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_ten_medium = Study.objects.filter(theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Trends", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_eleven_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Trends", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_eleven_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_twelve_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twelve_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Enablers", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twelve_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_thirteen_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirteen_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Challenges", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirteen_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_fourteen_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_fourteen_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_fourteen_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_fifteen_low = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_fifteen_high = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_fifteen_medium = Study.objects.filter(theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_sixteen_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_sixteen_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_seventeen_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_seventeen_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_seventeen_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_eighteen_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_eighteen_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_eighteen_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_nineteen_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_nineteen_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_nineteen_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_twenty_low = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_high = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_medium = Study.objects.filter(theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_one_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_one_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_twenty_two_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_two_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_two_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_twenty_three_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_three_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_three_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_twenty_four_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_four_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_four_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_twenty_five_low = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_five_high = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_five_medium = Study.objects.filter(theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_six_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_six_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_twenty_seven_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_seven_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_twenty_eight_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_eight_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_twenty_nine_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_nine_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_thirty_low = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_high = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_medium = Study.objects.filter(theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_one_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_one_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_thirty_two_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_two_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_two_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_thirty_three_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_three_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_three_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_thirty_four_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_four_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_four_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_thirty_five_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_five_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_five_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_six_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_six_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_thirty_seven_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_seven_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_thirty_eight_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_eight_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_thirty_nine_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_nine_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")

			cell_fourty_low = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_fourty_high = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
			cell_fourty_medium = Study.objects.filter(theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", title__icontains=keyword, theme=theme, category=category, region=region, country=country, publish="Public")
						
		#Keyword Seach with other parameters
		elif keyword!="" and theme=="" and category=="" and region=="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(title__icontains=keyword, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword!="" and theme!="" and category=="" and region=="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(title__icontains=keyword, theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword!="" and theme=="" and category!="" and region=="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(title__icontains=keyword, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword!="" and theme=="" and category=="" and region!="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(title__icontains=keyword, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword!="" and theme=="" and category=="" and region=="" and country!="":			

			#Row One
			cell_one_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(title__icontains=keyword, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		#Keyword and Theme Combination
		elif keyword!="" and theme!="" and category!="" and region=="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(title__icontains=keyword, theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword!="" and theme!="" and category=="" and region!="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(title__icontains=keyword, theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword!="" and theme!="" and category=="" and region=="" and country!="":			

			#Row One
			cell_one_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(title__icontains=keyword, theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		#Keyword and category Combination
		elif keyword!="" and theme=="" and category!="" and region!="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(title__icontains=keyword, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword!="" and theme=="" and category!="" and region=="" and country!="":			

			#Row One
			cell_one_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(title__icontains=keyword, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		#Keyword and region combination
		elif keyword!="" and theme=="" and category=="" and region!="" and country!="":			

			#Row One
			cell_one_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(title__icontains=keyword, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		#Theme Search
		elif keyword=="" and theme!="" and category=="" and region=="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(theme=theme, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(theme=theme, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(theme=theme, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword=="" and theme!="" and category!="" and region=="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword=="" and theme!="" and category=="" and region!="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(theme=theme, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword=="" and theme!="" and category=="" and region=="" and country!="":			

			#Row One
			cell_one_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(theme=theme, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		#Theme and Category Search
		elif keyword=="" and theme!="" and category!="" and region=="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(theme=theme, category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword=="" and theme!="" and category!="" and region!="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(theme=theme, category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword=="" and theme!="" and category!="" and region=="" and country!="":			

			#Row One
			cell_one_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(theme=theme, category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		#Theme and region combination
		elif keyword=="" and theme!="" and category=="" and region!="" and country!="":			

			#Row One
			cell_one_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(theme=theme, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		#Category search
		elif keyword=="" and theme=="" and category!="" and region=="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(category=category, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(category=category, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(category=category, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(category=category, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(category=category, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(category=category, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(category=category, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(category=category, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword=="" and theme=="" and category!="" and region!="" and country=="":			

			#Row One
			cell_one_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(category=category, region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword=="" and theme=="" and category!="" and region=="" and country!="":

			#Row One
			cell_one_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(category=category, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		#Category region combination
		elif keyword=="" and theme=="" and category!="" and region!="" and country!="":

			#Row One
			cell_one_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(category=category, region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		#Region Search
		elif keyword=="" and theme=="" and category=="" and region!="" and country=="":

			#Row One
			cell_one_low = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(region=region, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(region=region, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(region=region, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(region=region, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(region=region, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(region=region, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(region=region, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(region=region, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		elif keyword=="" and theme=="" and category=="" and region!="" and country!="":

			#Row One
			cell_one_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(region=region, country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")
		
		#Country Search
		elif keyword=="" and theme=="" and category=="" and region=="" and country!="":

			#Row One
			cell_one_low = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Low", publish="Public")
			cell_one_high = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="High", publish="Public")
			cell_one_medium = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Trends", quality="Medium", publish="Public")

			cell_two_low = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Low", publish="Public")
			cell_two_high = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="High", publish="Public")
			cell_two_medium = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_three_low = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Low", publish="Public")
			cell_three_high = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="High", publish="Public")
			cell_three_medium = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_four_low = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_four_high = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_four_medium = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_five_low = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_five_high = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_five_medium = Study.objects.filter(country=country, theme__theme_name="Internet Governance", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")


			#Row two
			cell_six_low = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Low", publish="Public")
			cell_six_high = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="High", publish="Public")
			cell_six_medium = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seven_low = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seven_high = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="High", publish="Public")
			cell_seven_medium = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eight_low = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eight_high = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="High", publish="Public")
			cell_eight_medium = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nine_low = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nine_high = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nine_medium = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_ten_low = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_ten_high = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_ten_medium = Study.objects.filter(country=country, theme__theme_name="Internet for Democracy", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row three
			cell_eleven_low = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Low", publish="Public")
			cell_eleven_high = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="High", publish="Public")
			cell_eleven_medium = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twelve_low = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twelve_high = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="High", publish="Public")
			cell_twelve_medium = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirteen_low = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirteen_high = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirteen_medium = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_fourteen_low = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_fourteen_high = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_fourteen_medium = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fifteen_low = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fifteen_high = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fifteen_medium = Study.objects.filter(country=country, theme__theme_name="Digital content", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row four
			cell_sixteen_low = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Low", publish="Public")
			cell_sixteen_high = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="High", publish="Public")
			cell_sixteen_medium = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Trends", quality="Medium", publish="Public")

			cell_seventeen_low = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Low", publish="Public")
			cell_seventeen_high = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="High", publish="Public")
			cell_seventeen_medium = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_eighteen_low = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Low", publish="Public")
			cell_eighteen_high = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="High", publish="Public")
			cell_eighteen_medium = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_nineteen_low = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_nineteen_high = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_nineteen_medium = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_low = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_high = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_medium = Study.objects.filter(country=country, theme__theme_name="Internet Safety", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row five
			cell_twenty_one_low = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_one_high = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_one_medium = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_two_low = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_two_high = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_two_medium = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_three_low = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_three_high = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_three_medium = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_four_low = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_four_high = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_four_medium = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_twenty_five_low = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_twenty_five_high = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_twenty_five_medium = Study.objects.filter(country=country, theme__theme_name="Internet Based Entrepreneurship", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row six
			cell_twenty_six_low = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Low", publish="Public")
			cell_twenty_six_high = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="High", publish="Public")
			cell_twenty_six_medium = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Trends", quality="Medium", publish="Public")

			cell_twenty_seven_low = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Low", publish="Public")
			cell_twenty_seven_high = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="High", publish="Public")
			cell_twenty_seven_medium = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_twenty_eight_low = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Low", publish="Public")
			cell_twenty_eight_high = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="High", publish="Public")
			cell_twenty_eight_medium = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_twenty_nine_low = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_twenty_nine_high = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_twenty_nine_medium = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_low = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_high = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_medium = Study.objects.filter(country=country, theme__theme_name="Internet Access, Affordability And Use", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row seven
			cell_thirty_one_low = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_one_high = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_one_medium = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_two_low = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_two_high = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_two_medium = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_three_low = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_three_high = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_three_medium = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_four_low = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_four_high = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_four_medium = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_thirty_five_low = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_thirty_five_high = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_thirty_five_medium = Study.objects.filter(country=country, theme__theme_name="Digital Literacy And Skills", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

			#Row eight
			cell_thirty_six_low = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Low", publish="Public")
			cell_thirty_six_high = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="High", publish="Public")
			cell_thirty_six_medium = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Trends", quality="Medium", publish="Public")

			cell_thirty_seven_low = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Low", publish="Public")
			cell_thirty_seven_high = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="High", publish="Public")
			cell_thirty_seven_medium = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Enablers", quality="Medium", publish="Public")

			cell_thirty_eight_low = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Low", publish="Public")
			cell_thirty_eight_high = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="High", publish="Public")
			cell_thirty_eight_medium = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Challenges", quality="Medium", publish="Public")

			cell_thirty_nine_low = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Low", publish="Public")
			cell_thirty_nine_high = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="High", publish="Public")
			cell_thirty_nine_medium = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Outcomes and Impacts", quality="Medium", publish="Public")

			cell_fourty_low = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Low", publish="Public")
			cell_fourty_high = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="High", publish="Public")
			cell_fourty_medium = Study.objects.filter(country=country, theme__theme_name="Internet Or Digital Rights and Freedoms", category__category_name="Solutions or Strategies", quality="Medium", publish="Public")

		context = {		
			'study_data':study_data,
			'theme_data':theme_data, 
			'region_data':region_data,
			'country_data':country_data,
			'category_data':category_data,
			
			#Row one
			'cell_one_low':cell_one_low,
			'cell_one_high':cell_one_high,
			'cell_one_medium':cell_one_medium,

			'cell_two_low':cell_two_low,
			'cell_two_high':cell_two_high,
			'cell_two_medium':cell_two_medium,

			'cell_three_low':cell_three_low,
			'cell_three_high':cell_three_high,
			'cell_three_medium':cell_three_medium,

			'cell_four_low':cell_four_low,
			'cell_four_high':cell_four_high,
			'cell_four_medium':cell_four_medium,

			'cell_five_low':cell_five_low,
			'cell_five_high':cell_five_high,
			'cell_five_medium':cell_five_medium,

			#Row two
			'cell_six_low':cell_six_low,
			'cell_six_high':cell_six_high,
			'cell_six_medium':cell_six_medium,

			'cell_seven_low':cell_seven_low,
			'cell_seven_high':cell_seven_high,
			'cell_seven_medium':cell_seven_medium,

			'cell_eight_low':cell_eight_low,
			'cell_eight_high':cell_eight_high,
			'cell_eight_medium':cell_eight_medium,

			'cell_nine_low':cell_nine_low,
			'cell_nine_high':cell_nine_high,
			'cell_nine_medium':cell_nine_medium,

			'cell_ten_low':cell_ten_low,
			'cell_ten_high':cell_ten_high,
			'cell_ten_medium':cell_ten_medium,

			#Row three
			'cell_eleven_low':cell_eleven_low,
			'cell_eleven_high':cell_eleven_high,
			'cell_eleven_medium':cell_eleven_medium,

			'cell_twelve_low':cell_twelve_low,
			'cell_twelve_high':cell_twelve_high,
			'cell_twelve_medium':cell_twelve_medium,

			'cell_thirteen_low':cell_thirteen_low,
			'cell_thirteen_high':cell_thirteen_high,
			'cell_thirteen_medium':cell_thirteen_medium,

			'cell_fourteen_low':cell_fourteen_low,
			'cell_fourteen_high':cell_fourteen_high,
			'cell_fourteen_medium':cell_fourteen_medium,

			'cell_fifteen_low':cell_fifteen_low,
			'cell_fifteen_high':cell_fifteen_high,
			'cell_fifteen_medium':cell_fifteen_medium,

			#Row four
			'cell_sixteen_low':cell_sixteen_low,
			'cell_sixteen_high':cell_sixteen_high,
			'cell_sixteen_medium':cell_sixteen_medium,

			'cell_seventeen_low':cell_seventeen_low,
			'cell_seventeen_high':cell_seventeen_high,
			'cell_seventeen_medium':cell_seventeen_medium,

			'cell_eighteen_low':cell_eighteen_low,
			'cell_eighteen_high':cell_eighteen_high,
			'cell_eighteen_medium':cell_eighteen_medium,

			'cell_nineteen_low':cell_nineteen_low,
			'cell_nineteen_high':cell_nineteen_high,
			'cell_nineteen_medium':cell_nineteen_medium,

			'cell_twenty_low':cell_twenty_low,
			'cell_twenty_high':cell_twenty_high,
			'cell_twenty_medium':cell_twenty_medium,

			#Row five
			'cell_twenty_one_low':cell_twenty_one_low,
			'cell_twenty_one_high':cell_twenty_one_high,
			'cell_twenty_one_medium':cell_twenty_one_medium,

			'cell_twenty_two_low':cell_twenty_two_low,
			'cell_twenty_two_high':cell_twenty_two_high,
			'cell_twenty_two_medium':cell_twenty_two_medium,

			'cell_twenty_three_low':cell_twenty_three_low,
			'cell_twenty_three_high':cell_twenty_three_high,
			'cell_twenty_three_medium':cell_twenty_three_medium,

			'cell_twenty_four_low':cell_twenty_four_low,
			'cell_twenty_four_high':cell_twenty_four_high,
			'cell_twenty_four_medium':cell_twenty_four_medium,

			'cell_twenty_five_low':cell_twenty_five_low,
			'cell_twenty_five_high':cell_twenty_five_high,
			'cell_twenty_five_medium':cell_twenty_five_medium,

			#Row six
			'cell_twenty_six_low':cell_twenty_six_low,
			'cell_twenty_six_high':cell_twenty_six_high,
			'cell_twenty_six_medium':cell_twenty_six_medium,

			'cell_twenty_seven_low':cell_twenty_seven_low,
			'cell_twenty_seven_high':cell_twenty_seven_high,
			'cell_twenty_seven_medium':cell_twenty_seven_medium,

			'cell_twenty_eight_low':cell_twenty_eight_low,
			'cell_twenty_eight_high':cell_twenty_eight_high,
			'cell_twenty_eight_medium':cell_twenty_eight_medium,

			'cell_twenty_nine_low':cell_twenty_nine_low,
			'cell_twenty_nine_high':cell_twenty_nine_high,
			'cell_twenty_nine_medium':cell_twenty_nine_medium,

			'cell_thirty_low':cell_thirty_low,
			'cell_thirty_high':cell_thirty_high,
			'cell_thirty_medium':cell_thirty_medium,

			#Row seven
			'cell_thirty_one_low':cell_thirty_one_low,
			'cell_thirty_one_high':cell_thirty_one_high,
			'cell_thirty_one_medium':cell_thirty_one_medium,

			'cell_thirty_two_low':cell_thirty_two_low,
			'cell_thirty_two_high':cell_thirty_two_high,
			'cell_thirty_two_medium':cell_thirty_two_medium,

			'cell_thirty_three_low':cell_thirty_three_low,
			'cell_thirty_three_high':cell_thirty_three_high,
			'cell_thirty_three_medium':cell_thirty_three_medium,

			'cell_thirty_four_low':cell_thirty_four_low,
			'cell_thirty_four_high':cell_thirty_four_high,
			'cell_thirty_four_medium':cell_thirty_four_medium,

			'cell_thirty_five_low':cell_thirty_five_low,
			'cell_thirty_five_high':cell_thirty_five_high,
			'cell_thirty_five_medium':cell_thirty_five_medium,

			#Row eight
			'cell_thirty_six_low':cell_thirty_six_low,
			'cell_thirty_six_high':cell_thirty_six_high,
			'cell_thirty_six_medium':cell_thirty_six_medium,

			'cell_thirty_seven_low':cell_thirty_seven_low,
			'cell_thirty_seven_high':cell_thirty_seven_high,
			'cell_thirty_seven_medium':cell_thirty_seven_medium,

			'cell_thirty_eight_low':cell_thirty_eight_low,
			'cell_thirty_eight_high':cell_thirty_eight_high,
			'cell_thirty_eight_medium':cell_thirty_eight_medium,

			'cell_thirty_nine_low':cell_thirty_nine_low,
			'cell_thirty_nine_high':cell_thirty_nine_high,
			'cell_thirty_nine_medium':cell_thirty_nine_medium,


			'cell_fourty_low':cell_fourty_low,
			'cell_fourty_high':cell_fourty_high,
			'cell_fourty_medium':cell_fourty_medium,

		}

		return render(request, 'core/search_result.html', context)	
	else:
		return redirect('home_page')



def search_two(request):
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


