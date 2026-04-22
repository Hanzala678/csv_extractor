import os
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import UploadForm
from .models import Execution
from .services import process_csv


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            execution = Execution.objects.create(
                input_file=form.cleaned_data['file'],
                status='PROCESSING'
            )

            input_path = execution.input_file.path
            output_path = os.path.join(settings.MEDIA_ROOT, f"outputs/output_{execution.id}.csv")

            try:
                rows_in, rows_out = process_csv(input_path, output_path)

                execution.output_file.name = f"outputs/output_{execution.id}.csv"
                execution.rows_input = rows_in
                execution.rows_output = rows_out
                execution.status = 'SUCCESS'
            except Exception as e:
                execution.status = f"FAILED: {str(e)}"

            execution.save()
            return redirect('history')
    else:
        form = UploadForm()

    return render(request, 'processor/upload.html', {'form': form})


def history(request):
    executions = Execution.objects.all().order_by('-created_at')
    return render(request, 'processor/history.html', {'executions': executions})
