from django.contrib import admin
from .models import Entertainment_news,reviews,articles,video,news_category,movies_category

admin.site.register(news_category)
admin.site.register(movies_category)
admin.site.register(Entertainment_news)
admin.site.register(reviews)
admin.site.register(articles)
admin.site.register(video)
# Register your models here.
