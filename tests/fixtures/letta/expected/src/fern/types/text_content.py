

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TextContent(UniversalBaseModel):
    text: str = pydantic.Field()
    """
    The text content of the message.
    """

    signature: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stores a unique identifier for any reasoning associated with this text content.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
