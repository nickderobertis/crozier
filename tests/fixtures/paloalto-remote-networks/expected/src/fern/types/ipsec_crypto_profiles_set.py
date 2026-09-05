

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ipsec_crypto_profiles import IpsecCryptoProfiles


class IpsecCryptoProfilesSet(UniversalBaseModel):
    """
    set of ipsec crypto profiles
    """

    ike_crypto_profiles: typing_extensions.Annotated[
        typing.Optional[typing.List[IpsecCryptoProfiles]],
        FieldMetadata(alias="IkeCryptoProfiles"),
        pydantic.Field(alias="IkeCryptoProfiles", description="The ipsec crypto profile"),
    ] = None
    """
    The ipsec crypto profile
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
