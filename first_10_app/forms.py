# -*- coding: utf-8 -*-
from django import forms

from first_10_app.models import Member

class MemberForm(forms.ModelForm):
	name = forms.CharField(error_messages={'required': 'Upps! Burayı atladın'})
	name0 = forms.CharField(error_messages={'required': 'Upps! Burayı atladın'})
	name1 = forms.CharField(error_messages={'required': 'Upps! Burayı atladın'})
	name2 = forms.CharField(error_messages={'required': 'Upps! Burayı atladın'})
	name3 = forms.CharField(error_messages={'required': 'Upps! Burayı atladın'})
	name4 = forms.CharField(error_messages={'required': 'Upps! Burayı atladın'})
	name5 = forms.CharField(error_messages={'required': 'Upps! Burayı atladın'})
	name6 = forms.CharField(error_messages={'required': 'Upps! Burayı atladın'})
	name7 = forms.CharField(error_messages={'required': 'Upps! Burayı atladın'})
	name8 = forms.CharField(error_messages={'required': 'Upps! Burayı atladın'})
	name9 = forms.CharField(error_messages={'required': 'Upps! Burayı atladın'})



	
	class Meta:
		model = Member
		fields = [
		"name",
		"name0",
		"name1",
		"name2",
		"name3",
		"name4",
		"name5",
		"name6",
		"name7",
		"name8",
		"name9",
		]