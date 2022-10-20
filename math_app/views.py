from math import sin, cos

from django.views.decorators.csrf import csrf_exempt
from spyne.model.primitive import Double
from spyne.decorator import rpc
from spyne.application import Application
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase


class MathService(ServiceBase):

    @rpc(Double(nillable=False), Double(nillable=False), _returns=Double)
    def min(self, a, b):
        return min(a, b)

    @rpc(Double(nillable=False), Double(nillable=False), _returns=Double)
    def max(self, a, b):
        return max(a, b)

    @rpc(Double(nillable=False),  _returns=Double)
    def sin(self, a):
        return sin(a)

    @rpc(Double(nillable=False), _returns=Double)
    def cos(self, a):
        return cos(a)


soap_app = Application([MathService], tns='math.isg.tn', in_protocol=Soap11(validator='lxml'), out_protocol=Soap11())
django_app = DjangoApplication(soap_app)
MyApplication = csrf_exempt(django_app)
