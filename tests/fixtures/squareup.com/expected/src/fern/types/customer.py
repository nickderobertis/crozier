

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .card import Card
from .customer_preferences import CustomerPreferences


class Customer(UniversalBaseModel):
    """
    Represents a Square customer profile in the Customer Directory of a Square seller.
    """

    address: typing.Optional[Address] = None
    birthday: typing.Optional[str] = pydantic.Field(default=None)
    """
    The birthday associated with the customer profile, in RFC 3339 format. The year is optional. The timezone and time are not allowed.
    For example, `0000-09-21T00:00:00-00:00` represents a birthday on September 21 and `1998-09-21T00:00:00-00:00` represents a birthday on September 21, 1998.
    """

    cards: typing.Optional[typing.List[Card]] = pydantic.Field(default=None)
    """
    Payment details of the credit, debit, and gift cards stored on file for the customer profile. 
    
    DEPRECATED at version 2021-06-16. Replaced by calling [ListCards](https://developer.squareup.com/reference/square_2021-08-18/cards-api/list-cards) (for credit and debit cards on file) 
    or [ListGiftCards](https://developer.squareup.com/reference/square_2021-08-18/gift-cards-api/list-gift-cards) (for gift cards on file) and including the `customer_id` query parameter. 
    For more information, see [Migrate to the Cards API and Gift Cards API](https://developer.squareup.com/docs/customers-api/use-the-api/integrate-with-other-services#migrate-customer-cards).
    """

    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A business name associated with the customer profile.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the customer profile was created, in RFC 3339 format.
    """

    creation_source: typing.Optional[str] = pydantic.Field(default=None)
    """
    A creation source represents the method used to create the
    customer profile.
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address associated with the customer profile.
    """

    family_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The family (i.e., last) name associated with the customer profile.
    """

    given_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The given (i.e., first) name associated with the customer profile.
    """

    group_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The IDs of customer groups the customer belongs to.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique Square-assigned ID for the customer profile.
    """

    nickname: typing.Optional[str] = pydantic.Field(default=None)
    """
    A nickname for the customer profile.
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    A custom note associated with the customer profile.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The 11-digit phone number associated with the customer profile.
    """

    preferences: typing.Optional[CustomerPreferences] = None
    reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional second ID used to associate the customer profile with an
    entity in another system.
    """

    segment_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The IDs of segments the customer belongs to.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the customer profile was last updated, in RFC 3339 format.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Square-assigned version number of the customer profile. The version number is incremented each time an update is committed to the customer profile, except for changes to customer segment membership and cards on file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
