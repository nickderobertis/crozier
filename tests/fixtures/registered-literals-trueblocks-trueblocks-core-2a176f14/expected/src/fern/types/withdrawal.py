

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Withdrawal(UniversalBaseModel):
    """
    withdrawal record for post-Shanghai withdrawals from the consensus layer
    """

    address: typing.Optional[str] = pydantic.Field(default=None)
    """
    the recipient for the withdrawn ether
    """

    amount: typing.Optional[str] = pydantic.Field(default=None)
    """
    a nonzero amount of ether given in gwei (1e9 wei)
    """

    ether: typing.Optional[str] = pydantic.Field(default=None)
    """
    if --ether is specified, the amount in ether (calculated)
    """

    block_number: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="blockNumber"),
        pydantic.Field(alias="blockNumber", description="the number of this block"),
    ] = None
    """
    the number of this block
    """

    index: typing.Optional[float] = pydantic.Field(default=None)
    """
    a monotonically increasing zero-based index that increments by 1 per withdrawal to uniquely identify each withdrawal
    """

    timestamp: typing.Optional[float] = pydantic.Field(default=None)
    """
    the timestamp for this block
    """

    date: typing.Optional[str] = pydantic.Field(default=None)
    """
    the timestamp as a date (calculated)
    """

    validator_index: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="validatorIndex"),
        pydantic.Field(
            alias="validatorIndex",
            description="the validator_index of the validator on the consensus layer the withdrawal corresponds to",
        ),
    ] = None
    """
    the validator_index of the validator on the consensus layer the withdrawal corresponds to
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
