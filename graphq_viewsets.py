import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django_cognito_jwt import JSONWebTokenAuthentication
from graphene_django.views import GraphQLView
from rest_framework import exceptions
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass


class JWTGraphQLView(JSONWebTokenAuthentication, GraphQLView):

    def dispatch(self, request, *args, **kwargs):
        try:
            # if not already authenticated by django cookie sessions
            # check the JWT token by re-using our DRF JWT
            if not request.user.is_authenticated():
                request.user, request.token = self.authenticate(request)
        except exceptions.AuthenticationFailed as e:
            response = HttpResponse(
                json.dumps({
                    'errors': [str(e)]
                }),
                status=401,
                content_type='application/json'
            )
            return response
        return super().dispatch(request, *args, **kwargs)


class AuthenticatedGraphQLView(GraphQLView):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def authenticate_request(self, request):
        for auth_class in self.authentication_classes:
            auth_tuple = auth_class().authenticate(request)
            if auth_tuple:
                request.user, request.token = auth_tuple
                break

    def check_permissions(self, request):
        for permission_class in self.permission_classes:
            if not permission_class().has_permission(request, self):
                return False
        return True

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        try:
            self.authenticate_request(request)
            has_permission = self.check_permissions(request)
            if not has_permission:
                return HttpResponse(
                    json.dumps({'errors': ['permission denied']}),
                    status=status.HTTP_403_FORBIDDEN,
                    content_type='application/json')
        except AuthenticationFailed as auth_failed_error:
            return HttpResponse(
                json.dumps({
                    'errors': [str(auth_failed_error)]
                }),
                status=status.HTTP_401_UNAUTHORIZED,
                content_type='application/json')
        return super().dispatch(request, *args, **kwargs)
