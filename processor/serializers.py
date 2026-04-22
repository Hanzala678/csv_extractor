from rest_framework import serializers
from .models import Execution


class ExecutionSerializer(serializers.ModelSerializer):
    input_file_url = serializers.SerializerMethodField()
    output_file_url = serializers.SerializerMethodField()

    class Meta:
        model = Execution
        fields = [
            'id',
            'status',
            'rows_input',
            'rows_output',
            'created_at',
            'input_file_url',
            'output_file_url'
        ]

    def get_input_file_url(self, obj):
        return obj.input_file.url if obj.input_file else None

    def get_output_file_url(self, obj):
        return obj.output_file.url if obj.output_file else None