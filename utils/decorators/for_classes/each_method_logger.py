def decorate_each_method_with(method_decorator):
    def class_decorator(cls):
        for attr_name, attr_value in cls.__dict__.items():
            if callable(attr_value) and not attr_name.startswith('_'):
                setattr(cls, attr_name, method_decorator(attr_value))

        return cls
    return class_decorator
