from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import SchoolLevel, Staff, News, SchoolInfo
from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    featured_news = News.objects.filter(is_featured=True)[:3]
    school_levels = SchoolLevel.objects.all()
    featured_staff = Staff.objects.filter(is_featured=True)[:4]
    
    context = {
        'featured_news': featured_news,
        'school_levels': school_levels,
        'featured_staff': featured_staff,
    }
    return render(request, 'core/home.html', context)

def about(request):
    """About page view"""
    proprietress = Staff.objects.filter(staff_type='PROPRIETRESS').first()
    head_teachers = Staff.objects.filter(staff_type='HEAD_TEACHER')
    teachers = Staff.objects.filter(staff_type='TEACHER')[:8]
    
    # Get school info from database or use defaults
    school_info = SchoolInfo.objects.first()
    if not school_info:
        # Create default if doesn't exist
        school_info = SchoolInfo.objects.create(
            years_of_excellence=13,
            total_students=300,
            total_graduates=30
        )
    
    context = {
        'proprietress': proprietress,
        'head_teachers': head_teachers,
        'teachers': teachers,
        'staff_count': Staff.objects.count(),
        'student_count': school_info.total_students,
        'years_count': school_info.years_of_excellence,
        'graduates_count': school_info.total_graduates,
    }
    return render(request, 'core/about.html', context)

def school_level_detail(request, slug):
    level = get_object_or_404(SchoolLevel, slug=slug)
    teachers = Staff.objects.filter(staff_type='TEACHER')[:6]
    
    context = {
        'level': level,
        'teachers': teachers,
    }
    return render(request, 'core/level_detail.html', context)

def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    news.views += 1
    news.save()
    
    related_news = News.objects.exclude(id=news.id)[:3]
    
    context = {
        'news': news,
        'related_news': related_news,
    }
    return render(request, 'core/news_detail.html', context)

def staff_directory(request):
    staff_by_type = {}
    for staff_type, label in Staff.STAFF_TYPES:
        staff_list = Staff.objects.filter(staff_type=staff_type)
        if staff_list.exists():
            staff_by_type[label] = staff_list
    
    context = {
        'staff_by_type': staff_by_type,
    }
    return render(request, 'core/staff.html', context)
from .forms import ContactForm
from django.contrib import messages

# Add this function at the bottom
def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'school_phone': '07086761149',
        'school_alt_phone': '08120469063',
        'school_email': 'baitulhikmah@gmail.com',
        'school_address': '5, Road 4, Idafa Okusiye, Maya, Ikorodu, Lagos State',
        'school_hours': 'Monday - Friday: 8:00 AM - 4:00 PM',
        'school_hours_sat': 'Saturday: 4:00 PM - 6:00 PM',
    }
    return render(request, 'core/contact.html', context)
from .forms import AdmissionForm
from .models import AdmissionApplication

def admission(request):
    """Admissions page with form"""
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            application = form.save()
            messages.success(request, f'Application submitted successfully! Your application number is: {application.application_number}')
            return redirect('core:admission_success', app_number=application.application_number)
    else:
        form = AdmissionForm()
    
    context = {
        'form': form,
        'school_levels': SchoolLevel.objects.all(),
    }
    return render(request, 'core/admission.html', context)

def admission_success(request, app_number):
    """Admission success page"""
    application = get_object_or_404(AdmissionApplication, application_number=app_number)
    return render(request, 'core/admission_success.html', {'application': application})
    python
from .models import Event
from django.utils import timezone

def events_list(request):
    """Events listing page"""
    today = timezone.now()
    
    # Upcoming events (future)
    upcoming_events = Event.objects.filter(
        start_date__gte=today,
        end_date__gte=today
    ).order_by('start_date')
    
    # Past events
    past_events = Event.objects.filter(
        end_date__lt=today
    ).order_by('-start_date')[:6]
    
    # Featured events
    featured_events = Event.objects.filter(
        is_featured=True,
        start_date__gte=today
    )[:3]
    
    # Islamic events
    islamic_events = Event.objects.filter(
        event_type='ISLAMIC',
        start_date__gte=today
    )[:3]
    
    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'featured_events': featured_events,
        'islamic_events': islamic_events,
    }
    return render(request, 'core/events.html', context)

def event_detail(request, slug):
    """Individual event page"""
    event = get_object_or_404(Event, slug=slug)
    
    # Get related events (same type)
    related_events = Event.objects.filter(
        event_type=event.event_type
    ).exclude(id=event.id)[:3]
    
    context = {
        'event': event,
        'related_events': related_events,
    }
    return render(request, 'core/event_detail.html', context)
from .models import Event, Graduand
from django.utils import timezone

def events_list(request):
    """Events listing page"""
    today = timezone.now()
    
    # Upcoming events (future)
    upcoming_events = Event.objects.filter(
        start_date__gte=today,
        end_date__gte=today
    ).order_by('start_date')
    
    # Past events
    past_events = Event.objects.filter(
        end_date__lt=today
    ).order_by('-start_date')[:6]
    
    # Featured events
    featured_events = Event.objects.filter(
        is_featured=True,
        start_date__gte=today
    )[:3]
    
    # Islamic events
    islamic_events = Event.objects.filter(
        event_type='ISLAMIC',
        start_date__gte=today
    )[:3]
    
    # End of Session Party (find or create event)
    end_of_session = Event.objects.filter(
        title__icontains='End of Session',
        start_date__gte=today
    ).first()
    
    # If no End of Session event exists, create a default one
    if not end_of_session:
        # This is just for display - you'll create one in admin
        end_of_session = None
    
    # Get SS3 Graduands
    graduands = Graduand.objects.filter(graduation_year='2025', is_featured=True)[:12]
    
    context = {
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'featured_events': featured_events,
        'islamic_events': islamic_events,
        'end_of_session': end_of_session,
        'graduands': graduands,
    }
    return render(request, 'core/events.html', context)
from .models import Gallery, GalleryImage

def gallery_list(request):
    """Gallery listing page"""
    galleries = Gallery.objects.all().order_by('-created_date')
    featured_galleries = Gallery.objects.filter(is_featured=True)[:3]
    
    context = {
        'galleries': galleries,
        'featured_galleries': featured_galleries,
        'total_galleries': galleries.count(),
        'total_images': GalleryImage.objects.count(),
    }
    return render(request, 'core/gallery_list.html', context)

def gallery_detail(request, slug):
    """Individual gallery detail page"""
    gallery = get_object_or_404(Gallery, slug=slug)
    images = gallery.images.all()
    
    context = {
        'gallery': gallery,
        'images': images,
    }
    return render(request, 'core/gallery_detail.html', context)
def faq(request):
    """FAQ page view"""
    from .models import FAQ
    
    # Group FAQs by category
    faqs_by_category = {}
    
    for category_code, category_name in FAQ.CATEGORY_CHOICES:
        faqs = FAQ.objects.filter(category=category_code, is_active=True).order_by('order')
        if faqs.exists():
            faqs_by_category[category_name] = faqs
    
    context = {
        'faqs_by_category': faqs_by_category,
        'total_faqs': FAQ.objects.filter(is_active=True).count(),
    }
    return render(request, 'core/faq.html', context)