

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .currency import Currency
from .ecommerce_customer_addresses_item import EcommerceCustomerAddressesItem
from .ecommerce_customer_status import EcommerceCustomerStatus
from .email import Email
from .id import Id
from .linked_ecommerce_order import LinkedEcommerceOrder
from .phone_number import PhoneNumber
from .updated_at import UpdatedAt


class EcommerceCustomer(UniversalBaseModel):
    addresses: typing.Optional[typing.List[EcommerceCustomerAddressesItem]] = pydantic.Field(default=None)
    """
    An array of addresses for the customer.
    """

    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Company name of the customer
    """

    created_at: typing.Optional[CreatedAt] = None
    currency: typing.Optional[Currency] = None
    emails: typing.Optional[typing.List[Email]] = pydantic.Field(default=None)
    """
    An array of email addresses for the customer.
    """

    first_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    First name of the customer
    """

    id: typing.Optional[Id] = None
    last_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Last name of the customer
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Full name of the customer
    """

    orders: typing.Optional[typing.List[LinkedEcommerceOrder]] = None
    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = pydantic.Field(default=None)
    """
    An array of phone numbers for the customer.
    """

    status: typing.Optional[EcommerceCustomerStatus] = pydantic.Field(default=None)
    """
    The current status of the customer
    """

    updated_at: typing.Optional[UpdatedAt] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
