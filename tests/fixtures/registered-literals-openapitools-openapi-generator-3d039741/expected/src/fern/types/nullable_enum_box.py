

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .nullable_enum_box_optional_enum import NullableEnumBoxOptionalEnum
from .nullable_enum_box_required_enum import NullableEnumBoxRequiredEnum


class NullableEnumBox(UniversalBaseModel):
    optional_enum: typing.Optional[NullableEnumBoxOptionalEnum] = None
    required_enum: typing.Optional[NullableEnumBoxRequiredEnum] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
