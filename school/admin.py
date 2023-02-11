from django.contrib import admin
from .models import Student, Courses, BaseModel, Teacher

admin.site.register(BaseModel)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Courses)