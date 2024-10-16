from django.contrib import admin
from .models import User, Student, Instructor, Technology, Course, Project, Enrollment, AssignmentSubmission

# Custom admin for the Course model
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'instructor', 'price', 'duration_weeks')
    search_fields = ['course_name', 'instructor__user__username']  # Search by course name or instructor's username

# Custom admin for the Instructor model
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user', 'expertise', 'bio')
    search_fields = ['user__username', 'expertise']

# Custom admin for Enrollment model
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'get_enrolled_content', 'enrollment_date')
    search_fields = ['student__user__username', 'content_type__model']  # Search by student username or course/project type
    list_filter = ('content_type',)  # Filter by whether it's a Course or Project enrollment

    def get_enrolled_content(self, obj):
        return str(obj.content_object)  # This will show either the course name or project title
    get_enrolled_content.short_description = 'Enrolled Content'

# Custom admin for Assignment Submission model
class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'project', 'submission_date', 'status')
    search_fields = ['student__user__username', 'project__project_title']
    list_filter = ('status',)

# Register your models here
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Technology)
admin.site.register(Course, CourseAdmin)
admin.site.register(Project)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(AssignmentSubmission, AssignmentSubmissionAdmin)
