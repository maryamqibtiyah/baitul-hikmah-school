from .models import SchoolLevel, News

def school_info(request):
    """Context processor to make school info available to all templates"""
    return {
        'school_name': 'Baitul-Hikmah Int\'l Academy',
        'school_address': '5, Road 4, Idafa Okusiye, Maya, Ikorodu, Lagos State',
        'school_phone': '07086761149',
        'school_email': 'baitulhikmah@gmail.com',
        'all_school_levels': SchoolLevel.objects.all().order_by('order'),
        'recent_news': News.objects.all()[:3],
    }