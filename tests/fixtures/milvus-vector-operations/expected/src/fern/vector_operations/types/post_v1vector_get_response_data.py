

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v1vector_get_response_data_data_item import PostV1VectorGetResponseDataDataItem


class PostV1VectorGetResponseData(UniversalBaseModel):
    code: typing.Optional[int] = pydantic.Field(default=None)
    """
    Response code.
    """

    data: typing.Optional[typing.List[PostV1VectorGetResponseDataDataItem]] = pydantic.Field(default=None)
    """
    Query results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
