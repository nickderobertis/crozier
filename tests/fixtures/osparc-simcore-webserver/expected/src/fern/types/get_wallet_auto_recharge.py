

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetWalletAutoRecharge(UniversalBaseModel):
    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enables/disables auto-recharge trigger in this wallet
    """

    payment_method_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="paymentMethodId"),
        pydantic.Field(
            alias="paymentMethodId",
            description="Payment method in the wallet used to perform the auto-recharge payments or None if still undefined",
        ),
    ] = None
    """
    Payment method in the wallet used to perform the auto-recharge payments or None if still undefined
    """

    min_balance_in_credits: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="minBalanceInCredits"),
        pydantic.Field(
            alias="minBalanceInCredits",
            description="Minimum balance in credits that triggers an auto-recharge [Read only]",
        ),
    ]
    """
    Minimum balance in credits that triggers an auto-recharge [Read only]
    """

    top_up_amount_in_usd: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="topUpAmountInUsd"),
        pydantic.Field(
            alias="topUpAmountInUsd", description="Amount in USD paid when auto-recharge condition is satisfied"
        ),
    ]
    """
    Amount in USD paid when auto-recharge condition is satisfied
    """

    monthly_limit_in_usd: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="monthlyLimitInUsd"),
        pydantic.Field(
            alias="monthlyLimitInUsd",
            description="Maximum amount in USD charged within a natural month.None indicates no limit.",
        ),
    ] = None
    """
    Maximum amount in USD charged within a natural month.None indicates no limit.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
