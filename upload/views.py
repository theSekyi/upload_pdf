from django.shortcuts import render
from django.http import JsonResponse
from .models import PDFUpload
from django.views import View
from .file_upload import FileUploadUtility


class PDFUploadView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "upload.html")

    def post(self, request, *args, **kwargs):
        uploaded_file = request.FILES["pdf_file"]
        file_size = uploaded_file.size

        file_path = FileUploadUtility.save_file(uploaded_file)

        new_pdf = PDFUpload(
            file_name=uploaded_file.name,
            file_path=file_path,
            size=file_size,
        )
        new_pdf.save()

        return JsonResponse({"status": "success"})
