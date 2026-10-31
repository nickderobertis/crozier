

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wallet_id_int import WalletIdInt
from .wallet_info_input_wallet_credit_amount import WalletInfoInputWalletCreditAmount


class WalletInfoInput(UniversalBaseModel):
    wallet_id: WalletIdInt
    wallet_name: str
    wallet_credit_amount: WalletInfoInputWalletCreditAmount

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
