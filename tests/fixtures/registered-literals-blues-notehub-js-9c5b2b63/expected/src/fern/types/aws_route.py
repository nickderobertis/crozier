

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filter import Filter
from .route_transform_settings import RouteTransformSettings


class AwsRoute(UniversalBaseModel):
    access_key_id: typing.Optional[str] = None
    access_key_secret: typing.Optional[str] = None
    channel: typing.Optional[str] = None
    disable_http_headers: typing.Optional[bool] = None
    filter: typing.Optional[Filter] = None
    fleets: typing.Optional[typing.List[str]] = None
    http_headers: typing.Optional[typing.Dict[str, str]] = None
    message_deduplication_id: typing.Optional[str] = None
    message_group_id: typing.Optional[str] = None
    region: typing.Optional[str] = None
    role_arn: typing.Optional[str] = pydantic.Field(default=None)
    """
    IAM Role ARN for role-based authentication via STS AssumeRole
    """

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
