from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_page_view(request):
    """
    [summary]

    Parameters
    ----------
    request : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """    
    return HttpResponse("hello world!\nare you ok?if you are fine tell me about it")