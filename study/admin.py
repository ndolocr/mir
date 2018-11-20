from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

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

# Register your models here.

admin.site.register(Tag)
#admin.site.register(Study)
admin.site.register(Theme)
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(Quality)
admin.site.register(Category)
admin.site.register(Resource)
admin.site.register(SubTheme)
admin.site.register(SubCategory)

@admin.register(Study)
class ViewAdmin(ImportExportModelAdmin):
	pass
