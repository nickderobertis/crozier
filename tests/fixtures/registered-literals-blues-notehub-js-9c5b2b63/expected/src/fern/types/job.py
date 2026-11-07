

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Job(UniversalBaseModel):
    created: int = pydantic.Field()
    """
    Unix timestamp when job was created
    """

    created_by: str = pydantic.Field()
    """
    User who created the job
    """

    job_uid: str = pydantic.Field()
    """
    Unique identifier for the job
    """

    last_run_completed: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp when the most recent run completed (0 if still in progress)
    """

    last_run_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Status of the most recent job run. Terminal values are: "submitted", "completed successfully", "dry run completed successfully", "completed with errors", "cancelled". While a job is running, intermediate per-device progress updates may appear (e.g. "dev:000000000000000 completed", "dev:000000000000000 updated: ...").
    """

    last_run_submitted: typing.Optional[int] = pydantic.Field(default=None)
    """
    Unix timestamp when the most recent run was submitted
    """

    name: str = pydantic.Field()
    """
    Human-readable job name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
