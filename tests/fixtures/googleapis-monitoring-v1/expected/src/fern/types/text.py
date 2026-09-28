

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .text_format import TextFormat
from .text_style import TextStyle


class Text(UniversalBaseModel):
    """
    A widget that displays textual content.
    """

    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text content to be displayed.
    """

    format: typing.Optional[TextFormat] = pydantic.Field(default=None)
    """
    How the text content is formatted.
    """

    style: typing.Optional[TextStyle] = pydantic.Field(default=None)
    """
    How the text is styled
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
