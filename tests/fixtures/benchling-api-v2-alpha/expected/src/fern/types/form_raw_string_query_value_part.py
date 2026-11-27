

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .form_raw_string_query_value_part_type import FormRawStringQueryValuePartType


class FormRawStringQueryValuePart(UniversalBaseModel):
    type: typing.Optional[FormRawStringQueryValuePartType] = None
    value: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
