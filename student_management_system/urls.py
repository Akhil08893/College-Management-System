from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import settings
from . import views,hod_views,staff_views,student_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.home,name='home'),
    path('login/',views.Login,name='login'),
    path('logout/',views.Logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/update',views.profile_update,name='profile_update'),
    
    #HOD
    path('hod/home',hod_views.home,name='hod_home'),
    path('hod/add_student',hod_views.add_student,name='add_student'),
    path('hod/view_student',hod_views.view_student,name='view_student'),
    path('hod/edit_student/<int:id>',hod_views.edit_student,name='edit_student'),
    path('hod/delete_student/<int:id>',hod_views.delete_student,name='delete_student'),
    path('hod/add_course',hod_views.add_course,name='add_course'),
    path('hod/view_course',hod_views.view_course,name='view_course'),
    path('hod/delete_course/<int:id>',hod_views.delete_course,name='delete_course'),
    path('hod/add_staff',hod_views.add_staff,name='add_staff'),
    path('hod/view_staff',hod_views.view_staff,name='view_staff'),
    path('hod/delete_staff/<int:id>',hod_views.delete_staff,name='delete_staff'),
    path('hod/delete_subject/<int:id>',hod_views.delete_subject,name='delete_subject'),
    path('hod/add_subject',hod_views.add_subject,name='add_subject'),
    path('hod/view_subject',hod_views.view_subject,name='view_subject'),
    path('hod/notifications',hod_views.view_notification,name='notifications'),
    path('hod/send_notifications',hod_views.send_notifications,name='send_notifications'),
    path('hod/leaves',hod_views.leaves,name='leaves'),
    path('hod/student_leaves',hod_views.student_leaves,name='student_leaves'),
    path('hod/approve_leave/<int:id>',hod_views.approve_leave,name='approve_leave'),
    path('hod/student_approve_leave/<int:id>',hod_views.student_approve_leave,name='student_approve_leave'),
    path('hod/disapprove_leave/<int:id>',hod_views.disapprove_leave,name='disapprove_leave'),
    path('hod/student_disapprove_leave/<int:id>',hod_views.student_disapprove_leave,name='student_disapprove_leave'),
    path('hod/feedback/',hod_views.feedback,name='feedback'),
    path('Timetable/',hod_views.Timetable,name='Timetable'),
    path('download_img/<int:image_id>',hod_views.download_image,name='download_image'),
    path('hod/holiday_list',hod_views.holiday_list,name='holiday_list'),
    path('hod/eventsList',hod_views.eventsList,name='events_list'),
    
    
    
    #staff
    path('staff/home',staff_views.home,name='staff_home'),
    path('staff/apply_leave',staff_views.apply_leave,name='apply_leave'),
    path('staff/feedback',staff_views.send_feedback,name='staff_feedback'),
    path('staff/Take_attendance',staff_views.Take_attendance,name='Take_attendance'),
    path('staff/save_attendance',staff_views.save_attendance,name='save_attendance'),
    path('staff/view_attendance',staff_views.view_attendance,name='view_attendance'),
    path('staff/Add_result',staff_views.Add_result,name='Add_result'),
    path('staff/save_result',staff_views.save_result,name='save_result'),
    path('staff/view_faculty',staff_views.view_faculty,name='view_faculties'),
    path('staff/view_students',staff_views.view_student,name='view_students'),
    path('staff/view_notifications',staff_views.view_notifications,name='view_notifications'),
    path('staff/read_notifications/<int:id>',staff_views.read_notifications,name='read_notifications'),
    path('staff/student_activities',staff_views.student_activities,name='student_activity'),
    path('staff/update_attendance/<int:id>',staff_views.update_attendance,name='update_attendance'),
    
    
    #student
    path('student/home',student_views.home,name='student_home'),
    path('student/feedback',student_views.send_feedback,name='student_feedback'),
    path('student/apply_leave',student_views.apply_leave,name='student_leave'),
    path('student/view_result',student_views.view_result,name='view_result'),
    path('student/faculty',student_views.view_faculty,name='view_faculty'),
    path('student/view_attendance',student_views.view_attendance,name='student_view_attendance'),
    path('student/view_timetable',student_views.Timetable,name='view_timetable'),
    path('student/library',student_views.library,name='library'),
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
