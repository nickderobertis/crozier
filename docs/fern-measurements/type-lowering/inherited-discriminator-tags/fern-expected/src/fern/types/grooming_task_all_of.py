

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .grooming_task_all_of_action import GroomingTaskAllOfAction


class GroomingTaskAllOf(UniversalBaseModel):
    action: typing.Optional[GroomingTaskAllOfAction] = pydantic.Field(default=None)
    """
    Groom a pet.
    """

    brush: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
