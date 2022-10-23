from django.shortcuts import redirect, render
from . models import TRACKING
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
def index(request):
    qs = []
    if request.method == 'POST':
        track_id = request.POST.get('id')
        fillid = TRACKING.objects.filter(TRACKING_ID=track_id)
        if fillid.exists():
            qs = TRACKING.objects.get(TRACKING_ID=track_id)
            context = {'data':qs}
            return render(request,'index/tracking.html',context)
        else:
            # messages.error(request, 'invalid ID')
            return render(request, 'index/error.html')
    return render(request, 'index/index.html')
def index2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' Message Sent Successfully !')
            return redirect('/#contact')
        else:
            messages.error(request, ' Message Not Sent, Please Try Again')
            return redirect('/#contact')
    return render(request, 'index/index.html')

def tracking(request):
    qs = []
    if request.method == 'POST':
        track_id = request.POST.get('id')
        fillid = TRACKING.objects.filter(TRACKING_ID=track_id)
        if fillid.exists():
            qs = TRACKING.objects.get(TRACKING_ID=track_id)
            context = {'data':qs}
            return render(request,'index/tracking.html',context)
        else:
            # messages.error(request, 'invalid ID')
            return render(request, 'index/error.html')
    return render(request, 'index/tracking.html')
def tracking2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' Message Sent Successfully')
            return redirect('/tracking/')
        else:
            messages.error(request, ' Message Not Sent, Please Try Again')
    else:
        return render(request, 'index/index.html')
    return render(request, 'index/tracking.html')

def pagerror(request):
    qs = []
    if request.method == 'POST':
        track_id = request.POST.get('id')
        fillid = TRACKING.objects.filter(TRACKING_ID=track_id)
        if fillid.exists():
            qs = TRACKING.objects.get(TRACKING_ID=track_id)
            context = {'data':qs}
            return render(request,'index/tracking.html',context)
        else:
            # messages.error(request, 'invalid ID')
            return render(request, 'index/error.html')
    return render(request, 'index/tracking.html')
def pagerror2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' Message Sent Successfully')
            return redirect('/error/')
        else:
            messages.error(request, ' Message Not Sent, Please Try Again')
    else:
        return render(request, 'index/error.html')
    return render(request, 'index/error.html')
def tracking_app_tablet(request):
    return redirect('/#tracking-app-tablet')
def major_services(request):
    return redirect('/#major-services')
def portfolio(request):
    return redirect('/#portfolio')
def contact(request):
    return redirect('/#contact')


