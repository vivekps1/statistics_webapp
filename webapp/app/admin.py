from django.contrib import admin  
from import_export.admin import ImportExportMixin 
from .models import *  
from import_export import resources
from django.utils.html import format_html 

# Register your models here. 

class StudentRegistrationResource(resources.ModelResource): 
    class Meta: 
        model = Student 
        fields = ('age', 'fullname') 
        import_id_fields = ['Full Name'] 


class StudentAdmin(ImportExportMixin, admin.ModelAdmin): 
    resource_class = StudentRegistrationResource
    list_display = ('fullname', 'age', 'registered_date', 'z_score', 'z_score_badge')
    search_fields = ('fullname')
    list_filter = ('registered_date', 'updated_date')
    list_per_page = 10
    list_max_show_all = 20 

    def z_score(self, obj): 
        return obj.calculate_z_score() 
    
    def z_score_badge(self, obj): 
        z_score = obj.calculate_z_score()
        if -3 > z_score < 3: 
            badge_color = 'red'
        else: 
            badge_color = 'gray'
admin.site.register(Student)