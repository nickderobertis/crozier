

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dbv0037diag_statistics_time1 import Dbv0037DiagStatisticsTime1


class Dbv0037DiagStatisticsUsers(UniversalBaseModel):
    """
    Statistics by user RPCs
    """

    user: typing.Optional[str] = pydantic.Field(default=None)
    """
    User name
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of RPCs
    """

    time: typing.Optional[Dbv0037DiagStatisticsTime1] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
