

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_employer_verification import CreditEmployerVerification
from .credit_employment_employee_type import CreditEmploymentEmployeeType
from .credit_employment_verification_status import CreditEmploymentVerificationStatus
from .credit_platform_ids import CreditPlatformIds


class CreditEmploymentVerification(UniversalBaseModel):
    """
    The object containing proof of employment data for an individual.
    """

    account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the payroll provider account.
    """

    employee_type: typing.Optional[CreditEmploymentEmployeeType] = None
    employer: CreditEmployerVerification
    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    End of employment, if applicable. Provided in ISO 8601 format (YYY-MM-DD).
    """

    last_paystub_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date of the employee's most recent paystub in ISO 8601 format (YYYY-MM-DD).
    """

    platform_ids: CreditPlatformIds
    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Start of employment in ISO 8601 format (YYYY-MM-DD).
    """

    status: typing.Optional[CreditEmploymentVerificationStatus] = None
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Current title of employee.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
