

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .automod_event_type import AutomodEventType
from .mention_spam_trigger_metadata import MentionSpamTriggerMetadata
from .mention_spam_upsert_request_partial_actions_item import MentionSpamUpsertRequestPartialActionsItem
from .snowflake_type import SnowflakeType


class MentionSpamUpsertRequestPartial(UniversalBaseModel):
    name: typing.Optional[str] = None
    event_type: typing.Optional[AutomodEventType] = None
    actions: typing.Optional[typing.List[MentionSpamUpsertRequestPartialActionsItem]] = None
    enabled: typing.Optional[bool] = None
    exempt_roles: typing.Optional[typing.List[SnowflakeType]] = None
    exempt_channels: typing.Optional[typing.List[SnowflakeType]] = None
    trigger_type: typing.Optional[int] = None
    trigger_metadata: typing.Optional[MentionSpamTriggerMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
