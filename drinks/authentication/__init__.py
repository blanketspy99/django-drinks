from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        # Implement your authentication logic here
        # Authenticate users using an external service (e.g., Azure AD)
        # Obtain user information like username or user ID

        # If authentication is successful, return a tuple (user, None)
        # If authentication fails, raise AuthenticationFailed exception

        # Example:
        jwt_token = request.META.get('HTTP_AUTHORIZATION')
        if jwt_token:
            return 'admin', None
        else:
            raise AuthenticationFailed('Authentication failed. Invalid token.')

        # For now, let's raise AuthenticationFailed for demonstration purposes
        # raise AuthenticationFailed('Authentication failed. Invalid token.')

    def authenticate_header(self, request):
        return 'Bearer'
