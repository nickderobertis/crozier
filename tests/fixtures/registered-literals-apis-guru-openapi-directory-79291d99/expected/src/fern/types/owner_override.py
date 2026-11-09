

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .address import Address
from .email import Email
from .phone_number import PhoneNumber


class OwnerOverride(UniversalBaseModel):
    """
    Data about the owner or owners of an account. Any fields not specified will be filled in with default Sandbox information.
    """

    addresses: typing.List[Address] = pydantic.Field()
    """
    Data about the various addresses associated with the account.
    """

    emails: typing.List[Email] = pydantic.Field()
    """
    A list of email addresses associated with the account.
    """

    names: typing.List[str] = pydantic.Field()
    """
    A list of names associated with the account by the financial institution. These should always be the names of individuals, even for business accounts. Note that the same name data will be used for all accounts associated with an Item.
    """

    phone_numbers: typing.List[PhoneNumber] = pydantic.Field()
    """
    A list of phone numbers associated with the account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
