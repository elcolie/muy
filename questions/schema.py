import graphene
from django.forms import ModelForm
from graphene import Field
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.forms.mutation import DjangoModelFormMutation
from graphene_django.rest_framework.mutation import SerializerMutation
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from questions.models import Question, PetModel, Category
from sieg_heil.schema import CategoryNode, IngredientNode, IngredientFilter


class QuestionType(DjangoObjectType):
    extra_field = graphene.String()

    class Meta:
        model = Question
        fields = (
            'id',
            'question_text',
            'category',
        )

    def resolve_extra_field(self, info):
        return 'Hello!'


class QuestionMutation(graphene.Mutation):
    question = graphene.Field(QuestionType)

    class Arguments:
        text = graphene.String(required=True)
        id = graphene.ID()

    def mutate(self, info, text, id):
        question = Question.objects.get(pk=id)
        question.text = text
        question.save()
        return QuestionMutation(question=question)


class DeleteQuestion(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        obj = Question.objects.get(id=kwargs.get('id'))
        obj.delete()
        return cls(ok=True)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'id',
            'question_text',
            'category',
        )


class QuestionSerializerMutation(SerializerMutation):
    delete_question = DeleteQuestion.Field()

    class Meta:
        serializer_class = QuestionSerializer
        model_operation = ['crated', 'update']
        lookup_field = 'id'


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = (
            'id',
            'foo',
        )


class PetForm(ModelForm):
    class Meta:
        model = PetModel
        fields = ('kind',)


class PetType(DjangoObjectType):
    class Meta:
        model = PetModel
        fields = (
            'id',
            'kind',
        )


class PetMutation(DjangoModelFormMutation):
    pet = Field(PetType)

    class Meta:
        form_class = PetForm


class PetSerializer(ModelSerializer):
    class Meta:
        model = PetModel
        fields = ['kind', ]


class PetMutation(SerializerMutation):
    class Meta:
        serializer_class = PetSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


class Mutation(graphene.ObjectType):
    update_question = QuestionMutation.Field()
    xxx = QuestionSerializerMutation.Field()


class QPQuery(graphene.ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)
    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode, filterset_class=IngredientFilter)

    questions = graphene.List(QuestionType)
    question = graphene.Field(QuestionType,
                              question_id=graphene.String(),
                              bar=graphene.Int())

    pets = graphene.List(PetType)
    pet = graphene.Field(PetType, pet_id=graphene.Int())

    def resolve_questions(self, info, **kwargs):
        return Question.objects.all()

    def resolve_question(self, info, question_id):
        return Question.objects.get(pk=question_id)

    def resolve_pets(self, info, **kwargs):
        return PetModel.objects.all()

    def resolve_pet(self, info, pet_id):
        return PetModel.objects.get(pk=pet_id)


schema = graphene.Schema(query=QPQuery, mutation=Mutation)
