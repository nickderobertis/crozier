

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .log import Log


class Receipt(UniversalBaseModel):
    """
    receipt data as returned from the RPC (with slight enhancements)
    """

    block_hash: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="blockHash"), pydantic.Field(alias="blockHash")
    ] = None
    block_number: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="blockNumber"), pydantic.Field(alias="blockNumber")
    ] = None
    contract_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="contractAddress"),
        pydantic.Field(alias="contractAddress", description="the address of the newly created contract, if any"),
    ] = None
    """
    the address of the newly created contract, if any
    """

    gas_used: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="gasUsed"),
        pydantic.Field(alias="gasUsed", description="the amount of gas actually used by the transaction"),
    ] = None
    """
    the amount of gas actually used by the transaction
    """

    is_error: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isError"), pydantic.Field(alias="isError")
    ] = None
    logs: typing.Optional[typing.List[Log]] = pydantic.Field(default=None)
    """
    a possibly empty array of logs
    """

    status: typing.Optional[float] = pydantic.Field(default=None)
    """
    `1` on transaction suceess, `null` if tx precedes Byzantium, `0` otherwise
    """

    transaction_hash: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="transactionHash"), pydantic.Field(alias="transactionHash")
    ] = None
    transaction_index: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="transactionIndex"), pydantic.Field(alias="transactionIndex")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
