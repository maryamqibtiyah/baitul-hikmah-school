from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admission/', views.admission, name='admission'),
    path('admission/success/<str:app_number>/', views.admission_success, name='admission_success'),
    path('events/', views.events_list, name='events'),
    path('events/<slug:slug>/', views.event_detail, name='event_detail'),
    path('gallery/', views.gallery_list, name='gallery_list'),  # ← ADD THIS
    path('gallery/<slug:slug>/', views.gallery_detail, name='gallery_detail'),  # ← ADD THIS
    path('faq/', views.faq, name='faq'),
    path('schools/<slug:slug>/', views.school_level_detail, name='school_level'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('staff/', views.staff_directory, name='staff'),
]