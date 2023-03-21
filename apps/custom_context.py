from .models import News ,Category

def latest_news(requests):
    latest_news = News.published.all().order_by("-publish")
    category_list = Category.objects.all()
    context = {
        "latest_news":latest_news ,
        "category_list": category_list,
    }

    return context
