
import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Execution
from ..serializers import ExecutionSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# =========================
# Execution History API
# =========================
@method_decorator(csrf_exempt, name='dispatch')
class ExecutionHistoryAPIView(APIView):
    
    def get(self, request):
        """Returns executions history sorted by creation date (newest first).

        Args:
            request (Request): HTTP request.

        Returns:
            Response: List of execution details.
        """
        
        executions = Execution.objects.all().order_by('-created_at')
        serializer = ExecutionSerializer(executions, many=True)
        return Response(serializer.data)