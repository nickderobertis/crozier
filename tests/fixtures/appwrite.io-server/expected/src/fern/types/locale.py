

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Locale(UniversalBaseModel):
    """
    Locale
    """

    continent: str = pydantic.Field()
    """
    Continent name. This field support localization.
    """

    continent_code: typing_extensions.Annotated[str, FieldMetadata(alias="continentCode")] = pydantic.Field()
    """
    Continent code. A two character continent code "AF" for Africa, "AN" for Antarctica, "AS" for Asia, "EU" for Europe, "NA" for North America, "OC" for Oceania, and "SA" for South America.
    """

    country: str = pydantic.Field()
    """
    Country name. This field support localization.
    """

    country_code: typing_extensions.Annotated[str, FieldMetadata(alias="countryCode")] = pydantic.Field()
    """
    Country code in [ISO 3166-1](http://en.wikipedia.org/wiki/ISO_3166-1) two-character format
    """

    currency: str = pydantic.Field()
    """
    Currency code in [ISO 4217-1](http://en.wikipedia.org/wiki/ISO_4217) three-character format
    """

    eu: bool = pydantic.Field()
    """
    True if country is part of the Europian Union.
    """

    ip: str = pydantic.Field()
    """
    User IP address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
