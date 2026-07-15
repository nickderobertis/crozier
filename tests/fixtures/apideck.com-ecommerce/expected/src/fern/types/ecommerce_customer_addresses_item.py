

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ecommerce_customer_addresses_item_type import EcommerceCustomerAddressesItemType
from .id import Id


class EcommerceCustomerAddressesItem(UniversalBaseModel):
    city: typing.Optional[str] = pydantic.Field(default=None)
    """
    City of the customer
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    Country of the customer
    """

    id: typing.Optional[Id] = None
    line1: typing.Optional[str] = pydantic.Field(default=None)
    """
    First line of the street address of the customer
    """

    line2: typing.Optional[str] = pydantic.Field(default=None)
    """
    Second line of the street address of the customer
    """

    postal_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Postal code of the customer
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    State of the customer
    """

    type: typing.Optional[EcommerceCustomerAddressesItemType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
