from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Category(models.Model):	
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	category_name = models.CharField(_('Category Name'), max_length=255, blank=False, null=False)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.category_name


class Country(models.Model):
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	country_name = models.CharField(_('Country Name'), max_length=255, blank=False, null=False)
	continent_name = models.CharField(_('Continent Name'), max_length=255, blank=False, null=False)	
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Countries'

	def __str__(self):
		return self.country_name


class Quality(models.Model):
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	quality_name = models.CharField(_('Quality'), max_length=255, blank=False, null=False)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Quality"
		verbose_name_plural = "Qualities"

	def __str__(self):
		return self.quality_name

class Region(models.Model):
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	region_name = models.CharField(_('Region'), max_length=255, blank=False, null=False)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Region"
		verbose_name_plural = "Regions"

	def __str__(self):
		return self.region_name

class Resource(models.Model):
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	resource_name = models.CharField(_('Resource'), max_length=255, blank=False, null=False)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)

	class Meta:
		verbose_name = "Resource"
		verbose_name_plural = "Resources"

	def __str__(self):
		return self.resource_name
