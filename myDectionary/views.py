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
        

def search(req):
    if req.method == "GET":
        # print(req.GET.get("q"))
        q = req.GET.get("q")
        # look for word=q, that match in word model/table
        word = Word.objects.filter(english__contains=q ) or Word.objects.filter(german__contains=q )
        # Hint: We can use or own query
        # Word.objects.raw("SELECT * FROM ....")
        # number = Model.objects.filter(column__gte=2) ==> greater than equal 2
        # SELECT * FROM Table WHERE condition1 OR condition2 OR Conditions_n
        # print(dir(word))
        # for w in word:
        #     print(w)
        return HttpResponse(loader.get_template('pages/search.html').render(context={"pageName": "Search Results", "words": word}, request=req)) 
