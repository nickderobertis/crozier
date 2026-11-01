

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workflows_include_filter_items_relation import WorkflowsIncludeFilterItemsRelation
from .workflows_scope_filter import WorkflowsScopeFilter


class WorkflowsIncludeFilterItems(UniversalBaseModel):
    relation: typing.Optional[WorkflowsIncludeFilterItemsRelation] = None
    scope: typing.Optional[WorkflowsScopeFilter] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
