
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import json
from django.contrib.auth import get_user_model
from core.apps.custom_user.forms import UserCreationForm
from core.apps.custom_user.forms import AccountSettingForm, PasswordChangeForm
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

# Login Views

User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

        # Check if the user's email is verified
        if not user.is_verified:
            raise AuthenticationFailed(
                'Email is not verified. <a href="/verify/?send_email=True">Verify Email</a>')

        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    data = json.loads(request.body)
    form = UserCreationForm(data)
    if form.is_valid():
        user = form.save(commit=False)
        user.generate_verification_code()
        user.save()


        data = {
            'type': 'success',
            'email': user.email,
            'message': 'Registration Successful.'
        }
        status = 200
    else:
        errors = eval(form.errors.as_json())

        data = {
            'type': 'error',
            'message': 'Registration Failed.',
            'errors': errors
        }
        status = 400
    return Response(status=status, data=data)





@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_account_password(request):
    form = PasswordChangeForm(request.user, request.data)

    if form.is_valid():
        form.save()
        return Response({'message': 'Password updated successfully'}, status=200)
    else:
        return Response(form.errors, status=400)




@api_view(['POST'])
@permission_classes([AllowAny])
def verify_email(request):
    data = json.loads(request.body)
    email = data.get('email')
    verification_code = data.get('otp')

    try:
        user = User.objects.get(email=email)
        if user.verification_code == verification_code:
            user.is_verified = True
            user.save()

            # Generate token
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            # Add custom claims
            token['email'] = user.email
            token['first_name'] = user.first_name
            token['last_name'] = user.last_name

            return Response({'message': 'Email verified successfully', 'token': token}, status=200)
        else:
            return Response({'message': 'Invalid verification code'}, status=400)
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=404)


@api_view(['POST'])
def send_verify_email(request):
    data = json.loads(request.body)
    email = data.get('email')
    user = User.objects.get(email=email)
    user.generate_verification_code()
    user.save()
    return Response({'message': 'Verification code sent successfully'}, status=200)
