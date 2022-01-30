
import os
import json
from unittest import result
from webbrowser import get
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def uptime1(request):
# sending the uptime command as an argument to popen()
# and saving the returned result (after truncating the trailing \n)
    t = os.popen('python -m uptime').read()[8:-17]
    n = os.popen('uptime -p').read()[:-19]
    m = [t,n]
    x = ['Up Time','Status']
    result = dict(zip(x,m))

    return Response(result)