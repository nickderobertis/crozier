

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .city import City
from .generic_country_code import GenericCountryCode
from .postal_code import PostalCode
from .region import Region
from .street import Street
from .street2 import Street2


class UserAddress(UniversalBaseModel):
    """
    Home address for the user.
    """

    city: City
    country: GenericCountryCode
    postal_code: PostalCode
    region: Region
    street: Street
    street2: typing.Optional[Street2] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
