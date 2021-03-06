# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.template.loader import get_template
from django.template import Context,RequestContext

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import random
from .models import Stock
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def homepage(request):
    template = get_template('index.html')

    stocks = Stock.objects.all()
    # stock_list = list()
    # for count, stock in enumerate(stocks):
    #     stock_list.append("No.{}:".format(str(count)) + str(stock) + "<hr>")
    #     stock_list.append("<small>" + str(stock.name) + "\t" +
    #                       str(stock.industry.encode('utf-8')) + "\t" +
    #                       str(stock.area.encode('utf-8')) + "\t" +
    #                       "</small><br></br>")

    now = datetime.now()
    upper_five_stock = upper_top_five()
    lower_five_stock = lower_top_five()
    html = template.render(locals())

    return HttpResponse(html)


def upper_top_five():
    # upper_five_stock = Stock.objects.all()[1:6]
    # 市盈率
    data = Stock.objects.order_by('pe')
    data = data[::-1]
    upper_five_stock = data[0:5]

    return upper_five_stock


def lower_top_five():
    data = Stock.objects.order_by('npr')
    data = data[::-1]

    lower_five_stock = data[0:5]

    return lower_five_stock


def show_stock(request, stock_code):
    template = get_template('stock.html')
    try:
        stock = Stock.objects.get(code=stock_code)
        # acc = LSTM(str(stock_code))
        stock_url = "/static/images/pic/" + str(stock.code) + "pre.png"
        if stock != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

@csrf_exempt
def search(request):
    template = get_template('stock.html')
    if request.method == 'POST':
        code = request.POST['code']
    stock_url = "/static/images/pic/" + str(code) + "pre.png"
    try:
        stock = Stock.objects.get(code=code)
        if stock != None:
            html = template.render(locals())
            return HttpResponse(html)
            # return render_to_response("stock.html", context_instance=RequestContext(request))
        else:
            return redirect('/error')
    except:
        return redirect('/error')



    
def show_definition(request):
    template = get_template('definition.html')
    html = template.render(locals())
    return HttpResponse(html)


def show_useKnown(request):
    temmplate=get_template('useKnown.html')
    html=temmplate.render(locals())
    return HttpResponse(html)


def stock_list(request):
    stocks = Stock.objects.all()
    paginator=Paginator(stocks,30)
    p=request.GET.get('p')
    try:
        s=paginator.page(p)
    except PageNotAnInteger:
        s=paginator.page(1)
    except EmptyPage:
        s=paginator.page(paginator.num_pages)
    #request_context=RequestContext(request)
    #request_context.push(locals())
    return render(request,'list.html',locals())

def stock_contact(request):
    template = get_template('contact.html')
    html = template.render(locals())
    return HttpResponse(html)

def show_error(request):
    template = get_template('error.html')
    html = template.render(locals())
    return HttpResponse(html)
