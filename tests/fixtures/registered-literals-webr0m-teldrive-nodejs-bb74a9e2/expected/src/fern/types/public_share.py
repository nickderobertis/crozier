

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .file_entry import FileEntry
from .share_permission import SharePermission
from .uuid_ import Uuid


class PublicShare(UniversalBaseModel):
    id: Uuid
    file: FileEntry
    password_protected: typing_extensions.Annotated[
        bool, FieldMetadata(alias="passwordProtected"), pydantic.Field(alias="passwordProtected")
    ]
    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ] = None
    permission: SharePermission

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
