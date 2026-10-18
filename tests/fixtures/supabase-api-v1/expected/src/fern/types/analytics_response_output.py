

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .analytics_response_output_error import AnalyticsResponseOutputError


class AnalyticsResponseOutput(UniversalBaseModel):
    result: typing.Optional[typing.List[typing.Any]] = None
    error: typing.Optional[AnalyticsResponseOutputError] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
