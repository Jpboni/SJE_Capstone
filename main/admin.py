from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources



# Register your models here.
from .models import Student, Faculty, Course, Department, Assignment, Announcement

class StudentResource(resources.ModelResource):
    class Meta:
        model = Student
        skip_unchanged = True
        report_skipped = True
        exclude = ('id','photo')
        import_id_fields = ('student_id',)
        fields=('student_id','name','email','password', 'role', 'course','department')

class Studentadmin (ImportExportModelAdmin):
    resource_class = StudentResource

admin.site.register(Student,Studentadmin)

class FacultyResource(resources.ModelResource):
    class Meta:
        model = Faculty
        skip_unchanged = True
        report_skipped = True
        exclude = ('id','photo')
        import_id_fields = ('faculty_id',)
        fields=('faculty_id','name','email','password', 'department','role')

class Facultyadmin (ImportExportModelAdmin):
    resource_class = FacultyResource

admin.site.register(Faculty,Facultyadmin)

class CourseResource(resources.ModelResource):
    class Meta:
        model = Course
        skip_unchanged = True
        report_skipped = True
        exclude = ('id','photo')
        import_id_fields = ('code',)
        fields=('code','name', 'department','FacultyID','studentKey','facultyKey')

class Courseadmin (ImportExportModelAdmin):
    resource_class = CourseResource


admin.site.register(Course,Courseadmin)

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department
        skip_unchanged = True
        report_skipped = True
        exclude = ('id','photo')
        import_id_fields = ('department_id',)
        fields=('department_id','name','description')

class Departmentadmin (ImportExportModelAdmin):
    resource_class = DepartmentResource

admin.site.register(Department,Departmentadmin)


admin.site.register(Assignment)


admin.site.register(Announcement)


