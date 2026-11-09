

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .numbers_ach import NumbersAch
from .numbers_bacs import NumbersBacs
from .numbers_eft import NumbersEft
from .numbers_international import NumbersInternational


class AuthGetNumbers(UniversalBaseModel):
    """
    An object containing identifying numbers used for making electronic transfers to and from the `accounts`. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by any `accounts` for which data has been requested, the array for that type will be empty.
    """

    ach: typing.List[NumbersAch] = pydantic.Field()
    """
    An array of ACH numbers identifying accounts.
    """

    bacs: typing.List[NumbersBacs] = pydantic.Field()
    """
    An array of BACS numbers identifying accounts.
    """

    eft: typing.List[NumbersEft] = pydantic.Field()
    """
    An array of EFT numbers identifying accounts.
    """

    international: typing.List[NumbersInternational] = pydantic.Field()
    """
    An array of IBAN numbers identifying accounts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
