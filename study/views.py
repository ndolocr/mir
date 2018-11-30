import csv, io
from study.models import Category
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
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

	data_set = csv_file.read().decode('UTF-8')
	io_string = io.StringIO(data_set)
	next(io_string)

	for column in csv.reader(io_string, delimiter='', quotechar="|"):
		_, created = Category.objects.update_or_create(
			category_name = column[0],
		)

	context ={}

	return render(request, template, context)