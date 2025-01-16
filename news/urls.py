from django.urls import path
from .views import News_view,article_view,review_view,video_view,route_news,route_article,route_review,route_video,home_view
urlpatterns = [
    path('',home_view,name='home'),
    path('news/',News_view,name='news'),
    path('article/',article_view,name='article'),
    path('reviews/',review_view,name='reviews'),
    path('video/',video_view,name='video'),
    path('news<int:pk>/',route_news,name='route_news'),
    path('articles/<int:pk>',route_article,name='route_article'),
    path('reviews/<int:pk>',route_review,name='route_reviews'),
    path('video/<int:pk>',route_video,name='route_video'),
]
