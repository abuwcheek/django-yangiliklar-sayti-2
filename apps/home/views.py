from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages
from .models import Category, Tag, New, Contact, About
from django.db.models import Q



class Lastest_news(View):
    def get(self, request, slug):
        lastest_newsss = New.objects.all().order_by('-id')[:6]
        context={
            'lastest_newsss': lastest_newsss
        }
        return render(request, 'index.html', context)



class IndexView(View):
    def get(self, request):
        news=New.objects.all().order_by('?')[:6]

        sport_news=New.objects.filter(category__name='Sport').order_by('-id')[:6]
        moda_news=New.objects.filter(category__name='Moda').order_by('?')[:6]
        texnologiy_news=New.objects.filter(category__name='Texnologiya').order_by('?')[:6]
        politic_news=New.objects.filter(category__name='Siyosat').order_by('?')[:6]   
        magazine_news=New.objects.filter(category__name='Magazin').order_by('?')[:6]
        private_news=New.objects.filter(category__name='Shaxsiy yangiliklar').order_by('?')[:7]
        

        day_news=New.objects.filter(category__name='Kundalik yangiliklar').order_by('-id')[:2]
        most_news=New.objects.filter(category__name='Mashhur yangiliklar').order_by('-id')[:4]
        lastest_news=New.objects.filter(category__name='Oxirgi yangiliklar').order_by('-id')[:4]

        context={
            'sport_news': sport_news,
            'moda_news': moda_news,
            'texnologiy_news': texnologiy_news,
            'politic_news': politic_news,
            'magazine_news': magazine_news,
            'day_news': day_news,
            'most_news': day_news,
            'lastest_news': lastest_news,
            'private_news': private_news,
        }

        return render(request, 'index.html', context)




class Category_list(View):
    def get(self, request, slug):

        ctg=Category.objects.get(slug=slug)
        news_list=New.objects.filter(category__slug=slug)
        context={
            'ctg':ctg,
            'news_list':news_list
        }
        return render(request, 'category_list.html', context)




class DetailView(View):
    def get(self, request, slug):

        sport_news=New.objects.filter(category__name='Sport').order_by('-id')[:6]
        moda_news=New.objects.filter(category__name='Moda').order_by('?')[:6]
        texnologiy_news=New.objects.filter(category__name='Texnologiya').order_by('?')[:6]
        politic_news=New.objects.filter(category__name='Siyosat').order_by('?')[:6]   
        magazine_news=New.objects.filter(category__name='Magazin').order_by('?')[:6]
        private_news=New.objects.filter(category__name='Shaxsiy yangiliklar').order_by('?')[:7]

        day_news=New.objects.filter(category__name='Kundalik yangiliklar').order_by('-id')[:2]
        most_news=New.objects.filter(category__name='Mashhur yangiliklar').order_by('-id')[:4]
        lastest_news=New.objects.filter(category__name='Oxirgi yangiliklar').order_by('-id')[:4]

        news=get_object_or_404(New, slug=slug)
        news.views+=1
        news.save()

        context={
            'news': news,
            'sport_news': sport_news,
            'moda_news': moda_news,
            'texnologiy_news': texnologiy_news,
            'politic_news': politic_news,
            'magazine_news': magazine_news,
            'day_news': day_news,
            'most_news': day_news,
            'lastest_news': lastest_news,
            'private_news': private_news,
        }
        return render(request, 'detail.html', context)



class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    
    def post(self, request):
        data=request.POST
        contact=Contact()

        contact.name=data.get('name')
        contact.phone=data.get('phone')
        contact.email=data.get('email')
        contact.subject=data.get('subject')
        contact.message=data.get('message')

        contact.save()

        return render(request, 'contact.html')




class AboutView(View):
    def get(self, request):
        data=About.objects.all()
        context={
            'data': data
        }
        return render(request, 'detail.html', context)



from itertools import chain

class SearchView(View):
    def get(self, request):
        query=request.GET.get('query')
        print(query)
        if not query:
            return redirect('home:home')
        
        tag=get_object_or_404(Tag, name=query)
        news = New.objects.all().filter( Q(title__icontains = query) | Q(body__icontains = query))
        tag_news=tag.new_set.all()
        result_list=list(chain(tag_news, new))
        
        context={
            "searchnews":news,
        }
        return render(request, 'search.html', context )