from django.shortcuts import render
import pandas as pd
from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadedFile
from .utils import process_file

# Create your views here.


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save()
            context = process_file(uploaded_file.file.path)
            return render(request, 'analysis/results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'analysis/upload.html', {'form': form})
