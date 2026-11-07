

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .internal_recent_api_calls import InternalRecentApiCalls


class InternalRecentAppApiCallsResponse(UniversalBaseModel):
    result: typing.Optional[typing.List[InternalRecentApiCalls]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
