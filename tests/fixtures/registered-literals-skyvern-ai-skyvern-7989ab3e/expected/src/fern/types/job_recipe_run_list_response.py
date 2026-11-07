

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job_recipe_run_summary import JobRecipeRunSummary


class JobRecipeRunListResponse(UniversalBaseModel):
    runs: typing.List[JobRecipeRunSummary]
    page: int
    page_size: int
    has_next: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
