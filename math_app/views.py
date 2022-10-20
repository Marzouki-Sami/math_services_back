from math import sin, cos

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from spyne import Double, rpc, Application
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase

import math_services


class MathService(ServiceBase):

    @rpc(Double(nullable=False), Double(nullable=False), _returns=Double)
    def min(self, a, b):
        return min(a, b)

    @rpc(Double(nullable=False), Double(nullable=False), _returns=Double)
    def max(self, a, b):
        return max(a, b)

    @rpc(Double(nullable=False), Double(nullable=False), _returns=Double)
    def sin(self, a):
        return sin(a)

    @rpc(Double(nullable=False), _returns=Double)
    def cos(self, a):
        return cos(a)

    soap_app = Application([math_services], tns='math.isg.tn', in_protocol=Soap11(validator='lxml'),out_protocol=Soap11())
    django_app = DjangoApplication(soap_app)
    MyApplication = csrf_exempt(django_app)
