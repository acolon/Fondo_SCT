from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CunaUser 

# ============================================================
# ============================================================

class CunaUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = CunaUser
		fields = ( 'username', 'email', 'miembro' )


class CunaUserChangeForm(UserChangeForm):

	class Meta:
		model = CunaUser
		fields = ( 'username', 'email', 'miembro' )
