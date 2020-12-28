from urllib import request

from django.conf.locale import hi
from django.http import HttpResponse
from django.shortcuts import render
from urllib import request

from django.conf.locale import hi
from django.http import HttpResponse
import pandas as pd

df1 = pd.read_csv('/Users/macosx/Downloads/github_question.csv')

# import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords


# import re

def preprocess(sentence):
    sentence = sentence.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(sentence)
    filtered_words = [w for w in tokens if not w in stopwords.words('english')]
    f = " ".join(filtered_words)

    count = {}
    for i in f.split(' '):
        count[i] = count.get(i, 0) + 1
    return count


def recherche(df1, requete,r):
    c = preprocess(requete)
    cont = 0
    listurl = []
    for i in range(0, len(df1)):

        a = preprocess(df1.title[i])
        b = preprocess(df1.description[i])

        for x in c.keys():
            if x in (a.keys() or x in (b.keys())):
                # listurl.append(df1.url[i])

                # if c not in listurl :
                A=  df1.title[i]
                B = "https://stackoverflow.com" + df1.url[i]
                C = df1.description[i]

    if r==1 :
        return A
    elif r==2 :
        return B
    else :
        return C

            # else :
            # cont=+1


def recherche1(df1, requete, r):
    c = preprocess(requete)
    cont = 0
    A = []
    B = []
    C = []
    for i in range(0, len(df1)):

        a = preprocess(df1.title[i])
        b = preprocess(df1.description[i])

        for x in c.keys():
            if x in (a.keys() or x in (b.keys())):
                # listurl.append(df1.url[i])

                if df1.title[i] not in A:
                    A.append("- TITLE :   " + df1.title[i])
                if df1.url[i] not in B:
                    B.append("- URL :   " + "https://stackoverflow.com" + df1.url[i])
                if df1.description[i] not in C:
                    C.append("- DESC :   " + df1.description[i])

        A = list(set(A))
        B = list(set(B))
        C = list(set(C))

    if r == 1:
        return (A)
    elif r == 2:
        return (B)
    else:
        return (C)






def get(self, request, *args, **kwargs):
    q = request.GET.get('requete')
    error = ''

    return render(request, 'index3.html' ,  {'error': error ,'q':q,})


def index(request):



    Req1 = "la de un une working  ou functionality  sauf de répercussions ?aaa sauf "


    document = recherche(df1,Req1,1)
    document2 = recherche(df1, Req1,2)
    document3= recherche(df1, Req1,3)
    context = {"document": document,"document2":document2 ,"document3":document3,}

    return render(request, 'index.html', context)



def index2(request):
    Req1 = request.GET.get('requete')
    #Req1 = "la de un une working  ou functionality  sauf de répercussions ?aaa sauf "
    #Req1 = How to customize account menu in opencart 3



    l = recherche1(df1, Req1, 1)
    l1 = recherche1(df1, Req1, 2)
    l2 = recherche1(df1, Req1, 3)
    from io import StringIO
    output = StringIO()
    for i in range(0, len(l)):
        print("RESULT", i + 1, "  :", "\n", l[i], "\n", "\n", l1[i], "\n", "\n",
              l2[i], "\n", "\n", "****************************************************************",
              "\n" , file=output )





    x= output.getvalue()


    context = {"Req1":Req1, "x":x}


    return render(request, 'index2.html', context)



def about(request):



    context = {}


    return render(request, 'index3.html', context)


def index4(request):
    Req1 = request.GET.get('requete1')
    #Req1 = "la de un une working  ou functionality  sauf de répercussions ?aaa sauf "
    #Req1 = How to customize account menu in opencart 3

    document = recherche(df1, Req1, 1)
    document2 = recherche(df1, Req1, 2)
    document3 = recherche(df1, Req1, 3)




    context = {"document": document, "document2": document2, "document3": document3,"Req1":Req1, }


    return render(request, 'index4.html', context)

def advanced(request):



    Req1 = "la de un une working  ou functionality  sauf de répercussions ?aaa sauf "


    document = recherche(df1,Req1,1)
    document2 = recherche(df1, Req1,2)
    document3= recherche(df1, Req1,3)
    context = {"document": document,"document2":document2 ,"document3":document3,}

    return render(request, 'advanced.html', context)