

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Dbv0037DiagStatisticsRollups(UniversalBaseModel):
    """
    Rollup statistics
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of rollup
    """

    last_run: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp of last rollup
    """

    last_cycle: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timestamp of last cycle
    """

    max_cycle: typing.Optional[int] = pydantic.Field(default=None)
    """
    Max time of all cycles
    """

    total_time: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total time (s) spent doing rollup
    """

    mean_cycles: typing.Optional[int] = pydantic.Field(default=None)
    """
    Average time (s) of cycle
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
