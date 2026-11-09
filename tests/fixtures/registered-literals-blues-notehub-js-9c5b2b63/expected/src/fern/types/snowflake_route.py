

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filter import Filter
from .route_transform_settings import RouteTransformSettings


class SnowflakeRoute(UniversalBaseModel):
    account_name: typing.Optional[str] = None
    filter: typing.Optional[Filter] = None
    fleets: typing.Optional[typing.List[str]] = None
    organization_name: typing.Optional[str] = None
    pem: typing.Optional[str] = None
    private_key_name: typing.Optional[str] = None
    timeout: typing.Optional[int] = None
    transform: typing.Optional[RouteTransformSettings] = None
    user_name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
