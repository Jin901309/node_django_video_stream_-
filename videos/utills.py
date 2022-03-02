import os
from . import models

from django.core.files.utils import FileProxyMixin


class RemoveAfterCloseFileProxy(FileProxyMixin):
    def __init__(self, file):
        self.file = file
        self.name = file.name

    def close(self):
        if not self.closed:
            self.file.close()
            try:
                os.remove(self.name)
            except FileNotFoundError:
                pass

    def __del__(self):
        self.close()