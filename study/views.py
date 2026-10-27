from django.shortcuts import render

def home(request):
    return render(request, "base.html", {
        "title": "Головна сторінка",
        "text": "Це моя перша сторінка на Django.",
    })

def about(request):
    return render(request, "base.html", {
        "title": "Про мене",
        "text": "Мене звати ...",
    })