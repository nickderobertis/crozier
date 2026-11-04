

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_user_segments_response_data_item import GetUserSegmentsResponseDataItem
from .get_user_segments_response_meta import GetUserSegmentsResponseMeta


class GetUserSegmentsResponse(UniversalBaseModel):
    meta: GetUserSegmentsResponseMeta
    data: typing.List[GetUserSegmentsResponseDataItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
