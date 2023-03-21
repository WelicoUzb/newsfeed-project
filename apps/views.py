from django.shortcuts import render
from .models import News , Category
from django.views.generic import TemplateView ,ListView
from .forms import MessageForm
from django.http import HttpResponse

# def Home(requests):
#     news = News.published.all().order_by("-publish")
#     category = Category.objects.all()
#
#     economy_ctg = Category.objects.get(direction='iqtisodiyot')
#     economy = News.published.filter(category=economy_ctg).order_by('-pk')
#
#     country_ctg = Category.objects.get(direction='uzbekiston')
#     country = News.published.filter(category=country_ctg).order_by('-pk')
#
#     technology_ctg = Category.objects.get(direction='texnologiya')
#     technology = News.published.filter(category=technology_ctg).order_by('-pk')
#
#     sport_ctg = Category.objects.get(direction='sport')
#     sport = News.published.filter(category=sport_ctg).order_by('-pk')
#
#     world_ctg = Category.objects.get(direction='jahon')
#     world = News.published.filter(category=world_ctg).order_by('-pk')
#
#     context = {
#         "news":news ,
#         "category":category,
#         'economy':economy,
#         'country':country ,
#         'technology':technology,
#         'sport':sport ,
#         'world':world ,
#     }
#     return render(requests , 'index.html' , context)





class Home(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['category']= Category.objects.all()
        context['economy']= News.published.filter(category__direction='economy').order_by('-pk')
        context['country']= News.published.filter(category__direction='uzbekistan').order_by('-pk')
        context['technology']= News.published.filter(category__direction='technology').order_by('-pk')
        context['sport']= News.published.filter(category__direction='sport').order_by('-pk')
        context['world']= News.published.filter(category__direction= 'world').order_by('-pk')

        return context

def View(requests,pk):
    news = News.published.all().order_by("-publish")
    view =News.objects.get(pk=pk)
    context = {
        'view':view,
        "news": news,
    }
    return render(requests ,'single_page.html' , context)



class Contact(TemplateView):
    model = MessageForm
    template_name = 'contact.html'

    def get(self ,requests , *args , **kvargs):
        news = News.published.all().order_by("-publish")
        form = MessageForm()
        context = {
            "form":form ,
            "news": news,
        }
        return render(requests , 'contact.html' , context)

    def post(self, requests, *args, **kvargs):
        form = MessageForm(requests.POST)
        if requests.method == "POST" and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaningiz uchun tashakkur ! </h2>")
        context = {
            "form": form,
        }
        return render(requests, 'contact.html', context)

def Error(requests):
    news = News.published.all().order_by("-publish")
    context = {
        "news": news,
    }
    return render(requests , '404.html' , context)

class Uzbekistan(ListView):
    model = News
    template_name = 'ctg_page/uzbekistan.html'
    context_object_name = 'uzbekistan_news'

    def get_queryset(self):
        context  = News.published.all().filter(category__direction='uzbekistan').order_by('-pk')

        return context

class World(ListView):
    model = News
    template_name = 'ctg_page/world.html'
    context_object_name = 'world_news'

    def get_queryset(self):
        context  = News.published.all().filter(category__direction='world').order_by('-pk')

        return context

class Economy(ListView):
    model = News
    template_name = 'ctg_page/economy.html'
    context_object_name = 'economy_news'

    def get_queryset(self):
        context  = News.published.all().filter(category__direction='economy').order_by('-pk')

        return context

class Technology(ListView):
    model = News
    template_name = 'ctg_page/technology.html'
    context_object_name = 'technology_news'

    def get_queryset(self):
        context  = News.published.all().filter(category__direction='technology').order_by('-pk')

        return context

class Sport(ListView):
    model = News
    template_name = 'ctg_page/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        context  = News.published.all().filter(category__direction='sport').order_by('-pk')

        return context


