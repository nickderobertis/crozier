

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .form_field_value_reference_type import FormFieldValueReferenceType


class FormFieldValueReference(UniversalBaseModel):
    key: typing.Optional[str] = None
    type: typing.Optional[FormFieldValueReferenceType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
