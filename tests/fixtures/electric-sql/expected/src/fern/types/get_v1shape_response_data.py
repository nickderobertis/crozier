

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_v1shape_response_data_data_item import GetV1ShapeResponseDataDataItem
from .get_v1shape_response_data_metadata import GetV1ShapeResponseDataMetadata


class GetV1ShapeResponseData(UniversalBaseModel):
    """
    Object containing subset snapshot data and metadata, returned when
    any `subset__*` parameters are present in the request.
    """

    metadata: GetV1ShapeResponseDataMetadata = pydantic.Field()
    """
    PostgreSQL snapshot metadata for tracking which changes to skip.
    This response format is returned when any `subset__*` parameters are present in the request.
    """

    data: typing.List[GetV1ShapeResponseDataDataItem] = pydantic.Field()
    """
    Array of operation messages (no control messages) representing the subset snapshot data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
