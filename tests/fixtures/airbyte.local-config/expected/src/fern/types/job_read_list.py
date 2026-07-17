

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .job_with_attempts_read import JobWithAttemptsRead


class JobReadList(UniversalBaseModel):
    jobs: typing.List[JobWithAttemptsRead]
    total_job_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalJobCount"),
        pydantic.Field(alias="totalJobCount", description="the total count of jobs for the specified connection"),
    ]
    """
    the total count of jobs for the specified connection
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
