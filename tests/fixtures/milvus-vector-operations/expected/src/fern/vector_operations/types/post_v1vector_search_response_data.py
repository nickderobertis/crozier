

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v1vector_search_response_data_data_item import PostV1VectorSearchResponseDataDataItem


class PostV1VectorSearchResponseData(UniversalBaseModel):
    code: typing.Optional[int] = pydantic.Field(default=None)
    """
    Response code.
    """

    data: typing.Optional[typing.List[PostV1VectorSearchResponseDataDataItem]] = pydantic.Field(default=None)
    """
    Response payload that carries the search results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
