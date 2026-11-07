

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Approval(UniversalBaseModel):
    """
    an ERC-20 token approval granting spending permission from owner to spender
    """

    allowance: typing.Optional[str] = pydantic.Field(default=None)
    """
    the amount of tokens approved for spending
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the current block number when the report was generated"),
    ] = None
    """
    the current block number when the report was generated
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the current timestamp when the report was generated
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    owner: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address of the owner of the token (the approver)
    """

    spender: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address being granted approval to spend tokens
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    the address of the ERC-20 token being approved
    """

    last_app_block: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="lastAppBlock"),
        pydantic.Field(alias="lastAppBlock", description="the block number of the last approval event"),
    ] = None
    """
    the block number of the last approval event
    """

    last_app_ts: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="lastAppTs"),
        pydantic.Field(alias="lastAppTs", description="the timestamp of the last approval event"),
    ] = None
    """
    the timestamp of the last approval event
    """

    last_app_tx_id: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="lastAppTxID"),
        pydantic.Field(alias="lastAppTxID", description="the transaction index of the last approval event"),
    ] = None
    """
    the transaction index of the last approval event
    """

    last_app_log_id: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="lastAppLogID"),
        pydantic.Field(alias="lastAppLogID", description="the log index of the last approval event"),
    ] = None
    """
    the log index of the last approval event
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
