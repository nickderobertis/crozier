

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .company_id import CompanyId
from .compensation import Compensation
from .id import Id
from .payroll_totals import PayrollTotals


class Payroll(UniversalBaseModel):
    check_date: str = pydantic.Field()
    """
    The date on which employees will be paid for the payroll.
    """

    company_id: typing.Optional[CompanyId] = None
    compensations: typing.Optional[typing.List[Compensation]] = pydantic.Field(default=None)
    """
    An array of compensations for the payroll.
    """

    end_date: str = pydantic.Field()
    """
    The end date, inclusive, of the pay period.
    """

    id: typing.Optional[Id] = None
    processed: bool = pydantic.Field()
    """
    Whether or not the payroll has been successfully processed. Note that processed payrolls cannot be updated.
    """

    processed_date: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date the payroll was processed.
    """

    start_date: str = pydantic.Field()
    """
    The start date, inclusive, of the pay period.
    """

    totals: typing.Optional[PayrollTotals] = pydantic.Field(default=None)
    """
    The overview of the payroll totals.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
