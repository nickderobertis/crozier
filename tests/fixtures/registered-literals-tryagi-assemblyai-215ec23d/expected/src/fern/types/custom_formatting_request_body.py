

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .custom_formatting_request_body_custom_formatting import CustomFormattingRequestBodyCustomFormatting


class CustomFormattingRequestBody(UniversalBaseModel):
    """
    Request body for [Custom Formatting](https://www.assemblyai.com/docs/speech-understanding/custom-formatting).
    """

    custom_formatting: CustomFormattingRequestBodyCustomFormatting

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
