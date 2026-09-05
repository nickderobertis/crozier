

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .snowflake_type import SnowflakeType
from .thread_auto_archive_duration import ThreadAutoArchiveDuration
from .video_quality_modes import VideoQualityModes


class UpdateThreadRequestPartial(UniversalBaseModel):
    name: typing.Optional[str] = None
    archived: typing.Optional[bool] = None
    locked: typing.Optional[bool] = None
    invitable: typing.Optional[bool] = None
    auto_archive_duration: typing.Optional[ThreadAutoArchiveDuration] = None
    rate_limit_per_user: typing.Optional[int] = None
    flags: typing.Optional[int] = None
    applied_tags: typing.Optional[typing.List[SnowflakeType]] = None
    bitrate: typing.Optional[int] = None
    user_limit: typing.Optional[int] = None
    rtc_region: typing.Optional[str] = None
    video_quality_mode: typing.Optional[VideoQualityModes] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
