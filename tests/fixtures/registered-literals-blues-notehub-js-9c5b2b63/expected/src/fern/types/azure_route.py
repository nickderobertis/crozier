

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filter import Filter
from .route_transform_settings import RouteTransformSettings


class AzureRoute(UniversalBaseModel):
    filter: typing.Optional[Filter] = None
    fleets: typing.Optional[typing.List[str]] = None
    functions_key_secret: typing.Optional[str] = None
    sas_policy_key: typing.Optional[str] = None
    sas_policy_name: typing.Optional[str] = None
    throttle_ms: typing.Optional[int] = None
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
