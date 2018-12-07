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
	
def download_sub_theme_template(request):
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