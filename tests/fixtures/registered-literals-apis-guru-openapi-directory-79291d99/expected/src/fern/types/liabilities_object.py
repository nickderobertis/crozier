

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_card_liability import CreditCardLiability
from .mortgage_liability import MortgageLiability
from .student_loan import StudentLoan


class LiabilitiesObject(UniversalBaseModel):
    """
    An object containing liability accounts
    """

    credit: typing.Optional[typing.List[CreditCardLiability]] = pydantic.Field(default=None)
    """
    The credit accounts returned.
    """

    mortgage: typing.Optional[typing.List[MortgageLiability]] = pydantic.Field(default=None)
    """
    The mortgage accounts returned.
    """

    student: typing.Optional[typing.List[StudentLoan]] = pydantic.Field(default=None)
    """
    The student loan accounts returned.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
