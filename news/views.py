from django.shortcuts import render,redirect,get_object_or_404
from .models import reviews,articles,video,Entertainment_news,news_category,movies_category,subscription_alert
from django.http import HttpResponse
from django.urls import reverse
from .forms import subscription_forms
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your views here.

n_category={category.id:category.category for category in news_category.objects.all()}
m_category=list(category.Category for category in movies_category.objects.all())

def home_view(request):
    article=articles.objects.all()
    news=Entertainment_news.objects.all()
    review=reviews.objects.all()
    videos=video.objects.all()
    if request.method=='POST':
        form=subscription_forms(request.POST)
        if form.is_valid():
            email=request.POST.get('Email')
            if subscription_alert.objects.filter(Email=email).exists():
                messages.error(request, 'Email already exists. Please login.')
            else:
                form_copy=form.save()
                subject='Thank you for subscribing Zoomaax'
                message=f'Dear {form_copy.First_name} {form_copy.Last_name},\n content\n\n\n\\n Regards,\n Zoomaax News.'
                send_mail(subject,message,settings.DEFAULT_FROM_EMAIL,[email])
                
    form=subscription_forms()
    context={
            'article':article,
            'news':news,
            'review':review,
            'videos':videos,
            'form':form,
        }
    return render(request,'home.html',context)

def News_view(request):
    news=Entertainment_news.objects.all()
    
    return render(request,'news.html',{'news':news})

def article_view(request):
    category=[]
    articles_all=articles.objects.all()
    for id,categories in n_category.items():
        category=articles.objects.filter(id=id)
    return render(request,'article.html',{'article':articles_all,'category':category,'category_id':n_category,'category_':category})

def review_view(request):
    review_all=reviews.objects.all()
    return render(request,'review.html',{'review':review_all})
    pass
def video_view(request):
    video_all=video.objects.all()
    return render(request,'video.html',{'videos':video_all})

def route_news(request,pk):
    item = get_object_or_404(Entertainment_news, id=pk)
    return render(request, 'route_article.html', {'item': item,'table':'Entertainment News'})
def route_article(request,pk):
    item = get_object_or_404(articles, id=pk)
    print()
    return render(request, 'route_article.html', {'item': item,'table':'Article'})
def route_review(request,pk):
    item = get_object_or_404(reviews, id=pk)
    return render(request, 'route_article.html', {'item': item,'table':'Movie Reviews'})
def route_video(request,pk):
    item = get_object_or_404(video, id=pk)
    return render(request, 'route_article.html', {'item': item,'table':'Video'})

@receiver(post_save,sender=Entertainment_news)
@receiver(post_save,sender=reviews)
@receiver(post_save,sender=articles)
@receiver(post_save,sender=video)
def alert_mails(sender,instance,created,**kwargs):
    if created:
        subscribers=subscription_alert.objects.filter(is_active=True).values_list('Email',flat=True)
        subject=f"Update in {sender.__name__}"
        message=f"Dear subscriber, \nInformation is been added : {instance}"
        send_mail(subject,message,settings.DEFAULT_FROM_EMAIL,subscribers)