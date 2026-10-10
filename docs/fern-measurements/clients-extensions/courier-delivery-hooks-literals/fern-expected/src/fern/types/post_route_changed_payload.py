

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_route_changed_payload_reason import PostRouteChangedPayloadReason


class PostRouteChangedPayload(UniversalBaseModel):
    route: typing.Optional[str] = None
    reason: typing.Optional[PostRouteChangedPayloadReason] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
