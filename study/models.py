from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Category(models.Model):	
	updated_on = models.DateTimeField(_('Updated On'), auto_now=True)
	created_on = models.DateTimeField(_('Created On'), auto_now_add=True)
	category_name = models.CharField(_('Category Name'), max_length=255, blank=False, null=False)
	created_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)