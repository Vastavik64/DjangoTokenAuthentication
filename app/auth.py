from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        '''
        This function generates a token. It takes a request and a serializer, collects the data and checks for validation, if it is valid then generates a token associated with the object
        '''
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({                           #Email, token and id are returned as response
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })