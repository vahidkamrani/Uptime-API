import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def uptime(request):
# sending the uptime command as an argument to popen()
# and saving the returned result (after truncating the trailing \n)
    t = os.popen('python -m uptime').read()[7:-1]
    n = os.popen('uptime -p').read()[:2]
    _values = [t,n]
    _keys = ['Up Time','Status']
    cal = dict(zip(_keys,_values))
    message = {'Message':"عملیات با موفقیت انجام شد"}
    status1 = status.is_success(200)
    print(status1)
    if  status1:
        result = dict(Haserrore = not status1)
        result.update(message)
        result.update(cal)
        return Response(result)
    else:
        result = dict(Haserorre = status1)
        message = {'masaage':"عملیات ناموفق است"}
        result.update(message)
        return Response(result)
