

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_v1shape_response_zero_item_headers_control import GetV1ShapeResponseZeroItemHeadersControl
from .get_v1shape_response_zero_item_headers_operation import GetV1ShapeResponseZeroItemHeadersOperation


class GetV1ShapeResponseZeroItemHeaders(UniversalBaseModel):
    """
    Metadata about the message.

    Messages can be `control` messages, providing information or
    instructions to the client. Or they can be operations that
    performed a certain `operation` on a row of data in the shape.

    Control messages include:
    - `up-to-date`: Indicates the client has received all available data
    - `must-refetch`: Indicates the client must discard local data and re-sync
    - `snapshot-end`: Marks the end of a subset snapshot, includes PostgreSQL
      snapshot metadata (xmin, xmax, xip_list) for tracking which changes to skip
    """

    control: typing.Optional[GetV1ShapeResponseZeroItemHeadersControl] = None
    xmin: typing.Optional[str] = pydantic.Field(default=None)
    """
    Minimum transaction ID in the snapshot (for `snapshot-end` control messages only).
    
    Part of the PostgreSQL snapshot metadata that allows clients to determine
    which changes have been incorporated into a snapshot.
    """

    xmax: typing.Optional[str] = pydantic.Field(default=None)
    """
    Maximum transaction ID in the snapshot (for `snapshot-end` control messages only).
    
    Part of the PostgreSQL snapshot metadata that allows clients to determine
    which changes have been incorporated into a snapshot.
    """

    xip_list: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of transaction IDs in progress during the snapshot (for `snapshot-end` control messages only).
    
    Part of the PostgreSQL snapshot metadata that allows clients to determine
    which changes have been incorporated into a snapshot.
    """

    operation: typing.Optional[GetV1ShapeResponseZeroItemHeadersOperation] = pydantic.Field(default=None)
    """
    The type of operation performed on the row of the shape.
    """

    lsn: typing.Optional[str] = pydantic.Field(default=None)
    """
    The logical sequence number of the operation.
    
    Only present on operations that were received from the event stream.
    It's missing on initial query results and on compacted items.
    Operations with the same LSN were committed in the same transaction and
    can be ordered by `op_position` within the same LSN.
    """

    op_position: typing.Optional[int] = pydantic.Field(default=None)
    """
    The position of the operation in the transaction.
    
    Only present on operations that were received from the event stream.
    It's missing on initial query results and on compacted items.
    """

    last: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this is the last operation in the transaction for this shape.
    
    Last operation in a transaction for the shape does not mean a last
    operation in the transaction for the database.
    
    Only present on operations that were received from the event stream.
    It's missing on initial query results and on compacted items.
    """

    txids: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    The list of transaction IDs that this operation was part of.
    
    Currently, this will only contain a single transaction ID, but future
    stream processors may merge operations from multiple transactions into a single
    operation in the event stream.
    """

    snapshot_mark: typing.Optional[int] = pydantic.Field(default=None)
    """
    Random number identifying which snapshot this operation belongs to.
    
    Only present on operation messages that are part of a subset snapshot response.
    Used to match snapshot data with its corresponding `snapshot-end` control message.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
