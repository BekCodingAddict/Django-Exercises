import django.forms as ModelsForm
from .models import Room

class RoomForm(ModelsForm.ModelForm):
	class Meta:
		model = Room
		fields = '__all__'
		