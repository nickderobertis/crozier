

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .link_token_create_request_user_name import LinkTokenCreateRequestUserName
from .user_address import UserAddress
from .user_id_number import UserIdNumber


class LinkTokenCreateRequestUser(UniversalBaseModel):
    """
    An object specifying information about the end user who will be linking their account.
    """

    address: typing.Optional[UserAddress] = None
    client_user_id: str = pydantic.Field()
    """
    A unique ID representing the end user. Typically this will be a user ID number from your application. Personally identifiable information, such as an email address or phone number, should not be used in the `client_user_id`. It is currently used as a means of searching logs for the given user in the Plaid Dashboard.
    """

    date_of_birth: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    To be provided in the format "yyyy-mm-dd". Not currently used.
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's email address. This field is optional, but required to enable the [pre-authenticated returning user flow](https://plaid.com/docs/link/returning-user/#pre-authenticated-rux).
    """

    email_address_verified_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the email address was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDThh:mm:ssZ`). This was previously an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user). This field is no longer required to enable the returning user experience.
    
     Only pass a verification time for an email address that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.
    
     Example: `2020-01-01T00:00:00Z`
    """

    id_number: typing.Optional[UserIdNumber] = None
    legal_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's full legal name, used for [micro-deposit based verification flows](https://plaid.com/docs/auth/coverage/). For a small number of customers on legacy flows, providing this field is required to enable micro-deposit-based flows. For all other customers, this field is optional, but providing the user's name in this field when using micro-deposit-based verification will enable certain risk checks and can reduce micro-deposit fraud.
    """

    name: typing.Optional[LinkTokenCreateRequestUserName] = pydantic.Field(default=None)
    """
    The user's full name. Optional if using the [Identity Verification](https://plaid.com/docs/api/products/identity-verification) product; if not using Identity Verification, this field is not allowed. Users will not be asked for their name when this field is provided.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The user's phone number in [E.164](https://en.wikipedia.org/wiki/E.164) format. This field is optional, but required to enable the [returning user experience](https://plaid.com/docs/link/returning-user).
    """

    phone_number_verified_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time the phone number was verified in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (`YYYY-MM-DDThh:mm:ssZ`). This was previously an optional field used in the [returning user experience](https://plaid.com/docs/link/returning-user). This field is no longer required to enable the returning user experience.
    
     Only pass a verification time for a phone number that you have verified. If you have performed verification but don’t have the time, you may supply a signal value of the start of the UNIX epoch.
    
     Example: `2020-01-01T00:00:00Z`
    """

    ssn: typing.Optional[str] = pydantic.Field(default=None)
    """
    To be provided in the format "ddd-dd-dddd". Not currently used.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
