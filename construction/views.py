from multiprocessing import context
from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from .form import *
from django.contrib import messages
from django.core.paginator import Paginator


def index(request):
    aboutus = Aboutus.objects.all()
    ourstory = Ourstory.objects.order_by('-date_posted').filter(published=True)
    whatwedo = Whatwedo.objects.all()
    integrity = Integrity.objects.all()
    gimg = Gallery.objects.all()[:4]
    stats = Stats.objects.all()
    slider = Slider.objects.all()
    customers = Customers.objects.all()
    testimonials = Testimonials.objects.all()[:4]
    moreinfo = Moreinfo.objects.order_by('-date_posted').filter(published=True)
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:2]
    ourservice = Ourservice.objects.order_by('-date_posted').filter(published=True)
    services = Services.objects.order_by('-date_posted').filter(published=True)[:6]

    context = { 
        'aboutus': aboutus,
        'ourstory': ourstory,
        'whatwedo': whatwedo,
        'integrity': integrity,
        'stats': stats,
        'moreinfo': moreinfo,
        'blog': blog,
        'slider': slider,
        'customers': customers,
        'testimonials': testimonials,
        'ourservice': ourservice,
        'services': services,
        'gimg':gimg    
}

    return render(request,'construction/index.html',context)

def services(request):
    whatweoffer = Whatweoffer.objects.order_by('-date_posted').filter(published=True)[:1]
    ourservice = Ourservice.objects.order_by('-date_posted').filter(published=True)
    services = Services.objects.order_by('-date_posted').filter(published=True)[:6]

    integrity = Integrity.objects.all() 
    gimg = Gallery.objects.all() 
    context = { 
        'whatweoffer': whatweoffer,
        'integrity': integrity,
        'ourservice': ourservice,
        'gimg':gimg,
        'services': services,
    }

    return render(request,'construction/services.html',context)

def gallery(request):   
    gimg = Gallery.objects.all()

    context = {
        'gimg':gimg
    }
    return render(request,'construction/gallery.html',context)

def about(request):
    moreinfo = Moreinfo.objects.order_by('-date_posted').filter(published=True)[:1]
    ourstory = Ourstory.objects.order_by('-date_posted').filter(published=True)[:1]
    ourteam = Ourteam.objects.order_by('-date_posted').filter(published=True)[:10]
    basicfuctions = Basicfuctions.objects.all()[:1]
    ourteamtext = Ourteamtext.objects.all()[:1]
    
    context = { 
    'moreinfo': moreinfo,
    'ourstory': ourstory,
    'basicfuctions': basicfuctions,
    'ourteamtext': ourteamtext,
    'ourteam': ourteam,
    }

    return render(request,'construction/about.html',context)

def blog(request):   
    blog = Blog.objects.order_by('-date_posted').filter(published=True)

    paginator = Paginator(blog, 9)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    
    context = {
        'blog': paged_blog,
    }
    return render(request,'construction/blog.html',context)

def blogdetail(request, slug_id):  
    blogdetail = Blog.objects.filter(slug=slug_id).first()
    services = Services.objects.order_by('-date_posted').filter(published=True)[:6]

    context = {
        'post': blogdetail,
        'services': services,
        
    }
    return render(request,'construction/blogdetail.html',context)    

def contact(request):
    if request.method == 'POST':
    
      try:
          connect = Contact(fname=request.POST['fname'],lname=request.POST['lname'],phone=request.POST['phone'],email=request.POST['email'],message=request.POST['message'])
          messages.success(request,f"{request.POST['fname']} Sent Successfully!!")

          connect.save()
          return redirect('contact')

      except Exception as e:
          messages.error(request,f"Something went wrong...")

    return render(request,'construction/contact.html')

def ourstorydetail(request, slug_id):
    ourstory = Ourstory.objects.filter(slug=slug_id).first()
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:6]
    context = {
        'blog': blog,
        'post': ourstory,
    }
    return render(request,'construction/ourstorydetail.html',context)

def aboutusdetail(request, my_id):
    aboutus = get_object_or_404(Aboutus, pk=my_id)
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:6]
    context = {
        'blog': blog,
        'post': aboutus,
    }
    return render(request,'construction/aboutusdetail.html',context)

def servicesdetail(request, slug_id):
    service = Services.objects.filter(slug=slug_id).first()
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:6]

    context = {
        'post': service,
        'blog': blog,

    }
    return render(request,'construction/servicesdetail.html',context)

def whatwedodetail(request, mm_id):
    whatwedo = get_object_or_404(Whatwedo, pk=mm_id)
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:6]
    context = {
        'blog': blog,
        'post': whatwedo,
    }
    return render(request,'construction/whatwedodetail.html',context)

def moreinfodetail(request, slug_id):
    moreinfo = Moreinfo.objects.filter(slug=slug_id).first()
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:6]
    context = {
        'blog': blog,
        'post': moreinfo,
    }
    return render(request,'construction/moreinfodetail.html',context)

def whatweofferdetail(request, slug_id):
    whatweoffer = Whatweoffer.objects.filter(slug=slug_id).first()
    blog = Blog.objects.order_by('-date_posted').filter(published=True)[:6]
    context = {
        'blog': blog,
        'post': whatweoffer,
    }
    return render(request,'construction/whatweofferdetail.html',context)




