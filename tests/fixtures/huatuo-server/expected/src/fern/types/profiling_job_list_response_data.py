

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .profiling_job import ProfilingJob


class ProfilingJobListResponseData(UniversalBaseModel):
    has_more: bool
    items: typing.List[ProfilingJob]
    limit: int
    offset: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
