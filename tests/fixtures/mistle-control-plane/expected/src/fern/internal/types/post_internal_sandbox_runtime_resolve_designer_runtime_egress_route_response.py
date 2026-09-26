

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_internal_sandbox_runtime_resolve_designer_runtime_egress_route_response_route import (
    PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRoute,
)


class PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponse(UniversalBaseModel):
    route: PostInternalSandboxRuntimeResolveDesignerRuntimeEgressRouteResponseRoute

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
