

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .numbers_ach_nullable import NumbersAchNullable
from .numbers_bacs_nullable import NumbersBacsNullable
from .numbers_eft_nullable import NumbersEftNullable
from .numbers_international_nullable import NumbersInternationalNullable


class ProcessorNumber(UniversalBaseModel):
    """
    An object containing identifying numbers used for making electronic transfers to and from the `account`. The identifying number type (ACH, EFT, IBAN, or BACS) used will depend on the country of the account. An account may have more than one number type. If a particular identifying number type is not used by the `account` for which auth data has been requested, a null value will be returned.
    """

    ach: typing.Optional[NumbersAchNullable] = None
    bacs: typing.Optional[NumbersBacsNullable] = None
    eft: typing.Optional[NumbersEftNullable] = None
    international: typing.Optional[NumbersInternationalNullable] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
