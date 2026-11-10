

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wallet_transaction_counterparty_numbers import WalletTransactionCounterpartyNumbers


class WalletTransactionCounterparty(UniversalBaseModel):
    """
    An object representing the e-wallet transaction's counterparty
    """

    name: str = pydantic.Field()
    """
    The name of the counterparty
    """

    numbers: WalletTransactionCounterpartyNumbers

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
