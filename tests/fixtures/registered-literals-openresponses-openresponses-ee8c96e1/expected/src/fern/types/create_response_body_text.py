

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_response_body_text_verbosity import CreateResponseBodyTextVerbosity
from .text_format_param import TextFormatParam


class CreateResponseBodyText(UniversalBaseModel):
    """
    Configuration options for text output.
    """

    format: typing.Optional[TextFormatParam] = pydantic.Field(default=None)
    """
    The format configuration for text output.
    """

    verbosity: typing.Optional[CreateResponseBodyTextVerbosity] = pydantic.Field(default=None)
    """
    Controls the level of detail in generated text output.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
