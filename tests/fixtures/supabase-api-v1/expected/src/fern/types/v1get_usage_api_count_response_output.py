

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1get_usage_api_count_response_output_error import V1GetUsageApiCountResponseOutputError
from .v1get_usage_api_count_response_output_result_item import V1GetUsageApiCountResponseOutputResultItem


class V1GetUsageApiCountResponseOutput(UniversalBaseModel):
    result: typing.Optional[typing.List[V1GetUsageApiCountResponseOutputResultItem]] = None
    error: typing.Optional[V1GetUsageApiCountResponseOutputError] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
