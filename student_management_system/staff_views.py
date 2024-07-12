from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import *
from django.db.models import Q

def home(request):
    if request.user.is_authenticated:
        students = Student.objects.all().count()
        staffs = staff.objects.all().count()
        courses = Course.objects.all().count()
        subjects = subject.objects.all().count()
        
        Staff = CustomUser.objects.get(id = request.user.id)
        st = staff.objects.get(staff_email = Staff.email)
        query = Q(staff_id = st) & Q(status = False)
        notifications = staff_notification.objects.filter(query)
        num_notification = notifications.count()
        
        
        context = {'students':students,
                    'staffs':staffs,
                    'courses':courses,
                    'subjects':subjects,
                    'notifications':notifications,
                    'num_notification':num_notification
                }
        
        return render(request,'staff/home.html',context)
    else:
        messages.success(request,'Please Login to continue...')
        return redirect('login')


def apply_leave(request):
    Staff =CustomUser.objects.get(id = request.user.id)
    staffs = staff.objects.get(staff_email=Staff.email)
    leaves = staff_leave.objects.filter(staff_id = staffs)
    if request.method == "POST":
        message = request.POST['message']
        date = request.POST['date']
        leave = staff_leave(
            message = message,
            leave_date = date,
            staff_id = staffs,
        )
        leave.save()
        messages.success(request,'Leave Applied')
        return redirect('apply_leave')
    return render(request,'staff/apply_leave.html',{'leaves':leaves})


def send_feedback(request):
    Staff = CustomUser.objects.get(id = request.user.id)
    staffs = staff.objects.get(staff_email = Staff.email)
    feedbacks = staff_feedback.objects.filter(staff_id = staffs)
    if request.method == "POST":
        feedback = staff_feedback(
            feedback = request.POST['feedback'],
            staff_id = staffs
        )
        feedback.save()
        messages.success(request,'Feedback send')
        return redirect('staff_feedback')
    return render(request,'staff/feedback.html',{'feedbacks':feedbacks})


def Take_attendance(request):
    Staff = CustomUser.objects.get(id = request.user.id)
    staffs = staff.objects.get(staff_email = Staff.email)
    subjects = subject.objects.filter(staff = staffs)
    Branches = Course.objects.all()
    sessions = session.objects.all()
    action = request.GET.get('action')
    
    students = None
    get_subject = None
    get_year = None
    if action is not None:
        if request.method == "POST":
            year = request.POST.get('year')
            branch =request.POST.get('branch')
            query = Q(Branch=branch) & Q(year=year)
            
            students = Student.objects.filter(query)
            get_year = year
            get_subject = request.POST.get('subject')
    context = {'subjects':subjects,
                'Branches':Branches,
                'sessions':sessions,
                'students':students,
                'action':action,
                'get_subject':get_subject,
                'get_year':get_year
                }
    return render(request,'staff/take_attendance.html',context)


def save_attendance(request):
    if request.method =="POST":
        get_subject = subject.objects.get(name=request.POST['subject_name'])
        get_year = session.objects.get(session_start=request.POST['year'])
        
        attendance = Attendance(
            subject_id = get_subject,
            attendance_date = request.POST['date'],
            session_year_id = get_year,
        )
        attendance.save()
        
        student =  request.POST.getlist('student_id')
        
        for i in student:
            stu_id = i
            int_stu = int(stu_id)
            
            present_student = Student.objects.get(id = int_stu)
            attendance_report = Attendance_report(
                student_id = present_student,
                attendance_id = attendance
            )
            attendance_report.save()
        
        messages.success(request,'Attendance Send')
        return redirect('Take_attendance')


def view_attendance(request):
    Staff = CustomUser.objects.get(id = request.user.id)
    staffs = staff.objects.get(staff_email = Staff.email)
    subjects = subject.objects.filter(staff = staffs)
    sessions = session.objects.all()
    action = request.GET.get('action')
    attendance_report= None
    if action is not None:
        if request.method == "POST":
            get_subject = subject.objects.get(name=request.POST.get('subject'))
            get_year = session.objects.get(session_start=request.POST['year'])
            attendances = Attendance.objects.filter(subject_id=get_subject,attendance_date=request.POST.get('date'),session_year_id=get_year)
            
            for i in attendances:
                attendance_iid = i.id
                attendance_report = Attendance_report.objects.filter(attendance_id=attendance_iid)
    context = {
                'subjects':subjects,
                'sessions':sessions,
                'action':action,
                'attendance_report':attendance_report
    }
    return render(request,'staff/view_attendance.html',context)

def update_attendance(request,id):
    attendance = Attendance_report.objects.get(id = id)
    attendance.delete()
    messages.success(request,'Attendance Updated')
    return redirect('view_attendance')

def Add_result(request):
    Staff = CustomUser.objects.get(id = request.user.id)
    staffs = staff.objects.get(staff_email = Staff.email)
    subjects = subject.objects.filter(staff = staffs)
    sessions = session.objects.all()
    action = request.GET.get('action')
    
    students = None
    get_subject = None
    get_year = None
    if action is not None:
        if request.method == "POST":
            year = request.POST.get('year')
            students = Student.objects.filter(year = year)
            get_year = year
            get_subject = request.POST.get('subject')
            
    context = {
                'subjects':subjects,
                
                'sessions':sessions,
                'students':students,
                'action':action,
                'get_subject':get_subject,
                
                }
    return render(request,'staff/Add_result.html',context)


def save_result(request):
    if request.method == "POST":
        student =  request.POST.get('student')
        student_id = Student.objects.get(student_id = student)
        subject_id = subject.objects.get(name = request.POST.get('subject'))
        result = Result(
            subject_id =  subject_id,
            student_id =student_id,
            internal_marks = request.POST.get('assignment_marks'),
            external_marks = request.POST.get('exam_marks'),
            total_marks = request.POST.get('total_marks'),
        )
        result.save()
        messages.success(request,'Results Added')
        return redirect('Add_result')
    
    
def view_faculty(request):
    staffs = staff.objects.exclude(id=request.user.id)
    
    return render(request,'staff/view_faculty.html',{'staffs':staffs})


def view_student(request):
    students = Student.objects.all()
    
    return render(request,'staff/view_student.html',{'students':students})

def view_notifications(request):
    Staff = CustomUser.objects.get(id = request.user.id)
    staffs = staff.objects.get(staff_email = Staff.email)
    notifications = staff_notification.objects.filter(staff_id = staffs)
    return render(request,'staff/notification.html',{'notifications':notifications})

def read_notifications(request,id):
    notification = staff_notification.objects.get(id = id)
    notification.status = True
    notification.save()
    return redirect('view_notifications')

def student_activities(request):
    students = Student.objects.all()
    activities = StudentActivity.objects.all()
    if request.method == "POST":
        student = Student.objects.get(student_id = request.POST['student'])
        activity = StudentActivity(
            student_id = student,
            description = request.POST['description']
        )
        activity.save()
        messages.success(request,'Activity saved successful..')
        return redirect('student_activity')
    return render(request,'staff/student_activity.html',{'students':students,'activities':activities})