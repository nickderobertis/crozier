

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1get_usage_api_requests_count_response_output_error import V1GetUsageApiRequestsCountResponseOutputError
from .v1get_usage_api_requests_count_response_output_result_item import (
    V1GetUsageApiRequestsCountResponseOutputResultItem,
)


class V1GetUsageApiRequestsCountResponseOutput(UniversalBaseModel):
    result: typing.Optional[typing.List[V1GetUsageApiRequestsCountResponseOutputResultItem]] = None
    error: typing.Optional[V1GetUsageApiRequestsCountResponseOutputError] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
