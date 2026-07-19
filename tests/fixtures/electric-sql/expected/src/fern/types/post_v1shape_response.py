

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_v1shape_response_data_item import PostV1ShapeResponseDataItem
from .post_v1shape_response_metadata import PostV1ShapeResponseMetadata


class PostV1ShapeResponse(UniversalBaseModel):
    metadata: PostV1ShapeResponseMetadata = pydantic.Field()
    """
    PostgreSQL snapshot metadata.
    """

    data: typing.List[PostV1ShapeResponseDataItem] = pydantic.Field()
    """
    Array of operation messages.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
