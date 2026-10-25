

import typing

from .field_template import FieldTemplate
from .templates_item_name import TemplatesItemName

TemplatesItem = typing.Union[FieldTemplate, TemplatesItemName]
