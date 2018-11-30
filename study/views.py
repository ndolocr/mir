import csv, io
import openpyxl
from study.models import Category
from django.shortcuts import render
from django.contrib import messages

# Create your views here.

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
			return render(request, "study/category_confirm.html", {"excel_data":excel_data})


	#context = {}
	#return render(request, template, context)

def country_upload(request):
	template = "study/country_upload.html"
	context = {}
	return render(request, template, context)

def quality_upload(request):
	template = "study/quality_upload.html"
	context = {}
	return render(request, template, context)

def region_upload(request):
	template = "study/region_upload.html"
	context = {}
	return render(request, template, context)

def resource_upload(request):
	template = "study/resource_upload.html"
	context = {}
	return render(request, template, context)

def study_upload(request):
	template = "study/study_upload.html"
	context = {}
	return render(request, template, context)

def sub_category_upload(request):
	template = "study/sub_category_upload.html"
	context = {}
	return render(request, template, context)

def sub_theme_upload(request):
	template = "study/sub_theme_upload.html"
	context = {}
	return render(request, template, context)

def tag_upload(request):
	template = "study/tag_upload.html"
	context = {}
	return render(request, template, context)

def theme_upload(request):
	template = "study/theme_upload.html"
	context = {}
	return render(request, template, context)

def study_upload(request):
	template = "study/study_upload.html"
	context = {}
	return render(request, template, context)
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