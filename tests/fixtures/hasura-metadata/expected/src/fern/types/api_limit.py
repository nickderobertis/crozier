

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .limit_max_batch_size import LimitMaxBatchSize
from .limit_max_depth import LimitMaxDepth
from .limit_max_nodes import LimitMaxNodes
from .limit_max_time import LimitMaxTime
from .limit_rate_limit_config import LimitRateLimitConfig


class ApiLimit(UniversalBaseModel):
    batch_limit: typing.Optional[LimitMaxBatchSize] = None
    depth_limit: typing.Optional[LimitMaxDepth] = None
    disabled: typing.Optional[bool] = None
    node_limit: typing.Optional[LimitMaxNodes] = None
    rate_limit: typing.Optional[LimitRateLimitConfig] = None
    time_limit: typing.Optional[LimitMaxTime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
