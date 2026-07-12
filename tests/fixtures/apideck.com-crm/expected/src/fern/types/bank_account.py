

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .bank_account_account_type import BankAccountAccountType
from .currency import Currency


class BankAccount(UniversalBaseModel):
    account_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name which you used in opening your bank account.
    """

    account_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    A bank account number is a number that is tied to your bank account. If you have several bank accounts, such as personal, joint, business (and so on), each account will have a different account number.
    """

    account_type: typing.Optional[BankAccountAccountType] = pydantic.Field(default=None)
    """
    The type of bank account.
    """

    bank_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    A bank code is a code assigned by a central bank, a bank supervisory body or a Bankers Association in a country to all its licensed member banks or financial institutions.
    """

    bic: typing.Optional[str] = None
    branch_identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    A branch identifier is a unique identifier for a branch of a bank or financial institution.
    """

    bsb_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    A BSB is a 6 digit numeric code used for identifying the branch of an Australian or New Zealand bank or financial institution.
    """

    currency: typing.Optional[Currency] = None
    iban: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
