

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payroll_item import PayrollItem


class PayrollData(UniversalBaseModel):
    """
    Payroll Data.
    """

    hours: typing.Optional[typing.List[PayrollItem]] = None
    hours_no_pto: typing.Optional[typing.List[PayrollItem]] = None
    rates: typing.Optional[typing.List[PayrollItem]] = None
    amount: typing.Optional[typing.List[PayrollItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
