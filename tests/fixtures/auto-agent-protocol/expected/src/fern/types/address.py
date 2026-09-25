

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Address(UniversalBaseModel):
    """
    Postal address. All fields are OPTIONAL by design — the buyer agent should pass through whatever pieces of the address are available (e.g. just a ZIP for regional pricing, or just city+state, or the full street address). The dealer is responsible for handling partial addresses gracefully.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Country code or name (e.g. 'US'). Optional; defaults to 'US' when omitted.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State / region code or full name (e.g. 'CA' or 'California').
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    City or locality (e.g. 'San Francisco').
    """

    address_line1: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="address_line_1"),
        pydantic.Field(alias="address_line_1", description="Primary street line (e.g. '1280 Howard Street')."),
    ] = None
    """
    Primary street line (e.g. '1280 Howard Street').
    """

    address_line2: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="address_line_2"),
        pydantic.Field(
            alias="address_line_2", description="Secondary street line (suite, apartment, building, floor)."
        ),
    ] = None
    """
    Secondary street line (suite, apartment, building, floor).
    """

    zip: typing.Optional[str] = pydantic.Field(default=None)
    """
    Postal / ZIP code (e.g. '94103' or '94103-1234').
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
