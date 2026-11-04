

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workspace_switch_response_workspaces_item_workspace import WorkspaceSwitchResponseWorkspacesItemWorkspace


class WorkspaceSwitchResponseWorkspacesItem(UniversalBaseModel):
    role: str
    workspace: WorkspaceSwitchResponseWorkspacesItemWorkspace

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
