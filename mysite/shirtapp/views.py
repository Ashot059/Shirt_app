import time
from django.contrib import messages
from .forms import BuyerForm
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback


def base(request):
    return render(request, 'shirtapp/base.html')


def feedback(request):
    return render(request, 'shirtapp/feedback.html')


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
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()  # Save the buyer's data to the database
            return redirect('success_page')  # Redirect to a success page or another appropriate page
    else:
        form = BuyerForm()

    return render(request, 'shirtapp/buy.html', {'form': form})


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review is accepted')  # Add success message
            time.sleep(1)
            return redirect('base')  # Redirect to the main page

    else:
        form = FeedbackForm()

    return render(request, 'shirtapp/feedback.html', {'form': form})


def feedback_list(request):
    feedback_data = Feedback.objects.all()
    return render(request, 'shirtapp/feedback_list.html', {'feedback_data': feedback_data})


def success_page(request):
    return render(request, 'shirtapp/success.html')


def about(request):
    return render(request, 'shirtapp/about.html')
