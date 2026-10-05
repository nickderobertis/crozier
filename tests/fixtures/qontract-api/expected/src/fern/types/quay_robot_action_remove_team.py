

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QuayRobotActionRemoveTeam(UniversalBaseModel):
    """
    Action: Remove a robot from a team.
    """

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
