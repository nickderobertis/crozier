

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .team_membership_states import TeamMembershipStates
from .user_response import UserResponse


class TeamMemberResponse(UniversalBaseModel):
    user: UserResponse
    team_id: SnowflakeType
    membership_state: TeamMembershipStates

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
