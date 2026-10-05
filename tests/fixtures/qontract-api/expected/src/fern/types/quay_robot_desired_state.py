

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .quay_robot_repository import QuayRobotRepository


class QuayRobotDesiredState(UniversalBaseModel):
    """
    Desired state for a single Quay robot account.
    """

    delete: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If True, delete the robot when it exists in Quay
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Robot description
    """

    name: str = pydantic.Field()
    """
    Robot short name (without org+ prefix)
    """

    repositories: typing.Optional[typing.List[QuayRobotRepository]] = pydantic.Field(default=None)
    """
    Desired repository permissions for this robot
    """

    teams: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Teams the robot should belong to (managedTeams only)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
