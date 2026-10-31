

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .workflows_scope_filter_fields import WorkflowsScopeFilterFields
from .workflows_scope_filter_order import WorkflowsScopeFilterOrder


class WorkflowsScopeFilter(UniversalBaseModel):
    offset: typing.Optional[int] = None
    limit: typing.Optional[int] = None
    skip: typing.Optional[int] = None
    order: typing.Optional[WorkflowsScopeFilterOrder] = None
    where: typing.Optional[typing.Dict[str, typing.Any]] = None
    fields: typing.Optional[WorkflowsScopeFilterFields] = None
    include: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
