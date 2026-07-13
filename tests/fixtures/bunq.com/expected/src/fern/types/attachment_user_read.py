

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attachment import Attachment


class AttachmentUserRead(UniversalBaseModel):
    attachment: typing.Optional[Attachment] = pydantic.Field(default=None)
    """
    The attachment.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the attachment's creation.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the attachment.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the attachment's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
