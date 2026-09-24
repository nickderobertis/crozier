

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V60AddressComponents(UniversalBaseModel):
    country_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="countryCode"),
        pydantic.Field(alias="countryCode", description="ISO-3 country code of the geocoded location (e.g. USA, CAN)."),
    ]
    """
    ISO-3 country code of the geocoded location (e.g. USA, CAN).
    """

    country_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="countryName"),
        pydantic.Field(
            alias="countryName", description="Full country name of the geocoded location (e.g. United States, Canada)."
        ),
    ]
    """
    Full country name of the geocoded location (e.g. United States, Canada).
    """

    state_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="stateCode"),
        pydantic.Field(alias="stateCode", description="State or province code (e.g. CA, ON)."),
    ]
    """
    State or province code (e.g. CA, ON).
    """

    state: str = pydantic.Field()
    """
    Full state or province name.
    """

    county: str = pydantic.Field()
    """
    County name, when available.
    """

    city: str = pydantic.Field()
    """
    City name.
    """

    street: str = pydantic.Field()
    """
    Street name.
    """

    postal_code: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="postalCode"),
        pydantic.Field(
            alias="postalCode",
            description="Full postal code (ZIP+4 for US addresses when available; full Canadian postal code for Canadian addresses).",
        ),
    ]
    """
    Full postal code (ZIP+4 for US addresses when available; full Canadian postal code for Canadian addresses).
    """

    house_number: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="houseNumber"),
        pydantic.Field(alias="houseNumber", description="House/street number, when available."),
    ]
    """
    House/street number, when available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
