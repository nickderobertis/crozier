

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .driving_behavior_base_mode import DrivingBehaviorBaseMode


class DrivingBehaviorBase(UniversalBaseModel):
    mode: typing.Optional[DrivingBehaviorBaseMode] = pydantic.Field(default=None)
    """
    Driving mode by driver selection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
