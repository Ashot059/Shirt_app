from django.shortcuts import render


def base(request):
    return render(request, 'shirtapp/base.html')


def tobarcelona(request):
    return render(request, 'shirtapp/barcelona.html')


def toreal(request):
    return render(request, 'shirtapp/real.html')


def tocity(request):
    return render(request, 'shirtapp/city.html')


def todvb(request):
    return render(request, 'shirtapp/dvb.html')


def tountd(request):
    return render(request, 'shirtapp/untd.html')


def toliverpool(request):
    return render(request, 'shirtapp/liv.html')
