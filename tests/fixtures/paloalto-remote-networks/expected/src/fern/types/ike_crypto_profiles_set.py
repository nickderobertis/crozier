

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ike_crypto_profiles import IkeCryptoProfiles


class IkeCryptoProfilesSet(UniversalBaseModel):
    """
    set of ike crypto profiles
    """

    ike_crypto_profiles: typing_extensions.Annotated[
        typing.Optional[typing.List[IkeCryptoProfiles]],
        FieldMetadata(alias="IkeCryptoProfiles"),
        pydantic.Field(alias="IkeCryptoProfiles", description="The ike crypto profile"),
    ] = None
    """
    The ike crypto profile
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
