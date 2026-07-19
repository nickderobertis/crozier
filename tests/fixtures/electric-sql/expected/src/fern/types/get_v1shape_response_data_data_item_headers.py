

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_v1shape_response_data_data_item_headers_operation import GetV1ShapeResponseDataDataItemHeadersOperation


class GetV1ShapeResponseDataDataItemHeaders(UniversalBaseModel):
    """
    Metadata about the operation.
    """

    operation: typing.Optional[GetV1ShapeResponseDataDataItemHeadersOperation] = pydantic.Field(default=None)
    """
    The type of operation performed on the row of the shape.
    """

    snapshot_mark: typing.Optional[int] = pydantic.Field(default=None)
    """
    Random number identifying this snapshot.
    Matches the `snapshot_mark` in the metadata object.
    """

    lsn: typing.Optional[str] = pydantic.Field(default=None)
    """
    The logical sequence number of the operation.
    
    Only present on operations that were received from the event stream.
    It's missing on initial query results and on compacted items.
    """

    op_position: typing.Optional[int] = pydantic.Field(default=None)
    """
    The position of the operation in the transaction.
    
    Only present on operations that were received from the event stream.
    """

    txids: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    The list of transaction IDs that this operation was part of.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
