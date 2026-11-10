

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .numbers_iban import NumbersIban


class NumbersInternationalIban(UniversalBaseModel):
    """
    Account numbers using the International Bank Account Number and BIC/SWIFT code format.
    """

    bic: str = pydantic.Field()
    """
    The Business Identifier Code, also known as SWIFT code, for this bank account.
    """

    iban: NumbersIban

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
