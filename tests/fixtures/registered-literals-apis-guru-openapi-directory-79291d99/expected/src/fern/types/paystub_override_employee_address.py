

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PaystubOverrideEmployeeAddress(UniversalBaseModel):
    """
    The address of the employee.
    """

    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full city name.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country of the address.
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    5 digit postal code.
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The region or state
    Example: `"NC"`
    """

    street: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full street address
    Example: `"564 Main Street, APT 15"`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
