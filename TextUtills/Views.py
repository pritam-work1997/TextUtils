from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunch = request.POST.get('removepunch','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    countchar = request.POST.get('countchar','off')
    if removepunch  == "on":

        print(djtext)
        print(removepunch)
        analyzed  = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removing Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request,'analyze.html',params)
    if(fullcaps == "on"):
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
        djtext = analyzed
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        #return render(request, 'analyze.html', params)
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed Space', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)
    if(countchar=="on"):
        analyzed = 0
        for char in djtext:
            analyzed +=1
        params = {'purpose': 'Count Character', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyze.html', params)
    if (removepunch != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)





#def removepuch(request):

#def capfirst(request):
    #return HttpResponse("capitalize first")
#def newlineremove(request):
    #return HttpResponse("New line remove")
#def spaceremove(request):
    #return HttpResponse("Space remove <a href = '/'>back<a/>")
#def charcount(request):
    #return HttpResponse("Char count")
