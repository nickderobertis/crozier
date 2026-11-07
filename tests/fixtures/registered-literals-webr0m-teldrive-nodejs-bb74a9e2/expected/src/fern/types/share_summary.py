

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .share_permission import SharePermission
from .uri import Uri
from .uuid_ import Uuid


class ShareSummary(UniversalBaseModel):
    id: Uuid
    file_id: typing_extensions.Annotated[Uuid, FieldMetadata(alias="fileId"), pydantic.Field(alias="fileId")]
    public_url: typing_extensions.Annotated[
        Uri,
        FieldMetadata(alias="publicUrl"),
        pydantic.Field(
            alias="publicUrl", description="Reusable public URL, available only to the authenticated owner."
        ),
    ]
    """
    Reusable public URL, available only to the authenticated owner.
    """

    password_protected: typing_extensions.Annotated[
        bool, FieldMetadata(alias="passwordProtected"), pydantic.Field(alias="passwordProtected")
    ]
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None
    max_downloads: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="maxDownloads"), pydantic.Field(alias="maxDownloads")
    ] = None
    download_count: typing_extensions.Annotated[
        int, FieldMetadata(alias="downloadCount"), pydantic.Field(alias="downloadCount")
    ]
    permission: SharePermission
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    revoked_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="revokedAt"), pydantic.Field(alias="revokedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
