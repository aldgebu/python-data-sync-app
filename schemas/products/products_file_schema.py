from marshmallow import fields, post_load, ValidationError

from schemas.ma import ma


class ProductsFileSchema(ma.Schema):
    file_name = fields.String()

    @post_load
    def post_load_processing(self, data, **kwargs):
        file_name = data['file_name']
        if not (file_name.endswith(".csv") or file_name.endswith('xlsx')):
            raise ValidationError('Only csv/xlsx files are accepted')

        return data
