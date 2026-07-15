

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_contentpro_similar_text_response_data_item import PostContentproSimilarTextResponseDataItem


class PostContentproSimilarTextResponse(UniversalBaseModel):
    calls_per_month: typing.Optional[str] = None
    count_remaining: typing.Optional[str] = None
    data: typing.Optional[typing.List[PostContentproSimilarTextResponseDataItem]] = None
    renewal_date: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
