

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v60address_components import V60AddressComponents
from .v60address_detail_incorporated import V60AddressDetailIncorporated


class V60AddressDetail(UniversalBaseModel):
    normalized_address: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="normalizedAddress"),
        pydantic.Field(
            alias="normalizedAddress",
            description="Standardized address returned by the geocoder, or empty when the location was not geocoded (e.g. postal-code-only lookups).",
        ),
    ]
    """
    Standardized address returned by the geocoder, or empty when the location was not geocoded (e.g. postal-code-only lookups).
    """

    incorporated: V60AddressDetailIncorporated = pydantic.Field()
    """
    Whether the location falls within incorporated city limits, as the string 'true' or 'false'.
    """

    geo_lat: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="geoLat"),
        pydantic.Field(
            alias="geoLat", description="Latitude of the geocoded location, or 0 when the location was not geocoded."
        ),
    ]
    """
    Latitude of the geocoded location, or 0 when the location was not geocoded.
    """

    geo_lng: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="geoLng"),
        pydantic.Field(
            alias="geoLng", description="Longitude of the geocoded location, or 0 when the location was not geocoded."
        ),
    ]
    """
    Longitude of the geocoded location, or 0 when the location was not geocoded.
    """

    address: typing.Optional[V60AddressComponents] = pydantic.Field(default=None)
    """
    Extended address components from the geocoder. Present only when addressDetailExtended=true is supplied on a geocoded (address or lat/lng) lookup. Available for both USA and Canadian lookups.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
