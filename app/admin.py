from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

class usermodel(UserAdmin):
    list_display=['username','user_type']

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(session)
admin.site.register(Student)
admin.site.register(staff)
admin.site.register(subject)
admin.site.register(staff_notification)
admin.site.register(staff_leave)
admin.site.register(staff_feedback)
admin.site.register(student_feedback)
admin.site.register(student_leave)
admin.site.register(Attendance)
admin.site.register(Attendance_report)
admin.site.register(Result)
admin.site.register(TimeTable)
admin.site.register(StudentActivity)
admin.site.register(Library)




