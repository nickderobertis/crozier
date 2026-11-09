

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .job import Job
from .job_definition import JobDefinition


class JobDetail(Job):
    """
    Batch job with full definition
    """

    definition: typing.Optional[JobDefinition] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
