from django.shortcuts import render
from .forms import BuyForm


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


def buy(request):
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            # Здесь вы можете обработать данные заказа, например, сохранить их в базе данных
            message = "Покупка прошла успешно."
        else:
            message = "Пожалуйста, исправьте ошибки в форме."
    else:
        form = BuyForm()
        message = ""

    return render(request, 'shirtapp/buy.html', {'form': form, 'message': message})
