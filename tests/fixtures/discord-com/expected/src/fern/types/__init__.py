



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .account_response import AccountResponse
    from .action_row_component_for_message_request import ActionRowComponentForMessageRequest
    from .action_row_component_for_message_request_components_item import (
        ActionRowComponentForMessageRequestComponentsItem,
    )
    from .action_row_component_for_modal_request import ActionRowComponentForModalRequest
    from .action_row_component_response import ActionRowComponentResponse
    from .action_row_component_response_components_item import ActionRowComponentResponseComponentsItem
    from .activities_attachment_response import ActivitiesAttachmentResponse
    from .add_group_dm_user_response import AddGroupDmUserResponse
    from .afk_timeouts import AfkTimeouts
    from .allowed_mention_types import AllowedMentionTypes
    from .application_command_attachment_option import ApplicationCommandAttachmentOption
    from .application_command_attachment_option_response import ApplicationCommandAttachmentOptionResponse
    from .application_command_autocomplete_callback_request import ApplicationCommandAutocompleteCallbackRequest
    from .application_command_autocomplete_callback_request_data import (
        ApplicationCommandAutocompleteCallbackRequestData,
    )
    from .application_command_boolean_option import ApplicationCommandBooleanOption
    from .application_command_boolean_option_response import ApplicationCommandBooleanOptionResponse
    from .application_command_channel_option import ApplicationCommandChannelOption
    from .application_command_channel_option_response import ApplicationCommandChannelOptionResponse
    from .application_command_create_request import ApplicationCommandCreateRequest
    from .application_command_create_request_options_item import ApplicationCommandCreateRequestOptionsItem
    from .application_command_handler import ApplicationCommandHandler
    from .application_command_integer_option import ApplicationCommandIntegerOption
    from .application_command_integer_option_response import ApplicationCommandIntegerOptionResponse
    from .application_command_interaction_metadata_response import ApplicationCommandInteractionMetadataResponse
    from .application_command_mentionable_option import ApplicationCommandMentionableOption
    from .application_command_mentionable_option_response import ApplicationCommandMentionableOptionResponse
    from .application_command_number_option import ApplicationCommandNumberOption
    from .application_command_number_option_response import ApplicationCommandNumberOptionResponse
    from .application_command_option_integer_choice import ApplicationCommandOptionIntegerChoice
    from .application_command_option_integer_choice_response import ApplicationCommandOptionIntegerChoiceResponse
    from .application_command_option_number_choice import ApplicationCommandOptionNumberChoice
    from .application_command_option_number_choice_response import ApplicationCommandOptionNumberChoiceResponse
    from .application_command_option_string_choice import ApplicationCommandOptionStringChoice
    from .application_command_option_string_choice_response import ApplicationCommandOptionStringChoiceResponse
    from .application_command_option_type import ApplicationCommandOptionType
    from .application_command_patch_request_partial import ApplicationCommandPatchRequestPartial
    from .application_command_patch_request_partial_options_item import ApplicationCommandPatchRequestPartialOptionsItem
    from .application_command_permission import ApplicationCommandPermission
    from .application_command_permission_type import ApplicationCommandPermissionType
    from .application_command_response import ApplicationCommandResponse
    from .application_command_response_options_item import ApplicationCommandResponseOptionsItem
    from .application_command_role_option import ApplicationCommandRoleOption
    from .application_command_role_option_response import ApplicationCommandRoleOptionResponse
    from .application_command_string_option import ApplicationCommandStringOption
    from .application_command_string_option_response import ApplicationCommandStringOptionResponse
    from .application_command_subcommand_group_option import ApplicationCommandSubcommandGroupOption
    from .application_command_subcommand_group_option_response import ApplicationCommandSubcommandGroupOptionResponse
    from .application_command_subcommand_option import ApplicationCommandSubcommandOption
    from .application_command_subcommand_option_options_item import ApplicationCommandSubcommandOptionOptionsItem
    from .application_command_subcommand_option_response import ApplicationCommandSubcommandOptionResponse
    from .application_command_subcommand_option_response_options_item import (
        ApplicationCommandSubcommandOptionResponseOptionsItem,
    )
    from .application_command_type import ApplicationCommandType
    from .application_command_update_request import ApplicationCommandUpdateRequest
    from .application_command_update_request_options_item import ApplicationCommandUpdateRequestOptionsItem
    from .application_command_user_option import ApplicationCommandUserOption
    from .application_command_user_option_response import ApplicationCommandUserOptionResponse
    from .application_explicit_content_filter_types import ApplicationExplicitContentFilterTypes
    from .application_form_partial import ApplicationFormPartial
    from .application_form_partial_description import ApplicationFormPartialDescription
    from .application_identity_provider_auth_type import ApplicationIdentityProviderAuthType
    from .application_incoming_webhook_response import ApplicationIncomingWebhookResponse
    from .application_integration_type import ApplicationIntegrationType
    from .application_integration_type_configuration import ApplicationIntegrationTypeConfiguration
    from .application_integration_type_configuration_response import ApplicationIntegrationTypeConfigurationResponse
    from .application_o_auth2install_params import ApplicationOAuth2InstallParams
    from .application_o_auth2install_params_response import ApplicationOAuth2InstallParamsResponse
    from .application_o_auth2install_params_response_scopes_item import ApplicationOAuth2InstallParamsResponseScopesItem
    from .application_o_auth2install_params_scopes_item import ApplicationOAuth2InstallParamsScopesItem
    from .application_response import ApplicationResponse
    from .application_role_connections_metadata_item_request import ApplicationRoleConnectionsMetadataItemRequest
    from .application_role_connections_metadata_item_response import ApplicationRoleConnectionsMetadataItemResponse
    from .application_types import ApplicationTypes
    from .application_user_role_connection_response import ApplicationUserRoleConnectionResponse
    from .attachment_response import AttachmentResponse
    from .audit_log_action_types import AuditLogActionTypes
    from .audit_log_entry_response import AuditLogEntryResponse
    from .audit_log_object_change_response import AuditLogObjectChangeResponse
    from .automod_action_type import AutomodActionType
    from .automod_event_type import AutomodEventType
    from .automod_keyword_preset_type import AutomodKeywordPresetType
    from .automod_trigger_type import AutomodTriggerType
    from .available_locales_enum import AvailableLocalesEnum
    from .base_create_message_create_request import BaseCreateMessageCreateRequest
    from .basic_application_response import BasicApplicationResponse
    from .basic_message_response import BasicMessageResponse
    from .basic_message_response_interaction_metadata import BasicMessageResponseInteractionMetadata
    from .basic_message_response_nonce import BasicMessageResponseNonce
    from .basic_message_response_stickers_item import BasicMessageResponseStickersItem
    from .block_message_action import BlockMessageAction
    from .block_message_action_metadata import BlockMessageActionMetadata
    from .block_message_action_metadata_response import BlockMessageActionMetadataResponse
    from .block_message_action_response import BlockMessageActionResponse
    from .bulk_ban_users_response import BulkBanUsersResponse
    from .bulk_update_guild_channels_request_body_item import BulkUpdateGuildChannelsRequestBodyItem
    from .bulk_update_guild_roles_request_body_item import BulkUpdateGuildRolesRequestBodyItem
    from .button_component_for_message_request import ButtonComponentForMessageRequest
    from .button_component_response import ButtonComponentResponse
    from .button_style_types import ButtonStyleTypes
    from .channel_follower_response import ChannelFollowerResponse
    from .channel_follower_webhook_response import ChannelFollowerWebhookResponse
    from .channel_permission_overwrite_request import ChannelPermissionOverwriteRequest
    from .channel_permission_overwrite_response import ChannelPermissionOverwriteResponse
    from .channel_permission_overwrites import ChannelPermissionOverwrites
    from .channel_select_component_for_message_request import ChannelSelectComponentForMessageRequest
    from .channel_select_component_response import ChannelSelectComponentResponse
    from .channel_select_default_value import ChannelSelectDefaultValue
    from .channel_select_default_value_response import ChannelSelectDefaultValueResponse
    from .channel_select_default_value_response_type import ChannelSelectDefaultValueResponseType
    from .channel_select_default_value_type import ChannelSelectDefaultValueType
    from .channel_types import ChannelTypes
    from .command_permission_response import CommandPermissionResponse
    from .command_permissions_response import CommandPermissionsResponse
    from .component_emoji_for_message_request import ComponentEmojiForMessageRequest
    from .component_emoji_response import ComponentEmojiResponse
    from .confetti_potion_create_request import ConfettiPotionCreateRequest
    from .connected_account_guild_response import ConnectedAccountGuildResponse
    from .connected_account_integration_response import ConnectedAccountIntegrationResponse
    from .connected_account_providers import ConnectedAccountProviders
    from .connected_account_response import ConnectedAccountResponse
    from .connected_account_visibility import ConnectedAccountVisibility
    from .create_auto_moderation_rule_request_body import CreateAutoModerationRuleRequestBody
    from .create_auto_moderation_rule_response import CreateAutoModerationRuleResponse
    from .create_channel_invite_request_body import CreateChannelInviteRequestBody
    from .create_channel_invite_response import CreateChannelInviteResponse
    from .create_dm_response import CreateDmResponse
    from .create_forum_thread_request import CreateForumThreadRequest
    from .create_group_dm_invite_request import CreateGroupDmInviteRequest
    from .create_guild_invite_request import CreateGuildInviteRequest
    from .create_guild_request_channel_item import CreateGuildRequestChannelItem
    from .create_guild_request_role_item import CreateGuildRequestRoleItem
    from .create_guild_scheduled_event_request_body import CreateGuildScheduledEventRequestBody
    from .create_guild_scheduled_event_response import CreateGuildScheduledEventResponse
    from .create_interaction_response_request_body import CreateInteractionResponseRequestBody
    from .create_message_interaction_callback_request import CreateMessageInteractionCallbackRequest
    from .create_message_interaction_callback_response import CreateMessageInteractionCallbackResponse
    from .create_or_update_thread_tag_request import CreateOrUpdateThreadTagRequest
    from .create_text_thread_without_message_request import CreateTextThreadWithoutMessageRequest
    from .create_thread_request_body import CreateThreadRequestBody
    from .created_thread_response import CreatedThreadResponse
    from .default_keyword_list_trigger_metadata import DefaultKeywordListTriggerMetadata
    from .default_keyword_list_trigger_metadata_response import DefaultKeywordListTriggerMetadataResponse
    from .default_keyword_list_upsert_request import DefaultKeywordListUpsertRequest
    from .default_keyword_list_upsert_request_actions_item import DefaultKeywordListUpsertRequestActionsItem
    from .default_keyword_list_upsert_request_partial import DefaultKeywordListUpsertRequestPartial
    from .default_keyword_list_upsert_request_partial_actions_item import (
        DefaultKeywordListUpsertRequestPartialActionsItem,
    )
    from .default_keyword_rule_response import DefaultKeywordRuleResponse
    from .default_keyword_rule_response_actions_item import DefaultKeywordRuleResponseActionsItem
    from .default_reaction_emoji_response import DefaultReactionEmojiResponse
    from .delete_channel_response import DeleteChannelResponse
    from .discord_integration_response import DiscordIntegrationResponse
    from .discord_integration_response_scopes_item import DiscordIntegrationResponseScopesItem
    from .discord_integration_response_type import DiscordIntegrationResponseType
    from .embedded_activity_instance import EmbeddedActivityInstance
    from .embedded_activity_instance_location import EmbeddedActivityInstanceLocation
    from .embedded_activity_location_kind import EmbeddedActivityLocationKind
    from .emoji_response import EmojiResponse
    from .entitlement_owner_types import EntitlementOwnerTypes
    from .entitlement_response import EntitlementResponse
    from .entitlement_tenant_fulfillment_status_response import EntitlementTenantFulfillmentStatusResponse
    from .entitlement_types import EntitlementTypes
    from .entity_metadata_external import EntityMetadataExternal
    from .entity_metadata_external_response import EntityMetadataExternalResponse
    from .entity_metadata_stage_instance import EntityMetadataStageInstance
    from .entity_metadata_stage_instance_response import EntityMetadataStageInstanceResponse
    from .entity_metadata_voice import EntityMetadataVoice
    from .entity_metadata_voice_response import EntityMetadataVoiceResponse
    from .error import Error
    from .error_details import ErrorDetails
    from .error_response import ErrorResponse
    from .execute_webhook_request_body import ExecuteWebhookRequestBody
    from .external_connection_integration_response import ExternalConnectionIntegrationResponse
    from .external_connection_integration_response_type import ExternalConnectionIntegrationResponseType
    from .external_scheduled_event_create_request import ExternalScheduledEventCreateRequest
    from .external_scheduled_event_patch_request_partial import ExternalScheduledEventPatchRequestPartial
    from .external_scheduled_event_response import ExternalScheduledEventResponse
    from .flag_to_channel_action import FlagToChannelAction
    from .flag_to_channel_action_metadata import FlagToChannelActionMetadata
    from .flag_to_channel_action_metadata_response import FlagToChannelActionMetadataResponse
    from .flag_to_channel_action_response import FlagToChannelActionResponse
    from .forum_layout import ForumLayout
    from .forum_tag_response import ForumTagResponse
    from .friend_invite_response import FriendInviteResponse
    from .gateway_bot_response import GatewayBotResponse
    from .gateway_bot_session_start_limit_response import GatewayBotSessionStartLimitResponse
    from .gateway_response import GatewayResponse
    from .get_auto_moderation_rule_response import GetAutoModerationRuleResponse
    from .get_channel_response import GetChannelResponse
    from .get_entitlements_request_sku_ids import GetEntitlementsRequestSkuIds
    from .get_guild_scheduled_event_response import GetGuildScheduledEventResponse
    from .get_guild_webhooks_response_item import GetGuildWebhooksResponseItem
    from .get_sticker_response import GetStickerResponse
    from .get_webhook_by_token_response import GetWebhookByTokenResponse
    from .get_webhook_response import GetWebhookResponse
    from .github_author import GithubAuthor
    from .github_check_app import GithubCheckApp
    from .github_check_pull_request import GithubCheckPullRequest
    from .github_check_run import GithubCheckRun
    from .github_check_run_output import GithubCheckRunOutput
    from .github_check_suite import GithubCheckSuite
    from .github_comment import GithubComment
    from .github_commit import GithubCommit
    from .github_discussion import GithubDiscussion
    from .github_issue import GithubIssue
    from .github_release import GithubRelease
    from .github_repository import GithubRepository
    from .github_review import GithubReview
    from .github_user import GithubUser
    from .group_dm_invite_response import GroupDmInviteResponse
    from .guild_audit_log_response import GuildAuditLogResponse
    from .guild_audit_log_response_auto_moderation_rules_item import GuildAuditLogResponseAutoModerationRulesItem
    from .guild_audit_log_response_guild_scheduled_events_item import GuildAuditLogResponseGuildScheduledEventsItem
    from .guild_audit_log_response_integrations_item import GuildAuditLogResponseIntegrationsItem
    from .guild_audit_log_response_webhooks_item import GuildAuditLogResponseWebhooksItem
    from .guild_ban_response import GuildBanResponse
    from .guild_channel_location import GuildChannelLocation
    from .guild_channel_location_kind import GuildChannelLocationKind
    from .guild_channel_response import GuildChannelResponse
    from .guild_explicit_content_filter_types import GuildExplicitContentFilterTypes
    from .guild_features import GuildFeatures
    from .guild_home_settings_response import GuildHomeSettingsResponse
    from .guild_incoming_webhook_response import GuildIncomingWebhookResponse
    from .guild_invite_response import GuildInviteResponse
    from .guild_member_response import GuildMemberResponse
    from .guild_mfa_level import GuildMfaLevel
    from .guild_mfa_level_response import GuildMfaLevelResponse
    from .guild_nsfw_content_level import GuildNsfwContentLevel
    from .guild_onboarding_mode import GuildOnboardingMode
    from .guild_onboarding_response import GuildOnboardingResponse
    from .guild_preview_response import GuildPreviewResponse
    from .guild_product_purchase_response import GuildProductPurchaseResponse
    from .guild_prune_response import GuildPruneResponse
    from .guild_response import GuildResponse
    from .guild_role_response import GuildRoleResponse
    from .guild_role_tags_response import GuildRoleTagsResponse
    from .guild_scheduled_event_entity_types import GuildScheduledEventEntityTypes
    from .guild_scheduled_event_privacy_levels import GuildScheduledEventPrivacyLevels
    from .guild_scheduled_event_statuses import GuildScheduledEventStatuses
    from .guild_sticker_response import GuildStickerResponse
    from .guild_subscription_integration_response import GuildSubscriptionIntegrationResponse
    from .guild_subscription_integration_response_type import GuildSubscriptionIntegrationResponseType
    from .guild_template_channel_response import GuildTemplateChannelResponse
    from .guild_template_channel_tags import GuildTemplateChannelTags
    from .guild_template_response import GuildTemplateResponse
    from .guild_template_role_response import GuildTemplateRoleResponse
    from .guild_template_snapshot_response import GuildTemplateSnapshotResponse
    from .guild_welcome_channel import GuildWelcomeChannel
    from .guild_welcome_screen_channel_response import GuildWelcomeScreenChannelResponse
    from .guild_welcome_screen_response import GuildWelcomeScreenResponse
    from .guild_with_counts_response import GuildWithCountsResponse
    from .icon_emoji_response import IconEmojiResponse
    from .incoming_webhook_interaction_request import IncomingWebhookInteractionRequest
    from .incoming_webhook_request_partial import IncomingWebhookRequestPartial
    from .incoming_webhook_update_for_interaction_callback_request_partial import (
        IncomingWebhookUpdateForInteractionCallbackRequestPartial,
    )
    from .incoming_webhook_update_request_partial import IncomingWebhookUpdateRequestPartial
    from .inner_errors import InnerErrors
    from .int53type import Int53Type
    from .integration_application_response import IntegrationApplicationResponse
    from .integration_expire_behavior_types import IntegrationExpireBehaviorTypes
    from .integration_expire_grace_period_types import IntegrationExpireGracePeriodTypes
    from .integration_types import IntegrationTypes
    from .interaction_application_command_autocomplete_callback_integer_data import (
        InteractionApplicationCommandAutocompleteCallbackIntegerData,
    )
    from .interaction_application_command_autocomplete_callback_number_data import (
        InteractionApplicationCommandAutocompleteCallbackNumberData,
    )
    from .interaction_application_command_autocomplete_callback_string_data import (
        InteractionApplicationCommandAutocompleteCallbackStringData,
    )
    from .interaction_callback_response import InteractionCallbackResponse
    from .interaction_callback_response_resource import InteractionCallbackResponseResource
    from .interaction_callback_types import InteractionCallbackTypes
    from .interaction_context_type import InteractionContextType
    from .interaction_response import InteractionResponse
    from .interaction_types import InteractionTypes
    from .invite_application_response import InviteApplicationResponse
    from .invite_channel_recipient_response import InviteChannelRecipientResponse
    from .invite_channel_response import InviteChannelResponse
    from .invite_guild_response import InviteGuildResponse
    from .invite_resolve_response import InviteResolveResponse
    from .invite_revoke_response import InviteRevokeResponse
    from .invite_stage_instance_response import InviteStageInstanceResponse
    from .invite_target_types import InviteTargetTypes
    from .invite_types import InviteTypes
    from .keyword_rule_response import KeywordRuleResponse
    from .keyword_rule_response_actions_item import KeywordRuleResponseActionsItem
    from .keyword_trigger_metadata import KeywordTriggerMetadata
    from .keyword_trigger_metadata_response import KeywordTriggerMetadataResponse
    from .keyword_upsert_request import KeywordUpsertRequest
    from .keyword_upsert_request_actions_item import KeywordUpsertRequestActionsItem
    from .keyword_upsert_request_partial import KeywordUpsertRequestPartial
    from .keyword_upsert_request_partial_actions_item import KeywordUpsertRequestPartialActionsItem
    from .launch_activity_interaction_callback_request import LaunchActivityInteractionCallbackRequest
    from .launch_activity_interaction_callback_response import LaunchActivityInteractionCallbackResponse
    from .list_application_emojis_response import ListApplicationEmojisResponse
    from .list_auto_moderation_rules_response_item import ListAutoModerationRulesResponseItem
    from .list_channel_invites_response_item import ListChannelInvitesResponseItem
    from .list_channel_webhooks_response_item import ListChannelWebhooksResponseItem
    from .list_guild_channels_response_item import ListGuildChannelsResponseItem
    from .list_guild_integrations_response_item import ListGuildIntegrationsResponseItem
    from .list_guild_invites_response_item import ListGuildInvitesResponseItem
    from .list_guild_scheduled_events_response_item import ListGuildScheduledEventsResponseItem
    from .list_guild_soundboard_sounds_response import ListGuildSoundboardSoundsResponse
    from .lobby_member_request import LobbyMemberRequest
    from .lobby_member_response import LobbyMemberResponse
    from .lobby_message_response import LobbyMessageResponse
    from .lobby_response import LobbyResponse
    from .mention_spam_rule_response import MentionSpamRuleResponse
    from .mention_spam_rule_response_actions_item import MentionSpamRuleResponseActionsItem
    from .mention_spam_trigger_metadata import MentionSpamTriggerMetadata
    from .mention_spam_trigger_metadata_response import MentionSpamTriggerMetadataResponse
    from .mention_spam_upsert_request import MentionSpamUpsertRequest
    from .mention_spam_upsert_request_actions_item import MentionSpamUpsertRequestActionsItem
    from .mention_spam_upsert_request_partial import MentionSpamUpsertRequestPartial
    from .mention_spam_upsert_request_partial_actions_item import MentionSpamUpsertRequestPartialActionsItem
    from .mentionable_select_component_for_message_request import MentionableSelectComponentForMessageRequest
    from .mentionable_select_component_for_message_request_default_values_item import (
        MentionableSelectComponentForMessageRequestDefaultValuesItem,
        MentionableSelectComponentForMessageRequestDefaultValuesItem_Role,
        MentionableSelectComponentForMessageRequestDefaultValuesItem_User,
    )
    from .mentionable_select_component_response import MentionableSelectComponentResponse
    from .mentionable_select_component_response_default_values_item import (
        MentionableSelectComponentResponseDefaultValuesItem,
        MentionableSelectComponentResponseDefaultValuesItem_Role,
        MentionableSelectComponentResponseDefaultValuesItem_User,
    )
    from .message_activity_response import MessageActivityResponse
    from .message_allowed_mentions_request import MessageAllowedMentionsRequest
    from .message_attachment_request import MessageAttachmentRequest
    from .message_attachment_response import MessageAttachmentResponse
    from .message_call_response import MessageCallResponse
    from .message_component_interaction_metadata_response import MessageComponentInteractionMetadataResponse
    from .message_component_types import MessageComponentTypes
    from .message_create_request_nonce import MessageCreateRequestNonce
    from .message_embed_author_response import MessageEmbedAuthorResponse
    from .message_embed_field_response import MessageEmbedFieldResponse
    from .message_embed_footer_response import MessageEmbedFooterResponse
    from .message_embed_image_response import MessageEmbedImageResponse
    from .message_embed_provider_response import MessageEmbedProviderResponse
    from .message_embed_response import MessageEmbedResponse
    from .message_embed_video_response import MessageEmbedVideoResponse
    from .message_interaction_response import MessageInteractionResponse
    from .message_mention_channel_response import MessageMentionChannelResponse
    from .message_reaction_count_details_response import MessageReactionCountDetailsResponse
    from .message_reaction_emoji_response import MessageReactionEmojiResponse
    from .message_reaction_response import MessageReactionResponse
    from .message_reference_request import MessageReferenceRequest
    from .message_reference_response import MessageReferenceResponse
    from .message_reference_type import MessageReferenceType
    from .message_response import MessageResponse
    from .message_response_interaction_metadata import MessageResponseInteractionMetadata
    from .message_response_nonce import MessageResponseNonce
    from .message_response_stickers_item import MessageResponseStickersItem
    from .message_role_subscription_data_response import MessageRoleSubscriptionDataResponse
    from .message_snapshot_response import MessageSnapshotResponse
    from .message_sticker_item_response import MessageStickerItemResponse
    from .message_type import MessageType
    from .metadata_item_types import MetadataItemTypes
    from .minimal_content_message_response import MinimalContentMessageResponse
    from .minimal_content_message_response_stickers_item import MinimalContentMessageResponseStickersItem
    from .ml_spam_rule_response import MlSpamRuleResponse
    from .ml_spam_rule_response_actions_item import MlSpamRuleResponseActionsItem
    from .ml_spam_trigger_metadata import MlSpamTriggerMetadata
    from .ml_spam_trigger_metadata_response import MlSpamTriggerMetadataResponse
    from .ml_spam_upsert_request import MlSpamUpsertRequest
    from .ml_spam_upsert_request_actions_item import MlSpamUpsertRequestActionsItem
    from .ml_spam_upsert_request_partial import MlSpamUpsertRequestPartial
    from .ml_spam_upsert_request_partial_actions_item import MlSpamUpsertRequestPartialActionsItem
    from .modal_interaction_callback_request import ModalInteractionCallbackRequest
    from .modal_interaction_callback_request_data import ModalInteractionCallbackRequestData
    from .modal_submit_interaction_metadata_response import ModalSubmitInteractionMetadataResponse
    from .modal_submit_interaction_metadata_response_triggering_interaction_metadata import (
        ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata,
    )
    from .my_guild_response import MyGuildResponse
    from .nameplate_palette import NameplatePalette
    from .new_member_action_response import NewMemberActionResponse
    from .new_member_action_type import NewMemberActionType
    from .o_auth2get_authorization_response import OAuth2GetAuthorizationResponse
    from .o_auth2get_keys import OAuth2GetKeys
    from .o_auth2get_open_id_connect_user_info_response import OAuth2GetOpenIdConnectUserInfoResponse
    from .o_auth2key import OAuth2Key
    from .o_auth2scopes import OAuth2Scopes
    from .oauth_scope import OauthScope
    from .onboarding_prompt_option_request import OnboardingPromptOptionRequest
    from .onboarding_prompt_option_response import OnboardingPromptOptionResponse
    from .onboarding_prompt_response import OnboardingPromptResponse
    from .onboarding_prompt_type import OnboardingPromptType
    from .partial_discord_integration_response import PartialDiscordIntegrationResponse
    from .partial_discord_integration_response_type import PartialDiscordIntegrationResponseType
    from .partial_external_connection_integration_response import PartialExternalConnectionIntegrationResponse
    from .partial_external_connection_integration_response_type import PartialExternalConnectionIntegrationResponseType
    from .partial_guild_subscription_integration_response import PartialGuildSubscriptionIntegrationResponse
    from .partial_guild_subscription_integration_response_type import PartialGuildSubscriptionIntegrationResponseType
    from .poll_answer_create_request import PollAnswerCreateRequest
    from .poll_answer_details_response import PollAnswerDetailsResponse
    from .poll_answer_response import PollAnswerResponse
    from .poll_create_request import PollCreateRequest
    from .poll_emoji import PollEmoji
    from .poll_emoji_create_request import PollEmojiCreateRequest
    from .poll_layout_types import PollLayoutTypes
    from .poll_media import PollMedia
    from .poll_media_create_request import PollMediaCreateRequest
    from .poll_media_response import PollMediaResponse
    from .poll_response import PollResponse
    from .poll_results_entry_response import PollResultsEntryResponse
    from .poll_results_response import PollResultsResponse
    from .pong_interaction_callback_request import PongInteractionCallbackRequest
    from .premium_guild_tiers import PremiumGuildTiers
    from .premium_types import PremiumTypes
    from .preview_prune_guild_request_include_roles import PreviewPruneGuildRequestIncludeRoles
    from .private_application_response import PrivateApplicationResponse
    from .private_channel_location import PrivateChannelLocation
    from .private_channel_location_kind import PrivateChannelLocationKind
    from .private_channel_response import PrivateChannelResponse
    from .private_group_channel_response import PrivateGroupChannelResponse
    from .private_guild_member_response import PrivateGuildMemberResponse
    from .provisional_token_response import ProvisionalTokenResponse
    from .prune_guild_request_include_roles import PruneGuildRequestIncludeRoles
    from .purchase_notification_response import PurchaseNotificationResponse
    from .purchase_type import PurchaseType
    from .quarantine_user_action import QuarantineUserAction
    from .quarantine_user_action_metadata import QuarantineUserActionMetadata
    from .quarantine_user_action_metadata_response import QuarantineUserActionMetadataResponse
    from .quarantine_user_action_response import QuarantineUserActionResponse
    from .reaction_types import ReactionTypes
    from .resolved_objects_response import ResolvedObjectsResponse
    from .resolved_objects_response_channels_value import ResolvedObjectsResponseChannelsValue
    from .resource_channel_response import ResourceChannelResponse
    from .rich_embed import RichEmbed
    from .rich_embed_author import RichEmbedAuthor
    from .rich_embed_field import RichEmbedField
    from .rich_embed_footer import RichEmbedFooter
    from .rich_embed_image import RichEmbedImage
    from .rich_embed_provider import RichEmbedProvider
    from .rich_embed_thumbnail import RichEmbedThumbnail
    from .rich_embed_video import RichEmbedVideo
    from .role_select_component_for_message_request import RoleSelectComponentForMessageRequest
    from .role_select_component_response import RoleSelectComponentResponse
    from .role_select_default_value import RoleSelectDefaultValue
    from .role_select_default_value_response import RoleSelectDefaultValueResponse
    from .role_select_default_value_response_type import RoleSelectDefaultValueResponseType
    from .role_select_default_value_type import RoleSelectDefaultValueType
    from .scheduled_event_response import ScheduledEventResponse
    from .scheduled_event_user_response import ScheduledEventUserResponse
    from .sdk_message_request_nonce import SdkMessageRequestNonce
    from .settings_emoji_response import SettingsEmojiResponse
    from .snowflake_select_default_value_types import SnowflakeSelectDefaultValueTypes
    from .snowflake_type import SnowflakeType
    from .sorting_order import SortingOrder
    from .soundboard_sound_response import SoundboardSoundResponse
    from .spam_link_rule_response import SpamLinkRuleResponse
    from .spam_link_rule_response_actions_item import SpamLinkRuleResponseActionsItem
    from .spam_link_trigger_metadata_response import SpamLinkTriggerMetadataResponse
    from .stage_instance_response import StageInstanceResponse
    from .stage_instances_privacy_levels import StageInstancesPrivacyLevels
    from .stage_scheduled_event_create_request import StageScheduledEventCreateRequest
    from .stage_scheduled_event_patch_request_partial import StageScheduledEventPatchRequestPartial
    from .stage_scheduled_event_response import StageScheduledEventResponse
    from .standard_sticker_response import StandardStickerResponse
    from .sticker_format_types import StickerFormatTypes
    from .sticker_pack_collection_response import StickerPackCollectionResponse
    from .sticker_pack_response import StickerPackResponse
    from .sticker_types import StickerTypes
    from .string_select_component_for_message_request import StringSelectComponentForMessageRequest
    from .string_select_component_response import StringSelectComponentResponse
    from .string_select_option_for_message_request import StringSelectOptionForMessageRequest
    from .string_select_option_response import StringSelectOptionResponse
    from .team_member_response import TeamMemberResponse
    from .team_membership_states import TeamMembershipStates
    from .team_response import TeamResponse
    from .text_input_component_for_modal_request import TextInputComponentForModalRequest
    from .text_input_component_response import TextInputComponentResponse
    from .text_input_style_types import TextInputStyleTypes
    from .thread_auto_archive_duration import ThreadAutoArchiveDuration
    from .thread_member_response import ThreadMemberResponse
    from .thread_metadata_response import ThreadMetadataResponse
    from .thread_response import ThreadResponse
    from .thread_search_request_tag import ThreadSearchRequestTag
    from .thread_search_response import ThreadSearchResponse
    from .thread_search_tag_setting import ThreadSearchTagSetting
    from .thread_sort_order import ThreadSortOrder
    from .thread_sorting_mode import ThreadSortingMode
    from .threads_response import ThreadsResponse
    from .typing_indicator_response import TypingIndicatorResponse
    from .u_int32type import UInt32Type
    from .update_auto_moderation_rule_request_body import UpdateAutoModerationRuleRequestBody
    from .update_auto_moderation_rule_response import UpdateAutoModerationRuleResponse
    from .update_channel_request_body import UpdateChannelRequestBody
    from .update_channel_response import UpdateChannelResponse
    from .update_default_reaction_emoji_request import UpdateDefaultReactionEmojiRequest
    from .update_dm_request_partial import UpdateDmRequestPartial
    from .update_group_dm_request_partial import UpdateGroupDmRequestPartial
    from .update_guild_channel_request_partial import UpdateGuildChannelRequestPartial
    from .update_guild_scheduled_event_request_body import UpdateGuildScheduledEventRequestBody
    from .update_guild_scheduled_event_response import UpdateGuildScheduledEventResponse
    from .update_message_interaction_callback_request import UpdateMessageInteractionCallbackRequest
    from .update_message_interaction_callback_response import UpdateMessageInteractionCallbackResponse
    from .update_onboarding_prompt_request import UpdateOnboardingPromptRequest
    from .update_thread_request_partial import UpdateThreadRequestPartial
    from .update_thread_tag_request import UpdateThreadTagRequest
    from .update_webhook_by_token_response import UpdateWebhookByTokenResponse
    from .update_webhook_response import UpdateWebhookResponse
    from .user_avatar_decoration_response import UserAvatarDecorationResponse
    from .user_collectibles_response import UserCollectiblesResponse
    from .user_communication_disabled_action import UserCommunicationDisabledAction
    from .user_communication_disabled_action_metadata import UserCommunicationDisabledActionMetadata
    from .user_communication_disabled_action_metadata_response import UserCommunicationDisabledActionMetadataResponse
    from .user_communication_disabled_action_response import UserCommunicationDisabledActionResponse
    from .user_guild_onboarding_response import UserGuildOnboardingResponse
    from .user_nameplate_response import UserNameplateResponse
    from .user_notification_settings import UserNotificationSettings
    from .user_pii_response import UserPiiResponse
    from .user_primary_guild_response import UserPrimaryGuildResponse
    from .user_response import UserResponse
    from .user_select_component_for_message_request import UserSelectComponentForMessageRequest
    from .user_select_component_response import UserSelectComponentResponse
    from .user_select_default_value import UserSelectDefaultValue
    from .user_select_default_value_response import UserSelectDefaultValueResponse
    from .user_select_default_value_response_type import UserSelectDefaultValueResponseType
    from .user_select_default_value_type import UserSelectDefaultValueType
    from .vanity_url_error_response import VanityUrlErrorResponse
    from .vanity_url_response import VanityUrlResponse
    from .verification_levels import VerificationLevels
    from .video_quality_modes import VideoQualityModes
    from .voice_region_response import VoiceRegionResponse
    from .voice_scheduled_event_create_request import VoiceScheduledEventCreateRequest
    from .voice_scheduled_event_patch_request_partial import VoiceScheduledEventPatchRequestPartial
    from .voice_scheduled_event_response import VoiceScheduledEventResponse
    from .voice_state_response import VoiceStateResponse
    from .webhook_slack_embed import WebhookSlackEmbed
    from .webhook_slack_embed_field import WebhookSlackEmbedField
    from .webhook_source_channel_response import WebhookSourceChannelResponse
    from .webhook_source_guild_response import WebhookSourceGuildResponse
    from .webhook_types import WebhookTypes
    from .welcome_message_response import WelcomeMessageResponse
    from .widget_activity import WidgetActivity
    from .widget_channel import WidgetChannel
    from .widget_image_styles import WidgetImageStyles
    from .widget_member import WidgetMember
    from .widget_response import WidgetResponse
    from .widget_settings_response import WidgetSettingsResponse
    from .widget_user_discriminator import WidgetUserDiscriminator
_dynamic_imports: typing.Dict[str, str] = {
    "AccountResponse": ".account_response",
    "ActionRowComponentForMessageRequest": ".action_row_component_for_message_request",
    "ActionRowComponentForMessageRequestComponentsItem": ".action_row_component_for_message_request_components_item",
    "ActionRowComponentForModalRequest": ".action_row_component_for_modal_request",
    "ActionRowComponentResponse": ".action_row_component_response",
    "ActionRowComponentResponseComponentsItem": ".action_row_component_response_components_item",
    "ActivitiesAttachmentResponse": ".activities_attachment_response",
    "AddGroupDmUserResponse": ".add_group_dm_user_response",
    "AfkTimeouts": ".afk_timeouts",
    "AllowedMentionTypes": ".allowed_mention_types",
    "ApplicationCommandAttachmentOption": ".application_command_attachment_option",
    "ApplicationCommandAttachmentOptionResponse": ".application_command_attachment_option_response",
    "ApplicationCommandAutocompleteCallbackRequest": ".application_command_autocomplete_callback_request",
    "ApplicationCommandAutocompleteCallbackRequestData": ".application_command_autocomplete_callback_request_data",
    "ApplicationCommandBooleanOption": ".application_command_boolean_option",
    "ApplicationCommandBooleanOptionResponse": ".application_command_boolean_option_response",
    "ApplicationCommandChannelOption": ".application_command_channel_option",
    "ApplicationCommandChannelOptionResponse": ".application_command_channel_option_response",
    "ApplicationCommandCreateRequest": ".application_command_create_request",
    "ApplicationCommandCreateRequestOptionsItem": ".application_command_create_request_options_item",
    "ApplicationCommandHandler": ".application_command_handler",
    "ApplicationCommandIntegerOption": ".application_command_integer_option",
    "ApplicationCommandIntegerOptionResponse": ".application_command_integer_option_response",
    "ApplicationCommandInteractionMetadataResponse": ".application_command_interaction_metadata_response",
    "ApplicationCommandMentionableOption": ".application_command_mentionable_option",
    "ApplicationCommandMentionableOptionResponse": ".application_command_mentionable_option_response",
    "ApplicationCommandNumberOption": ".application_command_number_option",
    "ApplicationCommandNumberOptionResponse": ".application_command_number_option_response",
    "ApplicationCommandOptionIntegerChoice": ".application_command_option_integer_choice",
    "ApplicationCommandOptionIntegerChoiceResponse": ".application_command_option_integer_choice_response",
    "ApplicationCommandOptionNumberChoice": ".application_command_option_number_choice",
    "ApplicationCommandOptionNumberChoiceResponse": ".application_command_option_number_choice_response",
    "ApplicationCommandOptionStringChoice": ".application_command_option_string_choice",
    "ApplicationCommandOptionStringChoiceResponse": ".application_command_option_string_choice_response",
    "ApplicationCommandOptionType": ".application_command_option_type",
    "ApplicationCommandPatchRequestPartial": ".application_command_patch_request_partial",
    "ApplicationCommandPatchRequestPartialOptionsItem": ".application_command_patch_request_partial_options_item",
    "ApplicationCommandPermission": ".application_command_permission",
    "ApplicationCommandPermissionType": ".application_command_permission_type",
    "ApplicationCommandResponse": ".application_command_response",
    "ApplicationCommandResponseOptionsItem": ".application_command_response_options_item",
    "ApplicationCommandRoleOption": ".application_command_role_option",
    "ApplicationCommandRoleOptionResponse": ".application_command_role_option_response",
    "ApplicationCommandStringOption": ".application_command_string_option",
    "ApplicationCommandStringOptionResponse": ".application_command_string_option_response",
    "ApplicationCommandSubcommandGroupOption": ".application_command_subcommand_group_option",
    "ApplicationCommandSubcommandGroupOptionResponse": ".application_command_subcommand_group_option_response",
    "ApplicationCommandSubcommandOption": ".application_command_subcommand_option",
    "ApplicationCommandSubcommandOptionOptionsItem": ".application_command_subcommand_option_options_item",
    "ApplicationCommandSubcommandOptionResponse": ".application_command_subcommand_option_response",
    "ApplicationCommandSubcommandOptionResponseOptionsItem": ".application_command_subcommand_option_response_options_item",
    "ApplicationCommandType": ".application_command_type",
    "ApplicationCommandUpdateRequest": ".application_command_update_request",
    "ApplicationCommandUpdateRequestOptionsItem": ".application_command_update_request_options_item",
    "ApplicationCommandUserOption": ".application_command_user_option",
    "ApplicationCommandUserOptionResponse": ".application_command_user_option_response",
    "ApplicationExplicitContentFilterTypes": ".application_explicit_content_filter_types",
    "ApplicationFormPartial": ".application_form_partial",
    "ApplicationFormPartialDescription": ".application_form_partial_description",
    "ApplicationIdentityProviderAuthType": ".application_identity_provider_auth_type",
    "ApplicationIncomingWebhookResponse": ".application_incoming_webhook_response",
    "ApplicationIntegrationType": ".application_integration_type",
    "ApplicationIntegrationTypeConfiguration": ".application_integration_type_configuration",
    "ApplicationIntegrationTypeConfigurationResponse": ".application_integration_type_configuration_response",
    "ApplicationOAuth2InstallParams": ".application_o_auth2install_params",
    "ApplicationOAuth2InstallParamsResponse": ".application_o_auth2install_params_response",
    "ApplicationOAuth2InstallParamsResponseScopesItem": ".application_o_auth2install_params_response_scopes_item",
    "ApplicationOAuth2InstallParamsScopesItem": ".application_o_auth2install_params_scopes_item",
    "ApplicationResponse": ".application_response",
    "ApplicationRoleConnectionsMetadataItemRequest": ".application_role_connections_metadata_item_request",
    "ApplicationRoleConnectionsMetadataItemResponse": ".application_role_connections_metadata_item_response",
    "ApplicationTypes": ".application_types",
    "ApplicationUserRoleConnectionResponse": ".application_user_role_connection_response",
    "AttachmentResponse": ".attachment_response",
    "AuditLogActionTypes": ".audit_log_action_types",
    "AuditLogEntryResponse": ".audit_log_entry_response",
    "AuditLogObjectChangeResponse": ".audit_log_object_change_response",
    "AutomodActionType": ".automod_action_type",
    "AutomodEventType": ".automod_event_type",
    "AutomodKeywordPresetType": ".automod_keyword_preset_type",
    "AutomodTriggerType": ".automod_trigger_type",
    "AvailableLocalesEnum": ".available_locales_enum",
    "BaseCreateMessageCreateRequest": ".base_create_message_create_request",
    "BasicApplicationResponse": ".basic_application_response",
    "BasicMessageResponse": ".basic_message_response",
    "BasicMessageResponseInteractionMetadata": ".basic_message_response_interaction_metadata",
    "BasicMessageResponseNonce": ".basic_message_response_nonce",
    "BasicMessageResponseStickersItem": ".basic_message_response_stickers_item",
    "BlockMessageAction": ".block_message_action",
    "BlockMessageActionMetadata": ".block_message_action_metadata",
    "BlockMessageActionMetadataResponse": ".block_message_action_metadata_response",
    "BlockMessageActionResponse": ".block_message_action_response",
    "BulkBanUsersResponse": ".bulk_ban_users_response",
    "BulkUpdateGuildChannelsRequestBodyItem": ".bulk_update_guild_channels_request_body_item",
    "BulkUpdateGuildRolesRequestBodyItem": ".bulk_update_guild_roles_request_body_item",
    "ButtonComponentForMessageRequest": ".button_component_for_message_request",
    "ButtonComponentResponse": ".button_component_response",
    "ButtonStyleTypes": ".button_style_types",
    "ChannelFollowerResponse": ".channel_follower_response",
    "ChannelFollowerWebhookResponse": ".channel_follower_webhook_response",
    "ChannelPermissionOverwriteRequest": ".channel_permission_overwrite_request",
    "ChannelPermissionOverwriteResponse": ".channel_permission_overwrite_response",
    "ChannelPermissionOverwrites": ".channel_permission_overwrites",
    "ChannelSelectComponentForMessageRequest": ".channel_select_component_for_message_request",
    "ChannelSelectComponentResponse": ".channel_select_component_response",
    "ChannelSelectDefaultValue": ".channel_select_default_value",
    "ChannelSelectDefaultValueResponse": ".channel_select_default_value_response",
    "ChannelSelectDefaultValueResponseType": ".channel_select_default_value_response_type",
    "ChannelSelectDefaultValueType": ".channel_select_default_value_type",
    "ChannelTypes": ".channel_types",
    "CommandPermissionResponse": ".command_permission_response",
    "CommandPermissionsResponse": ".command_permissions_response",
    "ComponentEmojiForMessageRequest": ".component_emoji_for_message_request",
    "ComponentEmojiResponse": ".component_emoji_response",
    "ConfettiPotionCreateRequest": ".confetti_potion_create_request",
    "ConnectedAccountGuildResponse": ".connected_account_guild_response",
    "ConnectedAccountIntegrationResponse": ".connected_account_integration_response",
    "ConnectedAccountProviders": ".connected_account_providers",
    "ConnectedAccountResponse": ".connected_account_response",
    "ConnectedAccountVisibility": ".connected_account_visibility",
    "CreateAutoModerationRuleRequestBody": ".create_auto_moderation_rule_request_body",
    "CreateAutoModerationRuleResponse": ".create_auto_moderation_rule_response",
    "CreateChannelInviteRequestBody": ".create_channel_invite_request_body",
    "CreateChannelInviteResponse": ".create_channel_invite_response",
    "CreateDmResponse": ".create_dm_response",
    "CreateForumThreadRequest": ".create_forum_thread_request",
    "CreateGroupDmInviteRequest": ".create_group_dm_invite_request",
    "CreateGuildInviteRequest": ".create_guild_invite_request",
    "CreateGuildRequestChannelItem": ".create_guild_request_channel_item",
    "CreateGuildRequestRoleItem": ".create_guild_request_role_item",
    "CreateGuildScheduledEventRequestBody": ".create_guild_scheduled_event_request_body",
    "CreateGuildScheduledEventResponse": ".create_guild_scheduled_event_response",
    "CreateInteractionResponseRequestBody": ".create_interaction_response_request_body",
    "CreateMessageInteractionCallbackRequest": ".create_message_interaction_callback_request",
    "CreateMessageInteractionCallbackResponse": ".create_message_interaction_callback_response",
    "CreateOrUpdateThreadTagRequest": ".create_or_update_thread_tag_request",
    "CreateTextThreadWithoutMessageRequest": ".create_text_thread_without_message_request",
    "CreateThreadRequestBody": ".create_thread_request_body",
    "CreatedThreadResponse": ".created_thread_response",
    "DefaultKeywordListTriggerMetadata": ".default_keyword_list_trigger_metadata",
    "DefaultKeywordListTriggerMetadataResponse": ".default_keyword_list_trigger_metadata_response",
    "DefaultKeywordListUpsertRequest": ".default_keyword_list_upsert_request",
    "DefaultKeywordListUpsertRequestActionsItem": ".default_keyword_list_upsert_request_actions_item",
    "DefaultKeywordListUpsertRequestPartial": ".default_keyword_list_upsert_request_partial",
    "DefaultKeywordListUpsertRequestPartialActionsItem": ".default_keyword_list_upsert_request_partial_actions_item",
    "DefaultKeywordRuleResponse": ".default_keyword_rule_response",
    "DefaultKeywordRuleResponseActionsItem": ".default_keyword_rule_response_actions_item",
    "DefaultReactionEmojiResponse": ".default_reaction_emoji_response",
    "DeleteChannelResponse": ".delete_channel_response",
    "DiscordIntegrationResponse": ".discord_integration_response",
    "DiscordIntegrationResponseScopesItem": ".discord_integration_response_scopes_item",
    "DiscordIntegrationResponseType": ".discord_integration_response_type",
    "EmbeddedActivityInstance": ".embedded_activity_instance",
    "EmbeddedActivityInstanceLocation": ".embedded_activity_instance_location",
    "EmbeddedActivityLocationKind": ".embedded_activity_location_kind",
    "EmojiResponse": ".emoji_response",
    "EntitlementOwnerTypes": ".entitlement_owner_types",
    "EntitlementResponse": ".entitlement_response",
    "EntitlementTenantFulfillmentStatusResponse": ".entitlement_tenant_fulfillment_status_response",
    "EntitlementTypes": ".entitlement_types",
    "EntityMetadataExternal": ".entity_metadata_external",
    "EntityMetadataExternalResponse": ".entity_metadata_external_response",
    "EntityMetadataStageInstance": ".entity_metadata_stage_instance",
    "EntityMetadataStageInstanceResponse": ".entity_metadata_stage_instance_response",
    "EntityMetadataVoice": ".entity_metadata_voice",
    "EntityMetadataVoiceResponse": ".entity_metadata_voice_response",
    "Error": ".error",
    "ErrorDetails": ".error_details",
    "ErrorResponse": ".error_response",
    "ExecuteWebhookRequestBody": ".execute_webhook_request_body",
    "ExternalConnectionIntegrationResponse": ".external_connection_integration_response",
    "ExternalConnectionIntegrationResponseType": ".external_connection_integration_response_type",
    "ExternalScheduledEventCreateRequest": ".external_scheduled_event_create_request",
    "ExternalScheduledEventPatchRequestPartial": ".external_scheduled_event_patch_request_partial",
    "ExternalScheduledEventResponse": ".external_scheduled_event_response",
    "FlagToChannelAction": ".flag_to_channel_action",
    "FlagToChannelActionMetadata": ".flag_to_channel_action_metadata",
    "FlagToChannelActionMetadataResponse": ".flag_to_channel_action_metadata_response",
    "FlagToChannelActionResponse": ".flag_to_channel_action_response",
    "ForumLayout": ".forum_layout",
    "ForumTagResponse": ".forum_tag_response",
    "FriendInviteResponse": ".friend_invite_response",
    "GatewayBotResponse": ".gateway_bot_response",
    "GatewayBotSessionStartLimitResponse": ".gateway_bot_session_start_limit_response",
    "GatewayResponse": ".gateway_response",
    "GetAutoModerationRuleResponse": ".get_auto_moderation_rule_response",
    "GetChannelResponse": ".get_channel_response",
    "GetEntitlementsRequestSkuIds": ".get_entitlements_request_sku_ids",
    "GetGuildScheduledEventResponse": ".get_guild_scheduled_event_response",
    "GetGuildWebhooksResponseItem": ".get_guild_webhooks_response_item",
    "GetStickerResponse": ".get_sticker_response",
    "GetWebhookByTokenResponse": ".get_webhook_by_token_response",
    "GetWebhookResponse": ".get_webhook_response",
    "GithubAuthor": ".github_author",
    "GithubCheckApp": ".github_check_app",
    "GithubCheckPullRequest": ".github_check_pull_request",
    "GithubCheckRun": ".github_check_run",
    "GithubCheckRunOutput": ".github_check_run_output",
    "GithubCheckSuite": ".github_check_suite",
    "GithubComment": ".github_comment",
    "GithubCommit": ".github_commit",
    "GithubDiscussion": ".github_discussion",
    "GithubIssue": ".github_issue",
    "GithubRelease": ".github_release",
    "GithubRepository": ".github_repository",
    "GithubReview": ".github_review",
    "GithubUser": ".github_user",
    "GroupDmInviteResponse": ".group_dm_invite_response",
    "GuildAuditLogResponse": ".guild_audit_log_response",
    "GuildAuditLogResponseAutoModerationRulesItem": ".guild_audit_log_response_auto_moderation_rules_item",
    "GuildAuditLogResponseGuildScheduledEventsItem": ".guild_audit_log_response_guild_scheduled_events_item",
    "GuildAuditLogResponseIntegrationsItem": ".guild_audit_log_response_integrations_item",
    "GuildAuditLogResponseWebhooksItem": ".guild_audit_log_response_webhooks_item",
    "GuildBanResponse": ".guild_ban_response",
    "GuildChannelLocation": ".guild_channel_location",
    "GuildChannelLocationKind": ".guild_channel_location_kind",
    "GuildChannelResponse": ".guild_channel_response",
    "GuildExplicitContentFilterTypes": ".guild_explicit_content_filter_types",
    "GuildFeatures": ".guild_features",
    "GuildHomeSettingsResponse": ".guild_home_settings_response",
    "GuildIncomingWebhookResponse": ".guild_incoming_webhook_response",
    "GuildInviteResponse": ".guild_invite_response",
    "GuildMemberResponse": ".guild_member_response",
    "GuildMfaLevel": ".guild_mfa_level",
    "GuildMfaLevelResponse": ".guild_mfa_level_response",
    "GuildNsfwContentLevel": ".guild_nsfw_content_level",
    "GuildOnboardingMode": ".guild_onboarding_mode",
    "GuildOnboardingResponse": ".guild_onboarding_response",
    "GuildPreviewResponse": ".guild_preview_response",
    "GuildProductPurchaseResponse": ".guild_product_purchase_response",
    "GuildPruneResponse": ".guild_prune_response",
    "GuildResponse": ".guild_response",
    "GuildRoleResponse": ".guild_role_response",
    "GuildRoleTagsResponse": ".guild_role_tags_response",
    "GuildScheduledEventEntityTypes": ".guild_scheduled_event_entity_types",
    "GuildScheduledEventPrivacyLevels": ".guild_scheduled_event_privacy_levels",
    "GuildScheduledEventStatuses": ".guild_scheduled_event_statuses",
    "GuildStickerResponse": ".guild_sticker_response",
    "GuildSubscriptionIntegrationResponse": ".guild_subscription_integration_response",
    "GuildSubscriptionIntegrationResponseType": ".guild_subscription_integration_response_type",
    "GuildTemplateChannelResponse": ".guild_template_channel_response",
    "GuildTemplateChannelTags": ".guild_template_channel_tags",
    "GuildTemplateResponse": ".guild_template_response",
    "GuildTemplateRoleResponse": ".guild_template_role_response",
    "GuildTemplateSnapshotResponse": ".guild_template_snapshot_response",
    "GuildWelcomeChannel": ".guild_welcome_channel",
    "GuildWelcomeScreenChannelResponse": ".guild_welcome_screen_channel_response",
    "GuildWelcomeScreenResponse": ".guild_welcome_screen_response",
    "GuildWithCountsResponse": ".guild_with_counts_response",
    "IconEmojiResponse": ".icon_emoji_response",
    "IncomingWebhookInteractionRequest": ".incoming_webhook_interaction_request",
    "IncomingWebhookRequestPartial": ".incoming_webhook_request_partial",
    "IncomingWebhookUpdateForInteractionCallbackRequestPartial": ".incoming_webhook_update_for_interaction_callback_request_partial",
    "IncomingWebhookUpdateRequestPartial": ".incoming_webhook_update_request_partial",
    "InnerErrors": ".inner_errors",
    "Int53Type": ".int53type",
    "IntegrationApplicationResponse": ".integration_application_response",
    "IntegrationExpireBehaviorTypes": ".integration_expire_behavior_types",
    "IntegrationExpireGracePeriodTypes": ".integration_expire_grace_period_types",
    "IntegrationTypes": ".integration_types",
    "InteractionApplicationCommandAutocompleteCallbackIntegerData": ".interaction_application_command_autocomplete_callback_integer_data",
    "InteractionApplicationCommandAutocompleteCallbackNumberData": ".interaction_application_command_autocomplete_callback_number_data",
    "InteractionApplicationCommandAutocompleteCallbackStringData": ".interaction_application_command_autocomplete_callback_string_data",
    "InteractionCallbackResponse": ".interaction_callback_response",
    "InteractionCallbackResponseResource": ".interaction_callback_response_resource",
    "InteractionCallbackTypes": ".interaction_callback_types",
    "InteractionContextType": ".interaction_context_type",
    "InteractionResponse": ".interaction_response",
    "InteractionTypes": ".interaction_types",
    "InviteApplicationResponse": ".invite_application_response",
    "InviteChannelRecipientResponse": ".invite_channel_recipient_response",
    "InviteChannelResponse": ".invite_channel_response",
    "InviteGuildResponse": ".invite_guild_response",
    "InviteResolveResponse": ".invite_resolve_response",
    "InviteRevokeResponse": ".invite_revoke_response",
    "InviteStageInstanceResponse": ".invite_stage_instance_response",
    "InviteTargetTypes": ".invite_target_types",
    "InviteTypes": ".invite_types",
    "KeywordRuleResponse": ".keyword_rule_response",
    "KeywordRuleResponseActionsItem": ".keyword_rule_response_actions_item",
    "KeywordTriggerMetadata": ".keyword_trigger_metadata",
    "KeywordTriggerMetadataResponse": ".keyword_trigger_metadata_response",
    "KeywordUpsertRequest": ".keyword_upsert_request",
    "KeywordUpsertRequestActionsItem": ".keyword_upsert_request_actions_item",
    "KeywordUpsertRequestPartial": ".keyword_upsert_request_partial",
    "KeywordUpsertRequestPartialActionsItem": ".keyword_upsert_request_partial_actions_item",
    "LaunchActivityInteractionCallbackRequest": ".launch_activity_interaction_callback_request",
    "LaunchActivityInteractionCallbackResponse": ".launch_activity_interaction_callback_response",
    "ListApplicationEmojisResponse": ".list_application_emojis_response",
    "ListAutoModerationRulesResponseItem": ".list_auto_moderation_rules_response_item",
    "ListChannelInvitesResponseItem": ".list_channel_invites_response_item",
    "ListChannelWebhooksResponseItem": ".list_channel_webhooks_response_item",
    "ListGuildChannelsResponseItem": ".list_guild_channels_response_item",
    "ListGuildIntegrationsResponseItem": ".list_guild_integrations_response_item",
    "ListGuildInvitesResponseItem": ".list_guild_invites_response_item",
    "ListGuildScheduledEventsResponseItem": ".list_guild_scheduled_events_response_item",
    "ListGuildSoundboardSoundsResponse": ".list_guild_soundboard_sounds_response",
    "LobbyMemberRequest": ".lobby_member_request",
    "LobbyMemberResponse": ".lobby_member_response",
    "LobbyMessageResponse": ".lobby_message_response",
    "LobbyResponse": ".lobby_response",
    "MentionSpamRuleResponse": ".mention_spam_rule_response",
    "MentionSpamRuleResponseActionsItem": ".mention_spam_rule_response_actions_item",
    "MentionSpamTriggerMetadata": ".mention_spam_trigger_metadata",
    "MentionSpamTriggerMetadataResponse": ".mention_spam_trigger_metadata_response",
    "MentionSpamUpsertRequest": ".mention_spam_upsert_request",
    "MentionSpamUpsertRequestActionsItem": ".mention_spam_upsert_request_actions_item",
    "MentionSpamUpsertRequestPartial": ".mention_spam_upsert_request_partial",
    "MentionSpamUpsertRequestPartialActionsItem": ".mention_spam_upsert_request_partial_actions_item",
    "MentionableSelectComponentForMessageRequest": ".mentionable_select_component_for_message_request",
    "MentionableSelectComponentForMessageRequestDefaultValuesItem": ".mentionable_select_component_for_message_request_default_values_item",
    "MentionableSelectComponentForMessageRequestDefaultValuesItem_Role": ".mentionable_select_component_for_message_request_default_values_item",
    "MentionableSelectComponentForMessageRequestDefaultValuesItem_User": ".mentionable_select_component_for_message_request_default_values_item",
    "MentionableSelectComponentResponse": ".mentionable_select_component_response",
    "MentionableSelectComponentResponseDefaultValuesItem": ".mentionable_select_component_response_default_values_item",
    "MentionableSelectComponentResponseDefaultValuesItem_Role": ".mentionable_select_component_response_default_values_item",
    "MentionableSelectComponentResponseDefaultValuesItem_User": ".mentionable_select_component_response_default_values_item",
    "MessageActivityResponse": ".message_activity_response",
    "MessageAllowedMentionsRequest": ".message_allowed_mentions_request",
    "MessageAttachmentRequest": ".message_attachment_request",
    "MessageAttachmentResponse": ".message_attachment_response",
    "MessageCallResponse": ".message_call_response",
    "MessageComponentInteractionMetadataResponse": ".message_component_interaction_metadata_response",
    "MessageComponentTypes": ".message_component_types",
    "MessageCreateRequestNonce": ".message_create_request_nonce",
    "MessageEmbedAuthorResponse": ".message_embed_author_response",
    "MessageEmbedFieldResponse": ".message_embed_field_response",
    "MessageEmbedFooterResponse": ".message_embed_footer_response",
    "MessageEmbedImageResponse": ".message_embed_image_response",
    "MessageEmbedProviderResponse": ".message_embed_provider_response",
    "MessageEmbedResponse": ".message_embed_response",
    "MessageEmbedVideoResponse": ".message_embed_video_response",
    "MessageInteractionResponse": ".message_interaction_response",
    "MessageMentionChannelResponse": ".message_mention_channel_response",
    "MessageReactionCountDetailsResponse": ".message_reaction_count_details_response",
    "MessageReactionEmojiResponse": ".message_reaction_emoji_response",
    "MessageReactionResponse": ".message_reaction_response",
    "MessageReferenceRequest": ".message_reference_request",
    "MessageReferenceResponse": ".message_reference_response",
    "MessageReferenceType": ".message_reference_type",
    "MessageResponse": ".message_response",
    "MessageResponseInteractionMetadata": ".message_response_interaction_metadata",
    "MessageResponseNonce": ".message_response_nonce",
    "MessageResponseStickersItem": ".message_response_stickers_item",
    "MessageRoleSubscriptionDataResponse": ".message_role_subscription_data_response",
    "MessageSnapshotResponse": ".message_snapshot_response",
    "MessageStickerItemResponse": ".message_sticker_item_response",
    "MessageType": ".message_type",
    "MetadataItemTypes": ".metadata_item_types",
    "MinimalContentMessageResponse": ".minimal_content_message_response",
    "MinimalContentMessageResponseStickersItem": ".minimal_content_message_response_stickers_item",
    "MlSpamRuleResponse": ".ml_spam_rule_response",
    "MlSpamRuleResponseActionsItem": ".ml_spam_rule_response_actions_item",
    "MlSpamTriggerMetadata": ".ml_spam_trigger_metadata",
    "MlSpamTriggerMetadataResponse": ".ml_spam_trigger_metadata_response",
    "MlSpamUpsertRequest": ".ml_spam_upsert_request",
    "MlSpamUpsertRequestActionsItem": ".ml_spam_upsert_request_actions_item",
    "MlSpamUpsertRequestPartial": ".ml_spam_upsert_request_partial",
    "MlSpamUpsertRequestPartialActionsItem": ".ml_spam_upsert_request_partial_actions_item",
    "ModalInteractionCallbackRequest": ".modal_interaction_callback_request",
    "ModalInteractionCallbackRequestData": ".modal_interaction_callback_request_data",
    "ModalSubmitInteractionMetadataResponse": ".modal_submit_interaction_metadata_response",
    "ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata": ".modal_submit_interaction_metadata_response_triggering_interaction_metadata",
    "MyGuildResponse": ".my_guild_response",
    "NameplatePalette": ".nameplate_palette",
    "NewMemberActionResponse": ".new_member_action_response",
    "NewMemberActionType": ".new_member_action_type",
    "OAuth2GetAuthorizationResponse": ".o_auth2get_authorization_response",
    "OAuth2GetKeys": ".o_auth2get_keys",
    "OAuth2GetOpenIdConnectUserInfoResponse": ".o_auth2get_open_id_connect_user_info_response",
    "OAuth2Key": ".o_auth2key",
    "OAuth2Scopes": ".o_auth2scopes",
    "OauthScope": ".oauth_scope",
    "OnboardingPromptOptionRequest": ".onboarding_prompt_option_request",
    "OnboardingPromptOptionResponse": ".onboarding_prompt_option_response",
    "OnboardingPromptResponse": ".onboarding_prompt_response",
    "OnboardingPromptType": ".onboarding_prompt_type",
    "PartialDiscordIntegrationResponse": ".partial_discord_integration_response",
    "PartialDiscordIntegrationResponseType": ".partial_discord_integration_response_type",
    "PartialExternalConnectionIntegrationResponse": ".partial_external_connection_integration_response",
    "PartialExternalConnectionIntegrationResponseType": ".partial_external_connection_integration_response_type",
    "PartialGuildSubscriptionIntegrationResponse": ".partial_guild_subscription_integration_response",
    "PartialGuildSubscriptionIntegrationResponseType": ".partial_guild_subscription_integration_response_type",
    "PollAnswerCreateRequest": ".poll_answer_create_request",
    "PollAnswerDetailsResponse": ".poll_answer_details_response",
    "PollAnswerResponse": ".poll_answer_response",
    "PollCreateRequest": ".poll_create_request",
    "PollEmoji": ".poll_emoji",
    "PollEmojiCreateRequest": ".poll_emoji_create_request",
    "PollLayoutTypes": ".poll_layout_types",
    "PollMedia": ".poll_media",
    "PollMediaCreateRequest": ".poll_media_create_request",
    "PollMediaResponse": ".poll_media_response",
    "PollResponse": ".poll_response",
    "PollResultsEntryResponse": ".poll_results_entry_response",
    "PollResultsResponse": ".poll_results_response",
    "PongInteractionCallbackRequest": ".pong_interaction_callback_request",
    "PremiumGuildTiers": ".premium_guild_tiers",
    "PremiumTypes": ".premium_types",
    "PreviewPruneGuildRequestIncludeRoles": ".preview_prune_guild_request_include_roles",
    "PrivateApplicationResponse": ".private_application_response",
    "PrivateChannelLocation": ".private_channel_location",
    "PrivateChannelLocationKind": ".private_channel_location_kind",
    "PrivateChannelResponse": ".private_channel_response",
    "PrivateGroupChannelResponse": ".private_group_channel_response",
    "PrivateGuildMemberResponse": ".private_guild_member_response",
    "ProvisionalTokenResponse": ".provisional_token_response",
    "PruneGuildRequestIncludeRoles": ".prune_guild_request_include_roles",
    "PurchaseNotificationResponse": ".purchase_notification_response",
    "PurchaseType": ".purchase_type",
    "QuarantineUserAction": ".quarantine_user_action",
    "QuarantineUserActionMetadata": ".quarantine_user_action_metadata",
    "QuarantineUserActionMetadataResponse": ".quarantine_user_action_metadata_response",
    "QuarantineUserActionResponse": ".quarantine_user_action_response",
    "ReactionTypes": ".reaction_types",
    "ResolvedObjectsResponse": ".resolved_objects_response",
    "ResolvedObjectsResponseChannelsValue": ".resolved_objects_response_channels_value",
    "ResourceChannelResponse": ".resource_channel_response",
    "RichEmbed": ".rich_embed",
    "RichEmbedAuthor": ".rich_embed_author",
    "RichEmbedField": ".rich_embed_field",
    "RichEmbedFooter": ".rich_embed_footer",
    "RichEmbedImage": ".rich_embed_image",
    "RichEmbedProvider": ".rich_embed_provider",
    "RichEmbedThumbnail": ".rich_embed_thumbnail",
    "RichEmbedVideo": ".rich_embed_video",
    "RoleSelectComponentForMessageRequest": ".role_select_component_for_message_request",
    "RoleSelectComponentResponse": ".role_select_component_response",
    "RoleSelectDefaultValue": ".role_select_default_value",
    "RoleSelectDefaultValueResponse": ".role_select_default_value_response",
    "RoleSelectDefaultValueResponseType": ".role_select_default_value_response_type",
    "RoleSelectDefaultValueType": ".role_select_default_value_type",
    "ScheduledEventResponse": ".scheduled_event_response",
    "ScheduledEventUserResponse": ".scheduled_event_user_response",
    "SdkMessageRequestNonce": ".sdk_message_request_nonce",
    "SettingsEmojiResponse": ".settings_emoji_response",
    "SnowflakeSelectDefaultValueTypes": ".snowflake_select_default_value_types",
    "SnowflakeType": ".snowflake_type",
    "SortingOrder": ".sorting_order",
    "SoundboardSoundResponse": ".soundboard_sound_response",
    "SpamLinkRuleResponse": ".spam_link_rule_response",
    "SpamLinkRuleResponseActionsItem": ".spam_link_rule_response_actions_item",
    "SpamLinkTriggerMetadataResponse": ".spam_link_trigger_metadata_response",
    "StageInstanceResponse": ".stage_instance_response",
    "StageInstancesPrivacyLevels": ".stage_instances_privacy_levels",
    "StageScheduledEventCreateRequest": ".stage_scheduled_event_create_request",
    "StageScheduledEventPatchRequestPartial": ".stage_scheduled_event_patch_request_partial",
    "StageScheduledEventResponse": ".stage_scheduled_event_response",
    "StandardStickerResponse": ".standard_sticker_response",
    "StickerFormatTypes": ".sticker_format_types",
    "StickerPackCollectionResponse": ".sticker_pack_collection_response",
    "StickerPackResponse": ".sticker_pack_response",
    "StickerTypes": ".sticker_types",
    "StringSelectComponentForMessageRequest": ".string_select_component_for_message_request",
    "StringSelectComponentResponse": ".string_select_component_response",
    "StringSelectOptionForMessageRequest": ".string_select_option_for_message_request",
    "StringSelectOptionResponse": ".string_select_option_response",
    "TeamMemberResponse": ".team_member_response",
    "TeamMembershipStates": ".team_membership_states",
    "TeamResponse": ".team_response",
    "TextInputComponentForModalRequest": ".text_input_component_for_modal_request",
    "TextInputComponentResponse": ".text_input_component_response",
    "TextInputStyleTypes": ".text_input_style_types",
    "ThreadAutoArchiveDuration": ".thread_auto_archive_duration",
    "ThreadMemberResponse": ".thread_member_response",
    "ThreadMetadataResponse": ".thread_metadata_response",
    "ThreadResponse": ".thread_response",
    "ThreadSearchRequestTag": ".thread_search_request_tag",
    "ThreadSearchResponse": ".thread_search_response",
    "ThreadSearchTagSetting": ".thread_search_tag_setting",
    "ThreadSortOrder": ".thread_sort_order",
    "ThreadSortingMode": ".thread_sorting_mode",
    "ThreadsResponse": ".threads_response",
    "TypingIndicatorResponse": ".typing_indicator_response",
    "UInt32Type": ".u_int32type",
    "UpdateAutoModerationRuleRequestBody": ".update_auto_moderation_rule_request_body",
    "UpdateAutoModerationRuleResponse": ".update_auto_moderation_rule_response",
    "UpdateChannelRequestBody": ".update_channel_request_body",
    "UpdateChannelResponse": ".update_channel_response",
    "UpdateDefaultReactionEmojiRequest": ".update_default_reaction_emoji_request",
    "UpdateDmRequestPartial": ".update_dm_request_partial",
    "UpdateGroupDmRequestPartial": ".update_group_dm_request_partial",
    "UpdateGuildChannelRequestPartial": ".update_guild_channel_request_partial",
    "UpdateGuildScheduledEventRequestBody": ".update_guild_scheduled_event_request_body",
    "UpdateGuildScheduledEventResponse": ".update_guild_scheduled_event_response",
    "UpdateMessageInteractionCallbackRequest": ".update_message_interaction_callback_request",
    "UpdateMessageInteractionCallbackResponse": ".update_message_interaction_callback_response",
    "UpdateOnboardingPromptRequest": ".update_onboarding_prompt_request",
    "UpdateThreadRequestPartial": ".update_thread_request_partial",
    "UpdateThreadTagRequest": ".update_thread_tag_request",
    "UpdateWebhookByTokenResponse": ".update_webhook_by_token_response",
    "UpdateWebhookResponse": ".update_webhook_response",
    "UserAvatarDecorationResponse": ".user_avatar_decoration_response",
    "UserCollectiblesResponse": ".user_collectibles_response",
    "UserCommunicationDisabledAction": ".user_communication_disabled_action",
    "UserCommunicationDisabledActionMetadata": ".user_communication_disabled_action_metadata",
    "UserCommunicationDisabledActionMetadataResponse": ".user_communication_disabled_action_metadata_response",
    "UserCommunicationDisabledActionResponse": ".user_communication_disabled_action_response",
    "UserGuildOnboardingResponse": ".user_guild_onboarding_response",
    "UserNameplateResponse": ".user_nameplate_response",
    "UserNotificationSettings": ".user_notification_settings",
    "UserPiiResponse": ".user_pii_response",
    "UserPrimaryGuildResponse": ".user_primary_guild_response",
    "UserResponse": ".user_response",
    "UserSelectComponentForMessageRequest": ".user_select_component_for_message_request",
    "UserSelectComponentResponse": ".user_select_component_response",
    "UserSelectDefaultValue": ".user_select_default_value",
    "UserSelectDefaultValueResponse": ".user_select_default_value_response",
    "UserSelectDefaultValueResponseType": ".user_select_default_value_response_type",
    "UserSelectDefaultValueType": ".user_select_default_value_type",
    "VanityUrlErrorResponse": ".vanity_url_error_response",
    "VanityUrlResponse": ".vanity_url_response",
    "VerificationLevels": ".verification_levels",
    "VideoQualityModes": ".video_quality_modes",
    "VoiceRegionResponse": ".voice_region_response",
    "VoiceScheduledEventCreateRequest": ".voice_scheduled_event_create_request",
    "VoiceScheduledEventPatchRequestPartial": ".voice_scheduled_event_patch_request_partial",
    "VoiceScheduledEventResponse": ".voice_scheduled_event_response",
    "VoiceStateResponse": ".voice_state_response",
    "WebhookSlackEmbed": ".webhook_slack_embed",
    "WebhookSlackEmbedField": ".webhook_slack_embed_field",
    "WebhookSourceChannelResponse": ".webhook_source_channel_response",
    "WebhookSourceGuildResponse": ".webhook_source_guild_response",
    "WebhookTypes": ".webhook_types",
    "WelcomeMessageResponse": ".welcome_message_response",
    "WidgetActivity": ".widget_activity",
    "WidgetChannel": ".widget_channel",
    "WidgetImageStyles": ".widget_image_styles",
    "WidgetMember": ".widget_member",
    "WidgetResponse": ".widget_response",
    "WidgetSettingsResponse": ".widget_settings_response",
    "WidgetUserDiscriminator": ".widget_user_discriminator",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AccountResponse",
    "ActionRowComponentForMessageRequest",
    "ActionRowComponentForMessageRequestComponentsItem",
    "ActionRowComponentForModalRequest",
    "ActionRowComponentResponse",
    "ActionRowComponentResponseComponentsItem",
    "ActivitiesAttachmentResponse",
    "AddGroupDmUserResponse",
    "AfkTimeouts",
    "AllowedMentionTypes",
    "ApplicationCommandAttachmentOption",
    "ApplicationCommandAttachmentOptionResponse",
    "ApplicationCommandAutocompleteCallbackRequest",
    "ApplicationCommandAutocompleteCallbackRequestData",
    "ApplicationCommandBooleanOption",
    "ApplicationCommandBooleanOptionResponse",
    "ApplicationCommandChannelOption",
    "ApplicationCommandChannelOptionResponse",
    "ApplicationCommandCreateRequest",
    "ApplicationCommandCreateRequestOptionsItem",
    "ApplicationCommandHandler",
    "ApplicationCommandIntegerOption",
    "ApplicationCommandIntegerOptionResponse",
    "ApplicationCommandInteractionMetadataResponse",
    "ApplicationCommandMentionableOption",
    "ApplicationCommandMentionableOptionResponse",
    "ApplicationCommandNumberOption",
    "ApplicationCommandNumberOptionResponse",
    "ApplicationCommandOptionIntegerChoice",
    "ApplicationCommandOptionIntegerChoiceResponse",
    "ApplicationCommandOptionNumberChoice",
    "ApplicationCommandOptionNumberChoiceResponse",
    "ApplicationCommandOptionStringChoice",
    "ApplicationCommandOptionStringChoiceResponse",
    "ApplicationCommandOptionType",
    "ApplicationCommandPatchRequestPartial",
    "ApplicationCommandPatchRequestPartialOptionsItem",
    "ApplicationCommandPermission",
    "ApplicationCommandPermissionType",
    "ApplicationCommandResponse",
    "ApplicationCommandResponseOptionsItem",
    "ApplicationCommandRoleOption",
    "ApplicationCommandRoleOptionResponse",
    "ApplicationCommandStringOption",
    "ApplicationCommandStringOptionResponse",
    "ApplicationCommandSubcommandGroupOption",
    "ApplicationCommandSubcommandGroupOptionResponse",
    "ApplicationCommandSubcommandOption",
    "ApplicationCommandSubcommandOptionOptionsItem",
    "ApplicationCommandSubcommandOptionResponse",
    "ApplicationCommandSubcommandOptionResponseOptionsItem",
    "ApplicationCommandType",
    "ApplicationCommandUpdateRequest",
    "ApplicationCommandUpdateRequestOptionsItem",
    "ApplicationCommandUserOption",
    "ApplicationCommandUserOptionResponse",
    "ApplicationExplicitContentFilterTypes",
    "ApplicationFormPartial",
    "ApplicationFormPartialDescription",
    "ApplicationIdentityProviderAuthType",
    "ApplicationIncomingWebhookResponse",
    "ApplicationIntegrationType",
    "ApplicationIntegrationTypeConfiguration",
    "ApplicationIntegrationTypeConfigurationResponse",
    "ApplicationOAuth2InstallParams",
    "ApplicationOAuth2InstallParamsResponse",
    "ApplicationOAuth2InstallParamsResponseScopesItem",
    "ApplicationOAuth2InstallParamsScopesItem",
    "ApplicationResponse",
    "ApplicationRoleConnectionsMetadataItemRequest",
    "ApplicationRoleConnectionsMetadataItemResponse",
    "ApplicationTypes",
    "ApplicationUserRoleConnectionResponse",
    "AttachmentResponse",
    "AuditLogActionTypes",
    "AuditLogEntryResponse",
    "AuditLogObjectChangeResponse",
    "AutomodActionType",
    "AutomodEventType",
    "AutomodKeywordPresetType",
    "AutomodTriggerType",
    "AvailableLocalesEnum",
    "BaseCreateMessageCreateRequest",
    "BasicApplicationResponse",
    "BasicMessageResponse",
    "BasicMessageResponseInteractionMetadata",
    "BasicMessageResponseNonce",
    "BasicMessageResponseStickersItem",
    "BlockMessageAction",
    "BlockMessageActionMetadata",
    "BlockMessageActionMetadataResponse",
    "BlockMessageActionResponse",
    "BulkBanUsersResponse",
    "BulkUpdateGuildChannelsRequestBodyItem",
    "BulkUpdateGuildRolesRequestBodyItem",
    "ButtonComponentForMessageRequest",
    "ButtonComponentResponse",
    "ButtonStyleTypes",
    "ChannelFollowerResponse",
    "ChannelFollowerWebhookResponse",
    "ChannelPermissionOverwriteRequest",
    "ChannelPermissionOverwriteResponse",
    "ChannelPermissionOverwrites",
    "ChannelSelectComponentForMessageRequest",
    "ChannelSelectComponentResponse",
    "ChannelSelectDefaultValue",
    "ChannelSelectDefaultValueResponse",
    "ChannelSelectDefaultValueResponseType",
    "ChannelSelectDefaultValueType",
    "ChannelTypes",
    "CommandPermissionResponse",
    "CommandPermissionsResponse",
    "ComponentEmojiForMessageRequest",
    "ComponentEmojiResponse",
    "ConfettiPotionCreateRequest",
    "ConnectedAccountGuildResponse",
    "ConnectedAccountIntegrationResponse",
    "ConnectedAccountProviders",
    "ConnectedAccountResponse",
    "ConnectedAccountVisibility",
    "CreateAutoModerationRuleRequestBody",
    "CreateAutoModerationRuleResponse",
    "CreateChannelInviteRequestBody",
    "CreateChannelInviteResponse",
    "CreateDmResponse",
    "CreateForumThreadRequest",
    "CreateGroupDmInviteRequest",
    "CreateGuildInviteRequest",
    "CreateGuildRequestChannelItem",
    "CreateGuildRequestRoleItem",
    "CreateGuildScheduledEventRequestBody",
    "CreateGuildScheduledEventResponse",
    "CreateInteractionResponseRequestBody",
    "CreateMessageInteractionCallbackRequest",
    "CreateMessageInteractionCallbackResponse",
    "CreateOrUpdateThreadTagRequest",
    "CreateTextThreadWithoutMessageRequest",
    "CreateThreadRequestBody",
    "CreatedThreadResponse",
    "DefaultKeywordListTriggerMetadata",
    "DefaultKeywordListTriggerMetadataResponse",
    "DefaultKeywordListUpsertRequest",
    "DefaultKeywordListUpsertRequestActionsItem",
    "DefaultKeywordListUpsertRequestPartial",
    "DefaultKeywordListUpsertRequestPartialActionsItem",
    "DefaultKeywordRuleResponse",
    "DefaultKeywordRuleResponseActionsItem",
    "DefaultReactionEmojiResponse",
    "DeleteChannelResponse",
    "DiscordIntegrationResponse",
    "DiscordIntegrationResponseScopesItem",
    "DiscordIntegrationResponseType",
    "EmbeddedActivityInstance",
    "EmbeddedActivityInstanceLocation",
    "EmbeddedActivityLocationKind",
    "EmojiResponse",
    "EntitlementOwnerTypes",
    "EntitlementResponse",
    "EntitlementTenantFulfillmentStatusResponse",
    "EntitlementTypes",
    "EntityMetadataExternal",
    "EntityMetadataExternalResponse",
    "EntityMetadataStageInstance",
    "EntityMetadataStageInstanceResponse",
    "EntityMetadataVoice",
    "EntityMetadataVoiceResponse",
    "Error",
    "ErrorDetails",
    "ErrorResponse",
    "ExecuteWebhookRequestBody",
    "ExternalConnectionIntegrationResponse",
    "ExternalConnectionIntegrationResponseType",
    "ExternalScheduledEventCreateRequest",
    "ExternalScheduledEventPatchRequestPartial",
    "ExternalScheduledEventResponse",
    "FlagToChannelAction",
    "FlagToChannelActionMetadata",
    "FlagToChannelActionMetadataResponse",
    "FlagToChannelActionResponse",
    "ForumLayout",
    "ForumTagResponse",
    "FriendInviteResponse",
    "GatewayBotResponse",
    "GatewayBotSessionStartLimitResponse",
    "GatewayResponse",
    "GetAutoModerationRuleResponse",
    "GetChannelResponse",
    "GetEntitlementsRequestSkuIds",
    "GetGuildScheduledEventResponse",
    "GetGuildWebhooksResponseItem",
    "GetStickerResponse",
    "GetWebhookByTokenResponse",
    "GetWebhookResponse",
    "GithubAuthor",
    "GithubCheckApp",
    "GithubCheckPullRequest",
    "GithubCheckRun",
    "GithubCheckRunOutput",
    "GithubCheckSuite",
    "GithubComment",
    "GithubCommit",
    "GithubDiscussion",
    "GithubIssue",
    "GithubRelease",
    "GithubRepository",
    "GithubReview",
    "GithubUser",
    "GroupDmInviteResponse",
    "GuildAuditLogResponse",
    "GuildAuditLogResponseAutoModerationRulesItem",
    "GuildAuditLogResponseGuildScheduledEventsItem",
    "GuildAuditLogResponseIntegrationsItem",
    "GuildAuditLogResponseWebhooksItem",
    "GuildBanResponse",
    "GuildChannelLocation",
    "GuildChannelLocationKind",
    "GuildChannelResponse",
    "GuildExplicitContentFilterTypes",
    "GuildFeatures",
    "GuildHomeSettingsResponse",
    "GuildIncomingWebhookResponse",
    "GuildInviteResponse",
    "GuildMemberResponse",
    "GuildMfaLevel",
    "GuildMfaLevelResponse",
    "GuildNsfwContentLevel",
    "GuildOnboardingMode",
    "GuildOnboardingResponse",
    "GuildPreviewResponse",
    "GuildProductPurchaseResponse",
    "GuildPruneResponse",
    "GuildResponse",
    "GuildRoleResponse",
    "GuildRoleTagsResponse",
    "GuildScheduledEventEntityTypes",
    "GuildScheduledEventPrivacyLevels",
    "GuildScheduledEventStatuses",
    "GuildStickerResponse",
    "GuildSubscriptionIntegrationResponse",
    "GuildSubscriptionIntegrationResponseType",
    "GuildTemplateChannelResponse",
    "GuildTemplateChannelTags",
    "GuildTemplateResponse",
    "GuildTemplateRoleResponse",
    "GuildTemplateSnapshotResponse",
    "GuildWelcomeChannel",
    "GuildWelcomeScreenChannelResponse",
    "GuildWelcomeScreenResponse",
    "GuildWithCountsResponse",
    "IconEmojiResponse",
    "IncomingWebhookInteractionRequest",
    "IncomingWebhookRequestPartial",
    "IncomingWebhookUpdateForInteractionCallbackRequestPartial",
    "IncomingWebhookUpdateRequestPartial",
    "InnerErrors",
    "Int53Type",
    "IntegrationApplicationResponse",
    "IntegrationExpireBehaviorTypes",
    "IntegrationExpireGracePeriodTypes",
    "IntegrationTypes",
    "InteractionApplicationCommandAutocompleteCallbackIntegerData",
    "InteractionApplicationCommandAutocompleteCallbackNumberData",
    "InteractionApplicationCommandAutocompleteCallbackStringData",
    "InteractionCallbackResponse",
    "InteractionCallbackResponseResource",
    "InteractionCallbackTypes",
    "InteractionContextType",
    "InteractionResponse",
    "InteractionTypes",
    "InviteApplicationResponse",
    "InviteChannelRecipientResponse",
    "InviteChannelResponse",
    "InviteGuildResponse",
    "InviteResolveResponse",
    "InviteRevokeResponse",
    "InviteStageInstanceResponse",
    "InviteTargetTypes",
    "InviteTypes",
    "KeywordRuleResponse",
    "KeywordRuleResponseActionsItem",
    "KeywordTriggerMetadata",
    "KeywordTriggerMetadataResponse",
    "KeywordUpsertRequest",
    "KeywordUpsertRequestActionsItem",
    "KeywordUpsertRequestPartial",
    "KeywordUpsertRequestPartialActionsItem",
    "LaunchActivityInteractionCallbackRequest",
    "LaunchActivityInteractionCallbackResponse",
    "ListApplicationEmojisResponse",
    "ListAutoModerationRulesResponseItem",
    "ListChannelInvitesResponseItem",
    "ListChannelWebhooksResponseItem",
    "ListGuildChannelsResponseItem",
    "ListGuildIntegrationsResponseItem",
    "ListGuildInvitesResponseItem",
    "ListGuildScheduledEventsResponseItem",
    "ListGuildSoundboardSoundsResponse",
    "LobbyMemberRequest",
    "LobbyMemberResponse",
    "LobbyMessageResponse",
    "LobbyResponse",
    "MentionSpamRuleResponse",
    "MentionSpamRuleResponseActionsItem",
    "MentionSpamTriggerMetadata",
    "MentionSpamTriggerMetadataResponse",
    "MentionSpamUpsertRequest",
    "MentionSpamUpsertRequestActionsItem",
    "MentionSpamUpsertRequestPartial",
    "MentionSpamUpsertRequestPartialActionsItem",
    "MentionableSelectComponentForMessageRequest",
    "MentionableSelectComponentForMessageRequestDefaultValuesItem",
    "MentionableSelectComponentForMessageRequestDefaultValuesItem_Role",
    "MentionableSelectComponentForMessageRequestDefaultValuesItem_User",
    "MentionableSelectComponentResponse",
    "MentionableSelectComponentResponseDefaultValuesItem",
    "MentionableSelectComponentResponseDefaultValuesItem_Role",
    "MentionableSelectComponentResponseDefaultValuesItem_User",
    "MessageActivityResponse",
    "MessageAllowedMentionsRequest",
    "MessageAttachmentRequest",
    "MessageAttachmentResponse",
    "MessageCallResponse",
    "MessageComponentInteractionMetadataResponse",
    "MessageComponentTypes",
    "MessageCreateRequestNonce",
    "MessageEmbedAuthorResponse",
    "MessageEmbedFieldResponse",
    "MessageEmbedFooterResponse",
    "MessageEmbedImageResponse",
    "MessageEmbedProviderResponse",
    "MessageEmbedResponse",
    "MessageEmbedVideoResponse",
    "MessageInteractionResponse",
    "MessageMentionChannelResponse",
    "MessageReactionCountDetailsResponse",
    "MessageReactionEmojiResponse",
    "MessageReactionResponse",
    "MessageReferenceRequest",
    "MessageReferenceResponse",
    "MessageReferenceType",
    "MessageResponse",
    "MessageResponseInteractionMetadata",
    "MessageResponseNonce",
    "MessageResponseStickersItem",
    "MessageRoleSubscriptionDataResponse",
    "MessageSnapshotResponse",
    "MessageStickerItemResponse",
    "MessageType",
    "MetadataItemTypes",
    "MinimalContentMessageResponse",
    "MinimalContentMessageResponseStickersItem",
    "MlSpamRuleResponse",
    "MlSpamRuleResponseActionsItem",
    "MlSpamTriggerMetadata",
    "MlSpamTriggerMetadataResponse",
    "MlSpamUpsertRequest",
    "MlSpamUpsertRequestActionsItem",
    "MlSpamUpsertRequestPartial",
    "MlSpamUpsertRequestPartialActionsItem",
    "ModalInteractionCallbackRequest",
    "ModalInteractionCallbackRequestData",
    "ModalSubmitInteractionMetadataResponse",
    "ModalSubmitInteractionMetadataResponseTriggeringInteractionMetadata",
    "MyGuildResponse",
    "NameplatePalette",
    "NewMemberActionResponse",
    "NewMemberActionType",
    "OAuth2GetAuthorizationResponse",
    "OAuth2GetKeys",
    "OAuth2GetOpenIdConnectUserInfoResponse",
    "OAuth2Key",
    "OAuth2Scopes",
    "OauthScope",
    "OnboardingPromptOptionRequest",
    "OnboardingPromptOptionResponse",
    "OnboardingPromptResponse",
    "OnboardingPromptType",
    "PartialDiscordIntegrationResponse",
    "PartialDiscordIntegrationResponseType",
    "PartialExternalConnectionIntegrationResponse",
    "PartialExternalConnectionIntegrationResponseType",
    "PartialGuildSubscriptionIntegrationResponse",
    "PartialGuildSubscriptionIntegrationResponseType",
    "PollAnswerCreateRequest",
    "PollAnswerDetailsResponse",
    "PollAnswerResponse",
    "PollCreateRequest",
    "PollEmoji",
    "PollEmojiCreateRequest",
    "PollLayoutTypes",
    "PollMedia",
    "PollMediaCreateRequest",
    "PollMediaResponse",
    "PollResponse",
    "PollResultsEntryResponse",
    "PollResultsResponse",
    "PongInteractionCallbackRequest",
    "PremiumGuildTiers",
    "PremiumTypes",
    "PreviewPruneGuildRequestIncludeRoles",
    "PrivateApplicationResponse",
    "PrivateChannelLocation",
    "PrivateChannelLocationKind",
    "PrivateChannelResponse",
    "PrivateGroupChannelResponse",
    "PrivateGuildMemberResponse",
    "ProvisionalTokenResponse",
    "PruneGuildRequestIncludeRoles",
    "PurchaseNotificationResponse",
    "PurchaseType",
    "QuarantineUserAction",
    "QuarantineUserActionMetadata",
    "QuarantineUserActionMetadataResponse",
    "QuarantineUserActionResponse",
    "ReactionTypes",
    "ResolvedObjectsResponse",
    "ResolvedObjectsResponseChannelsValue",
    "ResourceChannelResponse",
    "RichEmbed",
    "RichEmbedAuthor",
    "RichEmbedField",
    "RichEmbedFooter",
    "RichEmbedImage",
    "RichEmbedProvider",
    "RichEmbedThumbnail",
    "RichEmbedVideo",
    "RoleSelectComponentForMessageRequest",
    "RoleSelectComponentResponse",
    "RoleSelectDefaultValue",
    "RoleSelectDefaultValueResponse",
    "RoleSelectDefaultValueResponseType",
    "RoleSelectDefaultValueType",
    "ScheduledEventResponse",
    "ScheduledEventUserResponse",
    "SdkMessageRequestNonce",
    "SettingsEmojiResponse",
    "SnowflakeSelectDefaultValueTypes",
    "SnowflakeType",
    "SortingOrder",
    "SoundboardSoundResponse",
    "SpamLinkRuleResponse",
    "SpamLinkRuleResponseActionsItem",
    "SpamLinkTriggerMetadataResponse",
    "StageInstanceResponse",
    "StageInstancesPrivacyLevels",
    "StageScheduledEventCreateRequest",
    "StageScheduledEventPatchRequestPartial",
    "StageScheduledEventResponse",
    "StandardStickerResponse",
    "StickerFormatTypes",
    "StickerPackCollectionResponse",
    "StickerPackResponse",
    "StickerTypes",
    "StringSelectComponentForMessageRequest",
    "StringSelectComponentResponse",
    "StringSelectOptionForMessageRequest",
    "StringSelectOptionResponse",
    "TeamMemberResponse",
    "TeamMembershipStates",
    "TeamResponse",
    "TextInputComponentForModalRequest",
    "TextInputComponentResponse",
    "TextInputStyleTypes",
    "ThreadAutoArchiveDuration",
    "ThreadMemberResponse",
    "ThreadMetadataResponse",
    "ThreadResponse",
    "ThreadSearchRequestTag",
    "ThreadSearchResponse",
    "ThreadSearchTagSetting",
    "ThreadSortOrder",
    "ThreadSortingMode",
    "ThreadsResponse",
    "TypingIndicatorResponse",
    "UInt32Type",
    "UpdateAutoModerationRuleRequestBody",
    "UpdateAutoModerationRuleResponse",
    "UpdateChannelRequestBody",
    "UpdateChannelResponse",
    "UpdateDefaultReactionEmojiRequest",
    "UpdateDmRequestPartial",
    "UpdateGroupDmRequestPartial",
    "UpdateGuildChannelRequestPartial",
    "UpdateGuildScheduledEventRequestBody",
    "UpdateGuildScheduledEventResponse",
    "UpdateMessageInteractionCallbackRequest",
    "UpdateMessageInteractionCallbackResponse",
    "UpdateOnboardingPromptRequest",
    "UpdateThreadRequestPartial",
    "UpdateThreadTagRequest",
    "UpdateWebhookByTokenResponse",
    "UpdateWebhookResponse",
    "UserAvatarDecorationResponse",
    "UserCollectiblesResponse",
    "UserCommunicationDisabledAction",
    "UserCommunicationDisabledActionMetadata",
    "UserCommunicationDisabledActionMetadataResponse",
    "UserCommunicationDisabledActionResponse",
    "UserGuildOnboardingResponse",
    "UserNameplateResponse",
    "UserNotificationSettings",
    "UserPiiResponse",
    "UserPrimaryGuildResponse",
    "UserResponse",
    "UserSelectComponentForMessageRequest",
    "UserSelectComponentResponse",
    "UserSelectDefaultValue",
    "UserSelectDefaultValueResponse",
    "UserSelectDefaultValueResponseType",
    "UserSelectDefaultValueType",
    "VanityUrlErrorResponse",
    "VanityUrlResponse",
    "VerificationLevels",
    "VideoQualityModes",
    "VoiceRegionResponse",
    "VoiceScheduledEventCreateRequest",
    "VoiceScheduledEventPatchRequestPartial",
    "VoiceScheduledEventResponse",
    "VoiceStateResponse",
    "WebhookSlackEmbed",
    "WebhookSlackEmbedField",
    "WebhookSourceChannelResponse",
    "WebhookSourceGuildResponse",
    "WebhookTypes",
    "WelcomeMessageResponse",
    "WidgetActivity",
    "WidgetChannel",
    "WidgetImageStyles",
    "WidgetMember",
    "WidgetResponse",
    "WidgetSettingsResponse",
    "WidgetUserDiscriminator",
]
