from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER=(
        ("1",'HOD'),
        ("2",'Staff'),
        ("3",'student')
    )
    user_type = models.CharField(choices=USER,max_length=50,default=1)
    profilepic = models.ImageField(upload_to='media/img')

class Course(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class session(models.Model):
    session_start = models.CharField(max_length=50)
    session_end = models.CharField(max_length=50)
    
    def __str__(self):
        return self.session_start

class Student(models.Model):
    name = models.CharField(max_length=50,default = "sample")
    email = models.CharField(max_length=50,default= "sample@gmail.com")
    Branch = models.CharField(max_length=50,default="CSE")
    year = models.CharField(max_length=50,default="2021")
    student_id = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now_add=True)
    mobile_number = models.CharField(max_length=50)
    section = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    father_number = models.CharField(max_length=50)
    father_occupation = models.CharField(max_length=50)
    
    def __str__(self):
        return self.student_id
    
    
class staff(models.Model):
    staff_name = models.CharField(max_length=50)
    staff_id = models.CharField(max_length=50)
    staff_email = models.CharField(max_length=50)
    staff_mobile = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)
    date_of_birth =models.DateField(auto_now_add=True)
    experience = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    image =models.ImageField(upload_to='media/img')
    
    def __str__(self):
        return self.staff_name
    


class subject(models.Model):
    name =models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class staff_notification(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    staff_id = models.ForeignKey(staff,on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.staff_id.staff_name
    

class staff_leave(models.Model):
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE)
    leave_date = models.DateField(auto_now_add=True)
    message = models.TextField()
    status = models.BooleanField(default = False)
    disapprove = models.BooleanField(default = False)
    def __str__(self):
        return self.staff_id.staff_name + "("  +  str(self.leave_date) + ")"

class staff_feedback(models.Model):
    staff_id = models.ForeignKey(staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(default = '')
    status = models.BooleanField(default = False)
    
    def __str__(self):
        return self.staff_id.staff_name


class student_feedback(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField(default = '')
    status = models.BooleanField(default = False)
    
    def __str__(self):
        return self.student_id.name


class student_leave(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    leave_date = models.DateField(auto_now_add=True)
    message = models.TextField()
    status = models.BooleanField(default = False)
    disapprove = models.BooleanField(default = False)
    
    def __str__(self):
        return self.student_id.name +  "(" + str(self.leave_date) +  ")"


class Attendance(models.Model):
    subject_id = models.ForeignKey(subject, on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    session_year_id = models.ForeignKey(session, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject_id.name  + "(" + str(self.attendance_date) +  ")"



class Attendance_report(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance_id = models.ForeignKey(Attendance,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField( auto_now_add=True)
    
    def __str__(self):
        return self.student_id.name + "(" + str(self.attendance_id.subject_id.name) + "/" +  str(self.attendance_id.attendance_date) +   ")"


class Result(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id =models.ForeignKey(subject, on_delete=models.CASCADE)
    internal_marks = models.IntegerField()
    external_marks = models.IntegerField()
    total_marks = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.student_id.name + "(" + self.subject_id.name + ")"
    

class TimeTable(models.Model):
    year = models.ForeignKey(session, on_delete=models.CASCADE)
    branch = models.ForeignKey(Course, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='media/img')
    
    def __str__(self):
        return self.branch.name + "(" + self.year.session_start + ")"
    
    
class StudentActivity(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    activity_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    
    def __str__(self):
        return self.student_id.name + "("   + str(self.activity_date) + ")"
    

class Library(models.Model):
    book_id = models.CharField(max_length=10)
    book_name = models.CharField(max_length=50)
    language = models.CharField(max_length=10)
    department = models.ForeignKey( Course, on_delete=models.CASCADE)
    status = models.BooleanField(default = True)
    
    class Meta:
        verbose_name_plural = "Library"
        
    def __str__(self):
        return self.book_name
    


