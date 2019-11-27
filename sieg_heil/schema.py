from django_filters import FilterSet, OrderingFilter
from graphene import relay
from graphene_django import DjangoObjectType

from ingredients.models import Category, Ingredient


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node,)


class IngredientFilter(FilterSet):
    order_by = OrderingFilter(
        fields=(
            ('name', 'name'),
            ('notes', 'notes'),
            ('category__name', 'category__name'),
        )
    )

    class Meta:
        model = Ingredient
        fields = (
            'name',
            'notes',
            'category__name',
        )


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node,)
