

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessageAttachment(UniversalBaseModel):
    filename: str = pydantic.Field()
    """
    Original filename of the attachment
    """

    content: str = pydantic.Field()
    """
    Base64 encoded attachment content
    """

    content_type: str = pydantic.Field()
    """
    MIME content type of the attachment
    """

    content_id: str = pydantic.Field()
    """
    Content-ID for inline attachments
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
