import graphene
from graphene_django import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from rest_framework import serializers

from questions.models import Question, PetModel, Category


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

class Mutation(graphene.ObjectType):
    update_question = QuestionMutation.Field()

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'question_text',
            'category',
        )


class QuestionSerializerMutation(SerializerMutation):
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


class Pet(DjangoObjectType):
    class Meta:
        model = PetModel
        fields = (
            'kind',
        )
        convert_choices_to_enum = ['kind']


class Query(graphene.ObjectType):
    questions = graphene.List(QuestionType)
    question = graphene.Field(QuestionType,
                              question_id=graphene.String(),
                              bar=graphene.Int())
    pets = graphene.List(Pet)
    pet = graphene.Field(Pet, pet_id=graphene.Int())

    def resolve_questions(self, info, **kwargs):
        return Question.objects.all()

    def resolve_question(self, info, question_id, bar):
        return Question.objects.get(pk=question_id)

    def resolve_pets(self, info, **kwargs):
        return PetModel.objects.all()

    def resolve_pet(self, info, pet_id):
        return PetModel.objects.get(pk=pet_id)


schema = graphene.Schema(query=Query, mutation=Mutation)
