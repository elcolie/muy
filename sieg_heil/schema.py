import graphene

from fauzans.schemas import FauzanQueryMixin


class Query(FauzanQueryMixin, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
