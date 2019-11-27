import json

from django.test import TestCase


from graphene_django.utils.testing import GraphQLTestCase

from questions.schema import schema


class MyFancyTestCase(GraphQLTestCase):
    # Here you need to inject your test case's schema
    GRAPHQL_SCHEMA = schema

    def test_some_query(self):
        response = self.query(
            '''
            query{
                questions{
                    id
                    questionText
                }
            }
            '''
        )

        content = json.loads(response.content)

        # This validates the status code and if you get errors
        self.assertResponseNoErrors(response)

        # Add some more asserts if you like
