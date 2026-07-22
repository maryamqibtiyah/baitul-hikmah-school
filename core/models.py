from django.db import models
from django.utils.text import slugify

class SchoolLevel(models.Model):
    LEVEL_CHOICES = [
        ('Pre-school', 'Pre-school (2 years-3 years)'),
        ('NURSERY', 'Nursery (3-5 years)'),
        ('PRIMARY', 'Primary (6-11 years)'),
        ('JSS', 'Junior Secondary (12-14 years)'),
        ('SSS', 'Senior Secondary (15-18 years)'),
    ]
    
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, unique=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    age_range = models.CharField(max_length=50)
    description = models.TextField()
    curriculum = models.TextField(help_text="Nigerian curriculum details")
    islamic_studies = models.TextField(help_text="Quran, Arabic, Islamic studies")
    admission_requirements = models.TextField()
    fees_summary = models.TextField(help_text="Brief fee summary")
    image = models.ImageField(upload_to='school_levels/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Staff(models.Model):
    STAFF_TYPES = [
        ('PROPRIETRESS', 'Proprietress'),
        ('PRINCIPAL', 'Principal'),
        ('HEAD_TEACHER', 'Head Teacher'),
        ('TEACHER', 'Teacher'),
        ('QURAN_TEACHER', 'Qur\'an Teacher'),
        ('ADMIN', 'Administrator'),
    ]
    
    name = models.CharField(max_length=200)
    staff_type = models.CharField(max_length=20, choices=STAFF_TYPES)
    position = models.CharField(max_length=200)
    qualifications = models.TextField()
    quran_certification = models.CharField(max_length=200, blank=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to='staff/')
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['staff_type', 'order']
    
    def __str__(self):
        return f"{self.name} - {self.get_staff_type_display()}"

class News(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    summary = models.CharField(max_length=300)
    image = models.ImageField(upload_to='news/')
    published_date = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-published_date']
        verbose_name_plural = 'News'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
class SchoolInfo(models.Model):
    years_of_excellence = models.IntegerField(default=25, help_text="Number of years the school has been operating")
    total_students = models.IntegerField(default=500, help_text="Total number of students enrolled")
    total_graduates = models.IntegerField(default=1000, help_text="Total number of graduates")
    
    def __str__(self):
        return "School Statistics"
    
    class Meta:
        verbose_name_plural = "School Information"
class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
class AdmissionApplication(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Review'),
        ('SHORTLISTED', 'Shortlisted'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
        ('WAITLIST', 'Waitlist'),
    ]
    
    SESSION_CHOICES = [
        ('2025/2026', '2025/2026 Session'),
        ('2026/2027', '2026/2027 Session'),
    ]
    
    # Student Information
    student_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('MALE', 'Male'), ('FEMALE', 'Female')])
    applying_for = models.ForeignKey(SchoolLevel, on_delete=models.CASCADE)
    session = models.CharField(max_length=20, choices=SESSION_CHOICES, default='2025/2026')
    
    # Islamic Information
    quran_memorization = models.CharField(max_length=200, blank=True, help_text="Portion memorized (e.g., 5 Juz, Completed Quran)")
    can_recite_quran = models.BooleanField(default=False, help_text="Can recite Quran with Tajweed?")
    islamic_knowledge = models.TextField(blank=True, help_text="Basic Islamic knowledge summary")
    
    # Previous Education
    previous_school = models.CharField(max_length=200, blank=True)
    previous_class = models.CharField(max_length=100, blank=True)
    
    # Parent Information
    parent_name = models.CharField(max_length=200)
    parent_relationship = models.CharField(max_length=50, choices=[('FATHER', 'Father'), ('MOTHER', 'Mother'), ('GUARDIAN', 'Guardian')])
    parent_phone = models.CharField(max_length=15)
    parent_email = models.EmailField()
    parent_occupation = models.CharField(max_length=100, blank=True)
    
    # Address
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    
    # Application Tracking
    application_number = models.CharField(max_length=20, unique=True, blank=True)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    notes = models.TextField(blank=True, help_text="Admin notes")
    
    class Meta:
        ordering = ['-application_date']
        verbose_name_plural = "Admission Applications"
    
    def save(self, *args, **kwargs):
        if not self.application_number:
            # Generate application number: APP-2025-0001
            year = self.application_date.year if self.application_date else 2025
            last_app = AdmissionApplication.objects.filter(
                application_number__startswith=f'APP-{year}'
            ).order_by('-application_number').first()
            
            if last_app:
                last_num = int(last_app.application_number.split('-')[-1])
                new_num = str(last_num + 1).zfill(4)
            else:
                new_num = '0001'
            
            self.application_number = f'APP-{year}-{new_num}'
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.application_number} - {self.student_name}"
class Event(models.Model):
    EVENT_TYPES = (
        ('ACADEMIC', 'Academic Event'),
        ('ISLAMIC', 'Islamic Event'),
        ('SPORTS', 'Sports Event'),
        ('PARENT', 'Parent Meeting'),
        ('HOLIDAY', 'Holiday'),
        ('OTHER', 'Other'),
    )
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='ACADEMIC')
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['start_date']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
    
        @property
        def is_upcoming(self):
            from django.utils import timezone
            return self.start_date > timezone.now()
    
        @property
        def is_ongoing(self):
            from django.utils import timezone
        return self.start_date <= timezone.now() <= self.end_date
class Graduand(models.Model):
    """SS3 Graduating Students Profile"""
    name = models.CharField(max_length=200)
    nickname = models.CharField(max_length=100, blank=True, help_text="Short name or nickname")
    photo = models.ImageField(upload_to='graduands/')
    aspiration = models.TextField(help_text="Future aspiration or career goal")
    favorite_memory = models.TextField(help_text="Favorite memory from school")
    message = models.TextField(help_text="Message to school or younger students")
    achievements = models.TextField(blank=True, help_text="Notable achievements")
    future_plans = models.CharField(max_length=200, blank=True, help_text="Plans after graduation")
    graduation_year = models.CharField(max_length=10, default='2025')
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Graduands"
    
    def __str__(self):
        return f"{self.name} - Class of {self.graduation_year}"
class Gallery(models.Model):
    """Photo Gallery Album"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='gallery_covers/', blank=True, null=True)
    event_date = models.DateField(blank=True, null=True, help_text="Date of the event")
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_date']
        verbose_name_plural = "Galleries"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    """Individual images in a gallery"""
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.gallery.title} - Image {self.order + 1}"
class FAQ(models.Model):
    CATEGORY_CHOICES = (
        ('ADMISSIONS', 'Admissions'),
        ('ACADEMICS', 'Academics & Curriculum'),
        ('ISLAMIC', 'Islamic Studies'),
        ('FEES', 'Fees & Payments'),
        ('SCHOOL_LIFE', 'School Life'),
        ('GENERAL', 'General'),
    )
    
    question = models.CharField(max_length=300)
    answer = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='GENERAL')
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['category', 'order', 'created_date']
        verbose_name_plural = "FAQs"
    
    def __str__(self):
        return self.question