# import xlwt using: pip install xlwt
import io
import os
import csv
import xlwt
import openpyxl
from django.conf import settings
from django.http import HttpResponse

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

from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.

'''
	Starts Upload Category
'''
def category_upload(request):
	upload_template = "study/category_upload.html"
	prompt = {}

	if request.method == "GET":
		return render(request, upload_template, prompt)
	else:
		#Capture uploaded file
		excel_file = request.FILES['file_upload']

		#validation to ensure file is excel file
		if not excel_file.name.endswith('.xlsx'):
			messages.error(request, 'This is not an excel file')
		else:
			wb = openpyxl.load_workbook(excel_file)

			# getting a particular sheet by name out of many sheets
			worksheet = wb["Sheet1"]
			#print(worksheet)

			excel_data = list()
			# iterating over the rows and
			# getting value from each cell in row
			x = 1
			for row in worksheet.iter_rows():
				row_data = list()				
				if x>1:
					for cell in row:
						if cell !="":
							row_data.append(str(cell.value))
					excel_data.append(row_data)
				x = x + 1

			request.session['list'] = excel_data
			return render(request, "study/category_confirm.html", {"excel_data":excel_data})


def category_upload_confirm(request):
	
	if request.method == "POST":
		#excel_data = []
		excel_data = request.session['list']

		for row in excel_data:
			for cell in row:
				_, object_instance = Category.objects.update_or_create(
					category_name = cell,
				)
		return redirect('admin:index')


def download_category(request):
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')
	
	#decide file name
	response['Content-Disposition'] = 'attachment; filename="category_list.xls"'

	#creating workbook
	wrkbook = xlwt.Workbook(encoding='utf-8')

	#Category Worksheet
	wrksheet = wrkbook.add_sheet("category")

	data = Category.objects.all()

	row_num = 0

	#Styling Headers
	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True

	#column header names
	columns = ['Category Name',]

	#write column headers in sheet
	for col_num in range(len(columns)):
		wrksheet.write(row_num, col_num, columns[col_num], font_style)

	#Writting content on excel sheet
	for my_row in data:
		row_num = row_num + 1
		#category_wrksheet.write(category_row_num, 0, my_row.id)
		wrksheet.write(row_num, 0, my_row.category_name)		

	wrkbook.save(response)
	return response


'''
	End Upload Category
'''

'''
	Start Upload Country Information
'''

def country_upload(request):
	upload_template = "study/country_upload.html"
	prompt = {}

	if request.method == "GET":
		return render(request, upload_template, prompt)
	else:
		#Capture uploaded file
		excel_file = request.FILES['file_upload']

		#validation to ensure file is excel file
		if not excel_file.name.endswith('.xlsx'):
			messages.error(request, 'This is not an excel file')
		else:
			wb = openpyxl.load_workbook(excel_file)

			# getting a particular sheet by name out of many sheets
			worksheet = wb["Sheet1"]
			#print(worksheet)

			excel_data = list()
			# iterating over the rows and
			# getting value from each cell in row
			x = 1
			for row in worksheet.iter_rows():
				row_data = list()				
				if x>1:
					for cell in row:
						if cell !="":
							row_data.append(str(cell.value))
					excel_data.append(row_data)
				x = x + 1

			request.session['list'] = excel_data
			return render(request, "study/country_confirm.html", {"excel_data":excel_data})


def country_upload_confirm(request):
	
	if request.method == "POST":
		#excel_data = []
		excel_data = request.session['list']

		for row in excel_data:
			for cell in row:
				_, object_instance = Country.objects.update_or_create(
					country_name = cell,
				)
		return redirect('admin:index')

def download_country(request):
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')
	
	#decide file name
	response['Content-Disposition'] = 'attachment; filename="country_list.xls"'

	#creating workbook
	wrkbook = xlwt.Workbook(encoding='utf-8')

	#Category Worksheet
	wrksheet = wrkbook.add_sheet("country")

	data = Country.objects.all()

	row_num = 0

	#Styling Headers
	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True

	#column header names
	columns = ['Country Name',]

	#write column headers in sheet
	for col_num in range(len(columns)):
		wrksheet.write(row_num, col_num, columns[col_num], font_style)

	#Writting content on excel sheet
	for my_row in data:
		row_num = row_num + 1
		wrksheet.write(row_num, 0, my_row.country_name)		

	wrkbook.save(response)
	return response

'''
	End Upload Country Information
'''


'''
	Start Upload Quality Information
'''

def quality_upload(request):
	upload_template = "study/quality_upload.html"
	prompt = {}

	if request.method == "GET":
		return render(request, upload_template, prompt)
	else:
		#Capture uploaded file
		excel_file = request.FILES['file_upload']

		#validation to ensure file is excel file
		if not excel_file.name.endswith('.xlsx'):
			messages.error(request, 'This is not an excel file')
		else:
			wb = openpyxl.load_workbook(excel_file)

			# getting a particular sheet by name out of many sheets
			worksheet = wb["Sheet1"]
			#print(worksheet)

			excel_data = list()
			# iterating over the rows and
			# getting value from each cell in row
			x = 1
			for row in worksheet.iter_rows():
				row_data = list()				
				if x>1:
					for cell in row:
						if cell !="":
							row_data.append(str(cell.value))
					excel_data.append(row_data)
				x = x + 1

			request.session['list'] = excel_data
			return render(request, "study/quality_confirm.html", {"excel_data":excel_data})


def quality_upload_confirm(request):
	
	if request.method == "POST":
		#excel_data = []
		excel_data = request.session['list']

		for row in excel_data:
			for cell in row:
				_, object_instance = Quality.objects.update_or_create(
					quality_name = cell,
				)
		return redirect('admin:index')


def download_quality(request):
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')
	
	#decide file name
	response['Content-Disposition'] = 'attachment; filename="quality_list.xls"'

	#creating workbook
	wrkbook = xlwt.Workbook(encoding='utf-8')

	#Category Worksheet
	wrksheet = wrkbook.add_sheet("quality")

	data = Quality.objects.all()

	row_num = 0

	#Styling Headers
	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True

	#column header names
	columns = ['Quality Name',]

	#write column headers in sheet
	for col_num in range(len(columns)):
		wrksheet.write(row_num, col_num, columns[col_num], font_style)

	#Writting content on excel sheet
	for my_row in data:
		row_num = row_num + 1
		wrksheet.write(row_num, 0, my_row.quality_name)		

	wrkbook.save(response)
	return response


'''
	End Upload Quality Information
'''


'''
	Start Upload Region Information
'''

def region_upload(request):
	upload_template = "study/region_upload.html"
	prompt = {}

	if request.method == "GET":
		return render(request, upload_template, prompt)
	else:
		#Capture uploaded file
		excel_file = request.FILES['file_upload']

		#validation to ensure file is excel file
		if not excel_file.name.endswith('.xlsx'):
			messages.error(request, 'This is not an excel file')
		else:
			wb = openpyxl.load_workbook(excel_file)

			# getting a particular sheet by name out of many sheets
			worksheet = wb["Sheet1"]
			#print(worksheet)

			excel_data = list()
			# iterating over the rows and
			# getting value from each cell in row
			x = 1
			for row in worksheet.iter_rows():
				row_data = list()				
				if x>1:
					for cell in row:
						if cell !="":
							row_data.append(str(cell.value))
					excel_data.append(row_data)
				x = x + 1

			request.session['list'] = excel_data
			return render(request, "study/region_confirm.html", {"excel_data":excel_data})


def region_upload_confirm(request):
	
	if request.method == "POST":
		#excel_data = []
		excel_data = request.session['list']

		for row in excel_data:
			for cell in row:
				_, object_instance = Region.objects.update_or_create(
					region_name = cell,
				)
		return redirect('admin:index')


def download_region(request):
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')
	
	#decide file name
	response['Content-Disposition'] = 'attachment; filename="region_list.xls"'

	#creating workbook
	wrkbook = xlwt.Workbook(encoding='utf-8')

	#Category Worksheet
	wrksheet = wrkbook.add_sheet("region")

	data = Region.objects.all()

	row_num = 0

	#Styling Headers
	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True

	#column header names
	columns = ['Region Name',]

	#write column headers in sheet
	for col_num in range(len(columns)):
		wrksheet.write(row_num, col_num, columns[col_num], font_style)

	#Writting content on excel sheet
	for my_row in data:
		row_num = row_num + 1
		wrksheet.write(row_num, 0, my_row.region_name)		

	wrkbook.save(response)
	return response


'''
	End Upload Region Information
'''


'''
	Start Upload Resource Information
'''

def resource_upload(request):
	upload_template = "study/resource_upload.html"
	prompt = {}

	if request.method == "GET":
		return render(request, upload_template, prompt)
	else:
		#Capture uploaded file
		excel_file = request.FILES['file_upload']

		#validation to ensure file is excel file
		if not excel_file.name.endswith('.xlsx'):
			messages.error(request, 'This is not an excel file')
		else:
			wb = openpyxl.load_workbook(excel_file)

			# getting a particular sheet by name out of many sheets
			worksheet = wb["Sheet1"]
			#print(worksheet)

			excel_data = list()
			# iterating over the rows and
			# getting value from each cell in row
			x = 1
			for row in worksheet.iter_rows():
				row_data = list()				
				if x>1:
					for cell in row:
						if cell !="":
							row_data.append(str(cell.value))
					excel_data.append(row_data)
				x = x + 1

			request.session['list'] = excel_data
			return render(request, "study/resource_confirm.html", {"excel_data":excel_data})


def resource_upload_confirm(request):
	
	if request.method == "POST":
		#excel_data = []
		excel_data = request.session['list']

		for row in excel_data:
			for cell in row:
				_, object_instance = Resource.objects.update_or_create(
					resource_name = cell,
				)
		return redirect('admin:index')

'''
	End Upload Resource Information
'''

'''
	Start Upload Theme Information
'''

def theme_upload(request):
	upload_template = "study/theme_upload.html"
	prompt = {}

	if request.method == "GET":
		return render(request, upload_template, prompt)
	else:
		#Capture uploaded file
		excel_file = request.FILES['file_upload']

		#validation to ensure file is excel file
		if not excel_file.name.endswith('.xlsx'):
			messages.error(request, 'This is not an excel file')
		else:
			wb = openpyxl.load_workbook(excel_file)

			# getting a particular sheet by name out of many sheets
			worksheet = wb["Sheet1"]
			#print(worksheet)

			excel_data = list()
			# iterating over the rows and
			# getting value from each cell in row
			x = 1
			for row in worksheet.iter_rows():
				row_data = list()				
				if x>1:
					for cell in row:
						if cell !="":
							row_data.append(str(cell.value))
					excel_data.append(row_data)
				x = x + 1

			request.session['list'] = excel_data
			return render(request, "study/theme_confirm.html", {"excel_data":excel_data})


def theme_upload_confirm(request):
	
	if request.method == "POST":
		#excel_data = []
		excel_data = request.session['list']

		for row in excel_data:
			for cell in row:
				_, object_instance = Theme.objects.update_or_create(
					theme_name = cell,
				)
		return redirect('admin:index')

'''
	End Upload Theme Information
'''

'''
	Start Upload Tags Information
'''

def tag_upload(request):
	upload_template = "study/tag_upload.html"
	prompt = {}

	if request.method == "GET":
		return render(request, upload_template, prompt)
	else:
		#Capture uploaded file
		excel_file = request.FILES['file_upload']

		#validation to ensure file is excel file
		if not excel_file.name.endswith('.xlsx'):
			messages.error(request, 'This is not an excel file')
		else:
			wb = openpyxl.load_workbook(excel_file)

			# getting a particular sheet by name out of many sheets
			worksheet = wb["Sheet1"]
			#print(worksheet)

			excel_data = list()
			# iterating over the rows and
			# getting value from each cell in row
			x = 1
			for row in worksheet.iter_rows():
				row_data = list()				
				if x>1:
					for cell in row:
						if cell !="":
							row_data.append(str(cell.value))
					excel_data.append(row_data)
				x = x + 1

			request.session['list'] = excel_data
			return render(request, "study/tag_confirm.html", {"excel_data":excel_data})


def tag_upload_confirm(request):
	
	if request.method == "POST":
		#excel_data = []
		excel_data = request.session['list']

		for row in excel_data:
			for cell in row:
				_, object_instance = Tag.objects.update_or_create(
					tag_name = cell,
				)
		return redirect('admin:index')

'''
	End Upload Tag Information
'''

'''
	Start upload Sub Theme Information
'''
def sub_theme_upload(request):
	upload_template = "study/sub_theme_upload.html"
	prompt = {}

	if request.method == "GET":
		return render(request, upload_template, prompt)
	else:
		#Capture uploaded file
		excel_file = request.FILES['file_upload']

		#validation to ensure file is excel file
		if not excel_file.name.endswith('.xlsx'):
			messages.error(request, 'This is not an excel file')
		else:
			wb = openpyxl.load_workbook(excel_file)

			# getting a particular sheet by name out of many sheets
			worksheet = wb["Sheet1"]
			#print(worksheet)

			excel_data = list()
			# iterating over the rows and
			# getting value from each cell in row
			x = 1
			for row in worksheet.iter_rows():
				row_data = list()				
				if x>1:
					for cell in row:
						if cell !="":
							row_data.append(str(cell.value))
					excel_data.append(row_data)
				x = x + 1

			request.session['list'] = excel_data
			return render(request, "study/sub_theme_confirm.html", {"excel_data":excel_data})


def sub_theme_upload_confirm(request):
	
	if request.method == "POST":
		#excel_data = []
		excel_data = request.session['list']

		for row in excel_data:
			got_sub_theme_name = row[0]	
			theme_instance = int(row[1])	
			theme_object = Theme.objects.get(id = theme_instance)
			_, object_instance = SubTheme.objects.update_or_create(
				sub_theme_name = got_sub_theme_name,
				theme = theme_object,
			)	
		return redirect('admin:index')
'''
	End Upload of Sub Theme Information
'''

'''
	Start Upload of Sub Category Information
'''

def sub_category_upload(request):
	upload_template = "study/sub_category_upload.html"
	prompt = {}

	if request.method == "GET":
		return render(request, upload_template, prompt)
	else:
		#Capture uploaded file
		excel_file = request.FILES['file_upload']

		#validation to ensure file is excel file
		if not excel_file.name.endswith('.xlsx'):
			messages.error(request, 'This is not an excel file')
		else:
			wb = openpyxl.load_workbook(excel_file)

			# getting a particular sheet by name out of many sheets
			worksheet = wb["Sheet1"]
			#print(worksheet)

			excel_data = list()
			# iterating over the rows and
			# getting value from each cell in row
			x = 1
			for row in worksheet.iter_rows():
				row_data = list()				
				if x>1:
					for cell in row:
						if cell !="":
							row_data.append(str(cell.value))
					excel_data.append(row_data)
				x = x + 1

			request.session['list'] = excel_data
			return render(request, "study/sub_category_confirm.html", {"excel_data":excel_data})


def sub_category_upload_confirm(request):
	
	if request.method == "POST":
		#excel_data = []
		excel_data = request.session['list']

		for row in excel_data:
			got_sub_category_name = row[0]	
			category_instance = int(row[1])	
			category_object = Category.objects.get(id = category_instance)
			_, object_instance = SubCategory.objects.update_or_create(
				sub_category_name = got_sub_category_name,
				category = category_object,
			)	
		return redirect('admin:index')
'''
	End Upload of Sub Category Information
'''



def study_upload(request):
	template = "study/study_upload.html"
	context = {}
	return render(request, template, context)



def download_template(request, file_name):	
	file_path = os.path.join(settings.MEDIA_ROOT, file_name)
	if os.path.exists(file_path):
		with open(file_path, 'rb') as fh:
			response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
			response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
			return response 


	
def download_category_template(request):
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')
	
	#decide file name
	response['Content-Disposition'] = 'attachment; filename="list.xls"'

	#creating workbook
	wrkbook = xlwt.Workbook(encoding='utf-8')

	#Theme Worksheet
	#theme_wrksheet = wrkbook.add_sheet("sheet1")
	region_wrksheet = wrkbook.add_sheet("region")

	region_data = Region.objects.all()
	region_row_num = 0
	#Writting content on excel sheet
	for my_row in region_data:
		region_wrksheet.write(region_row_num, 0, my_row.id)
		region_wrksheet.write(region_row_num, 1, my_row.region_name)
		region_row_num = region_row_num + 1

	country_wrksheet = wrkbook.add_sheet("country")
	country_data = Country.objects.all()
	country_row_num = 0
	#Writting content on excel sheet
	for my_row in country_data:
		country_wrksheet.write(country_row_num, 0, my_row.id)
		country_wrksheet.write(country_row_num, 1, my_row.country_name)
		country_row_num = country_row_num + 1

	quality_wrksheet = wrkbook.add_sheet("quality")
	quality_data = Quality.objects.all()
	quality_row_num = 0
	#Writting content on excel sheet
	for my_row in quality_data:
		quality_wrksheet.write(quality_row_num, 0, my_row.id)
		quality_wrksheet.write(quality_row_num, 1, my_row.quality_name)
		quality_row_num = quality_row_num + 1

	#category_wrksheet = wrkbook.add_sheet("sheet5")
	resource_wrksheet = wrkbook.add_sheet("resource")
	resource_data = Resource.objects.all()
	resource_row_num = 0
	#Writting content on excel sheet
	for my_row in resource_data:
		resource_wrksheet.write(resource_row_num, 0, my_row.id)
		resource_wrksheet.write(resource_row_num, 1, my_row.resource_name)
		resource_row_num = resource_row_num + 1

	sub_theme_wrksheet = wrkbook.add_sheet("sub_theme")
	sub_theme_data = SubTheme.objects.all()
	sub_theme_row_num = 0
	#Writting content on excel sheet
	for my_row in sub_theme_data:
		sub_theme_wrksheet.write(sub_theme_row_num, 0, my_row.id)
		sub_theme_wrksheet.write(sub_theme_row_num, 1, my_row.sub_theme_name)
		sub_theme_row_num = sub_theme_row_num + 1

	sub_categroy_wrksheet = wrkbook.add_sheet("sub_category")
	sub_categroy_data = SubCategory.objects.all()
	sub_categroy_row_num = 0
	#Writting content on excel sheet
	for my_row in sub_categroy_data:
		sub_categroy_wrksheet.write(sub_categroy_row_num, 0, my_row.id)
		sub_categroy_wrksheet.write(sub_categroy_row_num, 1, my_row.sub_category_name)
		sub_categroy_row_num = sub_categroy_row_num + 1
	'''
	#Category 
	country_data = Country.objects.all()
	country_row_num = 0
	#Writting content on excel sheet
	for my_row in country_data:
		country_wrksheet.write(country_row_num, 0, my_row.id)
		country_wrksheet.write(country_row_num, 1, my_row.country_name)
		country_row_num = country_row_num + 1

	#Category 
	category_data = Category.objects.all()
	category_row_num = 0
	#Writting content on excel sheet
	for my_row in category_data:
		category_wrksheet.write(category_row_num, 0, my_row.id)
		category_wrksheet.write(category_row_num, 1, my_row.category_name)
		category_row_num = category_row_num + 1

	'''
	wrkbook.save(response)
	return response

	'''
	#determining file 
	file_name = 'Category.xlsx'
	file_path = os.path.join(settings.MEDIA_ROOT, file_name)	
	# content-type of response
	response = HttpResponse(content_type='application/ms-excel')
	#decide file name
	#response['Content-Disposition'] = 'attachment; filename="Sub_Theme.xlsx"'
	wrkbook = response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
	
	#creating workbook
	#wrkbook = xlwt.Workbook(encoding='utf-8')

	#adding sheet
	wrksheet_two = wrkbook.add_sheet("sheet2")

	#get your data, from database or from a text file...
	data = Theme.objects.all()

	row_num = 0
	#Writting content on excel sheet
	for my_row in data:
		wrksheet_two.write(row_num, 0, my_row.id)
		wrksheet_two.write(row_num, 1, my_row.sub_theme_name)

	wrkbook.save()
	return wrkbook
	'''
'''
def study_upload(request):
	template = "study/study_upload.html"
	context = {}
	return render(request, template, context)
'''


'''
def category_upload(request):
	template = "study/category_upload.html"

	prompt = {
		'order': 'Kindly list category names to be uploaded: '
	}

	if request.method=="GET":
		return render(request, template, prompt)

	csv_file = request.FILES['file_upload']

	if not csv_file.name.endswith('.xlsx'):
		messages.error(request, 'This is not an excel file')

	#data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)

	for column in csv.reader(io_string, delimiter='', quotechar="|"):
		_, created = Category.objects.update_or_create(
			category_name = column[0],
		)

	context ={}

	return render(request, template, context)


def index(request):
	template = "study/category_upload.html"

	if request.method=="GET":
		return render(request, template, {})
	else:
		excel_file = request.FILES["file_upload"]

		# you may put validations here to check extension or file size

		wb = openpyxl.load_workbook(excel_file)

		# getting a particular sheet by name out of many sheets
		worksheet = wb["Sheet1"]
		#print(worksheet)

		excel_data = list()
		# iterating over the rows and
		# getting value from each cell in row
		for row in worksheet.iter_rows():
			row_data = list()
			for cell in row:
				row_data.append(str(cell.value))
			excel_data.append(row_data)

		return render(request, "study/category_confirm.html", {"excel_data":excel_data})

'''