

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .business_hours import BusinessHours
from .coordinates import Coordinates
from .tax_ids import TaxIds


class Location(UniversalBaseModel):
    """ """

    address: typing.Optional[Address] = None
    business_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email of the location.
    This email is visible to the customers of the location.
    For example, the email appears on customer receipts. 
    For example, `help&#64;squareup.com`.
    """

    business_hours: typing.Optional[BusinessHours] = None
    business_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The business name of the location
    This is the name visible to the customers of the location.
    For example, this name appears on customer receipts.
    """

    capabilities: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The Square features that are enabled for the location.
    See [LocationCapability](https://developer.squareup.com/reference/square_2021-08-18/enums/LocationCapability) for possible values.
    """

    coordinates: typing.Optional[Coordinates] = None
    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country of the location, in ISO 3166-1-alpha-2 format.
    
    See [Country](https://developer.squareup.com/reference/square_2021-08-18/enums/Country) for possible values.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the location was created, in RFC 3339 format.
    For more information, see [Working with Dates](https://developer.squareup.com/docs/build-basics/working-with-dates).
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The currency used for all transactions at this location,
    in ISO 4217 format.
    See [Currency](https://developer.squareup.com/reference/square_2021-08-18/enums/Currency) for possible values.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the location.
    """

    facebook_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Facebook profile URL of the location. The URL should begin with 'facebook.com/'. For example, `https://www.facebook.com/square`.
    """

    full_format_logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of a full-format logo image for the location. The Seller must choose this logo in the
    Seller dashboard (Receipts section) for the logo to appear on transactions (such as receipts, invoices)
    that Square generates on behalf of the Seller. This image can have an aspect ratio of 2:1 or greater
    and is recommended to be at least 1280x648 pixels.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-issued ID of the location.
    """

    instagram_username: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Instagram username of the location without the '&#64;' symbol. For example, `square`.
    """

    language_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The language associated with the location, in
    [BCP 47 format](https://tools.ietf.org/html/bcp47#appendix-A). 
    For more information, see [Location language code](https://developer.squareup.com/docs/locations-api#location-language-code).
    """

    logo_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the logo image for the location. The Seller must choose this logo in the Seller
    dashboard (Receipts section) for the logo to appear on transactions (such as receipts, invoices)
    that Square generates on behalf of the Seller. This image should have an aspect ratio
    close to 1:1 and is recommended to be at least 200x200 pixels.
    """

    mcc: typing.Optional[str] = pydantic.Field(default=None)
    """
    The merchant category code (MCC) of the location, as standardized by ISO 18245.
    The MCC describes the kind of goods or services sold at the location.
    """

    merchant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the merchant that owns the location.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the location.
    This information appears in the dashboard as the nickname.
    A location name must be unique within a seller account.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number of the location in human readable format. For example, `+353 80 0 098 8099`.
    """

    pos_background_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the Point of Sale background image for the location.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the location, either active or inactive.
    """

    tax_ids: typing.Optional[TaxIds] = None
    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [IANA Timezone](https://www.iana.org/time-zones) identifier for
    the timezone of the location.
    """

    twitter_username: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Twitter username of the location without the '&#64;' symbol. For example, `Square`.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the location, either physical or mobile.
    """

    website_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The website URL of the location.  For example, `https://squareup.com`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
