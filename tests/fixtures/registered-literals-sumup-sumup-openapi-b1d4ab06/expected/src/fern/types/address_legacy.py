

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AddressLegacy(UniversalBaseModel):
    """
    Profile's personal address information.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    City name from the address.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Two letter country code formatted according to [ISO3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
    """

    line1: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="line_1"),
        pydantic.Field(
            alias="line_1", description="First line of the address with details of the street name and number."
        ),
    ] = None
    """
    First line of the address with details of the street name and number.
    """

    line2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="line_2"),
        pydantic.Field(
            alias="line_2",
            description="Second line of the address with details of the building, unit, apartment, and floor numbers.",
        ),
    ] = None
    """
    Second line of the address with details of the building, unit, apartment, and floor numbers.
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Postal code from the address.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State name or abbreviation from the address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
