from django.urls import path
from .views import IndexView, Category_list, DetailView, Lastest_news, ContactView, SearchView

app_name='home'
urlpatterns=[
    path('', IndexView.as_view(), name='home'),
    path('category/<str:slug>/', Category_list.as_view(), name="category" ),
    path('news/<str:slug>/', DetailView.as_view(), name="detail"),
    path('las_news/<str:slug>/', Lastest_news.as_view(), name="lastest"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('search/', SearchView.as_view(), name='search')
]