from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from . forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.views import View
# Create your views here.





@login_required
def home_view(request):
    offers = SkillOffer.objects.all()
    requests = SkillRequest.objects.all()

    context = {
        "offers":offers,
        "requests":requests
    }

    return render(request, "home.html", context)


@login_required
def create_offer(request):
    form = OfferForm(request.POST)
    if form.is_valid():
        offer = form.save(commit = False)
        offer.user = request.user
        offer.save()
        return redirect('home')
    else:
        form = OfferForm()
    
    
    return render(request, "offer_form.html", {"form":form})

@login_required
def create_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.requester = request.user
            req.save()
            return redirect('home')
    else:
        form = RequestForm()
    return render(request, 'request_form.html', {'form': form})





class Signup(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, "signup.html",{"form":form})
    
    def post(self, request):
        form = RegisterForm(request.POST or None)
        if form .is_valid():
            form.save()
            return redirect('login')
        return render(request,"signup.html", {"form":form})
    


def logout(request):
    auth_logout(request)
    return redirect('login')