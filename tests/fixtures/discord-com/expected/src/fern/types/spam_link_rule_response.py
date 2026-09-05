

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .automod_event_type import AutomodEventType
from .snowflake_type import SnowflakeType
from .spam_link_rule_response_actions_item import SpamLinkRuleResponseActionsItem
from .spam_link_trigger_metadata_response import SpamLinkTriggerMetadataResponse


class SpamLinkRuleResponse(UniversalBaseModel):
    id: SnowflakeType
    guild_id: SnowflakeType
    creator_id: SnowflakeType
    name: str
    event_type: AutomodEventType
    actions: typing.List[SpamLinkRuleResponseActionsItem]
    trigger_type: int
    enabled: typing.Optional[bool] = None
    exempt_roles: typing.Optional[typing.List[SnowflakeType]] = None
    exempt_channels: typing.Optional[typing.List[SnowflakeType]] = None
    trigger_metadata: SpamLinkTriggerMetadataResponse

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
