

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v1vector_insert_response_data_data import PostV1VectorInsertResponseDataData


class PostV1VectorInsertResponseData(UniversalBaseModel):
    code: typing.Optional[int] = pydantic.Field(default=None)
    """
    Response code.
    """

    data: typing.Optional[PostV1VectorInsertResponseDataData] = pydantic.Field(default=None)
    """
    Response payload which is the statistics on the insert results.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
