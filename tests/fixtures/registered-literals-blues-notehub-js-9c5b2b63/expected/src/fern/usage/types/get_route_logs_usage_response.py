

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.usage_route_logs_data import UsageRouteLogsData
from ...types.usage_truncated_field import UsageTruncatedField


class GetRouteLogsUsageResponse(UniversalBaseModel):
    route_logs: typing.List[UsageRouteLogsData]
    truncated: typing.Optional[UsageTruncatedField] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
