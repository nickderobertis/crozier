

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class JobRun(UniversalBaseModel):
    cancel: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether cancellation was requested
    """

    completed: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp when completed
    """

    dry_run: bool = pydantic.Field()
    """
    Whether this was a dry run
    """

    job_name: str = pydantic.Field()
    """
    Name of the job
    """

    job_uid: str = pydantic.Field()
    """
    Unique identifier for the job
    """

    report_uid: str = pydantic.Field()
    """
    Unique identifier for this run
    """

    results: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Full results (only in detail view)
    """

    started: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp when started
    """

    status: str = pydantic.Field()
    """
    Current status (submitted, running, completed, cancelled, failed)
    """

    submitted: int = pydantic.Field()
    """
    Unix timestamp when submitted
    """

    submitted_by: str = pydantic.Field()
    """
    User who submitted the run
    """

    updated: int = pydantic.Field()
    """
    Unix timestamp of last update
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
