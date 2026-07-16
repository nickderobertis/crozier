

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .bank_account import BankAccount
from .company_name import CompanyName
from .currency import Currency
from .customer_support_customer_status import CustomerSupportCustomerStatus
from .email import Email
from .first_name import FirstName
from .last_name import LastName
from .phone_number import PhoneNumber


class CustomerSupportCustomer(UniversalBaseModel):
    addresses: typing.Optional[typing.List[Address]] = None
    bank_accounts: typing.Optional[BankAccount] = None
    company_name: typing.Optional[CompanyName] = None
    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the object was created.
    """

    created_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user who created the object.
    """

    currency: typing.Optional[Currency] = None
    emails: typing.Optional[typing.List[Email]] = None
    first_name: typing.Optional[FirstName] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for an object.
    """

    individual: typing.Optional[bool] = None
    last_name: typing.Optional[LastName] = None
    notes: typing.Optional[str] = None
    phone_numbers: typing.Optional[typing.List[PhoneNumber]] = None
    status: typing.Optional[CustomerSupportCustomerStatus] = pydantic.Field(default=None)
    """
    Customer status
    """

    tax_number: typing.Optional[str] = None
    updated_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time when the object was last updated.
    """

    updated_by: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user who last updated the object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
