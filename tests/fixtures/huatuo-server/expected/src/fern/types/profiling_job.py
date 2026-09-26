

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .job import Job
from .profiling_language import ProfilingLanguage
from .profiling_mode import ProfilingMode
from .profiling_type import ProfilingType


class ProfilingJob(Job):
    binary_match_path: typing.Optional[str] = None
    language: ProfilingLanguage
    mode: ProfilingMode
    type: ProfilingType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
