import os
import boto3


class FileUploadUtility:
    @staticmethod
    def save_file(uploaded_file, directory_path=None):
        if os.environ.get("DEBUG", "True") == "True":
            # Local saving logic
            if directory_path is None:
                directory_path = os.getcwd()

            local_file_path = os.path.join(directory_path, uploaded_file.name)
            with open(local_file_path, "wb+") as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            return local_file_path
        else:
            # S3 saving logic
            s3 = boto3.client("s3")
            bucket_name = "your-s3-bucket-name"

            s3.upload_fileobj(uploaded_file, bucket_name, uploaded_file.name)
            return f"s3://{bucket_name}/{uploaded_file.name}"
