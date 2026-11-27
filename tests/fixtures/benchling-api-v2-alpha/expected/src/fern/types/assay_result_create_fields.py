

import typing

from .assay_fields_create import AssayFieldsCreate
from .fields import Fields

AssayResultCreateFields = typing.Union[Fields, AssayFieldsCreate]
