

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .base_create_message_create_request import BaseCreateMessageCreateRequest
from .snowflake_type import SnowflakeType
from .thread_auto_archive_duration import ThreadAutoArchiveDuration


class CreateForumThreadRequest(UniversalBaseModel):
    name: str
    auto_archive_duration: typing.Optional[ThreadAutoArchiveDuration] = None
    rate_limit_per_user: typing.Optional[int] = None
    applied_tags: typing.Optional[typing.List[SnowflakeType]] = None
    message: BaseCreateMessageCreateRequest

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
