

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payroll_employee import PayrollEmployee


class PayrollPeriod(UniversalBaseModel):
    """
    Payroll Period.
    """

    period: str
    employees: typing.Optional[typing.List[PayrollEmployee]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
