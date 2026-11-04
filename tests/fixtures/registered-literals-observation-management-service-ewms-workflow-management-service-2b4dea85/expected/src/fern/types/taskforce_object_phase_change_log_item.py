

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskforceObjectPhaseChangeLogItem(UniversalBaseModel):
    target_phase: str = pydantic.Field()
    """
    The phase that the system was attempting to transition to.
    """

    timestamp: float = pydantic.Field()
    """
    The epoch timestamp when this phase change attempt was recorded in the system.
    """

    was_successful: bool = pydantic.Field()
    """
    Indicates whether the phase change was completed successfully, i.e. did it actually change?
    """

    source_event_time: typing.Optional[float] = pydantic.Field(default=None)
    """
    The epoch timestamp of the external event that led to this phase change attempt.
    """

    source_entity: str = pydantic.Field()
    """
    The entity (person, system, or process) responsible for the external event that triggered this phase change attempt.
    """

    context: str = pydantic.Field()
    """
    The circumstances or background information about the phase change attempt.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
