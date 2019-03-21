from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
# Create your models here.

'''
CATEGORY MODEL
'''
class Category(models.Model):	

	category_name = models.CharField(_('Category Name'), max_length=255, unique=True, blank=False, null=False)
	
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)	
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)	
	#created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.category_name

'''
COUNTRY MODEL
'''
class Country(models.Model):
	country_name = models.CharField(_('Country Name'), max_length=255, blank=False, null=False)
	#continent_name = models.CharField(_('Continent Name'), max_length=255, unique=True, blank=False, null=False)	

	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)		
	#created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Countries'

	def __str__(self):
		return self.country_name

'''
QUALITY MODEL
'''
class Quality(models.Model):	
	quality_name = models.CharField(_('Quality'), max_length=255, unique=True, blank=False, null=False)

	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	#created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Quality"
		verbose_name_plural = "Qualities"

	def __str__(self):
		return self.quality_name

'''
REGION MODEL
'''
class Region(models.Model):
	region_name = models.CharField(_('Region'), max_length=255, unique=True, blank=False, null=False)

	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	#created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Region"
		verbose_name_plural = "Regions"

	def __str__(self):
		return self.region_name

'''
RESOURCE MODEL
'''
class Resource(models.Model):
	resource_name = models.CharField(_('Resource'), max_length=255, unique=True, blank=False, null=False)

	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	#created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Resource"
		verbose_name_plural = "Resources"

	def __str__(self):
		return self.resource_name

'''
THEME MODEL
'''
class Theme(models.Model):
	theme_name = models.CharField(_('Theme'), max_length=255, unique=True, blank=False, null=False)

	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	#created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Theme"
		verbose_name_plural = "Theme"

	def __str__(self):
		return self.theme_name

'''
SUB THEME MODEL
'''
class SubTheme(models.Model):	
	sub_theme_name = models.CharField(_('Sub Theme'), max_length=255, unique=True, blank=False, null=False)
	theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	#created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Sub Theme"
		verbose_name_plural = "Sub Themes"

	def __str__(self):
		return self.sub_theme_name

'''
SUB CATEGORY MODEL
'''
class SubCategory(models.Model):
	sub_category_name = models.CharField(_('Sub Category'), max_length=255, unique=True, blank=False, null=False)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)		
	
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	#created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Sub Category"
		verbose_name_plural = "Sub Categories"

	def __str__(self):
		return self.sub_category_name

'''
TAG MODEL
'''
class Tag(models.Model):
	tag_name = models.CharField(_('Tag'), max_length=255, unique=True, blank=False, null=False)

	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	#created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Tag"
		verbose_name_plural = "Tags"

	def __str__(self):
		return self.tag_name

'''
STUDY MODEL
'''
class Study(models.Model):
	
	QUALITY_CHOICES = (
        ('Low', 'Low'),
        ('High', 'High'),
        ('Medium', 'Medium'),        
    )
	
	PUBLISH_CHOICES = (
		('Public', 'Public'),
		('Private', 'Private'),		
	)

	'''
	THEME_CHOICES = (
        ('Digital Content', 'Digital Content'),
        ('Digital Literacy', 'Digital Literacy'),
        ('Internet Access and Use', 'Internet Access and Use'),
        ('Internet/Digital Safety', 'Internet/Digital Safety'),
        ('Internet/ICT for Democracy', 'Internet/ICT for Democracy'),
        ('Internet/Digital Governance', 'Internet/Digital Governance'),
        ('Internet Based Entrepreneurship', 'Internet Based Entrepreneurship'),
        ('Internet/Digital Rights and Freedoms', 'Internet/Digital Rights and Freedoms'),
    )	
	'''
	
	title = models.CharField(_('Title'), max_length=255, blank=False, null=False)
	author = models.CharField(_('Author'), max_length=255, blank=False, null=False)
	link = models.CharField(_('link'), max_length=255, blank=False, null=False)
	description = models.TextField(_('Description'), blank=True, default='')
	#tags = models.ManyToManyField(Tag)
	year = models.PositiveIntegerField(_('Year'))
	'''FOREGIN KEY FIELDS'''
	region = models.ManyToManyField(Region)
	country = models.ManyToManyField(Country)
	theme = models.ManyToManyField(Theme)	
	category = models.ManyToManyField(Category)
	resource = models.ForeignKey(Resource, default=1, on_delete=models.CASCADE)	
	quality = models.CharField(_('Quality'), max_length=6, choices=QUALITY_CHOICES, default='Low')
	publish =  models.CharField(_('Publish'), max_length=7, choices=PUBLISH_CHOICES, default='Private')

	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	#created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Study"
		verbose_name_plural = "Studies"

	def __str__(self):
		return self.title
