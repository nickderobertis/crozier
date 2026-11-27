

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .person import Person
from .robot_holder_type import RobotHolderType


class RobotHolder(Person):
    type: typing.Optional[RobotHolderType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
