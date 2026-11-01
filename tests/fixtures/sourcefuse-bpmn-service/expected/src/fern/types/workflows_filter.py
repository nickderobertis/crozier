

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workflows_filter_fields import WorkflowsFilterFields
from .workflows_filter_include_item import WorkflowsFilterIncludeItem
from .workflows_filter_order import WorkflowsFilterOrder


class WorkflowsFilter(UniversalBaseModel):
    offset: typing.Optional[int] = None
    limit: typing.Optional[int] = None
    skip: typing.Optional[int] = None
    order: typing.Optional[WorkflowsFilterOrder] = None
    where: typing.Optional[typing.Dict[str, typing.Any]] = None
    fields: typing.Optional[WorkflowsFilterFields] = None
    include: typing.Optional[typing.List[WorkflowsFilterIncludeItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
