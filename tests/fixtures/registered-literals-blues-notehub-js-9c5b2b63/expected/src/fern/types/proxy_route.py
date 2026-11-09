

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .route_transform_settings import RouteTransformSettings


class ProxyRoute(UniversalBaseModel):
    alias: typing.Optional[str] = None
    fleets: typing.Optional[typing.List[str]] = None
    http_headers: typing.Optional[typing.Dict[str, str]] = None
    timeout: typing.Optional[int] = None
    transform: typing.Optional[RouteTransformSettings] = None
    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
