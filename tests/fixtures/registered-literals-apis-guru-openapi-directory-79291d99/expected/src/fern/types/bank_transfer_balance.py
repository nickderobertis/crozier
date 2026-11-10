

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BankTransferBalance(UniversalBaseModel):
    """
    Information about the balance of a bank transfer
    """

    available: str = pydantic.Field()
    """
    The total available balance - the sum of all successful debit transfer amounts minus all credit transfer amounts.
    """

    transactable: str = pydantic.Field()
    """
    The transactable balance shows the amount in your account that you are able to use for transfers, and is essentially your available balance minus your minimum balance.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
