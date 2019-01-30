from study.models import Study
from rest_framework.serializers import ModelSerializer

class StudySerializer(ModelSerializer):
	class Meta:
		model = Study
		fields=[
			'id',
			'title',
			'link',
		]