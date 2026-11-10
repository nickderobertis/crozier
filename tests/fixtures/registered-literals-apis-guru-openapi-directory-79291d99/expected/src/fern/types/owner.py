

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .email import Email
from .phone_number import PhoneNumber


class Owner(UniversalBaseModel):
    """
    Data returned from the financial institution about the owner or owners of an account. Only the `names` array must be non-empty.
    """

    addresses: typing.List[Address] = pydantic.Field()
    """
    Data about the various addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution.
    """

    emails: typing.List[Email] = pydantic.Field()
    """
    A list of email addresses associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution.
    """

    names: typing.List[str] = pydantic.Field()
    """
    A list of names associated with the account by the financial institution. In the case of a joint account, Plaid will make a best effort to report the names of all account holders.
    
    If an Item contains multiple accounts with different owner names, some institutions will report all names associated with the Item in each account's `names` array.
    """

    phone_numbers: typing.List[PhoneNumber] = pydantic.Field()
    """
    A list of phone numbers associated with the account by the financial institution. May be an empty array if no relevant information is returned from the financial institution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
