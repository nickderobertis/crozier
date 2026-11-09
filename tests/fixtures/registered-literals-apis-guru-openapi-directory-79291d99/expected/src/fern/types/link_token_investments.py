

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LinkTokenInvestments(UniversalBaseModel):
    """
    Configuration parameters for the Investments product
    """

    allow_unverified_crypto_wallets: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, allow self-custody crypto wallets to be added without requiring signature verification. Defaults to `false`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
