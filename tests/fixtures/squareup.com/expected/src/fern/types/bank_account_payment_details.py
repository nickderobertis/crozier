

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ach_details import AchDetails
from .error import Error


class BankAccountPaymentDetails(UniversalBaseModel):
    """
    Additional details about BANK_ACCOUNT type payments.
    """

    account_ownership_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ownership type of the bank account performing the transfer.
    The type can be `INDIVIDUAL`, `COMPANY`, or `UNKNOWN`.
    """

    ach_details: typing.Optional[AchDetails] = None
    bank_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the bank associated with the bank account.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The two-letter ISO code representing the country the bank account is located in.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    fingerprint: typing.Optional[str] = pydantic.Field(default=None)
    """
    Uniquely identifies the bank account for this seller and can be used
    to determine if payments are from the same bank account.
    """

    statement_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The statement description as sent to the bank.
    """

    transfer_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the bank transfer. The type can be `ACH` or `UNKNOWN`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
