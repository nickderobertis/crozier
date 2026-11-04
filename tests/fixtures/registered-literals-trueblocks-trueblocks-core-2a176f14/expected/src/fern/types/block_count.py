

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BlockCount(UniversalBaseModel):
    """
    counts of various parts of the block data such as tx_count, trace_count, etc.
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the block's block number"),
    ] = None
    """
    the block's block number
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the timestamp of the block
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    transactions_cnt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="transactionsCnt"),
        pydantic.Field(alias="transactionsCnt", description="the number transactions in the block"),
    ] = None
    """
    the number transactions in the block
    """

    uncles_cnt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="unclesCnt"),
        pydantic.Field(alias="unclesCnt", description="the number of uncles in the block"),
    ] = None
    """
    the number of uncles in the block
    """

    logs_cnt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="logsCnt"),
        pydantic.Field(alias="logsCnt", description="the number of logs in the block"),
    ] = None
    """
    the number of logs in the block
    """

    traces_cnt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="tracesCnt"),
        pydantic.Field(alias="tracesCnt", description="the number of traces in the block"),
    ] = None
    """
    the number of traces in the block
    """

    withdrawals_cnt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="withdrawalsCnt"),
        pydantic.Field(alias="withdrawalsCnt", description="the number of withdrawals in the block"),
    ] = None
    """
    the number of withdrawals in the block
    """

    address_cnt: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="addressCnt"),
        pydantic.Field(alias="addressCnt", description="the number of address appearances in the block"),
    ] = None
    """
    the number of address appearances in the block
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
