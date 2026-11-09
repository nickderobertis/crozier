

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .employer_verification import EmployerVerification
from .employment_verification_status import EmploymentVerificationStatus
from .platform_ids import PlatformIds


class EmploymentVerification(UniversalBaseModel):
    """
    An object containing proof of employment data for an individual
    """

    employer: typing.Optional[EmployerVerification] = None
    end_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    End of employment, if applicable. Provided in ISO 8601 format (YYY-MM-DD).
    """

    platform_ids: typing.Optional[PlatformIds] = None
    start_date: typing.Optional[dt.date] = pydantic.Field(default=None)
    """
    Start of employment in ISO 8601 format (YYYY-MM-DD).
    """

    status: typing.Optional[EmploymentVerificationStatus] = None
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
