

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wallet_get_with_available_credits import WalletGetWithAvailableCredits


class EnvelopeListWalletGetWithAvailableCredits(UniversalBaseModel):
    data: typing.Optional[typing.List[WalletGetWithAvailableCredits]] = None
    error: typing.Optional[typing.Any] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
