

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .job_recipe_run_summary_recipe import JobRecipeRunSummaryRecipe


class JobRecipeRunSummary(UniversalBaseModel):
    workflow_run_id: str
    workflow_permanent_id: str
    recipe: JobRecipeRunSummaryRecipe
    status: str
    created_at: dt.datetime
    job_url: typing.Optional[str] = None
    failure_reason: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
