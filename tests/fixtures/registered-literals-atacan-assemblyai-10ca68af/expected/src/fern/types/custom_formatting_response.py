

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .custom_formatting_response_custom_formatting import CustomFormattingResponseCustomFormatting


class CustomFormattingResponse(UniversalBaseModel):
    custom_formatting: typing.Optional[CustomFormattingResponseCustomFormatting] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
