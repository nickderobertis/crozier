

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .filter import Filter
from .route_transform_settings import RouteTransformSettings


class S3ArchiveRoute(UniversalBaseModel):
    archive_count_exceeds: typing.Optional[int] = None
    archive_every_mins: typing.Optional[int] = None
    archive_id: typing.Optional[str] = None
    bucket_endpoint: typing.Optional[str] = None
    bucket_name: typing.Optional[str] = None
    bucket_region: typing.Optional[str] = None
    file_access: typing.Optional[str] = None
    file_folder: typing.Optional[str] = None
    file_format: typing.Optional[str] = None
    filter: typing.Optional[Filter] = None
    fleets: typing.Optional[typing.List[str]] = None
    key_id: typing.Optional[str] = None
    key_secret: typing.Optional[str] = None
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
