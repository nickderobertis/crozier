

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wallet_transaction_counterparty_bacs import WalletTransactionCounterpartyBacs
from .wallet_transaction_counterparty_international import WalletTransactionCounterpartyInternational


class WalletTransactionCounterpartyNumbers(UniversalBaseModel):
    """
    The counterparty's bank account numbers. Exactly one of IBAN or BACS data is required.
    """

    bacs: typing.Optional[WalletTransactionCounterpartyBacs] = None
    international: typing.Optional[WalletTransactionCounterpartyInternational] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
