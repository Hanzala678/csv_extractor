from django.urls import path
from .views_folder import UploadProcessAPIView, ExecutionHistoryAPIView
from processor.views import upload_page, history_page

urlpatterns = [
    path('', upload_page, name='upload'),
    path('history/', history_page, name='history'),
    
    #APIs
    path('api/process/', UploadProcessAPIView.as_view(), name='api-process'),
    path('api/history/', ExecutionHistoryAPIView.as_view(), name='api-history'),
]