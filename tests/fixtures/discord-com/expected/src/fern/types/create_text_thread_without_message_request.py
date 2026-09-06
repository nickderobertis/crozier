

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .thread_auto_archive_duration import ThreadAutoArchiveDuration


class CreateTextThreadWithoutMessageRequest(UniversalBaseModel):
    name: str
    auto_archive_duration: typing.Optional[ThreadAutoArchiveDuration] = None
    rate_limit_per_user: typing.Optional[int] = None
    type: typing.Optional[int] = None
    invitable: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
