

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Benefit(UniversalBaseModel):
    employee_deduction: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount deducted for benefit.
    """

    employer_contribution: typing.Optional[float] = pydantic.Field(default=None)
    """
    The amount of employer contribution.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the benefit.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
