

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EvidenceIssuer(UniversalBaseModel):
    """
    JSON object containing information about the issuer of this document.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Designation of the issuer of the document.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    String denoting the country or supranational organization that issued the document.
    """

    country_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    String denoting the country or supranational organization that issued the document as ISO 3166/ICAO 3-letter codes [ICAO-Doc9303], e.g., "USA" or "JPN". 2-letter ICAO codes MAY be used in some circumstances for compatibility reasons.
    """

    jurisdiction: typing.Optional[str] = pydantic.Field(default=None)
    """
    String containing the name of the region(s)/state(s)/province(s)/municipality(ies) that issuer has jurisdiction over 
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
