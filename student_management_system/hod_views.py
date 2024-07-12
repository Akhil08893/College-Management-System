from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from app.models import *
from django.db.models import Q,Sum,F
from django.http import HttpResponse
from django.http import HttpResponseNotFound



def home(request):
    if request.user.is_authenticated:
        students = Student.objects.all().count()
        staffs = staff.objects.all().count()
        courses = Course.objects.all().count()
        subjects = subject.objects.all().count()
        
        activities = StudentActivity.objects.all()
        
        student_male = Student.objects.filter(gender='Male').count()
        student_female = Student.objects.filter(gender='Female').count()
        
        student_totals = (Result.objects
                        .values('student_id')
                        .annotate(total_marks=Sum('total_marks'))
                        .order_by('-total_marks')[:3])
        
        top_students = []
        for student_total in student_totals:
            student = Student.objects.get(pk=student_total['student_id'])
            top_students.append({
                'student': student,
                'total_marks': student_total['total_marks']
                })
        
        context = {
                    'students':students,
                    'staffs':staffs,
                    'courses':courses,
                    'subjects':subjects,
                    'student_female':student_female,
                    'student_male':student_male,
                    'top_students':top_students,
                    'activities':activities
                }
        
        
        return render(request,'Hod/home.html',context)
    else:
        messages.success(request,'Login To continue')
        return redirect('login')


def add_student(request):
    if request.user.is_authenticated:
        courses = Course.objects.all()
        Batches = session.objects.all()
        if request.method == "POST":
            student_id = request.POST['student_id']
            if  CustomUser.objects.filter(email=request.POST['student_email']).exists():
                messages.success(request,"email already taken..")
                return redirect('add_student')
            
            user = CustomUser(
                first_name=request.POST['first_name'],
                email=request.POST['student_email'],
                username = request.POST['first_name'],
                user_type = 3,
                profilepic = request.FILES.get('profile_pic')
                )
            user.set_password(student_id)
            user.save()
            student = Student(
                name = request.POST['first_name'],
                email = request.POST['student_email'],
                Branch = request.POST['course'],
                year = request.POST['session_year'],
                student_id = student_id,
                gender = request.POST['gender'],
                date_of_birth = request.POST['dob'],
                mobile_number =  request.POST['mobile_number'],
                section = request.POST['section'],
                address = request.POST['address'],
                father_name = request.POST['father_name'],
                mother_name = request.POST['mother_name'],
                father_number = request.POST['father_number'],
                father_occupation=request.POST['father_occupation']
            )
            
            student.save()
            
            messages.success(request,'student information Added Successful..')
            return redirect('add_student')
        return render(request,'Hod/add_student.html',{'courses':courses,'Batches':Batches})
    else:
        messages.success(request,'Login To continue')
        return redirect('login')
    
#students
def view_student(request):
    students = Student.objects.all().order_by("student_id")
    return render(request,'Hod/view_student.html',{'students':students})

def edit_student(request,id):
    student = Student.objects.get(id = id)
    courses =Course.objects.all()
    Batches = session.objects.all()
    if request.method == "POST":
        
        student.name = request.POST['first_name']
        student.email = request.POST['student_email']
        student.Branch = request.POST['course']
        student.year = request.POST['session_year']
        student.student_id = request.POST['student_id']
        student.gender = request.POST['gender']
        student.date_of_birth = request.POST['dob']
        student.mobile_number = request.POST['mobile_number']
        student.section = request.POST['section']
        student.address = request.POST['address']
        
        student.save()
        messages.success(request,'student information Updated Successful..')
        return redirect('view_student')
    
    return render(request,'Hod/edit_student.html',{'student':student,'Batches':Batches,'courses':courses})

def delete_student(request,id):
    student = Student.objects.get(id=id)
    user = CustomUser.objects.get(email=student.email)
    student.delete()
    user.delete()
    messages.success(request,'Student record deleted successful...')
    return redirect('view_student')

#courses
def add_course(request):
    if request.method == "POST":
        course_name = request.POST['course_name']
        course = Course(
            name = course_name
        )
        course.save()
        messages.success(request,'Course Added successful..')
        return redirect('add_course')
    return render(request,'Hod/add_course.html')

def add_subject(request):
    if request.user.is_authenticated:
        courses = Course.objects.all()
        staffs = staff.objects.all()
        if request.method == "POST":
            course = Course.objects.get(name = request.POST['course'])
            teacher = staff.objects.get(staff_name = request.POST['staff'])
            subject1 = subject(
                staff = teacher,
                name = request.POST['subject_name'],
                course = course,
            )
            subject1.save()
            messages.success(request,"Subject Added Successful..")
            return redirect('add_subject')
        else:
            return render(request,'Hod/add_subject.html',{'courses':courses,'staff':staffs})


def view_course(request):
    courses = Course.objects.all()
    return render(request,'Hod/view_course.html',{'courses':courses})

def view_subject(request):
    subjects = subject.objects.all()
    return render(request,'Hod/view_subject.html',{'subjects':subjects})

def delete_course(request,id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request,'course deleted Successful..')
    return redirect('view_course')

def delete_subject(request,id):
    subjects = subject.objects.get(id=id)
    subjects.delete()
    messages.success(request,'subject deleted Successful..')
    return redirect('view_subject')


#staff
def add_staff(request):
    if request.method == "POST":
        if  CustomUser.objects.filter(email=request.POST['staff_email']).exists():
            messages.success(request,'Email already taken...')
            return redirect('add_staff')
        user = CustomUser(
            first_name = request.POST['staff_name'],
            username = request.POST['staff_name'],
            user_type = 2,
            profilepic = request.FILES.get("profile_pic"),
            email = request.POST["staff_email"]            
        )
        
        user.set_password(request.POST["staff_id"])
        user.save()
        teacher = staff(
            staff_name = request.POST['staff_name'],
            staff_id = request.POST['staff_id'],
            staff_mobile = request.POST['staff_mobile'],
            staff_email = request.POST['staff_email'],
            date_of_birth = request.POST['dob'],
            gender = request.POST['gender'],
            qualification = request.POST['qualification'],
            experience = request.POST['experience'],
            address = request.POST['address'],
            city = request.POST['city'],
            state = request.POST['state'],
            zipcode = request.POST['zipcode'],
            image = request.FILES.get("profile_pic"),
        )
        teacher.save()
        messages.success(request,'Staff details Added...')
        return redirect('add_staff')
    return render(request,'Hod/add_staff.html')

def view_staff(request):
    staffs = staff.objects.all()
    return render(request,'Hod/view_staff.html',{'staffs':staffs})

def delete_staff(request,id):
    Staff =staff.objects.get(id=id)
    user = CustomUser.objects.get(email=Staff.staff_email)
    Staff.delete()
    user.delete()
    messages.success(request,"Staff deleted successful...")
    return redirect('view_staff')

def view_notification(request):
    staffs = staff.objects.all()
    notifications  = staff_notification.objects.all()
    if request.method == "POST":
        st = staff.objects.get(id = request.POST["staff_Id"])
        notification = staff_notification(
            message = request.POST["notification_message"],
            staff_id = st
        )
        notification.save()
        messages.success(request,'notification send successful..')
        return redirect('notifications')
    return render(request,'hod/send_notification.html',{'staffs':staffs,'notifications':notifications})

def send_notifications(request):
    if request.method == "POST":
        staffs = staff.objects.all()
        for i in staffs:
            notification = staff_notification(
                message = request.POST['message1'],
                staff_id = i
            )
            notification.save()
        return redirect('notifications')

def leaves(request):
    Leaves = staff_leave.objects.all()
    return render(request,'Hod/leaves.html',{'leaves':Leaves})

def student_leaves(request):
    Leaves = student_leave.objects.all()
    return render(request,'Hod/student_leaves.html',{'leaves':Leaves})


#staff_leave
def approve_leave(request,id):
    leave = staff_leave.objects.get(id = id)
    leave.status = True
    leave.save()
    messages.success(request,'Leave approved')
    return redirect('leaves')

def student_approve_leave(request,id):
    leave = student_leave.objects.get(id = id)
    leave.status = True
    leave.save()
    messages.success(request,'Leave approved')
    return redirect('student_leaves')

def disapprove_leave(request,id):
    leave = staff_leave.objects.get(id = id)
    leave.disapprove = True
    leave.save()
    messages.success(request,'Leave disapproved')
    return redirect('leaves')

def student_disapprove_leave(request,id):
    leave = student_leave.objects.get(id = id)
    leave.disapprove = True
    leave.save()
    messages.success(request,'Leave disapproved')
    return redirect('student_leaves')


def feedback(request):
    feedbacks = staff_feedback.objects.all()
    if request.method == "POST":
        feed = staff_feedback.objects.get(id = request.POST['feedback_Id'])
        feed.feedback_reply = request.POST['feedback']
        feed.status = True
        feed.save()
        messages.success(request,'Feedback reply send successful')
        return redirect('feedback')
    return render(request,'Hod/feedback.html',{'feedbacks':feedbacks})


def Timetable(request):
    years = session.objects.all()
    branches = Course.objects.all()
    action = request.GET.get('action')
    timetable = None
    if action is not None:
        if request.method == "POST":
            year = session.objects.get(session_start = request.POST.get('year'))
            course = Course.objects.get(name =request.POST.get('branch'))
            try:
                timetable =  TimeTable.objects.get(year=year,branch=course)
            except :
                messages.success(request,'TimeTable not found')
                return redirect('Timetable')
            
    print(timetable)
    context = {
        'action':action,
        'years':years,
        'branches':branches,
        'timetable':timetable
    }
    return render(request,'Hod/Timetable.html',context)

def download_image(request,image_id):
    image =  TimeTable.objects.get(id=image_id)
    response = HttpResponse(image.photo, content_type='image/jpeg')
    response['Content-Disposition'] = f'attachment; filename="{image.branch}_timetable.jpg"'
    return response

def holiday_list(request):
    return render(request,'Hod/holidaylist.html')

def eventsList(request):
    return render(request,'Hod/events.html')