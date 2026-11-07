

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TraceCount(UniversalBaseModel):
    """
    counts the number of traces in a transaction
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the block number"),
    ] = None
    """
    the block number
    """

    transaction_index: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="transactionIndex"),
        pydantic.Field(alias="transactionIndex", description="the transaction index"),
    ] = None
    """
    the transaction index
    """

    transaction_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transactionHash"),
        pydantic.Field(alias="transactionHash", description="the transaction's hash"),
    ] = None
    """
    the transaction's hash
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the timestamp of the block
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    traces_cnt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="tracesCnt"),
        pydantic.Field(alias="tracesCnt", description="the number of traces in the transaction"),
    ] = None
    """
    the number of traces in the transaction
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
