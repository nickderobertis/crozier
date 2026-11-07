

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TraceAction(UniversalBaseModel):
    """
    trace action data as returned from the RPC (with slight enhancements)
    """

    from_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="from"),
        pydantic.Field(alias="from", description="address from which the trace was sent"),
    ] = None
    """
    address from which the trace was sent
    """

    to: typing.Optional[str] = pydantic.Field(default=None)
    """
    address to which the trace was sent
    """

    gas: typing.Optional[float] = pydantic.Field(default=None)
    """
    the maximum number of gas allowed for this trace
    """

    input: typing.Optional[str] = pydantic.Field(default=None)
    """
    an encoded version of the function call
    """

    call_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="callType"),
        pydantic.Field(alias="callType", description="the type of call"),
    ] = None
    """
    the type of call
    """

    refund_address: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="refundAddress"),
        pydantic.Field(
            alias="refundAddress",
            description="if the call type is self-destruct, the address to which the refund is sent",
        ),
    ] = None
    """
    if the call type is self-destruct, the address to which the refund is sent
    """

    reward_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="rewardType"),
        pydantic.Field(alias="rewardType", description="the type of reward"),
    ] = None
    """
    the type of reward
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    the value (in wei) of this trace action
    """

    ether: typing.Optional[str] = pydantic.Field(default=None)
    """
    if --ether is specified, the value in ether (calculated)
    """

    self_destructed: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="selfDestructed"),
        pydantic.Field(alias="selfDestructed", description="`true` if the contract self-destructed, `false` otherwise"),
    ] = None
    """
    `true` if the contract self-destructed, `false` otherwise
    """

    balance: typing.Optional[str] = pydantic.Field(default=None)
    """
    if self-destructed, the balance of the contract at that time
    """

    balance_eth: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="balanceEth"),
        pydantic.Field(alias="balanceEth", description="if --ether is specified, the balance in ether (calculated)"),
    ] = None
    """
    if --ether is specified, the balance in ether (calculated)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
