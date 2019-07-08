import graphene
from graphene import Node
from graphene_django import DjangoObjectType

from fauzans.models import Fauzan


class FauzanNode(DjangoObjectType):
    class Meta:
        model = Fauzan
        interfaces = (Node,)
        filter_fields = {
            'id': ['exact', ],
            'label': ['exact', 'icontains', 'istartswith'],
            # 'name__key': ['exact', 'icontains', 'istartswith'],
        }


class FauzanQueryMixin:
    fauzans = graphene.List(FauzanNode)

    def resolve_fauzans(self, info):
        return Fauzan.objects.all()
