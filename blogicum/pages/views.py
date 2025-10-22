from django.shortcuts import render

app_name = 'pages'


def about(request):
    """Описание"""
    template = 'about/about.html'
    return render(request, template)


def rules(request):
    """Правила"""
    template = 'rules/rules.html'
    return render(request, template)
