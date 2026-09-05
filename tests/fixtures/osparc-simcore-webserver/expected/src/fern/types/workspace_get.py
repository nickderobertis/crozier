

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_rights import AccessRights
from .group_id_int import GroupIdInt


class WorkspaceGet(UniversalBaseModel):
    workspace_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    name: str
    description: typing.Optional[str] = None
    thumbnail: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    modified_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="modifiedAt"), pydantic.Field(alias="modifiedAt")
    ]
    trashed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="trashedAt"), pydantic.Field(alias="trashedAt")
    ] = None
    trashed_by: typing_extensions.Annotated[
        typing.Optional[GroupIdInt],
        FieldMetadata(alias="trashedBy"),
        pydantic.Field(alias="trashedBy", description="The primary gid of the user who trashed"),
    ] = None
    """
    The primary gid of the user who trashed
    """

    my_access_rights: typing_extensions.Annotated[
        AccessRights, FieldMetadata(alias="myAccessRights"), pydantic.Field(alias="myAccessRights")
    ]
    access_rights: typing_extensions.Annotated[
        typing.Dict[str, AccessRights], FieldMetadata(alias="accessRights"), pydantic.Field(alias="accessRights")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
