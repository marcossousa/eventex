# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from forms import SubscriptionForm
from models import Subscription

def success(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    context = RequestContext(request, {'subscription': subscription})
    return render_to_response('subscription/success.html', context)

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)
        
def create(request):
    form = SubscriptionForm(request.POST)
    
    if not form.is_valid():
        return render_to_subscription_form(form, request)
    
    subscription = form.save()
    send_confirmation_email(subscription) # should be moved to form or model?
    return HttpResponseRedirect(reverse('subscription:success', args=[ subscription.pk ]))

def new(request):
    form = SubscriptionForm()
    return render_to_subscription_form(form, request)
    
def render_to_subscription_form(form, request):
    context = RequestContext(request, {'form' : form})
    return render_to_response('subscription/new.html', context)
    
def send_confirmation_email(subscription):
    from django.core.mail import send_mail
    send_mail( 
        subject = u'Inscrição no EventeX', 
        message = u'Obrigado por se inscrever no EventeX!', 
        from_email = 'contato@eventex.com', 
        recipient_list = [ subscription.email ],
    )