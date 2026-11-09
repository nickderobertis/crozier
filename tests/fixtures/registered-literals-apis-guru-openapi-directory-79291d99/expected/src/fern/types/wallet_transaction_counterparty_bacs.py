

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .recipient_bacs import RecipientBacs


class WalletTransactionCounterpartyBacs(RecipientBacs):
    """
    The account number and sort code of the counterparty's account
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
