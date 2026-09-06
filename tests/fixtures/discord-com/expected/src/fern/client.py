

import datetime as dt
import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.action_row_component_for_message_request import ActionRowComponentForMessageRequest
from .types.activities_attachment_response import ActivitiesAttachmentResponse
from .types.add_group_dm_user_response import AddGroupDmUserResponse
from .types.afk_timeouts import AfkTimeouts
from .types.application_command_create_request_options_item import ApplicationCommandCreateRequestOptionsItem
from .types.application_command_handler import ApplicationCommandHandler
from .types.application_command_patch_request_partial_options_item import (
    ApplicationCommandPatchRequestPartialOptionsItem,
)
from .types.application_command_permission import ApplicationCommandPermission
from .types.application_command_response import ApplicationCommandResponse
from .types.application_command_type import ApplicationCommandType
from .types.application_command_update_request import ApplicationCommandUpdateRequest
from .types.application_explicit_content_filter_types import ApplicationExplicitContentFilterTypes
from .types.application_form_partial_description import ApplicationFormPartialDescription
from .types.application_identity_provider_auth_type import ApplicationIdentityProviderAuthType
from .types.application_integration_type import ApplicationIntegrationType
from .types.application_integration_type_configuration import ApplicationIntegrationTypeConfiguration
from .types.application_o_auth2install_params import ApplicationOAuth2InstallParams
from .types.application_role_connections_metadata_item_request import ApplicationRoleConnectionsMetadataItemRequest
from .types.application_role_connections_metadata_item_response import ApplicationRoleConnectionsMetadataItemResponse
from .types.application_types import ApplicationTypes
from .types.application_user_role_connection_response import ApplicationUserRoleConnectionResponse
from .types.available_locales_enum import AvailableLocalesEnum
from .types.bulk_ban_users_response import BulkBanUsersResponse
from .types.bulk_update_guild_channels_request_body_item import BulkUpdateGuildChannelsRequestBodyItem
from .types.bulk_update_guild_roles_request_body_item import BulkUpdateGuildRolesRequestBodyItem
from .types.channel_follower_response import ChannelFollowerResponse
from .types.channel_permission_overwrite_request import ChannelPermissionOverwriteRequest
from .types.channel_permission_overwrites import ChannelPermissionOverwrites
from .types.command_permissions_response import CommandPermissionsResponse
from .types.confetti_potion_create_request import ConfettiPotionCreateRequest
from .types.connected_account_response import ConnectedAccountResponse
from .types.create_auto_moderation_rule_request_body import CreateAutoModerationRuleRequestBody
from .types.create_auto_moderation_rule_response import CreateAutoModerationRuleResponse
from .types.create_channel_invite_request_body import CreateChannelInviteRequestBody
from .types.create_channel_invite_response import CreateChannelInviteResponse
from .types.create_dm_response import CreateDmResponse
from .types.create_guild_request_channel_item import CreateGuildRequestChannelItem
from .types.create_guild_request_role_item import CreateGuildRequestRoleItem
from .types.create_guild_scheduled_event_request_body import CreateGuildScheduledEventRequestBody
from .types.create_guild_scheduled_event_response import CreateGuildScheduledEventResponse
from .types.create_interaction_response_request_body import CreateInteractionResponseRequestBody
from .types.create_or_update_thread_tag_request import CreateOrUpdateThreadTagRequest
from .types.create_thread_request_body import CreateThreadRequestBody
from .types.created_thread_response import CreatedThreadResponse
from .types.delete_channel_response import DeleteChannelResponse
from .types.embedded_activity_instance import EmbeddedActivityInstance
from .types.emoji_response import EmojiResponse
from .types.entitlement_owner_types import EntitlementOwnerTypes
from .types.entitlement_response import EntitlementResponse
from .types.execute_webhook_request_body import ExecuteWebhookRequestBody
from .types.forum_layout import ForumLayout
from .types.gateway_bot_response import GatewayBotResponse
from .types.gateway_response import GatewayResponse
from .types.get_auto_moderation_rule_response import GetAutoModerationRuleResponse
from .types.get_channel_response import GetChannelResponse
from .types.get_entitlements_request_sku_ids import GetEntitlementsRequestSkuIds
from .types.get_guild_scheduled_event_response import GetGuildScheduledEventResponse
from .types.get_guild_webhooks_response_item import GetGuildWebhooksResponseItem
from .types.get_sticker_response import GetStickerResponse
from .types.get_webhook_by_token_response import GetWebhookByTokenResponse
from .types.get_webhook_response import GetWebhookResponse
from .types.github_check_run import GithubCheckRun
from .types.github_check_suite import GithubCheckSuite
from .types.github_comment import GithubComment
from .types.github_commit import GithubCommit
from .types.github_discussion import GithubDiscussion
from .types.github_issue import GithubIssue
from .types.github_release import GithubRelease
from .types.github_repository import GithubRepository
from .types.github_review import GithubReview
from .types.github_user import GithubUser
from .types.guild_audit_log_response import GuildAuditLogResponse
from .types.guild_ban_response import GuildBanResponse
from .types.guild_channel_response import GuildChannelResponse
from .types.guild_explicit_content_filter_types import GuildExplicitContentFilterTypes
from .types.guild_home_settings_response import GuildHomeSettingsResponse
from .types.guild_incoming_webhook_response import GuildIncomingWebhookResponse
from .types.guild_member_response import GuildMemberResponse
from .types.guild_mfa_level import GuildMfaLevel
from .types.guild_mfa_level_response import GuildMfaLevelResponse
from .types.guild_onboarding_mode import GuildOnboardingMode
from .types.guild_onboarding_response import GuildOnboardingResponse
from .types.guild_preview_response import GuildPreviewResponse
from .types.guild_prune_response import GuildPruneResponse
from .types.guild_response import GuildResponse
from .types.guild_role_response import GuildRoleResponse
from .types.guild_sticker_response import GuildStickerResponse
from .types.guild_template_response import GuildTemplateResponse
from .types.guild_welcome_channel import GuildWelcomeChannel
from .types.guild_welcome_screen_response import GuildWelcomeScreenResponse
from .types.guild_with_counts_response import GuildWithCountsResponse
from .types.interaction_callback_response import InteractionCallbackResponse
from .types.interaction_context_type import InteractionContextType
from .types.invite_resolve_response import InviteResolveResponse
from .types.invite_revoke_response import InviteRevokeResponse
from .types.list_application_emojis_response import ListApplicationEmojisResponse
from .types.list_auto_moderation_rules_response_item import ListAutoModerationRulesResponseItem
from .types.list_channel_invites_response_item import ListChannelInvitesResponseItem
from .types.list_channel_webhooks_response_item import ListChannelWebhooksResponseItem
from .types.list_guild_channels_response_item import ListGuildChannelsResponseItem
from .types.list_guild_integrations_response_item import ListGuildIntegrationsResponseItem
from .types.list_guild_invites_response_item import ListGuildInvitesResponseItem
from .types.list_guild_scheduled_events_response_item import ListGuildScheduledEventsResponseItem
from .types.list_guild_soundboard_sounds_response import ListGuildSoundboardSoundsResponse
from .types.lobby_member_request import LobbyMemberRequest
from .types.lobby_member_response import LobbyMemberResponse
from .types.lobby_message_response import LobbyMessageResponse
from .types.lobby_response import LobbyResponse
from .types.message_allowed_mentions_request import MessageAllowedMentionsRequest
from .types.message_attachment_request import MessageAttachmentRequest
from .types.message_create_request_nonce import MessageCreateRequestNonce
from .types.message_reference_request import MessageReferenceRequest
from .types.message_response import MessageResponse
from .types.my_guild_response import MyGuildResponse
from .types.o_auth2get_authorization_response import OAuth2GetAuthorizationResponse
from .types.o_auth2get_keys import OAuth2GetKeys
from .types.o_auth2get_open_id_connect_user_info_response import OAuth2GetOpenIdConnectUserInfoResponse
from .types.poll_answer_details_response import PollAnswerDetailsResponse
from .types.poll_create_request import PollCreateRequest
from .types.preview_prune_guild_request_include_roles import PreviewPruneGuildRequestIncludeRoles
from .types.private_application_response import PrivateApplicationResponse
from .types.private_guild_member_response import PrivateGuildMemberResponse
from .types.provisional_token_response import ProvisionalTokenResponse
from .types.prune_guild_request_include_roles import PruneGuildRequestIncludeRoles
from .types.reaction_types import ReactionTypes
from .types.rich_embed import RichEmbed
from .types.scheduled_event_user_response import ScheduledEventUserResponse
from .types.sdk_message_request_nonce import SdkMessageRequestNonce
from .types.snowflake_type import SnowflakeType
from .types.sorting_order import SortingOrder
from .types.soundboard_sound_response import SoundboardSoundResponse
from .types.stage_instance_response import StageInstanceResponse
from .types.stage_instances_privacy_levels import StageInstancesPrivacyLevels
from .types.sticker_pack_collection_response import StickerPackCollectionResponse
from .types.sticker_pack_response import StickerPackResponse
from .types.thread_auto_archive_duration import ThreadAutoArchiveDuration
from .types.thread_member_response import ThreadMemberResponse
from .types.thread_response import ThreadResponse
from .types.thread_search_request_tag import ThreadSearchRequestTag
from .types.thread_search_response import ThreadSearchResponse
from .types.thread_search_tag_setting import ThreadSearchTagSetting
from .types.thread_sort_order import ThreadSortOrder
from .types.thread_sorting_mode import ThreadSortingMode
from .types.threads_response import ThreadsResponse
from .types.typing_indicator_response import TypingIndicatorResponse
from .types.update_auto_moderation_rule_request_body import UpdateAutoModerationRuleRequestBody
from .types.update_auto_moderation_rule_response import UpdateAutoModerationRuleResponse
from .types.update_channel_request_body import UpdateChannelRequestBody
from .types.update_channel_response import UpdateChannelResponse
from .types.update_default_reaction_emoji_request import UpdateDefaultReactionEmojiRequest
from .types.update_guild_scheduled_event_request_body import UpdateGuildScheduledEventRequestBody
from .types.update_guild_scheduled_event_response import UpdateGuildScheduledEventResponse
from .types.update_onboarding_prompt_request import UpdateOnboardingPromptRequest
from .types.update_webhook_by_token_response import UpdateWebhookByTokenResponse
from .types.update_webhook_response import UpdateWebhookResponse
from .types.user_guild_onboarding_response import UserGuildOnboardingResponse
from .types.user_notification_settings import UserNotificationSettings
from .types.user_pii_response import UserPiiResponse
from .types.user_response import UserResponse
from .types.vanity_url_response import VanityUrlResponse
from .types.verification_levels import VerificationLevels
from .types.video_quality_modes import VideoQualityModes
from .types.voice_region_response import VoiceRegionResponse
from .types.voice_state_response import VoiceStateResponse
from .types.webhook_slack_embed import WebhookSlackEmbed
from .types.widget_image_styles import WidgetImageStyles
from .types.widget_response import WidgetResponse
from .types.widget_settings_response import WidgetSettingsResponse


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def partner_sdk_unmerge_provisional_account(
        self,
        *,
        client_id: SnowflakeType,
        external_auth_token: str,
        external_auth_type: ApplicationIdentityProviderAuthType,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        client_id : SnowflakeType

        external_auth_token : str

        external_auth_type : ApplicationIdentityProviderAuthType

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.partner_sdk_unmerge_provisional_account(
            client_id="client_id",
            external_auth_token="external_auth_token",
            external_auth_type="external_auth_type",
        )
        """
        _response = self._raw_client.partner_sdk_unmerge_provisional_account(
            client_id=client_id,
            external_auth_token=external_auth_token,
            external_auth_type=external_auth_type,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data

    def get_my_oauth2application(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PrivateApplicationResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateApplicationResponse
            200 response for get_my_oauth2_application

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_my_oauth2application()
        """
        _response = self._raw_client.get_my_oauth2application(request_options=request_options)
        return _response.data

    def list_my_connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ConnectedAccountResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ConnectedAccountResponse]]
            200 response for list_my_connections

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_my_connections()
        """
        _response = self._raw_client.list_my_connections(request_options=request_options)
        return _response.data

    def create_dm(
        self,
        *,
        recipient_id: typing.Optional[SnowflakeType] = OMIT,
        access_tokens: typing.Optional[typing.Sequence[str]] = OMIT,
        nicks: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDmResponse:
        """
        Parameters
        ----------
        recipient_id : typing.Optional[SnowflakeType]

        access_tokens : typing.Optional[typing.Sequence[str]]

        nicks : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDmResponse
            200 response for create_dm

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_dm()
        """
        _response = self._raw_client.create_dm(
            recipient_id=recipient_id, access_tokens=access_tokens, nicks=nicks, request_options=request_options
        )
        return _response.data

    def list_my_guilds(
        self,
        *,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        with_counts: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[MyGuildResponse]]:
        """
        Parameters
        ----------
        before : typing.Optional[SnowflakeType]

        after : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        with_counts : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[MyGuildResponse]]
            200 response for list_my_guilds

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_my_guilds()
        """
        _response = self._raw_client.list_my_guilds(
            before=before, after=after, limit=limit, with_counts=with_counts, request_options=request_options
        )
        return _response.data

    def get_my_application(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PrivateApplicationResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateApplicationResponse
            200 response for get_my_application

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_my_application()
        """
        _response = self._raw_client.get_my_application(request_options=request_options)
        return _response.data

    def update_my_application(
        self,
        *,
        description: typing.Optional[ApplicationFormPartialDescription] = OMIT,
        icon: typing.Optional[str] = OMIT,
        cover_image: typing.Optional[str] = OMIT,
        team_id: typing.Optional[SnowflakeType] = OMIT,
        flags: typing.Optional[int] = OMIT,
        interactions_endpoint_url: typing.Optional[str] = OMIT,
        explicit_content_filter: typing.Optional[ApplicationExplicitContentFilterTypes] = OMIT,
        max_participants: typing.Optional[int] = OMIT,
        type: typing.Optional[ApplicationTypes] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        custom_install_url: typing.Optional[str] = OMIT,
        install_params: typing.Optional[ApplicationOAuth2InstallParams] = OMIT,
        role_connections_verification_url: typing.Optional[str] = OMIT,
        integration_types_config: typing.Optional[
            typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateApplicationResponse:
        """
        Parameters
        ----------
        description : typing.Optional[ApplicationFormPartialDescription]

        icon : typing.Optional[str]

        cover_image : typing.Optional[str]

        team_id : typing.Optional[SnowflakeType]

        flags : typing.Optional[int]

        interactions_endpoint_url : typing.Optional[str]

        explicit_content_filter : typing.Optional[ApplicationExplicitContentFilterTypes]

        max_participants : typing.Optional[int]

        type : typing.Optional[ApplicationTypes]

        tags : typing.Optional[typing.Sequence[str]]

        custom_install_url : typing.Optional[str]

        install_params : typing.Optional[ApplicationOAuth2InstallParams]

        role_connections_verification_url : typing.Optional[str]

        integration_types_config : typing.Optional[typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateApplicationResponse
            200 response for update_my_application

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_my_application()
        """
        _response = self._raw_client.update_my_application(
            description=description,
            icon=icon,
            cover_image=cover_image,
            team_id=team_id,
            flags=flags,
            interactions_endpoint_url=interactions_endpoint_url,
            explicit_content_filter=explicit_content_filter,
            max_participants=max_participants,
            type=type,
            tags=tags,
            custom_install_url=custom_install_url,
            install_params=install_params,
            role_connections_verification_url=role_connections_verification_url,
            integration_types_config=integration_types_config,
            request_options=request_options,
        )
        return _response.data

    def partner_sdk_token(
        self,
        *,
        client_id: SnowflakeType,
        external_auth_token: str,
        external_auth_type: ApplicationIdentityProviderAuthType,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisionalTokenResponse:
        """
        Parameters
        ----------
        client_id : SnowflakeType

        external_auth_token : str

        external_auth_type : ApplicationIdentityProviderAuthType

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisionalTokenResponse
            200 response for partner_sdk_token

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.partner_sdk_token(
            client_id="client_id",
            external_auth_token="external_auth_token",
            external_auth_type="external_auth_type",
        )
        """
        _response = self._raw_client.partner_sdk_token(
            client_id=client_id,
            external_auth_token=external_auth_token,
            external_auth_type=external_auth_type,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data

    def get_bot_gateway(self, *, request_options: typing.Optional[RequestOptions] = None) -> GatewayBotResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GatewayBotResponse
            200 response for get_bot_gateway

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_bot_gateway()
        """
        _response = self._raw_client.get_bot_gateway(request_options=request_options)
        return _response.data

    def get_openid_connect_userinfo(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OAuth2GetOpenIdConnectUserInfoResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuth2GetOpenIdConnectUserInfoResponse
            200 response for get_openid_connect_userinfo

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_openid_connect_userinfo()
        """
        _response = self._raw_client.get_openid_connect_userinfo(request_options=request_options)
        return _response.data

    def get_public_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> OAuth2GetKeys:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuth2GetKeys
            200 response for get_public_keys

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_public_keys()
        """
        _response = self._raw_client.get_public_keys(request_options=request_options)
        return _response.data

    def get_my_oauth2authorization(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OAuth2GetAuthorizationResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuth2GetAuthorizationResponse
            200 response for get_my_oauth2_authorization

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_my_oauth2authorization()
        """
        _response = self._raw_client.get_my_oauth2authorization(request_options=request_options)
        return _response.data

    def list_voice_regions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[VoiceRegionResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[VoiceRegionResponse]]
            200 response for list_voice_regions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_voice_regions()
        """
        _response = self._raw_client.list_voice_regions(request_options=request_options)
        return _response.data

    def get_my_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserPiiResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserPiiResponse
            200 response for get_my_user

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_my_user()
        """
        _response = self._raw_client.get_my_user(request_options=request_options)
        return _response.data

    def update_my_user(
        self,
        *,
        username: str,
        avatar: typing.Optional[str] = OMIT,
        banner: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserPiiResponse:
        """
        Parameters
        ----------
        username : str

        avatar : typing.Optional[str]

        banner : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserPiiResponse
            200 response for update_my_user

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_my_user(
            username="username",
        )
        """
        _response = self._raw_client.update_my_user(
            username=username, avatar=avatar, banner=banner, request_options=request_options
        )
        return _response.data

    def get_soundboard_default_sounds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SoundboardSoundResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SoundboardSoundResponse]
            200 response for get_soundboard_default_sounds

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_soundboard_default_sounds()
        """
        _response = self._raw_client.get_soundboard_default_sounds(request_options=request_options)
        return _response.data

    def create_stage_instance(
        self,
        *,
        topic: str,
        channel_id: SnowflakeType,
        privacy_level: typing.Optional[StageInstancesPrivacyLevels] = OMIT,
        guild_scheduled_event_id: typing.Optional[SnowflakeType] = OMIT,
        send_start_notification: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StageInstanceResponse:
        """
        Parameters
        ----------
        topic : str

        channel_id : SnowflakeType

        privacy_level : typing.Optional[StageInstancesPrivacyLevels]

        guild_scheduled_event_id : typing.Optional[SnowflakeType]

        send_start_notification : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StageInstanceResponse
            200 response for create_stage_instance

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_stage_instance(
            topic="topic",
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.create_stage_instance(
            topic=topic,
            channel_id=channel_id,
            privacy_level=privacy_level,
            guild_scheduled_event_id=guild_scheduled_event_id,
            send_start_notification=send_start_notification,
            request_options=request_options,
        )
        return _response.data

    def list_sticker_packs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StickerPackCollectionResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StickerPackCollectionResponse
            200 response for list_sticker_packs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_sticker_packs()
        """
        _response = self._raw_client.list_sticker_packs(request_options=request_options)
        return _response.data

    def get_gateway(self, *, request_options: typing.Optional[RequestOptions] = None) -> GatewayResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GatewayResponse
            200 response for get_gateway

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_gateway()
        """
        _response = self._raw_client.get_gateway(request_options=request_options)
        return _response.data

    def create_lobby(
        self,
        *,
        idle_timeout_seconds: typing.Optional[int] = OMIT,
        members: typing.Optional[typing.Sequence[LobbyMemberRequest]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyResponse:
        """
        Parameters
        ----------
        idle_timeout_seconds : typing.Optional[int]

        members : typing.Optional[typing.Sequence[LobbyMemberRequest]]

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyResponse
            201 response for create_lobby

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_lobby()
        """
        _response = self._raw_client.create_lobby(
            idle_timeout_seconds=idle_timeout_seconds,
            members=members,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def create_or_join_lobby(
        self,
        *,
        secret: str,
        idle_timeout_seconds: typing.Optional[int] = OMIT,
        lobby_metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        member_metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyResponse:
        """
        Parameters
        ----------
        secret : str

        idle_timeout_seconds : typing.Optional[int]

        lobby_metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        member_metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyResponse
            200 response for create_or_join_lobby

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_or_join_lobby(
            secret="secret",
        )
        """
        _response = self._raw_client.create_or_join_lobby(
            secret=secret,
            idle_timeout_seconds=idle_timeout_seconds,
            lobby_metadata=lobby_metadata,
            member_metadata=member_metadata,
            request_options=request_options,
        )
        return _response.data

    def create_guild(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        verification_level: typing.Optional[VerificationLevels] = OMIT,
        default_message_notifications: typing.Optional[UserNotificationSettings] = OMIT,
        explicit_content_filter: typing.Optional[GuildExplicitContentFilterTypes] = OMIT,
        preferred_locale: typing.Optional[AvailableLocalesEnum] = OMIT,
        afk_timeout: typing.Optional[AfkTimeouts] = OMIT,
        roles: typing.Optional[typing.Sequence[CreateGuildRequestRoleItem]] = OMIT,
        channels: typing.Optional[typing.Sequence[CreateGuildRequestChannelItem]] = OMIT,
        afk_channel_id: typing.Optional[SnowflakeType] = OMIT,
        system_channel_id: typing.Optional[SnowflakeType] = OMIT,
        system_channel_flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildResponse:
        """
        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        region : typing.Optional[str]

        icon : typing.Optional[str]

        verification_level : typing.Optional[VerificationLevels]

        default_message_notifications : typing.Optional[UserNotificationSettings]

        explicit_content_filter : typing.Optional[GuildExplicitContentFilterTypes]

        preferred_locale : typing.Optional[AvailableLocalesEnum]

        afk_timeout : typing.Optional[AfkTimeouts]

        roles : typing.Optional[typing.Sequence[CreateGuildRequestRoleItem]]

        channels : typing.Optional[typing.Sequence[CreateGuildRequestChannelItem]]

        afk_channel_id : typing.Optional[SnowflakeType]

        system_channel_id : typing.Optional[SnowflakeType]

        system_channel_flags : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildResponse
            201 response for create_guild

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_guild(
            name="name",
        )
        """
        _response = self._raw_client.create_guild(
            name=name,
            description=description,
            region=region,
            icon=icon,
            verification_level=verification_level,
            default_message_notifications=default_message_notifications,
            explicit_content_filter=explicit_content_filter,
            preferred_locale=preferred_locale,
            afk_timeout=afk_timeout,
            roles=roles,
            channels=channels,
            afk_channel_id=afk_channel_id,
            system_channel_id=system_channel_id,
            system_channel_flags=system_channel_flags,
            request_options=request_options,
        )
        return _response.data

    def list_my_private_archived_threads(
        self,
        channel_id: SnowflakeType,
        *,
        before: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadsResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        before : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadsResponse
            200 response for list_my_private_archived_threads

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_my_private_archived_threads(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.list_my_private_archived_threads(
            channel_id, before=before, limit=limit, request_options=request_options
        )
        return _response.data

    def list_guild_application_command_permissions(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CommandPermissionsResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CommandPermissionsResponse]
            200 response for list_guild_application_command_permissions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_application_command_permissions(
            application_id="application_id",
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_application_command_permissions(
            application_id, guild_id, request_options=request_options
        )
        return _response.data

    def get_guild_application_command_permissions(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommandPermissionsResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandPermissionsResponse
            200 response for get_guild_application_command_permissions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_application_command_permissions(
            application_id="application_id",
            guild_id="guild_id",
            command_id="command_id",
        )
        """
        _response = self._raw_client.get_guild_application_command_permissions(
            application_id, guild_id, command_id, request_options=request_options
        )
        return _response.data

    def set_guild_application_command_permissions(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        permissions: typing.Optional[typing.Sequence[ApplicationCommandPermission]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommandPermissionsResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        command_id : SnowflakeType

        permissions : typing.Optional[typing.Sequence[ApplicationCommandPermission]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandPermissionsResponse
            200 response for set_guild_application_command_permissions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.set_guild_application_command_permissions(
            application_id="application_id",
            guild_id="guild_id",
            command_id="command_id",
        )
        """
        _response = self._raw_client.set_guild_application_command_permissions(
            application_id, guild_id, command_id, permissions=permissions, request_options=request_options
        )
        return _response.data

    def add_my_message_reaction(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        emoji_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.add_my_message_reaction(
            channel_id="channel_id",
            message_id="message_id",
            emoji_name="emoji_name",
        )
        """
        _response = self._raw_client.add_my_message_reaction(
            channel_id, message_id, emoji_name, request_options=request_options
        )
        return _response.data

    def delete_my_message_reaction(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        emoji_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_my_message_reaction(
            channel_id="channel_id",
            message_id="message_id",
            emoji_name="emoji_name",
        )
        """
        _response = self._raw_client.delete_my_message_reaction(
            channel_id, message_id, emoji_name, request_options=request_options
        )
        return _response.data

    def list_private_archived_threads(
        self,
        channel_id: SnowflakeType,
        *,
        before: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadsResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        before : typing.Optional[dt.datetime]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadsResponse
            200 response for list_private_archived_threads

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_private_archived_threads(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.list_private_archived_threads(
            channel_id, before=before, limit=limit, request_options=request_options
        )
        return _response.data

    def list_public_archived_threads(
        self,
        channel_id: SnowflakeType,
        *,
        before: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadsResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        before : typing.Optional[dt.datetime]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadsResponse
            200 response for list_public_archived_threads

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_public_archived_threads(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.list_public_archived_threads(
            channel_id, before=before, limit=limit, request_options=request_options
        )
        return _response.data

    def get_application_user_role_connection(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationUserRoleConnectionResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationUserRoleConnectionResponse
            200 response for get_application_user_role_connection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_application_user_role_connection(
            application_id="application_id",
        )
        """
        _response = self._raw_client.get_application_user_role_connection(
            application_id, request_options=request_options
        )
        return _response.data

    def update_application_user_role_connection(
        self,
        application_id: SnowflakeType,
        *,
        platform_name: typing.Optional[str] = OMIT,
        platform_username: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationUserRoleConnectionResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        platform_name : typing.Optional[str]

        platform_username : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationUserRoleConnectionResponse
            200 response for update_application_user_role_connection

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_application_user_role_connection(
            application_id="application_id",
        )
        """
        _response = self._raw_client.update_application_user_role_connection(
            application_id,
            platform_name=platform_name,
            platform_username=platform_username,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def delete_application_user_role_connection(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_application_user_role_connection(
            application_id="application_id",
        )
        """
        _response = self._raw_client.delete_application_user_role_connection(
            application_id, request_options=request_options
        )
        return _response.data

    def get_my_guild_member(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PrivateGuildMemberResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateGuildMemberResponse
            200 response for get_my_guild_member

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_my_guild_member(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.get_my_guild_member(guild_id, request_options=request_options)
        return _response.data

    def get_application_role_connections_metadata(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]
            200 response for get_application_role_connections_metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_application_role_connections_metadata(
            application_id="application_id",
        )
        """
        _response = self._raw_client.get_application_role_connections_metadata(
            application_id, request_options=request_options
        )
        return _response.data

    def update_application_role_connections_metadata(
        self,
        application_id: SnowflakeType,
        *,
        request: typing.Optional[typing.Sequence[ApplicationRoleConnectionsMetadataItemRequest]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request : typing.Optional[typing.Sequence[ApplicationRoleConnectionsMetadataItemRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]
            200 response for update_application_role_connections_metadata

        Examples
        --------
        from fern import ApplicationRoleConnectionsMetadataItemRequest, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_application_role_connections_metadata(
            application_id="application_id",
            request=[
                ApplicationRoleConnectionsMetadataItemRequest(
                    type=1,
                    key="key",
                    name="name",
                    description="description",
                )
            ],
        )
        """
        _response = self._raw_client.update_application_role_connections_metadata(
            application_id, request=request, request_options=request_options
        )
        return _response.data

    def consume_entitlement(
        self,
        application_id: SnowflakeType,
        entitlement_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        entitlement_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.consume_entitlement(
            application_id="application_id",
            entitlement_id="entitlement_id",
        )
        """
        _response = self._raw_client.consume_entitlement(
            application_id, entitlement_id, request_options=request_options
        )
        return _response.data

    def get_guild_application_command(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCommandResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCommandResponse
            200 response for get_guild_application_command

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_application_command(
            application_id="application_id",
            guild_id="guild_id",
            command_id="command_id",
        )
        """
        _response = self._raw_client.get_guild_application_command(
            application_id, guild_id, command_id, request_options=request_options
        )
        return _response.data

    def delete_guild_application_command(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_guild_application_command(
            application_id="application_id",
            guild_id="guild_id",
            command_id="command_id",
        )
        """
        _response = self._raw_client.delete_guild_application_command(
            application_id, guild_id, command_id, request_options=request_options
        )
        return _response.data

    def update_guild_application_command(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        options: typing.Optional[typing.Sequence[ApplicationCommandPatchRequestPartialOptionsItem]] = OMIT,
        default_member_permissions: typing.Optional[int] = OMIT,
        dm_permission: typing.Optional[bool] = OMIT,
        contexts: typing.Optional[typing.Sequence[InteractionContextType]] = OMIT,
        integration_types: typing.Optional[typing.Sequence[ApplicationIntegrationType]] = OMIT,
        handler: typing.Optional[ApplicationCommandHandler] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCommandResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        command_id : SnowflakeType

        name : typing.Optional[str]

        name_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        description : typing.Optional[str]

        description_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        options : typing.Optional[typing.Sequence[ApplicationCommandPatchRequestPartialOptionsItem]]

        default_member_permissions : typing.Optional[int]

        dm_permission : typing.Optional[bool]

        contexts : typing.Optional[typing.Sequence[InteractionContextType]]

        integration_types : typing.Optional[typing.Sequence[ApplicationIntegrationType]]

        handler : typing.Optional[ApplicationCommandHandler]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCommandResponse
            200 response for update_guild_application_command

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_guild_application_command(
            application_id="application_id",
            guild_id="guild_id",
            command_id="command_id",
        )
        """
        _response = self._raw_client.update_guild_application_command(
            application_id,
            guild_id,
            command_id,
            name=name,
            name_localizations=name_localizations,
            description=description,
            description_localizations=description_localizations,
            options=options,
            default_member_permissions=default_member_permissions,
            dm_permission=dm_permission,
            contexts=contexts,
            integration_types=integration_types,
            handler=handler,
            request_options=request_options,
        )
        return _response.data

    def list_guild_application_commands(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        with_localizations: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ApplicationCommandResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        with_localizations : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ApplicationCommandResponse]]
            200 response for list_guild_application_commands

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_application_commands(
            application_id="application_id",
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_application_commands(
            application_id, guild_id, with_localizations=with_localizations, request_options=request_options
        )
        return _response.data

    def create_guild_application_command(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        name: str,
        name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        options: typing.Optional[typing.Sequence[ApplicationCommandCreateRequestOptionsItem]] = OMIT,
        default_member_permissions: typing.Optional[int] = OMIT,
        dm_permission: typing.Optional[bool] = OMIT,
        contexts: typing.Optional[typing.Sequence[InteractionContextType]] = OMIT,
        integration_types: typing.Optional[typing.Sequence[ApplicationIntegrationType]] = OMIT,
        handler: typing.Optional[ApplicationCommandHandler] = OMIT,
        type: typing.Optional[ApplicationCommandType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCommandResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        name : str

        name_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        description : typing.Optional[str]

        description_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        options : typing.Optional[typing.Sequence[ApplicationCommandCreateRequestOptionsItem]]

        default_member_permissions : typing.Optional[int]

        dm_permission : typing.Optional[bool]

        contexts : typing.Optional[typing.Sequence[InteractionContextType]]

        integration_types : typing.Optional[typing.Sequence[ApplicationIntegrationType]]

        handler : typing.Optional[ApplicationCommandHandler]

        type : typing.Optional[ApplicationCommandType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCommandResponse
            200 response for create_guild_application_command

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_guild_application_command(
            application_id="application_id",
            guild_id="guild_id",
            name="name",
        )
        """
        _response = self._raw_client.create_guild_application_command(
            application_id,
            guild_id,
            name=name,
            name_localizations=name_localizations,
            description=description,
            description_localizations=description_localizations,
            options=options,
            default_member_permissions=default_member_permissions,
            dm_permission=dm_permission,
            contexts=contexts,
            integration_types=integration_types,
            handler=handler,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def bulk_set_guild_application_commands(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        request: typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ApplicationCommandResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        request : typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ApplicationCommandResponse]]
            200 response for bulk_set_guild_application_commands

        Examples
        --------
        from fern import ApplicationCommandUpdateRequest, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.bulk_set_guild_application_commands(
            application_id="application_id",
            guild_id="guild_id",
            request=[
                ApplicationCommandUpdateRequest(
                    name="name",
                )
            ],
        )
        """
        _response = self._raw_client.bulk_set_guild_application_commands(
            application_id, guild_id, request=request, request_options=request_options
        )
        return _response.data

    def join_thread(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.join_thread(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.join_thread(channel_id, request_options=request_options)
        return _response.data

    def leave_thread(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.leave_thread(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.leave_thread(channel_id, request_options=request_options)
        return _response.data

    def bulk_delete_messages(
        self,
        channel_id: SnowflakeType,
        *,
        messages: typing.Sequence[SnowflakeType],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        messages : typing.Sequence[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.bulk_delete_messages(
            channel_id="channel_id",
            messages=["messages"],
        )
        """
        _response = self._raw_client.bulk_delete_messages(
            channel_id, messages=messages, request_options=request_options
        )
        return _response.data

    def delete_user_message_reaction(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        emoji_name : str

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_user_message_reaction(
            channel_id="channel_id",
            message_id="message_id",
            emoji_name="emoji_name",
            user_id="user_id",
        )
        """
        _response = self._raw_client.delete_user_message_reaction(
            channel_id, message_id, emoji_name, user_id, request_options=request_options
        )
        return _response.data

    def list_message_reactions_by_emoji(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        type: typing.Optional[ReactionTypes] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[UserResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        emoji_name : str

        after : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        type : typing.Optional[ReactionTypes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserResponse]
            200 response for list_message_reactions_by_emoji

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_message_reactions_by_emoji(
            channel_id="channel_id",
            message_id="message_id",
            emoji_name="emoji_name",
        )
        """
        _response = self._raw_client.list_message_reactions_by_emoji(
            channel_id, message_id, emoji_name, after=after, limit=limit, type=type, request_options=request_options
        )
        return _response.data

    def delete_all_message_reactions_by_emoji(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        emoji_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_all_message_reactions_by_emoji(
            channel_id="channel_id",
            message_id="message_id",
            emoji_name="emoji_name",
        )
        """
        _response = self._raw_client.delete_all_message_reactions_by_emoji(
            channel_id, message_id, emoji_name, request_options=request_options
        )
        return _response.data

    def delete_all_message_reactions(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_all_message_reactions(
            channel_id="channel_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.delete_all_message_reactions(
            channel_id, message_id, request_options=request_options
        )
        return _response.data

    def crosspost_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for crosspost_message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.crosspost_message(
            channel_id="channel_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.crosspost_message(channel_id, message_id, request_options=request_options)
        return _response.data

    def create_thread_from_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        name: str,
        auto_archive_duration: typing.Optional[ThreadAutoArchiveDuration] = OMIT,
        rate_limit_per_user: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        name : str

        auto_archive_duration : typing.Optional[ThreadAutoArchiveDuration]

        rate_limit_per_user : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadResponse
            201 response for create_thread_from_message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_thread_from_message(
            channel_id="channel_id",
            message_id="message_id",
            name="name",
        )
        """
        _response = self._raw_client.create_thread_from_message(
            channel_id,
            message_id,
            name=name,
            auto_archive_duration=auto_archive_duration,
            rate_limit_per_user=rate_limit_per_user,
            request_options=request_options,
        )
        return _response.data

    def thread_search(
        self,
        channel_id: SnowflakeType,
        *,
        name: typing.Optional[str] = None,
        slop: typing.Optional[int] = None,
        min_id: typing.Optional[SnowflakeType] = None,
        max_id: typing.Optional[SnowflakeType] = None,
        tag: typing.Optional[ThreadSearchRequestTag] = None,
        tag_setting: typing.Optional[ThreadSearchTagSetting] = None,
        archived: typing.Optional[bool] = None,
        sort_by: typing.Optional[ThreadSortingMode] = None,
        sort_order: typing.Optional[SortingOrder] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadSearchResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        name : typing.Optional[str]

        slop : typing.Optional[int]

        min_id : typing.Optional[SnowflakeType]

        max_id : typing.Optional[SnowflakeType]

        tag : typing.Optional[ThreadSearchRequestTag]

        tag_setting : typing.Optional[ThreadSearchTagSetting]

        archived : typing.Optional[bool]

        sort_by : typing.Optional[ThreadSortingMode]

        sort_order : typing.Optional[SortingOrder]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadSearchResponse
            200 response for thread_search

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.thread_search(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.thread_search(
            channel_id,
            name=name,
            slop=slop,
            min_id=min_id,
            max_id=max_id,
            tag=tag,
            tag_setting=tag_setting,
            archived=archived,
            sort_by=sort_by,
            sort_order=sort_order,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def get_answer_voters(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        answer_id: int,
        *,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PollAnswerDetailsResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        answer_id : int

        after : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PollAnswerDetailsResponse
            200 response for get_answer_voters

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_answer_voters(
            channel_id="channel_id",
            message_id="message_id",
            answer_id=1,
        )
        """
        _response = self._raw_client.get_answer_voters(
            channel_id, message_id, answer_id, after=after, limit=limit, request_options=request_options
        )
        return _response.data

    def poll_expire(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for poll_expire

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.poll_expire(
            channel_id="channel_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.poll_expire(channel_id, message_id, request_options=request_options)
        return _response.data

    def get_original_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        thread_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for get_original_webhook_message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_original_webhook_message(
            webhook_id="webhook_id",
            webhook_token="webhook_token",
        )
        """
        _response = self._raw_client.get_original_webhook_message(
            webhook_id, webhook_token, thread_id=thread_id, request_options=request_options
        )
        return _response.data

    def delete_original_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        thread_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_original_webhook_message(
            webhook_id="webhook_id",
            webhook_token="webhook_token",
        )
        """
        _response = self._raw_client.delete_original_webhook_message(
            webhook_id, webhook_token, thread_id=thread_id, request_options=request_options
        )
        return _response.data

    def update_original_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        with_components: typing.Optional[bool] = None,
        content: typing.Optional[str] = OMIT,
        embeds: typing.Optional[typing.Sequence[RichEmbed]] = OMIT,
        allowed_mentions: typing.Optional[MessageAllowedMentionsRequest] = OMIT,
        components: typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]] = OMIT,
        attachments: typing.Optional[typing.Sequence[MessageAttachmentRequest]] = OMIT,
        poll: typing.Optional[PollCreateRequest] = OMIT,
        flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        thread_id : typing.Optional[SnowflakeType]

        with_components : typing.Optional[bool]

        content : typing.Optional[str]

        embeds : typing.Optional[typing.Sequence[RichEmbed]]

        allowed_mentions : typing.Optional[MessageAllowedMentionsRequest]

        components : typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]]

        attachments : typing.Optional[typing.Sequence[MessageAttachmentRequest]]

        poll : typing.Optional[PollCreateRequest]

        flags : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for update_original_webhook_message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_original_webhook_message(
            webhook_id="webhook_id",
            webhook_token="webhook_token",
        )
        """
        _response = self._raw_client.update_original_webhook_message(
            webhook_id,
            webhook_token,
            thread_id=thread_id,
            with_components=with_components,
            content=content,
            embeds=embeds,
            allowed_mentions=allowed_mentions,
            components=components,
            attachments=attachments,
            poll=poll,
            flags=flags,
            request_options=request_options,
        )
        return _response.data

    def leave_lobby(self, lobby_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.leave_lobby(
            lobby_id="lobby_id",
        )
        """
        _response = self._raw_client.leave_lobby(lobby_id, request_options=request_options)
        return _response.data

    def list_guild_scheduled_event_users(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        with_member: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ScheduledEventUserResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        guild_scheduled_event_id : SnowflakeType

        with_member : typing.Optional[bool]

        limit : typing.Optional[int]

        before : typing.Optional[SnowflakeType]

        after : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ScheduledEventUserResponse]]
            200 response for list_guild_scheduled_event_users

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_scheduled_event_users(
            guild_id="guild_id",
            guild_scheduled_event_id="guild_scheduled_event_id",
        )
        """
        _response = self._raw_client.list_guild_scheduled_event_users(
            guild_id,
            guild_scheduled_event_id,
            with_member=with_member,
            limit=limit,
            before=before,
            after=after,
            request_options=request_options,
        )
        return _response.data

    def get_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        rule_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAutoModerationRuleResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        rule_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAutoModerationRuleResponse
            200 response for get_auto_moderation_rule

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_auto_moderation_rule(
            guild_id="guild_id",
            rule_id="rule_id",
        )
        """
        _response = self._raw_client.get_auto_moderation_rule(guild_id, rule_id, request_options=request_options)
        return _response.data

    def delete_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        rule_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        rule_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_auto_moderation_rule(
            guild_id="guild_id",
            rule_id="rule_id",
        )
        """
        _response = self._raw_client.delete_auto_moderation_rule(guild_id, rule_id, request_options=request_options)
        return _response.data

    def update_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        rule_id: SnowflakeType,
        *,
        request: UpdateAutoModerationRuleRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAutoModerationRuleResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        rule_id : SnowflakeType

        request : UpdateAutoModerationRuleRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAutoModerationRuleResponse
            200 response for update_auto_moderation_rule

        Examples
        --------
        from fern import DefaultKeywordListUpsertRequestPartial, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_auto_moderation_rule(
            guild_id="guild_id",
            rule_id="rule_id",
            request=DefaultKeywordListUpsertRequestPartial(),
        )
        """
        _response = self._raw_client.update_auto_moderation_rule(
            guild_id, rule_id, request=request, request_options=request_options
        )
        return _response.data

    def list_auto_moderation_rules(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[typing.Optional[ListAutoModerationRulesResponseItem]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[typing.Optional[ListAutoModerationRulesResponseItem]]]
            200 response for list_auto_moderation_rules

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_auto_moderation_rules(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_auto_moderation_rules(guild_id, request_options=request_options)
        return _response.data

    def create_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        *,
        request: CreateAutoModerationRuleRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAutoModerationRuleResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : CreateAutoModerationRuleRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAutoModerationRuleResponse
            200 response for create_auto_moderation_rule

        Examples
        --------
        from fern import (
            DefaultKeywordListTriggerMetadata,
            DefaultKeywordListUpsertRequest,
            FernApi,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_auto_moderation_rule(
            guild_id="guild_id",
            request=DefaultKeywordListUpsertRequest(
                name="name",
                event_type=1,
                trigger_type=1,
                trigger_metadata=DefaultKeywordListTriggerMetadata(),
            ),
        )
        """
        _response = self._raw_client.create_auto_moderation_rule(
            guild_id, request=request, request_options=request_options
        )
        return _response.data

    def get_self_voice_state(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceStateResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceStateResponse
            200 response for get_self_voice_state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_self_voice_state(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.get_self_voice_state(guild_id, request_options=request_options)
        return _response.data

    def update_self_voice_state(
        self,
        guild_id: SnowflakeType,
        *,
        request_to_speak_timestamp: typing.Optional[dt.datetime] = OMIT,
        suppress: typing.Optional[bool] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_to_speak_timestamp : typing.Optional[dt.datetime]

        suppress : typing.Optional[bool]

        channel_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_self_voice_state(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.update_self_voice_state(
            guild_id,
            request_to_speak_timestamp=request_to_speak_timestamp,
            suppress=suppress,
            channel_id=channel_id,
            request_options=request_options,
        )
        return _response.data

    def search_guild_members(
        self,
        guild_id: SnowflakeType,
        *,
        limit: int,
        query: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        limit : int

        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GuildMemberResponse]
            200 response for search_guild_members

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.search_guild_members(
            guild_id="guild_id",
            limit=1,
            query="query",
        )
        """
        _response = self._raw_client.search_guild_members(
            guild_id, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    def get_active_guild_threads(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThreadsResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadsResponse
            200 response for get_active_guild_threads

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_active_guild_threads(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.get_active_guild_threads(guild_id, request_options=request_options)
        return _response.data

    def update_my_guild_member(
        self,
        guild_id: SnowflakeType,
        *,
        nick: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateGuildMemberResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        nick : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateGuildMemberResponse
            200 response for update_my_guild_member

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_my_guild_member(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.update_my_guild_member(guild_id, nick=nick, request_options=request_options)
        return _response.data

    def add_guild_member_role(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        role_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.add_guild_member_role(
            guild_id="guild_id",
            user_id="user_id",
            role_id="role_id",
        )
        """
        _response = self._raw_client.add_guild_member_role(guild_id, user_id, role_id, request_options=request_options)
        return _response.data

    def delete_guild_member_role(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        role_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_guild_member_role(
            guild_id="guild_id",
            user_id="user_id",
            role_id="role_id",
        )
        """
        _response = self._raw_client.delete_guild_member_role(
            guild_id, user_id, role_id, request_options=request_options
        )
        return _response.data

    def leave_guild(self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.leave_guild(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.leave_guild(guild_id, request_options=request_options)
        return _response.data

    def applications_get_activity_instance(
        self,
        application_id: SnowflakeType,
        instance_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmbeddedActivityInstance:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmbeddedActivityInstance
            200 response for applications_get_activity_instance

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.applications_get_activity_instance(
            application_id="application_id",
            instance_id="instance_id",
        )
        """
        _response = self._raw_client.applications_get_activity_instance(
            application_id, instance_id, request_options=request_options
        )
        return _response.data

    def get_entitlement(
        self,
        application_id: SnowflakeType,
        entitlement_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntitlementResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        entitlement_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntitlementResponse
            200 response for get_entitlement

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_entitlement(
            application_id="application_id",
            entitlement_id="entitlement_id",
        )
        """
        _response = self._raw_client.get_entitlement(application_id, entitlement_id, request_options=request_options)
        return _response.data

    def delete_entitlement(
        self,
        application_id: SnowflakeType,
        entitlement_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        entitlement_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_entitlement(
            application_id="application_id",
            entitlement_id="entitlement_id",
        )
        """
        _response = self._raw_client.delete_entitlement(application_id, entitlement_id, request_options=request_options)
        return _response.data

    def get_entitlements(
        self,
        application_id: SnowflakeType,
        *,
        sku_ids: GetEntitlementsRequestSkuIds,
        user_id: typing.Optional[SnowflakeType] = None,
        guild_id: typing.Optional[SnowflakeType] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        exclude_ended: typing.Optional[bool] = None,
        exclude_deleted: typing.Optional[bool] = None,
        only_active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Optional[EntitlementResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        sku_ids : GetEntitlementsRequestSkuIds

        user_id : typing.Optional[SnowflakeType]

        guild_id : typing.Optional[SnowflakeType]

        before : typing.Optional[SnowflakeType]

        after : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        exclude_ended : typing.Optional[bool]

        exclude_deleted : typing.Optional[bool]

        only_active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Optional[EntitlementResponse]]
            200 response for get_entitlements

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_entitlements(
            application_id="application_id",
            sku_ids="sku_ids",
        )
        """
        _response = self._raw_client.get_entitlements(
            application_id,
            sku_ids=sku_ids,
            user_id=user_id,
            guild_id=guild_id,
            before=before,
            after=after,
            limit=limit,
            exclude_ended=exclude_ended,
            exclude_deleted=exclude_deleted,
            only_active=only_active,
            request_options=request_options,
        )
        return _response.data

    def create_entitlement(
        self,
        application_id: SnowflakeType,
        *,
        sku_id: SnowflakeType,
        owner_id: SnowflakeType,
        owner_type: EntitlementOwnerTypes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntitlementResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        sku_id : SnowflakeType

        owner_id : SnowflakeType

        owner_type : EntitlementOwnerTypes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntitlementResponse
            200 response for create_entitlement

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_entitlement(
            application_id="application_id",
            sku_id="sku_id",
            owner_id="owner_id",
            owner_type=1,
        )
        """
        _response = self._raw_client.create_entitlement(
            application_id, sku_id=sku_id, owner_id=owner_id, owner_type=owner_type, request_options=request_options
        )
        return _response.data

    def upload_application_attachment(
        self, application_id: SnowflakeType, *, file: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ActivitiesAttachmentResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        file : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActivitiesAttachmentResponse
            200 response for upload_application_attachment

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.upload_application_attachment(
            application_id="application_id",
            file="file",
        )
        """
        _response = self._raw_client.upload_application_attachment(
            application_id, file=file, request_options=request_options
        )
        return _response.data

    def get_application_command(
        self,
        application_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCommandResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCommandResponse
            200 response for get_application_command

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_application_command(
            application_id="application_id",
            command_id="command_id",
        )
        """
        _response = self._raw_client.get_application_command(
            application_id, command_id, request_options=request_options
        )
        return _response.data

    def delete_application_command(
        self,
        application_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_application_command(
            application_id="application_id",
            command_id="command_id",
        )
        """
        _response = self._raw_client.delete_application_command(
            application_id, command_id, request_options=request_options
        )
        return _response.data

    def update_application_command(
        self,
        application_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        options: typing.Optional[typing.Sequence[ApplicationCommandPatchRequestPartialOptionsItem]] = OMIT,
        default_member_permissions: typing.Optional[int] = OMIT,
        dm_permission: typing.Optional[bool] = OMIT,
        contexts: typing.Optional[typing.Sequence[InteractionContextType]] = OMIT,
        integration_types: typing.Optional[typing.Sequence[ApplicationIntegrationType]] = OMIT,
        handler: typing.Optional[ApplicationCommandHandler] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCommandResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        command_id : SnowflakeType

        name : typing.Optional[str]

        name_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        description : typing.Optional[str]

        description_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        options : typing.Optional[typing.Sequence[ApplicationCommandPatchRequestPartialOptionsItem]]

        default_member_permissions : typing.Optional[int]

        dm_permission : typing.Optional[bool]

        contexts : typing.Optional[typing.Sequence[InteractionContextType]]

        integration_types : typing.Optional[typing.Sequence[ApplicationIntegrationType]]

        handler : typing.Optional[ApplicationCommandHandler]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCommandResponse
            200 response for update_application_command

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_application_command(
            application_id="application_id",
            command_id="command_id",
        )
        """
        _response = self._raw_client.update_application_command(
            application_id,
            command_id,
            name=name,
            name_localizations=name_localizations,
            description=description,
            description_localizations=description_localizations,
            options=options,
            default_member_permissions=default_member_permissions,
            dm_permission=dm_permission,
            contexts=contexts,
            integration_types=integration_types,
            handler=handler,
            request_options=request_options,
        )
        return _response.data

    def list_application_commands(
        self,
        application_id: SnowflakeType,
        *,
        with_localizations: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ApplicationCommandResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        with_localizations : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ApplicationCommandResponse]]
            200 response for list_application_commands

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_application_commands(
            application_id="application_id",
        )
        """
        _response = self._raw_client.list_application_commands(
            application_id, with_localizations=with_localizations, request_options=request_options
        )
        return _response.data

    def create_application_command(
        self,
        application_id: SnowflakeType,
        *,
        name: str,
        name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        options: typing.Optional[typing.Sequence[ApplicationCommandCreateRequestOptionsItem]] = OMIT,
        default_member_permissions: typing.Optional[int] = OMIT,
        dm_permission: typing.Optional[bool] = OMIT,
        contexts: typing.Optional[typing.Sequence[InteractionContextType]] = OMIT,
        integration_types: typing.Optional[typing.Sequence[ApplicationIntegrationType]] = OMIT,
        handler: typing.Optional[ApplicationCommandHandler] = OMIT,
        type: typing.Optional[ApplicationCommandType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCommandResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        name : str

        name_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        description : typing.Optional[str]

        description_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        options : typing.Optional[typing.Sequence[ApplicationCommandCreateRequestOptionsItem]]

        default_member_permissions : typing.Optional[int]

        dm_permission : typing.Optional[bool]

        contexts : typing.Optional[typing.Sequence[InteractionContextType]]

        integration_types : typing.Optional[typing.Sequence[ApplicationIntegrationType]]

        handler : typing.Optional[ApplicationCommandHandler]

        type : typing.Optional[ApplicationCommandType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCommandResponse
            200 response for create_application_command

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_application_command(
            application_id="application_id",
            name="name",
        )
        """
        _response = self._raw_client.create_application_command(
            application_id,
            name=name,
            name_localizations=name_localizations,
            description=description,
            description_localizations=description_localizations,
            options=options,
            default_member_permissions=default_member_permissions,
            dm_permission=dm_permission,
            contexts=contexts,
            integration_types=integration_types,
            handler=handler,
            type=type,
            request_options=request_options,
        )
        return _response.data

    def bulk_set_application_commands(
        self,
        application_id: SnowflakeType,
        *,
        request: typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ApplicationCommandResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request : typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ApplicationCommandResponse]]
            200 response for bulk_set_application_commands

        Examples
        --------
        from fern import ApplicationCommandUpdateRequest, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.bulk_set_application_commands(
            application_id="application_id",
            request=[
                ApplicationCommandUpdateRequest(
                    name="name",
                )
            ],
        )
        """
        _response = self._raw_client.bulk_set_application_commands(
            application_id, request=request, request_options=request_options
        )
        return _response.data

    def get_application_emoji(
        self,
        application_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmojiResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmojiResponse
            200 response for get_application_emoji

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_application_emoji(
            application_id="application_id",
            emoji_id="emoji_id",
        )
        """
        _response = self._raw_client.get_application_emoji(application_id, emoji_id, request_options=request_options)
        return _response.data

    def delete_application_emoji(
        self,
        application_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_application_emoji(
            application_id="application_id",
            emoji_id="emoji_id",
        )
        """
        _response = self._raw_client.delete_application_emoji(application_id, emoji_id, request_options=request_options)
        return _response.data

    def update_application_emoji(
        self,
        application_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmojiResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        emoji_id : SnowflakeType

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmojiResponse
            200 response for update_application_emoji

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_application_emoji(
            application_id="application_id",
            emoji_id="emoji_id",
        )
        """
        _response = self._raw_client.update_application_emoji(
            application_id, emoji_id, name=name, request_options=request_options
        )
        return _response.data

    def list_application_emojis(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListApplicationEmojisResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListApplicationEmojisResponse
            200 response for list_application_emojis

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_application_emojis(
            application_id="application_id",
        )
        """
        _response = self._raw_client.list_application_emojis(application_id, request_options=request_options)
        return _response.data

    def create_application_emoji(
        self,
        application_id: SnowflakeType,
        *,
        name: str,
        image: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmojiResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        name : str

        image : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmojiResponse
            201 response for create_application_emoji

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_application_emoji(
            application_id="application_id",
            name="name",
            image="image",
        )
        """
        _response = self._raw_client.create_application_emoji(
            application_id, name=name, image=image, request_options=request_options
        )
        return _response.data

    def create_interaction_response(
        self,
        interaction_id: SnowflakeType,
        interaction_token: str,
        *,
        request: CreateInteractionResponseRequestBody,
        with_response: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[InteractionCallbackResponse]:
        """
        Parameters
        ----------
        interaction_id : SnowflakeType

        interaction_token : str

        request : CreateInteractionResponseRequestBody

        with_response : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[InteractionCallbackResponse]
            200 response for create_interaction_response

        Examples
        --------
        from fern import (
            ApplicationCommandAutocompleteCallbackRequest,
            FernApi,
            InteractionApplicationCommandAutocompleteCallbackIntegerData,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_interaction_response(
            interaction_id="interaction_id",
            interaction_token="interaction_token",
            request=ApplicationCommandAutocompleteCallbackRequest(
                type=1,
                data=InteractionApplicationCommandAutocompleteCallbackIntegerData(),
            ),
        )
        """
        _response = self._raw_client.create_interaction_response(
            interaction_id,
            interaction_token,
            request=request,
            with_response=with_response,
            request_options=request_options,
        )
        return _response.data

    def send_soundboard_sound(
        self,
        channel_id: SnowflakeType,
        *,
        sound_id: SnowflakeType,
        source_guild_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        sound_id : SnowflakeType

        source_guild_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.send_soundboard_sound(
            channel_id="channel_id",
            sound_id="sound_id",
        )
        """
        _response = self._raw_client.send_soundboard_sound(
            channel_id, sound_id=sound_id, source_guild_id=source_guild_id, request_options=request_options
        )
        return _response.data

    def get_thread_member(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        with_member: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadMemberResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        with_member : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadMemberResponse
            200 response for get_thread_member

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_thread_member(
            channel_id="channel_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.get_thread_member(
            channel_id, user_id, with_member=with_member, request_options=request_options
        )
        return _response.data

    def add_thread_member(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.add_thread_member(
            channel_id="channel_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.add_thread_member(channel_id, user_id, request_options=request_options)
        return _response.data

    def delete_thread_member(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_thread_member(
            channel_id="channel_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.delete_thread_member(channel_id, user_id, request_options=request_options)
        return _response.data

    def list_thread_members(
        self,
        channel_id: SnowflakeType,
        *,
        with_member: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ThreadMemberResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        with_member : typing.Optional[bool]

        limit : typing.Optional[int]

        after : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThreadMemberResponse]
            200 response for list_thread_members

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_thread_members(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.list_thread_members(
            channel_id, with_member=with_member, limit=limit, after=after, request_options=request_options
        )
        return _response.data

    def set_channel_permission_overwrite(
        self,
        channel_id: SnowflakeType,
        overwrite_id: SnowflakeType,
        *,
        type: typing.Optional[ChannelPermissionOverwrites] = OMIT,
        allow: typing.Optional[int] = OMIT,
        deny: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        overwrite_id : SnowflakeType

        type : typing.Optional[ChannelPermissionOverwrites]

        allow : typing.Optional[int]

        deny : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.set_channel_permission_overwrite(
            channel_id="channel_id",
            overwrite_id="overwrite_id",
        )
        """
        _response = self._raw_client.set_channel_permission_overwrite(
            channel_id, overwrite_id, type=type, allow=allow, deny=deny, request_options=request_options
        )
        return _response.data

    def delete_channel_permission_overwrite(
        self,
        channel_id: SnowflakeType,
        overwrite_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        overwrite_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_channel_permission_overwrite(
            channel_id="channel_id",
            overwrite_id="overwrite_id",
        )
        """
        _response = self._raw_client.delete_channel_permission_overwrite(
            channel_id, overwrite_id, request_options=request_options
        )
        return _response.data

    def add_group_dm_user(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        access_token: typing.Optional[str] = OMIT,
        nick: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[AddGroupDmUserResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        access_token : typing.Optional[str]

        nick : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[AddGroupDmUserResponse]
            201 response for add_group_dm_user

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.add_group_dm_user(
            channel_id="channel_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.add_group_dm_user(
            channel_id, user_id, access_token=access_token, nick=nick, request_options=request_options
        )
        return _response.data

    def delete_group_dm_user(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_group_dm_user(
            channel_id="channel_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.delete_group_dm_user(channel_id, user_id, request_options=request_options)
        return _response.data

    def follow_channel(
        self,
        channel_id: SnowflakeType,
        *,
        webhook_channel_id: SnowflakeType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChannelFollowerResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        webhook_channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelFollowerResponse
            200 response for follow_channel

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.follow_channel(
            channel_id="channel_id",
            webhook_channel_id="webhook_channel_id",
        )
        """
        _response = self._raw_client.follow_channel(
            channel_id, webhook_channel_id=webhook_channel_id, request_options=request_options
        )
        return _response.data

    def get_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for get_message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_message(
            channel_id="channel_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.get_message(channel_id, message_id, request_options=request_options)
        return _response.data

    def delete_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_message(
            channel_id="channel_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.delete_message(channel_id, message_id, request_options=request_options)
        return _response.data

    def update_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        content: typing.Optional[str] = OMIT,
        embeds: typing.Optional[typing.Sequence[RichEmbed]] = OMIT,
        flags: typing.Optional[int] = OMIT,
        allowed_mentions: typing.Optional[MessageAllowedMentionsRequest] = OMIT,
        sticker_ids: typing.Optional[typing.Sequence[SnowflakeType]] = OMIT,
        components: typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]] = OMIT,
        attachments: typing.Optional[typing.Sequence[MessageAttachmentRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        content : typing.Optional[str]

        embeds : typing.Optional[typing.Sequence[RichEmbed]]

        flags : typing.Optional[int]

        allowed_mentions : typing.Optional[MessageAllowedMentionsRequest]

        sticker_ids : typing.Optional[typing.Sequence[SnowflakeType]]

        components : typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]]

        attachments : typing.Optional[typing.Sequence[MessageAttachmentRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for update_message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_message(
            channel_id="channel_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.update_message(
            channel_id,
            message_id,
            content=content,
            embeds=embeds,
            flags=flags,
            allowed_mentions=allowed_mentions,
            sticker_ids=sticker_ids,
            components=components,
            attachments=attachments,
            request_options=request_options,
        )
        return _response.data

    def list_messages(
        self,
        channel_id: SnowflakeType,
        *,
        around: typing.Optional[SnowflakeType] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[MessageResponse]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        around : typing.Optional[SnowflakeType]

        before : typing.Optional[SnowflakeType]

        after : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[MessageResponse]]
            200 response for list_messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_messages(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.list_messages(
            channel_id, around=around, before=before, after=after, limit=limit, request_options=request_options
        )
        return _response.data

    def create_message(
        self,
        channel_id: SnowflakeType,
        *,
        content: typing.Optional[str] = OMIT,
        embeds: typing.Optional[typing.Sequence[RichEmbed]] = OMIT,
        allowed_mentions: typing.Optional[MessageAllowedMentionsRequest] = OMIT,
        sticker_ids: typing.Optional[typing.Sequence[SnowflakeType]] = OMIT,
        components: typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]] = OMIT,
        flags: typing.Optional[int] = OMIT,
        attachments: typing.Optional[typing.Sequence[MessageAttachmentRequest]] = OMIT,
        poll: typing.Optional[PollCreateRequest] = OMIT,
        confetti_potion: typing.Optional[ConfettiPotionCreateRequest] = OMIT,
        message_reference: typing.Optional[MessageReferenceRequest] = OMIT,
        nonce: typing.Optional[MessageCreateRequestNonce] = OMIT,
        enforce_nonce: typing.Optional[bool] = OMIT,
        tts: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        content : typing.Optional[str]

        embeds : typing.Optional[typing.Sequence[RichEmbed]]

        allowed_mentions : typing.Optional[MessageAllowedMentionsRequest]

        sticker_ids : typing.Optional[typing.Sequence[SnowflakeType]]

        components : typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]]

        flags : typing.Optional[int]

        attachments : typing.Optional[typing.Sequence[MessageAttachmentRequest]]

        poll : typing.Optional[PollCreateRequest]

        confetti_potion : typing.Optional[ConfettiPotionCreateRequest]

        message_reference : typing.Optional[MessageReferenceRequest]

        nonce : typing.Optional[MessageCreateRequestNonce]

        enforce_nonce : typing.Optional[bool]

        tts : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for create_message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_message(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.create_message(
            channel_id,
            content=content,
            embeds=embeds,
            allowed_mentions=allowed_mentions,
            sticker_ids=sticker_ids,
            components=components,
            flags=flags,
            attachments=attachments,
            poll=poll,
            confetti_potion=confetti_potion,
            message_reference=message_reference,
            nonce=nonce,
            enforce_nonce=enforce_nonce,
            tts=tts,
            request_options=request_options,
        )
        return _response.data

    def list_channel_webhooks(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ListChannelWebhooksResponseItem]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ListChannelWebhooksResponseItem]]
            200 response for list_channel_webhooks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_channel_webhooks(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.list_channel_webhooks(channel_id, request_options=request_options)
        return _response.data

    def create_webhook(
        self,
        channel_id: SnowflakeType,
        *,
        name: str,
        avatar: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildIncomingWebhookResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        name : str

        avatar : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildIncomingWebhookResponse
            200 response for create_webhook

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_webhook(
            channel_id="channel_id",
            name="name",
        )
        """
        _response = self._raw_client.create_webhook(
            channel_id, name=name, avatar=avatar, request_options=request_options
        )
        return _response.data

    def list_channel_invites(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ListChannelInvitesResponseItem]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ListChannelInvitesResponseItem]]
            200 response for list_channel_invites

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_channel_invites(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.list_channel_invites(channel_id, request_options=request_options)
        return _response.data

    def create_channel_invite(
        self,
        channel_id: SnowflakeType,
        *,
        request: CreateChannelInviteRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[CreateChannelInviteResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request : CreateChannelInviteRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CreateChannelInviteResponse]
            200 response for create_channel_invite

        Examples
        --------
        from fern import CreateGroupDmInviteRequest, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_channel_invite(
            channel_id="channel_id",
            request=CreateGroupDmInviteRequest(),
        )
        """
        _response = self._raw_client.create_channel_invite(channel_id, request=request, request_options=request_options)
        return _response.data

    def create_thread(
        self,
        channel_id: SnowflakeType,
        *,
        request: CreateThreadRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedThreadResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request : CreateThreadRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedThreadResponse
            201 response for create_thread

        Examples
        --------
        from fern import (
            BaseCreateMessageCreateRequest,
            CreateForumThreadRequest,
            FernApi,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_thread(
            channel_id="channel_id",
            request=CreateForumThreadRequest(
                name="name",
                message=BaseCreateMessageCreateRequest(),
            ),
        )
        """
        _response = self._raw_client.create_thread(channel_id, request=request, request_options=request_options)
        return _response.data

    def trigger_typing_indicator(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[TypingIndicatorResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[TypingIndicatorResponse]
            200 response for trigger_typing_indicator

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.trigger_typing_indicator(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.trigger_typing_indicator(channel_id, request_options=request_options)
        return _response.data

    def pin_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.pin_message(
            channel_id="channel_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.pin_message(channel_id, message_id, request_options=request_options)
        return _response.data

    def unpin_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.unpin_message(
            channel_id="channel_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.unpin_message(channel_id, message_id, request_options=request_options)
        return _response.data

    def list_pinned_messages(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[MessageResponse]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[MessageResponse]]
            200 response for list_pinned_messages

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_pinned_messages(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.list_pinned_messages(channel_id, request_options=request_options)
        return _response.data

    def get_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        message_id: SnowflakeType,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        message_id : SnowflakeType

        thread_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for get_webhook_message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_webhook_message(
            webhook_id="webhook_id",
            webhook_token="webhook_token",
            message_id="message_id",
        )
        """
        _response = self._raw_client.get_webhook_message(
            webhook_id, webhook_token, message_id, thread_id=thread_id, request_options=request_options
        )
        return _response.data

    def delete_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        message_id: SnowflakeType,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        message_id : SnowflakeType

        thread_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_webhook_message(
            webhook_id="webhook_id",
            webhook_token="webhook_token",
            message_id="message_id",
        )
        """
        _response = self._raw_client.delete_webhook_message(
            webhook_id, webhook_token, message_id, thread_id=thread_id, request_options=request_options
        )
        return _response.data

    def update_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        message_id: SnowflakeType,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        with_components: typing.Optional[bool] = None,
        content: typing.Optional[str] = OMIT,
        embeds: typing.Optional[typing.Sequence[RichEmbed]] = OMIT,
        allowed_mentions: typing.Optional[MessageAllowedMentionsRequest] = OMIT,
        components: typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]] = OMIT,
        attachments: typing.Optional[typing.Sequence[MessageAttachmentRequest]] = OMIT,
        poll: typing.Optional[PollCreateRequest] = OMIT,
        flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        message_id : SnowflakeType

        thread_id : typing.Optional[SnowflakeType]

        with_components : typing.Optional[bool]

        content : typing.Optional[str]

        embeds : typing.Optional[typing.Sequence[RichEmbed]]

        allowed_mentions : typing.Optional[MessageAllowedMentionsRequest]

        components : typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]]

        attachments : typing.Optional[typing.Sequence[MessageAttachmentRequest]]

        poll : typing.Optional[PollCreateRequest]

        flags : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for update_webhook_message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_webhook_message(
            webhook_id="webhook_id",
            webhook_token="webhook_token",
            message_id="message_id",
        )
        """
        _response = self._raw_client.update_webhook_message(
            webhook_id,
            webhook_token,
            message_id,
            thread_id=thread_id,
            with_components=with_components,
            content=content,
            embeds=embeds,
            allowed_mentions=allowed_mentions,
            components=components,
            attachments=attachments,
            poll=poll,
            flags=flags,
            request_options=request_options,
        )
        return _response.data

    def execute_github_compatible_webhook(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        sender: GithubUser,
        wait: typing.Optional[bool] = None,
        thread_id: typing.Optional[SnowflakeType] = None,
        action: typing.Optional[str] = OMIT,
        ref: typing.Optional[str] = OMIT,
        ref_type: typing.Optional[str] = OMIT,
        comment: typing.Optional[GithubComment] = OMIT,
        issue: typing.Optional[GithubIssue] = OMIT,
        pull_request: typing.Optional[GithubIssue] = OMIT,
        repository: typing.Optional[GithubRepository] = OMIT,
        forkee: typing.Optional[GithubRepository] = OMIT,
        member: typing.Optional[GithubUser] = OMIT,
        release: typing.Optional[GithubRelease] = OMIT,
        head_commit: typing.Optional[GithubCommit] = OMIT,
        commits: typing.Optional[typing.Sequence[GithubCommit]] = OMIT,
        forced: typing.Optional[bool] = OMIT,
        compare: typing.Optional[str] = OMIT,
        review: typing.Optional[GithubReview] = OMIT,
        check_run: typing.Optional[GithubCheckRun] = OMIT,
        check_suite: typing.Optional[GithubCheckSuite] = OMIT,
        discussion: typing.Optional[GithubDiscussion] = OMIT,
        answer: typing.Optional[GithubComment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        sender : GithubUser

        wait : typing.Optional[bool]

        thread_id : typing.Optional[SnowflakeType]

        action : typing.Optional[str]

        ref : typing.Optional[str]

        ref_type : typing.Optional[str]

        comment : typing.Optional[GithubComment]

        issue : typing.Optional[GithubIssue]

        pull_request : typing.Optional[GithubIssue]

        repository : typing.Optional[GithubRepository]

        forkee : typing.Optional[GithubRepository]

        member : typing.Optional[GithubUser]

        release : typing.Optional[GithubRelease]

        head_commit : typing.Optional[GithubCommit]

        commits : typing.Optional[typing.Sequence[GithubCommit]]

        forced : typing.Optional[bool]

        compare : typing.Optional[str]

        review : typing.Optional[GithubReview]

        check_run : typing.Optional[GithubCheckRun]

        check_suite : typing.Optional[GithubCheckSuite]

        discussion : typing.Optional[GithubDiscussion]

        answer : typing.Optional[GithubComment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, GithubUser

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.execute_github_compatible_webhook(
            webhook_id="webhook_id",
            webhook_token="webhook_token",
            sender=GithubUser(
                id=1,
                login="login",
                html_url="html_url",
                avatar_url="avatar_url",
            ),
        )
        """
        _response = self._raw_client.execute_github_compatible_webhook(
            webhook_id,
            webhook_token,
            sender=sender,
            wait=wait,
            thread_id=thread_id,
            action=action,
            ref=ref,
            ref_type=ref_type,
            comment=comment,
            issue=issue,
            pull_request=pull_request,
            repository=repository,
            forkee=forkee,
            member=member,
            release=release,
            head_commit=head_commit,
            commits=commits,
            forced=forced,
            compare=compare,
            review=review,
            check_run=check_run,
            check_suite=check_suite,
            discussion=discussion,
            answer=answer,
            request_options=request_options,
        )
        return _response.data

    def execute_slack_compatible_webhook(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        wait: typing.Optional[bool] = None,
        thread_id: typing.Optional[SnowflakeType] = None,
        text: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        icon_url: typing.Optional[str] = OMIT,
        attachments: typing.Optional[typing.Sequence[WebhookSlackEmbed]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[str]:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        wait : typing.Optional[bool]

        thread_id : typing.Optional[SnowflakeType]

        text : typing.Optional[str]

        username : typing.Optional[str]

        icon_url : typing.Optional[str]

        attachments : typing.Optional[typing.Sequence[WebhookSlackEmbed]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[str]
            200 response for execute_slack_compatible_webhook

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.execute_slack_compatible_webhook(
            webhook_id="webhook_id",
            webhook_token="webhook_token",
        )
        """
        _response = self._raw_client.execute_slack_compatible_webhook(
            webhook_id,
            webhook_token,
            wait=wait,
            thread_id=thread_id,
            text=text,
            username=username,
            icon_url=icon_url,
            attachments=attachments,
            request_options=request_options,
        )
        return _response.data

    def edit_lobby_channel_link(
        self,
        lobby_id: SnowflakeType,
        *,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyResponse:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        channel_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyResponse
            200 response for edit_lobby_channel_link

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.edit_lobby_channel_link(
            lobby_id="lobby_id",
        )
        """
        _response = self._raw_client.edit_lobby_channel_link(
            lobby_id, channel_id=channel_id, request_options=request_options
        )
        return _response.data

    def create_lobby_message(
        self,
        lobby_id: SnowflakeType,
        *,
        content: typing.Optional[str] = OMIT,
        embeds: typing.Optional[typing.Sequence[RichEmbed]] = OMIT,
        allowed_mentions: typing.Optional[MessageAllowedMentionsRequest] = OMIT,
        sticker_ids: typing.Optional[typing.Sequence[SnowflakeType]] = OMIT,
        components: typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]] = OMIT,
        flags: typing.Optional[int] = OMIT,
        attachments: typing.Optional[typing.Sequence[MessageAttachmentRequest]] = OMIT,
        poll: typing.Optional[PollCreateRequest] = OMIT,
        confetti_potion: typing.Optional[ConfettiPotionCreateRequest] = OMIT,
        message_reference: typing.Optional[MessageReferenceRequest] = OMIT,
        nonce: typing.Optional[SdkMessageRequestNonce] = OMIT,
        enforce_nonce: typing.Optional[bool] = OMIT,
        tts: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyMessageResponse:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        content : typing.Optional[str]

        embeds : typing.Optional[typing.Sequence[RichEmbed]]

        allowed_mentions : typing.Optional[MessageAllowedMentionsRequest]

        sticker_ids : typing.Optional[typing.Sequence[SnowflakeType]]

        components : typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]]

        flags : typing.Optional[int]

        attachments : typing.Optional[typing.Sequence[MessageAttachmentRequest]]

        poll : typing.Optional[PollCreateRequest]

        confetti_potion : typing.Optional[ConfettiPotionCreateRequest]

        message_reference : typing.Optional[MessageReferenceRequest]

        nonce : typing.Optional[SdkMessageRequestNonce]

        enforce_nonce : typing.Optional[bool]

        tts : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyMessageResponse
            201 response for create_lobby_message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_lobby_message(
            lobby_id="lobby_id",
        )
        """
        _response = self._raw_client.create_lobby_message(
            lobby_id,
            content=content,
            embeds=embeds,
            allowed_mentions=allowed_mentions,
            sticker_ids=sticker_ids,
            components=components,
            flags=flags,
            attachments=attachments,
            poll=poll,
            confetti_potion=confetti_potion,
            message_reference=message_reference,
            nonce=nonce,
            enforce_nonce=enforce_nonce,
            tts=tts,
            request_options=request_options,
        )
        return _response.data

    def add_lobby_member(
        self,
        lobby_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyMemberResponse:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        user_id : SnowflakeType

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        flags : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyMemberResponse
            200 response for add_lobby_member

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.add_lobby_member(
            lobby_id="lobby_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.add_lobby_member(
            lobby_id, user_id, metadata=metadata, flags=flags, request_options=request_options
        )
        return _response.data

    def delete_lobby_member(
        self,
        lobby_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_lobby_member(
            lobby_id="lobby_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.delete_lobby_member(lobby_id, user_id, request_options=request_options)
        return _response.data

    def get_guild_template(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuildTemplateResponse:
        """
        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildTemplateResponse
            200 response for get_guild_template

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_template(
            code="code",
        )
        """
        _response = self._raw_client.get_guild_template(code, request_options=request_options)
        return _response.data

    def create_guild_from_template(
        self,
        code: str,
        *,
        name: str,
        icon: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildResponse:
        """
        Parameters
        ----------
        code : str

        name : str

        icon : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildResponse
            201 response for create_guild_from_template

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_guild_from_template(
            code="code",
            name="name",
        )
        """
        _response = self._raw_client.create_guild_from_template(
            code, name=name, icon=icon, request_options=request_options
        )
        return _response.data

    def get_guild_new_member_welcome(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[GuildHomeSettingsResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[GuildHomeSettingsResponse]
            200 response for get_guild_new_member_welcome

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_new_member_welcome(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.get_guild_new_member_welcome(guild_id, request_options=request_options)
        return _response.data

    def get_guild_soundboard_sound(
        self,
        guild_id: SnowflakeType,
        sound_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoundboardSoundResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sound_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoundboardSoundResponse
            200 response for get_guild_soundboard_sound

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_soundboard_sound(
            guild_id="guild_id",
            sound_id="sound_id",
        )
        """
        _response = self._raw_client.get_guild_soundboard_sound(guild_id, sound_id, request_options=request_options)
        return _response.data

    def delete_guild_soundboard_sound(
        self,
        guild_id: SnowflakeType,
        sound_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sound_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_guild_soundboard_sound(
            guild_id="guild_id",
            sound_id="sound_id",
        )
        """
        _response = self._raw_client.delete_guild_soundboard_sound(guild_id, sound_id, request_options=request_options)
        return _response.data

    def update_guild_soundboard_sound(
        self,
        guild_id: SnowflakeType,
        sound_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        volume: typing.Optional[float] = OMIT,
        emoji_id: typing.Optional[SnowflakeType] = OMIT,
        emoji_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoundboardSoundResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sound_id : SnowflakeType

        name : typing.Optional[str]

        volume : typing.Optional[float]

        emoji_id : typing.Optional[SnowflakeType]

        emoji_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoundboardSoundResponse
            200 response for update_guild_soundboard_sound

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_guild_soundboard_sound(
            guild_id="guild_id",
            sound_id="sound_id",
        )
        """
        _response = self._raw_client.update_guild_soundboard_sound(
            guild_id,
            sound_id,
            name=name,
            volume=volume,
            emoji_id=emoji_id,
            emoji_name=emoji_name,
            request_options=request_options,
        )
        return _response.data

    def list_guild_soundboard_sounds(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListGuildSoundboardSoundsResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGuildSoundboardSoundsResponse
            200 response for list_guild_soundboard_sounds

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_soundboard_sounds(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_soundboard_sounds(guild_id, request_options=request_options)
        return _response.data

    def create_guild_soundboard_sound(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        sound: str,
        volume: typing.Optional[float] = OMIT,
        emoji_id: typing.Optional[SnowflakeType] = OMIT,
        emoji_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoundboardSoundResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : str

        sound : str

        volume : typing.Optional[float]

        emoji_id : typing.Optional[SnowflakeType]

        emoji_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoundboardSoundResponse
            201 response for create_guild_soundboard_sound

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_guild_soundboard_sound(
            guild_id="guild_id",
            name="name",
            sound="sound",
        )
        """
        _response = self._raw_client.create_guild_soundboard_sound(
            guild_id,
            name=name,
            sound=sound,
            volume=volume,
            emoji_id=emoji_id,
            emoji_name=emoji_name,
            request_options=request_options,
        )
        return _response.data

    def get_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        with_user_count: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetGuildScheduledEventResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        guild_scheduled_event_id : SnowflakeType

        with_user_count : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGuildScheduledEventResponse
            200 response for get_guild_scheduled_event

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_scheduled_event(
            guild_id="guild_id",
            guild_scheduled_event_id="guild_scheduled_event_id",
        )
        """
        _response = self._raw_client.get_guild_scheduled_event(
            guild_id, guild_scheduled_event_id, with_user_count=with_user_count, request_options=request_options
        )
        return _response.data

    def delete_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        guild_scheduled_event_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_guild_scheduled_event(
            guild_id="guild_id",
            guild_scheduled_event_id="guild_scheduled_event_id",
        )
        """
        _response = self._raw_client.delete_guild_scheduled_event(
            guild_id, guild_scheduled_event_id, request_options=request_options
        )
        return _response.data

    def update_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        request: UpdateGuildScheduledEventRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateGuildScheduledEventResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        guild_scheduled_event_id : SnowflakeType

        request : UpdateGuildScheduledEventRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateGuildScheduledEventResponse
            200 response for update_guild_scheduled_event

        Examples
        --------
        from fern import ExternalScheduledEventPatchRequestPartial, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_guild_scheduled_event(
            guild_id="guild_id",
            guild_scheduled_event_id="guild_scheduled_event_id",
            request=ExternalScheduledEventPatchRequestPartial(),
        )
        """
        _response = self._raw_client.update_guild_scheduled_event(
            guild_id, guild_scheduled_event_id, request=request, request_options=request_options
        )
        return _response.data

    def list_guild_scheduled_events(
        self,
        guild_id: SnowflakeType,
        *,
        with_user_count: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ListGuildScheduledEventsResponseItem]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        with_user_count : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ListGuildScheduledEventsResponseItem]]
            200 response for list_guild_scheduled_events

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_scheduled_events(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_scheduled_events(
            guild_id, with_user_count=with_user_count, request_options=request_options
        )
        return _response.data

    def create_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        *,
        request: CreateGuildScheduledEventRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateGuildScheduledEventResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : CreateGuildScheduledEventRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGuildScheduledEventResponse
            200 response for create_guild_scheduled_event

        Examples
        --------
        import datetime

        from fern import (
            EntityMetadataExternal,
            ExternalScheduledEventCreateRequest,
            FernApi,
        )

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_guild_scheduled_event(
            guild_id="guild_id",
            request=ExternalScheduledEventCreateRequest(
                name="name",
                scheduled_start_time=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                privacy_level=1,
                entity_type=1,
                entity_metadata=EntityMetadataExternal(
                    location="location",
                ),
            ),
        )
        """
        _response = self._raw_client.create_guild_scheduled_event(
            guild_id, request=request, request_options=request_options
        )
        return _response.data

    def get_guild_welcome_screen(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuildWelcomeScreenResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildWelcomeScreenResponse
            200 response for get_guild_welcome_screen

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_welcome_screen(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.get_guild_welcome_screen(guild_id, request_options=request_options)
        return _response.data

    def update_guild_welcome_screen(
        self,
        guild_id: SnowflakeType,
        *,
        description: typing.Optional[str] = OMIT,
        welcome_channels: typing.Optional[typing.Sequence[GuildWelcomeChannel]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildWelcomeScreenResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        description : typing.Optional[str]

        welcome_channels : typing.Optional[typing.Sequence[GuildWelcomeChannel]]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildWelcomeScreenResponse
            200 response for update_guild_welcome_screen

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_guild_welcome_screen(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.update_guild_welcome_screen(
            guild_id,
            description=description,
            welcome_channels=welcome_channels,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    def get_voice_state(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoiceStateResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceStateResponse
            200 response for get_voice_state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_voice_state(
            guild_id="guild_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.get_voice_state(guild_id, user_id, request_options=request_options)
        return _response.data

    def update_voice_state(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        suppress: typing.Optional[bool] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        suppress : typing.Optional[bool]

        channel_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_voice_state(
            guild_id="guild_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.update_voice_state(
            guild_id, user_id, suppress=suppress, channel_id=channel_id, request_options=request_options
        )
        return _response.data

    def delete_guild_integration(
        self,
        guild_id: SnowflakeType,
        integration_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        integration_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_guild_integration(
            guild_id="guild_id",
            integration_id="integration_id",
        )
        """
        _response = self._raw_client.delete_guild_integration(guild_id, integration_id, request_options=request_options)
        return _response.data

    def list_guild_integrations(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ListGuildIntegrationsResponseItem]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ListGuildIntegrationsResponseItem]]
            200 response for list_guild_integrations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_integrations(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_integrations(guild_id, request_options=request_options)
        return _response.data

    def get_guild_widget(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WidgetResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WidgetResponse
            200 response for get_guild_widget

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_widget(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.get_guild_widget(guild_id, request_options=request_options)
        return _response.data

    def get_guilds_onboarding(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGuildOnboardingResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGuildOnboardingResponse
            200 response for get_guilds_onboarding

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guilds_onboarding(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.get_guilds_onboarding(guild_id, request_options=request_options)
        return _response.data

    def put_guilds_onboarding(
        self,
        guild_id: SnowflakeType,
        *,
        prompts: typing.Optional[typing.Sequence[UpdateOnboardingPromptRequest]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        default_channel_ids: typing.Optional[typing.Sequence[SnowflakeType]] = OMIT,
        mode: typing.Optional[GuildOnboardingMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildOnboardingResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        prompts : typing.Optional[typing.Sequence[UpdateOnboardingPromptRequest]]

        enabled : typing.Optional[bool]

        default_channel_ids : typing.Optional[typing.Sequence[SnowflakeType]]

        mode : typing.Optional[GuildOnboardingMode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildOnboardingResponse
            200 response for put_guilds_onboarding

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.put_guilds_onboarding(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.put_guilds_onboarding(
            guild_id,
            prompts=prompts,
            enabled=enabled,
            default_channel_ids=default_channel_ids,
            mode=mode,
            request_options=request_options,
        )
        return _response.data

    def get_guild_vanity_url(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VanityUrlResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VanityUrlResponse
            200 response for get_guild_vanity_url

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_vanity_url(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.get_guild_vanity_url(guild_id, request_options=request_options)
        return _response.data

    def list_guild_audit_log_entries(
        self,
        guild_id: SnowflakeType,
        *,
        user_id: typing.Optional[SnowflakeType] = None,
        target_id: typing.Optional[SnowflakeType] = None,
        action_type: typing.Optional[int] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildAuditLogResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : typing.Optional[SnowflakeType]

        target_id : typing.Optional[SnowflakeType]

        action_type : typing.Optional[int]

        before : typing.Optional[SnowflakeType]

        after : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildAuditLogResponse
            200 response for list_guild_audit_log_entries

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_audit_log_entries(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_audit_log_entries(
            guild_id,
            user_id=user_id,
            target_id=target_id,
            action_type=action_type,
            before=before,
            after=after,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def get_guild_widget_png(
        self,
        guild_id: SnowflakeType,
        *,
        style: typing.Optional[WidgetImageStyles] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        style : typing.Optional[WidgetImageStyles]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            200 response for get_guild_widget_png
        """
        with self._raw_client.get_guild_widget_png(guild_id, style=style, request_options=request_options) as r:
            yield from r.data

    def sync_guild_template(
        self, guild_id: SnowflakeType, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuildTemplateResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildTemplateResponse
            200 response for sync_guild_template

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.sync_guild_template(
            guild_id="guild_id",
            code="code",
        )
        """
        _response = self._raw_client.sync_guild_template(guild_id, code, request_options=request_options)
        return _response.data

    def delete_guild_template(
        self, guild_id: SnowflakeType, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuildTemplateResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildTemplateResponse
            200 response for delete_guild_template

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_guild_template(
            guild_id="guild_id",
            code="code",
        )
        """
        _response = self._raw_client.delete_guild_template(guild_id, code, request_options=request_options)
        return _response.data

    def update_guild_template(
        self,
        guild_id: SnowflakeType,
        code: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildTemplateResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        code : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildTemplateResponse
            200 response for update_guild_template

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_guild_template(
            guild_id="guild_id",
            code="code",
        )
        """
        _response = self._raw_client.update_guild_template(
            guild_id, code, name=name, description=description, request_options=request_options
        )
        return _response.data

    def list_guild_templates(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[GuildTemplateResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[GuildTemplateResponse]]
            200 response for list_guild_templates

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_templates(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_templates(guild_id, request_options=request_options)
        return _response.data

    def create_guild_template(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildTemplateResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildTemplateResponse
            200 response for create_guild_template

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_guild_template(
            guild_id="guild_id",
            name="name",
        )
        """
        _response = self._raw_client.create_guild_template(
            guild_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    def get_guild_sticker(
        self,
        guild_id: SnowflakeType,
        sticker_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildStickerResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sticker_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildStickerResponse
            200 response for get_guild_sticker

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_sticker(
            guild_id="guild_id",
            sticker_id="sticker_id",
        )
        """
        _response = self._raw_client.get_guild_sticker(guild_id, sticker_id, request_options=request_options)
        return _response.data

    def delete_guild_sticker(
        self,
        guild_id: SnowflakeType,
        sticker_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sticker_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_guild_sticker(
            guild_id="guild_id",
            sticker_id="sticker_id",
        )
        """
        _response = self._raw_client.delete_guild_sticker(guild_id, sticker_id, request_options=request_options)
        return _response.data

    def update_guild_sticker(
        self,
        guild_id: SnowflakeType,
        sticker_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildStickerResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sticker_id : SnowflakeType

        name : typing.Optional[str]

        tags : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildStickerResponse
            200 response for update_guild_sticker

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_guild_sticker(
            guild_id="guild_id",
            sticker_id="sticker_id",
        )
        """
        _response = self._raw_client.update_guild_sticker(
            guild_id, sticker_id, name=name, tags=tags, description=description, request_options=request_options
        )
        return _response.data

    def bulk_ban_users_from_guild(
        self,
        guild_id: SnowflakeType,
        *,
        user_ids: typing.Sequence[SnowflakeType],
        delete_message_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkBanUsersResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_ids : typing.Sequence[SnowflakeType]

        delete_message_seconds : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkBanUsersResponse
            200 response for bulk_ban_users_from_guild

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.bulk_ban_users_from_guild(
            guild_id="guild_id",
            user_ids=["user_ids"],
        )
        """
        _response = self._raw_client.bulk_ban_users_from_guild(
            guild_id, user_ids=user_ids, delete_message_seconds=delete_message_seconds, request_options=request_options
        )
        return _response.data

    def list_guild_stickers(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GuildStickerResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GuildStickerResponse]
            200 response for list_guild_stickers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_stickers(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_stickers(guild_id, request_options=request_options)
        return _response.data

    def create_guild_sticker(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        tags: str,
        file: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildStickerResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : str

        tags : str

        file : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildStickerResponse
            201 response for create_guild_sticker

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_guild_sticker(
            guild_id="guild_id",
            name="name",
            tags="tags",
            file="file",
        )
        """
        _response = self._raw_client.create_guild_sticker(
            guild_id, name=name, tags=tags, file=file, description=description, request_options=request_options
        )
        return _response.data

    def get_guild_webhooks(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[GetGuildWebhooksResponseItem]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[GetGuildWebhooksResponseItem]]
            200 response for get_guild_webhooks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_webhooks(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.get_guild_webhooks(guild_id, request_options=request_options)
        return _response.data

    def list_guild_channels(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ListGuildChannelsResponseItem]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ListGuildChannelsResponseItem]]
            200 response for list_guild_channels

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_channels(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_channels(guild_id, request_options=request_options)
        return _response.data

    def create_guild_channel(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        type: typing.Optional[int] = OMIT,
        position: typing.Optional[int] = OMIT,
        topic: typing.Optional[str] = OMIT,
        bitrate: typing.Optional[int] = OMIT,
        user_limit: typing.Optional[int] = OMIT,
        nsfw: typing.Optional[bool] = OMIT,
        rate_limit_per_user: typing.Optional[int] = OMIT,
        parent_id: typing.Optional[SnowflakeType] = OMIT,
        permission_overwrites: typing.Optional[typing.Sequence[ChannelPermissionOverwriteRequest]] = OMIT,
        rtc_region: typing.Optional[str] = OMIT,
        video_quality_mode: typing.Optional[VideoQualityModes] = OMIT,
        default_auto_archive_duration: typing.Optional[ThreadAutoArchiveDuration] = OMIT,
        default_reaction_emoji: typing.Optional[UpdateDefaultReactionEmojiRequest] = OMIT,
        default_thread_rate_limit_per_user: typing.Optional[int] = OMIT,
        default_sort_order: typing.Optional[ThreadSortOrder] = OMIT,
        default_forum_layout: typing.Optional[ForumLayout] = OMIT,
        available_tags: typing.Optional[typing.Sequence[typing.Optional[CreateOrUpdateThreadTagRequest]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildChannelResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : str

        type : typing.Optional[int]

        position : typing.Optional[int]

        topic : typing.Optional[str]

        bitrate : typing.Optional[int]

        user_limit : typing.Optional[int]

        nsfw : typing.Optional[bool]

        rate_limit_per_user : typing.Optional[int]

        parent_id : typing.Optional[SnowflakeType]

        permission_overwrites : typing.Optional[typing.Sequence[ChannelPermissionOverwriteRequest]]

        rtc_region : typing.Optional[str]

        video_quality_mode : typing.Optional[VideoQualityModes]

        default_auto_archive_duration : typing.Optional[ThreadAutoArchiveDuration]

        default_reaction_emoji : typing.Optional[UpdateDefaultReactionEmojiRequest]

        default_thread_rate_limit_per_user : typing.Optional[int]

        default_sort_order : typing.Optional[ThreadSortOrder]

        default_forum_layout : typing.Optional[ForumLayout]

        available_tags : typing.Optional[typing.Sequence[typing.Optional[CreateOrUpdateThreadTagRequest]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildChannelResponse
            201 response for create_guild_channel

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_guild_channel(
            guild_id="guild_id",
            name="name",
        )
        """
        _response = self._raw_client.create_guild_channel(
            guild_id,
            name=name,
            type=type,
            position=position,
            topic=topic,
            bitrate=bitrate,
            user_limit=user_limit,
            nsfw=nsfw,
            rate_limit_per_user=rate_limit_per_user,
            parent_id=parent_id,
            permission_overwrites=permission_overwrites,
            rtc_region=rtc_region,
            video_quality_mode=video_quality_mode,
            default_auto_archive_duration=default_auto_archive_duration,
            default_reaction_emoji=default_reaction_emoji,
            default_thread_rate_limit_per_user=default_thread_rate_limit_per_user,
            default_sort_order=default_sort_order,
            default_forum_layout=default_forum_layout,
            available_tags=available_tags,
            request_options=request_options,
        )
        return _response.data

    def bulk_update_guild_channels(
        self,
        guild_id: SnowflakeType,
        *,
        request: typing.Sequence[BulkUpdateGuildChannelsRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : typing.Sequence[BulkUpdateGuildChannelsRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import BulkUpdateGuildChannelsRequestBodyItem, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.bulk_update_guild_channels(
            guild_id="guild_id",
            request=[BulkUpdateGuildChannelsRequestBodyItem()],
        )
        """
        _response = self._raw_client.bulk_update_guild_channels(
            guild_id, request=request, request_options=request_options
        )
        return _response.data

    def get_guild_member(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildMemberResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildMemberResponse
            200 response for get_guild_member

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_member(
            guild_id="guild_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.get_guild_member(guild_id, user_id, request_options=request_options)
        return _response.data

    def add_guild_member(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        access_token: str,
        nick: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]] = OMIT,
        mute: typing.Optional[bool] = OMIT,
        deaf: typing.Optional[bool] = OMIT,
        flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[GuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        access_token : str

        nick : typing.Optional[str]

        roles : typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]]

        mute : typing.Optional[bool]

        deaf : typing.Optional[bool]

        flags : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[GuildMemberResponse]
            201 response for add_guild_member

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.add_guild_member(
            guild_id="guild_id",
            user_id="user_id",
            access_token="access_token",
        )
        """
        _response = self._raw_client.add_guild_member(
            guild_id,
            user_id,
            access_token=access_token,
            nick=nick,
            roles=roles,
            mute=mute,
            deaf=deaf,
            flags=flags,
            request_options=request_options,
        )
        return _response.data

    def delete_guild_member(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_guild_member(
            guild_id="guild_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.delete_guild_member(guild_id, user_id, request_options=request_options)
        return _response.data

    def update_guild_member(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        nick: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]] = OMIT,
        mute: typing.Optional[bool] = OMIT,
        deaf: typing.Optional[bool] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        communication_disabled_until: typing.Optional[dt.datetime] = OMIT,
        flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[GuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        nick : typing.Optional[str]

        roles : typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]]

        mute : typing.Optional[bool]

        deaf : typing.Optional[bool]

        channel_id : typing.Optional[SnowflakeType]

        communication_disabled_until : typing.Optional[dt.datetime]

        flags : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[GuildMemberResponse]
            200 response for update_guild_member

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_guild_member(
            guild_id="guild_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.update_guild_member(
            guild_id,
            user_id,
            nick=nick,
            roles=roles,
            mute=mute,
            deaf=deaf,
            channel_id=channel_id,
            communication_disabled_until=communication_disabled_until,
            flags=flags,
            request_options=request_options,
        )
        return _response.data

    def list_guild_members(
        self,
        guild_id: SnowflakeType,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        limit : typing.Optional[int]

        after : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GuildMemberResponse]
            200 response for list_guild_members

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_members(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_members(
            guild_id, limit=limit, after=after, request_options=request_options
        )
        return _response.data

    def get_guild_preview(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuildPreviewResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildPreviewResponse
            200 response for get_guild_preview

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_preview(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.get_guild_preview(guild_id, request_options=request_options)
        return _response.data

    def list_guild_invites(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ListGuildInvitesResponseItem]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ListGuildInvitesResponseItem]]
            200 response for list_guild_invites

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_invites(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_invites(guild_id, request_options=request_options)
        return _response.data

    def list_guild_voice_regions(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[VoiceRegionResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[VoiceRegionResponse]]
            200 response for list_guild_voice_regions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_voice_regions(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_voice_regions(guild_id, request_options=request_options)
        return _response.data

    def get_guild_emoji(
        self,
        guild_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmojiResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmojiResponse
            200 response for get_guild_emoji

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_emoji(
            guild_id="guild_id",
            emoji_id="emoji_id",
        )
        """
        _response = self._raw_client.get_guild_emoji(guild_id, emoji_id, request_options=request_options)
        return _response.data

    def delete_guild_emoji(
        self,
        guild_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_guild_emoji(
            guild_id="guild_id",
            emoji_id="emoji_id",
        )
        """
        _response = self._raw_client.delete_guild_emoji(guild_id, emoji_id, request_options=request_options)
        return _response.data

    def update_guild_emoji(
        self,
        guild_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmojiResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        emoji_id : SnowflakeType

        name : typing.Optional[str]

        roles : typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmojiResponse
            200 response for update_guild_emoji

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_guild_emoji(
            guild_id="guild_id",
            emoji_id="emoji_id",
        )
        """
        _response = self._raw_client.update_guild_emoji(
            guild_id, emoji_id, name=name, roles=roles, request_options=request_options
        )
        return _response.data

    def list_guild_emojis(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[EmojiResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[EmojiResponse]]
            200 response for list_guild_emojis

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_emojis(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_emojis(guild_id, request_options=request_options)
        return _response.data

    def create_guild_emoji(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        image: str,
        roles: typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmojiResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : str

        image : str

        roles : typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmojiResponse
            201 response for create_guild_emoji

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_guild_emoji(
            guild_id="guild_id",
            name="name",
            image="image",
        )
        """
        _response = self._raw_client.create_guild_emoji(
            guild_id, name=name, image=image, roles=roles, request_options=request_options
        )
        return _response.data

    def get_guild_widget_settings(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WidgetSettingsResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WidgetSettingsResponse
            200 response for get_guild_widget_settings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_widget_settings(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.get_guild_widget_settings(guild_id, request_options=request_options)
        return _response.data

    def update_guild_widget_settings(
        self,
        guild_id: SnowflakeType,
        *,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WidgetSettingsResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        channel_id : typing.Optional[SnowflakeType]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WidgetSettingsResponse
            200 response for update_guild_widget_settings

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_guild_widget_settings(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.update_guild_widget_settings(
            guild_id, channel_id=channel_id, enabled=enabled, request_options=request_options
        )
        return _response.data

    def get_guild_role(
        self,
        guild_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildRoleResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        role_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildRoleResponse
            200 response for get_guild_role

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_role(
            guild_id="guild_id",
            role_id="role_id",
        )
        """
        _response = self._raw_client.get_guild_role(guild_id, role_id, request_options=request_options)
        return _response.data

    def delete_guild_role(
        self,
        guild_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        role_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_guild_role(
            guild_id="guild_id",
            role_id="role_id",
        )
        """
        _response = self._raw_client.delete_guild_role(guild_id, role_id, request_options=request_options)
        return _response.data

    def update_guild_role(
        self,
        guild_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        permissions: typing.Optional[int] = OMIT,
        color: typing.Optional[int] = OMIT,
        hoist: typing.Optional[bool] = OMIT,
        mentionable: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        unicode_emoji: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildRoleResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        role_id : SnowflakeType

        name : typing.Optional[str]

        permissions : typing.Optional[int]

        color : typing.Optional[int]

        hoist : typing.Optional[bool]

        mentionable : typing.Optional[bool]

        icon : typing.Optional[str]

        unicode_emoji : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildRoleResponse
            200 response for update_guild_role

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_guild_role(
            guild_id="guild_id",
            role_id="role_id",
        )
        """
        _response = self._raw_client.update_guild_role(
            guild_id,
            role_id,
            name=name,
            permissions=permissions,
            color=color,
            hoist=hoist,
            mentionable=mentionable,
            icon=icon,
            unicode_emoji=unicode_emoji,
            request_options=request_options,
        )
        return _response.data

    def list_guild_roles(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GuildRoleResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GuildRoleResponse]
            200 response for list_guild_roles

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_roles(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_roles(guild_id, request_options=request_options)
        return _response.data

    def create_guild_role(
        self,
        guild_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        permissions: typing.Optional[int] = OMIT,
        color: typing.Optional[int] = OMIT,
        hoist: typing.Optional[bool] = OMIT,
        mentionable: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        unicode_emoji: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildRoleResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : typing.Optional[str]

        permissions : typing.Optional[int]

        color : typing.Optional[int]

        hoist : typing.Optional[bool]

        mentionable : typing.Optional[bool]

        icon : typing.Optional[str]

        unicode_emoji : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildRoleResponse
            200 response for create_guild_role

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.create_guild_role(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.create_guild_role(
            guild_id,
            name=name,
            permissions=permissions,
            color=color,
            hoist=hoist,
            mentionable=mentionable,
            icon=icon,
            unicode_emoji=unicode_emoji,
            request_options=request_options,
        )
        return _response.data

    def bulk_update_guild_roles(
        self,
        guild_id: SnowflakeType,
        *,
        request: typing.Sequence[BulkUpdateGuildRolesRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GuildRoleResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : typing.Sequence[BulkUpdateGuildRolesRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GuildRoleResponse]
            200 response for bulk_update_guild_roles

        Examples
        --------
        from fern import BulkUpdateGuildRolesRequestBodyItem, FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.bulk_update_guild_roles(
            guild_id="guild_id",
            request=[BulkUpdateGuildRolesRequestBodyItem()],
        )
        """
        _response = self._raw_client.bulk_update_guild_roles(guild_id, request=request, request_options=request_options)
        return _response.data

    def preview_prune_guild(
        self,
        guild_id: SnowflakeType,
        *,
        days: typing.Optional[int] = None,
        include_roles: typing.Optional[PreviewPruneGuildRequestIncludeRoles] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildPruneResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        days : typing.Optional[int]

        include_roles : typing.Optional[PreviewPruneGuildRequestIncludeRoles]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildPruneResponse
            200 response for preview_prune_guild

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.preview_prune_guild(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.preview_prune_guild(
            guild_id, days=days, include_roles=include_roles, request_options=request_options
        )
        return _response.data

    def prune_guild(
        self,
        guild_id: SnowflakeType,
        *,
        days: typing.Optional[int] = OMIT,
        compute_prune_count: typing.Optional[bool] = OMIT,
        include_roles: typing.Optional[PruneGuildRequestIncludeRoles] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildPruneResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        days : typing.Optional[int]

        compute_prune_count : typing.Optional[bool]

        include_roles : typing.Optional[PruneGuildRequestIncludeRoles]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildPruneResponse
            200 response for prune_guild

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.prune_guild(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.prune_guild(
            guild_id,
            days=days,
            compute_prune_count=compute_prune_count,
            include_roles=include_roles,
            request_options=request_options,
        )
        return _response.data

    def get_guild_ban(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildBanResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildBanResponse
            200 response for get_guild_ban

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild_ban(
            guild_id="guild_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.get_guild_ban(guild_id, user_id, request_options=request_options)
        return _response.data

    def ban_user_from_guild(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        delete_message_seconds: typing.Optional[int] = OMIT,
        delete_message_days: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        delete_message_seconds : typing.Optional[int]

        delete_message_days : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.ban_user_from_guild(
            guild_id="guild_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.ban_user_from_guild(
            guild_id,
            user_id,
            delete_message_seconds=delete_message_seconds,
            delete_message_days=delete_message_days,
            request_options=request_options,
        )
        return _response.data

    def unban_user_from_guild(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.unban_user_from_guild(
            guild_id="guild_id",
            user_id="user_id",
        )
        """
        _response = self._raw_client.unban_user_from_guild(guild_id, user_id, request_options=request_options)
        return _response.data

    def list_guild_bans(
        self,
        guild_id: SnowflakeType,
        *,
        limit: typing.Optional[int] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[GuildBanResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        limit : typing.Optional[int]

        before : typing.Optional[SnowflakeType]

        after : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[GuildBanResponse]]
            200 response for list_guild_bans

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.list_guild_bans(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.list_guild_bans(
            guild_id, limit=limit, before=before, after=after, request_options=request_options
        )
        return _response.data

    def set_guild_mfa_level(
        self, guild_id: SnowflakeType, *, level: GuildMfaLevel, request_options: typing.Optional[RequestOptions] = None
    ) -> GuildMfaLevelResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        level : GuildMfaLevel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildMfaLevelResponse
            200 response for set_guild_mfa_level

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.set_guild_mfa_level(
            guild_id="guild_id",
            level=1,
        )
        """
        _response = self._raw_client.set_guild_mfa_level(guild_id, level=level, request_options=request_options)
        return _response.data

    def get_stage_instance(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StageInstanceResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StageInstanceResponse
            200 response for get_stage_instance

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_stage_instance(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.get_stage_instance(channel_id, request_options=request_options)
        return _response.data

    def delete_stage_instance(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_stage_instance(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.delete_stage_instance(channel_id, request_options=request_options)
        return _response.data

    def update_stage_instance(
        self,
        channel_id: SnowflakeType,
        *,
        topic: typing.Optional[str] = OMIT,
        privacy_level: typing.Optional[StageInstancesPrivacyLevels] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StageInstanceResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        topic : typing.Optional[str]

        privacy_level : typing.Optional[StageInstancesPrivacyLevels]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StageInstanceResponse
            200 response for update_stage_instance

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_stage_instance(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.update_stage_instance(
            channel_id, topic=topic, privacy_level=privacy_level, request_options=request_options
        )
        return _response.data

    def get_sticker_pack(
        self, pack_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StickerPackResponse:
        """
        Parameters
        ----------
        pack_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StickerPackResponse
            200 response for get_sticker_pack

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_sticker_pack(
            pack_id="pack_id",
        )
        """
        _response = self._raw_client.get_sticker_pack(pack_id, request_options=request_options)
        return _response.data

    def get_application(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PrivateApplicationResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateApplicationResponse
            200 response for get_application

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_application(
            application_id="application_id",
        )
        """
        _response = self._raw_client.get_application(application_id, request_options=request_options)
        return _response.data

    def update_application(
        self,
        application_id: SnowflakeType,
        *,
        description: typing.Optional[ApplicationFormPartialDescription] = OMIT,
        icon: typing.Optional[str] = OMIT,
        cover_image: typing.Optional[str] = OMIT,
        team_id: typing.Optional[SnowflakeType] = OMIT,
        flags: typing.Optional[int] = OMIT,
        interactions_endpoint_url: typing.Optional[str] = OMIT,
        explicit_content_filter: typing.Optional[ApplicationExplicitContentFilterTypes] = OMIT,
        max_participants: typing.Optional[int] = OMIT,
        type: typing.Optional[ApplicationTypes] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        custom_install_url: typing.Optional[str] = OMIT,
        install_params: typing.Optional[ApplicationOAuth2InstallParams] = OMIT,
        role_connections_verification_url: typing.Optional[str] = OMIT,
        integration_types_config: typing.Optional[
            typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateApplicationResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        description : typing.Optional[ApplicationFormPartialDescription]

        icon : typing.Optional[str]

        cover_image : typing.Optional[str]

        team_id : typing.Optional[SnowflakeType]

        flags : typing.Optional[int]

        interactions_endpoint_url : typing.Optional[str]

        explicit_content_filter : typing.Optional[ApplicationExplicitContentFilterTypes]

        max_participants : typing.Optional[int]

        type : typing.Optional[ApplicationTypes]

        tags : typing.Optional[typing.Sequence[str]]

        custom_install_url : typing.Optional[str]

        install_params : typing.Optional[ApplicationOAuth2InstallParams]

        role_connections_verification_url : typing.Optional[str]

        integration_types_config : typing.Optional[typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateApplicationResponse
            200 response for update_application

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_application(
            application_id="application_id",
        )
        """
        _response = self._raw_client.update_application(
            application_id,
            description=description,
            icon=icon,
            cover_image=cover_image,
            team_id=team_id,
            flags=flags,
            interactions_endpoint_url=interactions_endpoint_url,
            explicit_content_filter=explicit_content_filter,
            max_participants=max_participants,
            type=type,
            tags=tags,
            custom_install_url=custom_install_url,
            install_params=install_params,
            role_connections_verification_url=role_connections_verification_url,
            integration_types_config=integration_types_config,
            request_options=request_options,
        )
        return _response.data

    def get_webhook_by_token(
        self, webhook_id: SnowflakeType, webhook_token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhookByTokenResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhookByTokenResponse
            200 response for get_webhook_by_token

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_webhook_by_token(
            webhook_id="webhook_id",
            webhook_token="webhook_token",
        )
        """
        _response = self._raw_client.get_webhook_by_token(webhook_id, webhook_token, request_options=request_options)
        return _response.data

    def execute_webhook(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        request: ExecuteWebhookRequestBody,
        wait: typing.Optional[bool] = None,
        thread_id: typing.Optional[SnowflakeType] = None,
        with_components: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[MessageResponse]:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        request : ExecuteWebhookRequestBody

        wait : typing.Optional[bool]

        thread_id : typing.Optional[SnowflakeType]

        with_components : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MessageResponse]
            200 response for execute_webhook

        Examples
        --------
        from fern import FernApi, IncomingWebhookRequestPartial

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.execute_webhook(
            webhook_id="webhook_id",
            webhook_token="webhook_token",
            request=IncomingWebhookRequestPartial(),
        )
        """
        _response = self._raw_client.execute_webhook(
            webhook_id,
            webhook_token,
            request=request,
            wait=wait,
            thread_id=thread_id,
            with_components=with_components,
            request_options=request_options,
        )
        return _response.data

    def delete_webhook_by_token(
        self, webhook_id: SnowflakeType, webhook_token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_webhook_by_token(
            webhook_id="webhook_id",
            webhook_token="webhook_token",
        )
        """
        _response = self._raw_client.delete_webhook_by_token(webhook_id, webhook_token, request_options=request_options)
        return _response.data

    def update_webhook_by_token(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        name: typing.Optional[str] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhookByTokenResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        name : typing.Optional[str]

        avatar : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhookByTokenResponse
            200 response for update_webhook_by_token

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_webhook_by_token(
            webhook_id="webhook_id",
            webhook_token="webhook_token",
        )
        """
        _response = self._raw_client.update_webhook_by_token(
            webhook_id, webhook_token, name=name, avatar=avatar, request_options=request_options
        )
        return _response.data

    def get_sticker(
        self, sticker_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStickerResponse:
        """
        Parameters
        ----------
        sticker_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStickerResponse
            200 response for get_sticker

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_sticker(
            sticker_id="sticker_id",
        )
        """
        _response = self._raw_client.get_sticker(sticker_id, request_options=request_options)
        return _response.data

    def get_webhook(
        self, webhook_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhookResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhookResponse
            200 response for get_webhook

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_webhook(
            webhook_id="webhook_id",
        )
        """
        _response = self._raw_client.get_webhook(webhook_id, request_options=request_options)
        return _response.data

    def delete_webhook(
        self, webhook_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_webhook(
            webhook_id="webhook_id",
        )
        """
        _response = self._raw_client.delete_webhook(webhook_id, request_options=request_options)
        return _response.data

    def update_webhook(
        self,
        webhook_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhookResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        name : typing.Optional[str]

        avatar : typing.Optional[str]

        channel_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhookResponse
            200 response for update_webhook

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_webhook(
            webhook_id="webhook_id",
        )
        """
        _response = self._raw_client.update_webhook(
            webhook_id, name=name, avatar=avatar, channel_id=channel_id, request_options=request_options
        )
        return _response.data

    def get_channel(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChannelResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChannelResponse
            200 response for get_channel

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_channel(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.get_channel(channel_id, request_options=request_options)
        return _response.data

    def delete_channel(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteChannelResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteChannelResponse
            200 response for delete_channel

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_channel(
            channel_id="channel_id",
        )
        """
        _response = self._raw_client.delete_channel(channel_id, request_options=request_options)
        return _response.data

    def update_channel(
        self,
        channel_id: SnowflakeType,
        *,
        request: UpdateChannelRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateChannelResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request : UpdateChannelRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateChannelResponse
            200 response for update_channel

        Examples
        --------
        from fern import FernApi, UpdateDmRequestPartial

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_channel(
            channel_id="channel_id",
            request=UpdateDmRequestPartial(),
        )
        """
        _response = self._raw_client.update_channel(channel_id, request=request, request_options=request_options)
        return _response.data

    def invite_resolve(
        self,
        code: str,
        *,
        with_counts: typing.Optional[bool] = None,
        guild_scheduled_event_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InviteResolveResponse:
        """
        Parameters
        ----------
        code : str

        with_counts : typing.Optional[bool]

        guild_scheduled_event_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteResolveResponse
            200 response for invite_resolve

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.invite_resolve(
            code="code",
        )
        """
        _response = self._raw_client.invite_resolve(
            code,
            with_counts=with_counts,
            guild_scheduled_event_id=guild_scheduled_event_id,
            request_options=request_options,
        )
        return _response.data

    def invite_revoke(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InviteRevokeResponse:
        """
        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteRevokeResponse
            200 response for invite_revoke

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.invite_revoke(
            code="code",
        )
        """
        _response = self._raw_client.invite_revoke(code, request_options=request_options)
        return _response.data

    def get_lobby(
        self, lobby_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LobbyResponse:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyResponse
            200 response for get_lobby

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_lobby(
            lobby_id="lobby_id",
        )
        """
        _response = self._raw_client.get_lobby(lobby_id, request_options=request_options)
        return _response.data

    def edit_lobby(
        self,
        lobby_id: SnowflakeType,
        *,
        idle_timeout_seconds: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        members: typing.Optional[typing.Sequence[LobbyMemberRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyResponse:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        idle_timeout_seconds : typing.Optional[int]

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        members : typing.Optional[typing.Sequence[LobbyMemberRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyResponse
            200 response for edit_lobby

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.edit_lobby(
            lobby_id="lobby_id",
        )
        """
        _response = self._raw_client.edit_lobby(
            lobby_id,
            idle_timeout_seconds=idle_timeout_seconds,
            metadata=metadata,
            members=members,
            request_options=request_options,
        )
        return _response.data

    def get_guild(
        self,
        guild_id: SnowflakeType,
        *,
        with_counts: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildWithCountsResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        with_counts : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildWithCountsResponse
            200 response for get_guild

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_guild(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.get_guild(guild_id, with_counts=with_counts, request_options=request_options)
        return _response.data

    def delete_guild(self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.delete_guild(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.delete_guild(guild_id, request_options=request_options)
        return _response.data

    def update_guild(
        self,
        guild_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        verification_level: typing.Optional[VerificationLevels] = OMIT,
        default_message_notifications: typing.Optional[UserNotificationSettings] = OMIT,
        explicit_content_filter: typing.Optional[GuildExplicitContentFilterTypes] = OMIT,
        preferred_locale: typing.Optional[AvailableLocalesEnum] = OMIT,
        afk_timeout: typing.Optional[AfkTimeouts] = OMIT,
        afk_channel_id: typing.Optional[SnowflakeType] = OMIT,
        system_channel_id: typing.Optional[SnowflakeType] = OMIT,
        owner_id: typing.Optional[SnowflakeType] = OMIT,
        splash: typing.Optional[str] = OMIT,
        banner: typing.Optional[str] = OMIT,
        system_channel_flags: typing.Optional[int] = OMIT,
        features: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        discovery_splash: typing.Optional[str] = OMIT,
        home_header: typing.Optional[str] = OMIT,
        rules_channel_id: typing.Optional[SnowflakeType] = OMIT,
        safety_alerts_channel_id: typing.Optional[SnowflakeType] = OMIT,
        public_updates_channel_id: typing.Optional[SnowflakeType] = OMIT,
        premium_progress_bar_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : typing.Optional[str]

        description : typing.Optional[str]

        region : typing.Optional[str]

        icon : typing.Optional[str]

        verification_level : typing.Optional[VerificationLevels]

        default_message_notifications : typing.Optional[UserNotificationSettings]

        explicit_content_filter : typing.Optional[GuildExplicitContentFilterTypes]

        preferred_locale : typing.Optional[AvailableLocalesEnum]

        afk_timeout : typing.Optional[AfkTimeouts]

        afk_channel_id : typing.Optional[SnowflakeType]

        system_channel_id : typing.Optional[SnowflakeType]

        owner_id : typing.Optional[SnowflakeType]

        splash : typing.Optional[str]

        banner : typing.Optional[str]

        system_channel_flags : typing.Optional[int]

        features : typing.Optional[typing.Sequence[typing.Optional[str]]]

        discovery_splash : typing.Optional[str]

        home_header : typing.Optional[str]

        rules_channel_id : typing.Optional[SnowflakeType]

        safety_alerts_channel_id : typing.Optional[SnowflakeType]

        public_updates_channel_id : typing.Optional[SnowflakeType]

        premium_progress_bar_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildResponse
            200 response for update_guild

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.update_guild(
            guild_id="guild_id",
        )
        """
        _response = self._raw_client.update_guild(
            guild_id,
            name=name,
            description=description,
            region=region,
            icon=icon,
            verification_level=verification_level,
            default_message_notifications=default_message_notifications,
            explicit_content_filter=explicit_content_filter,
            preferred_locale=preferred_locale,
            afk_timeout=afk_timeout,
            afk_channel_id=afk_channel_id,
            system_channel_id=system_channel_id,
            owner_id=owner_id,
            splash=splash,
            banner=banner,
            system_channel_flags=system_channel_flags,
            features=features,
            discovery_splash=discovery_splash,
            home_header=home_header,
            rules_channel_id=rules_channel_id,
            safety_alerts_channel_id=safety_alerts_channel_id,
            public_updates_channel_id=public_updates_channel_id,
            premium_progress_bar_enabled=premium_progress_bar_enabled,
            request_options=request_options,
        )
        return _response.data

    def get_user(
        self, user_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserResponse:
        """
        Parameters
        ----------
        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserResponse
            200 response for get_user

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.get_user(
            user_id="user_id",
        )
        """
        _response = self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : FernApiEnvironment
        The environment to use for requests from the client. from .environment import FernApiEnvironment



        Defaults to FernApiEnvironment.DEFAULT



    api_key : str
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        api_key: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def partner_sdk_unmerge_provisional_account(
        self,
        *,
        client_id: SnowflakeType,
        external_auth_token: str,
        external_auth_type: ApplicationIdentityProviderAuthType,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        client_id : SnowflakeType

        external_auth_token : str

        external_auth_type : ApplicationIdentityProviderAuthType

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.partner_sdk_unmerge_provisional_account(
                client_id="client_id",
                external_auth_token="external_auth_token",
                external_auth_type="external_auth_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.partner_sdk_unmerge_provisional_account(
            client_id=client_id,
            external_auth_token=external_auth_token,
            external_auth_type=external_auth_type,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data

    async def get_my_oauth2application(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PrivateApplicationResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateApplicationResponse
            200 response for get_my_oauth2_application

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_my_oauth2application()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_my_oauth2application(request_options=request_options)
        return _response.data

    async def list_my_connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ConnectedAccountResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ConnectedAccountResponse]]
            200 response for list_my_connections

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_my_connections()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_my_connections(request_options=request_options)
        return _response.data

    async def create_dm(
        self,
        *,
        recipient_id: typing.Optional[SnowflakeType] = OMIT,
        access_tokens: typing.Optional[typing.Sequence[str]] = OMIT,
        nicks: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDmResponse:
        """
        Parameters
        ----------
        recipient_id : typing.Optional[SnowflakeType]

        access_tokens : typing.Optional[typing.Sequence[str]]

        nicks : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDmResponse
            200 response for create_dm

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_dm()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_dm(
            recipient_id=recipient_id, access_tokens=access_tokens, nicks=nicks, request_options=request_options
        )
        return _response.data

    async def list_my_guilds(
        self,
        *,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        with_counts: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[MyGuildResponse]]:
        """
        Parameters
        ----------
        before : typing.Optional[SnowflakeType]

        after : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        with_counts : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[MyGuildResponse]]
            200 response for list_my_guilds

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_my_guilds()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_my_guilds(
            before=before, after=after, limit=limit, with_counts=with_counts, request_options=request_options
        )
        return _response.data

    async def get_my_application(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PrivateApplicationResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateApplicationResponse
            200 response for get_my_application

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_my_application()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_my_application(request_options=request_options)
        return _response.data

    async def update_my_application(
        self,
        *,
        description: typing.Optional[ApplicationFormPartialDescription] = OMIT,
        icon: typing.Optional[str] = OMIT,
        cover_image: typing.Optional[str] = OMIT,
        team_id: typing.Optional[SnowflakeType] = OMIT,
        flags: typing.Optional[int] = OMIT,
        interactions_endpoint_url: typing.Optional[str] = OMIT,
        explicit_content_filter: typing.Optional[ApplicationExplicitContentFilterTypes] = OMIT,
        max_participants: typing.Optional[int] = OMIT,
        type: typing.Optional[ApplicationTypes] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        custom_install_url: typing.Optional[str] = OMIT,
        install_params: typing.Optional[ApplicationOAuth2InstallParams] = OMIT,
        role_connections_verification_url: typing.Optional[str] = OMIT,
        integration_types_config: typing.Optional[
            typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateApplicationResponse:
        """
        Parameters
        ----------
        description : typing.Optional[ApplicationFormPartialDescription]

        icon : typing.Optional[str]

        cover_image : typing.Optional[str]

        team_id : typing.Optional[SnowflakeType]

        flags : typing.Optional[int]

        interactions_endpoint_url : typing.Optional[str]

        explicit_content_filter : typing.Optional[ApplicationExplicitContentFilterTypes]

        max_participants : typing.Optional[int]

        type : typing.Optional[ApplicationTypes]

        tags : typing.Optional[typing.Sequence[str]]

        custom_install_url : typing.Optional[str]

        install_params : typing.Optional[ApplicationOAuth2InstallParams]

        role_connections_verification_url : typing.Optional[str]

        integration_types_config : typing.Optional[typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateApplicationResponse
            200 response for update_my_application

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_my_application()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_my_application(
            description=description,
            icon=icon,
            cover_image=cover_image,
            team_id=team_id,
            flags=flags,
            interactions_endpoint_url=interactions_endpoint_url,
            explicit_content_filter=explicit_content_filter,
            max_participants=max_participants,
            type=type,
            tags=tags,
            custom_install_url=custom_install_url,
            install_params=install_params,
            role_connections_verification_url=role_connections_verification_url,
            integration_types_config=integration_types_config,
            request_options=request_options,
        )
        return _response.data

    async def partner_sdk_token(
        self,
        *,
        client_id: SnowflakeType,
        external_auth_token: str,
        external_auth_type: ApplicationIdentityProviderAuthType,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvisionalTokenResponse:
        """
        Parameters
        ----------
        client_id : SnowflakeType

        external_auth_token : str

        external_auth_type : ApplicationIdentityProviderAuthType

        client_secret : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvisionalTokenResponse
            200 response for partner_sdk_token

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.partner_sdk_token(
                client_id="client_id",
                external_auth_token="external_auth_token",
                external_auth_type="external_auth_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.partner_sdk_token(
            client_id=client_id,
            external_auth_token=external_auth_token,
            external_auth_type=external_auth_type,
            client_secret=client_secret,
            request_options=request_options,
        )
        return _response.data

    async def get_bot_gateway(self, *, request_options: typing.Optional[RequestOptions] = None) -> GatewayBotResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GatewayBotResponse
            200 response for get_bot_gateway

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_bot_gateway()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_bot_gateway(request_options=request_options)
        return _response.data

    async def get_openid_connect_userinfo(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OAuth2GetOpenIdConnectUserInfoResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuth2GetOpenIdConnectUserInfoResponse
            200 response for get_openid_connect_userinfo

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_openid_connect_userinfo()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_openid_connect_userinfo(request_options=request_options)
        return _response.data

    async def get_public_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> OAuth2GetKeys:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuth2GetKeys
            200 response for get_public_keys

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_public_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_public_keys(request_options=request_options)
        return _response.data

    async def get_my_oauth2authorization(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OAuth2GetAuthorizationResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OAuth2GetAuthorizationResponse
            200 response for get_my_oauth2_authorization

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_my_oauth2authorization()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_my_oauth2authorization(request_options=request_options)
        return _response.data

    async def list_voice_regions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[VoiceRegionResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[VoiceRegionResponse]]
            200 response for list_voice_regions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_voice_regions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_voice_regions(request_options=request_options)
        return _response.data

    async def get_my_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> UserPiiResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserPiiResponse
            200 response for get_my_user

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_my_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_my_user(request_options=request_options)
        return _response.data

    async def update_my_user(
        self,
        *,
        username: str,
        avatar: typing.Optional[str] = OMIT,
        banner: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UserPiiResponse:
        """
        Parameters
        ----------
        username : str

        avatar : typing.Optional[str]

        banner : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserPiiResponse
            200 response for update_my_user

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_my_user(
                username="username",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_my_user(
            username=username, avatar=avatar, banner=banner, request_options=request_options
        )
        return _response.data

    async def get_soundboard_default_sounds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SoundboardSoundResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SoundboardSoundResponse]
            200 response for get_soundboard_default_sounds

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_soundboard_default_sounds()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_soundboard_default_sounds(request_options=request_options)
        return _response.data

    async def create_stage_instance(
        self,
        *,
        topic: str,
        channel_id: SnowflakeType,
        privacy_level: typing.Optional[StageInstancesPrivacyLevels] = OMIT,
        guild_scheduled_event_id: typing.Optional[SnowflakeType] = OMIT,
        send_start_notification: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StageInstanceResponse:
        """
        Parameters
        ----------
        topic : str

        channel_id : SnowflakeType

        privacy_level : typing.Optional[StageInstancesPrivacyLevels]

        guild_scheduled_event_id : typing.Optional[SnowflakeType]

        send_start_notification : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StageInstanceResponse
            200 response for create_stage_instance

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_stage_instance(
                topic="topic",
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_stage_instance(
            topic=topic,
            channel_id=channel_id,
            privacy_level=privacy_level,
            guild_scheduled_event_id=guild_scheduled_event_id,
            send_start_notification=send_start_notification,
            request_options=request_options,
        )
        return _response.data

    async def list_sticker_packs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StickerPackCollectionResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StickerPackCollectionResponse
            200 response for list_sticker_packs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_sticker_packs()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_sticker_packs(request_options=request_options)
        return _response.data

    async def get_gateway(self, *, request_options: typing.Optional[RequestOptions] = None) -> GatewayResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GatewayResponse
            200 response for get_gateway

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_gateway()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_gateway(request_options=request_options)
        return _response.data

    async def create_lobby(
        self,
        *,
        idle_timeout_seconds: typing.Optional[int] = OMIT,
        members: typing.Optional[typing.Sequence[LobbyMemberRequest]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyResponse:
        """
        Parameters
        ----------
        idle_timeout_seconds : typing.Optional[int]

        members : typing.Optional[typing.Sequence[LobbyMemberRequest]]

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyResponse
            201 response for create_lobby

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_lobby()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_lobby(
            idle_timeout_seconds=idle_timeout_seconds,
            members=members,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def create_or_join_lobby(
        self,
        *,
        secret: str,
        idle_timeout_seconds: typing.Optional[int] = OMIT,
        lobby_metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        member_metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyResponse:
        """
        Parameters
        ----------
        secret : str

        idle_timeout_seconds : typing.Optional[int]

        lobby_metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        member_metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyResponse
            200 response for create_or_join_lobby

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_or_join_lobby(
                secret="secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_or_join_lobby(
            secret=secret,
            idle_timeout_seconds=idle_timeout_seconds,
            lobby_metadata=lobby_metadata,
            member_metadata=member_metadata,
            request_options=request_options,
        )
        return _response.data

    async def create_guild(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        verification_level: typing.Optional[VerificationLevels] = OMIT,
        default_message_notifications: typing.Optional[UserNotificationSettings] = OMIT,
        explicit_content_filter: typing.Optional[GuildExplicitContentFilterTypes] = OMIT,
        preferred_locale: typing.Optional[AvailableLocalesEnum] = OMIT,
        afk_timeout: typing.Optional[AfkTimeouts] = OMIT,
        roles: typing.Optional[typing.Sequence[CreateGuildRequestRoleItem]] = OMIT,
        channels: typing.Optional[typing.Sequence[CreateGuildRequestChannelItem]] = OMIT,
        afk_channel_id: typing.Optional[SnowflakeType] = OMIT,
        system_channel_id: typing.Optional[SnowflakeType] = OMIT,
        system_channel_flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildResponse:
        """
        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        region : typing.Optional[str]

        icon : typing.Optional[str]

        verification_level : typing.Optional[VerificationLevels]

        default_message_notifications : typing.Optional[UserNotificationSettings]

        explicit_content_filter : typing.Optional[GuildExplicitContentFilterTypes]

        preferred_locale : typing.Optional[AvailableLocalesEnum]

        afk_timeout : typing.Optional[AfkTimeouts]

        roles : typing.Optional[typing.Sequence[CreateGuildRequestRoleItem]]

        channels : typing.Optional[typing.Sequence[CreateGuildRequestChannelItem]]

        afk_channel_id : typing.Optional[SnowflakeType]

        system_channel_id : typing.Optional[SnowflakeType]

        system_channel_flags : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildResponse
            201 response for create_guild

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_guild(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_guild(
            name=name,
            description=description,
            region=region,
            icon=icon,
            verification_level=verification_level,
            default_message_notifications=default_message_notifications,
            explicit_content_filter=explicit_content_filter,
            preferred_locale=preferred_locale,
            afk_timeout=afk_timeout,
            roles=roles,
            channels=channels,
            afk_channel_id=afk_channel_id,
            system_channel_id=system_channel_id,
            system_channel_flags=system_channel_flags,
            request_options=request_options,
        )
        return _response.data

    async def list_my_private_archived_threads(
        self,
        channel_id: SnowflakeType,
        *,
        before: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadsResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        before : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadsResponse
            200 response for list_my_private_archived_threads

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_my_private_archived_threads(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_my_private_archived_threads(
            channel_id, before=before, limit=limit, request_options=request_options
        )
        return _response.data

    async def list_guild_application_command_permissions(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[CommandPermissionsResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[CommandPermissionsResponse]
            200 response for list_guild_application_command_permissions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_application_command_permissions(
                application_id="application_id",
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_application_command_permissions(
            application_id, guild_id, request_options=request_options
        )
        return _response.data

    async def get_guild_application_command_permissions(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommandPermissionsResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandPermissionsResponse
            200 response for get_guild_application_command_permissions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_application_command_permissions(
                application_id="application_id",
                guild_id="guild_id",
                command_id="command_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_application_command_permissions(
            application_id, guild_id, command_id, request_options=request_options
        )
        return _response.data

    async def set_guild_application_command_permissions(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        permissions: typing.Optional[typing.Sequence[ApplicationCommandPermission]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CommandPermissionsResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        command_id : SnowflakeType

        permissions : typing.Optional[typing.Sequence[ApplicationCommandPermission]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommandPermissionsResponse
            200 response for set_guild_application_command_permissions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.set_guild_application_command_permissions(
                application_id="application_id",
                guild_id="guild_id",
                command_id="command_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_guild_application_command_permissions(
            application_id, guild_id, command_id, permissions=permissions, request_options=request_options
        )
        return _response.data

    async def add_my_message_reaction(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        emoji_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.add_my_message_reaction(
                channel_id="channel_id",
                message_id="message_id",
                emoji_name="emoji_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_my_message_reaction(
            channel_id, message_id, emoji_name, request_options=request_options
        )
        return _response.data

    async def delete_my_message_reaction(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        emoji_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_my_message_reaction(
                channel_id="channel_id",
                message_id="message_id",
                emoji_name="emoji_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_my_message_reaction(
            channel_id, message_id, emoji_name, request_options=request_options
        )
        return _response.data

    async def list_private_archived_threads(
        self,
        channel_id: SnowflakeType,
        *,
        before: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadsResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        before : typing.Optional[dt.datetime]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadsResponse
            200 response for list_private_archived_threads

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_private_archived_threads(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_private_archived_threads(
            channel_id, before=before, limit=limit, request_options=request_options
        )
        return _response.data

    async def list_public_archived_threads(
        self,
        channel_id: SnowflakeType,
        *,
        before: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadsResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        before : typing.Optional[dt.datetime]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadsResponse
            200 response for list_public_archived_threads

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_public_archived_threads(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_public_archived_threads(
            channel_id, before=before, limit=limit, request_options=request_options
        )
        return _response.data

    async def get_application_user_role_connection(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ApplicationUserRoleConnectionResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationUserRoleConnectionResponse
            200 response for get_application_user_role_connection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_application_user_role_connection(
                application_id="application_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_application_user_role_connection(
            application_id, request_options=request_options
        )
        return _response.data

    async def update_application_user_role_connection(
        self,
        application_id: SnowflakeType,
        *,
        platform_name: typing.Optional[str] = OMIT,
        platform_username: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationUserRoleConnectionResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        platform_name : typing.Optional[str]

        platform_username : typing.Optional[str]

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationUserRoleConnectionResponse
            200 response for update_application_user_role_connection

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_application_user_role_connection(
                application_id="application_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_application_user_role_connection(
            application_id,
            platform_name=platform_name,
            platform_username=platform_username,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def delete_application_user_role_connection(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_application_user_role_connection(
                application_id="application_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_application_user_role_connection(
            application_id, request_options=request_options
        )
        return _response.data

    async def get_my_guild_member(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PrivateGuildMemberResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateGuildMemberResponse
            200 response for get_my_guild_member

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_my_guild_member(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_my_guild_member(guild_id, request_options=request_options)
        return _response.data

    async def get_application_role_connections_metadata(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]
            200 response for get_application_role_connections_metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_application_role_connections_metadata(
                application_id="application_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_application_role_connections_metadata(
            application_id, request_options=request_options
        )
        return _response.data

    async def update_application_role_connections_metadata(
        self,
        application_id: SnowflakeType,
        *,
        request: typing.Optional[typing.Sequence[ApplicationRoleConnectionsMetadataItemRequest]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request : typing.Optional[typing.Sequence[ApplicationRoleConnectionsMetadataItemRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]
            200 response for update_application_role_connections_metadata

        Examples
        --------
        import asyncio

        from fern import ApplicationRoleConnectionsMetadataItemRequest, AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_application_role_connections_metadata(
                application_id="application_id",
                request=[
                    ApplicationRoleConnectionsMetadataItemRequest(
                        type=1,
                        key="key",
                        name="name",
                        description="description",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_application_role_connections_metadata(
            application_id, request=request, request_options=request_options
        )
        return _response.data

    async def consume_entitlement(
        self,
        application_id: SnowflakeType,
        entitlement_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        entitlement_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.consume_entitlement(
                application_id="application_id",
                entitlement_id="entitlement_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.consume_entitlement(
            application_id, entitlement_id, request_options=request_options
        )
        return _response.data

    async def get_guild_application_command(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCommandResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCommandResponse
            200 response for get_guild_application_command

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_application_command(
                application_id="application_id",
                guild_id="guild_id",
                command_id="command_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_application_command(
            application_id, guild_id, command_id, request_options=request_options
        )
        return _response.data

    async def delete_guild_application_command(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_guild_application_command(
                application_id="application_id",
                guild_id="guild_id",
                command_id="command_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_guild_application_command(
            application_id, guild_id, command_id, request_options=request_options
        )
        return _response.data

    async def update_guild_application_command(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        options: typing.Optional[typing.Sequence[ApplicationCommandPatchRequestPartialOptionsItem]] = OMIT,
        default_member_permissions: typing.Optional[int] = OMIT,
        dm_permission: typing.Optional[bool] = OMIT,
        contexts: typing.Optional[typing.Sequence[InteractionContextType]] = OMIT,
        integration_types: typing.Optional[typing.Sequence[ApplicationIntegrationType]] = OMIT,
        handler: typing.Optional[ApplicationCommandHandler] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCommandResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        command_id : SnowflakeType

        name : typing.Optional[str]

        name_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        description : typing.Optional[str]

        description_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        options : typing.Optional[typing.Sequence[ApplicationCommandPatchRequestPartialOptionsItem]]

        default_member_permissions : typing.Optional[int]

        dm_permission : typing.Optional[bool]

        contexts : typing.Optional[typing.Sequence[InteractionContextType]]

        integration_types : typing.Optional[typing.Sequence[ApplicationIntegrationType]]

        handler : typing.Optional[ApplicationCommandHandler]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCommandResponse
            200 response for update_guild_application_command

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_guild_application_command(
                application_id="application_id",
                guild_id="guild_id",
                command_id="command_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_guild_application_command(
            application_id,
            guild_id,
            command_id,
            name=name,
            name_localizations=name_localizations,
            description=description,
            description_localizations=description_localizations,
            options=options,
            default_member_permissions=default_member_permissions,
            dm_permission=dm_permission,
            contexts=contexts,
            integration_types=integration_types,
            handler=handler,
            request_options=request_options,
        )
        return _response.data

    async def list_guild_application_commands(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        with_localizations: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ApplicationCommandResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        with_localizations : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ApplicationCommandResponse]]
            200 response for list_guild_application_commands

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_application_commands(
                application_id="application_id",
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_application_commands(
            application_id, guild_id, with_localizations=with_localizations, request_options=request_options
        )
        return _response.data

    async def create_guild_application_command(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        name: str,
        name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        options: typing.Optional[typing.Sequence[ApplicationCommandCreateRequestOptionsItem]] = OMIT,
        default_member_permissions: typing.Optional[int] = OMIT,
        dm_permission: typing.Optional[bool] = OMIT,
        contexts: typing.Optional[typing.Sequence[InteractionContextType]] = OMIT,
        integration_types: typing.Optional[typing.Sequence[ApplicationIntegrationType]] = OMIT,
        handler: typing.Optional[ApplicationCommandHandler] = OMIT,
        type: typing.Optional[ApplicationCommandType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCommandResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        name : str

        name_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        description : typing.Optional[str]

        description_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        options : typing.Optional[typing.Sequence[ApplicationCommandCreateRequestOptionsItem]]

        default_member_permissions : typing.Optional[int]

        dm_permission : typing.Optional[bool]

        contexts : typing.Optional[typing.Sequence[InteractionContextType]]

        integration_types : typing.Optional[typing.Sequence[ApplicationIntegrationType]]

        handler : typing.Optional[ApplicationCommandHandler]

        type : typing.Optional[ApplicationCommandType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCommandResponse
            200 response for create_guild_application_command

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_guild_application_command(
                application_id="application_id",
                guild_id="guild_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_guild_application_command(
            application_id,
            guild_id,
            name=name,
            name_localizations=name_localizations,
            description=description,
            description_localizations=description_localizations,
            options=options,
            default_member_permissions=default_member_permissions,
            dm_permission=dm_permission,
            contexts=contexts,
            integration_types=integration_types,
            handler=handler,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def bulk_set_guild_application_commands(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        request: typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ApplicationCommandResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        request : typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ApplicationCommandResponse]]
            200 response for bulk_set_guild_application_commands

        Examples
        --------
        import asyncio

        from fern import ApplicationCommandUpdateRequest, AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.bulk_set_guild_application_commands(
                application_id="application_id",
                guild_id="guild_id",
                request=[
                    ApplicationCommandUpdateRequest(
                        name="name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_set_guild_application_commands(
            application_id, guild_id, request=request, request_options=request_options
        )
        return _response.data

    async def join_thread(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.join_thread(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.join_thread(channel_id, request_options=request_options)
        return _response.data

    async def leave_thread(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.leave_thread(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.leave_thread(channel_id, request_options=request_options)
        return _response.data

    async def bulk_delete_messages(
        self,
        channel_id: SnowflakeType,
        *,
        messages: typing.Sequence[SnowflakeType],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        messages : typing.Sequence[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.bulk_delete_messages(
                channel_id="channel_id",
                messages=["messages"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_delete_messages(
            channel_id, messages=messages, request_options=request_options
        )
        return _response.data

    async def delete_user_message_reaction(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        emoji_name : str

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_user_message_reaction(
                channel_id="channel_id",
                message_id="message_id",
                emoji_name="emoji_name",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_user_message_reaction(
            channel_id, message_id, emoji_name, user_id, request_options=request_options
        )
        return _response.data

    async def list_message_reactions_by_emoji(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        type: typing.Optional[ReactionTypes] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[UserResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        emoji_name : str

        after : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        type : typing.Optional[ReactionTypes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[UserResponse]
            200 response for list_message_reactions_by_emoji

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_message_reactions_by_emoji(
                channel_id="channel_id",
                message_id="message_id",
                emoji_name="emoji_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_message_reactions_by_emoji(
            channel_id, message_id, emoji_name, after=after, limit=limit, type=type, request_options=request_options
        )
        return _response.data

    async def delete_all_message_reactions_by_emoji(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        emoji_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_all_message_reactions_by_emoji(
                channel_id="channel_id",
                message_id="message_id",
                emoji_name="emoji_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_all_message_reactions_by_emoji(
            channel_id, message_id, emoji_name, request_options=request_options
        )
        return _response.data

    async def delete_all_message_reactions(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_all_message_reactions(
                channel_id="channel_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_all_message_reactions(
            channel_id, message_id, request_options=request_options
        )
        return _response.data

    async def crosspost_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for crosspost_message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.crosspost_message(
                channel_id="channel_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.crosspost_message(channel_id, message_id, request_options=request_options)
        return _response.data

    async def create_thread_from_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        name: str,
        auto_archive_duration: typing.Optional[ThreadAutoArchiveDuration] = OMIT,
        rate_limit_per_user: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        name : str

        auto_archive_duration : typing.Optional[ThreadAutoArchiveDuration]

        rate_limit_per_user : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadResponse
            201 response for create_thread_from_message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_thread_from_message(
                channel_id="channel_id",
                message_id="message_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_thread_from_message(
            channel_id,
            message_id,
            name=name,
            auto_archive_duration=auto_archive_duration,
            rate_limit_per_user=rate_limit_per_user,
            request_options=request_options,
        )
        return _response.data

    async def thread_search(
        self,
        channel_id: SnowflakeType,
        *,
        name: typing.Optional[str] = None,
        slop: typing.Optional[int] = None,
        min_id: typing.Optional[SnowflakeType] = None,
        max_id: typing.Optional[SnowflakeType] = None,
        tag: typing.Optional[ThreadSearchRequestTag] = None,
        tag_setting: typing.Optional[ThreadSearchTagSetting] = None,
        archived: typing.Optional[bool] = None,
        sort_by: typing.Optional[ThreadSortingMode] = None,
        sort_order: typing.Optional[SortingOrder] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadSearchResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        name : typing.Optional[str]

        slop : typing.Optional[int]

        min_id : typing.Optional[SnowflakeType]

        max_id : typing.Optional[SnowflakeType]

        tag : typing.Optional[ThreadSearchRequestTag]

        tag_setting : typing.Optional[ThreadSearchTagSetting]

        archived : typing.Optional[bool]

        sort_by : typing.Optional[ThreadSortingMode]

        sort_order : typing.Optional[SortingOrder]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadSearchResponse
            200 response for thread_search

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.thread_search(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.thread_search(
            channel_id,
            name=name,
            slop=slop,
            min_id=min_id,
            max_id=max_id,
            tag=tag,
            tag_setting=tag_setting,
            archived=archived,
            sort_by=sort_by,
            sort_order=sort_order,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def get_answer_voters(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        answer_id: int,
        *,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PollAnswerDetailsResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        answer_id : int

        after : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PollAnswerDetailsResponse
            200 response for get_answer_voters

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_answer_voters(
                channel_id="channel_id",
                message_id="message_id",
                answer_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_answer_voters(
            channel_id, message_id, answer_id, after=after, limit=limit, request_options=request_options
        )
        return _response.data

    async def poll_expire(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for poll_expire

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.poll_expire(
                channel_id="channel_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.poll_expire(channel_id, message_id, request_options=request_options)
        return _response.data

    async def get_original_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        thread_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for get_original_webhook_message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_original_webhook_message(
                webhook_id="webhook_id",
                webhook_token="webhook_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_original_webhook_message(
            webhook_id, webhook_token, thread_id=thread_id, request_options=request_options
        )
        return _response.data

    async def delete_original_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        thread_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_original_webhook_message(
                webhook_id="webhook_id",
                webhook_token="webhook_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_original_webhook_message(
            webhook_id, webhook_token, thread_id=thread_id, request_options=request_options
        )
        return _response.data

    async def update_original_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        with_components: typing.Optional[bool] = None,
        content: typing.Optional[str] = OMIT,
        embeds: typing.Optional[typing.Sequence[RichEmbed]] = OMIT,
        allowed_mentions: typing.Optional[MessageAllowedMentionsRequest] = OMIT,
        components: typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]] = OMIT,
        attachments: typing.Optional[typing.Sequence[MessageAttachmentRequest]] = OMIT,
        poll: typing.Optional[PollCreateRequest] = OMIT,
        flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        thread_id : typing.Optional[SnowflakeType]

        with_components : typing.Optional[bool]

        content : typing.Optional[str]

        embeds : typing.Optional[typing.Sequence[RichEmbed]]

        allowed_mentions : typing.Optional[MessageAllowedMentionsRequest]

        components : typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]]

        attachments : typing.Optional[typing.Sequence[MessageAttachmentRequest]]

        poll : typing.Optional[PollCreateRequest]

        flags : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for update_original_webhook_message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_original_webhook_message(
                webhook_id="webhook_id",
                webhook_token="webhook_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_original_webhook_message(
            webhook_id,
            webhook_token,
            thread_id=thread_id,
            with_components=with_components,
            content=content,
            embeds=embeds,
            allowed_mentions=allowed_mentions,
            components=components,
            attachments=attachments,
            poll=poll,
            flags=flags,
            request_options=request_options,
        )
        return _response.data

    async def leave_lobby(
        self, lobby_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.leave_lobby(
                lobby_id="lobby_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.leave_lobby(lobby_id, request_options=request_options)
        return _response.data

    async def list_guild_scheduled_event_users(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        with_member: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ScheduledEventUserResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        guild_scheduled_event_id : SnowflakeType

        with_member : typing.Optional[bool]

        limit : typing.Optional[int]

        before : typing.Optional[SnowflakeType]

        after : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ScheduledEventUserResponse]]
            200 response for list_guild_scheduled_event_users

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_scheduled_event_users(
                guild_id="guild_id",
                guild_scheduled_event_id="guild_scheduled_event_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_scheduled_event_users(
            guild_id,
            guild_scheduled_event_id,
            with_member=with_member,
            limit=limit,
            before=before,
            after=after,
            request_options=request_options,
        )
        return _response.data

    async def get_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        rule_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetAutoModerationRuleResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        rule_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAutoModerationRuleResponse
            200 response for get_auto_moderation_rule

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_auto_moderation_rule(
                guild_id="guild_id",
                rule_id="rule_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_auto_moderation_rule(guild_id, rule_id, request_options=request_options)
        return _response.data

    async def delete_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        rule_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        rule_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_auto_moderation_rule(
                guild_id="guild_id",
                rule_id="rule_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_auto_moderation_rule(
            guild_id, rule_id, request_options=request_options
        )
        return _response.data

    async def update_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        rule_id: SnowflakeType,
        *,
        request: UpdateAutoModerationRuleRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAutoModerationRuleResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        rule_id : SnowflakeType

        request : UpdateAutoModerationRuleRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAutoModerationRuleResponse
            200 response for update_auto_moderation_rule

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, DefaultKeywordListUpsertRequestPartial

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_auto_moderation_rule(
                guild_id="guild_id",
                rule_id="rule_id",
                request=DefaultKeywordListUpsertRequestPartial(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_auto_moderation_rule(
            guild_id, rule_id, request=request, request_options=request_options
        )
        return _response.data

    async def list_auto_moderation_rules(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[typing.Optional[ListAutoModerationRulesResponseItem]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[typing.Optional[ListAutoModerationRulesResponseItem]]]
            200 response for list_auto_moderation_rules

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_auto_moderation_rules(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_auto_moderation_rules(guild_id, request_options=request_options)
        return _response.data

    async def create_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        *,
        request: CreateAutoModerationRuleRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAutoModerationRuleResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : CreateAutoModerationRuleRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAutoModerationRuleResponse
            200 response for create_auto_moderation_rule

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            DefaultKeywordListTriggerMetadata,
            DefaultKeywordListUpsertRequest,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_auto_moderation_rule(
                guild_id="guild_id",
                request=DefaultKeywordListUpsertRequest(
                    name="name",
                    event_type=1,
                    trigger_type=1,
                    trigger_metadata=DefaultKeywordListTriggerMetadata(),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_auto_moderation_rule(
            guild_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_self_voice_state(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VoiceStateResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceStateResponse
            200 response for get_self_voice_state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_self_voice_state(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_self_voice_state(guild_id, request_options=request_options)
        return _response.data

    async def update_self_voice_state(
        self,
        guild_id: SnowflakeType,
        *,
        request_to_speak_timestamp: typing.Optional[dt.datetime] = OMIT,
        suppress: typing.Optional[bool] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_to_speak_timestamp : typing.Optional[dt.datetime]

        suppress : typing.Optional[bool]

        channel_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_self_voice_state(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_self_voice_state(
            guild_id,
            request_to_speak_timestamp=request_to_speak_timestamp,
            suppress=suppress,
            channel_id=channel_id,
            request_options=request_options,
        )
        return _response.data

    async def search_guild_members(
        self,
        guild_id: SnowflakeType,
        *,
        limit: int,
        query: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        limit : int

        query : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GuildMemberResponse]
            200 response for search_guild_members

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search_guild_members(
                guild_id="guild_id",
                limit=1,
                query="query",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_guild_members(
            guild_id, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    async def get_active_guild_threads(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThreadsResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadsResponse
            200 response for get_active_guild_threads

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_active_guild_threads(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_active_guild_threads(guild_id, request_options=request_options)
        return _response.data

    async def update_my_guild_member(
        self,
        guild_id: SnowflakeType,
        *,
        nick: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateGuildMemberResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        nick : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateGuildMemberResponse
            200 response for update_my_guild_member

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_my_guild_member(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_my_guild_member(guild_id, nick=nick, request_options=request_options)
        return _response.data

    async def add_guild_member_role(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        role_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.add_guild_member_role(
                guild_id="guild_id",
                user_id="user_id",
                role_id="role_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_guild_member_role(
            guild_id, user_id, role_id, request_options=request_options
        )
        return _response.data

    async def delete_guild_member_role(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        role_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_guild_member_role(
                guild_id="guild_id",
                user_id="user_id",
                role_id="role_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_guild_member_role(
            guild_id, user_id, role_id, request_options=request_options
        )
        return _response.data

    async def leave_guild(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.leave_guild(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.leave_guild(guild_id, request_options=request_options)
        return _response.data

    async def applications_get_activity_instance(
        self,
        application_id: SnowflakeType,
        instance_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmbeddedActivityInstance:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmbeddedActivityInstance
            200 response for applications_get_activity_instance

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.applications_get_activity_instance(
                application_id="application_id",
                instance_id="instance_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.applications_get_activity_instance(
            application_id, instance_id, request_options=request_options
        )
        return _response.data

    async def get_entitlement(
        self,
        application_id: SnowflakeType,
        entitlement_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntitlementResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        entitlement_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntitlementResponse
            200 response for get_entitlement

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_entitlement(
                application_id="application_id",
                entitlement_id="entitlement_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entitlement(
            application_id, entitlement_id, request_options=request_options
        )
        return _response.data

    async def delete_entitlement(
        self,
        application_id: SnowflakeType,
        entitlement_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        entitlement_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_entitlement(
                application_id="application_id",
                entitlement_id="entitlement_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_entitlement(
            application_id, entitlement_id, request_options=request_options
        )
        return _response.data

    async def get_entitlements(
        self,
        application_id: SnowflakeType,
        *,
        sku_ids: GetEntitlementsRequestSkuIds,
        user_id: typing.Optional[SnowflakeType] = None,
        guild_id: typing.Optional[SnowflakeType] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        exclude_ended: typing.Optional[bool] = None,
        exclude_deleted: typing.Optional[bool] = None,
        only_active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Optional[EntitlementResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        sku_ids : GetEntitlementsRequestSkuIds

        user_id : typing.Optional[SnowflakeType]

        guild_id : typing.Optional[SnowflakeType]

        before : typing.Optional[SnowflakeType]

        after : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        exclude_ended : typing.Optional[bool]

        exclude_deleted : typing.Optional[bool]

        only_active : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Optional[EntitlementResponse]]
            200 response for get_entitlements

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_entitlements(
                application_id="application_id",
                sku_ids="sku_ids",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_entitlements(
            application_id,
            sku_ids=sku_ids,
            user_id=user_id,
            guild_id=guild_id,
            before=before,
            after=after,
            limit=limit,
            exclude_ended=exclude_ended,
            exclude_deleted=exclude_deleted,
            only_active=only_active,
            request_options=request_options,
        )
        return _response.data

    async def create_entitlement(
        self,
        application_id: SnowflakeType,
        *,
        sku_id: SnowflakeType,
        owner_id: SnowflakeType,
        owner_type: EntitlementOwnerTypes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntitlementResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        sku_id : SnowflakeType

        owner_id : SnowflakeType

        owner_type : EntitlementOwnerTypes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntitlementResponse
            200 response for create_entitlement

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_entitlement(
                application_id="application_id",
                sku_id="sku_id",
                owner_id="owner_id",
                owner_type=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_entitlement(
            application_id, sku_id=sku_id, owner_id=owner_id, owner_type=owner_type, request_options=request_options
        )
        return _response.data

    async def upload_application_attachment(
        self, application_id: SnowflakeType, *, file: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ActivitiesAttachmentResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        file : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActivitiesAttachmentResponse
            200 response for upload_application_attachment

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.upload_application_attachment(
                application_id="application_id",
                file="file",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_application_attachment(
            application_id, file=file, request_options=request_options
        )
        return _response.data

    async def get_application_command(
        self,
        application_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCommandResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCommandResponse
            200 response for get_application_command

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_application_command(
                application_id="application_id",
                command_id="command_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_application_command(
            application_id, command_id, request_options=request_options
        )
        return _response.data

    async def delete_application_command(
        self,
        application_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_application_command(
                application_id="application_id",
                command_id="command_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_application_command(
            application_id, command_id, request_options=request_options
        )
        return _response.data

    async def update_application_command(
        self,
        application_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        options: typing.Optional[typing.Sequence[ApplicationCommandPatchRequestPartialOptionsItem]] = OMIT,
        default_member_permissions: typing.Optional[int] = OMIT,
        dm_permission: typing.Optional[bool] = OMIT,
        contexts: typing.Optional[typing.Sequence[InteractionContextType]] = OMIT,
        integration_types: typing.Optional[typing.Sequence[ApplicationIntegrationType]] = OMIT,
        handler: typing.Optional[ApplicationCommandHandler] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCommandResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        command_id : SnowflakeType

        name : typing.Optional[str]

        name_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        description : typing.Optional[str]

        description_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        options : typing.Optional[typing.Sequence[ApplicationCommandPatchRequestPartialOptionsItem]]

        default_member_permissions : typing.Optional[int]

        dm_permission : typing.Optional[bool]

        contexts : typing.Optional[typing.Sequence[InteractionContextType]]

        integration_types : typing.Optional[typing.Sequence[ApplicationIntegrationType]]

        handler : typing.Optional[ApplicationCommandHandler]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCommandResponse
            200 response for update_application_command

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_application_command(
                application_id="application_id",
                command_id="command_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_application_command(
            application_id,
            command_id,
            name=name,
            name_localizations=name_localizations,
            description=description,
            description_localizations=description_localizations,
            options=options,
            default_member_permissions=default_member_permissions,
            dm_permission=dm_permission,
            contexts=contexts,
            integration_types=integration_types,
            handler=handler,
            request_options=request_options,
        )
        return _response.data

    async def list_application_commands(
        self,
        application_id: SnowflakeType,
        *,
        with_localizations: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ApplicationCommandResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        with_localizations : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ApplicationCommandResponse]]
            200 response for list_application_commands

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_application_commands(
                application_id="application_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_application_commands(
            application_id, with_localizations=with_localizations, request_options=request_options
        )
        return _response.data

    async def create_application_command(
        self,
        application_id: SnowflakeType,
        *,
        name: str,
        name_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_localizations: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        options: typing.Optional[typing.Sequence[ApplicationCommandCreateRequestOptionsItem]] = OMIT,
        default_member_permissions: typing.Optional[int] = OMIT,
        dm_permission: typing.Optional[bool] = OMIT,
        contexts: typing.Optional[typing.Sequence[InteractionContextType]] = OMIT,
        integration_types: typing.Optional[typing.Sequence[ApplicationIntegrationType]] = OMIT,
        handler: typing.Optional[ApplicationCommandHandler] = OMIT,
        type: typing.Optional[ApplicationCommandType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApplicationCommandResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        name : str

        name_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        description : typing.Optional[str]

        description_localizations : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        options : typing.Optional[typing.Sequence[ApplicationCommandCreateRequestOptionsItem]]

        default_member_permissions : typing.Optional[int]

        dm_permission : typing.Optional[bool]

        contexts : typing.Optional[typing.Sequence[InteractionContextType]]

        integration_types : typing.Optional[typing.Sequence[ApplicationIntegrationType]]

        handler : typing.Optional[ApplicationCommandHandler]

        type : typing.Optional[ApplicationCommandType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApplicationCommandResponse
            200 response for create_application_command

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_application_command(
                application_id="application_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_application_command(
            application_id,
            name=name,
            name_localizations=name_localizations,
            description=description,
            description_localizations=description_localizations,
            options=options,
            default_member_permissions=default_member_permissions,
            dm_permission=dm_permission,
            contexts=contexts,
            integration_types=integration_types,
            handler=handler,
            type=type,
            request_options=request_options,
        )
        return _response.data

    async def bulk_set_application_commands(
        self,
        application_id: SnowflakeType,
        *,
        request: typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ApplicationCommandResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request : typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ApplicationCommandResponse]]
            200 response for bulk_set_application_commands

        Examples
        --------
        import asyncio

        from fern import ApplicationCommandUpdateRequest, AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.bulk_set_application_commands(
                application_id="application_id",
                request=[
                    ApplicationCommandUpdateRequest(
                        name="name",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_set_application_commands(
            application_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_application_emoji(
        self,
        application_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmojiResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmojiResponse
            200 response for get_application_emoji

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_application_emoji(
                application_id="application_id",
                emoji_id="emoji_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_application_emoji(
            application_id, emoji_id, request_options=request_options
        )
        return _response.data

    async def delete_application_emoji(
        self,
        application_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_application_emoji(
                application_id="application_id",
                emoji_id="emoji_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_application_emoji(
            application_id, emoji_id, request_options=request_options
        )
        return _response.data

    async def update_application_emoji(
        self,
        application_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmojiResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        emoji_id : SnowflakeType

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmojiResponse
            200 response for update_application_emoji

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_application_emoji(
                application_id="application_id",
                emoji_id="emoji_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_application_emoji(
            application_id, emoji_id, name=name, request_options=request_options
        )
        return _response.data

    async def list_application_emojis(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListApplicationEmojisResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListApplicationEmojisResponse
            200 response for list_application_emojis

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_application_emojis(
                application_id="application_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_application_emojis(application_id, request_options=request_options)
        return _response.data

    async def create_application_emoji(
        self,
        application_id: SnowflakeType,
        *,
        name: str,
        image: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmojiResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        name : str

        image : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmojiResponse
            201 response for create_application_emoji

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_application_emoji(
                application_id="application_id",
                name="name",
                image="image",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_application_emoji(
            application_id, name=name, image=image, request_options=request_options
        )
        return _response.data

    async def create_interaction_response(
        self,
        interaction_id: SnowflakeType,
        interaction_token: str,
        *,
        request: CreateInteractionResponseRequestBody,
        with_response: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[InteractionCallbackResponse]:
        """
        Parameters
        ----------
        interaction_id : SnowflakeType

        interaction_token : str

        request : CreateInteractionResponseRequestBody

        with_response : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[InteractionCallbackResponse]
            200 response for create_interaction_response

        Examples
        --------
        import asyncio

        from fern import (
            ApplicationCommandAutocompleteCallbackRequest,
            AsyncFernApi,
            InteractionApplicationCommandAutocompleteCallbackIntegerData,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_interaction_response(
                interaction_id="interaction_id",
                interaction_token="interaction_token",
                request=ApplicationCommandAutocompleteCallbackRequest(
                    type=1,
                    data=InteractionApplicationCommandAutocompleteCallbackIntegerData(),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_interaction_response(
            interaction_id,
            interaction_token,
            request=request,
            with_response=with_response,
            request_options=request_options,
        )
        return _response.data

    async def send_soundboard_sound(
        self,
        channel_id: SnowflakeType,
        *,
        sound_id: SnowflakeType,
        source_guild_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        sound_id : SnowflakeType

        source_guild_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.send_soundboard_sound(
                channel_id="channel_id",
                sound_id="sound_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_soundboard_sound(
            channel_id, sound_id=sound_id, source_guild_id=source_guild_id, request_options=request_options
        )
        return _response.data

    async def get_thread_member(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        with_member: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadMemberResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        with_member : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadMemberResponse
            200 response for get_thread_member

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_thread_member(
                channel_id="channel_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_thread_member(
            channel_id, user_id, with_member=with_member, request_options=request_options
        )
        return _response.data

    async def add_thread_member(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.add_thread_member(
                channel_id="channel_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_thread_member(channel_id, user_id, request_options=request_options)
        return _response.data

    async def delete_thread_member(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_thread_member(
                channel_id="channel_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_thread_member(channel_id, user_id, request_options=request_options)
        return _response.data

    async def list_thread_members(
        self,
        channel_id: SnowflakeType,
        *,
        with_member: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ThreadMemberResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        with_member : typing.Optional[bool]

        limit : typing.Optional[int]

        after : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThreadMemberResponse]
            200 response for list_thread_members

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_thread_members(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_thread_members(
            channel_id, with_member=with_member, limit=limit, after=after, request_options=request_options
        )
        return _response.data

    async def set_channel_permission_overwrite(
        self,
        channel_id: SnowflakeType,
        overwrite_id: SnowflakeType,
        *,
        type: typing.Optional[ChannelPermissionOverwrites] = OMIT,
        allow: typing.Optional[int] = OMIT,
        deny: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        overwrite_id : SnowflakeType

        type : typing.Optional[ChannelPermissionOverwrites]

        allow : typing.Optional[int]

        deny : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.set_channel_permission_overwrite(
                channel_id="channel_id",
                overwrite_id="overwrite_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_channel_permission_overwrite(
            channel_id, overwrite_id, type=type, allow=allow, deny=deny, request_options=request_options
        )
        return _response.data

    async def delete_channel_permission_overwrite(
        self,
        channel_id: SnowflakeType,
        overwrite_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        overwrite_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_channel_permission_overwrite(
                channel_id="channel_id",
                overwrite_id="overwrite_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_channel_permission_overwrite(
            channel_id, overwrite_id, request_options=request_options
        )
        return _response.data

    async def add_group_dm_user(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        access_token: typing.Optional[str] = OMIT,
        nick: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[AddGroupDmUserResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        access_token : typing.Optional[str]

        nick : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[AddGroupDmUserResponse]
            201 response for add_group_dm_user

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.add_group_dm_user(
                channel_id="channel_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_group_dm_user(
            channel_id, user_id, access_token=access_token, nick=nick, request_options=request_options
        )
        return _response.data

    async def delete_group_dm_user(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_group_dm_user(
                channel_id="channel_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_group_dm_user(channel_id, user_id, request_options=request_options)
        return _response.data

    async def follow_channel(
        self,
        channel_id: SnowflakeType,
        *,
        webhook_channel_id: SnowflakeType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ChannelFollowerResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        webhook_channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ChannelFollowerResponse
            200 response for follow_channel

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.follow_channel(
                channel_id="channel_id",
                webhook_channel_id="webhook_channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_channel(
            channel_id, webhook_channel_id=webhook_channel_id, request_options=request_options
        )
        return _response.data

    async def get_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for get_message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_message(
                channel_id="channel_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_message(channel_id, message_id, request_options=request_options)
        return _response.data

    async def delete_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_message(
                channel_id="channel_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_message(channel_id, message_id, request_options=request_options)
        return _response.data

    async def update_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        content: typing.Optional[str] = OMIT,
        embeds: typing.Optional[typing.Sequence[RichEmbed]] = OMIT,
        flags: typing.Optional[int] = OMIT,
        allowed_mentions: typing.Optional[MessageAllowedMentionsRequest] = OMIT,
        sticker_ids: typing.Optional[typing.Sequence[SnowflakeType]] = OMIT,
        components: typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]] = OMIT,
        attachments: typing.Optional[typing.Sequence[MessageAttachmentRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        content : typing.Optional[str]

        embeds : typing.Optional[typing.Sequence[RichEmbed]]

        flags : typing.Optional[int]

        allowed_mentions : typing.Optional[MessageAllowedMentionsRequest]

        sticker_ids : typing.Optional[typing.Sequence[SnowflakeType]]

        components : typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]]

        attachments : typing.Optional[typing.Sequence[MessageAttachmentRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for update_message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_message(
                channel_id="channel_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_message(
            channel_id,
            message_id,
            content=content,
            embeds=embeds,
            flags=flags,
            allowed_mentions=allowed_mentions,
            sticker_ids=sticker_ids,
            components=components,
            attachments=attachments,
            request_options=request_options,
        )
        return _response.data

    async def list_messages(
        self,
        channel_id: SnowflakeType,
        *,
        around: typing.Optional[SnowflakeType] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[MessageResponse]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        around : typing.Optional[SnowflakeType]

        before : typing.Optional[SnowflakeType]

        after : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[MessageResponse]]
            200 response for list_messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_messages(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_messages(
            channel_id, around=around, before=before, after=after, limit=limit, request_options=request_options
        )
        return _response.data

    async def create_message(
        self,
        channel_id: SnowflakeType,
        *,
        content: typing.Optional[str] = OMIT,
        embeds: typing.Optional[typing.Sequence[RichEmbed]] = OMIT,
        allowed_mentions: typing.Optional[MessageAllowedMentionsRequest] = OMIT,
        sticker_ids: typing.Optional[typing.Sequence[SnowflakeType]] = OMIT,
        components: typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]] = OMIT,
        flags: typing.Optional[int] = OMIT,
        attachments: typing.Optional[typing.Sequence[MessageAttachmentRequest]] = OMIT,
        poll: typing.Optional[PollCreateRequest] = OMIT,
        confetti_potion: typing.Optional[ConfettiPotionCreateRequest] = OMIT,
        message_reference: typing.Optional[MessageReferenceRequest] = OMIT,
        nonce: typing.Optional[MessageCreateRequestNonce] = OMIT,
        enforce_nonce: typing.Optional[bool] = OMIT,
        tts: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        content : typing.Optional[str]

        embeds : typing.Optional[typing.Sequence[RichEmbed]]

        allowed_mentions : typing.Optional[MessageAllowedMentionsRequest]

        sticker_ids : typing.Optional[typing.Sequence[SnowflakeType]]

        components : typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]]

        flags : typing.Optional[int]

        attachments : typing.Optional[typing.Sequence[MessageAttachmentRequest]]

        poll : typing.Optional[PollCreateRequest]

        confetti_potion : typing.Optional[ConfettiPotionCreateRequest]

        message_reference : typing.Optional[MessageReferenceRequest]

        nonce : typing.Optional[MessageCreateRequestNonce]

        enforce_nonce : typing.Optional[bool]

        tts : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for create_message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_message(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_message(
            channel_id,
            content=content,
            embeds=embeds,
            allowed_mentions=allowed_mentions,
            sticker_ids=sticker_ids,
            components=components,
            flags=flags,
            attachments=attachments,
            poll=poll,
            confetti_potion=confetti_potion,
            message_reference=message_reference,
            nonce=nonce,
            enforce_nonce=enforce_nonce,
            tts=tts,
            request_options=request_options,
        )
        return _response.data

    async def list_channel_webhooks(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ListChannelWebhooksResponseItem]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ListChannelWebhooksResponseItem]]
            200 response for list_channel_webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_channel_webhooks(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_channel_webhooks(channel_id, request_options=request_options)
        return _response.data

    async def create_webhook(
        self,
        channel_id: SnowflakeType,
        *,
        name: str,
        avatar: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildIncomingWebhookResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        name : str

        avatar : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildIncomingWebhookResponse
            200 response for create_webhook

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_webhook(
                channel_id="channel_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_webhook(
            channel_id, name=name, avatar=avatar, request_options=request_options
        )
        return _response.data

    async def list_channel_invites(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ListChannelInvitesResponseItem]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ListChannelInvitesResponseItem]]
            200 response for list_channel_invites

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_channel_invites(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_channel_invites(channel_id, request_options=request_options)
        return _response.data

    async def create_channel_invite(
        self,
        channel_id: SnowflakeType,
        *,
        request: CreateChannelInviteRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[CreateChannelInviteResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request : CreateChannelInviteRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[CreateChannelInviteResponse]
            200 response for create_channel_invite

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, CreateGroupDmInviteRequest

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_channel_invite(
                channel_id="channel_id",
                request=CreateGroupDmInviteRequest(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_channel_invite(
            channel_id, request=request, request_options=request_options
        )
        return _response.data

    async def create_thread(
        self,
        channel_id: SnowflakeType,
        *,
        request: CreateThreadRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatedThreadResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request : CreateThreadRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatedThreadResponse
            201 response for create_thread

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            BaseCreateMessageCreateRequest,
            CreateForumThreadRequest,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_thread(
                channel_id="channel_id",
                request=CreateForumThreadRequest(
                    name="name",
                    message=BaseCreateMessageCreateRequest(),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_thread(channel_id, request=request, request_options=request_options)
        return _response.data

    async def trigger_typing_indicator(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[TypingIndicatorResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[TypingIndicatorResponse]
            200 response for trigger_typing_indicator

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.trigger_typing_indicator(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trigger_typing_indicator(channel_id, request_options=request_options)
        return _response.data

    async def pin_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.pin_message(
                channel_id="channel_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pin_message(channel_id, message_id, request_options=request_options)
        return _response.data

    async def unpin_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.unpin_message(
                channel_id="channel_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unpin_message(channel_id, message_id, request_options=request_options)
        return _response.data

    async def list_pinned_messages(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[MessageResponse]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[MessageResponse]]
            200 response for list_pinned_messages

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_pinned_messages(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_pinned_messages(channel_id, request_options=request_options)
        return _response.data

    async def get_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        message_id: SnowflakeType,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        message_id : SnowflakeType

        thread_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for get_webhook_message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_webhook_message(
                webhook_id="webhook_id",
                webhook_token="webhook_token",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhook_message(
            webhook_id, webhook_token, message_id, thread_id=thread_id, request_options=request_options
        )
        return _response.data

    async def delete_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        message_id: SnowflakeType,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        message_id : SnowflakeType

        thread_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_webhook_message(
                webhook_id="webhook_id",
                webhook_token="webhook_token",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_webhook_message(
            webhook_id, webhook_token, message_id, thread_id=thread_id, request_options=request_options
        )
        return _response.data

    async def update_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        message_id: SnowflakeType,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        with_components: typing.Optional[bool] = None,
        content: typing.Optional[str] = OMIT,
        embeds: typing.Optional[typing.Sequence[RichEmbed]] = OMIT,
        allowed_mentions: typing.Optional[MessageAllowedMentionsRequest] = OMIT,
        components: typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]] = OMIT,
        attachments: typing.Optional[typing.Sequence[MessageAttachmentRequest]] = OMIT,
        poll: typing.Optional[PollCreateRequest] = OMIT,
        flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        message_id : SnowflakeType

        thread_id : typing.Optional[SnowflakeType]

        with_components : typing.Optional[bool]

        content : typing.Optional[str]

        embeds : typing.Optional[typing.Sequence[RichEmbed]]

        allowed_mentions : typing.Optional[MessageAllowedMentionsRequest]

        components : typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]]

        attachments : typing.Optional[typing.Sequence[MessageAttachmentRequest]]

        poll : typing.Optional[PollCreateRequest]

        flags : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageResponse
            200 response for update_webhook_message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_webhook_message(
                webhook_id="webhook_id",
                webhook_token="webhook_token",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_webhook_message(
            webhook_id,
            webhook_token,
            message_id,
            thread_id=thread_id,
            with_components=with_components,
            content=content,
            embeds=embeds,
            allowed_mentions=allowed_mentions,
            components=components,
            attachments=attachments,
            poll=poll,
            flags=flags,
            request_options=request_options,
        )
        return _response.data

    async def execute_github_compatible_webhook(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        sender: GithubUser,
        wait: typing.Optional[bool] = None,
        thread_id: typing.Optional[SnowflakeType] = None,
        action: typing.Optional[str] = OMIT,
        ref: typing.Optional[str] = OMIT,
        ref_type: typing.Optional[str] = OMIT,
        comment: typing.Optional[GithubComment] = OMIT,
        issue: typing.Optional[GithubIssue] = OMIT,
        pull_request: typing.Optional[GithubIssue] = OMIT,
        repository: typing.Optional[GithubRepository] = OMIT,
        forkee: typing.Optional[GithubRepository] = OMIT,
        member: typing.Optional[GithubUser] = OMIT,
        release: typing.Optional[GithubRelease] = OMIT,
        head_commit: typing.Optional[GithubCommit] = OMIT,
        commits: typing.Optional[typing.Sequence[GithubCommit]] = OMIT,
        forced: typing.Optional[bool] = OMIT,
        compare: typing.Optional[str] = OMIT,
        review: typing.Optional[GithubReview] = OMIT,
        check_run: typing.Optional[GithubCheckRun] = OMIT,
        check_suite: typing.Optional[GithubCheckSuite] = OMIT,
        discussion: typing.Optional[GithubDiscussion] = OMIT,
        answer: typing.Optional[GithubComment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        sender : GithubUser

        wait : typing.Optional[bool]

        thread_id : typing.Optional[SnowflakeType]

        action : typing.Optional[str]

        ref : typing.Optional[str]

        ref_type : typing.Optional[str]

        comment : typing.Optional[GithubComment]

        issue : typing.Optional[GithubIssue]

        pull_request : typing.Optional[GithubIssue]

        repository : typing.Optional[GithubRepository]

        forkee : typing.Optional[GithubRepository]

        member : typing.Optional[GithubUser]

        release : typing.Optional[GithubRelease]

        head_commit : typing.Optional[GithubCommit]

        commits : typing.Optional[typing.Sequence[GithubCommit]]

        forced : typing.Optional[bool]

        compare : typing.Optional[str]

        review : typing.Optional[GithubReview]

        check_run : typing.Optional[GithubCheckRun]

        check_suite : typing.Optional[GithubCheckSuite]

        discussion : typing.Optional[GithubDiscussion]

        answer : typing.Optional[GithubComment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GithubUser

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.execute_github_compatible_webhook(
                webhook_id="webhook_id",
                webhook_token="webhook_token",
                sender=GithubUser(
                    id=1,
                    login="login",
                    html_url="html_url",
                    avatar_url="avatar_url",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_github_compatible_webhook(
            webhook_id,
            webhook_token,
            sender=sender,
            wait=wait,
            thread_id=thread_id,
            action=action,
            ref=ref,
            ref_type=ref_type,
            comment=comment,
            issue=issue,
            pull_request=pull_request,
            repository=repository,
            forkee=forkee,
            member=member,
            release=release,
            head_commit=head_commit,
            commits=commits,
            forced=forced,
            compare=compare,
            review=review,
            check_run=check_run,
            check_suite=check_suite,
            discussion=discussion,
            answer=answer,
            request_options=request_options,
        )
        return _response.data

    async def execute_slack_compatible_webhook(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        wait: typing.Optional[bool] = None,
        thread_id: typing.Optional[SnowflakeType] = None,
        text: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        icon_url: typing.Optional[str] = OMIT,
        attachments: typing.Optional[typing.Sequence[WebhookSlackEmbed]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[str]:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        wait : typing.Optional[bool]

        thread_id : typing.Optional[SnowflakeType]

        text : typing.Optional[str]

        username : typing.Optional[str]

        icon_url : typing.Optional[str]

        attachments : typing.Optional[typing.Sequence[WebhookSlackEmbed]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[str]
            200 response for execute_slack_compatible_webhook

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.execute_slack_compatible_webhook(
                webhook_id="webhook_id",
                webhook_token="webhook_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_slack_compatible_webhook(
            webhook_id,
            webhook_token,
            wait=wait,
            thread_id=thread_id,
            text=text,
            username=username,
            icon_url=icon_url,
            attachments=attachments,
            request_options=request_options,
        )
        return _response.data

    async def edit_lobby_channel_link(
        self,
        lobby_id: SnowflakeType,
        *,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyResponse:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        channel_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyResponse
            200 response for edit_lobby_channel_link

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.edit_lobby_channel_link(
                lobby_id="lobby_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.edit_lobby_channel_link(
            lobby_id, channel_id=channel_id, request_options=request_options
        )
        return _response.data

    async def create_lobby_message(
        self,
        lobby_id: SnowflakeType,
        *,
        content: typing.Optional[str] = OMIT,
        embeds: typing.Optional[typing.Sequence[RichEmbed]] = OMIT,
        allowed_mentions: typing.Optional[MessageAllowedMentionsRequest] = OMIT,
        sticker_ids: typing.Optional[typing.Sequence[SnowflakeType]] = OMIT,
        components: typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]] = OMIT,
        flags: typing.Optional[int] = OMIT,
        attachments: typing.Optional[typing.Sequence[MessageAttachmentRequest]] = OMIT,
        poll: typing.Optional[PollCreateRequest] = OMIT,
        confetti_potion: typing.Optional[ConfettiPotionCreateRequest] = OMIT,
        message_reference: typing.Optional[MessageReferenceRequest] = OMIT,
        nonce: typing.Optional[SdkMessageRequestNonce] = OMIT,
        enforce_nonce: typing.Optional[bool] = OMIT,
        tts: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyMessageResponse:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        content : typing.Optional[str]

        embeds : typing.Optional[typing.Sequence[RichEmbed]]

        allowed_mentions : typing.Optional[MessageAllowedMentionsRequest]

        sticker_ids : typing.Optional[typing.Sequence[SnowflakeType]]

        components : typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]]

        flags : typing.Optional[int]

        attachments : typing.Optional[typing.Sequence[MessageAttachmentRequest]]

        poll : typing.Optional[PollCreateRequest]

        confetti_potion : typing.Optional[ConfettiPotionCreateRequest]

        message_reference : typing.Optional[MessageReferenceRequest]

        nonce : typing.Optional[SdkMessageRequestNonce]

        enforce_nonce : typing.Optional[bool]

        tts : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyMessageResponse
            201 response for create_lobby_message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_lobby_message(
                lobby_id="lobby_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_lobby_message(
            lobby_id,
            content=content,
            embeds=embeds,
            allowed_mentions=allowed_mentions,
            sticker_ids=sticker_ids,
            components=components,
            flags=flags,
            attachments=attachments,
            poll=poll,
            confetti_potion=confetti_potion,
            message_reference=message_reference,
            nonce=nonce,
            enforce_nonce=enforce_nonce,
            tts=tts,
            request_options=request_options,
        )
        return _response.data

    async def add_lobby_member(
        self,
        lobby_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyMemberResponse:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        user_id : SnowflakeType

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        flags : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyMemberResponse
            200 response for add_lobby_member

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.add_lobby_member(
                lobby_id="lobby_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_lobby_member(
            lobby_id, user_id, metadata=metadata, flags=flags, request_options=request_options
        )
        return _response.data

    async def delete_lobby_member(
        self,
        lobby_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_lobby_member(
                lobby_id="lobby_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_lobby_member(lobby_id, user_id, request_options=request_options)
        return _response.data

    async def get_guild_template(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuildTemplateResponse:
        """
        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildTemplateResponse
            200 response for get_guild_template

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_template(
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_template(code, request_options=request_options)
        return _response.data

    async def create_guild_from_template(
        self,
        code: str,
        *,
        name: str,
        icon: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildResponse:
        """
        Parameters
        ----------
        code : str

        name : str

        icon : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildResponse
            201 response for create_guild_from_template

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_guild_from_template(
                code="code",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_guild_from_template(
            code, name=name, icon=icon, request_options=request_options
        )
        return _response.data

    async def get_guild_new_member_welcome(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[GuildHomeSettingsResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[GuildHomeSettingsResponse]
            200 response for get_guild_new_member_welcome

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_new_member_welcome(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_new_member_welcome(guild_id, request_options=request_options)
        return _response.data

    async def get_guild_soundboard_sound(
        self,
        guild_id: SnowflakeType,
        sound_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoundboardSoundResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sound_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoundboardSoundResponse
            200 response for get_guild_soundboard_sound

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_soundboard_sound(
                guild_id="guild_id",
                sound_id="sound_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_soundboard_sound(
            guild_id, sound_id, request_options=request_options
        )
        return _response.data

    async def delete_guild_soundboard_sound(
        self,
        guild_id: SnowflakeType,
        sound_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sound_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_guild_soundboard_sound(
                guild_id="guild_id",
                sound_id="sound_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_guild_soundboard_sound(
            guild_id, sound_id, request_options=request_options
        )
        return _response.data

    async def update_guild_soundboard_sound(
        self,
        guild_id: SnowflakeType,
        sound_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        volume: typing.Optional[float] = OMIT,
        emoji_id: typing.Optional[SnowflakeType] = OMIT,
        emoji_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoundboardSoundResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sound_id : SnowflakeType

        name : typing.Optional[str]

        volume : typing.Optional[float]

        emoji_id : typing.Optional[SnowflakeType]

        emoji_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoundboardSoundResponse
            200 response for update_guild_soundboard_sound

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_guild_soundboard_sound(
                guild_id="guild_id",
                sound_id="sound_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_guild_soundboard_sound(
            guild_id,
            sound_id,
            name=name,
            volume=volume,
            emoji_id=emoji_id,
            emoji_name=emoji_name,
            request_options=request_options,
        )
        return _response.data

    async def list_guild_soundboard_sounds(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListGuildSoundboardSoundsResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListGuildSoundboardSoundsResponse
            200 response for list_guild_soundboard_sounds

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_soundboard_sounds(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_soundboard_sounds(guild_id, request_options=request_options)
        return _response.data

    async def create_guild_soundboard_sound(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        sound: str,
        volume: typing.Optional[float] = OMIT,
        emoji_id: typing.Optional[SnowflakeType] = OMIT,
        emoji_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SoundboardSoundResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : str

        sound : str

        volume : typing.Optional[float]

        emoji_id : typing.Optional[SnowflakeType]

        emoji_name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SoundboardSoundResponse
            201 response for create_guild_soundboard_sound

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_guild_soundboard_sound(
                guild_id="guild_id",
                name="name",
                sound="sound",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_guild_soundboard_sound(
            guild_id,
            name=name,
            sound=sound,
            volume=volume,
            emoji_id=emoji_id,
            emoji_name=emoji_name,
            request_options=request_options,
        )
        return _response.data

    async def get_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        with_user_count: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetGuildScheduledEventResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        guild_scheduled_event_id : SnowflakeType

        with_user_count : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetGuildScheduledEventResponse
            200 response for get_guild_scheduled_event

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_scheduled_event(
                guild_id="guild_id",
                guild_scheduled_event_id="guild_scheduled_event_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_scheduled_event(
            guild_id, guild_scheduled_event_id, with_user_count=with_user_count, request_options=request_options
        )
        return _response.data

    async def delete_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        guild_scheduled_event_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_guild_scheduled_event(
                guild_id="guild_id",
                guild_scheduled_event_id="guild_scheduled_event_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_guild_scheduled_event(
            guild_id, guild_scheduled_event_id, request_options=request_options
        )
        return _response.data

    async def update_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        request: UpdateGuildScheduledEventRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateGuildScheduledEventResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        guild_scheduled_event_id : SnowflakeType

        request : UpdateGuildScheduledEventRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateGuildScheduledEventResponse
            200 response for update_guild_scheduled_event

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ExternalScheduledEventPatchRequestPartial

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_guild_scheduled_event(
                guild_id="guild_id",
                guild_scheduled_event_id="guild_scheduled_event_id",
                request=ExternalScheduledEventPatchRequestPartial(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_guild_scheduled_event(
            guild_id, guild_scheduled_event_id, request=request, request_options=request_options
        )
        return _response.data

    async def list_guild_scheduled_events(
        self,
        guild_id: SnowflakeType,
        *,
        with_user_count: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[ListGuildScheduledEventsResponseItem]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        with_user_count : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ListGuildScheduledEventsResponseItem]]
            200 response for list_guild_scheduled_events

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_scheduled_events(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_scheduled_events(
            guild_id, with_user_count=with_user_count, request_options=request_options
        )
        return _response.data

    async def create_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        *,
        request: CreateGuildScheduledEventRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateGuildScheduledEventResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : CreateGuildScheduledEventRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateGuildScheduledEventResponse
            200 response for create_guild_scheduled_event

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            EntityMetadataExternal,
            ExternalScheduledEventCreateRequest,
        )

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_guild_scheduled_event(
                guild_id="guild_id",
                request=ExternalScheduledEventCreateRequest(
                    name="name",
                    scheduled_start_time=datetime.datetime.fromisoformat(
                        "2024-01-15 09:30:00+00:00",
                    ),
                    privacy_level=1,
                    entity_type=1,
                    entity_metadata=EntityMetadataExternal(
                        location="location",
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_guild_scheduled_event(
            guild_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_guild_welcome_screen(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuildWelcomeScreenResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildWelcomeScreenResponse
            200 response for get_guild_welcome_screen

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_welcome_screen(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_welcome_screen(guild_id, request_options=request_options)
        return _response.data

    async def update_guild_welcome_screen(
        self,
        guild_id: SnowflakeType,
        *,
        description: typing.Optional[str] = OMIT,
        welcome_channels: typing.Optional[typing.Sequence[GuildWelcomeChannel]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildWelcomeScreenResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        description : typing.Optional[str]

        welcome_channels : typing.Optional[typing.Sequence[GuildWelcomeChannel]]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildWelcomeScreenResponse
            200 response for update_guild_welcome_screen

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_guild_welcome_screen(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_guild_welcome_screen(
            guild_id,
            description=description,
            welcome_channels=welcome_channels,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    async def get_voice_state(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VoiceStateResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VoiceStateResponse
            200 response for get_voice_state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_voice_state(
                guild_id="guild_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_voice_state(guild_id, user_id, request_options=request_options)
        return _response.data

    async def update_voice_state(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        suppress: typing.Optional[bool] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        suppress : typing.Optional[bool]

        channel_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_voice_state(
                guild_id="guild_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_voice_state(
            guild_id, user_id, suppress=suppress, channel_id=channel_id, request_options=request_options
        )
        return _response.data

    async def delete_guild_integration(
        self,
        guild_id: SnowflakeType,
        integration_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        integration_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_guild_integration(
                guild_id="guild_id",
                integration_id="integration_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_guild_integration(
            guild_id, integration_id, request_options=request_options
        )
        return _response.data

    async def list_guild_integrations(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ListGuildIntegrationsResponseItem]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ListGuildIntegrationsResponseItem]]
            200 response for list_guild_integrations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_integrations(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_integrations(guild_id, request_options=request_options)
        return _response.data

    async def get_guild_widget(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WidgetResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WidgetResponse
            200 response for get_guild_widget

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_widget(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_widget(guild_id, request_options=request_options)
        return _response.data

    async def get_guilds_onboarding(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserGuildOnboardingResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserGuildOnboardingResponse
            200 response for get_guilds_onboarding

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guilds_onboarding(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guilds_onboarding(guild_id, request_options=request_options)
        return _response.data

    async def put_guilds_onboarding(
        self,
        guild_id: SnowflakeType,
        *,
        prompts: typing.Optional[typing.Sequence[UpdateOnboardingPromptRequest]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        default_channel_ids: typing.Optional[typing.Sequence[SnowflakeType]] = OMIT,
        mode: typing.Optional[GuildOnboardingMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildOnboardingResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        prompts : typing.Optional[typing.Sequence[UpdateOnboardingPromptRequest]]

        enabled : typing.Optional[bool]

        default_channel_ids : typing.Optional[typing.Sequence[SnowflakeType]]

        mode : typing.Optional[GuildOnboardingMode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildOnboardingResponse
            200 response for put_guilds_onboarding

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.put_guilds_onboarding(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_guilds_onboarding(
            guild_id,
            prompts=prompts,
            enabled=enabled,
            default_channel_ids=default_channel_ids,
            mode=mode,
            request_options=request_options,
        )
        return _response.data

    async def get_guild_vanity_url(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> VanityUrlResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VanityUrlResponse
            200 response for get_guild_vanity_url

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_vanity_url(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_vanity_url(guild_id, request_options=request_options)
        return _response.data

    async def list_guild_audit_log_entries(
        self,
        guild_id: SnowflakeType,
        *,
        user_id: typing.Optional[SnowflakeType] = None,
        target_id: typing.Optional[SnowflakeType] = None,
        action_type: typing.Optional[int] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildAuditLogResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : typing.Optional[SnowflakeType]

        target_id : typing.Optional[SnowflakeType]

        action_type : typing.Optional[int]

        before : typing.Optional[SnowflakeType]

        after : typing.Optional[SnowflakeType]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildAuditLogResponse
            200 response for list_guild_audit_log_entries

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_audit_log_entries(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_audit_log_entries(
            guild_id,
            user_id=user_id,
            target_id=target_id,
            action_type=action_type,
            before=before,
            after=after,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def get_guild_widget_png(
        self,
        guild_id: SnowflakeType,
        *,
        style: typing.Optional[WidgetImageStyles] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        style : typing.Optional[WidgetImageStyles]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            200 response for get_guild_widget_png
        """
        async with self._raw_client.get_guild_widget_png(guild_id, style=style, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def sync_guild_template(
        self, guild_id: SnowflakeType, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuildTemplateResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildTemplateResponse
            200 response for sync_guild_template

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.sync_guild_template(
                guild_id="guild_id",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sync_guild_template(guild_id, code, request_options=request_options)
        return _response.data

    async def delete_guild_template(
        self, guild_id: SnowflakeType, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuildTemplateResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildTemplateResponse
            200 response for delete_guild_template

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_guild_template(
                guild_id="guild_id",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_guild_template(guild_id, code, request_options=request_options)
        return _response.data

    async def update_guild_template(
        self,
        guild_id: SnowflakeType,
        code: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildTemplateResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        code : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildTemplateResponse
            200 response for update_guild_template

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_guild_template(
                guild_id="guild_id",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_guild_template(
            guild_id, code, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def list_guild_templates(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[GuildTemplateResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[GuildTemplateResponse]]
            200 response for list_guild_templates

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_templates(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_templates(guild_id, request_options=request_options)
        return _response.data

    async def create_guild_template(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildTemplateResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildTemplateResponse
            200 response for create_guild_template

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_guild_template(
                guild_id="guild_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_guild_template(
            guild_id, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def get_guild_sticker(
        self,
        guild_id: SnowflakeType,
        sticker_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildStickerResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sticker_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildStickerResponse
            200 response for get_guild_sticker

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_sticker(
                guild_id="guild_id",
                sticker_id="sticker_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_sticker(guild_id, sticker_id, request_options=request_options)
        return _response.data

    async def delete_guild_sticker(
        self,
        guild_id: SnowflakeType,
        sticker_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sticker_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_guild_sticker(
                guild_id="guild_id",
                sticker_id="sticker_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_guild_sticker(guild_id, sticker_id, request_options=request_options)
        return _response.data

    async def update_guild_sticker(
        self,
        guild_id: SnowflakeType,
        sticker_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildStickerResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sticker_id : SnowflakeType

        name : typing.Optional[str]

        tags : typing.Optional[str]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildStickerResponse
            200 response for update_guild_sticker

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_guild_sticker(
                guild_id="guild_id",
                sticker_id="sticker_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_guild_sticker(
            guild_id, sticker_id, name=name, tags=tags, description=description, request_options=request_options
        )
        return _response.data

    async def bulk_ban_users_from_guild(
        self,
        guild_id: SnowflakeType,
        *,
        user_ids: typing.Sequence[SnowflakeType],
        delete_message_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BulkBanUsersResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_ids : typing.Sequence[SnowflakeType]

        delete_message_seconds : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BulkBanUsersResponse
            200 response for bulk_ban_users_from_guild

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.bulk_ban_users_from_guild(
                guild_id="guild_id",
                user_ids=["user_ids"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_ban_users_from_guild(
            guild_id, user_ids=user_ids, delete_message_seconds=delete_message_seconds, request_options=request_options
        )
        return _response.data

    async def list_guild_stickers(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GuildStickerResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GuildStickerResponse]
            200 response for list_guild_stickers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_stickers(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_stickers(guild_id, request_options=request_options)
        return _response.data

    async def create_guild_sticker(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        tags: str,
        file: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildStickerResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : str

        tags : str

        file : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildStickerResponse
            201 response for create_guild_sticker

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_guild_sticker(
                guild_id="guild_id",
                name="name",
                tags="tags",
                file="file",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_guild_sticker(
            guild_id, name=name, tags=tags, file=file, description=description, request_options=request_options
        )
        return _response.data

    async def get_guild_webhooks(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[GetGuildWebhooksResponseItem]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[GetGuildWebhooksResponseItem]]
            200 response for get_guild_webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_webhooks(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_webhooks(guild_id, request_options=request_options)
        return _response.data

    async def list_guild_channels(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ListGuildChannelsResponseItem]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ListGuildChannelsResponseItem]]
            200 response for list_guild_channels

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_channels(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_channels(guild_id, request_options=request_options)
        return _response.data

    async def create_guild_channel(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        type: typing.Optional[int] = OMIT,
        position: typing.Optional[int] = OMIT,
        topic: typing.Optional[str] = OMIT,
        bitrate: typing.Optional[int] = OMIT,
        user_limit: typing.Optional[int] = OMIT,
        nsfw: typing.Optional[bool] = OMIT,
        rate_limit_per_user: typing.Optional[int] = OMIT,
        parent_id: typing.Optional[SnowflakeType] = OMIT,
        permission_overwrites: typing.Optional[typing.Sequence[ChannelPermissionOverwriteRequest]] = OMIT,
        rtc_region: typing.Optional[str] = OMIT,
        video_quality_mode: typing.Optional[VideoQualityModes] = OMIT,
        default_auto_archive_duration: typing.Optional[ThreadAutoArchiveDuration] = OMIT,
        default_reaction_emoji: typing.Optional[UpdateDefaultReactionEmojiRequest] = OMIT,
        default_thread_rate_limit_per_user: typing.Optional[int] = OMIT,
        default_sort_order: typing.Optional[ThreadSortOrder] = OMIT,
        default_forum_layout: typing.Optional[ForumLayout] = OMIT,
        available_tags: typing.Optional[typing.Sequence[typing.Optional[CreateOrUpdateThreadTagRequest]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildChannelResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : str

        type : typing.Optional[int]

        position : typing.Optional[int]

        topic : typing.Optional[str]

        bitrate : typing.Optional[int]

        user_limit : typing.Optional[int]

        nsfw : typing.Optional[bool]

        rate_limit_per_user : typing.Optional[int]

        parent_id : typing.Optional[SnowflakeType]

        permission_overwrites : typing.Optional[typing.Sequence[ChannelPermissionOverwriteRequest]]

        rtc_region : typing.Optional[str]

        video_quality_mode : typing.Optional[VideoQualityModes]

        default_auto_archive_duration : typing.Optional[ThreadAutoArchiveDuration]

        default_reaction_emoji : typing.Optional[UpdateDefaultReactionEmojiRequest]

        default_thread_rate_limit_per_user : typing.Optional[int]

        default_sort_order : typing.Optional[ThreadSortOrder]

        default_forum_layout : typing.Optional[ForumLayout]

        available_tags : typing.Optional[typing.Sequence[typing.Optional[CreateOrUpdateThreadTagRequest]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildChannelResponse
            201 response for create_guild_channel

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_guild_channel(
                guild_id="guild_id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_guild_channel(
            guild_id,
            name=name,
            type=type,
            position=position,
            topic=topic,
            bitrate=bitrate,
            user_limit=user_limit,
            nsfw=nsfw,
            rate_limit_per_user=rate_limit_per_user,
            parent_id=parent_id,
            permission_overwrites=permission_overwrites,
            rtc_region=rtc_region,
            video_quality_mode=video_quality_mode,
            default_auto_archive_duration=default_auto_archive_duration,
            default_reaction_emoji=default_reaction_emoji,
            default_thread_rate_limit_per_user=default_thread_rate_limit_per_user,
            default_sort_order=default_sort_order,
            default_forum_layout=default_forum_layout,
            available_tags=available_tags,
            request_options=request_options,
        )
        return _response.data

    async def bulk_update_guild_channels(
        self,
        guild_id: SnowflakeType,
        *,
        request: typing.Sequence[BulkUpdateGuildChannelsRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : typing.Sequence[BulkUpdateGuildChannelsRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BulkUpdateGuildChannelsRequestBodyItem

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.bulk_update_guild_channels(
                guild_id="guild_id",
                request=[BulkUpdateGuildChannelsRequestBodyItem()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_update_guild_channels(
            guild_id, request=request, request_options=request_options
        )
        return _response.data

    async def get_guild_member(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildMemberResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildMemberResponse
            200 response for get_guild_member

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_member(
                guild_id="guild_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_member(guild_id, user_id, request_options=request_options)
        return _response.data

    async def add_guild_member(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        access_token: str,
        nick: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]] = OMIT,
        mute: typing.Optional[bool] = OMIT,
        deaf: typing.Optional[bool] = OMIT,
        flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[GuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        access_token : str

        nick : typing.Optional[str]

        roles : typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]]

        mute : typing.Optional[bool]

        deaf : typing.Optional[bool]

        flags : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[GuildMemberResponse]
            201 response for add_guild_member

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.add_guild_member(
                guild_id="guild_id",
                user_id="user_id",
                access_token="access_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_guild_member(
            guild_id,
            user_id,
            access_token=access_token,
            nick=nick,
            roles=roles,
            mute=mute,
            deaf=deaf,
            flags=flags,
            request_options=request_options,
        )
        return _response.data

    async def delete_guild_member(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_guild_member(
                guild_id="guild_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_guild_member(guild_id, user_id, request_options=request_options)
        return _response.data

    async def update_guild_member(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        nick: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]] = OMIT,
        mute: typing.Optional[bool] = OMIT,
        deaf: typing.Optional[bool] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        communication_disabled_until: typing.Optional[dt.datetime] = OMIT,
        flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[GuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        nick : typing.Optional[str]

        roles : typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]]

        mute : typing.Optional[bool]

        deaf : typing.Optional[bool]

        channel_id : typing.Optional[SnowflakeType]

        communication_disabled_until : typing.Optional[dt.datetime]

        flags : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[GuildMemberResponse]
            200 response for update_guild_member

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_guild_member(
                guild_id="guild_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_guild_member(
            guild_id,
            user_id,
            nick=nick,
            roles=roles,
            mute=mute,
            deaf=deaf,
            channel_id=channel_id,
            communication_disabled_until=communication_disabled_until,
            flags=flags,
            request_options=request_options,
        )
        return _response.data

    async def list_guild_members(
        self,
        guild_id: SnowflakeType,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        limit : typing.Optional[int]

        after : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GuildMemberResponse]
            200 response for list_guild_members

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_members(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_members(
            guild_id, limit=limit, after=after, request_options=request_options
        )
        return _response.data

    async def get_guild_preview(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GuildPreviewResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildPreviewResponse
            200 response for get_guild_preview

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_preview(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_preview(guild_id, request_options=request_options)
        return _response.data

    async def list_guild_invites(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[ListGuildInvitesResponseItem]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[ListGuildInvitesResponseItem]]
            200 response for list_guild_invites

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_invites(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_invites(guild_id, request_options=request_options)
        return _response.data

    async def list_guild_voice_regions(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[VoiceRegionResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[VoiceRegionResponse]]
            200 response for list_guild_voice_regions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_voice_regions(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_voice_regions(guild_id, request_options=request_options)
        return _response.data

    async def get_guild_emoji(
        self,
        guild_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmojiResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmojiResponse
            200 response for get_guild_emoji

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_emoji(
                guild_id="guild_id",
                emoji_id="emoji_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_emoji(guild_id, emoji_id, request_options=request_options)
        return _response.data

    async def delete_guild_emoji(
        self,
        guild_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_guild_emoji(
                guild_id="guild_id",
                emoji_id="emoji_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_guild_emoji(guild_id, emoji_id, request_options=request_options)
        return _response.data

    async def update_guild_emoji(
        self,
        guild_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmojiResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        emoji_id : SnowflakeType

        name : typing.Optional[str]

        roles : typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmojiResponse
            200 response for update_guild_emoji

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_guild_emoji(
                guild_id="guild_id",
                emoji_id="emoji_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_guild_emoji(
            guild_id, emoji_id, name=name, roles=roles, request_options=request_options
        )
        return _response.data

    async def list_guild_emojis(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[typing.List[EmojiResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[EmojiResponse]]
            200 response for list_guild_emojis

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_emojis(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_emojis(guild_id, request_options=request_options)
        return _response.data

    async def create_guild_emoji(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        image: str,
        roles: typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmojiResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : str

        image : str

        roles : typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmojiResponse
            201 response for create_guild_emoji

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_guild_emoji(
                guild_id="guild_id",
                name="name",
                image="image",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_guild_emoji(
            guild_id, name=name, image=image, roles=roles, request_options=request_options
        )
        return _response.data

    async def get_guild_widget_settings(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WidgetSettingsResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WidgetSettingsResponse
            200 response for get_guild_widget_settings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_widget_settings(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_widget_settings(guild_id, request_options=request_options)
        return _response.data

    async def update_guild_widget_settings(
        self,
        guild_id: SnowflakeType,
        *,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WidgetSettingsResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        channel_id : typing.Optional[SnowflakeType]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WidgetSettingsResponse
            200 response for update_guild_widget_settings

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_guild_widget_settings(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_guild_widget_settings(
            guild_id, channel_id=channel_id, enabled=enabled, request_options=request_options
        )
        return _response.data

    async def get_guild_role(
        self,
        guild_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildRoleResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        role_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildRoleResponse
            200 response for get_guild_role

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_role(
                guild_id="guild_id",
                role_id="role_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_role(guild_id, role_id, request_options=request_options)
        return _response.data

    async def delete_guild_role(
        self,
        guild_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        role_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_guild_role(
                guild_id="guild_id",
                role_id="role_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_guild_role(guild_id, role_id, request_options=request_options)
        return _response.data

    async def update_guild_role(
        self,
        guild_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        permissions: typing.Optional[int] = OMIT,
        color: typing.Optional[int] = OMIT,
        hoist: typing.Optional[bool] = OMIT,
        mentionable: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        unicode_emoji: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildRoleResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        role_id : SnowflakeType

        name : typing.Optional[str]

        permissions : typing.Optional[int]

        color : typing.Optional[int]

        hoist : typing.Optional[bool]

        mentionable : typing.Optional[bool]

        icon : typing.Optional[str]

        unicode_emoji : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildRoleResponse
            200 response for update_guild_role

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_guild_role(
                guild_id="guild_id",
                role_id="role_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_guild_role(
            guild_id,
            role_id,
            name=name,
            permissions=permissions,
            color=color,
            hoist=hoist,
            mentionable=mentionable,
            icon=icon,
            unicode_emoji=unicode_emoji,
            request_options=request_options,
        )
        return _response.data

    async def list_guild_roles(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GuildRoleResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GuildRoleResponse]
            200 response for list_guild_roles

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_roles(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_roles(guild_id, request_options=request_options)
        return _response.data

    async def create_guild_role(
        self,
        guild_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        permissions: typing.Optional[int] = OMIT,
        color: typing.Optional[int] = OMIT,
        hoist: typing.Optional[bool] = OMIT,
        mentionable: typing.Optional[bool] = OMIT,
        icon: typing.Optional[str] = OMIT,
        unicode_emoji: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildRoleResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : typing.Optional[str]

        permissions : typing.Optional[int]

        color : typing.Optional[int]

        hoist : typing.Optional[bool]

        mentionable : typing.Optional[bool]

        icon : typing.Optional[str]

        unicode_emoji : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildRoleResponse
            200 response for create_guild_role

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.create_guild_role(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_guild_role(
            guild_id,
            name=name,
            permissions=permissions,
            color=color,
            hoist=hoist,
            mentionable=mentionable,
            icon=icon,
            unicode_emoji=unicode_emoji,
            request_options=request_options,
        )
        return _response.data

    async def bulk_update_guild_roles(
        self,
        guild_id: SnowflakeType,
        *,
        request: typing.Sequence[BulkUpdateGuildRolesRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GuildRoleResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : typing.Sequence[BulkUpdateGuildRolesRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GuildRoleResponse]
            200 response for bulk_update_guild_roles

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BulkUpdateGuildRolesRequestBodyItem

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.bulk_update_guild_roles(
                guild_id="guild_id",
                request=[BulkUpdateGuildRolesRequestBodyItem()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_update_guild_roles(
            guild_id, request=request, request_options=request_options
        )
        return _response.data

    async def preview_prune_guild(
        self,
        guild_id: SnowflakeType,
        *,
        days: typing.Optional[int] = None,
        include_roles: typing.Optional[PreviewPruneGuildRequestIncludeRoles] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildPruneResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        days : typing.Optional[int]

        include_roles : typing.Optional[PreviewPruneGuildRequestIncludeRoles]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildPruneResponse
            200 response for preview_prune_guild

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.preview_prune_guild(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_prune_guild(
            guild_id, days=days, include_roles=include_roles, request_options=request_options
        )
        return _response.data

    async def prune_guild(
        self,
        guild_id: SnowflakeType,
        *,
        days: typing.Optional[int] = OMIT,
        compute_prune_count: typing.Optional[bool] = OMIT,
        include_roles: typing.Optional[PruneGuildRequestIncludeRoles] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildPruneResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        days : typing.Optional[int]

        compute_prune_count : typing.Optional[bool]

        include_roles : typing.Optional[PruneGuildRequestIncludeRoles]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildPruneResponse
            200 response for prune_guild

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.prune_guild(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.prune_guild(
            guild_id,
            days=days,
            compute_prune_count=compute_prune_count,
            include_roles=include_roles,
            request_options=request_options,
        )
        return _response.data

    async def get_guild_ban(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildBanResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildBanResponse
            200 response for get_guild_ban

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild_ban(
                guild_id="guild_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild_ban(guild_id, user_id, request_options=request_options)
        return _response.data

    async def ban_user_from_guild(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        delete_message_seconds: typing.Optional[int] = OMIT,
        delete_message_days: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        delete_message_seconds : typing.Optional[int]

        delete_message_days : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.ban_user_from_guild(
                guild_id="guild_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ban_user_from_guild(
            guild_id,
            user_id,
            delete_message_seconds=delete_message_seconds,
            delete_message_days=delete_message_days,
            request_options=request_options,
        )
        return _response.data

    async def unban_user_from_guild(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.unban_user_from_guild(
                guild_id="guild_id",
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unban_user_from_guild(guild_id, user_id, request_options=request_options)
        return _response.data

    async def list_guild_bans(
        self,
        guild_id: SnowflakeType,
        *,
        limit: typing.Optional[int] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[typing.List[GuildBanResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        limit : typing.Optional[int]

        before : typing.Optional[SnowflakeType]

        after : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[typing.List[GuildBanResponse]]
            200 response for list_guild_bans

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.list_guild_bans(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_guild_bans(
            guild_id, limit=limit, before=before, after=after, request_options=request_options
        )
        return _response.data

    async def set_guild_mfa_level(
        self, guild_id: SnowflakeType, *, level: GuildMfaLevel, request_options: typing.Optional[RequestOptions] = None
    ) -> GuildMfaLevelResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        level : GuildMfaLevel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildMfaLevelResponse
            200 response for set_guild_mfa_level

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.set_guild_mfa_level(
                guild_id="guild_id",
                level=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_guild_mfa_level(guild_id, level=level, request_options=request_options)
        return _response.data

    async def get_stage_instance(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StageInstanceResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StageInstanceResponse
            200 response for get_stage_instance

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_stage_instance(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_stage_instance(channel_id, request_options=request_options)
        return _response.data

    async def delete_stage_instance(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_stage_instance(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_stage_instance(channel_id, request_options=request_options)
        return _response.data

    async def update_stage_instance(
        self,
        channel_id: SnowflakeType,
        *,
        topic: typing.Optional[str] = OMIT,
        privacy_level: typing.Optional[StageInstancesPrivacyLevels] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StageInstanceResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        topic : typing.Optional[str]

        privacy_level : typing.Optional[StageInstancesPrivacyLevels]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StageInstanceResponse
            200 response for update_stage_instance

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_stage_instance(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_stage_instance(
            channel_id, topic=topic, privacy_level=privacy_level, request_options=request_options
        )
        return _response.data

    async def get_sticker_pack(
        self, pack_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StickerPackResponse:
        """
        Parameters
        ----------
        pack_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StickerPackResponse
            200 response for get_sticker_pack

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_sticker_pack(
                pack_id="pack_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sticker_pack(pack_id, request_options=request_options)
        return _response.data

    async def get_application(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PrivateApplicationResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateApplicationResponse
            200 response for get_application

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_application(
                application_id="application_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_application(application_id, request_options=request_options)
        return _response.data

    async def update_application(
        self,
        application_id: SnowflakeType,
        *,
        description: typing.Optional[ApplicationFormPartialDescription] = OMIT,
        icon: typing.Optional[str] = OMIT,
        cover_image: typing.Optional[str] = OMIT,
        team_id: typing.Optional[SnowflakeType] = OMIT,
        flags: typing.Optional[int] = OMIT,
        interactions_endpoint_url: typing.Optional[str] = OMIT,
        explicit_content_filter: typing.Optional[ApplicationExplicitContentFilterTypes] = OMIT,
        max_participants: typing.Optional[int] = OMIT,
        type: typing.Optional[ApplicationTypes] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        custom_install_url: typing.Optional[str] = OMIT,
        install_params: typing.Optional[ApplicationOAuth2InstallParams] = OMIT,
        role_connections_verification_url: typing.Optional[str] = OMIT,
        integration_types_config: typing.Optional[
            typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PrivateApplicationResponse:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        description : typing.Optional[ApplicationFormPartialDescription]

        icon : typing.Optional[str]

        cover_image : typing.Optional[str]

        team_id : typing.Optional[SnowflakeType]

        flags : typing.Optional[int]

        interactions_endpoint_url : typing.Optional[str]

        explicit_content_filter : typing.Optional[ApplicationExplicitContentFilterTypes]

        max_participants : typing.Optional[int]

        type : typing.Optional[ApplicationTypes]

        tags : typing.Optional[typing.Sequence[str]]

        custom_install_url : typing.Optional[str]

        install_params : typing.Optional[ApplicationOAuth2InstallParams]

        role_connections_verification_url : typing.Optional[str]

        integration_types_config : typing.Optional[typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PrivateApplicationResponse
            200 response for update_application

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_application(
                application_id="application_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_application(
            application_id,
            description=description,
            icon=icon,
            cover_image=cover_image,
            team_id=team_id,
            flags=flags,
            interactions_endpoint_url=interactions_endpoint_url,
            explicit_content_filter=explicit_content_filter,
            max_participants=max_participants,
            type=type,
            tags=tags,
            custom_install_url=custom_install_url,
            install_params=install_params,
            role_connections_verification_url=role_connections_verification_url,
            integration_types_config=integration_types_config,
            request_options=request_options,
        )
        return _response.data

    async def get_webhook_by_token(
        self, webhook_id: SnowflakeType, webhook_token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhookByTokenResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhookByTokenResponse
            200 response for get_webhook_by_token

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_webhook_by_token(
                webhook_id="webhook_id",
                webhook_token="webhook_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhook_by_token(
            webhook_id, webhook_token, request_options=request_options
        )
        return _response.data

    async def execute_webhook(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        request: ExecuteWebhookRequestBody,
        wait: typing.Optional[bool] = None,
        thread_id: typing.Optional[SnowflakeType] = None,
        with_components: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[MessageResponse]:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        request : ExecuteWebhookRequestBody

        wait : typing.Optional[bool]

        thread_id : typing.Optional[SnowflakeType]

        with_components : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[MessageResponse]
            200 response for execute_webhook

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, IncomingWebhookRequestPartial

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.execute_webhook(
                webhook_id="webhook_id",
                webhook_token="webhook_token",
                request=IncomingWebhookRequestPartial(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_webhook(
            webhook_id,
            webhook_token,
            request=request,
            wait=wait,
            thread_id=thread_id,
            with_components=with_components,
            request_options=request_options,
        )
        return _response.data

    async def delete_webhook_by_token(
        self, webhook_id: SnowflakeType, webhook_token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_webhook_by_token(
                webhook_id="webhook_id",
                webhook_token="webhook_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_webhook_by_token(
            webhook_id, webhook_token, request_options=request_options
        )
        return _response.data

    async def update_webhook_by_token(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        name: typing.Optional[str] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhookByTokenResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        name : typing.Optional[str]

        avatar : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhookByTokenResponse
            200 response for update_webhook_by_token

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_webhook_by_token(
                webhook_id="webhook_id",
                webhook_token="webhook_token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_webhook_by_token(
            webhook_id, webhook_token, name=name, avatar=avatar, request_options=request_options
        )
        return _response.data

    async def get_sticker(
        self, sticker_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetStickerResponse:
        """
        Parameters
        ----------
        sticker_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetStickerResponse
            200 response for get_sticker

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_sticker(
                sticker_id="sticker_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sticker(sticker_id, request_options=request_options)
        return _response.data

    async def get_webhook(
        self, webhook_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhookResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhookResponse
            200 response for get_webhook

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_webhook(
                webhook_id="webhook_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhook(webhook_id, request_options=request_options)
        return _response.data

    async def delete_webhook(
        self, webhook_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_webhook(
                webhook_id="webhook_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_webhook(webhook_id, request_options=request_options)
        return _response.data

    async def update_webhook(
        self,
        webhook_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhookResponse:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        name : typing.Optional[str]

        avatar : typing.Optional[str]

        channel_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhookResponse
            200 response for update_webhook

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_webhook(
                webhook_id="webhook_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_webhook(
            webhook_id, name=name, avatar=avatar, channel_id=channel_id, request_options=request_options
        )
        return _response.data

    async def get_channel(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetChannelResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetChannelResponse
            200 response for get_channel

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_channel(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_channel(channel_id, request_options=request_options)
        return _response.data

    async def delete_channel(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteChannelResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteChannelResponse
            200 response for delete_channel

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_channel(
                channel_id="channel_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_channel(channel_id, request_options=request_options)
        return _response.data

    async def update_channel(
        self,
        channel_id: SnowflakeType,
        *,
        request: UpdateChannelRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateChannelResponse:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request : UpdateChannelRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateChannelResponse
            200 response for update_channel

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UpdateDmRequestPartial

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_channel(
                channel_id="channel_id",
                request=UpdateDmRequestPartial(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_channel(channel_id, request=request, request_options=request_options)
        return _response.data

    async def invite_resolve(
        self,
        code: str,
        *,
        with_counts: typing.Optional[bool] = None,
        guild_scheduled_event_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InviteResolveResponse:
        """
        Parameters
        ----------
        code : str

        with_counts : typing.Optional[bool]

        guild_scheduled_event_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteResolveResponse
            200 response for invite_resolve

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.invite_resolve(
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invite_resolve(
            code,
            with_counts=with_counts,
            guild_scheduled_event_id=guild_scheduled_event_id,
            request_options=request_options,
        )
        return _response.data

    async def invite_revoke(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> InviteRevokeResponse:
        """
        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteRevokeResponse
            200 response for invite_revoke

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.invite_revoke(
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invite_revoke(code, request_options=request_options)
        return _response.data

    async def get_lobby(
        self, lobby_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> LobbyResponse:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyResponse
            200 response for get_lobby

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_lobby(
                lobby_id="lobby_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lobby(lobby_id, request_options=request_options)
        return _response.data

    async def edit_lobby(
        self,
        lobby_id: SnowflakeType,
        *,
        idle_timeout_seconds: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        members: typing.Optional[typing.Sequence[LobbyMemberRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LobbyResponse:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        idle_timeout_seconds : typing.Optional[int]

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        members : typing.Optional[typing.Sequence[LobbyMemberRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LobbyResponse
            200 response for edit_lobby

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.edit_lobby(
                lobby_id="lobby_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.edit_lobby(
            lobby_id,
            idle_timeout_seconds=idle_timeout_seconds,
            metadata=metadata,
            members=members,
            request_options=request_options,
        )
        return _response.data

    async def get_guild(
        self,
        guild_id: SnowflakeType,
        *,
        with_counts: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildWithCountsResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        with_counts : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildWithCountsResponse
            200 response for get_guild

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_guild(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_guild(guild_id, with_counts=with_counts, request_options=request_options)
        return _response.data

    async def delete_guild(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.delete_guild(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_guild(guild_id, request_options=request_options)
        return _response.data

    async def update_guild(
        self,
        guild_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        verification_level: typing.Optional[VerificationLevels] = OMIT,
        default_message_notifications: typing.Optional[UserNotificationSettings] = OMIT,
        explicit_content_filter: typing.Optional[GuildExplicitContentFilterTypes] = OMIT,
        preferred_locale: typing.Optional[AvailableLocalesEnum] = OMIT,
        afk_timeout: typing.Optional[AfkTimeouts] = OMIT,
        afk_channel_id: typing.Optional[SnowflakeType] = OMIT,
        system_channel_id: typing.Optional[SnowflakeType] = OMIT,
        owner_id: typing.Optional[SnowflakeType] = OMIT,
        splash: typing.Optional[str] = OMIT,
        banner: typing.Optional[str] = OMIT,
        system_channel_flags: typing.Optional[int] = OMIT,
        features: typing.Optional[typing.Sequence[typing.Optional[str]]] = OMIT,
        discovery_splash: typing.Optional[str] = OMIT,
        home_header: typing.Optional[str] = OMIT,
        rules_channel_id: typing.Optional[SnowflakeType] = OMIT,
        safety_alerts_channel_id: typing.Optional[SnowflakeType] = OMIT,
        public_updates_channel_id: typing.Optional[SnowflakeType] = OMIT,
        premium_progress_bar_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GuildResponse:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        name : typing.Optional[str]

        description : typing.Optional[str]

        region : typing.Optional[str]

        icon : typing.Optional[str]

        verification_level : typing.Optional[VerificationLevels]

        default_message_notifications : typing.Optional[UserNotificationSettings]

        explicit_content_filter : typing.Optional[GuildExplicitContentFilterTypes]

        preferred_locale : typing.Optional[AvailableLocalesEnum]

        afk_timeout : typing.Optional[AfkTimeouts]

        afk_channel_id : typing.Optional[SnowflakeType]

        system_channel_id : typing.Optional[SnowflakeType]

        owner_id : typing.Optional[SnowflakeType]

        splash : typing.Optional[str]

        banner : typing.Optional[str]

        system_channel_flags : typing.Optional[int]

        features : typing.Optional[typing.Sequence[typing.Optional[str]]]

        discovery_splash : typing.Optional[str]

        home_header : typing.Optional[str]

        rules_channel_id : typing.Optional[SnowflakeType]

        safety_alerts_channel_id : typing.Optional[SnowflakeType]

        public_updates_channel_id : typing.Optional[SnowflakeType]

        premium_progress_bar_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GuildResponse
            200 response for update_guild

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.update_guild(
                guild_id="guild_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_guild(
            guild_id,
            name=name,
            description=description,
            region=region,
            icon=icon,
            verification_level=verification_level,
            default_message_notifications=default_message_notifications,
            explicit_content_filter=explicit_content_filter,
            preferred_locale=preferred_locale,
            afk_timeout=afk_timeout,
            afk_channel_id=afk_channel_id,
            system_channel_id=system_channel_id,
            owner_id=owner_id,
            splash=splash,
            banner=banner,
            system_channel_flags=system_channel_flags,
            features=features,
            discovery_splash=discovery_splash,
            home_header=home_header,
            rules_channel_id=rules_channel_id,
            safety_alerts_channel_id=safety_alerts_channel_id,
            public_updates_channel_id=public_updates_channel_id,
            premium_progress_bar_enabled=premium_progress_bar_enabled,
            request_options=request_options,
        )
        return _response.data

    async def get_user(
        self, user_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UserResponse:
        """
        Parameters
        ----------
        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UserResponse
            200 response for get_user

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.get_user(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_user(user_id, request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
