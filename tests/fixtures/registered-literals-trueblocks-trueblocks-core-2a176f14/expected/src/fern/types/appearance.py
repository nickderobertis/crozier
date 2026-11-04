

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Appearance(UniversalBaseModel):
    """
    an appearance (`<blockNumber,transactionIndex>`) of an address anywhere on the chain (note that in some cases, not all fields will appear depending on the command)
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address of the appearance
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the number of the block"),
    ] = None
    """
    the number of the block
    """

    transaction_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="transactionIndex"),
        pydantic.Field(alias="transactionIndex", description="the index of the transaction in the block"),
    ] = None
    """
    the index of the transaction in the block
    """

    trace_index: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="traceIndex"),
        pydantic.Field(alias="traceIndex", description="the zero-based index of the trace in the transaction"),
    ] = None
    """
    the zero-based index of the trace in the transaction
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    the location in the data where the appearance was found
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the timestamp for this appearance
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
