

import typing

from .file_with_bytes import FileWithBytes
from .file_with_uri import FileWithUri

FilePartFile = typing.Union[FileWithBytes, FileWithUri]
