from marshmallow import fields, post_load, ValidationError

from config import Config

from utils.file_manager import FileManager

from schemas.ma import ma


class ProductsFileSchema(ma.Schema):
    file_name = fields.String()

    @post_load
    def post_load_processing(self, data, **kwargs):
        file_name = data['file_name']

        file_extension = FileManager.get_file_extension(file_name)
        if not file_extension in Config.ALLOWED_FILE_EXTENSIONS:
            raise ValidationError('Only csv/xlsx files are accepted')

        return data
