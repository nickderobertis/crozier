

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .team_member_response import TeamMemberResponse


class TeamResponse(UniversalBaseModel):
    id: SnowflakeType
    icon: typing.Optional[str] = None
    name: str
    owner_user_id: SnowflakeType
    members: typing.List[TeamMemberResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
