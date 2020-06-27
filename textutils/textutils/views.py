#Created By- Ayush Jain

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    d = {'name':'Ayush', 'place': 'Indore'}
    return render(request, 'index.html', d)

def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepu = request.POST.get('removepunc', 'off')
    caps = request.POST.get('caps', 'off')
    newline = request.POST.get('newline', 'off')
    space = request.POST.get('space', 'off')



    if removepu == "on":
        analyze = ""
        punctuations = '''!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        d = {'purpose': 'Removed Punctuations', 'analyze_text': analyze}
        djtext = analyze
        
    if(caps=="on"):
        analyze = ""
        for char in djtext:
            analyze = analyze + char.upper()
        d = {'purpose': 'UPPERCASE', 'analyze_text': analyze}
        djtext = analyze

    if(newline == "on"):
        analyze = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyze = analyze + char
        d = {'purpose': 'New Line Removal', 'analyze_text': analyze}
        djtext = analyze

    if (space == "on"):
        analyze = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]== " " and djtext[index+1] == " "):
                analyze = analyze + char
        d = {'purpose': 'Extra Space Removal', 'analyze_text': analyze}
        djtext = analyze

    if((removepu != "on") and (caps != "on") and (newline != "on") and (space != "on")):
        return HttpResponse("Error")

    return render(request, 'analyze.html', d)