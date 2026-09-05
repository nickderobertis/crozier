

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ipsec_crypto_profiles_ah_authentication_item import IpsecCryptoProfilesAhAuthenticationItem


class IpsecCryptoProfilesAh(UniversalBaseModel):
    authentication: typing.List[IpsecCryptoProfilesAhAuthenticationItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
