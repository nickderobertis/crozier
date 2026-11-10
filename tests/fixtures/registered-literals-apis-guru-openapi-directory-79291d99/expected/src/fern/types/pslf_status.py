

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PslfStatus(UniversalBaseModel):
    """
    Information about the student's eligibility in the Public Service Loan Forgiveness program. This is only returned if the institution is FedLoan (`ins_116527`).
    """

    estimated_eligibility_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    The estimated date borrower will have completed 120 qualifying monthly payments. Returned in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).
    """

    payments_made: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of qualifying payments that have been made.
    """

    payments_remaining: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of qualifying payments remaining.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
