from django.http import HttpResponse
"""
    #This Middleware to print/store the request info from the client
"""
def requestLoggerMiddleware(getResponse):

    def middleware(req):
        print("\u001b[32mMy first Middleware is working\u001b[0m")
        # print query
        # http://localhost:5000/?car=bmw&color=red
        car = req.GET.get('car') # ===> bmw
        print(car)
        color = req.GET.get('color')
        print(color)
        # to dir/ explor objects in python, use dir(OBJ)
        # print(dir(req.GET))
        # for q in req.GET.items():
        #     print(q)
        response = getResponse(req)
        # some processing, missing some params/ queries
        # return HttpResponse("You are looking for a " + car + " with color: " + color)
        return response
    
    return middleware

def requestLoggerMiddleware2(getResponse):

    def middleware(req):
        print("\u001b[32mMy second Middleware is working\u001b[0m")
        response = getResponse(req)

        return response

    return middleware

# Middleware to control /add router entries
def checkEntries(get_response):
    def middleware(req):
        response = get_response(req)
        # if URL is /add AND if the method is POST
        if req.path == "/add/" and req.method == "POST":
            # check if german & english NOT EMPTY
            english = req.POST.get('english').strip()
            german = req.POST.get("german").strip() 
            if english == "" or german == "":
                # send error
                return HttpResponse("Please add word")
            if len(english) == 1 or len(german) == 1:
                 return HttpResponse("Please add a Real word !!!")
            return response
        else:
            return response
    return middleware