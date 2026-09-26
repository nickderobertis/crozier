

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_internal_sandbox_runtime_compile_plan_response_runtime_plan_associated_resource_event_routing_resources_item import (
    PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAssociatedResourceEventRoutingResourcesItem,
)


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAssociatedResourceEventRouting(UniversalBaseModel):
    enabled: bool
    resources: typing.List[
        PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanAssociatedResourceEventRoutingResourcesItem
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
