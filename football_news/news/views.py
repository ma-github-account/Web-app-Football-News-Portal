
from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request, category_slug=None):

    news = News.objects.order_by('-date_created')

    return render(request, 'news_list.html', {'news': news})


def news_detail(request, id):

    news = get_object_or_404(News, id=id)

    return render(request, 'news_detail.html', {'news': news})
