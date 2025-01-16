from django.db import models
from django.utils.timezone import now

class news_category(models.Model):
    category=models.CharField(max_length=25)
    
    class Meta:
        db_table='News Category'
        
    def __str__(self):
        return self.category

class movies_category(models.Model):
    Category=models.CharField(max_length=25)
    
    class Meta:
        db_table='Movies Category'
    
    def __str__(self):
        return self.Category    
class Entertainment_news(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='static/zoom', height_field=None, width_field=None, max_length=None)
    date=models.DateField(default=now,auto_now=False, auto_now_add=False)
    category=models.ForeignKey("movies_category", on_delete=models.CASCADE)
    class Meta:
        db_table = 'Entertainment News'
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("movie", kwargs={"pk": self.pk})

class reviews(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='static/zoom', height_field=None, width_field=None, max_length=None)
    date=models.DateField(default=now,auto_now=False, auto_now_add=False)
    category=models.ForeignKey("movies_category", on_delete=models.CASCADE)
    class Meta:
        db_table='Reviews'
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("movie", kwargs={"pk": self.pk})
        
class articles(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    img=models.ImageField(upload_to='static/zoom', height_field=None, width_field=None, max_length=None)
    date=models.DateField(default=now,auto_now=False, auto_now_add=False)
    category=models.ForeignKey("news_category", on_delete=models.CASCADE)
    class Meta:
        db_table='Articles'
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("movie", kwargs={"pk": self.pk})
        
class video(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    img1=models.FileField(upload_to='static/zoom', max_length=100)
    vid=models.ImageField(upload_to='static/zoom')
    date=models.DateField(default=now,auto_now=False, auto_now_add=False)
    category=models.ForeignKey("news_category", on_delete=models.CASCADE)
    class Meta:
        db_table='Video'
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("movie", kwargs={"pk": self.pk})
        
class subscription_alert(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=254)
    is_active=models.BooleanField( default=True)
    