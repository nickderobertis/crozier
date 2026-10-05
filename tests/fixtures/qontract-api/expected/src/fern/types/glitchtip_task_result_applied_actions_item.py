

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GlitchtipTaskResultAppliedActionsItem_AddProjectToTeam(UniversalBaseModel):
    action_type: typing.Literal["add_project_to_team"] = "add_project_to_team"
    instance: str
    organization: str
    project_slug: str
    team_slug: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_AddUserToTeam(UniversalBaseModel):
    action_type: typing.Literal["add_user_to_team"] = "add_user_to_team"
    email: str
    instance: str
    organization: str
    pk: typing.Optional[int] = None
    team_slug: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_CreateOrganization(UniversalBaseModel):
    action_type: typing.Literal["create_organization"] = "create_organization"
    instance: str
    organization: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_CreateProject(UniversalBaseModel):
    action_type: typing.Literal["create_project"] = "create_project"
    event_throttle_rate: typing.Optional[int] = None
    instance: str
    organization: str
    platform: typing.Optional[str] = None
    project_name: str
    teams: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_CreateTeam(UniversalBaseModel):
    action_type: typing.Literal["create_team"] = "create_team"
    instance: str
    organization: str
    team_slug: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_DeleteOrganization(UniversalBaseModel):
    action_type: typing.Literal["delete_organization"] = "delete_organization"
    instance: str
    organization: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_DeleteProject(UniversalBaseModel):
    action_type: typing.Literal["delete_project"] = "delete_project"
    instance: str
    organization: str
    project_slug: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_DeleteTeam(UniversalBaseModel):
    action_type: typing.Literal["delete_team"] = "delete_team"
    instance: str
    organization: str
    team_slug: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_DeleteUser(UniversalBaseModel):
    action_type: typing.Literal["delete_user"] = "delete_user"
    email: str
    instance: str
    organization: str
    pk: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_InviteUser(UniversalBaseModel):
    action_type: typing.Literal["invite_user"] = "invite_user"
    email: str
    instance: str
    organization: str
    role: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_RemoveProjectFromTeam(UniversalBaseModel):
    action_type: typing.Literal["remove_project_from_team"] = "remove_project_from_team"
    instance: str
    organization: str
    project_slug: str
    team_slug: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_RemoveUserFromTeam(UniversalBaseModel):
    action_type: typing.Literal["remove_user_from_team"] = "remove_user_from_team"
    email: str
    instance: str
    organization: str
    pk: int
    team_slug: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_UpdateProject(UniversalBaseModel):
    action_type: typing.Literal["update_project"] = "update_project"
    event_throttle_rate: typing.Optional[int] = None
    instance: str
    name: str
    organization: str
    platform: typing.Optional[str] = None
    project_slug: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GlitchtipTaskResultAppliedActionsItem_UpdateUserRole(UniversalBaseModel):
    action_type: typing.Literal["update_user_role"] = "update_user_role"
    email: str
    instance: str
    organization: str
    pk: int
    role: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GlitchtipTaskResultAppliedActionsItem = typing_extensions.Annotated[
    typing.Union[
        GlitchtipTaskResultAppliedActionsItem_AddProjectToTeam,
        GlitchtipTaskResultAppliedActionsItem_AddUserToTeam,
        GlitchtipTaskResultAppliedActionsItem_CreateOrganization,
        GlitchtipTaskResultAppliedActionsItem_CreateProject,
        GlitchtipTaskResultAppliedActionsItem_CreateTeam,
        GlitchtipTaskResultAppliedActionsItem_DeleteOrganization,
        GlitchtipTaskResultAppliedActionsItem_DeleteProject,
        GlitchtipTaskResultAppliedActionsItem_DeleteTeam,
        GlitchtipTaskResultAppliedActionsItem_DeleteUser,
        GlitchtipTaskResultAppliedActionsItem_InviteUser,
        GlitchtipTaskResultAppliedActionsItem_RemoveProjectFromTeam,
        GlitchtipTaskResultAppliedActionsItem_RemoveUserFromTeam,
        GlitchtipTaskResultAppliedActionsItem_UpdateProject,
        GlitchtipTaskResultAppliedActionsItem_UpdateUserRole,
    ],
    pydantic.Field(discriminator="action_type"),
]
