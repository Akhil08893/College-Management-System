from django.shortcuts import render,redirect
from django.contrib import messages
from app.models import *

def home(request):
    return render(request,'student/home.html')


def send_feedback(request):
    student = CustomUser.objects.get(id = request.user.id)
    student = Student.objects.get(email = student.email)
    feedbacks = student_feedback.objects.filter(student_id = student)
    if request.method == "POST":
        feedback = student_feedback(
            feedback = request.POST['feedback'],
            student_id = student
        )
        feedback.save()
        messages.success(request,'Feedback send')
        return redirect('student_feedback')
    return render(request,'student/feedback.html',{'feedbacks':feedbacks})

def apply_leave(request):
    student =CustomUser.objects.get(id = request.user.id)
    student = Student.objects.get(email=student.email)
    leaves = student_leave.objects.filter(student_id = student)
    if request.method == "POST":
        message = request.POST['message']
        date = request.POST['date']
        leave = student_leave(
            message = message,
            leave_date = date,
            student_id = student,
        )
        leave.save()
        messages.success(request,'Leave Applied')
        return redirect('student_leave')
    return render(request,'student/apply_leave.html',{'leaves':leaves})


def view_result(request):
    student =CustomUser.objects.get(id = request.user.id)
    student = Student.objects.get(email=student.email)
    status = True
    try:
        results = Result.objects.filter(student_id = student)

        for result in results:
            total_marks = result.internal_marks + result.external_marks
            if total_marks > 90:
                result.grade = "A+"
                result.status = "PASS"
            elif 80 <= total_marks <= 90:
                result.grade = "A"
                result.status = "PASS"
            elif 70 <= total_marks <= 80:
                result.grade = "B"
                result.status = "PASS"
            elif 60 <= total_marks <= 70:
                result.grade = "C"
                result.status = "PASS"
            else:
                result.grade = "D"  
                result.status = "FAIL"
    except:
        status = False
        
    return render(request,'student/view_result.html',{'student':student,'results':results,'status':status})

def view_faculty(request):
    staffs = staff.objects.all()
    return render(request,'student/view_faculty.html',{'staffs':staffs})


def view_attendance(request):
    student = CustomUser.objects.get(id = request.user.id)
    students = Student.objects.get(email = student.email)
    
    sample = Attendance_report.objects.filter(student_id = students)
    
    
    context = {
                'sample':sample
    }
    return render(request,'student/view_attendance.html',context)


def Timetable(request):
    student = CustomUser.objects.get(id = request.user.id)
    students = Student.objects.get(email = student.email)
    year = session.objects.get(session_start =  students.year)
    Branch = Course.objects.get(name = students.Branch)
    try:
        timetable = TimeTable.objects.get(year = year,branch = Branch)
    except:
        timetable = False
    return render(request,'student/timetable.html',{'timetable':timetable})

def library(request):
    books = Library.objects.all()
    return render(request,'student/library.html',{'books':books})