

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CustomersFilter(UniversalBaseModel):
    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company Name of customer to search for
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display Name of customer to search for
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email of customer to search for
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    First name of customer to search for
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last name of customer to search for
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
