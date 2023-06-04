from re import T
from django.db import models
from datetime import datetime
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Slider(models.Model):
    title1 = models.CharField(max_length=1000,null=True,blank=True)
    smalltext1 = models.CharField(max_length=1000,null=True,blank=True)
    title2 = models.CharField(max_length=1000,null=True,blank=True)
    smalltext2 = models.CharField(max_length=1000,null=True,blank=True)
    title3 = models.CharField(max_length=1000,null=True,blank=True)
    smalltext3 = models.CharField(max_length=1000,null=True,blank=True)
    title4 = models.CharField(max_length=1000,null=True,blank=True)
    smalltext4 = models.CharField(max_length=1000,null=True,blank=True)
    def __str__(self):
        return self.title1

class Basicfuctions(models.Model):
    title = models.CharField(max_length=550)
    title1 = models.CharField(max_length=550)
    text1 = models.TextField()
    title2 = models.CharField(max_length=550)
    text2 = models.TextField()
    title3 = models.CharField(max_length=550)
    text3 = models.TextField()
    title4 = models.CharField(max_length=550)
    text4 = models.TextField()


    def __str__(self):
        return self.title

class Moreinfo(models.Model):
    subtitle = models.CharField(max_length=550)
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    leadimg = models.ImageField(default='myleadimg.jpg',null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Moreinfo, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Moreinfo'
        managed = True
        verbose_name = 'Moreinfo'
        verbose_name_plural = 'Moreinfo'

class Ourstory(models.Model):
    subtitle = models.CharField(max_length=550)
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg')
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Ourstory, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Ourstory'
        managed = True
        verbose_name = 'Ourstory'
        verbose_name_plural = 'Ourstory'

class Customers(models.Model):
    name = models.CharField(max_length=550)
    city = models.CharField(max_length=550)
    date_posted = models.DateTimeField(default=datetime.now())
    img = models.ImageField()
    body = models.TextField()

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    subtitle = models.CharField(max_length=550)
    title = models.CharField(max_length=550)
    body = models.TextField()

    def __str__(self):
        return self.title

class Aboutus(models.Model):
    subtitle = models.CharField(max_length=550)
    title = models.CharField(max_length=550)
    title1 = models.CharField(max_length=550)
    title2 = models.CharField(max_length=550)
    title3 = models.CharField(max_length=550)
    leadimg = models.ImageField(default='myleadimg.jpg',null=True,blank=True)

    body = RichTextField()

    def __str__(self):
        return self.title

class Whatwedo(models.Model):  
    subtitle = models.CharField(max_length=550)
    title = models.CharField(max_length=550)
    quality_services = models.CharField(max_length=550,null=True,blank=True)
    number1 = models.CharField(max_length=550,null=True,blank=True)
    Weorking_ability = models.CharField(max_length=550,null=True,blank=True)
    number2 = models.CharField(max_length=550,null=True,blank=True)
    machine_power = models.CharField(max_length=550,null=True,blank=True)
    number3 = models.CharField(max_length=550,null=True,blank=True)
    detailed_planning = models.CharField(max_length=550,null=True,blank=True)
    number4 = models.CharField(max_length=550,null=True,blank=True)
    improved_operating_conditions = models.CharField(max_length=550,null=True,blank=True)
    number5 = models.CharField(max_length=550,null=True,blank=True)
    leadimg = models.ImageField(default='myleadimg.jpg',null=True,blank=True)
    body = RichTextField()

    def __str__(self):
        return self.title

class Whatweoffer(models.Model):
    subtitle = models.CharField(max_length=550)
    title = models.CharField(max_length=550)
    firsttext = models.TextField()
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    leadimg = models.ImageField(default='myleadimg.jpg',null=True,blank=True)
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Whatweoffer, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Whatweoffer'
        managed = True
        verbose_name = 'Whatweoffer'
        verbose_name_plural = 'Whatweoffer'

class Integrity(models.Model):
    title1 = models.CharField(max_length=550)
    text1 = models.TextField()
    title2 = models.CharField(max_length=550)
    text2 = models.TextField()
    title3 = models.CharField(max_length=550)
    text3 = models.TextField()
    title4 = models.CharField(max_length=550)
    text4 = models.TextField()

    def __str__(self):
        return self.title1

class Ourservice(models.Model):
    subtitle = models.CharField(max_length=550)
    title = models.CharField(max_length=550)
    subtext = models.TextField()
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Ourservice, self).save(*args, **kwargs)

    class Meta:
        db_table = 'ourservice'
        managed = True
        verbose_name = 'ourservice'
        verbose_name_plural = 'ourservice'

class Services(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    leadimg = models.ImageField(default='myleadimg.jpg')
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Services, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Services'
        managed = True
        verbose_name = 'Services'
        verbose_name_plural = 'Services'

class Ourteamtext(models.Model):
    subtitle = models.CharField(max_length=550)
    title = models.CharField(max_length=550)
    text = models.TextField()

    def __str__(self):
        return self.title

class Ourteam(models.Model):
    title = models.CharField(max_length=550)
    post = models.CharField(max_length=550)
    published = models.BooleanField(default=True,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    img = models.ImageField()

class Stats(models.Model):
    subtitle = models.CharField(max_length=550)
    title = models.CharField(max_length=550)
    img1 = models.ImageField()
    img2 = models.ImageField()
    text = models.TextField()
    number1 = models.CharField(max_length=50)
    text1 = models.CharField(max_length=50)
    number2 = models.CharField(max_length=50)
    text2 = models.CharField(max_length=50)
    number3 = models.CharField(max_length=50)
    text3 = models.CharField(max_length=50)
    number4 = models.CharField(max_length=50)
    text4 = models.CharField(max_length=50)

    def __str__(self):
        return self.title
        
class Blog(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=550,null=True,blank=True)
    published = models.BooleanField(default=True,null=True,blank=True)
    flag = models.BooleanField(default=False,null=True,blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    leadimg = models.ImageField(default='myleadimg.jpg')
    body = RichTextField()

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Blog'
        managed = True
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

class Gallery(models.Model):
    imggallery = models.ImageField()
    title = models.CharField(max_length=100)

    class Meta:
        db_table = 'gallery'
        managed = True
        verbose_name = 'Gallerys'
        verbose_name_plural = 'Gallerys'

class Contact(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.fname} {self.lname}'

    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contacts'
        verbose_name_plural = 'Contacts'          