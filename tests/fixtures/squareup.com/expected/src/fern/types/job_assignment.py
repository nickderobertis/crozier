

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class JobAssignment(UniversalBaseModel):
    """
    An object describing a job that a team member is assigned to.
    """

    annual_rate: typing.Optional[Money] = None
    hourly_rate: typing.Optional[Money] = None
    job_title: str = pydantic.Field()
    """
    The title of the job.
    """

    pay_type: str = pydantic.Field()
    """
    The current pay type for the job assignment used to
    calculate the pay amount in a pay period.
    """

    weekly_hours: typing.Optional[int] = pydantic.Field(default=None)
    """
    The planned hours per week for the job. Set if the job `PayType` is `SALARY`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
