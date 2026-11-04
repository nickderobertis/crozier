

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .response_format_text_type import ResponseFormatTextType


class ResponseFormatText(UniversalBaseModel):
    """
    Default response format. Used to generate text responses.
    """

    type: ResponseFormatTextType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
