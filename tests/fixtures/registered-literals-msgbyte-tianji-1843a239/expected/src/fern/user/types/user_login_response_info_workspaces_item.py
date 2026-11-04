

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_login_response_info_workspaces_item_workspace import UserLoginResponseInfoWorkspacesItemWorkspace


class UserLoginResponseInfoWorkspacesItem(UniversalBaseModel):
    role: str
    workspace: UserLoginResponseInfoWorkspacesItemWorkspace

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
