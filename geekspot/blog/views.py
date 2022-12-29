from django.shortcuts import render
from json import loads
from django.http import HttpResponse
# Create your views here.
site = """
<h1>Text 1</h1> \n
<h2>Text 2</h2> \n
<h3>Text 3</h3> \n
<h4>Text 4</h4> \n
<h5>Text 5</h5> \n
<h6>Text 6</h6> \n
"""
def index(request):
    return HttpResponse(site)