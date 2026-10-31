

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job_summary import JobSummary


class JobListResponse(UniversalBaseModel):
    """
    Cursor-paginated page of job summaries for the authenticated tenant.
    """

    data: typing.List[JobSummary]
    next_cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Opaque cursor for the next page, or `null` when exhausted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
