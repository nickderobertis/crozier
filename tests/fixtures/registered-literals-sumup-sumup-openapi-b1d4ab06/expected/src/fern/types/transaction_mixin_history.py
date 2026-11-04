

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transaction_mixin_history_payout_plan import TransactionMixinHistoryPayoutPlan


class TransactionMixinHistory(UniversalBaseModel):
    """
    Additional transaction fields used by history and detailed views.
    """

    product_summary: typing.Optional[str] = pydantic.Field(default=None)
    """
    Short description of the payment. The value is taken from the `description` property of the related checkout resource.
    """

    payouts_total: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of payouts to the registered user specified in the `user` property.
    """

    payouts_received: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of payouts that are made to the registered user specified in the `user` property.
    """

    payout_plan: typing.Optional[TransactionMixinHistoryPayoutPlan] = pydantic.Field(default=None)
    """
    Payout plan of the registered user at the time when the transaction was made.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
