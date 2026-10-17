

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .analytics_response_output_error_code_errors_item import AnalyticsResponseOutputErrorCodeErrorsItem


class AnalyticsResponseOutputErrorCode(UniversalBaseModel):
    code: float
    errors: typing.List[AnalyticsResponseOutputErrorCodeErrorsItem]
    message: str
    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
