from .models import Category, Tag, About, Ads, OurImage, LastesPost, New

def index_processor(request):
    kategoriyalar=Category.objects.all()
    tags=Tag.objects.all()[:20]
    about=About.objects.first()
    ads_one=Ads.objects.all().filter(position='one', is_active=True).order_by('?')  
    image_our_one=OurImage.objects.all().filter(position='two', is_active=True ).order_by('?')
    laspost=New.objects.all().order_by('-id')[:2]
    most_views=New.objects.all().order_by('-views')[:4]
    random_news=New.objects.all().order_by('-id')[:3]

    context={
        'kategoriyalar': kategoriyalar,
        'tags': tags,
        'about': about,
        'ads_one': ads_one,
        'image_our_one': image_our_one,
        'laspost': laspost,
        'most_views': most_views,
        'random_news': random_news,
    }
    return context