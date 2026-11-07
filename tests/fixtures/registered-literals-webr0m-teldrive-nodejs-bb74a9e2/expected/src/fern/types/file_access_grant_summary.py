

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .share_permission import SharePermission
from .uuid_ import Uuid


class FileAccessGrantSummary(UniversalBaseModel):
    id: Uuid
    file_id: typing_extensions.Annotated[Uuid, FieldMetadata(alias="fileId"), pydantic.Field(alias="fileId")]
    owner_id: typing_extensions.Annotated[int, FieldMetadata(alias="ownerId"), pydantic.Field(alias="ownerId")]
    grantee_user_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="granteeUserId"), pydantic.Field(alias="granteeUserId")
    ]
    grantee_display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="granteeDisplayName"), pydantic.Field(alias="granteeDisplayName")
    ] = None
    grantee_username: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="granteeUsername"), pydantic.Field(alias="granteeUsername")
    ] = None
    permission: SharePermission
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
