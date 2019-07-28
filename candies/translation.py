from modeltranslation.translator import translator, TranslationOptions

from candies.models import Candy


class CandyTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)


translator.register(Candy, CandyTranslationOptions)
