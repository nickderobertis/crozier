

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job import Job
from .next_cursor import NextCursor
from .retry_budget import RetryBudget


class JobPage(UniversalBaseModel):
    next: typing.Optional[NextCursor] = None
    budget: typing.Optional[RetryBudget] = None
    jobs: typing.Optional[typing.List[Job]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
