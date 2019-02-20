from rest_framework import serializers
from .models import Test, Student


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['test_name', 'points_for_test']


class StudSerializer(serializers.ModelSerializer):
    tests = TestSerializer(many=True, read_only=False)

    class Meta:
        model = Student
        fields = ['id', 'name', 'telegram_username', 'tests']
