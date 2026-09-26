

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .payroll_period import PayrollPeriod


class Payroll(UniversalBaseModel):
    """
    Payroll.
    """

    gusto_company_id: str
    company_id: str = pydantic.Field()
    """
    Company id.
    """

    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_name: str
    data: typing.Optional[typing.List[PayrollPeriod]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
