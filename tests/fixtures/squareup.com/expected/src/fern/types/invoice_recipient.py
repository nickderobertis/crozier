

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address


class InvoiceRecipient(UniversalBaseModel):
    """
    Provides customer data that Square uses to deliver an invoice.
    """

    address: typing.Optional[Address] = None
    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the recipient's company.
    """

    customer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the customer. This is the customer profile ID that 
    you provide when creating a draft invoice.
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The recipient's email address.
    """

    family_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The recipient's family (that is, last) name.
    """

    given_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The recipient's given (that is, first) name.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The recipient's phone number.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
