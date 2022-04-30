from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib import messages
from .forms import mangaaddform,genreaddform
from .models import booktbl,genretbl

from django.urls import reverse


def animedetailsfunc(request):
    return render(request, 'animedetails.html',)

def animewatchingfunc(request):
    return render(request, 'animewatching.html',)

def blogfunc(request):
    return render(request, 'blog.html',)

def blogdetailsfunc(request):
    return render(request, 'blogdetails.html',)

def genrefunc(request):
    return render(request, 'genre.html',)

def loginfunc(request):
    return render(request, 'login.html',)

def homefunc(request):
    return render(request, 'index.html', )


#def mangaaddformfunc(request):
    #context ={'form':mangaform}
    #return render(request, "mangaform.html",context)

    
def mangalistfunc(request):
    if booktbl.objects.exists():
        temp = booktbl.objects.all()
        context = {'temp':temp}
        return render(request, 'mangalist.html', context)
    else:
        if not booktbl.objects.exists():
            return render(request, 'mangalist.html',)
    return render(request, 'mangalist.html', context)


def mangareaderfunc(request):
    return render(request, 'mangareader.html',)

def signupfunc(request):
    return render(request, 'signup.html',)


def mangaaddformfunc(request):
    if request.method=='GET':
        form = mangaaddform()
        context={'form':form}
        return render(request, 'mangaaddform.html', context)
    elif request.method=='POST':
        form = mangaaddform(request.POST)
        if form.is_valid():
            temp=form.save(commit=True)
            print(temp.id)
        return render(request, 'mangaaddform.html')
            

def genreaddformfunc(request):
    form = genreaddform()
    if request.method == "POST":
        form = genreaddform(request.POST)
        if form.is_valid():
            #temp = form.save()
            messages.success(request, "form saved")
            print("success")
            a = form.save(commit = False)
            a.save()

            # return redirect("home")
        # form = genreaddform()
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            print("unsuccess")
    return render (request=request, template_name="genreaddform.html", context={"form":form})


def genrelistfunc(request):
    if genretbl.objects.exists():
        temp = genretbl.objects.all()
        context = {'temp':temp}
        return render(request, 'genrelist.html', context)
    else:
        if not genretbl.objects.exists():
            return render(request, 'genrelist.html',)
    return render(request, 'genrelist.html', context)
