

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ipsec_crypto_profiles_esp_encryption_item import IpsecCryptoProfilesEspEncryptionItem


class IpsecCryptoProfilesEsp(UniversalBaseModel):
    authentication: typing.List[str] = pydantic.Field()
    """
    Authentication algorithm
    """

    encryption: typing.List[IpsecCryptoProfilesEspEncryptionItem] = pydantic.Field()
    """
    Encryption algorithm
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
