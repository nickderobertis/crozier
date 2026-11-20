

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job_summary import JobSummary


class Jobs(UniversalBaseModel):
    """
    The jobs the caller may see (governed by the datasets each wrote).
    """

    jobs: typing.List[JobSummary]
    total: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
