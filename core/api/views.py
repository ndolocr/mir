from study.models import Study
from rest_framework.generics import ListAPIView
from core.api.serializers import StudySerializer

class StudyListAPIView(ListAPIView):
	queryset = Study.objects.all()
	serializer_class = StudySerializer