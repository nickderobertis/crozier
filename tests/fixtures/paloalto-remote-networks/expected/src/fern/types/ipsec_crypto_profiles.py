

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ipsec_crypto_profiles_ah import IpsecCryptoProfilesAh
from .ipsec_crypto_profiles_dh_group import IpsecCryptoProfilesDhGroup
from .ipsec_crypto_profiles_esp import IpsecCryptoProfilesEsp
from .lifesize import Lifesize
from .lifetime import Lifetime


class IpsecCryptoProfiles(UniversalBaseModel):
    ah: typing.Optional[IpsecCryptoProfilesAh] = None
    dh_group: typing.Optional[IpsecCryptoProfilesDhGroup] = pydantic.Field(default=None)
    """
    phase-2 DH group (PFS DH group)
    """

    esp: typing.Optional[IpsecCryptoProfilesEsp] = None
    lifesize: typing.Optional[Lifesize] = None
    lifetime: Lifetime
    name: str = pydantic.Field()
    """
    Alphanumeric string begin with letter: [0-9a-zA-Z._-]
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
