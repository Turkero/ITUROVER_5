from django.contrib import admin

# Register your models here.
from .models import Member

class MemberAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	class Meta:
		model = Member

admin.site.register(Member, MemberAdmin)