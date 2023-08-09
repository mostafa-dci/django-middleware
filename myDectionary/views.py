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
        print(req.POST.get("german"))
        english = req.POST.get('english')
        german = req.POST.get("german")
        mo = req.POST.get("mostafa")
        print(mo)
        if german == "" or english == "":
            return HttpResponse("ERROR")
        else:
            return HttpResponse("Done")
