

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .turn_state_running_status import TurnStateRunningStatus


class TurnStateRunning(UniversalBaseModel):
    status: TurnStateRunningStatus = pydantic.Field()
    """
    Turn is still executing.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
