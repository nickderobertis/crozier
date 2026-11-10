

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .numbers_iban import NumbersIban


class WalletTransactionCounterpartyInternational(UniversalBaseModel):
    """
    International Bank Account Number for a Wallet Transaction
    """

    iban: typing.Optional[NumbersIban] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
