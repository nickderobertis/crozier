

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filter import Filter
from .route_transform_settings import RouteTransformSettings


class MqttRoute(UniversalBaseModel):
    broker: typing.Optional[str] = None
    certificate: typing.Optional[str] = None
    certificate_name: typing.Optional[str] = None
    client_id: typing.Optional[str] = None
    filter: typing.Optional[Filter] = None
    fleets: typing.Optional[typing.List[str]] = None
    key: typing.Optional[str] = None
    password: typing.Optional[str] = None
    port: typing.Optional[str] = None
    private_key_name: typing.Optional[str] = None
    throttle_ms: typing.Optional[int] = None
    timeout: typing.Optional[int] = None
    topic: typing.Optional[str] = None
    transform: typing.Optional[RouteTransformSettings] = None
    username: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
