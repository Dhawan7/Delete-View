from django.contrib import admin
from cbvapp.models import Collage,student

class studentAdmin(admin.ModelAdmin):
    list_display = ['id','name','collage','email','contact','age']
admin.site.register(Collage)
admin.site.register(student,studentAdmin)
