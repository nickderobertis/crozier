

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .student_loan_status_type import StudentLoanStatusType


class StudentLoanStatus(UniversalBaseModel):
    """
    An object representing the status of the student loan
    """

    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The date until which the loan will be in its current status. Dates are returned in an [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    type: typing.Optional[StudentLoanStatusType] = pydantic.Field(default=None)
    """
    The status type of the student loan
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
