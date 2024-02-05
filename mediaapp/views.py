from django.shortcuts import render
from mediaapp.models import Media

def media(request):
    return render(request,'media.html')

def Audio(request):
    audio_files = Media.objects.audio()
    context={}
    context['data']=audio_files
    return render(request,'audio.html',context)

def Video(request):
    video_files = Media.objects.video()
    context={}
    context['data']=video_files
    return render(request,'video.html',context)

def Images(request):
    image_files = Media.objects.images()
    context={}
    context['data']=image_files
    return render(request,'images.html',context)



