

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037diag_statistics_time import Dbv0037DiagStatisticsTime


class Dbv0037DiagStatisticsRpCs(UniversalBaseModel):
    """
    Statistics by RPC type
    """

    rpc: typing.Optional[str] = pydantic.Field(default=None)
    """
    RPC type
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of RPCs
    """

    time: typing.Optional[Dbv0037DiagStatisticsTime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
