from rest_framework.decorators import api_view
from rest_framework.response import Response
from students.models import Student
from .serializers import StudentSerializer


@api_view(['GET'])
def get_all_students(request):
    students = Student.objects.all()
    response_data = StudentSerializer(students, many=True).data
    return Response(response_data)


@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
