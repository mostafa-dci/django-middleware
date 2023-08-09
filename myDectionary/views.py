from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Word, WordForm
# Create your views here.

## index view
def index(req):
    # return HttpResponse("Hello World")
    return HttpResponse(loader.get_template('pages/home.html').render(context={"pageName": "Landing Page"}))

def addWord(req):
    if req.method == "GET":
        return HttpResponse(loader.get_template('pages/addWord.html').render(context={"pageName": "Add Word", "form": WordForm()}, request=req))
    else:# For POST Request
        # Store the new word
        print("################")
        wordForm = WordForm(req.POST)
        if wordForm.is_valid():
            # Store
            wordForm.save()
            return HttpResponse("Done")
        else:
            return HttpResponse("ERROR, Not saved")
        
def all(req):
    return HttpResponse(loader.get_template('pages/all.html').render(context={"pageName": "All Words", "words": Word.objects.all()}, request=req))
        
