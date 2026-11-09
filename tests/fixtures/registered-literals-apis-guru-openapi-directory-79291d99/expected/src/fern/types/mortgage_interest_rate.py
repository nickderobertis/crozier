

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MortgageInterestRate(UniversalBaseModel):
    """
    Object containing metadata about the interest rate for the mortgage.
    """

    percentage: typing.Optional[float] = pydantic.Field(default=None)
    """
    Percentage value (interest rate of current mortgage, not APR) of interest payable on a loan.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of interest charged (fixed or variable).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
