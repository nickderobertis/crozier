

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wallet_balance import WalletBalance
from .wallet_numbers import WalletNumbers
from .wallet_status import WalletStatus


class Wallet(UniversalBaseModel):
    """
    An object representing the e-wallet
    """

    balance: WalletBalance
    numbers: WalletNumbers
    recipient_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the recipient that corresponds to the e-wallet account numbers
    """

    status: WalletStatus
    wallet_id: str = pydantic.Field()
    """
    A unique ID identifying the e-wallet
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
