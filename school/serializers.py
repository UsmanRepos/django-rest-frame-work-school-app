import re
from rest_framework import serializers
from .models import Student, Courses, Teacher


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

    def validate_name(self, value):
        pattern = r'^[a-zA-Z ]+$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("Name should only contain letters")

        if len(value) < 5:
            raise serializers.ValidationError("Name should have at least 5 characters")

        return value
    
    def validate_duaration(self, value):
        if value < 0:
            raise serializers.ValidationError("Duration should be a positive integer")
        return value

class StudentSerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'

    def validate_first_name(self, value):
        pattern = r'^[a-zA-Z]+$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("First Name should only contain letters")

        if len(value) < 3:
            raise serializers.ValidationError("First name should have at least 5 characters")
        return value

    def validate_last_name(self, value):
        pattern = r'^[a-zA-Z]+$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("Last Name should only contain letters")

        if len(value) < 3:
            raise serializers.ValidationError("Last name should have at least 5 characters")
        return value

    def validate_email(self, value):
        if Student.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value):
            raise serializers.ValidationError("Email is not in correct format.")
        return value

    def validate_major(self, value):
        # Check that the major is not empty
        if not value:
            raise serializers.ValidationError({'major': 'This field may not be blank.'})
        return value

    def validate_cgpa(self, value):
        if value < 0 or value > 4:
            raise serializers.ValidationError("CGPA should be between 0 and 4")
        return value

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

    def validate_experience(self, value):
        if value < 0:
            raise serializers.ValidationError("Experience should be a positive integer")
        return value
