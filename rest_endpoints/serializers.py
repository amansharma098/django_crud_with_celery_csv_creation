from rest_framework import serializers
from student_register.models import Student

class StudentSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    fullname = serializers.CharField()
    emp_code = serializers.CharField()
    mobile = serializers.CharField()

    course = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field='title'
        )

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__' 