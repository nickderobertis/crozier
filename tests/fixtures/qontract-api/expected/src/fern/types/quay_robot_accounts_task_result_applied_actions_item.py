

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QuayRobotAccountsTaskResultAppliedActionsItem_AddTeam(UniversalBaseModel):
    action_type: typing.Literal["add_team"] = "add_team"
    instance_name: str
    org_name: str
    robot_name: str
    team: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class QuayRobotAccountsTaskResultAppliedActionsItem_Create(UniversalBaseModel):
    action_type: typing.Literal["create"] = "create"
    description: typing.Optional[str] = None
    instance_name: str
    org_name: str
    robot_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class QuayRobotAccountsTaskResultAppliedActionsItem_Delete(UniversalBaseModel):
    action_type: typing.Literal["delete"] = "delete"
    instance_name: str
    org_name: str
    robot_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class QuayRobotAccountsTaskResultAppliedActionsItem_RemoveRepoPermission(UniversalBaseModel):
    action_type: typing.Literal["remove_repo_permission"] = "remove_repo_permission"
    instance_name: str
    org_name: str
    repo: str
    robot_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class QuayRobotAccountsTaskResultAppliedActionsItem_RemoveTeam(UniversalBaseModel):
    action_type: typing.Literal["remove_team"] = "remove_team"
    instance_name: str
    org_name: str
    robot_name: str
    team: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class QuayRobotAccountsTaskResultAppliedActionsItem_SetRepoPermission(UniversalBaseModel):
    action_type: typing.Literal["set_repo_permission"] = "set_repo_permission"
    instance_name: str
    org_name: str
    permission: str
    repo: str
    robot_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


QuayRobotAccountsTaskResultAppliedActionsItem = typing_extensions.Annotated[
    typing.Union[
        QuayRobotAccountsTaskResultAppliedActionsItem_AddTeam,
        QuayRobotAccountsTaskResultAppliedActionsItem_Create,
        QuayRobotAccountsTaskResultAppliedActionsItem_Delete,
        QuayRobotAccountsTaskResultAppliedActionsItem_RemoveRepoPermission,
        QuayRobotAccountsTaskResultAppliedActionsItem_RemoveTeam,
        QuayRobotAccountsTaskResultAppliedActionsItem_SetRepoPermission,
    ],
    pydantic.Field(discriminator="action_type"),
]
