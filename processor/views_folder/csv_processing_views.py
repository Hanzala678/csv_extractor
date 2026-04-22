import os
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..models import Execution
from ..services import process_csv
from ..serializers import ExecutionSerializer

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import AllowAny

# =========================
# Upload + Process API
# =========================
@method_decorator(csrf_exempt, name='dispatch')
class UploadProcessAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def post(self, request):
        """Takes cvs as input, performs processing and returns execution details with output file link.

        Args:
            request (Request): HTTP request containing the uploaded file.

        Returns:
            Response: Execution details with output file link.
        """
        
        file = request.FILES.get('file')

        if not file:
            return Response(
                {"error": "No file uploaded"},
                status=status.HTTP_400_BAD_REQUEST
            )

        execution = Execution.objects.create(
            input_file=file,
            status='PROCESSING'
        )

        input_path = execution.input_file.path
        output_path = os.path.join(
            settings.MEDIA_ROOT,
            f"outputs/output_{execution.id}.csv"
        )

        try:
            rows_in, rows_out = process_csv(input_path, output_path)

            execution.output_file.name = f"outputs/output_{execution.id}.csv"
            execution.rows_input = rows_in
            execution.rows_output = rows_out
            execution.status = 'SUCCESS'

        except Exception as e:
            execution.status = f"FAILED: {str(e)}"

        execution.save()

        return Response(
            ExecutionSerializer(execution).data,
            status=status.HTTP_200_OK
        )
