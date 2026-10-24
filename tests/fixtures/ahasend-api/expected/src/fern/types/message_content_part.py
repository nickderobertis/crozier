

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessageContentPart(UniversalBaseModel):
    content_type: str = pydantic.Field()
    """
    MIME content type (e.g., "text/plain", "text/html")
    """

    content: str = pydantic.Field()
    """
    The actual content for this part
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
