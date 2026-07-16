

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .custom_field_type_label import CustomFieldTypeLabel
from .custom_field_type_value import CustomFieldTypeValue


class CustomFieldType(UniversalBaseModel):
    label: CustomFieldTypeLabel
    value: CustomFieldTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
