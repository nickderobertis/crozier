

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attachment_url import AttachmentUrl


class Attachment(UniversalBaseModel):
    content_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The content type of the attachment's file.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the attachment.
    """

    urls: typing.Optional[typing.List[AttachmentUrl]] = pydantic.Field(default=None)
    """
    The URLs where the file can be downloaded.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
