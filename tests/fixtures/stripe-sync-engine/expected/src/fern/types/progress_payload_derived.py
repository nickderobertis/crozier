

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_status import RunStatus


class ProgressPayloadDerived(UniversalBaseModel):
    """
    Computed aggregates.
    """

    status: RunStatus
    records_per_second: float = pydantic.Field()
    """
    Overall throughput for the entire run.
    """

    states_per_second: float = pydantic.Field()
    """
    State checkpoints per second.
    """

    total_record_count: int = pydantic.Field()
    """
    Total records across all streams.
    """

    total_state_count: int = pydantic.Field()
    """
    Total source_state messages across all streams.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
