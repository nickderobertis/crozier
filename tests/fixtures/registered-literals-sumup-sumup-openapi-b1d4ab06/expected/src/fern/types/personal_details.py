

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address_legacy import AddressLegacy


class PersonalDetails(UniversalBaseModel):
    """
    Personal details for the customer.
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    First name of the customer.
    """

    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last name of the customer.
    """

    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email address of the customer.
    """

    phone: typing.Optional[str] = pydantic.Field(default=None)
    """
    Phone number of the customer.
    """

    birth_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Date of birth of the customer.
    """

    tax_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identification number used for tax purposes, such as a CPF in Brazil.
    """

    address: typing.Optional[AddressLegacy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
