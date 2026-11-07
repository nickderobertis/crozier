

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .country_code import CountryCode
from .geocode import Geocode


class Address(UniversalBaseModel):
    city: str
    country: CountryCode
    geo: typing.Optional[Geocode] = None
    postal_code: typing_extensions.Annotated[str, FieldMetadata(alias="postalCode"), pydantic.Field(alias="postalCode")]
    region: typing.Optional[str] = None
    street: str
    street2: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
