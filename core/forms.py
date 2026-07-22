from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '08012345678'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Message Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your message here...'}),
        }
from .models import AdmissionApplication

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = [
            'student_name', 'date_of_birth', 'gender', 'applying_for', 'session',
            'quran_memorization', 'can_recite_quran', 'islamic_knowledge',
            'previous_school', 'previous_class',
            'parent_name', 'parent_relationship', 'parent_phone', 'parent_email', 'parent_occupation',
            'address', 'city', 'state'
        ]
        widgets = {
            'student_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name of student'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'applying_for': forms.Select(attrs={'class': 'form-select'}),
            'session': forms.Select(attrs={'class': 'form-select'}),
            'quran_memorization': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., 5 Juz, Completed Quran'}),
            'can_recite_quran': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'islamic_knowledge': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brief description of Islamic knowledge'}),
            'previous_school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Previous school name (if any)'}),
            'previous_class': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last class completed'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Parent/Guardian full name'}),
            'parent_relationship': forms.Select(attrs={'class': 'form-select'}),
            'parent_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '08012345678'}),
            'parent_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'parent@email.com'}),
            'parent_occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Occupation'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Home address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
        }