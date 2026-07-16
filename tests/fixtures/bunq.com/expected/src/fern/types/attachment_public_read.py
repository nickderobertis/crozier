

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .attachment import Attachment


class AttachmentPublicRead(UniversalBaseModel):
    attachment: typing.Optional[Attachment] = pydantic.Field(default=None)
    """
    The attachment.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the attachment's creation.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the attachment's last update.
    """

    uuid_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="The UUID of the attachment."),
    ] = None
    """
    The UUID of the attachment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
