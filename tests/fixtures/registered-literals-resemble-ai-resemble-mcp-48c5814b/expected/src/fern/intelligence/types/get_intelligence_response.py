

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_intelligence_response_item import GetIntelligenceResponseItem


class GetIntelligenceResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    item: typing.Optional[GetIntelligenceResponseItem] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
