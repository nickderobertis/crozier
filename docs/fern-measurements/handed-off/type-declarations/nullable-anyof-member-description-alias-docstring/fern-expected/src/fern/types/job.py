

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_stopped import JobStopped


class Job(UniversalBaseModel):
    job_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="jobId"), pydantic.Field(alias="jobId")
    ] = None
    stopped: typing.Optional[JobStopped] = pydantic.Field(default=None)
    """
    Why the job stopped.
    """

    stopped_at: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="stoppedAt"),
        pydantic.Field(alias="stoppedAt", description="When the job stopped, in epoch seconds."),
    ] = None
    """
    When the job stopped, in epoch seconds.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
