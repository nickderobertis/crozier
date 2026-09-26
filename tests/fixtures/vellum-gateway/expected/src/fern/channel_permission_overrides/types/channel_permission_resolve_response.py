

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_permission_resolve_response_resolved import ChannelPermissionResolveResponseResolved


class ChannelPermissionResolveResponse(UniversalBaseModel):
    resolved: typing.Optional[ChannelPermissionResolveResponseResolved] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
