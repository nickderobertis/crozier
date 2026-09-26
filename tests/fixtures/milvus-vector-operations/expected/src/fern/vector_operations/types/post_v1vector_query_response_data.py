

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v1vector_query_response_data_data_item import PostV1VectorQueryResponseDataDataItem


class PostV1VectorQueryResponseData(UniversalBaseModel):
    code: typing.Optional[int] = pydantic.Field(default=None)
    """
    Response code.
    """

    data: typing.Optional[typing.List[PostV1VectorQueryResponseDataDataItem]] = pydantic.Field(default=None)
    """
    Response payload which is an array of objects that contain the specified output fields and their corresponding values.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
