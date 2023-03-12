from django.contrib import admin
from news.models import News


class NewsAdmin(admin.ModelAdmin):
  model = News
  list_display = ('name', 'title', 'description')
  search_fields = ['name']

# Register your models here.
admin.site.register(News, NewsAdmin)