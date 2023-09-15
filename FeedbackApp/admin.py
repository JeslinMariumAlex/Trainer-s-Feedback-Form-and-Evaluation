from django.contrib import admin
from .models import Feedback,Batch,Course

# Register your models here.
class adminfeedback(admin.ModelAdmin):
    list_display=['student_name','trainer_name','batch_name','course_name','rating','suggestion']
    # list_display='__all__'

admin.site.register(Feedback,adminfeedback,)
admin.site.register(Batch)
admin.site.register(Course)