

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ike_crypto_profiles_dh_group_item import IkeCryptoProfilesDhGroupItem
from .ike_crypto_profiles_encryption_item import IkeCryptoProfilesEncryptionItem
from .ike_crypto_profiles_hash_item import IkeCryptoProfilesHashItem
from .ike_crypto_profiles_lifetime import IkeCryptoProfilesLifetime


class IkeCryptoProfiles(UniversalBaseModel):
    authentication_multiple: typing.Optional[int] = pydantic.Field(default=None)
    """
    IKEv2 SA reauthentication interval equals authetication-multiple * rekey-lifetime; 0 means reauthentication disabled
    """

    dh_group: typing.List[IkeCryptoProfilesDhGroupItem]
    encryption: typing.List[IkeCryptoProfilesEncryptionItem] = pydantic.Field()
    """
    Encryption algorithm
    """

    hash: typing.List[IkeCryptoProfilesHashItem]
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    uuid of the resource
    """

    lifetime: typing.Optional[IkeCryptoProfilesLifetime] = None
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
