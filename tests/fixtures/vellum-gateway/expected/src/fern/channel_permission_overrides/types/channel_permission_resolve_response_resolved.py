

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_permission_resolve_response_resolved_scope import ChannelPermissionResolveResponseResolvedScope
from .channel_permission_resolve_response_resolved_threshold import ChannelPermissionResolveResponseResolvedThreshold


class ChannelPermissionResolveResponseResolved(UniversalBaseModel):
    threshold: ChannelPermissionResolveResponseResolvedThreshold
    scope: ChannelPermissionResolveResponseResolvedScope

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
