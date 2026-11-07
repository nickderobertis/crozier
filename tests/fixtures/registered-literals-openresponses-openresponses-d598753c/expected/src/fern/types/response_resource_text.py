

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_resource_text_format import ResponseResourceTextFormat
from .verbosity_enum import VerbosityEnum


class ResponseResourceText(UniversalBaseModel):
    """
    Configuration options for text output that were used.
    """

    format: ResponseResourceTextFormat
    verbosity: typing.Optional[VerbosityEnum] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
