import re
import pandas
from werkzeug.datastructures import FileStorage


class FileManager:
    @classmethod
    def get_file_extension(cls, file_name: str) -> str:
        match = re.search(r'\.([^.]+)$', file_name)
        return match.group(1) if match else ''

    @classmethod
    def get_rows(cls, file: FileStorage):
        file_name = file.filename
        file.stream.seek(0)

        if file_name.endswith(".csv"):
            df = pandas.read_csv(file.stream)
        elif file_name.endswith(".xlsx"):
            df = pandas.read_excel(file.stream) # Better to FileReader classes for csv and xlsx
        else:
            raise ValueError("Unsupported file format")

        for _, row in df.iterrows():
            yield row.to_dict()
