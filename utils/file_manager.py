import pandas
from werkzeug.datastructures import FileStorage


class FileManager:
    @classmethod
    def get_rows(cls, file: FileStorage):
        file_name = file.filename
        file.stream.seek(0)

        if file_name.endswith(".csv"):
            df = pandas.read_csv(file.stream)
        elif file_name.endswith(".xlsx"):
            df = pandas.read_excel(file.stream)
        else:
            raise ValueError("Unsupported file format")

        for _, row in df.iterrows():
            yield row.to_dict()
