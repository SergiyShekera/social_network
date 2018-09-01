from django.contrib import admin
from .models import User_Acc


class User_Acc_Admin(admin.ModelAdmin):

    list_display = ['user','first_name', 'last_name']



admin.site.register(User_Acc, User_Acc_Admin)
