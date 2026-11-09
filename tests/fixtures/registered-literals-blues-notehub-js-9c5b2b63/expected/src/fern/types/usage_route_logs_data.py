

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UsageRouteLogsData(UniversalBaseModel):
    avg_latency_ms: typing.Optional[float] = pydantic.Field(default=None)
    """
    Average routing latency in milliseconds for route logs with recorded duration
    """

    failed_routes: int
    period: dt.datetime
    route: typing.Optional[str] = pydantic.Field(default=None)
    """
    The route UID (only present when aggregate is 'route')
    """

    successful_routes: int
    total_routes: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
