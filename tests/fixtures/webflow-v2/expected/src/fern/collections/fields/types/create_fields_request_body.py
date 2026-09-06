

import typing

from .option_field import OptionField
from .reference_field import ReferenceField
from .static_field import StaticField

CreateFieldsRequestBody = typing.Union[StaticField, OptionField, ReferenceField]
