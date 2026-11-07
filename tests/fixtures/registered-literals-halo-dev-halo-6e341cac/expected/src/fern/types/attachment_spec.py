

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AttachmentSpec(UniversalBaseModel):
    """
    Desired attachment metadata and storage placement.
    """

    display_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="displayName"),
        pydantic.Field(alias="displayName", description="Display name shown for the attachment."),
    ] = None
    """
    Display name shown for the attachment.
    """

    group_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="groupName"),
        pydantic.Field(alias="groupName", description="Attachment group metadata.name this attachment belongs to."),
    ] = None
    """
    Attachment group metadata.name this attachment belongs to.
    """

    media_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="mediaType"),
        pydantic.Field(
            alias="mediaType", description="Media type detected or supplied for the attachment, such as image/png."
        ),
    ] = None
    """
    Media type detected or supplied for the attachment, such as image/png.
    """

    owner_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ownerName"),
        pydantic.Field(alias="ownerName", description="User metadata.name of the uploader."),
    ] = None
    """
    User metadata.name of the uploader.
    """

    policy_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="policyName"),
        pydantic.Field(alias="policyName", description="Storage policy metadata.name used to store this attachment."),
    ] = None
    """
    Storage policy metadata.name used to store this attachment.
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size of the attachment in bytes.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Free-form tags assigned to the attachment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
