from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter

def homepage(request):
    return render(request,'home.html')
def wordcount(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    wordcount = {}
    for k in wordlist:
        if k in wordcount:
            #increase number
            wordcount[k]+=1
        else:
            wordcount[k]=1

    wordcount = [[k,v] for k,v in wordcount.items()]
    #wordcount = (sorted(wordcount)).reverse()
    #wordcount = sorted(wordcount, key=lambda tup: tup[1]))
    wordcount=sorted(wordcount, key=itemgetter(1),reverse = True)

    return render(request,'wordcount.html',{'fulltext':fulltext,'count':len(wordlist),'wordcount':wordcount})
def about(request):
    return render(request,'about.html')
