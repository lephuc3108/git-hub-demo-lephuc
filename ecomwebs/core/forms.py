from django import forms
from .models import Join, Login
from django_countries.fields import CountryField

# form dang ky
class JoinIn(forms.ModelForm):
	class Meta:
		model = Join
		fields = ('username', 'password', 'password_again')



'''class LogIn(forms.ModelForm):
	class Meta:
		model = Login
		fields = ('username', 'password', 'remember')'''


# form dang nhap
class LogIn(forms.Form):
	username = forms.CharField(max_length=155)
	password = forms.CharField(max_length=100)
	remember = forms.BooleanField()

	def __str__(self):
		return self.username



# trang thanh toan 
class CheckOut(forms.Form):
	street_address = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'City',
		'class': 'input'
		}))
	apartment_address = forms.CharField(widget=forms.TextInput(attrs={
		'placeholder': 'Address',
		'class': 'input'
		}))
	country = CountryField(blank_label='(select country)').formfield(attrs={
		'class': 'input'
		})
	zip = forms.CharField()
	telephone = forms.IntegerField()
	same_billing_address = forms.BooleanField(widget=forms.CheckboxInput)
	save_info = forms.BooleanField(widget=forms.CheckboxInput)
	payment_option = forms.BooleanField(widget=forms.RadioSelect())
	bank = forms.CharField()
	card_number = forms.IntegerField()

