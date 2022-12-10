from rest_framework.serializers import ModelSerializer, CharField
from .models import Employee


class EmployeeSerializer(ModelSerializer):

    password = CharField(write_only=True)

    def create(self, validated_data):

        user = Employee.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            password=validated_data["password"],
            email=validated_data["email"],
            phone=validated_data["phone"],
            mobile=validated_data["mobile"],
            user_team=validated_data["user_team"],
        )

        user.save()

        return user

    class Meta:
        model = Employee
        # Tuple of serialized model fields (see link [2])
        fields = [
            "id",
            "first_name",
            "last_name",
            "password",
            "email",
            "phone",
            "mobile",
            "user_team",
        ]
