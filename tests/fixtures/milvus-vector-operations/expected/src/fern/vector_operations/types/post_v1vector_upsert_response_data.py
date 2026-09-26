

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v1vector_upsert_response_data_data import PostV1VectorUpsertResponseDataData


class PostV1VectorUpsertResponseData(UniversalBaseModel):
    code: typing.Optional[int] = pydantic.Field(default=None)
    """
    Response code.
    """

    data: typing.Optional[PostV1VectorUpsertResponseDataData] = pydantic.Field(default=None)
    """
    Response payload.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
