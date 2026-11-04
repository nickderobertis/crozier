

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .uint64 import Uint64


class Trace(UniversalBaseModel):
    """
    trace data as returned from the RPC (with slight enhancements)
    """

    block_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="blockHash"),
        pydantic.Field(alias="blockHash", description="the hash of the block containing this trace"),
    ] = None
    """
    the hash of the block containing this trace
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the number of the block"),
    ] = None
    """
    the number of the block
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the timestamp of the block
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    transaction_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transactionHash"),
        pydantic.Field(alias="transactionHash", description="the transaction's hash containing this trace"),
    ] = None
    """
    the transaction's hash containing this trace
    """

    transaction_index: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="transactionIndex"),
        pydantic.Field(
            alias="transactionIndex", description="the zero-indexed position of the transaction in the block"
        ),
    ] = None
    """
    the zero-indexed position of the transaction in the block
    """

    trace_address: typing_extensions.Annotated[
        typing.Optional[typing.List[Uint64]],
        FieldMetadata(alias="traceAddress"),
        pydantic.Field(alias="traceAddress", description="a particular trace's address in the trace tree"),
    ] = None
    """
    a particular trace's address in the trace tree
    """

    subtraces: typing.Optional[int] = pydantic.Field(default=None)
    """
    the number of children traces that the trace hash
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    the type of the trace
    """

    action: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    the trace action for this trace
    """

    result: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    the trace result of this trace
    """

    articulated_trace: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="articulatedTrace"),
        pydantic.Field(alias="articulatedTrace", description="human readable version of the trace action input data"),
    ] = None
    """
    human readable version of the trace action input data
    """

    compressed_trace: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="compressedTrace"),
        pydantic.Field(
            alias="compressedTrace", description="a compressed string version of the articulated trace (calculated)"
        ),
    ] = None
    """
    a compressed string version of the articulated trace (calculated)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
