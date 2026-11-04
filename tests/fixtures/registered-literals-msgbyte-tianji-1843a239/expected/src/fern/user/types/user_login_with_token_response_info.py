

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .user_login_with_token_response_info_workspaces_item import UserLoginWithTokenResponseInfoWorkspacesItem


class UserLoginWithTokenResponseInfo(UniversalBaseModel):
    id: str
    role: str
    username: str
    nickname: typing.Optional[str] = None
    avatar: typing.Optional[str] = None
    email: typing.Optional[str] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    deleted_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="deletedAt"), pydantic.Field(alias="deletedAt")
    ] = None
    current_workspace_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="currentWorkspaceId"), pydantic.Field(alias="currentWorkspaceId")
    ] = None
    workspaces: typing.List[UserLoginWithTokenResponseInfoWorkspacesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
