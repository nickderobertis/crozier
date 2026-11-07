

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .topic import Topic


class Log(UniversalBaseModel):
    """
    log data as returned from the RPC (with slight enhancements)
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the number of the block"),
    ] = None
    """
    the number of the block
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

    log_index: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="logIndex"),
        pydantic.Field(alias="logIndex", description="the zero-indexed position of this log relative to the block"),
    ] = None
    """
    the zero-indexed position of this log relative to the block
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the timestamp of the block this log appears in
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the smart contract that emitted this log
    """

    topics: typing.Optional[typing.List[Topic]] = pydantic.Field(default=None)
    """
    first topic event signature up to 3 additional index parameters may appear
    """

    data: typing.Optional[str] = pydantic.Field(default=None)
    """
    any remaining un-indexed parameters to the event
    """

    transaction_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="transactionHash"),
        pydantic.Field(alias="transactionHash", description="the hash of the transction"),
    ] = None
    """
    the hash of the transction
    """

    block_hash: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="blockHash"),
        pydantic.Field(alias="blockHash", description="the hash of the block"),
    ] = None
    """
    the hash of the block
    """

    articulated_log: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="articulatedLog"),
        pydantic.Field(alias="articulatedLog", description="a human-readable version of the topic and data fields"),
    ] = None
    """
    a human-readable version of the topic and data fields
    """

    compressed_log: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="compressedLog"),
        pydantic.Field(
            alias="compressedLog", description="a truncated, more readable version of the articulation (calculated)"
        ),
    ] = None
    """
    a truncated, more readable version of the articulation (calculated)
    """

    is_nft: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isNFT"),
        pydantic.Field(alias="isNFT", description="true if the log is an NFT transfer (calculated)"),
    ] = None
    """
    true if the log is an NFT transfer (calculated)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
