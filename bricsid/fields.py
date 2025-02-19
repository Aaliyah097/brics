from django.db import models
import ulid

class ULIDField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 26
        kwargs['default'] = self.generate_ulid
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)

    def generate_ulid(self):
        return str(ulid.new())
