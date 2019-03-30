from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from eventexx.subscriptions.forms import SubscriptionForm

def subscribe(request):
    context = {'form': SubscriptionForm()}
    return render(request, 'subscriptions/subscription_form.html', context)