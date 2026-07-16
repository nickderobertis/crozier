

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address


class OrderFulfillmentRecipient(UniversalBaseModel):
    """
    Contains information about the recipient of a fulfillment.
    """

    address: typing.Optional[Address] = None
    customer_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The customer ID of the customer associated with the fulfillment.
    
    If `customer_id` is provided, the fulfillment recipient's `display_name`,
    `email_address`, and `phone_number` are automatically populated from the
    targeted customer profile. If these fields are set in the request, the request
    values overrides the information from the customer profile. If the
    targeted customer profile does not contain the necessary information and
    these fields are left unset, the request results in an error.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The display name of the fulfillment recipient.
    
    If provided, the display name overrides the value pulled from the customer profile indicated by `customer_id`.
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address of the fulfillment recipient.
    
    If provided, the email address overrides the value pulled from the customer profile indicated by `customer_id`.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number of the fulfillment recipient.
    
    If provided, the phone number overrides the value pulled from the customer profile indicated by `customer_id`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
