from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
    words = Word.objects.all()
    return HttpResponse(loader.get_template('pages/all.html').render(context={"pageName": "All Words", "words": words, "total": len(words) }, request=req))
        

def search(req):
        q = req.GET.get("q")
        # if exact choise is on
        exact = req.GET.get("exact")
        if exact == "on":
            word = Word.objects.filter(english=q ) or Word.objects.filter(german=q )
            return HttpResponse(loader.get_template('pages/search.html').render(context={"pageName": "Search Results", "words": word, "total": len(word)}, request=req)) 
        else:
            # print(req.GET.get("q"))
            # look for word=q, that match in word model/table
            word = Word.objects.filter(english__contains=q ) or Word.objects.filter(german__contains=q )
            # Hint: We can use or own query
            # Word.objects.raw("SELECT * FROM ....")
            # number = Model.objects.filter(column__gte=2) ==> greater than equal 2
            # SELECT * FROM Table WHERE condition1 OR condition2 OR Conditions_n
            # print(dir(word))
            # for w in word:
            #     print(w)
            return HttpResponse(loader.get_template('pages/search.html').render(context={"pageName": "Search Results", "words": word, "total": len(word)}, request=req)) 

def delete(req):
    if req.method == "POST":
        print("You ar trying to delete: "+req.POST.get('word_id'))
        word_PK = req.POST.get('word_id')
        Word.objects.filter(pk=word_PK).delete()

        # for i in w:
        #     print(i)
        return HttpResponseRedirect('/all')
    

def edit(req):
    if req.method == "GET":
        word_id = req.GET.get("word_Id")
        word = Word.objects.filter(pk=word_id).first()
        form = WordForm(instance = word)
        return HttpResponse(loader.get_template("pages/edit.html").render(context={"pageName": "Edit", "word": word ,"form":form}, request=req))
    else:
        word_Id = req.POST.get("pk")
        english = req.POST.get("english")
        german = req.POST.get("german")
        print(word_Id)
        """
        The Following method works to update: 
        """
        # word = Word.objects.select_for_update().filter(pk = word_Id).update(english=english,german=german)
        w = Word.objects.get(pk= word_Id)
        w.english = english
        w.german = german
        w.save() 
        return HttpResponseRedirect('/all')
