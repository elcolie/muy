from model_mommy import mommy


def gen_func():
    return {
        'key': "value"
    }


mommy.generators.add('django.contrib.postgres.fields.JSONField', gen_func)
