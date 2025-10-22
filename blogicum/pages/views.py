from django.shortcuts import render

app_name = 'pages'


def about(request):
    """Описание"""
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    """Правила"""
    template = 'pages/rules.html'
    return render(request, template)
