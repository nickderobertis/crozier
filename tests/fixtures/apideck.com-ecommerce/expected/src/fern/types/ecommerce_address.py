

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EcommerceAddress(UniversalBaseModel):
    """
    An object representing a shipping or billing address.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    City of the billing address.
    """

    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company name of the customer
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Country of the billing address.
    """

    line1: typing.Optional[str] = pydantic.Field(default=None)
    """
    Address line 1 of the billing address.
    """

    line2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Address line 2 of the billing address.
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Postal/ZIP code of the billing address.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State/province of the billing address.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
