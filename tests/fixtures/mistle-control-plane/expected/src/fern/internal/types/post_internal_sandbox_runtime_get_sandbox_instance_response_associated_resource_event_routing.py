

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_internal_sandbox_runtime_get_sandbox_instance_response_associated_resource_event_routing_resources_item import (
    PostInternalSandboxRuntimeGetSandboxInstanceResponseAssociatedResourceEventRoutingResourcesItem,
)


class PostInternalSandboxRuntimeGetSandboxInstanceResponseAssociatedResourceEventRouting(UniversalBaseModel):
    enabled: bool
    resources: typing.List[
        PostInternalSandboxRuntimeGetSandboxInstanceResponseAssociatedResourceEventRoutingResourcesItem
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
