

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class QuayRobotActionSetRepoPermission(UniversalBaseModel):
    """
    Action: Set or update a robot's repository permission.
    """

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
