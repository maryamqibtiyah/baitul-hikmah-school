from django.contrib import admin
from .models import SchoolLevel, Staff, News, SchoolInfo, Event

@admin.register(SchoolLevel)
class SchoolLevelAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'age_range', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'staff_type', 'position', 'order', 'is_featured']
    list_filter = ['staff_type', 'is_featured']
    list_editable = ['order', 'is_featured']
    search_fields = ['name', 'position']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date', 'is_featured', 'views']
    list_filter = ['is_featured', 'published_date']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['views']

@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    pass
from .models import SchoolLevel, Staff, News, SchoolInfo, ContactMessage

# Add this at the bottom of the file
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_date', 'is_read']
    list_filter = ['is_read', 'created_date']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'phone', 'subject', 'message', 'created_date']
    actions = ['mark_as_read']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"
from .models import AdmissionApplication

@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ['application_number', 'student_name', 'applying_for', 'session', 'status', 'application_date']
    list_filter = ['status', 'applying_for', 'session', 'gender']
    search_fields = ['application_number', 'student_name', 'parent_name', 'parent_email']
    readonly_fields = ['application_number', 'application_date']
    list_editable = ['status']
    
    fieldsets = (
        ('Application Info', {
            'fields': ('application_number', 'application_date', 'status', 'session')
        }),
        ('Student Information', {
            'fields': ('student_name', 'date_of_birth', 'gender', 'applying_for')
        }),
        ('Islamic Information', {
            'fields': ('quran_memorization', 'can_recite_quran', 'islamic_knowledge')
        }),
        ('Previous Education', {
            'fields': ('previous_school', 'previous_class')
        }),
        ('Parent Information', {
            'fields': ('parent_name', 'parent_relationship', 'parent_phone', 'parent_email', 'parent_occupation')
        }),
        ('Address', {
            'fields': ('address', 'city', 'state')
        }),
        ('Admin Notes', {
            'fields': ('notes',)
        }),
    )
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'start_date', 'end_date', 'location', 'is_featured']
    list_filter = ['event_type', 'is_featured', 'start_date']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'start_date'
    fieldsets = (
        ('Event Information', {
            'fields': ('title', 'slug', 'event_type', 'description', 'location')
        }),
        ('Date and Time', {
            'fields': ('start_date', 'end_date')
        }),
        ('Media', {
            'fields': ('image', 'is_featured')
        }),
    )
from .models import Graduand

@admin.register(Graduand)
class GraduandAdmin(admin.ModelAdmin):
    list_display = ['name', 'graduation_year', 'is_featured', 'order']
    list_editable = ['order', 'is_featured']
    search_fields = ['name', 'nickname']
    list_filter = ['graduation_year', 'is_featured']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'nickname', 'photo', 'graduation_year', 'order', 'is_featured')
        }),
        ('Student Story', {
            'fields': ('aspiration', 'favorite_memory', 'message', 'achievements', 'future_plans')
        }),
    )
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['question', 'answer']
    fieldsets = (
        ('FAQ Information', {
            'fields': ('question', 'answer', 'category', 'order', 'is_active')
        }),
    )