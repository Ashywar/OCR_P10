from rest_framework.views import APIView
from rest_framework import generics
from .serializers import RegisterSerializer, UpdateSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from datetime import date

from .models import UserData


def verify_age(data):
    """
    Verify age-related data and deny access if the user is under 15.
    """
    # Get the 'birthdate' from the data if it exists
    birthdate = data.get("birthdate")

    if birthdate:
        try:
            birthdate = date.fromisoformat(birthdate)
        except ValueError:
            # Handle the case where the birthdate is incorrectly formatted
            # You may want to log a warning or raise an exception based on your needs
            raise ValidationError({"birthdate": ["Invalid date format."]})

        today = date.today()
        age = (
            today.year
            - birthdate.year
            - ((today.month, today.day) < (birthdate.month, birthdate.day))
        )

        # Deny access if the user is under 15
        if age < 15:
            raise ValidationError(
                {"birthdate": ["Users under 15 are not allowed to create an account."]}
            )

        # Update the fields based on age
        data["can_be_contacted"] = False
        data["can_data_be_shared"] = False

    return data


# View for registering users
class RegisterView(APIView):
    def post(self, request):
        # Verify age-related data before user registration
        data = verify_age(request.data)

        # Serialize and save user data
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


# View for listing and updating user data
class ManageView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = UserData.objects.all()
    serializer_class = UpdateSerializer

    def get_object(self):
        # Retrieve the authenticated user
        return self.request.user

    def put(self, request):
        # Verify age-related data before updating user data
        data = verify_age(request.data)
        return super().put(request, data=data)
