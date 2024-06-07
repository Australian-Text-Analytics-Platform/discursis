import io

import pandas as pd
from ipywidgets import FileUpload


def read_uploaded_file(uploader: FileUpload):
    if not len(uploader.value) == 1:
        print("This example code only works for a single uploaded file")
    file_info = uploader.value[0]
    print("Reading data...")
    data = pd.read_excel(io.BytesIO(file_info["content"]))
    return data