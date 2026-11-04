

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_account_segments_response_data_item import GetAccountSegmentsResponseDataItem
from .get_account_segments_response_meta import GetAccountSegmentsResponseMeta


class GetAccountSegmentsResponse(UniversalBaseModel):
    meta: GetAccountSegmentsResponseMeta
    data: typing.List[GetAccountSegmentsResponseDataItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
