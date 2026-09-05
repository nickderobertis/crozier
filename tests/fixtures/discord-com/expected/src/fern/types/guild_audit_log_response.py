

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_command_response import ApplicationCommandResponse
from .audit_log_entry_response import AuditLogEntryResponse
from .guild_audit_log_response_auto_moderation_rules_item import GuildAuditLogResponseAutoModerationRulesItem
from .guild_audit_log_response_guild_scheduled_events_item import GuildAuditLogResponseGuildScheduledEventsItem
from .guild_audit_log_response_integrations_item import GuildAuditLogResponseIntegrationsItem
from .guild_audit_log_response_webhooks_item import GuildAuditLogResponseWebhooksItem
from .thread_response import ThreadResponse
from .user_response import UserResponse


class GuildAuditLogResponse(UniversalBaseModel):
    audit_log_entries: typing.List[AuditLogEntryResponse]
    users: typing.List[UserResponse]
    integrations: typing.List[GuildAuditLogResponseIntegrationsItem]
    webhooks: typing.List[GuildAuditLogResponseWebhooksItem]
    guild_scheduled_events: typing.List[GuildAuditLogResponseGuildScheduledEventsItem]
    threads: typing.List[ThreadResponse]
    application_commands: typing.List[ApplicationCommandResponse]
    auto_moderation_rules: typing.List[typing.Optional[GuildAuditLogResponseAutoModerationRulesItem]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
