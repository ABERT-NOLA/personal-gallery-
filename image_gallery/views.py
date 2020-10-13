from django.shortcuts import render
from image_gallery.models import imggal

def imagedisplay(request):
    resultsdisplay=imggal.objects.all()
    return render(request,'index.html',{'imggal':resultsdisplay})
