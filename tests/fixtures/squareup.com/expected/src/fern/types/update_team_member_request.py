

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .team_member import TeamMember


class UpdateTeamMemberRequest(UniversalBaseModel):
    """
    Represents an update request for a `TeamMember` object.
    """

    team_member: typing.Optional[TeamMember] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
