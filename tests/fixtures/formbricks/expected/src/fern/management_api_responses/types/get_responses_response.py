

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_responses_response_data_item import GetResponsesResponseDataItem
from .get_responses_response_meta import GetResponsesResponseMeta


class GetResponsesResponse(UniversalBaseModel):
    data: typing.Optional[typing.List[GetResponsesResponseDataItem]] = None
    meta: typing.Optional[GetResponsesResponseMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
