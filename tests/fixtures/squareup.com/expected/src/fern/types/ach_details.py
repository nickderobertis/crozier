

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AchDetails(UniversalBaseModel):
    """
    ACH-specific details about `BANK_ACCOUNT` type payments with the `transfer_type` of `ACH`.
    """

    account_number_suffix: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last few digits of the bank account number.
    """

    account_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the bank account performing the transfer. The account type can be `CHECKING`,
    `SAVINGS`, or `UNKNOWN`.
    """

    routing_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The routing number for the bank account.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
