

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .computation_collection_run_task_rest_get import ComputationCollectionRunTaskRestGet


class PageComputationCollectionRunTaskRestGet(UniversalBaseModel):
    items: typing.List[ComputationCollectionRunTaskRestGet]
    total: int
    page: int
    size: int
    pages: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
