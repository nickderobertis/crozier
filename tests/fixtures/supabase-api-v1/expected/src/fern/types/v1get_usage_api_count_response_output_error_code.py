

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1get_usage_api_count_response_output_error_code_errors_item import (
    V1GetUsageApiCountResponseOutputErrorCodeErrorsItem,
)


class V1GetUsageApiCountResponseOutputErrorCode(UniversalBaseModel):
    code: float
    errors: typing.List[V1GetUsageApiCountResponseOutputErrorCodeErrorsItem]
    message: str
    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
