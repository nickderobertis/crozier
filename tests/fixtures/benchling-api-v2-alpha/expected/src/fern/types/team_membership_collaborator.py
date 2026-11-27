

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .team_membership_collaborator_role import TeamMembershipCollaboratorRole
from .team_membership_collaborator_type import TeamMembershipCollaboratorType
from .team_summary import TeamSummary


class TeamMembershipCollaborator(UniversalBaseModel):
    role: typing.Optional[TeamMembershipCollaboratorRole] = None
    team: typing.Optional[TeamSummary] = None
    type: typing.Optional[TeamMembershipCollaboratorType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
