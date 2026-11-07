

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .common_deal import CommonDeal
from .common_response_status import CommonResponseStatus


class CrmGetDealResponse(UniversalBaseModel):
    status: CommonResponseStatus
    result: CommonDeal

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
