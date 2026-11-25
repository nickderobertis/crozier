

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .walking_task_all_of_action import WalkingTaskAllOfAction


class WalkingTaskAllOf(UniversalBaseModel):
    action: typing.Optional[WalkingTaskAllOfAction] = pydantic.Field(default=None)
    """
    Walk a pet.
    """

    distance: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
