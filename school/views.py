from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import StudentSerializer, CoursesSerializer
from .models import Student, Courses


class StudentViewSet(ModelViewSet):
    serializer_class=StudentSerializer
    queryset=Student.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data
        student = Student.objects.create(
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],  
            major=data['major'], 
            cgpa=data['cgpa'], 
        )
        student.save()
        courses = data.pop('courses')
        for course_id in courses:
            course = Courses.objects.get(pk=course_id)
            student.courses.add(course)

        student_serializer = self.get_serializer(student)
        return Response(student_serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        data = request.data
        courses = data.pop('courses')
        student = self.get_object()

        student.first_name = data['first_name']
        student.last_name = data['last_name']
        student.email = data['email']
        student.major = data['major']
        student.cgpa = data['cgpa']
        
        student.courses.clear()   
        for course_id in courses:
            course = Courses.objects.get(pk=course_id)
            student.courses.add(course)
        student.save()

        student_serializer = self.get_serializer(student)
        return Response(student_serializer.data, status=status.HTTP_200_OK)

    def partial_update(self, request, *args, **kwargs):
        data = request.data
        student = self.get_object()

        student.first_name = data.get('first_name', student.first_name)
        student.last_name = data.get('last_name', student.last_name)
        student.email = data.get('email', student.email)
        student.major = data.get('major', student.major)
        student.cgpa = data.get('cgpa', student.cgpa)
        
        try:
            courses = data['courses']
            student.courses.clear()   
            for course_id in courses:
                course = Courses.objects.get(pk=course_id)
                student.courses.add(course)
        except KeyError:
            pass
        student.save()

        student_serializer = self.get_serializer(student)
        return Response(student_serializer.data, status=status.HTTP_200_OK)


class CoursesViewSet(ModelViewSet):
    serializer_class=CoursesSerializer
    queryset=Courses.objects.all()