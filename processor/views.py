from django.shortcuts import render

def upload_page(request):
    return render(request, 'processor/upload.html')

def history_page(request):
    return render(request, 'processor/history.html')