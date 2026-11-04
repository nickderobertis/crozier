

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .text_field_format import TextFieldFormat
from .verbosity_enum import VerbosityEnum


class TextField(UniversalBaseModel):
    format: TextFieldFormat
    verbosity: typing.Optional[VerbosityEnum] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
