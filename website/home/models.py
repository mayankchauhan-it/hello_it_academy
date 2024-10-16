from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Custom User Model
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    # Add unique related_name to avoid clashes with the default 'auth.User'
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Change related_name here
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Change related_name here
        blank=True,
    )

    def __str__(self):
        return self.username

# Student Model
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='students/', null=True, blank=True)

    def __str__(self):
        return self.user.username

# Instructor Model
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=255)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='instructors/', null=True, blank=True)

    def __str__(self):
        return self.user.username

# Technology Model
class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

# Course Model
# Existing Course and Project Models
class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    duration_weeks = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_name

class Project(models.Model):
    project_title = models.CharField(max_length=255)
    description = models.TextField()
    duration_days = models.IntegerField()
    difficulty_level = models.CharField(max_length=50)
    technologies = models.ManyToManyField(Technology, related_name='projects')

    def __str__(self):
        return self.project_title

# Updated Enrollment Model to handle both Course and Proje
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.content_object}"

# Assignment Submission Model
class AssignmentSubmission(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Checked', 'Checked'),
        ('Rejected', 'Rejected'),
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    submission_file = models.FileField(upload_to='submissions/')
    submission_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.project.project_title}"
