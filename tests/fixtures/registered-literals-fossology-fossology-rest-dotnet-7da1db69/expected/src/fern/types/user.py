

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .analysis import Analysis
from .user_access_level import UserAccessLevel


class User(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    ID of the user
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique username
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of the user
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email of the user, needs to be unique and is required
    """

    access_level: typing_extensions.Annotated[
        typing.Optional[UserAccessLevel], FieldMetadata(alias="accessLevel"), pydantic.Field(alias="accessLevel")
    ] = None
    root_folder_id: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="rootFolderId"),
        pydantic.Field(alias="rootFolderId", description="root folder id of the user"),
    ] = None
    """
    root folder id of the user
    """

    email_notification: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="emailNotification"),
        pydantic.Field(alias="emailNotification", description="enable email notification when upload scan completes"),
    ] = None
    """
    enable email notification when upload scan completes
    """

    default_group: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="defaultGroup"),
        pydantic.Field(alias="defaultGroup", description="Default group id of the user"),
    ] = None
    """
    Default group id of the user
    """

    agents: typing.Optional[Analysis] = None
    default_bucketpool: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="defaultBucketpool"),
        pydantic.Field(alias="defaultBucketpool", description="Default bucket pool id"),
    ] = None
    """
    Default bucket pool id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
