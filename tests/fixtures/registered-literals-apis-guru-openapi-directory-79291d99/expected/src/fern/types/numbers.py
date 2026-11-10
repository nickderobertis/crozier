

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Numbers(UniversalBaseModel):
    """
    Account and bank identifier number data used to configure the test account. All values are optional.
    """

    account: typing.Optional[str] = pydantic.Field(default=None)
    """
    Will be used for the account number.
    """

    ach_routing: typing.Optional[str] = pydantic.Field(default=None)
    """
    Must be a valid ACH routing number.
    """

    ach_wire_routing: typing.Optional[str] = pydantic.Field(default=None)
    """
    Must be a valid wire transfer routing number.
    """

    bacs_sort_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    BACS sort code
    """

    eft_branch: typing.Optional[str] = pydantic.Field(default=None)
    """
    EFT branch number. Must be specified alongside `eft_institution`.
    """

    eft_institution: typing.Optional[str] = pydantic.Field(default=None)
    """
    EFT institution number. Must be specified alongside `eft_branch`.
    """

    international_bic: typing.Optional[str] = pydantic.Field(default=None)
    """
    Bank identifier code (BIC). Must be specified alongside `international_iban`.
    """

    international_iban: typing.Optional[str] = pydantic.Field(default=None)
    """
    International bank account number (IBAN). If no account number is specified via `account`, will also be used as the account number by default. Must be specified alongside `international_bic`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
