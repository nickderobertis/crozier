

import contextlib
import datetime as dt
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.datetime_utils import serialize_datetime
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def partner_sdk_unmerge_provisional_account(
        self,
        *,
        client_id: SnowflakeType,
        external_auth_token: str,
        external_auth_type: ApplicationIdentityProviderAuthType,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "partner-sdk/provisional-accounts/unmerge",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "external_auth_token": external_auth_token,
                "external_auth_type": external_auth_type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_my_oauth2application(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PrivateApplicationResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PrivateApplicationResponse]
            200 response for get_my_oauth2_application
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth2/applications/@me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateApplicationResponse,
                    parse_obj_as(
                        type_=PrivateApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_my_connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[ConnectedAccountResponse]]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[ConnectedAccountResponse]]]
            200 response for list_my_connections
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/@me/connections",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ConnectedAccountResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ConnectedAccountResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_dm(
        self,
        *,
        recipient_id: typing.Optional[SnowflakeType] = OMIT,
        access_tokens: typing.Optional[typing.Sequence[str]] = OMIT,
        nicks: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDmResponse]:
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
        HttpResponse[CreateDmResponse]
            200 response for create_dm
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/@me/channels",
            method="POST",
            json={
                "recipient_id": recipient_id,
                "access_tokens": access_tokens,
                "nicks": nicks,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDmResponse,
                    parse_obj_as(
                        type_=CreateDmResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_my_guilds(
        self,
        *,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        with_counts: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[MyGuildResponse]]]:
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
        HttpResponse[typing.Optional[typing.List[MyGuildResponse]]]
            200 response for list_my_guilds
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/@me/guilds",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "with_counts": with_counts,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[MyGuildResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[MyGuildResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_my_application(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PrivateApplicationResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PrivateApplicationResponse]
            200 response for get_my_application
        """
        _response = self._client_wrapper.httpx_client.request(
            "applications/@me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateApplicationResponse,
                    parse_obj_as(
                        type_=PrivateApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[PrivateApplicationResponse]:
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
        HttpResponse[PrivateApplicationResponse]
            200 response for update_my_application
        """
        _response = self._client_wrapper.httpx_client.request(
            "applications/@me",
            method="PATCH",
            json={
                "description": convert_and_respect_annotation_metadata(
                    object_=description,
                    annotation=typing.Optional[ApplicationFormPartialDescription],
                    direction="write",
                ),
                "icon": icon,
                "cover_image": cover_image,
                "team_id": team_id,
                "flags": flags,
                "interactions_endpoint_url": interactions_endpoint_url,
                "explicit_content_filter": explicit_content_filter,
                "max_participants": max_participants,
                "type": type,
                "tags": tags,
                "custom_install_url": custom_install_url,
                "install_params": convert_and_respect_annotation_metadata(
                    object_=install_params,
                    annotation=typing.Optional[ApplicationOAuth2InstallParams],
                    direction="write",
                ),
                "role_connections_verification_url": role_connections_verification_url,
                "integration_types_config": convert_and_respect_annotation_metadata(
                    object_=integration_types_config,
                    annotation=typing.Optional[
                        typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]
                    ],
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateApplicationResponse,
                    parse_obj_as(
                        type_=PrivateApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def partner_sdk_token(
        self,
        *,
        client_id: SnowflakeType,
        external_auth_token: str,
        external_auth_type: ApplicationIdentityProviderAuthType,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProvisionalTokenResponse]:
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
        HttpResponse[ProvisionalTokenResponse]
            200 response for partner_sdk_token
        """
        _response = self._client_wrapper.httpx_client.request(
            "partner-sdk/token",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "external_auth_token": external_auth_token,
                "external_auth_type": external_auth_type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisionalTokenResponse,
                    parse_obj_as(
                        type_=ProvisionalTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_bot_gateway(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GatewayBotResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GatewayBotResponse]
            200 response for get_bot_gateway
        """
        _response = self._client_wrapper.httpx_client.request(
            "gateway/bot",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GatewayBotResponse,
                    parse_obj_as(
                        type_=GatewayBotResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_openid_connect_userinfo(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OAuth2GetOpenIdConnectUserInfoResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OAuth2GetOpenIdConnectUserInfoResponse]
            200 response for get_openid_connect_userinfo
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth2/userinfo",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OAuth2GetOpenIdConnectUserInfoResponse,
                    parse_obj_as(
                        type_=OAuth2GetOpenIdConnectUserInfoResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_public_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OAuth2GetKeys]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OAuth2GetKeys]
            200 response for get_public_keys
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth2/keys",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OAuth2GetKeys,
                    parse_obj_as(
                        type_=OAuth2GetKeys,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_my_oauth2authorization(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OAuth2GetAuthorizationResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OAuth2GetAuthorizationResponse]
            200 response for get_my_oauth2_authorization
        """
        _response = self._client_wrapper.httpx_client.request(
            "oauth2/@me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OAuth2GetAuthorizationResponse,
                    parse_obj_as(
                        type_=OAuth2GetAuthorizationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_voice_regions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[VoiceRegionResponse]]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[VoiceRegionResponse]]]
            200 response for list_voice_regions
        """
        _response = self._client_wrapper.httpx_client.request(
            "voice/regions",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[VoiceRegionResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[VoiceRegionResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_my_user(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[UserPiiResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserPiiResponse]
            200 response for get_my_user
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/@me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserPiiResponse,
                    parse_obj_as(
                        type_=UserPiiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_my_user(
        self,
        *,
        username: str,
        avatar: typing.Optional[str] = OMIT,
        banner: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserPiiResponse]:
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
        HttpResponse[UserPiiResponse]
            200 response for update_my_user
        """
        _response = self._client_wrapper.httpx_client.request(
            "users/@me",
            method="PATCH",
            json={
                "username": username,
                "avatar": avatar,
                "banner": banner,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserPiiResponse,
                    parse_obj_as(
                        type_=UserPiiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_soundboard_default_sounds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[SoundboardSoundResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[SoundboardSoundResponse]]
            200 response for get_soundboard_default_sounds
        """
        _response = self._client_wrapper.httpx_client.request(
            "soundboard-default-sounds",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SoundboardSoundResponse],
                    parse_obj_as(
                        type_=typing.List[SoundboardSoundResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_stage_instance(
        self,
        *,
        topic: str,
        channel_id: SnowflakeType,
        privacy_level: typing.Optional[StageInstancesPrivacyLevels] = OMIT,
        guild_scheduled_event_id: typing.Optional[SnowflakeType] = OMIT,
        send_start_notification: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StageInstanceResponse]:
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
        HttpResponse[StageInstanceResponse]
            200 response for create_stage_instance
        """
        _response = self._client_wrapper.httpx_client.request(
            "stage-instances",
            method="POST",
            json={
                "topic": topic,
                "channel_id": channel_id,
                "privacy_level": privacy_level,
                "guild_scheduled_event_id": guild_scheduled_event_id,
                "send_start_notification": send_start_notification,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StageInstanceResponse,
                    parse_obj_as(
                        type_=StageInstanceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_sticker_packs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StickerPackCollectionResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StickerPackCollectionResponse]
            200 response for list_sticker_packs
        """
        _response = self._client_wrapper.httpx_client.request(
            "sticker-packs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StickerPackCollectionResponse,
                    parse_obj_as(
                        type_=StickerPackCollectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_gateway(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[GatewayResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GatewayResponse]
            200 response for get_gateway
        """
        _response = self._client_wrapper.httpx_client.request(
            "gateway",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GatewayResponse,
                    parse_obj_as(
                        type_=GatewayResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_lobby(
        self,
        *,
        idle_timeout_seconds: typing.Optional[int] = OMIT,
        members: typing.Optional[typing.Sequence[LobbyMemberRequest]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LobbyResponse]:
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
        HttpResponse[LobbyResponse]
            201 response for create_lobby
        """
        _response = self._client_wrapper.httpx_client.request(
            "lobbies",
            method="POST",
            json={
                "idle_timeout_seconds": idle_timeout_seconds,
                "members": convert_and_respect_annotation_metadata(
                    object_=members, annotation=typing.Optional[typing.Sequence[LobbyMemberRequest]], direction="write"
                ),
                "metadata": metadata,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyResponse,
                    parse_obj_as(
                        type_=LobbyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_or_join_lobby(
        self,
        *,
        secret: str,
        idle_timeout_seconds: typing.Optional[int] = OMIT,
        lobby_metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        member_metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LobbyResponse]:
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
        HttpResponse[LobbyResponse]
            200 response for create_or_join_lobby
        """
        _response = self._client_wrapper.httpx_client.request(
            "lobbies",
            method="PUT",
            json={
                "idle_timeout_seconds": idle_timeout_seconds,
                "lobby_metadata": lobby_metadata,
                "member_metadata": member_metadata,
                "secret": secret,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyResponse,
                    parse_obj_as(
                        type_=LobbyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[GuildResponse]:
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
        HttpResponse[GuildResponse]
            201 response for create_guild
        """
        _response = self._client_wrapper.httpx_client.request(
            "guilds",
            method="POST",
            json={
                "description": description,
                "name": name,
                "region": region,
                "icon": icon,
                "verification_level": verification_level,
                "default_message_notifications": default_message_notifications,
                "explicit_content_filter": explicit_content_filter,
                "preferred_locale": preferred_locale,
                "afk_timeout": afk_timeout,
                "roles": convert_and_respect_annotation_metadata(
                    object_=roles,
                    annotation=typing.Optional[typing.Sequence[CreateGuildRequestRoleItem]],
                    direction="write",
                ),
                "channels": convert_and_respect_annotation_metadata(
                    object_=channels,
                    annotation=typing.Optional[typing.Sequence[CreateGuildRequestChannelItem]],
                    direction="write",
                ),
                "afk_channel_id": afk_channel_id,
                "system_channel_id": system_channel_id,
                "system_channel_flags": system_channel_flags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildResponse,
                    parse_obj_as(
                        type_=GuildResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_my_private_archived_threads(
        self,
        channel_id: SnowflakeType,
        *,
        before: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThreadsResponse]:
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
        HttpResponse[ThreadsResponse]
            200 response for list_my_private_archived_threads
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/users/@me/threads/archived/private",
            method="GET",
            params={
                "before": before,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadsResponse,
                    parse_obj_as(
                        type_=ThreadsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_application_command_permissions(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[CommandPermissionsResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CommandPermissionsResponse]]
            200 response for list_guild_application_command_permissions
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands/permissions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CommandPermissionsResponse],
                    parse_obj_as(
                        type_=typing.List[CommandPermissionsResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_application_command_permissions(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CommandPermissionsResponse]:
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
        HttpResponse[CommandPermissionsResponse]
            200 response for get_guild_application_command_permissions
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands/{encode_path_param(command_id)}/permissions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CommandPermissionsResponse,
                    parse_obj_as(
                        type_=CommandPermissionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_guild_application_command_permissions(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        permissions: typing.Optional[typing.Sequence[ApplicationCommandPermission]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CommandPermissionsResponse]:
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
        HttpResponse[CommandPermissionsResponse]
            200 response for set_guild_application_command_permissions
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands/{encode_path_param(command_id)}/permissions",
            method="PUT",
            json={
                "permissions": convert_and_respect_annotation_metadata(
                    object_=permissions,
                    annotation=typing.Optional[typing.Sequence[ApplicationCommandPermission]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CommandPermissionsResponse,
                    parse_obj_as(
                        type_=CommandPermissionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_my_message_reaction(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/reactions/{encode_path_param(emoji_name)}/@me",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_my_message_reaction(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/reactions/{encode_path_param(emoji_name)}/@me",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_private_archived_threads(
        self,
        channel_id: SnowflakeType,
        *,
        before: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThreadsResponse]:
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
        HttpResponse[ThreadsResponse]
            200 response for list_private_archived_threads
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/threads/archived/private",
            method="GET",
            params={
                "before": serialize_datetime(before) if before is not None else None,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadsResponse,
                    parse_obj_as(
                        type_=ThreadsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_public_archived_threads(
        self,
        channel_id: SnowflakeType,
        *,
        before: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThreadsResponse]:
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
        HttpResponse[ThreadsResponse]
            200 response for list_public_archived_threads
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/threads/archived/public",
            method="GET",
            params={
                "before": serialize_datetime(before) if before is not None else None,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadsResponse,
                    parse_obj_as(
                        type_=ThreadsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_application_user_role_connection(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApplicationUserRoleConnectionResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApplicationUserRoleConnectionResponse]
            200 response for get_application_user_role_connection
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/@me/applications/{encode_path_param(application_id)}/role-connection",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationUserRoleConnectionResponse,
                    parse_obj_as(
                        type_=ApplicationUserRoleConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_application_user_role_connection(
        self,
        application_id: SnowflakeType,
        *,
        platform_name: typing.Optional[str] = OMIT,
        platform_username: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApplicationUserRoleConnectionResponse]:
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
        HttpResponse[ApplicationUserRoleConnectionResponse]
            200 response for update_application_user_role_connection
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/@me/applications/{encode_path_param(application_id)}/role-connection",
            method="PUT",
            json={
                "platform_name": platform_name,
                "platform_username": platform_username,
                "metadata": metadata,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationUserRoleConnectionResponse,
                    parse_obj_as(
                        type_=ApplicationUserRoleConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_application_user_role_connection(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/@me/applications/{encode_path_param(application_id)}/role-connection",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_my_guild_member(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PrivateGuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PrivateGuildMemberResponse]
            200 response for get_my_guild_member
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/@me/guilds/{encode_path_param(guild_id)}/member",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateGuildMemberResponse,
                    parse_obj_as(
                        type_=PrivateGuildMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_application_role_connections_metadata(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]]
            200 response for get_application_role_connections_metadata
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/role-connections/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_application_role_connections_metadata(
        self,
        application_id: SnowflakeType,
        *,
        request: typing.Optional[typing.Sequence[ApplicationRoleConnectionsMetadataItemRequest]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request : typing.Optional[typing.Sequence[ApplicationRoleConnectionsMetadataItemRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]]
            200 response for update_application_role_connections_metadata
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/role-connections/metadata",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Optional[typing.Sequence[ApplicationRoleConnectionsMetadataItemRequest]],
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def consume_entitlement(
        self,
        application_id: SnowflakeType,
        entitlement_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        entitlement_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/entitlements/{encode_path_param(entitlement_id)}/consume",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_application_command(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApplicationCommandResponse]:
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
        HttpResponse[ApplicationCommandResponse]
            200 response for get_guild_application_command
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands/{encode_path_param(command_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationCommandResponse,
                    parse_obj_as(
                        type_=ApplicationCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_guild_application_command(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands/{encode_path_param(command_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ApplicationCommandResponse]:
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
        HttpResponse[ApplicationCommandResponse]
            200 response for update_guild_application_command
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands/{encode_path_param(command_id)}",
            method="PATCH",
            json={
                "name": name,
                "name_localizations": name_localizations,
                "description": description,
                "description_localizations": description_localizations,
                "options": convert_and_respect_annotation_metadata(
                    object_=options,
                    annotation=typing.Optional[typing.Sequence[ApplicationCommandPatchRequestPartialOptionsItem]],
                    direction="write",
                ),
                "default_member_permissions": default_member_permissions,
                "dm_permission": dm_permission,
                "contexts": contexts,
                "integration_types": integration_types,
                "handler": handler,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationCommandResponse,
                    parse_obj_as(
                        type_=ApplicationCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_application_commands(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        with_localizations: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]:
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
        HttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]
            200 response for list_guild_application_commands
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands",
            method="GET",
            params={
                "with_localizations": with_localizations,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ApplicationCommandResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ApplicationCommandResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ApplicationCommandResponse]:
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
        HttpResponse[ApplicationCommandResponse]
            200 response for create_guild_application_command
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands",
            method="POST",
            json={
                "name": name,
                "name_localizations": name_localizations,
                "description": description,
                "description_localizations": description_localizations,
                "options": convert_and_respect_annotation_metadata(
                    object_=options,
                    annotation=typing.Optional[typing.Sequence[ApplicationCommandCreateRequestOptionsItem]],
                    direction="write",
                ),
                "default_member_permissions": default_member_permissions,
                "dm_permission": dm_permission,
                "contexts": contexts,
                "integration_types": integration_types,
                "handler": handler,
                "type": type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationCommandResponse,
                    parse_obj_as(
                        type_=ApplicationCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bulk_set_guild_application_commands(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        request: typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]:
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
        HttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]
            200 response for bulk_set_guild_application_commands
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]],
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ApplicationCommandResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ApplicationCommandResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def join_thread(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/thread-members/@me",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def leave_thread(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/thread-members/@me",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bulk_delete_messages(
        self,
        channel_id: SnowflakeType,
        *,
        messages: typing.Sequence[SnowflakeType],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        messages : typing.Sequence[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/bulk-delete",
            method="POST",
            json={
                "messages": messages,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_user_message_reaction(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/reactions/{encode_path_param(emoji_name)}/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.List[UserResponse]]:
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
        HttpResponse[typing.List[UserResponse]]
            200 response for list_message_reactions_by_emoji
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/reactions/{encode_path_param(emoji_name)}",
            method="GET",
            params={
                "after": after,
                "limit": limit,
                "type": type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UserResponse],
                    parse_obj_as(
                        type_=typing.List[UserResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_all_message_reactions_by_emoji(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/reactions/{encode_path_param(emoji_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_all_message_reactions(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/reactions",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def crosspost_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MessageResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessageResponse]
            200 response for crosspost_message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/crosspost",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_thread_from_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        name: str,
        auto_archive_duration: typing.Optional[ThreadAutoArchiveDuration] = OMIT,
        rate_limit_per_user: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThreadResponse]:
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
        HttpResponse[ThreadResponse]
            201 response for create_thread_from_message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/threads",
            method="POST",
            json={
                "name": name,
                "auto_archive_duration": auto_archive_duration,
                "rate_limit_per_user": rate_limit_per_user,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadResponse,
                    parse_obj_as(
                        type_=ThreadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ThreadSearchResponse]:
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
        HttpResponse[ThreadSearchResponse]
            200 response for thread_search
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/threads/search",
            method="GET",
            params={
                "name": name,
                "slop": slop,
                "min_id": min_id,
                "max_id": max_id,
                "tag": convert_and_respect_annotation_metadata(
                    object_=tag, annotation=ThreadSearchRequestTag, direction="write"
                ),
                "tag_setting": tag_setting,
                "archived": archived,
                "sort_by": sort_by,
                "sort_order": sort_order,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadSearchResponse,
                    parse_obj_as(
                        type_=ThreadSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_answer_voters(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        answer_id: int,
        *,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PollAnswerDetailsResponse]:
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
        HttpResponse[PollAnswerDetailsResponse]
            200 response for get_answer_voters
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/polls/{encode_path_param(message_id)}/answers/{encode_path_param(answer_id)}",
            method="GET",
            params={
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PollAnswerDetailsResponse,
                    parse_obj_as(
                        type_=PollAnswerDetailsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def poll_expire(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MessageResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessageResponse]
            200 response for poll_expire
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/polls/{encode_path_param(message_id)}/expire",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_original_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MessageResponse]:
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
        HttpResponse[MessageResponse]
            200 response for get_original_webhook_message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/messages/@original",
            method="GET",
            params={
                "thread_id": thread_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_original_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/messages/@original",
            method="DELETE",
            params={
                "thread_id": thread_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[MessageResponse]:
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
        HttpResponse[MessageResponse]
            200 response for update_original_webhook_message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/messages/@original",
            method="PATCH",
            params={
                "thread_id": thread_id,
                "with_components": with_components,
            },
            json={
                "content": content,
                "embeds": convert_and_respect_annotation_metadata(
                    object_=embeds, annotation=typing.Optional[typing.Sequence[RichEmbed]], direction="write"
                ),
                "allowed_mentions": convert_and_respect_annotation_metadata(
                    object_=allowed_mentions,
                    annotation=typing.Optional[MessageAllowedMentionsRequest],
                    direction="write",
                ),
                "components": convert_and_respect_annotation_metadata(
                    object_=components,
                    annotation=typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]],
                    direction="write",
                ),
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments,
                    annotation=typing.Optional[typing.Sequence[MessageAttachmentRequest]],
                    direction="write",
                ),
                "poll": convert_and_respect_annotation_metadata(
                    object_=poll, annotation=typing.Optional[PollCreateRequest], direction="write"
                ),
                "flags": flags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def leave_lobby(
        self, lobby_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}/members/@me",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.Optional[typing.List[ScheduledEventUserResponse]]]:
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
        HttpResponse[typing.Optional[typing.List[ScheduledEventUserResponse]]]
            200 response for list_guild_scheduled_event_users
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/scheduled-events/{encode_path_param(guild_scheduled_event_id)}/users",
            method="GET",
            params={
                "with_member": with_member,
                "limit": limit,
                "before": before,
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ScheduledEventUserResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ScheduledEventUserResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        rule_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAutoModerationRuleResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        rule_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAutoModerationRuleResponse]
            200 response for get_auto_moderation_rule
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/auto-moderation/rules/{encode_path_param(rule_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAutoModerationRuleResponse,
                    parse_obj_as(
                        type_=GetAutoModerationRuleResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        rule_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        rule_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/auto-moderation/rules/{encode_path_param(rule_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        rule_id: SnowflakeType,
        *,
        request: UpdateAutoModerationRuleRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateAutoModerationRuleResponse]:
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
        HttpResponse[UpdateAutoModerationRuleResponse]
            200 response for update_auto_moderation_rule
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/auto-moderation/rules/{encode_path_param(rule_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateAutoModerationRuleRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateAutoModerationRuleResponse,
                    parse_obj_as(
                        type_=UpdateAutoModerationRuleResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_auto_moderation_rules(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[typing.Optional[ListAutoModerationRulesResponseItem]]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[typing.Optional[ListAutoModerationRulesResponseItem]]]]
            200 response for list_auto_moderation_rules
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/auto-moderation/rules",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[typing.Optional[ListAutoModerationRulesResponseItem]]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[typing.Optional[ListAutoModerationRulesResponseItem]]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        *,
        request: CreateAutoModerationRuleRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAutoModerationRuleResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : CreateAutoModerationRuleRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateAutoModerationRuleResponse]
            200 response for create_auto_moderation_rule
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/auto-moderation/rules",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateAutoModerationRuleRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateAutoModerationRuleResponse,
                    parse_obj_as(
                        type_=CreateAutoModerationRuleResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_self_voice_state(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VoiceStateResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceStateResponse]
            200 response for get_self_voice_state
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/voice-states/@me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceStateResponse,
                    parse_obj_as(
                        type_=VoiceStateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_self_voice_state(
        self,
        guild_id: SnowflakeType,
        *,
        request_to_speak_timestamp: typing.Optional[dt.datetime] = OMIT,
        suppress: typing.Optional[bool] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/voice-states/@me",
            method="PATCH",
            json={
                "request_to_speak_timestamp": request_to_speak_timestamp,
                "suppress": suppress,
                "channel_id": channel_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_guild_members(
        self,
        guild_id: SnowflakeType,
        *,
        limit: int,
        query: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GuildMemberResponse]]:
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
        HttpResponse[typing.List[GuildMemberResponse]]
            200 response for search_guild_members
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/search",
            method="GET",
            params={
                "limit": limit,
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GuildMemberResponse],
                    parse_obj_as(
                        type_=typing.List[GuildMemberResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_active_guild_threads(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ThreadsResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ThreadsResponse]
            200 response for get_active_guild_threads
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/threads/active",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadsResponse,
                    parse_obj_as(
                        type_=ThreadsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_my_guild_member(
        self,
        guild_id: SnowflakeType,
        *,
        nick: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PrivateGuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        nick : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PrivateGuildMemberResponse]
            200 response for update_my_guild_member
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/@me",
            method="PATCH",
            json={
                "nick": nick,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateGuildMemberResponse,
                    parse_obj_as(
                        type_=PrivateGuildMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_guild_member_role(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/{encode_path_param(user_id)}/roles/{encode_path_param(role_id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_guild_member_role(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/{encode_path_param(user_id)}/roles/{encode_path_param(role_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def leave_guild(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/@me/guilds/{encode_path_param(guild_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def applications_get_activity_instance(
        self,
        application_id: SnowflakeType,
        instance_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmbeddedActivityInstance]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmbeddedActivityInstance]
            200 response for applications_get_activity_instance
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/activity-instances/{encode_path_param(instance_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmbeddedActivityInstance,
                    parse_obj_as(
                        type_=EmbeddedActivityInstance,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_entitlement(
        self,
        application_id: SnowflakeType,
        entitlement_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntitlementResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        entitlement_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntitlementResponse]
            200 response for get_entitlement
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/entitlements/{encode_path_param(entitlement_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntitlementResponse,
                    parse_obj_as(
                        type_=EntitlementResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_entitlement(
        self,
        application_id: SnowflakeType,
        entitlement_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        entitlement_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/entitlements/{encode_path_param(entitlement_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.List[typing.Optional[EntitlementResponse]]]:
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
        HttpResponse[typing.List[typing.Optional[EntitlementResponse]]]
            200 response for get_entitlements
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/entitlements",
            method="GET",
            params={
                "user_id": user_id,
                "sku_ids": convert_and_respect_annotation_metadata(
                    object_=sku_ids, annotation=GetEntitlementsRequestSkuIds, direction="write"
                ),
                "guild_id": guild_id,
                "before": before,
                "after": after,
                "limit": limit,
                "exclude_ended": exclude_ended,
                "exclude_deleted": exclude_deleted,
                "only_active": only_active,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Optional[EntitlementResponse]],
                    parse_obj_as(
                        type_=typing.List[typing.Optional[EntitlementResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_entitlement(
        self,
        application_id: SnowflakeType,
        *,
        sku_id: SnowflakeType,
        owner_id: SnowflakeType,
        owner_type: EntitlementOwnerTypes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntitlementResponse]:
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
        HttpResponse[EntitlementResponse]
            200 response for create_entitlement
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/entitlements",
            method="POST",
            json={
                "sku_id": sku_id,
                "owner_id": owner_id,
                "owner_type": owner_type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntitlementResponse,
                    parse_obj_as(
                        type_=EntitlementResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def upload_application_attachment(
        self, application_id: SnowflakeType, *, file: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ActivitiesAttachmentResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        file : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ActivitiesAttachmentResponse]
            200 response for upload_application_attachment
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/attachment",
            method="POST",
            data={
                "file": file,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActivitiesAttachmentResponse,
                    parse_obj_as(
                        type_=ActivitiesAttachmentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_application_command(
        self,
        application_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApplicationCommandResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApplicationCommandResponse]
            200 response for get_application_command
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/commands/{encode_path_param(command_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationCommandResponse,
                    parse_obj_as(
                        type_=ApplicationCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_application_command(
        self,
        application_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/commands/{encode_path_param(command_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ApplicationCommandResponse]:
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
        HttpResponse[ApplicationCommandResponse]
            200 response for update_application_command
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/commands/{encode_path_param(command_id)}",
            method="PATCH",
            json={
                "name": name,
                "name_localizations": name_localizations,
                "description": description,
                "description_localizations": description_localizations,
                "options": convert_and_respect_annotation_metadata(
                    object_=options,
                    annotation=typing.Optional[typing.Sequence[ApplicationCommandPatchRequestPartialOptionsItem]],
                    direction="write",
                ),
                "default_member_permissions": default_member_permissions,
                "dm_permission": dm_permission,
                "contexts": contexts,
                "integration_types": integration_types,
                "handler": handler,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationCommandResponse,
                    parse_obj_as(
                        type_=ApplicationCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_application_commands(
        self,
        application_id: SnowflakeType,
        *,
        with_localizations: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        with_localizations : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]
            200 response for list_application_commands
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/commands",
            method="GET",
            params={
                "with_localizations": with_localizations,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ApplicationCommandResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ApplicationCommandResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ApplicationCommandResponse]:
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
        HttpResponse[ApplicationCommandResponse]
            200 response for create_application_command
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/commands",
            method="POST",
            json={
                "name": name,
                "name_localizations": name_localizations,
                "description": description,
                "description_localizations": description_localizations,
                "options": convert_and_respect_annotation_metadata(
                    object_=options,
                    annotation=typing.Optional[typing.Sequence[ApplicationCommandCreateRequestOptionsItem]],
                    direction="write",
                ),
                "default_member_permissions": default_member_permissions,
                "dm_permission": dm_permission,
                "contexts": contexts,
                "integration_types": integration_types,
                "handler": handler,
                "type": type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationCommandResponse,
                    parse_obj_as(
                        type_=ApplicationCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bulk_set_application_commands(
        self,
        application_id: SnowflakeType,
        *,
        request: typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request : typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]
            200 response for bulk_set_application_commands
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/commands",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]],
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ApplicationCommandResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ApplicationCommandResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_application_emoji(
        self,
        application_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmojiResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmojiResponse]
            200 response for get_application_emoji
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/emojis/{encode_path_param(emoji_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmojiResponse,
                    parse_obj_as(
                        type_=EmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_application_emoji(
        self,
        application_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/emojis/{encode_path_param(emoji_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_application_emoji(
        self,
        application_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmojiResponse]:
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
        HttpResponse[EmojiResponse]
            200 response for update_application_emoji
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/emojis/{encode_path_param(emoji_id)}",
            method="PATCH",
            json={
                "name": name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmojiResponse,
                    parse_obj_as(
                        type_=EmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_application_emojis(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListApplicationEmojisResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListApplicationEmojisResponse]
            200 response for list_application_emojis
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/emojis",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListApplicationEmojisResponse,
                    parse_obj_as(
                        type_=ListApplicationEmojisResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_application_emoji(
        self,
        application_id: SnowflakeType,
        *,
        name: str,
        image: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmojiResponse]:
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
        HttpResponse[EmojiResponse]
            201 response for create_application_emoji
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/emojis",
            method="POST",
            json={
                "name": name,
                "image": image,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmojiResponse,
                    parse_obj_as(
                        type_=EmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_interaction_response(
        self,
        interaction_id: SnowflakeType,
        interaction_token: str,
        *,
        request: CreateInteractionResponseRequestBody,
        with_response: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[InteractionCallbackResponse]]:
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
        HttpResponse[typing.Optional[InteractionCallbackResponse]]
            200 response for create_interaction_response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"interactions/{encode_path_param(interaction_id)}/{encode_path_param(interaction_token)}/callback",
            method="POST",
            params={
                "with_response": with_response,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateInteractionResponseRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[InteractionCallbackResponse],
                    parse_obj_as(
                        type_=typing.Optional[InteractionCallbackResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def send_soundboard_sound(
        self,
        channel_id: SnowflakeType,
        *,
        sound_id: SnowflakeType,
        source_guild_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/send-soundboard-sound",
            method="POST",
            json={
                "sound_id": sound_id,
                "source_guild_id": source_guild_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_thread_member(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        with_member: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThreadMemberResponse]:
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
        HttpResponse[ThreadMemberResponse]
            200 response for get_thread_member
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/thread-members/{encode_path_param(user_id)}",
            method="GET",
            params={
                "with_member": with_member,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadMemberResponse,
                    parse_obj_as(
                        type_=ThreadMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_thread_member(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/thread-members/{encode_path_param(user_id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_thread_member(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/thread-members/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_thread_members(
        self,
        channel_id: SnowflakeType,
        *,
        with_member: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ThreadMemberResponse]]:
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
        HttpResponse[typing.List[ThreadMemberResponse]]
            200 response for list_thread_members
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/thread-members",
            method="GET",
            params={
                "with_member": with_member,
                "limit": limit,
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ThreadMemberResponse],
                    parse_obj_as(
                        type_=typing.List[ThreadMemberResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_channel_permission_overwrite(
        self,
        channel_id: SnowflakeType,
        overwrite_id: SnowflakeType,
        *,
        type: typing.Optional[ChannelPermissionOverwrites] = OMIT,
        allow: typing.Optional[int] = OMIT,
        deny: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/permissions/{encode_path_param(overwrite_id)}",
            method="PUT",
            json={
                "type": type,
                "allow": allow,
                "deny": deny,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_channel_permission_overwrite(
        self,
        channel_id: SnowflakeType,
        overwrite_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        overwrite_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/permissions/{encode_path_param(overwrite_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_group_dm_user(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        access_token: typing.Optional[str] = OMIT,
        nick: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[AddGroupDmUserResponse]]:
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
        HttpResponse[typing.Optional[AddGroupDmUserResponse]]
            201 response for add_group_dm_user
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/recipients/{encode_path_param(user_id)}",
            method="PUT",
            json={
                "access_token": access_token,
                "nick": nick,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AddGroupDmUserResponse],
                    parse_obj_as(
                        type_=typing.Optional[AddGroupDmUserResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_group_dm_user(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/recipients/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_channel(
        self,
        channel_id: SnowflakeType,
        *,
        webhook_channel_id: SnowflakeType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChannelFollowerResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        webhook_channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChannelFollowerResponse]
            200 response for follow_channel
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/followers",
            method="POST",
            json={
                "webhook_channel_id": webhook_channel_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChannelFollowerResponse,
                    parse_obj_as(
                        type_=ChannelFollowerResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MessageResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessageResponse]
            200 response for get_message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[MessageResponse]:
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
        HttpResponse[MessageResponse]
            200 response for update_message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}",
            method="PATCH",
            json={
                "content": content,
                "embeds": convert_and_respect_annotation_metadata(
                    object_=embeds, annotation=typing.Optional[typing.Sequence[RichEmbed]], direction="write"
                ),
                "flags": flags,
                "allowed_mentions": convert_and_respect_annotation_metadata(
                    object_=allowed_mentions,
                    annotation=typing.Optional[MessageAllowedMentionsRequest],
                    direction="write",
                ),
                "sticker_ids": sticker_ids,
                "components": convert_and_respect_annotation_metadata(
                    object_=components,
                    annotation=typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]],
                    direction="write",
                ),
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments,
                    annotation=typing.Optional[typing.Sequence[MessageAttachmentRequest]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_messages(
        self,
        channel_id: SnowflakeType,
        *,
        around: typing.Optional[SnowflakeType] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[MessageResponse]]]:
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
        HttpResponse[typing.Optional[typing.List[MessageResponse]]]
            200 response for list_messages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages",
            method="GET",
            params={
                "around": around,
                "before": before,
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[MessageResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[MessageResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[MessageResponse]:
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
        HttpResponse[MessageResponse]
            200 response for create_message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages",
            method="POST",
            json={
                "content": content,
                "embeds": convert_and_respect_annotation_metadata(
                    object_=embeds, annotation=typing.Optional[typing.Sequence[RichEmbed]], direction="write"
                ),
                "allowed_mentions": convert_and_respect_annotation_metadata(
                    object_=allowed_mentions,
                    annotation=typing.Optional[MessageAllowedMentionsRequest],
                    direction="write",
                ),
                "sticker_ids": sticker_ids,
                "components": convert_and_respect_annotation_metadata(
                    object_=components,
                    annotation=typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]],
                    direction="write",
                ),
                "flags": flags,
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments,
                    annotation=typing.Optional[typing.Sequence[MessageAttachmentRequest]],
                    direction="write",
                ),
                "poll": convert_and_respect_annotation_metadata(
                    object_=poll, annotation=typing.Optional[PollCreateRequest], direction="write"
                ),
                "confetti_potion": convert_and_respect_annotation_metadata(
                    object_=confetti_potion, annotation=typing.Optional[ConfettiPotionCreateRequest], direction="write"
                ),
                "message_reference": convert_and_respect_annotation_metadata(
                    object_=message_reference, annotation=typing.Optional[MessageReferenceRequest], direction="write"
                ),
                "nonce": convert_and_respect_annotation_metadata(
                    object_=nonce, annotation=typing.Optional[MessageCreateRequestNonce], direction="write"
                ),
                "enforce_nonce": enforce_nonce,
                "tts": tts,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_channel_webhooks(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[ListChannelWebhooksResponseItem]]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[ListChannelWebhooksResponseItem]]]
            200 response for list_channel_webhooks
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/webhooks",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ListChannelWebhooksResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ListChannelWebhooksResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_webhook(
        self,
        channel_id: SnowflakeType,
        *,
        name: str,
        avatar: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildIncomingWebhookResponse]:
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
        HttpResponse[GuildIncomingWebhookResponse]
            200 response for create_webhook
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/webhooks",
            method="POST",
            json={
                "name": name,
                "avatar": avatar,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildIncomingWebhookResponse,
                    parse_obj_as(
                        type_=GuildIncomingWebhookResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_channel_invites(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[ListChannelInvitesResponseItem]]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[ListChannelInvitesResponseItem]]]
            200 response for list_channel_invites
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/invites",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ListChannelInvitesResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ListChannelInvitesResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_channel_invite(
        self,
        channel_id: SnowflakeType,
        *,
        request: CreateChannelInviteRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[CreateChannelInviteResponse]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request : CreateChannelInviteRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[CreateChannelInviteResponse]]
            200 response for create_channel_invite
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/invites",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateChannelInviteRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CreateChannelInviteResponse],
                    parse_obj_as(
                        type_=typing.Optional[CreateChannelInviteResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_thread(
        self,
        channel_id: SnowflakeType,
        *,
        request: CreateThreadRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreatedThreadResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request : CreateThreadRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreatedThreadResponse]
            201 response for create_thread
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/threads",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateThreadRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreatedThreadResponse,
                    parse_obj_as(
                        type_=CreatedThreadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def trigger_typing_indicator(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[TypingIndicatorResponse]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[TypingIndicatorResponse]]
            200 response for trigger_typing_indicator
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/typing",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[TypingIndicatorResponse],
                    parse_obj_as(
                        type_=typing.Optional[TypingIndicatorResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def pin_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/pins/{encode_path_param(message_id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def unpin_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/pins/{encode_path_param(message_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_pinned_messages(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[MessageResponse]]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[MessageResponse]]]
            200 response for list_pinned_messages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/pins",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[MessageResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[MessageResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        message_id: SnowflakeType,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MessageResponse]:
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
        HttpResponse[MessageResponse]
            200 response for get_webhook_message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/messages/{encode_path_param(message_id)}",
            method="GET",
            params={
                "thread_id": thread_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        message_id: SnowflakeType,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/messages/{encode_path_param(message_id)}",
            method="DELETE",
            params={
                "thread_id": thread_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[MessageResponse]:
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
        HttpResponse[MessageResponse]
            200 response for update_webhook_message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/messages/{encode_path_param(message_id)}",
            method="PATCH",
            params={
                "thread_id": thread_id,
                "with_components": with_components,
            },
            json={
                "content": content,
                "embeds": convert_and_respect_annotation_metadata(
                    object_=embeds, annotation=typing.Optional[typing.Sequence[RichEmbed]], direction="write"
                ),
                "allowed_mentions": convert_and_respect_annotation_metadata(
                    object_=allowed_mentions,
                    annotation=typing.Optional[MessageAllowedMentionsRequest],
                    direction="write",
                ),
                "components": convert_and_respect_annotation_metadata(
                    object_=components,
                    annotation=typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]],
                    direction="write",
                ),
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments,
                    annotation=typing.Optional[typing.Sequence[MessageAttachmentRequest]],
                    direction="write",
                ),
                "poll": convert_and_respect_annotation_metadata(
                    object_=poll, annotation=typing.Optional[PollCreateRequest], direction="write"
                ),
                "flags": flags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/github",
            method="POST",
            params={
                "wait": wait,
                "thread_id": thread_id,
            },
            json={
                "action": action,
                "ref": ref,
                "ref_type": ref_type,
                "comment": convert_and_respect_annotation_metadata(
                    object_=comment, annotation=typing.Optional[GithubComment], direction="write"
                ),
                "issue": convert_and_respect_annotation_metadata(
                    object_=issue, annotation=typing.Optional[GithubIssue], direction="write"
                ),
                "pull_request": convert_and_respect_annotation_metadata(
                    object_=pull_request, annotation=typing.Optional[GithubIssue], direction="write"
                ),
                "repository": convert_and_respect_annotation_metadata(
                    object_=repository, annotation=typing.Optional[GithubRepository], direction="write"
                ),
                "forkee": convert_and_respect_annotation_metadata(
                    object_=forkee, annotation=typing.Optional[GithubRepository], direction="write"
                ),
                "sender": convert_and_respect_annotation_metadata(
                    object_=sender, annotation=GithubUser, direction="write"
                ),
                "member": convert_and_respect_annotation_metadata(
                    object_=member, annotation=typing.Optional[GithubUser], direction="write"
                ),
                "release": convert_and_respect_annotation_metadata(
                    object_=release, annotation=typing.Optional[GithubRelease], direction="write"
                ),
                "head_commit": convert_and_respect_annotation_metadata(
                    object_=head_commit, annotation=typing.Optional[GithubCommit], direction="write"
                ),
                "commits": convert_and_respect_annotation_metadata(
                    object_=commits, annotation=typing.Optional[typing.Sequence[GithubCommit]], direction="write"
                ),
                "forced": forced,
                "compare": compare,
                "review": convert_and_respect_annotation_metadata(
                    object_=review, annotation=typing.Optional[GithubReview], direction="write"
                ),
                "check_run": convert_and_respect_annotation_metadata(
                    object_=check_run, annotation=typing.Optional[GithubCheckRun], direction="write"
                ),
                "check_suite": convert_and_respect_annotation_metadata(
                    object_=check_suite, annotation=typing.Optional[GithubCheckSuite], direction="write"
                ),
                "discussion": convert_and_respect_annotation_metadata(
                    object_=discussion, annotation=typing.Optional[GithubDiscussion], direction="write"
                ),
                "answer": convert_and_respect_annotation_metadata(
                    object_=answer, annotation=typing.Optional[GithubComment], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.Optional[str]]:
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
        HttpResponse[typing.Optional[str]]
            200 response for execute_slack_compatible_webhook
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/slack",
            method="POST",
            params={
                "wait": wait,
                "thread_id": thread_id,
            },
            json={
                "text": text,
                "username": username,
                "icon_url": icon_url,
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments,
                    annotation=typing.Optional[typing.Sequence[WebhookSlackEmbed]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[str],
                    parse_obj_as(
                        type_=typing.Optional[str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def edit_lobby_channel_link(
        self,
        lobby_id: SnowflakeType,
        *,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LobbyResponse]:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        channel_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LobbyResponse]
            200 response for edit_lobby_channel_link
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}/channel-linking",
            method="PATCH",
            json={
                "channel_id": channel_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyResponse,
                    parse_obj_as(
                        type_=LobbyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[LobbyMessageResponse]:
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
        HttpResponse[LobbyMessageResponse]
            201 response for create_lobby_message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}/messages",
            method="POST",
            json={
                "content": content,
                "embeds": convert_and_respect_annotation_metadata(
                    object_=embeds, annotation=typing.Optional[typing.Sequence[RichEmbed]], direction="write"
                ),
                "allowed_mentions": convert_and_respect_annotation_metadata(
                    object_=allowed_mentions,
                    annotation=typing.Optional[MessageAllowedMentionsRequest],
                    direction="write",
                ),
                "sticker_ids": sticker_ids,
                "components": convert_and_respect_annotation_metadata(
                    object_=components,
                    annotation=typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]],
                    direction="write",
                ),
                "flags": flags,
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments,
                    annotation=typing.Optional[typing.Sequence[MessageAttachmentRequest]],
                    direction="write",
                ),
                "poll": convert_and_respect_annotation_metadata(
                    object_=poll, annotation=typing.Optional[PollCreateRequest], direction="write"
                ),
                "confetti_potion": convert_and_respect_annotation_metadata(
                    object_=confetti_potion, annotation=typing.Optional[ConfettiPotionCreateRequest], direction="write"
                ),
                "message_reference": convert_and_respect_annotation_metadata(
                    object_=message_reference, annotation=typing.Optional[MessageReferenceRequest], direction="write"
                ),
                "nonce": convert_and_respect_annotation_metadata(
                    object_=nonce, annotation=typing.Optional[SdkMessageRequestNonce], direction="write"
                ),
                "enforce_nonce": enforce_nonce,
                "tts": tts,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyMessageResponse,
                    parse_obj_as(
                        type_=LobbyMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_lobby_member(
        self,
        lobby_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LobbyMemberResponse]:
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
        HttpResponse[LobbyMemberResponse]
            200 response for add_lobby_member
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}/members/{encode_path_param(user_id)}",
            method="PUT",
            json={
                "metadata": metadata,
                "flags": flags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyMemberResponse,
                    parse_obj_as(
                        type_=LobbyMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_lobby_member(
        self,
        lobby_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}/members/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_template(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GuildTemplateResponse]:
        """
        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GuildTemplateResponse]
            200 response for get_guild_template
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/templates/{encode_path_param(code)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildTemplateResponse,
                    parse_obj_as(
                        type_=GuildTemplateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_guild_from_template(
        self,
        code: str,
        *,
        name: str,
        icon: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildResponse]:
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
        HttpResponse[GuildResponse]
            201 response for create_guild_from_template
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/templates/{encode_path_param(code)}",
            method="POST",
            json={
                "name": name,
                "icon": icon,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildResponse,
                    parse_obj_as(
                        type_=GuildResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_new_member_welcome(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[GuildHomeSettingsResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[GuildHomeSettingsResponse]]
            200 response for get_guild_new_member_welcome
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/new-member-welcome",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[GuildHomeSettingsResponse],
                    parse_obj_as(
                        type_=typing.Optional[GuildHomeSettingsResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_soundboard_sound(
        self,
        guild_id: SnowflakeType,
        sound_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SoundboardSoundResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sound_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SoundboardSoundResponse]
            200 response for get_guild_soundboard_sound
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/soundboard-sounds/{encode_path_param(sound_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SoundboardSoundResponse,
                    parse_obj_as(
                        type_=SoundboardSoundResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_guild_soundboard_sound(
        self,
        guild_id: SnowflakeType,
        sound_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sound_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/soundboard-sounds/{encode_path_param(sound_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[SoundboardSoundResponse]:
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
        HttpResponse[SoundboardSoundResponse]
            200 response for update_guild_soundboard_sound
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/soundboard-sounds/{encode_path_param(sound_id)}",
            method="PATCH",
            json={
                "name": name,
                "volume": volume,
                "emoji_id": emoji_id,
                "emoji_name": emoji_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SoundboardSoundResponse,
                    parse_obj_as(
                        type_=SoundboardSoundResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_soundboard_sounds(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListGuildSoundboardSoundsResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListGuildSoundboardSoundsResponse]
            200 response for list_guild_soundboard_sounds
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/soundboard-sounds",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListGuildSoundboardSoundsResponse,
                    parse_obj_as(
                        type_=ListGuildSoundboardSoundsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[SoundboardSoundResponse]:
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
        HttpResponse[SoundboardSoundResponse]
            201 response for create_guild_soundboard_sound
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/soundboard-sounds",
            method="POST",
            json={
                "name": name,
                "volume": volume,
                "emoji_id": emoji_id,
                "emoji_name": emoji_name,
                "sound": sound,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SoundboardSoundResponse,
                    parse_obj_as(
                        type_=SoundboardSoundResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        with_user_count: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetGuildScheduledEventResponse]:
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
        HttpResponse[GetGuildScheduledEventResponse]
            200 response for get_guild_scheduled_event
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/scheduled-events/{encode_path_param(guild_scheduled_event_id)}",
            method="GET",
            params={
                "with_user_count": with_user_count,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGuildScheduledEventResponse,
                    parse_obj_as(
                        type_=GetGuildScheduledEventResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        guild_scheduled_event_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/scheduled-events/{encode_path_param(guild_scheduled_event_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        request: UpdateGuildScheduledEventRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateGuildScheduledEventResponse]:
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
        HttpResponse[UpdateGuildScheduledEventResponse]
            200 response for update_guild_scheduled_event
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/scheduled-events/{encode_path_param(guild_scheduled_event_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateGuildScheduledEventRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateGuildScheduledEventResponse,
                    parse_obj_as(
                        type_=UpdateGuildScheduledEventResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_scheduled_events(
        self,
        guild_id: SnowflakeType,
        *,
        with_user_count: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[ListGuildScheduledEventsResponseItem]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        with_user_count : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[ListGuildScheduledEventsResponseItem]]]
            200 response for list_guild_scheduled_events
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/scheduled-events",
            method="GET",
            params={
                "with_user_count": with_user_count,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ListGuildScheduledEventsResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ListGuildScheduledEventsResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        *,
        request: CreateGuildScheduledEventRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateGuildScheduledEventResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : CreateGuildScheduledEventRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateGuildScheduledEventResponse]
            200 response for create_guild_scheduled_event
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/scheduled-events",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateGuildScheduledEventRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateGuildScheduledEventResponse,
                    parse_obj_as(
                        type_=CreateGuildScheduledEventResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_welcome_screen(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GuildWelcomeScreenResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GuildWelcomeScreenResponse]
            200 response for get_guild_welcome_screen
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/welcome-screen",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildWelcomeScreenResponse,
                    parse_obj_as(
                        type_=GuildWelcomeScreenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_guild_welcome_screen(
        self,
        guild_id: SnowflakeType,
        *,
        description: typing.Optional[str] = OMIT,
        welcome_channels: typing.Optional[typing.Sequence[GuildWelcomeChannel]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildWelcomeScreenResponse]:
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
        HttpResponse[GuildWelcomeScreenResponse]
            200 response for update_guild_welcome_screen
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/welcome-screen",
            method="PATCH",
            json={
                "description": description,
                "welcome_channels": convert_and_respect_annotation_metadata(
                    object_=welcome_channels,
                    annotation=typing.Optional[typing.Sequence[GuildWelcomeChannel]],
                    direction="write",
                ),
                "enabled": enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildWelcomeScreenResponse,
                    parse_obj_as(
                        type_=GuildWelcomeScreenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_voice_state(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[VoiceStateResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VoiceStateResponse]
            200 response for get_voice_state
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/voice-states/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceStateResponse,
                    parse_obj_as(
                        type_=VoiceStateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_voice_state(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        suppress: typing.Optional[bool] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/voice-states/{encode_path_param(user_id)}",
            method="PATCH",
            json={
                "suppress": suppress,
                "channel_id": channel_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_guild_integration(
        self,
        guild_id: SnowflakeType,
        integration_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        integration_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/integrations/{encode_path_param(integration_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_integrations(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[ListGuildIntegrationsResponseItem]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[ListGuildIntegrationsResponseItem]]]
            200 response for list_guild_integrations
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/integrations",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ListGuildIntegrationsResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ListGuildIntegrationsResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_widget(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WidgetResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WidgetResponse]
            200 response for get_guild_widget
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/widget.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WidgetResponse,
                    parse_obj_as(
                        type_=WidgetResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guilds_onboarding(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserGuildOnboardingResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserGuildOnboardingResponse]
            200 response for get_guilds_onboarding
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/onboarding",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGuildOnboardingResponse,
                    parse_obj_as(
                        type_=UserGuildOnboardingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def put_guilds_onboarding(
        self,
        guild_id: SnowflakeType,
        *,
        prompts: typing.Optional[typing.Sequence[UpdateOnboardingPromptRequest]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        default_channel_ids: typing.Optional[typing.Sequence[SnowflakeType]] = OMIT,
        mode: typing.Optional[GuildOnboardingMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildOnboardingResponse]:
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
        HttpResponse[GuildOnboardingResponse]
            200 response for put_guilds_onboarding
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/onboarding",
            method="PUT",
            json={
                "prompts": convert_and_respect_annotation_metadata(
                    object_=prompts,
                    annotation=typing.Optional[typing.Sequence[UpdateOnboardingPromptRequest]],
                    direction="write",
                ),
                "enabled": enabled,
                "default_channel_ids": default_channel_ids,
                "mode": mode,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildOnboardingResponse,
                    parse_obj_as(
                        type_=GuildOnboardingResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_vanity_url(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[VanityUrlResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[VanityUrlResponse]
            200 response for get_guild_vanity_url
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/vanity-url",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VanityUrlResponse,
                    parse_obj_as(
                        type_=VanityUrlResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[GuildAuditLogResponse]:
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
        HttpResponse[GuildAuditLogResponse]
            200 response for list_guild_audit_log_entries
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/audit-logs",
            method="GET",
            params={
                "user_id": user_id,
                "target_id": target_id,
                "action_type": action_type,
                "before": before,
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildAuditLogResponse,
                    parse_obj_as(
                        type_=GuildAuditLogResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def get_guild_widget_png(
        self,
        guild_id: SnowflakeType,
        *,
        style: typing.Optional[WidgetImageStyles] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        style : typing.Optional[WidgetImageStyles]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            200 response for get_guild_widget_png
        """
        with self._client_wrapper.httpx_client.stream(
            f"guilds/{encode_path_param(guild_id)}/widget.png",
            method="GET",
            params={
                "style": style,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def sync_guild_template(
        self, guild_id: SnowflakeType, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GuildTemplateResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GuildTemplateResponse]
            200 response for sync_guild_template
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/templates/{encode_path_param(code)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildTemplateResponse,
                    parse_obj_as(
                        type_=GuildTemplateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_guild_template(
        self, guild_id: SnowflakeType, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GuildTemplateResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GuildTemplateResponse]
            200 response for delete_guild_template
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/templates/{encode_path_param(code)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildTemplateResponse,
                    parse_obj_as(
                        type_=GuildTemplateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_guild_template(
        self,
        guild_id: SnowflakeType,
        code: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildTemplateResponse]:
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
        HttpResponse[GuildTemplateResponse]
            200 response for update_guild_template
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/templates/{encode_path_param(code)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildTemplateResponse,
                    parse_obj_as(
                        type_=GuildTemplateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_templates(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[GuildTemplateResponse]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[GuildTemplateResponse]]]
            200 response for list_guild_templates
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/templates",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[GuildTemplateResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[GuildTemplateResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_guild_template(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildTemplateResponse]:
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
        HttpResponse[GuildTemplateResponse]
            200 response for create_guild_template
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/templates",
            method="POST",
            json={
                "name": name,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildTemplateResponse,
                    parse_obj_as(
                        type_=GuildTemplateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_sticker(
        self,
        guild_id: SnowflakeType,
        sticker_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildStickerResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sticker_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GuildStickerResponse]
            200 response for get_guild_sticker
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/stickers/{encode_path_param(sticker_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildStickerResponse,
                    parse_obj_as(
                        type_=GuildStickerResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_guild_sticker(
        self,
        guild_id: SnowflakeType,
        sticker_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sticker_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/stickers/{encode_path_param(sticker_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_guild_sticker(
        self,
        guild_id: SnowflakeType,
        sticker_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildStickerResponse]:
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
        HttpResponse[GuildStickerResponse]
            200 response for update_guild_sticker
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/stickers/{encode_path_param(sticker_id)}",
            method="PATCH",
            json={
                "name": name,
                "tags": tags,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildStickerResponse,
                    parse_obj_as(
                        type_=GuildStickerResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bulk_ban_users_from_guild(
        self,
        guild_id: SnowflakeType,
        *,
        user_ids: typing.Sequence[SnowflakeType],
        delete_message_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkBanUsersResponse]:
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
        HttpResponse[BulkBanUsersResponse]
            200 response for bulk_ban_users_from_guild
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/bulk-ban",
            method="POST",
            json={
                "user_ids": user_ids,
                "delete_message_seconds": delete_message_seconds,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkBanUsersResponse,
                    parse_obj_as(
                        type_=BulkBanUsersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_stickers(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GuildStickerResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GuildStickerResponse]]
            200 response for list_guild_stickers
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/stickers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GuildStickerResponse],
                    parse_obj_as(
                        type_=typing.List[GuildStickerResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_guild_sticker(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        tags: str,
        file: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildStickerResponse]:
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
        HttpResponse[GuildStickerResponse]
            201 response for create_guild_sticker
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/stickers",
            method="POST",
            data={
                "name": name,
                "tags": tags,
                "description": description,
                "file": file,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildStickerResponse,
                    parse_obj_as(
                        type_=GuildStickerResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_webhooks(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[GetGuildWebhooksResponseItem]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[GetGuildWebhooksResponseItem]]]
            200 response for get_guild_webhooks
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/webhooks",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[GetGuildWebhooksResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[GetGuildWebhooksResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_channels(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[ListGuildChannelsResponseItem]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[ListGuildChannelsResponseItem]]]
            200 response for list_guild_channels
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/channels",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ListGuildChannelsResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ListGuildChannelsResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[GuildChannelResponse]:
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
        HttpResponse[GuildChannelResponse]
            201 response for create_guild_channel
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/channels",
            method="POST",
            json={
                "type": type,
                "name": name,
                "position": position,
                "topic": topic,
                "bitrate": bitrate,
                "user_limit": user_limit,
                "nsfw": nsfw,
                "rate_limit_per_user": rate_limit_per_user,
                "parent_id": parent_id,
                "permission_overwrites": convert_and_respect_annotation_metadata(
                    object_=permission_overwrites,
                    annotation=typing.Optional[typing.Sequence[ChannelPermissionOverwriteRequest]],
                    direction="write",
                ),
                "rtc_region": rtc_region,
                "video_quality_mode": video_quality_mode,
                "default_auto_archive_duration": default_auto_archive_duration,
                "default_reaction_emoji": convert_and_respect_annotation_metadata(
                    object_=default_reaction_emoji,
                    annotation=typing.Optional[UpdateDefaultReactionEmojiRequest],
                    direction="write",
                ),
                "default_thread_rate_limit_per_user": default_thread_rate_limit_per_user,
                "default_sort_order": default_sort_order,
                "default_forum_layout": default_forum_layout,
                "available_tags": convert_and_respect_annotation_metadata(
                    object_=available_tags,
                    annotation=typing.Optional[typing.Sequence[typing.Optional[CreateOrUpdateThreadTagRequest]]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildChannelResponse,
                    parse_obj_as(
                        type_=GuildChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bulk_update_guild_channels(
        self,
        guild_id: SnowflakeType,
        *,
        request: typing.Sequence[BulkUpdateGuildChannelsRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : typing.Sequence[BulkUpdateGuildChannelsRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/channels",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[BulkUpdateGuildChannelsRequestBodyItem], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_member(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GuildMemberResponse]
            200 response for get_guild_member
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildMemberResponse,
                    parse_obj_as(
                        type_=GuildMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.Optional[GuildMemberResponse]]:
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
        HttpResponse[typing.Optional[GuildMemberResponse]]
            201 response for add_guild_member
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/{encode_path_param(user_id)}",
            method="PUT",
            json={
                "nick": nick,
                "roles": roles,
                "mute": mute,
                "deaf": deaf,
                "access_token": access_token,
                "flags": flags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[GuildMemberResponse],
                    parse_obj_as(
                        type_=typing.Optional[GuildMemberResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_guild_member(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.Optional[GuildMemberResponse]]:
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
        HttpResponse[typing.Optional[GuildMemberResponse]]
            200 response for update_guild_member
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/{encode_path_param(user_id)}",
            method="PATCH",
            json={
                "nick": nick,
                "roles": roles,
                "mute": mute,
                "deaf": deaf,
                "channel_id": channel_id,
                "communication_disabled_until": communication_disabled_until,
                "flags": flags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[GuildMemberResponse],
                    parse_obj_as(
                        type_=typing.Optional[GuildMemberResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_members(
        self,
        guild_id: SnowflakeType,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GuildMemberResponse]]:
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
        HttpResponse[typing.List[GuildMemberResponse]]
            200 response for list_guild_members
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members",
            method="GET",
            params={
                "limit": limit,
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GuildMemberResponse],
                    parse_obj_as(
                        type_=typing.List[GuildMemberResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_preview(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GuildPreviewResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GuildPreviewResponse]
            200 response for get_guild_preview
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/preview",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildPreviewResponse,
                    parse_obj_as(
                        type_=GuildPreviewResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_invites(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[ListGuildInvitesResponseItem]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[ListGuildInvitesResponseItem]]]
            200 response for list_guild_invites
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/invites",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ListGuildInvitesResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ListGuildInvitesResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_voice_regions(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[VoiceRegionResponse]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[VoiceRegionResponse]]]
            200 response for list_guild_voice_regions
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/regions",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[VoiceRegionResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[VoiceRegionResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_emoji(
        self,
        guild_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmojiResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmojiResponse]
            200 response for get_guild_emoji
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/emojis/{encode_path_param(emoji_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmojiResponse,
                    parse_obj_as(
                        type_=EmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_guild_emoji(
        self,
        guild_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/emojis/{encode_path_param(emoji_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_guild_emoji(
        self,
        guild_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmojiResponse]:
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
        HttpResponse[EmojiResponse]
            200 response for update_guild_emoji
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/emojis/{encode_path_param(emoji_id)}",
            method="PATCH",
            json={
                "name": name,
                "roles": roles,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmojiResponse,
                    parse_obj_as(
                        type_=EmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_emojis(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[typing.List[EmojiResponse]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[typing.List[EmojiResponse]]]
            200 response for list_guild_emojis
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/emojis",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[EmojiResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[EmojiResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_guild_emoji(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        image: str,
        roles: typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmojiResponse]:
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
        HttpResponse[EmojiResponse]
            201 response for create_guild_emoji
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/emojis",
            method="POST",
            json={
                "name": name,
                "image": image,
                "roles": roles,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmojiResponse,
                    parse_obj_as(
                        type_=EmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_widget_settings(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WidgetSettingsResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WidgetSettingsResponse]
            200 response for get_guild_widget_settings
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/widget",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WidgetSettingsResponse,
                    parse_obj_as(
                        type_=WidgetSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_guild_widget_settings(
        self,
        guild_id: SnowflakeType,
        *,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WidgetSettingsResponse]:
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
        HttpResponse[WidgetSettingsResponse]
            200 response for update_guild_widget_settings
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/widget",
            method="PATCH",
            json={
                "channel_id": channel_id,
                "enabled": enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WidgetSettingsResponse,
                    parse_obj_as(
                        type_=WidgetSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_role(
        self,
        guild_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildRoleResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        role_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GuildRoleResponse]
            200 response for get_guild_role
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/roles/{encode_path_param(role_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildRoleResponse,
                    parse_obj_as(
                        type_=GuildRoleResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_guild_role(
        self,
        guild_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        role_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/roles/{encode_path_param(role_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[GuildRoleResponse]:
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
        HttpResponse[GuildRoleResponse]
            200 response for update_guild_role
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/roles/{encode_path_param(role_id)}",
            method="PATCH",
            json={
                "name": name,
                "permissions": permissions,
                "color": color,
                "hoist": hoist,
                "mentionable": mentionable,
                "icon": icon,
                "unicode_emoji": unicode_emoji,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildRoleResponse,
                    parse_obj_as(
                        type_=GuildRoleResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_roles(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GuildRoleResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GuildRoleResponse]]
            200 response for list_guild_roles
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/roles",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GuildRoleResponse],
                    parse_obj_as(
                        type_=typing.List[GuildRoleResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[GuildRoleResponse]:
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
        HttpResponse[GuildRoleResponse]
            200 response for create_guild_role
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/roles",
            method="POST",
            json={
                "name": name,
                "permissions": permissions,
                "color": color,
                "hoist": hoist,
                "mentionable": mentionable,
                "icon": icon,
                "unicode_emoji": unicode_emoji,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildRoleResponse,
                    parse_obj_as(
                        type_=GuildRoleResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bulk_update_guild_roles(
        self,
        guild_id: SnowflakeType,
        *,
        request: typing.Sequence[BulkUpdateGuildRolesRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GuildRoleResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : typing.Sequence[BulkUpdateGuildRolesRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GuildRoleResponse]]
            200 response for bulk_update_guild_roles
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/roles",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[BulkUpdateGuildRolesRequestBodyItem], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GuildRoleResponse],
                    parse_obj_as(
                        type_=typing.List[GuildRoleResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def preview_prune_guild(
        self,
        guild_id: SnowflakeType,
        *,
        days: typing.Optional[int] = None,
        include_roles: typing.Optional[PreviewPruneGuildRequestIncludeRoles] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildPruneResponse]:
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
        HttpResponse[GuildPruneResponse]
            200 response for preview_prune_guild
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/prune",
            method="GET",
            params={
                "days": days,
                "include_roles": convert_and_respect_annotation_metadata(
                    object_=include_roles, annotation=PreviewPruneGuildRequestIncludeRoles, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildPruneResponse,
                    parse_obj_as(
                        type_=GuildPruneResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def prune_guild(
        self,
        guild_id: SnowflakeType,
        *,
        days: typing.Optional[int] = OMIT,
        compute_prune_count: typing.Optional[bool] = OMIT,
        include_roles: typing.Optional[PruneGuildRequestIncludeRoles] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildPruneResponse]:
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
        HttpResponse[GuildPruneResponse]
            200 response for prune_guild
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/prune",
            method="POST",
            json={
                "days": days,
                "compute_prune_count": compute_prune_count,
                "include_roles": convert_and_respect_annotation_metadata(
                    object_=include_roles, annotation=typing.Optional[PruneGuildRequestIncludeRoles], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildPruneResponse,
                    parse_obj_as(
                        type_=GuildPruneResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild_ban(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildBanResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GuildBanResponse]
            200 response for get_guild_ban
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/bans/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildBanResponse,
                    parse_obj_as(
                        type_=GuildBanResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ban_user_from_guild(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        delete_message_seconds: typing.Optional[int] = OMIT,
        delete_message_days: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/bans/{encode_path_param(user_id)}",
            method="PUT",
            json={
                "delete_message_seconds": delete_message_seconds,
                "delete_message_days": delete_message_days,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def unban_user_from_guild(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/bans/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_guild_bans(
        self,
        guild_id: SnowflakeType,
        *,
        limit: typing.Optional[int] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[typing.List[GuildBanResponse]]]:
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
        HttpResponse[typing.Optional[typing.List[GuildBanResponse]]]
            200 response for list_guild_bans
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/bans",
            method="GET",
            params={
                "limit": limit,
                "before": before,
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[GuildBanResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[GuildBanResponse]],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_guild_mfa_level(
        self, guild_id: SnowflakeType, *, level: GuildMfaLevel, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GuildMfaLevelResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        level : GuildMfaLevel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GuildMfaLevelResponse]
            200 response for set_guild_mfa_level
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/mfa",
            method="POST",
            json={
                "level": level,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildMfaLevelResponse,
                    parse_obj_as(
                        type_=GuildMfaLevelResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_stage_instance(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StageInstanceResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StageInstanceResponse]
            200 response for get_stage_instance
        """
        _response = self._client_wrapper.httpx_client.request(
            f"stage-instances/{encode_path_param(channel_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StageInstanceResponse,
                    parse_obj_as(
                        type_=StageInstanceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_stage_instance(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"stage-instances/{encode_path_param(channel_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_stage_instance(
        self,
        channel_id: SnowflakeType,
        *,
        topic: typing.Optional[str] = OMIT,
        privacy_level: typing.Optional[StageInstancesPrivacyLevels] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StageInstanceResponse]:
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
        HttpResponse[StageInstanceResponse]
            200 response for update_stage_instance
        """
        _response = self._client_wrapper.httpx_client.request(
            f"stage-instances/{encode_path_param(channel_id)}",
            method="PATCH",
            json={
                "topic": topic,
                "privacy_level": privacy_level,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StageInstanceResponse,
                    parse_obj_as(
                        type_=StageInstanceResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_sticker_pack(
        self, pack_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StickerPackResponse]:
        """
        Parameters
        ----------
        pack_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StickerPackResponse]
            200 response for get_sticker_pack
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sticker-packs/{encode_path_param(pack_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StickerPackResponse,
                    parse_obj_as(
                        type_=StickerPackResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_application(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PrivateApplicationResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PrivateApplicationResponse]
            200 response for get_application
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateApplicationResponse,
                    parse_obj_as(
                        type_=PrivateApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[PrivateApplicationResponse]:
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
        HttpResponse[PrivateApplicationResponse]
            200 response for update_application
        """
        _response = self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}",
            method="PATCH",
            json={
                "description": convert_and_respect_annotation_metadata(
                    object_=description,
                    annotation=typing.Optional[ApplicationFormPartialDescription],
                    direction="write",
                ),
                "icon": icon,
                "cover_image": cover_image,
                "team_id": team_id,
                "flags": flags,
                "interactions_endpoint_url": interactions_endpoint_url,
                "explicit_content_filter": explicit_content_filter,
                "max_participants": max_participants,
                "type": type,
                "tags": tags,
                "custom_install_url": custom_install_url,
                "install_params": convert_and_respect_annotation_metadata(
                    object_=install_params,
                    annotation=typing.Optional[ApplicationOAuth2InstallParams],
                    direction="write",
                ),
                "role_connections_verification_url": role_connections_verification_url,
                "integration_types_config": convert_and_respect_annotation_metadata(
                    object_=integration_types_config,
                    annotation=typing.Optional[
                        typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]
                    ],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateApplicationResponse,
                    parse_obj_as(
                        type_=PrivateApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_webhook_by_token(
        self, webhook_id: SnowflakeType, webhook_token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetWebhookByTokenResponse]:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetWebhookByTokenResponse]
            200 response for get_webhook_by_token
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWebhookByTokenResponse,
                    parse_obj_as(
                        type_=GetWebhookByTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[typing.Optional[MessageResponse]]:
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
        HttpResponse[typing.Optional[MessageResponse]]
            200 response for execute_webhook
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}",
            method="POST",
            params={
                "wait": wait,
                "thread_id": thread_id,
                "with_components": with_components,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ExecuteWebhookRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[MessageResponse],
                    parse_obj_as(
                        type_=typing.Optional[MessageResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_webhook_by_token(
        self, webhook_id: SnowflakeType, webhook_token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_webhook_by_token(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        name: typing.Optional[str] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateWebhookByTokenResponse]:
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
        HttpResponse[UpdateWebhookByTokenResponse]
            200 response for update_webhook_by_token
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}",
            method="PATCH",
            json={
                "name": name,
                "avatar": avatar,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateWebhookByTokenResponse,
                    parse_obj_as(
                        type_=UpdateWebhookByTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_sticker(
        self, sticker_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetStickerResponse]:
        """
        Parameters
        ----------
        sticker_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetStickerResponse]
            200 response for get_sticker
        """
        _response = self._client_wrapper.httpx_client.request(
            f"stickers/{encode_path_param(sticker_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetStickerResponse,
                    parse_obj_as(
                        type_=GetStickerResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_webhook(
        self, webhook_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetWebhookResponse]:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetWebhookResponse]
            200 response for get_webhook
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWebhookResponse,
                    parse_obj_as(
                        type_=GetWebhookResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_webhook(
        self, webhook_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_webhook(
        self,
        webhook_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateWebhookResponse]:
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
        HttpResponse[UpdateWebhookResponse]
            200 response for update_webhook
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}",
            method="PATCH",
            json={
                "name": name,
                "avatar": avatar,
                "channel_id": channel_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateWebhookResponse,
                    parse_obj_as(
                        type_=UpdateWebhookResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_channel(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetChannelResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChannelResponse]
            200 response for get_channel
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChannelResponse,
                    parse_obj_as(
                        type_=GetChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_channel(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteChannelResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteChannelResponse]
            200 response for delete_channel
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteChannelResponse,
                    parse_obj_as(
                        type_=DeleteChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_channel(
        self,
        channel_id: SnowflakeType,
        *,
        request: UpdateChannelRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateChannelResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request : UpdateChannelRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateChannelResponse]
            200 response for update_channel
        """
        _response = self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateChannelRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateChannelResponse,
                    parse_obj_as(
                        type_=UpdateChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def invite_resolve(
        self,
        code: str,
        *,
        with_counts: typing.Optional[bool] = None,
        guild_scheduled_event_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InviteResolveResponse]:
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
        HttpResponse[InviteResolveResponse]
            200 response for invite_resolve
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invites/{encode_path_param(code)}",
            method="GET",
            params={
                "with_counts": with_counts,
                "guild_scheduled_event_id": guild_scheduled_event_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InviteResolveResponse,
                    parse_obj_as(
                        type_=InviteResolveResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def invite_revoke(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InviteRevokeResponse]:
        """
        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InviteRevokeResponse]
            200 response for invite_revoke
        """
        _response = self._client_wrapper.httpx_client.request(
            f"invites/{encode_path_param(code)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InviteRevokeResponse,
                    parse_obj_as(
                        type_=InviteRevokeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_lobby(
        self, lobby_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LobbyResponse]:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LobbyResponse]
            200 response for get_lobby
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyResponse,
                    parse_obj_as(
                        type_=LobbyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def edit_lobby(
        self,
        lobby_id: SnowflakeType,
        *,
        idle_timeout_seconds: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        members: typing.Optional[typing.Sequence[LobbyMemberRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LobbyResponse]:
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
        HttpResponse[LobbyResponse]
            200 response for edit_lobby
        """
        _response = self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}",
            method="PATCH",
            json={
                "idle_timeout_seconds": idle_timeout_seconds,
                "metadata": metadata,
                "members": convert_and_respect_annotation_metadata(
                    object_=members, annotation=typing.Optional[typing.Sequence[LobbyMemberRequest]], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyResponse,
                    parse_obj_as(
                        type_=LobbyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_guild(
        self,
        guild_id: SnowflakeType,
        *,
        with_counts: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GuildWithCountsResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        with_counts : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GuildWithCountsResponse]
            200 response for get_guild
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}",
            method="GET",
            params={
                "with_counts": with_counts,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildWithCountsResponse,
                    parse_obj_as(
                        type_=GuildWithCountsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_guild(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[GuildResponse]:
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
        HttpResponse[GuildResponse]
            200 response for update_guild
        """
        _response = self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "region": region,
                "icon": icon,
                "verification_level": verification_level,
                "default_message_notifications": default_message_notifications,
                "explicit_content_filter": explicit_content_filter,
                "preferred_locale": preferred_locale,
                "afk_timeout": afk_timeout,
                "afk_channel_id": afk_channel_id,
                "system_channel_id": system_channel_id,
                "owner_id": owner_id,
                "splash": splash,
                "banner": banner,
                "system_channel_flags": system_channel_flags,
                "features": features,
                "discovery_splash": discovery_splash,
                "home_header": home_header,
                "rules_channel_id": rules_channel_id,
                "safety_alerts_channel_id": safety_alerts_channel_id,
                "public_updates_channel_id": public_updates_channel_id,
                "premium_progress_bar_enabled": premium_progress_bar_enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildResponse,
                    parse_obj_as(
                        type_=GuildResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_user(
        self, user_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserResponse]:
        """
        Parameters
        ----------
        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserResponse]
            200 response for get_user
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserResponse,
                    parse_obj_as(
                        type_=UserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def partner_sdk_unmerge_provisional_account(
        self,
        *,
        client_id: SnowflakeType,
        external_auth_token: str,
        external_auth_type: ApplicationIdentityProviderAuthType,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "partner-sdk/provisional-accounts/unmerge",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "external_auth_token": external_auth_token,
                "external_auth_type": external_auth_type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_my_oauth2application(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PrivateApplicationResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PrivateApplicationResponse]
            200 response for get_my_oauth2_application
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth2/applications/@me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateApplicationResponse,
                    parse_obj_as(
                        type_=PrivateApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_my_connections(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ConnectedAccountResponse]]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[ConnectedAccountResponse]]]
            200 response for list_my_connections
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/@me/connections",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ConnectedAccountResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ConnectedAccountResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_dm(
        self,
        *,
        recipient_id: typing.Optional[SnowflakeType] = OMIT,
        access_tokens: typing.Optional[typing.Sequence[str]] = OMIT,
        nicks: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDmResponse]:
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
        AsyncHttpResponse[CreateDmResponse]
            200 response for create_dm
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/@me/channels",
            method="POST",
            json={
                "recipient_id": recipient_id,
                "access_tokens": access_tokens,
                "nicks": nicks,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDmResponse,
                    parse_obj_as(
                        type_=CreateDmResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_my_guilds(
        self,
        *,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        with_counts: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[MyGuildResponse]]]:
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
        AsyncHttpResponse[typing.Optional[typing.List[MyGuildResponse]]]
            200 response for list_my_guilds
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/@me/guilds",
            method="GET",
            params={
                "before": before,
                "after": after,
                "limit": limit,
                "with_counts": with_counts,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[MyGuildResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[MyGuildResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_my_application(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PrivateApplicationResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PrivateApplicationResponse]
            200 response for get_my_application
        """
        _response = await self._client_wrapper.httpx_client.request(
            "applications/@me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateApplicationResponse,
                    parse_obj_as(
                        type_=PrivateApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[PrivateApplicationResponse]:
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
        AsyncHttpResponse[PrivateApplicationResponse]
            200 response for update_my_application
        """
        _response = await self._client_wrapper.httpx_client.request(
            "applications/@me",
            method="PATCH",
            json={
                "description": convert_and_respect_annotation_metadata(
                    object_=description,
                    annotation=typing.Optional[ApplicationFormPartialDescription],
                    direction="write",
                ),
                "icon": icon,
                "cover_image": cover_image,
                "team_id": team_id,
                "flags": flags,
                "interactions_endpoint_url": interactions_endpoint_url,
                "explicit_content_filter": explicit_content_filter,
                "max_participants": max_participants,
                "type": type,
                "tags": tags,
                "custom_install_url": custom_install_url,
                "install_params": convert_and_respect_annotation_metadata(
                    object_=install_params,
                    annotation=typing.Optional[ApplicationOAuth2InstallParams],
                    direction="write",
                ),
                "role_connections_verification_url": role_connections_verification_url,
                "integration_types_config": convert_and_respect_annotation_metadata(
                    object_=integration_types_config,
                    annotation=typing.Optional[
                        typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]
                    ],
                    direction="write",
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateApplicationResponse,
                    parse_obj_as(
                        type_=PrivateApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def partner_sdk_token(
        self,
        *,
        client_id: SnowflakeType,
        external_auth_token: str,
        external_auth_type: ApplicationIdentityProviderAuthType,
        client_secret: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProvisionalTokenResponse]:
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
        AsyncHttpResponse[ProvisionalTokenResponse]
            200 response for partner_sdk_token
        """
        _response = await self._client_wrapper.httpx_client.request(
            "partner-sdk/token",
            method="POST",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "external_auth_token": external_auth_token,
                "external_auth_type": external_auth_type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisionalTokenResponse,
                    parse_obj_as(
                        type_=ProvisionalTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_bot_gateway(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GatewayBotResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GatewayBotResponse]
            200 response for get_bot_gateway
        """
        _response = await self._client_wrapper.httpx_client.request(
            "gateway/bot",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GatewayBotResponse,
                    parse_obj_as(
                        type_=GatewayBotResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_openid_connect_userinfo(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OAuth2GetOpenIdConnectUserInfoResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OAuth2GetOpenIdConnectUserInfoResponse]
            200 response for get_openid_connect_userinfo
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth2/userinfo",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OAuth2GetOpenIdConnectUserInfoResponse,
                    parse_obj_as(
                        type_=OAuth2GetOpenIdConnectUserInfoResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_public_keys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OAuth2GetKeys]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OAuth2GetKeys]
            200 response for get_public_keys
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth2/keys",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OAuth2GetKeys,
                    parse_obj_as(
                        type_=OAuth2GetKeys,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_my_oauth2authorization(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OAuth2GetAuthorizationResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OAuth2GetAuthorizationResponse]
            200 response for get_my_oauth2_authorization
        """
        _response = await self._client_wrapper.httpx_client.request(
            "oauth2/@me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OAuth2GetAuthorizationResponse,
                    parse_obj_as(
                        type_=OAuth2GetAuthorizationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_voice_regions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[VoiceRegionResponse]]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[VoiceRegionResponse]]]
            200 response for list_voice_regions
        """
        _response = await self._client_wrapper.httpx_client.request(
            "voice/regions",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[VoiceRegionResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[VoiceRegionResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_my_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserPiiResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserPiiResponse]
            200 response for get_my_user
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/@me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserPiiResponse,
                    parse_obj_as(
                        type_=UserPiiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_my_user(
        self,
        *,
        username: str,
        avatar: typing.Optional[str] = OMIT,
        banner: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserPiiResponse]:
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
        AsyncHttpResponse[UserPiiResponse]
            200 response for update_my_user
        """
        _response = await self._client_wrapper.httpx_client.request(
            "users/@me",
            method="PATCH",
            json={
                "username": username,
                "avatar": avatar,
                "banner": banner,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserPiiResponse,
                    parse_obj_as(
                        type_=UserPiiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_soundboard_default_sounds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[SoundboardSoundResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[SoundboardSoundResponse]]
            200 response for get_soundboard_default_sounds
        """
        _response = await self._client_wrapper.httpx_client.request(
            "soundboard-default-sounds",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SoundboardSoundResponse],
                    parse_obj_as(
                        type_=typing.List[SoundboardSoundResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_stage_instance(
        self,
        *,
        topic: str,
        channel_id: SnowflakeType,
        privacy_level: typing.Optional[StageInstancesPrivacyLevels] = OMIT,
        guild_scheduled_event_id: typing.Optional[SnowflakeType] = OMIT,
        send_start_notification: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StageInstanceResponse]:
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
        AsyncHttpResponse[StageInstanceResponse]
            200 response for create_stage_instance
        """
        _response = await self._client_wrapper.httpx_client.request(
            "stage-instances",
            method="POST",
            json={
                "topic": topic,
                "channel_id": channel_id,
                "privacy_level": privacy_level,
                "guild_scheduled_event_id": guild_scheduled_event_id,
                "send_start_notification": send_start_notification,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StageInstanceResponse,
                    parse_obj_as(
                        type_=StageInstanceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_sticker_packs(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StickerPackCollectionResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StickerPackCollectionResponse]
            200 response for list_sticker_packs
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sticker-packs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StickerPackCollectionResponse,
                    parse_obj_as(
                        type_=StickerPackCollectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_gateway(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GatewayResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GatewayResponse]
            200 response for get_gateway
        """
        _response = await self._client_wrapper.httpx_client.request(
            "gateway",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GatewayResponse,
                    parse_obj_as(
                        type_=GatewayResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_lobby(
        self,
        *,
        idle_timeout_seconds: typing.Optional[int] = OMIT,
        members: typing.Optional[typing.Sequence[LobbyMemberRequest]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LobbyResponse]:
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
        AsyncHttpResponse[LobbyResponse]
            201 response for create_lobby
        """
        _response = await self._client_wrapper.httpx_client.request(
            "lobbies",
            method="POST",
            json={
                "idle_timeout_seconds": idle_timeout_seconds,
                "members": convert_and_respect_annotation_metadata(
                    object_=members, annotation=typing.Optional[typing.Sequence[LobbyMemberRequest]], direction="write"
                ),
                "metadata": metadata,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyResponse,
                    parse_obj_as(
                        type_=LobbyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_or_join_lobby(
        self,
        *,
        secret: str,
        idle_timeout_seconds: typing.Optional[int] = OMIT,
        lobby_metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        member_metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LobbyResponse]:
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
        AsyncHttpResponse[LobbyResponse]
            200 response for create_or_join_lobby
        """
        _response = await self._client_wrapper.httpx_client.request(
            "lobbies",
            method="PUT",
            json={
                "idle_timeout_seconds": idle_timeout_seconds,
                "lobby_metadata": lobby_metadata,
                "member_metadata": member_metadata,
                "secret": secret,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyResponse,
                    parse_obj_as(
                        type_=LobbyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[GuildResponse]:
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
        AsyncHttpResponse[GuildResponse]
            201 response for create_guild
        """
        _response = await self._client_wrapper.httpx_client.request(
            "guilds",
            method="POST",
            json={
                "description": description,
                "name": name,
                "region": region,
                "icon": icon,
                "verification_level": verification_level,
                "default_message_notifications": default_message_notifications,
                "explicit_content_filter": explicit_content_filter,
                "preferred_locale": preferred_locale,
                "afk_timeout": afk_timeout,
                "roles": convert_and_respect_annotation_metadata(
                    object_=roles,
                    annotation=typing.Optional[typing.Sequence[CreateGuildRequestRoleItem]],
                    direction="write",
                ),
                "channels": convert_and_respect_annotation_metadata(
                    object_=channels,
                    annotation=typing.Optional[typing.Sequence[CreateGuildRequestChannelItem]],
                    direction="write",
                ),
                "afk_channel_id": afk_channel_id,
                "system_channel_id": system_channel_id,
                "system_channel_flags": system_channel_flags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildResponse,
                    parse_obj_as(
                        type_=GuildResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_my_private_archived_threads(
        self,
        channel_id: SnowflakeType,
        *,
        before: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThreadsResponse]:
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
        AsyncHttpResponse[ThreadsResponse]
            200 response for list_my_private_archived_threads
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/users/@me/threads/archived/private",
            method="GET",
            params={
                "before": before,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadsResponse,
                    parse_obj_as(
                        type_=ThreadsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_application_command_permissions(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[CommandPermissionsResponse]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CommandPermissionsResponse]]
            200 response for list_guild_application_command_permissions
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands/permissions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CommandPermissionsResponse],
                    parse_obj_as(
                        type_=typing.List[CommandPermissionsResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_application_command_permissions(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CommandPermissionsResponse]:
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
        AsyncHttpResponse[CommandPermissionsResponse]
            200 response for get_guild_application_command_permissions
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands/{encode_path_param(command_id)}/permissions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CommandPermissionsResponse,
                    parse_obj_as(
                        type_=CommandPermissionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_guild_application_command_permissions(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        permissions: typing.Optional[typing.Sequence[ApplicationCommandPermission]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CommandPermissionsResponse]:
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
        AsyncHttpResponse[CommandPermissionsResponse]
            200 response for set_guild_application_command_permissions
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands/{encode_path_param(command_id)}/permissions",
            method="PUT",
            json={
                "permissions": convert_and_respect_annotation_metadata(
                    object_=permissions,
                    annotation=typing.Optional[typing.Sequence[ApplicationCommandPermission]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CommandPermissionsResponse,
                    parse_obj_as(
                        type_=CommandPermissionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_my_message_reaction(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/reactions/{encode_path_param(emoji_name)}/@me",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_my_message_reaction(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/reactions/{encode_path_param(emoji_name)}/@me",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_private_archived_threads(
        self,
        channel_id: SnowflakeType,
        *,
        before: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThreadsResponse]:
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
        AsyncHttpResponse[ThreadsResponse]
            200 response for list_private_archived_threads
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/threads/archived/private",
            method="GET",
            params={
                "before": serialize_datetime(before) if before is not None else None,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadsResponse,
                    parse_obj_as(
                        type_=ThreadsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_public_archived_threads(
        self,
        channel_id: SnowflakeType,
        *,
        before: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThreadsResponse]:
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
        AsyncHttpResponse[ThreadsResponse]
            200 response for list_public_archived_threads
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/threads/archived/public",
            method="GET",
            params={
                "before": serialize_datetime(before) if before is not None else None,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadsResponse,
                    parse_obj_as(
                        type_=ThreadsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_application_user_role_connection(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApplicationUserRoleConnectionResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApplicationUserRoleConnectionResponse]
            200 response for get_application_user_role_connection
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/@me/applications/{encode_path_param(application_id)}/role-connection",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationUserRoleConnectionResponse,
                    parse_obj_as(
                        type_=ApplicationUserRoleConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_application_user_role_connection(
        self,
        application_id: SnowflakeType,
        *,
        platform_name: typing.Optional[str] = OMIT,
        platform_username: typing.Optional[str] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApplicationUserRoleConnectionResponse]:
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
        AsyncHttpResponse[ApplicationUserRoleConnectionResponse]
            200 response for update_application_user_role_connection
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/@me/applications/{encode_path_param(application_id)}/role-connection",
            method="PUT",
            json={
                "platform_name": platform_name,
                "platform_username": platform_username,
                "metadata": metadata,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationUserRoleConnectionResponse,
                    parse_obj_as(
                        type_=ApplicationUserRoleConnectionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_application_user_role_connection(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/@me/applications/{encode_path_param(application_id)}/role-connection",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_my_guild_member(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PrivateGuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PrivateGuildMemberResponse]
            200 response for get_my_guild_member
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/@me/guilds/{encode_path_param(guild_id)}/member",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateGuildMemberResponse,
                    parse_obj_as(
                        type_=PrivateGuildMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_application_role_connections_metadata(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]]
            200 response for get_application_role_connections_metadata
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/role-connections/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_application_role_connections_metadata(
        self,
        application_id: SnowflakeType,
        *,
        request: typing.Optional[typing.Sequence[ApplicationRoleConnectionsMetadataItemRequest]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request : typing.Optional[typing.Sequence[ApplicationRoleConnectionsMetadataItemRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]]]
            200 response for update_application_role_connections_metadata
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/role-connections/metadata",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Optional[typing.Sequence[ApplicationRoleConnectionsMetadataItemRequest]],
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ApplicationRoleConnectionsMetadataItemResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def consume_entitlement(
        self,
        application_id: SnowflakeType,
        entitlement_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        entitlement_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/entitlements/{encode_path_param(entitlement_id)}/consume",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_application_command(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApplicationCommandResponse]:
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
        AsyncHttpResponse[ApplicationCommandResponse]
            200 response for get_guild_application_command
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands/{encode_path_param(command_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationCommandResponse,
                    parse_obj_as(
                        type_=ApplicationCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_guild_application_command(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands/{encode_path_param(command_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ApplicationCommandResponse]:
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
        AsyncHttpResponse[ApplicationCommandResponse]
            200 response for update_guild_application_command
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands/{encode_path_param(command_id)}",
            method="PATCH",
            json={
                "name": name,
                "name_localizations": name_localizations,
                "description": description,
                "description_localizations": description_localizations,
                "options": convert_and_respect_annotation_metadata(
                    object_=options,
                    annotation=typing.Optional[typing.Sequence[ApplicationCommandPatchRequestPartialOptionsItem]],
                    direction="write",
                ),
                "default_member_permissions": default_member_permissions,
                "dm_permission": dm_permission,
                "contexts": contexts,
                "integration_types": integration_types,
                "handler": handler,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationCommandResponse,
                    parse_obj_as(
                        type_=ApplicationCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_application_commands(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        with_localizations: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]:
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
        AsyncHttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]
            200 response for list_guild_application_commands
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands",
            method="GET",
            params={
                "with_localizations": with_localizations,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ApplicationCommandResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ApplicationCommandResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ApplicationCommandResponse]:
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
        AsyncHttpResponse[ApplicationCommandResponse]
            200 response for create_guild_application_command
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands",
            method="POST",
            json={
                "name": name,
                "name_localizations": name_localizations,
                "description": description,
                "description_localizations": description_localizations,
                "options": convert_and_respect_annotation_metadata(
                    object_=options,
                    annotation=typing.Optional[typing.Sequence[ApplicationCommandCreateRequestOptionsItem]],
                    direction="write",
                ),
                "default_member_permissions": default_member_permissions,
                "dm_permission": dm_permission,
                "contexts": contexts,
                "integration_types": integration_types,
                "handler": handler,
                "type": type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationCommandResponse,
                    parse_obj_as(
                        type_=ApplicationCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bulk_set_guild_application_commands(
        self,
        application_id: SnowflakeType,
        guild_id: SnowflakeType,
        *,
        request: typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]:
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
        AsyncHttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]
            200 response for bulk_set_guild_application_commands
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/guilds/{encode_path_param(guild_id)}/commands",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]],
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ApplicationCommandResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ApplicationCommandResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def join_thread(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/thread-members/@me",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def leave_thread(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/thread-members/@me",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bulk_delete_messages(
        self,
        channel_id: SnowflakeType,
        *,
        messages: typing.Sequence[SnowflakeType],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        messages : typing.Sequence[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/bulk-delete",
            method="POST",
            json={
                "messages": messages,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_user_message_reaction(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/reactions/{encode_path_param(emoji_name)}/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.List[UserResponse]]:
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
        AsyncHttpResponse[typing.List[UserResponse]]
            200 response for list_message_reactions_by_emoji
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/reactions/{encode_path_param(emoji_name)}",
            method="GET",
            params={
                "after": after,
                "limit": limit,
                "type": type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[UserResponse],
                    parse_obj_as(
                        type_=typing.List[UserResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_all_message_reactions_by_emoji(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        emoji_name: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/reactions/{encode_path_param(emoji_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_all_message_reactions(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/reactions",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def crosspost_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MessageResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessageResponse]
            200 response for crosspost_message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/crosspost",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_thread_from_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        name: str,
        auto_archive_duration: typing.Optional[ThreadAutoArchiveDuration] = OMIT,
        rate_limit_per_user: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThreadResponse]:
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
        AsyncHttpResponse[ThreadResponse]
            201 response for create_thread_from_message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}/threads",
            method="POST",
            json={
                "name": name,
                "auto_archive_duration": auto_archive_duration,
                "rate_limit_per_user": rate_limit_per_user,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadResponse,
                    parse_obj_as(
                        type_=ThreadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ThreadSearchResponse]:
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
        AsyncHttpResponse[ThreadSearchResponse]
            200 response for thread_search
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/threads/search",
            method="GET",
            params={
                "name": name,
                "slop": slop,
                "min_id": min_id,
                "max_id": max_id,
                "tag": convert_and_respect_annotation_metadata(
                    object_=tag, annotation=ThreadSearchRequestTag, direction="write"
                ),
                "tag_setting": tag_setting,
                "archived": archived,
                "sort_by": sort_by,
                "sort_order": sort_order,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadSearchResponse,
                    parse_obj_as(
                        type_=ThreadSearchResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_answer_voters(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        answer_id: int,
        *,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PollAnswerDetailsResponse]:
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
        AsyncHttpResponse[PollAnswerDetailsResponse]
            200 response for get_answer_voters
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/polls/{encode_path_param(message_id)}/answers/{encode_path_param(answer_id)}",
            method="GET",
            params={
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PollAnswerDetailsResponse,
                    parse_obj_as(
                        type_=PollAnswerDetailsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def poll_expire(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MessageResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessageResponse]
            200 response for poll_expire
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/polls/{encode_path_param(message_id)}/expire",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_original_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MessageResponse]:
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
        AsyncHttpResponse[MessageResponse]
            200 response for get_original_webhook_message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/messages/@original",
            method="GET",
            params={
                "thread_id": thread_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_original_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/messages/@original",
            method="DELETE",
            params={
                "thread_id": thread_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[MessageResponse]:
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
        AsyncHttpResponse[MessageResponse]
            200 response for update_original_webhook_message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/messages/@original",
            method="PATCH",
            params={
                "thread_id": thread_id,
                "with_components": with_components,
            },
            json={
                "content": content,
                "embeds": convert_and_respect_annotation_metadata(
                    object_=embeds, annotation=typing.Optional[typing.Sequence[RichEmbed]], direction="write"
                ),
                "allowed_mentions": convert_and_respect_annotation_metadata(
                    object_=allowed_mentions,
                    annotation=typing.Optional[MessageAllowedMentionsRequest],
                    direction="write",
                ),
                "components": convert_and_respect_annotation_metadata(
                    object_=components,
                    annotation=typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]],
                    direction="write",
                ),
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments,
                    annotation=typing.Optional[typing.Sequence[MessageAttachmentRequest]],
                    direction="write",
                ),
                "poll": convert_and_respect_annotation_metadata(
                    object_=poll, annotation=typing.Optional[PollCreateRequest], direction="write"
                ),
                "flags": flags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def leave_lobby(
        self, lobby_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}/members/@me",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ScheduledEventUserResponse]]]:
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
        AsyncHttpResponse[typing.Optional[typing.List[ScheduledEventUserResponse]]]
            200 response for list_guild_scheduled_event_users
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/scheduled-events/{encode_path_param(guild_scheduled_event_id)}/users",
            method="GET",
            params={
                "with_member": with_member,
                "limit": limit,
                "before": before,
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ScheduledEventUserResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ScheduledEventUserResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        rule_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetAutoModerationRuleResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        rule_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAutoModerationRuleResponse]
            200 response for get_auto_moderation_rule
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/auto-moderation/rules/{encode_path_param(rule_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAutoModerationRuleResponse,
                    parse_obj_as(
                        type_=GetAutoModerationRuleResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        rule_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        rule_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/auto-moderation/rules/{encode_path_param(rule_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        rule_id: SnowflakeType,
        *,
        request: UpdateAutoModerationRuleRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateAutoModerationRuleResponse]:
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
        AsyncHttpResponse[UpdateAutoModerationRuleResponse]
            200 response for update_auto_moderation_rule
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/auto-moderation/rules/{encode_path_param(rule_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateAutoModerationRuleRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateAutoModerationRuleResponse,
                    parse_obj_as(
                        type_=UpdateAutoModerationRuleResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_auto_moderation_rules(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[typing.Optional[ListAutoModerationRulesResponseItem]]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[typing.Optional[ListAutoModerationRulesResponseItem]]]]
            200 response for list_auto_moderation_rules
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/auto-moderation/rules",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[typing.Optional[ListAutoModerationRulesResponseItem]]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[typing.Optional[ListAutoModerationRulesResponseItem]]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_auto_moderation_rule(
        self,
        guild_id: SnowflakeType,
        *,
        request: CreateAutoModerationRuleRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateAutoModerationRuleResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : CreateAutoModerationRuleRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateAutoModerationRuleResponse]
            200 response for create_auto_moderation_rule
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/auto-moderation/rules",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateAutoModerationRuleRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateAutoModerationRuleResponse,
                    parse_obj_as(
                        type_=CreateAutoModerationRuleResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_self_voice_state(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VoiceStateResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceStateResponse]
            200 response for get_self_voice_state
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/voice-states/@me",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceStateResponse,
                    parse_obj_as(
                        type_=VoiceStateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_self_voice_state(
        self,
        guild_id: SnowflakeType,
        *,
        request_to_speak_timestamp: typing.Optional[dt.datetime] = OMIT,
        suppress: typing.Optional[bool] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/voice-states/@me",
            method="PATCH",
            json={
                "request_to_speak_timestamp": request_to_speak_timestamp,
                "suppress": suppress,
                "channel_id": channel_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_guild_members(
        self,
        guild_id: SnowflakeType,
        *,
        limit: int,
        query: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GuildMemberResponse]]:
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
        AsyncHttpResponse[typing.List[GuildMemberResponse]]
            200 response for search_guild_members
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/search",
            method="GET",
            params={
                "limit": limit,
                "query": query,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GuildMemberResponse],
                    parse_obj_as(
                        type_=typing.List[GuildMemberResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_active_guild_threads(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ThreadsResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ThreadsResponse]
            200 response for get_active_guild_threads
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/threads/active",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadsResponse,
                    parse_obj_as(
                        type_=ThreadsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_my_guild_member(
        self,
        guild_id: SnowflakeType,
        *,
        nick: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PrivateGuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        nick : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PrivateGuildMemberResponse]
            200 response for update_my_guild_member
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/@me",
            method="PATCH",
            json={
                "nick": nick,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateGuildMemberResponse,
                    parse_obj_as(
                        type_=PrivateGuildMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_guild_member_role(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/{encode_path_param(user_id)}/roles/{encode_path_param(role_id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_guild_member_role(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/{encode_path_param(user_id)}/roles/{encode_path_param(role_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def leave_guild(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/@me/guilds/{encode_path_param(guild_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def applications_get_activity_instance(
        self,
        application_id: SnowflakeType,
        instance_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmbeddedActivityInstance]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        instance_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmbeddedActivityInstance]
            200 response for applications_get_activity_instance
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/activity-instances/{encode_path_param(instance_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmbeddedActivityInstance,
                    parse_obj_as(
                        type_=EmbeddedActivityInstance,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_entitlement(
        self,
        application_id: SnowflakeType,
        entitlement_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntitlementResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        entitlement_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntitlementResponse]
            200 response for get_entitlement
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/entitlements/{encode_path_param(entitlement_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntitlementResponse,
                    parse_obj_as(
                        type_=EntitlementResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_entitlement(
        self,
        application_id: SnowflakeType,
        entitlement_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        entitlement_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/entitlements/{encode_path_param(entitlement_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.List[typing.Optional[EntitlementResponse]]]:
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
        AsyncHttpResponse[typing.List[typing.Optional[EntitlementResponse]]]
            200 response for get_entitlements
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/entitlements",
            method="GET",
            params={
                "user_id": user_id,
                "sku_ids": convert_and_respect_annotation_metadata(
                    object_=sku_ids, annotation=GetEntitlementsRequestSkuIds, direction="write"
                ),
                "guild_id": guild_id,
                "before": before,
                "after": after,
                "limit": limit,
                "exclude_ended": exclude_ended,
                "exclude_deleted": exclude_deleted,
                "only_active": only_active,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[typing.Optional[EntitlementResponse]],
                    parse_obj_as(
                        type_=typing.List[typing.Optional[EntitlementResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_entitlement(
        self,
        application_id: SnowflakeType,
        *,
        sku_id: SnowflakeType,
        owner_id: SnowflakeType,
        owner_type: EntitlementOwnerTypes,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntitlementResponse]:
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
        AsyncHttpResponse[EntitlementResponse]
            200 response for create_entitlement
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/entitlements",
            method="POST",
            json={
                "sku_id": sku_id,
                "owner_id": owner_id,
                "owner_type": owner_type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntitlementResponse,
                    parse_obj_as(
                        type_=EntitlementResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def upload_application_attachment(
        self, application_id: SnowflakeType, *, file: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ActivitiesAttachmentResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        file : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ActivitiesAttachmentResponse]
            200 response for upload_application_attachment
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/attachment",
            method="POST",
            data={
                "file": file,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ActivitiesAttachmentResponse,
                    parse_obj_as(
                        type_=ActivitiesAttachmentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_application_command(
        self,
        application_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApplicationCommandResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApplicationCommandResponse]
            200 response for get_application_command
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/commands/{encode_path_param(command_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationCommandResponse,
                    parse_obj_as(
                        type_=ApplicationCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_application_command(
        self,
        application_id: SnowflakeType,
        command_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        command_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/commands/{encode_path_param(command_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ApplicationCommandResponse]:
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
        AsyncHttpResponse[ApplicationCommandResponse]
            200 response for update_application_command
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/commands/{encode_path_param(command_id)}",
            method="PATCH",
            json={
                "name": name,
                "name_localizations": name_localizations,
                "description": description,
                "description_localizations": description_localizations,
                "options": convert_and_respect_annotation_metadata(
                    object_=options,
                    annotation=typing.Optional[typing.Sequence[ApplicationCommandPatchRequestPartialOptionsItem]],
                    direction="write",
                ),
                "default_member_permissions": default_member_permissions,
                "dm_permission": dm_permission,
                "contexts": contexts,
                "integration_types": integration_types,
                "handler": handler,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationCommandResponse,
                    parse_obj_as(
                        type_=ApplicationCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_application_commands(
        self,
        application_id: SnowflakeType,
        *,
        with_localizations: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        with_localizations : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]
            200 response for list_application_commands
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/commands",
            method="GET",
            params={
                "with_localizations": with_localizations,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ApplicationCommandResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ApplicationCommandResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ApplicationCommandResponse]:
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
        AsyncHttpResponse[ApplicationCommandResponse]
            200 response for create_application_command
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/commands",
            method="POST",
            json={
                "name": name,
                "name_localizations": name_localizations,
                "description": description,
                "description_localizations": description_localizations,
                "options": convert_and_respect_annotation_metadata(
                    object_=options,
                    annotation=typing.Optional[typing.Sequence[ApplicationCommandCreateRequestOptionsItem]],
                    direction="write",
                ),
                "default_member_permissions": default_member_permissions,
                "dm_permission": dm_permission,
                "contexts": contexts,
                "integration_types": integration_types,
                "handler": handler,
                "type": type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationCommandResponse,
                    parse_obj_as(
                        type_=ApplicationCommandResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bulk_set_application_commands(
        self,
        application_id: SnowflakeType,
        *,
        request: typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request : typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[ApplicationCommandResponse]]]
            200 response for bulk_set_application_commands
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/commands",
            method="PUT",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Optional[typing.Sequence[ApplicationCommandUpdateRequest]],
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ApplicationCommandResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ApplicationCommandResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_application_emoji(
        self,
        application_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmojiResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmojiResponse]
            200 response for get_application_emoji
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/emojis/{encode_path_param(emoji_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmojiResponse,
                    parse_obj_as(
                        type_=EmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_application_emoji(
        self,
        application_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/emojis/{encode_path_param(emoji_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_application_emoji(
        self,
        application_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmojiResponse]:
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
        AsyncHttpResponse[EmojiResponse]
            200 response for update_application_emoji
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/emojis/{encode_path_param(emoji_id)}",
            method="PATCH",
            json={
                "name": name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmojiResponse,
                    parse_obj_as(
                        type_=EmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_application_emojis(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListApplicationEmojisResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListApplicationEmojisResponse]
            200 response for list_application_emojis
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/emojis",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListApplicationEmojisResponse,
                    parse_obj_as(
                        type_=ListApplicationEmojisResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_application_emoji(
        self,
        application_id: SnowflakeType,
        *,
        name: str,
        image: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmojiResponse]:
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
        AsyncHttpResponse[EmojiResponse]
            201 response for create_application_emoji
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}/emojis",
            method="POST",
            json={
                "name": name,
                "image": image,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmojiResponse,
                    parse_obj_as(
                        type_=EmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_interaction_response(
        self,
        interaction_id: SnowflakeType,
        interaction_token: str,
        *,
        request: CreateInteractionResponseRequestBody,
        with_response: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[InteractionCallbackResponse]]:
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
        AsyncHttpResponse[typing.Optional[InteractionCallbackResponse]]
            200 response for create_interaction_response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"interactions/{encode_path_param(interaction_id)}/{encode_path_param(interaction_token)}/callback",
            method="POST",
            params={
                "with_response": with_response,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateInteractionResponseRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[InteractionCallbackResponse],
                    parse_obj_as(
                        type_=typing.Optional[InteractionCallbackResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def send_soundboard_sound(
        self,
        channel_id: SnowflakeType,
        *,
        sound_id: SnowflakeType,
        source_guild_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/send-soundboard-sound",
            method="POST",
            json={
                "sound_id": sound_id,
                "source_guild_id": source_guild_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_thread_member(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        with_member: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThreadMemberResponse]:
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
        AsyncHttpResponse[ThreadMemberResponse]
            200 response for get_thread_member
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/thread-members/{encode_path_param(user_id)}",
            method="GET",
            params={
                "with_member": with_member,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadMemberResponse,
                    parse_obj_as(
                        type_=ThreadMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_thread_member(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/thread-members/{encode_path_param(user_id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_thread_member(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/thread-members/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_thread_members(
        self,
        channel_id: SnowflakeType,
        *,
        with_member: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ThreadMemberResponse]]:
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
        AsyncHttpResponse[typing.List[ThreadMemberResponse]]
            200 response for list_thread_members
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/thread-members",
            method="GET",
            params={
                "with_member": with_member,
                "limit": limit,
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ThreadMemberResponse],
                    parse_obj_as(
                        type_=typing.List[ThreadMemberResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_channel_permission_overwrite(
        self,
        channel_id: SnowflakeType,
        overwrite_id: SnowflakeType,
        *,
        type: typing.Optional[ChannelPermissionOverwrites] = OMIT,
        allow: typing.Optional[int] = OMIT,
        deny: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/permissions/{encode_path_param(overwrite_id)}",
            method="PUT",
            json={
                "type": type,
                "allow": allow,
                "deny": deny,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_channel_permission_overwrite(
        self,
        channel_id: SnowflakeType,
        overwrite_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        overwrite_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/permissions/{encode_path_param(overwrite_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_group_dm_user(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        access_token: typing.Optional[str] = OMIT,
        nick: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[AddGroupDmUserResponse]]:
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
        AsyncHttpResponse[typing.Optional[AddGroupDmUserResponse]]
            201 response for add_group_dm_user
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/recipients/{encode_path_param(user_id)}",
            method="PUT",
            json={
                "access_token": access_token,
                "nick": nick,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[AddGroupDmUserResponse],
                    parse_obj_as(
                        type_=typing.Optional[AddGroupDmUserResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_group_dm_user(
        self,
        channel_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/recipients/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_channel(
        self,
        channel_id: SnowflakeType,
        *,
        webhook_channel_id: SnowflakeType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChannelFollowerResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        webhook_channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChannelFollowerResponse]
            200 response for follow_channel
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/followers",
            method="POST",
            json={
                "webhook_channel_id": webhook_channel_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChannelFollowerResponse,
                    parse_obj_as(
                        type_=ChannelFollowerResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MessageResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessageResponse]
            200 response for get_message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[MessageResponse]:
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
        AsyncHttpResponse[MessageResponse]
            200 response for update_message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages/{encode_path_param(message_id)}",
            method="PATCH",
            json={
                "content": content,
                "embeds": convert_and_respect_annotation_metadata(
                    object_=embeds, annotation=typing.Optional[typing.Sequence[RichEmbed]], direction="write"
                ),
                "flags": flags,
                "allowed_mentions": convert_and_respect_annotation_metadata(
                    object_=allowed_mentions,
                    annotation=typing.Optional[MessageAllowedMentionsRequest],
                    direction="write",
                ),
                "sticker_ids": sticker_ids,
                "components": convert_and_respect_annotation_metadata(
                    object_=components,
                    annotation=typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]],
                    direction="write",
                ),
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments,
                    annotation=typing.Optional[typing.Sequence[MessageAttachmentRequest]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_messages(
        self,
        channel_id: SnowflakeType,
        *,
        around: typing.Optional[SnowflakeType] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[MessageResponse]]]:
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
        AsyncHttpResponse[typing.Optional[typing.List[MessageResponse]]]
            200 response for list_messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages",
            method="GET",
            params={
                "around": around,
                "before": before,
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[MessageResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[MessageResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[MessageResponse]:
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
        AsyncHttpResponse[MessageResponse]
            200 response for create_message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/messages",
            method="POST",
            json={
                "content": content,
                "embeds": convert_and_respect_annotation_metadata(
                    object_=embeds, annotation=typing.Optional[typing.Sequence[RichEmbed]], direction="write"
                ),
                "allowed_mentions": convert_and_respect_annotation_metadata(
                    object_=allowed_mentions,
                    annotation=typing.Optional[MessageAllowedMentionsRequest],
                    direction="write",
                ),
                "sticker_ids": sticker_ids,
                "components": convert_and_respect_annotation_metadata(
                    object_=components,
                    annotation=typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]],
                    direction="write",
                ),
                "flags": flags,
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments,
                    annotation=typing.Optional[typing.Sequence[MessageAttachmentRequest]],
                    direction="write",
                ),
                "poll": convert_and_respect_annotation_metadata(
                    object_=poll, annotation=typing.Optional[PollCreateRequest], direction="write"
                ),
                "confetti_potion": convert_and_respect_annotation_metadata(
                    object_=confetti_potion, annotation=typing.Optional[ConfettiPotionCreateRequest], direction="write"
                ),
                "message_reference": convert_and_respect_annotation_metadata(
                    object_=message_reference, annotation=typing.Optional[MessageReferenceRequest], direction="write"
                ),
                "nonce": convert_and_respect_annotation_metadata(
                    object_=nonce, annotation=typing.Optional[MessageCreateRequestNonce], direction="write"
                ),
                "enforce_nonce": enforce_nonce,
                "tts": tts,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_channel_webhooks(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ListChannelWebhooksResponseItem]]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[ListChannelWebhooksResponseItem]]]
            200 response for list_channel_webhooks
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/webhooks",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ListChannelWebhooksResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ListChannelWebhooksResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_webhook(
        self,
        channel_id: SnowflakeType,
        *,
        name: str,
        avatar: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildIncomingWebhookResponse]:
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
        AsyncHttpResponse[GuildIncomingWebhookResponse]
            200 response for create_webhook
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/webhooks",
            method="POST",
            json={
                "name": name,
                "avatar": avatar,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildIncomingWebhookResponse,
                    parse_obj_as(
                        type_=GuildIncomingWebhookResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_channel_invites(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ListChannelInvitesResponseItem]]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[ListChannelInvitesResponseItem]]]
            200 response for list_channel_invites
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/invites",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ListChannelInvitesResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ListChannelInvitesResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_channel_invite(
        self,
        channel_id: SnowflakeType,
        *,
        request: CreateChannelInviteRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[CreateChannelInviteResponse]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request : CreateChannelInviteRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[CreateChannelInviteResponse]]
            200 response for create_channel_invite
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/invites",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateChannelInviteRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[CreateChannelInviteResponse],
                    parse_obj_as(
                        type_=typing.Optional[CreateChannelInviteResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_thread(
        self,
        channel_id: SnowflakeType,
        *,
        request: CreateThreadRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreatedThreadResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request : CreateThreadRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreatedThreadResponse]
            201 response for create_thread
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/threads",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateThreadRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreatedThreadResponse,
                    parse_obj_as(
                        type_=CreatedThreadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def trigger_typing_indicator(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[TypingIndicatorResponse]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[TypingIndicatorResponse]]
            200 response for trigger_typing_indicator
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/typing",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[TypingIndicatorResponse],
                    parse_obj_as(
                        type_=typing.Optional[TypingIndicatorResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def pin_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/pins/{encode_path_param(message_id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def unpin_message(
        self,
        channel_id: SnowflakeType,
        message_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        message_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/pins/{encode_path_param(message_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_pinned_messages(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[MessageResponse]]]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[MessageResponse]]]
            200 response for list_pinned_messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}/pins",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[MessageResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[MessageResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        message_id: SnowflakeType,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MessageResponse]:
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
        AsyncHttpResponse[MessageResponse]
            200 response for get_webhook_message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/messages/{encode_path_param(message_id)}",
            method="GET",
            params={
                "thread_id": thread_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_webhook_message(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        message_id: SnowflakeType,
        *,
        thread_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/messages/{encode_path_param(message_id)}",
            method="DELETE",
            params={
                "thread_id": thread_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[MessageResponse]:
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
        AsyncHttpResponse[MessageResponse]
            200 response for update_webhook_message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/messages/{encode_path_param(message_id)}",
            method="PATCH",
            params={
                "thread_id": thread_id,
                "with_components": with_components,
            },
            json={
                "content": content,
                "embeds": convert_and_respect_annotation_metadata(
                    object_=embeds, annotation=typing.Optional[typing.Sequence[RichEmbed]], direction="write"
                ),
                "allowed_mentions": convert_and_respect_annotation_metadata(
                    object_=allowed_mentions,
                    annotation=typing.Optional[MessageAllowedMentionsRequest],
                    direction="write",
                ),
                "components": convert_and_respect_annotation_metadata(
                    object_=components,
                    annotation=typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]],
                    direction="write",
                ),
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments,
                    annotation=typing.Optional[typing.Sequence[MessageAttachmentRequest]],
                    direction="write",
                ),
                "poll": convert_and_respect_annotation_metadata(
                    object_=poll, annotation=typing.Optional[PollCreateRequest], direction="write"
                ),
                "flags": flags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageResponse,
                    parse_obj_as(
                        type_=MessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/github",
            method="POST",
            params={
                "wait": wait,
                "thread_id": thread_id,
            },
            json={
                "action": action,
                "ref": ref,
                "ref_type": ref_type,
                "comment": convert_and_respect_annotation_metadata(
                    object_=comment, annotation=typing.Optional[GithubComment], direction="write"
                ),
                "issue": convert_and_respect_annotation_metadata(
                    object_=issue, annotation=typing.Optional[GithubIssue], direction="write"
                ),
                "pull_request": convert_and_respect_annotation_metadata(
                    object_=pull_request, annotation=typing.Optional[GithubIssue], direction="write"
                ),
                "repository": convert_and_respect_annotation_metadata(
                    object_=repository, annotation=typing.Optional[GithubRepository], direction="write"
                ),
                "forkee": convert_and_respect_annotation_metadata(
                    object_=forkee, annotation=typing.Optional[GithubRepository], direction="write"
                ),
                "sender": convert_and_respect_annotation_metadata(
                    object_=sender, annotation=GithubUser, direction="write"
                ),
                "member": convert_and_respect_annotation_metadata(
                    object_=member, annotation=typing.Optional[GithubUser], direction="write"
                ),
                "release": convert_and_respect_annotation_metadata(
                    object_=release, annotation=typing.Optional[GithubRelease], direction="write"
                ),
                "head_commit": convert_and_respect_annotation_metadata(
                    object_=head_commit, annotation=typing.Optional[GithubCommit], direction="write"
                ),
                "commits": convert_and_respect_annotation_metadata(
                    object_=commits, annotation=typing.Optional[typing.Sequence[GithubCommit]], direction="write"
                ),
                "forced": forced,
                "compare": compare,
                "review": convert_and_respect_annotation_metadata(
                    object_=review, annotation=typing.Optional[GithubReview], direction="write"
                ),
                "check_run": convert_and_respect_annotation_metadata(
                    object_=check_run, annotation=typing.Optional[GithubCheckRun], direction="write"
                ),
                "check_suite": convert_and_respect_annotation_metadata(
                    object_=check_suite, annotation=typing.Optional[GithubCheckSuite], direction="write"
                ),
                "discussion": convert_and_respect_annotation_metadata(
                    object_=discussion, annotation=typing.Optional[GithubDiscussion], direction="write"
                ),
                "answer": convert_and_respect_annotation_metadata(
                    object_=answer, annotation=typing.Optional[GithubComment], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.Optional[str]]:
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
        AsyncHttpResponse[typing.Optional[str]]
            200 response for execute_slack_compatible_webhook
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}/slack",
            method="POST",
            params={
                "wait": wait,
                "thread_id": thread_id,
            },
            json={
                "text": text,
                "username": username,
                "icon_url": icon_url,
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments,
                    annotation=typing.Optional[typing.Sequence[WebhookSlackEmbed]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[str],
                    parse_obj_as(
                        type_=typing.Optional[str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def edit_lobby_channel_link(
        self,
        lobby_id: SnowflakeType,
        *,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LobbyResponse]:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        channel_id : typing.Optional[SnowflakeType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LobbyResponse]
            200 response for edit_lobby_channel_link
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}/channel-linking",
            method="PATCH",
            json={
                "channel_id": channel_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyResponse,
                    parse_obj_as(
                        type_=LobbyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[LobbyMessageResponse]:
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
        AsyncHttpResponse[LobbyMessageResponse]
            201 response for create_lobby_message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}/messages",
            method="POST",
            json={
                "content": content,
                "embeds": convert_and_respect_annotation_metadata(
                    object_=embeds, annotation=typing.Optional[typing.Sequence[RichEmbed]], direction="write"
                ),
                "allowed_mentions": convert_and_respect_annotation_metadata(
                    object_=allowed_mentions,
                    annotation=typing.Optional[MessageAllowedMentionsRequest],
                    direction="write",
                ),
                "sticker_ids": sticker_ids,
                "components": convert_and_respect_annotation_metadata(
                    object_=components,
                    annotation=typing.Optional[typing.Sequence[ActionRowComponentForMessageRequest]],
                    direction="write",
                ),
                "flags": flags,
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments,
                    annotation=typing.Optional[typing.Sequence[MessageAttachmentRequest]],
                    direction="write",
                ),
                "poll": convert_and_respect_annotation_metadata(
                    object_=poll, annotation=typing.Optional[PollCreateRequest], direction="write"
                ),
                "confetti_potion": convert_and_respect_annotation_metadata(
                    object_=confetti_potion, annotation=typing.Optional[ConfettiPotionCreateRequest], direction="write"
                ),
                "message_reference": convert_and_respect_annotation_metadata(
                    object_=message_reference, annotation=typing.Optional[MessageReferenceRequest], direction="write"
                ),
                "nonce": convert_and_respect_annotation_metadata(
                    object_=nonce, annotation=typing.Optional[SdkMessageRequestNonce], direction="write"
                ),
                "enforce_nonce": enforce_nonce,
                "tts": tts,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyMessageResponse,
                    parse_obj_as(
                        type_=LobbyMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_lobby_member(
        self,
        lobby_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        flags: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LobbyMemberResponse]:
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
        AsyncHttpResponse[LobbyMemberResponse]
            200 response for add_lobby_member
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}/members/{encode_path_param(user_id)}",
            method="PUT",
            json={
                "metadata": metadata,
                "flags": flags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyMemberResponse,
                    parse_obj_as(
                        type_=LobbyMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_lobby_member(
        self,
        lobby_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}/members/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_template(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GuildTemplateResponse]:
        """
        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GuildTemplateResponse]
            200 response for get_guild_template
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/templates/{encode_path_param(code)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildTemplateResponse,
                    parse_obj_as(
                        type_=GuildTemplateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_guild_from_template(
        self,
        code: str,
        *,
        name: str,
        icon: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildResponse]:
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
        AsyncHttpResponse[GuildResponse]
            201 response for create_guild_from_template
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/templates/{encode_path_param(code)}",
            method="POST",
            json={
                "name": name,
                "icon": icon,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildResponse,
                    parse_obj_as(
                        type_=GuildResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_new_member_welcome(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[GuildHomeSettingsResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[GuildHomeSettingsResponse]]
            200 response for get_guild_new_member_welcome
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/new-member-welcome",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[GuildHomeSettingsResponse],
                    parse_obj_as(
                        type_=typing.Optional[GuildHomeSettingsResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_soundboard_sound(
        self,
        guild_id: SnowflakeType,
        sound_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SoundboardSoundResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sound_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SoundboardSoundResponse]
            200 response for get_guild_soundboard_sound
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/soundboard-sounds/{encode_path_param(sound_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SoundboardSoundResponse,
                    parse_obj_as(
                        type_=SoundboardSoundResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_guild_soundboard_sound(
        self,
        guild_id: SnowflakeType,
        sound_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sound_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/soundboard-sounds/{encode_path_param(sound_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[SoundboardSoundResponse]:
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
        AsyncHttpResponse[SoundboardSoundResponse]
            200 response for update_guild_soundboard_sound
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/soundboard-sounds/{encode_path_param(sound_id)}",
            method="PATCH",
            json={
                "name": name,
                "volume": volume,
                "emoji_id": emoji_id,
                "emoji_name": emoji_name,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SoundboardSoundResponse,
                    parse_obj_as(
                        type_=SoundboardSoundResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_soundboard_sounds(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListGuildSoundboardSoundsResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListGuildSoundboardSoundsResponse]
            200 response for list_guild_soundboard_sounds
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/soundboard-sounds",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListGuildSoundboardSoundsResponse,
                    parse_obj_as(
                        type_=ListGuildSoundboardSoundsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[SoundboardSoundResponse]:
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
        AsyncHttpResponse[SoundboardSoundResponse]
            201 response for create_guild_soundboard_sound
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/soundboard-sounds",
            method="POST",
            json={
                "name": name,
                "volume": volume,
                "emoji_id": emoji_id,
                "emoji_name": emoji_name,
                "sound": sound,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SoundboardSoundResponse,
                    parse_obj_as(
                        type_=SoundboardSoundResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        with_user_count: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetGuildScheduledEventResponse]:
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
        AsyncHttpResponse[GetGuildScheduledEventResponse]
            200 response for get_guild_scheduled_event
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/scheduled-events/{encode_path_param(guild_scheduled_event_id)}",
            method="GET",
            params={
                "with_user_count": with_user_count,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGuildScheduledEventResponse,
                    parse_obj_as(
                        type_=GetGuildScheduledEventResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        guild_scheduled_event_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/scheduled-events/{encode_path_param(guild_scheduled_event_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        guild_scheduled_event_id: SnowflakeType,
        *,
        request: UpdateGuildScheduledEventRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateGuildScheduledEventResponse]:
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
        AsyncHttpResponse[UpdateGuildScheduledEventResponse]
            200 response for update_guild_scheduled_event
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/scheduled-events/{encode_path_param(guild_scheduled_event_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateGuildScheduledEventRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateGuildScheduledEventResponse,
                    parse_obj_as(
                        type_=UpdateGuildScheduledEventResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_scheduled_events(
        self,
        guild_id: SnowflakeType,
        *,
        with_user_count: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ListGuildScheduledEventsResponseItem]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        with_user_count : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[ListGuildScheduledEventsResponseItem]]]
            200 response for list_guild_scheduled_events
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/scheduled-events",
            method="GET",
            params={
                "with_user_count": with_user_count,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ListGuildScheduledEventsResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ListGuildScheduledEventsResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_guild_scheduled_event(
        self,
        guild_id: SnowflakeType,
        *,
        request: CreateGuildScheduledEventRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateGuildScheduledEventResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : CreateGuildScheduledEventRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateGuildScheduledEventResponse]
            200 response for create_guild_scheduled_event
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/scheduled-events",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateGuildScheduledEventRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateGuildScheduledEventResponse,
                    parse_obj_as(
                        type_=CreateGuildScheduledEventResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_welcome_screen(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GuildWelcomeScreenResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GuildWelcomeScreenResponse]
            200 response for get_guild_welcome_screen
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/welcome-screen",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildWelcomeScreenResponse,
                    parse_obj_as(
                        type_=GuildWelcomeScreenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_guild_welcome_screen(
        self,
        guild_id: SnowflakeType,
        *,
        description: typing.Optional[str] = OMIT,
        welcome_channels: typing.Optional[typing.Sequence[GuildWelcomeChannel]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildWelcomeScreenResponse]:
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
        AsyncHttpResponse[GuildWelcomeScreenResponse]
            200 response for update_guild_welcome_screen
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/welcome-screen",
            method="PATCH",
            json={
                "description": description,
                "welcome_channels": convert_and_respect_annotation_metadata(
                    object_=welcome_channels,
                    annotation=typing.Optional[typing.Sequence[GuildWelcomeChannel]],
                    direction="write",
                ),
                "enabled": enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildWelcomeScreenResponse,
                    parse_obj_as(
                        type_=GuildWelcomeScreenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_voice_state(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[VoiceStateResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VoiceStateResponse]
            200 response for get_voice_state
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/voice-states/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VoiceStateResponse,
                    parse_obj_as(
                        type_=VoiceStateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_voice_state(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        suppress: typing.Optional[bool] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/voice-states/{encode_path_param(user_id)}",
            method="PATCH",
            json={
                "suppress": suppress,
                "channel_id": channel_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_guild_integration(
        self,
        guild_id: SnowflakeType,
        integration_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        integration_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/integrations/{encode_path_param(integration_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_integrations(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ListGuildIntegrationsResponseItem]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[ListGuildIntegrationsResponseItem]]]
            200 response for list_guild_integrations
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/integrations",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ListGuildIntegrationsResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ListGuildIntegrationsResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_widget(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WidgetResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WidgetResponse]
            200 response for get_guild_widget
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/widget.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WidgetResponse,
                    parse_obj_as(
                        type_=WidgetResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guilds_onboarding(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserGuildOnboardingResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserGuildOnboardingResponse]
            200 response for get_guilds_onboarding
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/onboarding",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserGuildOnboardingResponse,
                    parse_obj_as(
                        type_=UserGuildOnboardingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def put_guilds_onboarding(
        self,
        guild_id: SnowflakeType,
        *,
        prompts: typing.Optional[typing.Sequence[UpdateOnboardingPromptRequest]] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        default_channel_ids: typing.Optional[typing.Sequence[SnowflakeType]] = OMIT,
        mode: typing.Optional[GuildOnboardingMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildOnboardingResponse]:
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
        AsyncHttpResponse[GuildOnboardingResponse]
            200 response for put_guilds_onboarding
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/onboarding",
            method="PUT",
            json={
                "prompts": convert_and_respect_annotation_metadata(
                    object_=prompts,
                    annotation=typing.Optional[typing.Sequence[UpdateOnboardingPromptRequest]],
                    direction="write",
                ),
                "enabled": enabled,
                "default_channel_ids": default_channel_ids,
                "mode": mode,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildOnboardingResponse,
                    parse_obj_as(
                        type_=GuildOnboardingResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_vanity_url(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[VanityUrlResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[VanityUrlResponse]
            200 response for get_guild_vanity_url
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/vanity-url",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    VanityUrlResponse,
                    parse_obj_as(
                        type_=VanityUrlResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[GuildAuditLogResponse]:
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
        AsyncHttpResponse[GuildAuditLogResponse]
            200 response for list_guild_audit_log_entries
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/audit-logs",
            method="GET",
            params={
                "user_id": user_id,
                "target_id": target_id,
                "action_type": action_type,
                "before": before,
                "after": after,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildAuditLogResponse,
                    parse_obj_as(
                        type_=GuildAuditLogResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def get_guild_widget_png(
        self,
        guild_id: SnowflakeType,
        *,
        style: typing.Optional[WidgetImageStyles] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        style : typing.Optional[WidgetImageStyles]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            200 response for get_guild_widget_png
        """
        async with self._client_wrapper.httpx_client.stream(
            f"guilds/{encode_path_param(guild_id)}/widget.png",
            method="GET",
            params={
                "style": style,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def sync_guild_template(
        self, guild_id: SnowflakeType, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GuildTemplateResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GuildTemplateResponse]
            200 response for sync_guild_template
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/templates/{encode_path_param(code)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildTemplateResponse,
                    parse_obj_as(
                        type_=GuildTemplateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_guild_template(
        self, guild_id: SnowflakeType, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GuildTemplateResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GuildTemplateResponse]
            200 response for delete_guild_template
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/templates/{encode_path_param(code)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildTemplateResponse,
                    parse_obj_as(
                        type_=GuildTemplateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_guild_template(
        self,
        guild_id: SnowflakeType,
        code: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildTemplateResponse]:
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
        AsyncHttpResponse[GuildTemplateResponse]
            200 response for update_guild_template
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/templates/{encode_path_param(code)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildTemplateResponse,
                    parse_obj_as(
                        type_=GuildTemplateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_templates(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[GuildTemplateResponse]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[GuildTemplateResponse]]]
            200 response for list_guild_templates
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/templates",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[GuildTemplateResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[GuildTemplateResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_guild_template(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildTemplateResponse]:
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
        AsyncHttpResponse[GuildTemplateResponse]
            200 response for create_guild_template
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/templates",
            method="POST",
            json={
                "name": name,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildTemplateResponse,
                    parse_obj_as(
                        type_=GuildTemplateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_sticker(
        self,
        guild_id: SnowflakeType,
        sticker_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildStickerResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sticker_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GuildStickerResponse]
            200 response for get_guild_sticker
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/stickers/{encode_path_param(sticker_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildStickerResponse,
                    parse_obj_as(
                        type_=GuildStickerResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_guild_sticker(
        self,
        guild_id: SnowflakeType,
        sticker_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        sticker_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/stickers/{encode_path_param(sticker_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_guild_sticker(
        self,
        guild_id: SnowflakeType,
        sticker_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        tags: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildStickerResponse]:
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
        AsyncHttpResponse[GuildStickerResponse]
            200 response for update_guild_sticker
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/stickers/{encode_path_param(sticker_id)}",
            method="PATCH",
            json={
                "name": name,
                "tags": tags,
                "description": description,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildStickerResponse,
                    parse_obj_as(
                        type_=GuildStickerResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bulk_ban_users_from_guild(
        self,
        guild_id: SnowflakeType,
        *,
        user_ids: typing.Sequence[SnowflakeType],
        delete_message_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkBanUsersResponse]:
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
        AsyncHttpResponse[BulkBanUsersResponse]
            200 response for bulk_ban_users_from_guild
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/bulk-ban",
            method="POST",
            json={
                "user_ids": user_ids,
                "delete_message_seconds": delete_message_seconds,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkBanUsersResponse,
                    parse_obj_as(
                        type_=BulkBanUsersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_stickers(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GuildStickerResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GuildStickerResponse]]
            200 response for list_guild_stickers
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/stickers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GuildStickerResponse],
                    parse_obj_as(
                        type_=typing.List[GuildStickerResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_guild_sticker(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        tags: str,
        file: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildStickerResponse]:
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
        AsyncHttpResponse[GuildStickerResponse]
            201 response for create_guild_sticker
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/stickers",
            method="POST",
            data={
                "name": name,
                "tags": tags,
                "description": description,
                "file": file,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildStickerResponse,
                    parse_obj_as(
                        type_=GuildStickerResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_webhooks(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[GetGuildWebhooksResponseItem]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[GetGuildWebhooksResponseItem]]]
            200 response for get_guild_webhooks
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/webhooks",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[GetGuildWebhooksResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[GetGuildWebhooksResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_channels(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ListGuildChannelsResponseItem]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[ListGuildChannelsResponseItem]]]
            200 response for list_guild_channels
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/channels",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ListGuildChannelsResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ListGuildChannelsResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[GuildChannelResponse]:
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
        AsyncHttpResponse[GuildChannelResponse]
            201 response for create_guild_channel
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/channels",
            method="POST",
            json={
                "type": type,
                "name": name,
                "position": position,
                "topic": topic,
                "bitrate": bitrate,
                "user_limit": user_limit,
                "nsfw": nsfw,
                "rate_limit_per_user": rate_limit_per_user,
                "parent_id": parent_id,
                "permission_overwrites": convert_and_respect_annotation_metadata(
                    object_=permission_overwrites,
                    annotation=typing.Optional[typing.Sequence[ChannelPermissionOverwriteRequest]],
                    direction="write",
                ),
                "rtc_region": rtc_region,
                "video_quality_mode": video_quality_mode,
                "default_auto_archive_duration": default_auto_archive_duration,
                "default_reaction_emoji": convert_and_respect_annotation_metadata(
                    object_=default_reaction_emoji,
                    annotation=typing.Optional[UpdateDefaultReactionEmojiRequest],
                    direction="write",
                ),
                "default_thread_rate_limit_per_user": default_thread_rate_limit_per_user,
                "default_sort_order": default_sort_order,
                "default_forum_layout": default_forum_layout,
                "available_tags": convert_and_respect_annotation_metadata(
                    object_=available_tags,
                    annotation=typing.Optional[typing.Sequence[typing.Optional[CreateOrUpdateThreadTagRequest]]],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildChannelResponse,
                    parse_obj_as(
                        type_=GuildChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bulk_update_guild_channels(
        self,
        guild_id: SnowflakeType,
        *,
        request: typing.Sequence[BulkUpdateGuildChannelsRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : typing.Sequence[BulkUpdateGuildChannelsRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/channels",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[BulkUpdateGuildChannelsRequestBodyItem], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_member(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildMemberResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GuildMemberResponse]
            200 response for get_guild_member
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildMemberResponse,
                    parse_obj_as(
                        type_=GuildMemberResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.Optional[GuildMemberResponse]]:
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
        AsyncHttpResponse[typing.Optional[GuildMemberResponse]]
            201 response for add_guild_member
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/{encode_path_param(user_id)}",
            method="PUT",
            json={
                "nick": nick,
                "roles": roles,
                "mute": mute,
                "deaf": deaf,
                "access_token": access_token,
                "flags": flags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[GuildMemberResponse],
                    parse_obj_as(
                        type_=typing.Optional[GuildMemberResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_guild_member(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.Optional[GuildMemberResponse]]:
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
        AsyncHttpResponse[typing.Optional[GuildMemberResponse]]
            200 response for update_guild_member
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members/{encode_path_param(user_id)}",
            method="PATCH",
            json={
                "nick": nick,
                "roles": roles,
                "mute": mute,
                "deaf": deaf,
                "channel_id": channel_id,
                "communication_disabled_until": communication_disabled_until,
                "flags": flags,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[GuildMemberResponse],
                    parse_obj_as(
                        type_=typing.Optional[GuildMemberResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_members(
        self,
        guild_id: SnowflakeType,
        *,
        limit: typing.Optional[int] = None,
        after: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GuildMemberResponse]]:
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
        AsyncHttpResponse[typing.List[GuildMemberResponse]]
            200 response for list_guild_members
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/members",
            method="GET",
            params={
                "limit": limit,
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GuildMemberResponse],
                    parse_obj_as(
                        type_=typing.List[GuildMemberResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_preview(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GuildPreviewResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GuildPreviewResponse]
            200 response for get_guild_preview
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/preview",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildPreviewResponse,
                    parse_obj_as(
                        type_=GuildPreviewResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_invites(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[ListGuildInvitesResponseItem]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[ListGuildInvitesResponseItem]]]
            200 response for list_guild_invites
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/invites",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[ListGuildInvitesResponseItem]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[ListGuildInvitesResponseItem]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_voice_regions(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[VoiceRegionResponse]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[VoiceRegionResponse]]]
            200 response for list_guild_voice_regions
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/regions",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[VoiceRegionResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[VoiceRegionResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_emoji(
        self,
        guild_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmojiResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmojiResponse]
            200 response for get_guild_emoji
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/emojis/{encode_path_param(emoji_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmojiResponse,
                    parse_obj_as(
                        type_=EmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_guild_emoji(
        self,
        guild_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        emoji_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/emojis/{encode_path_param(emoji_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_guild_emoji(
        self,
        guild_id: SnowflakeType,
        emoji_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        roles: typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmojiResponse]:
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
        AsyncHttpResponse[EmojiResponse]
            200 response for update_guild_emoji
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/emojis/{encode_path_param(emoji_id)}",
            method="PATCH",
            json={
                "name": name,
                "roles": roles,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmojiResponse,
                    parse_obj_as(
                        type_=EmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_emojis(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[typing.List[EmojiResponse]]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[typing.List[EmojiResponse]]]
            200 response for list_guild_emojis
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/emojis",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[EmojiResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[EmojiResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_guild_emoji(
        self,
        guild_id: SnowflakeType,
        *,
        name: str,
        image: str,
        roles: typing.Optional[typing.Sequence[typing.Optional[SnowflakeType]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmojiResponse]:
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
        AsyncHttpResponse[EmojiResponse]
            201 response for create_guild_emoji
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/emojis",
            method="POST",
            json={
                "name": name,
                "image": image,
                "roles": roles,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmojiResponse,
                    parse_obj_as(
                        type_=EmojiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_widget_settings(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WidgetSettingsResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WidgetSettingsResponse]
            200 response for get_guild_widget_settings
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/widget",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WidgetSettingsResponse,
                    parse_obj_as(
                        type_=WidgetSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_guild_widget_settings(
        self,
        guild_id: SnowflakeType,
        *,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WidgetSettingsResponse]:
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
        AsyncHttpResponse[WidgetSettingsResponse]
            200 response for update_guild_widget_settings
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/widget",
            method="PATCH",
            json={
                "channel_id": channel_id,
                "enabled": enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WidgetSettingsResponse,
                    parse_obj_as(
                        type_=WidgetSettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_role(
        self,
        guild_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildRoleResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        role_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GuildRoleResponse]
            200 response for get_guild_role
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/roles/{encode_path_param(role_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildRoleResponse,
                    parse_obj_as(
                        type_=GuildRoleResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_guild_role(
        self,
        guild_id: SnowflakeType,
        role_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        role_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/roles/{encode_path_param(role_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[GuildRoleResponse]:
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
        AsyncHttpResponse[GuildRoleResponse]
            200 response for update_guild_role
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/roles/{encode_path_param(role_id)}",
            method="PATCH",
            json={
                "name": name,
                "permissions": permissions,
                "color": color,
                "hoist": hoist,
                "mentionable": mentionable,
                "icon": icon,
                "unicode_emoji": unicode_emoji,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildRoleResponse,
                    parse_obj_as(
                        type_=GuildRoleResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_roles(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GuildRoleResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GuildRoleResponse]]
            200 response for list_guild_roles
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/roles",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GuildRoleResponse],
                    parse_obj_as(
                        type_=typing.List[GuildRoleResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[GuildRoleResponse]:
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
        AsyncHttpResponse[GuildRoleResponse]
            200 response for create_guild_role
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/roles",
            method="POST",
            json={
                "name": name,
                "permissions": permissions,
                "color": color,
                "hoist": hoist,
                "mentionable": mentionable,
                "icon": icon,
                "unicode_emoji": unicode_emoji,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildRoleResponse,
                    parse_obj_as(
                        type_=GuildRoleResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bulk_update_guild_roles(
        self,
        guild_id: SnowflakeType,
        *,
        request: typing.Sequence[BulkUpdateGuildRolesRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GuildRoleResponse]]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request : typing.Sequence[BulkUpdateGuildRolesRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GuildRoleResponse]]
            200 response for bulk_update_guild_roles
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/roles",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=typing.Sequence[BulkUpdateGuildRolesRequestBodyItem], direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GuildRoleResponse],
                    parse_obj_as(
                        type_=typing.List[GuildRoleResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def preview_prune_guild(
        self,
        guild_id: SnowflakeType,
        *,
        days: typing.Optional[int] = None,
        include_roles: typing.Optional[PreviewPruneGuildRequestIncludeRoles] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildPruneResponse]:
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
        AsyncHttpResponse[GuildPruneResponse]
            200 response for preview_prune_guild
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/prune",
            method="GET",
            params={
                "days": days,
                "include_roles": convert_and_respect_annotation_metadata(
                    object_=include_roles, annotation=PreviewPruneGuildRequestIncludeRoles, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildPruneResponse,
                    parse_obj_as(
                        type_=GuildPruneResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def prune_guild(
        self,
        guild_id: SnowflakeType,
        *,
        days: typing.Optional[int] = OMIT,
        compute_prune_count: typing.Optional[bool] = OMIT,
        include_roles: typing.Optional[PruneGuildRequestIncludeRoles] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildPruneResponse]:
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
        AsyncHttpResponse[GuildPruneResponse]
            200 response for prune_guild
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/prune",
            method="POST",
            json={
                "days": days,
                "compute_prune_count": compute_prune_count,
                "include_roles": convert_and_respect_annotation_metadata(
                    object_=include_roles, annotation=typing.Optional[PruneGuildRequestIncludeRoles], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildPruneResponse,
                    parse_obj_as(
                        type_=GuildPruneResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild_ban(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildBanResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GuildBanResponse]
            200 response for get_guild_ban
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/bans/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildBanResponse,
                    parse_obj_as(
                        type_=GuildBanResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ban_user_from_guild(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        delete_message_seconds: typing.Optional[int] = OMIT,
        delete_message_days: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/bans/{encode_path_param(user_id)}",
            method="PUT",
            json={
                "delete_message_seconds": delete_message_seconds,
                "delete_message_days": delete_message_days,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def unban_user_from_guild(
        self,
        guild_id: SnowflakeType,
        user_id: SnowflakeType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/bans/{encode_path_param(user_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_guild_bans(
        self,
        guild_id: SnowflakeType,
        *,
        limit: typing.Optional[int] = None,
        before: typing.Optional[SnowflakeType] = None,
        after: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[typing.List[GuildBanResponse]]]:
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
        AsyncHttpResponse[typing.Optional[typing.List[GuildBanResponse]]]
            200 response for list_guild_bans
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/bans",
            method="GET",
            params={
                "limit": limit,
                "before": before,
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[typing.List[GuildBanResponse]],
                    parse_obj_as(
                        type_=typing.Optional[typing.List[GuildBanResponse]],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_guild_mfa_level(
        self, guild_id: SnowflakeType, *, level: GuildMfaLevel, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GuildMfaLevelResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        level : GuildMfaLevel

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GuildMfaLevelResponse]
            200 response for set_guild_mfa_level
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}/mfa",
            method="POST",
            json={
                "level": level,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildMfaLevelResponse,
                    parse_obj_as(
                        type_=GuildMfaLevelResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_stage_instance(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StageInstanceResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StageInstanceResponse]
            200 response for get_stage_instance
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"stage-instances/{encode_path_param(channel_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StageInstanceResponse,
                    parse_obj_as(
                        type_=StageInstanceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_stage_instance(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"stage-instances/{encode_path_param(channel_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_stage_instance(
        self,
        channel_id: SnowflakeType,
        *,
        topic: typing.Optional[str] = OMIT,
        privacy_level: typing.Optional[StageInstancesPrivacyLevels] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StageInstanceResponse]:
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
        AsyncHttpResponse[StageInstanceResponse]
            200 response for update_stage_instance
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"stage-instances/{encode_path_param(channel_id)}",
            method="PATCH",
            json={
                "topic": topic,
                "privacy_level": privacy_level,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StageInstanceResponse,
                    parse_obj_as(
                        type_=StageInstanceResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_sticker_pack(
        self, pack_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StickerPackResponse]:
        """
        Parameters
        ----------
        pack_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StickerPackResponse]
            200 response for get_sticker_pack
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sticker-packs/{encode_path_param(pack_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StickerPackResponse,
                    parse_obj_as(
                        type_=StickerPackResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_application(
        self, application_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PrivateApplicationResponse]:
        """
        Parameters
        ----------
        application_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PrivateApplicationResponse]
            200 response for get_application
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateApplicationResponse,
                    parse_obj_as(
                        type_=PrivateApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[PrivateApplicationResponse]:
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
        AsyncHttpResponse[PrivateApplicationResponse]
            200 response for update_application
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"applications/{encode_path_param(application_id)}",
            method="PATCH",
            json={
                "description": convert_and_respect_annotation_metadata(
                    object_=description,
                    annotation=typing.Optional[ApplicationFormPartialDescription],
                    direction="write",
                ),
                "icon": icon,
                "cover_image": cover_image,
                "team_id": team_id,
                "flags": flags,
                "interactions_endpoint_url": interactions_endpoint_url,
                "explicit_content_filter": explicit_content_filter,
                "max_participants": max_participants,
                "type": type,
                "tags": tags,
                "custom_install_url": custom_install_url,
                "install_params": convert_and_respect_annotation_metadata(
                    object_=install_params,
                    annotation=typing.Optional[ApplicationOAuth2InstallParams],
                    direction="write",
                ),
                "role_connections_verification_url": role_connections_verification_url,
                "integration_types_config": convert_and_respect_annotation_metadata(
                    object_=integration_types_config,
                    annotation=typing.Optional[
                        typing.Dict[str, typing.Optional[ApplicationIntegrationTypeConfiguration]]
                    ],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateApplicationResponse,
                    parse_obj_as(
                        type_=PrivateApplicationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_webhook_by_token(
        self, webhook_id: SnowflakeType, webhook_token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetWebhookByTokenResponse]:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetWebhookByTokenResponse]
            200 response for get_webhook_by_token
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWebhookByTokenResponse,
                    parse_obj_as(
                        type_=GetWebhookByTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[typing.Optional[MessageResponse]]:
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
        AsyncHttpResponse[typing.Optional[MessageResponse]]
            200 response for execute_webhook
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}",
            method="POST",
            params={
                "wait": wait,
                "thread_id": thread_id,
                "with_components": with_components,
            },
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ExecuteWebhookRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[MessageResponse],
                    parse_obj_as(
                        type_=typing.Optional[MessageResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_webhook_by_token(
        self, webhook_id: SnowflakeType, webhook_token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        webhook_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_webhook_by_token(
        self,
        webhook_id: SnowflakeType,
        webhook_token: str,
        *,
        name: typing.Optional[str] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateWebhookByTokenResponse]:
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
        AsyncHttpResponse[UpdateWebhookByTokenResponse]
            200 response for update_webhook_by_token
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/{encode_path_param(webhook_token)}",
            method="PATCH",
            json={
                "name": name,
                "avatar": avatar,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateWebhookByTokenResponse,
                    parse_obj_as(
                        type_=UpdateWebhookByTokenResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_sticker(
        self, sticker_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetStickerResponse]:
        """
        Parameters
        ----------
        sticker_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetStickerResponse]
            200 response for get_sticker
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"stickers/{encode_path_param(sticker_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetStickerResponse,
                    parse_obj_as(
                        type_=GetStickerResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_webhook(
        self, webhook_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetWebhookResponse]:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetWebhookResponse]
            200 response for get_webhook
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWebhookResponse,
                    parse_obj_as(
                        type_=GetWebhookResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_webhook(
        self, webhook_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        webhook_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_webhook(
        self,
        webhook_id: SnowflakeType,
        *,
        name: typing.Optional[str] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        channel_id: typing.Optional[SnowflakeType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateWebhookResponse]:
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
        AsyncHttpResponse[UpdateWebhookResponse]
            200 response for update_webhook
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}",
            method="PATCH",
            json={
                "name": name,
                "avatar": avatar,
                "channel_id": channel_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateWebhookResponse,
                    parse_obj_as(
                        type_=UpdateWebhookResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_channel(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetChannelResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChannelResponse]
            200 response for get_channel
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetChannelResponse,
                    parse_obj_as(
                        type_=GetChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_channel(
        self, channel_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteChannelResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteChannelResponse]
            200 response for delete_channel
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteChannelResponse,
                    parse_obj_as(
                        type_=DeleteChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_channel(
        self,
        channel_id: SnowflakeType,
        *,
        request: UpdateChannelRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateChannelResponse]:
        """
        Parameters
        ----------
        channel_id : SnowflakeType

        request : UpdateChannelRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateChannelResponse]
            200 response for update_channel
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"channels/{encode_path_param(channel_id)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateChannelRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateChannelResponse,
                    parse_obj_as(
                        type_=UpdateChannelResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def invite_resolve(
        self,
        code: str,
        *,
        with_counts: typing.Optional[bool] = None,
        guild_scheduled_event_id: typing.Optional[SnowflakeType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InviteResolveResponse]:
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
        AsyncHttpResponse[InviteResolveResponse]
            200 response for invite_resolve
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invites/{encode_path_param(code)}",
            method="GET",
            params={
                "with_counts": with_counts,
                "guild_scheduled_event_id": guild_scheduled_event_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InviteResolveResponse,
                    parse_obj_as(
                        type_=InviteResolveResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def invite_revoke(
        self, code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InviteRevokeResponse]:
        """
        Parameters
        ----------
        code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InviteRevokeResponse]
            200 response for invite_revoke
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"invites/{encode_path_param(code)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InviteRevokeResponse,
                    parse_obj_as(
                        type_=InviteRevokeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_lobby(
        self, lobby_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LobbyResponse]:
        """
        Parameters
        ----------
        lobby_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LobbyResponse]
            200 response for get_lobby
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyResponse,
                    parse_obj_as(
                        type_=LobbyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def edit_lobby(
        self,
        lobby_id: SnowflakeType,
        *,
        idle_timeout_seconds: typing.Optional[int] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        members: typing.Optional[typing.Sequence[LobbyMemberRequest]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LobbyResponse]:
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
        AsyncHttpResponse[LobbyResponse]
            200 response for edit_lobby
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"lobbies/{encode_path_param(lobby_id)}",
            method="PATCH",
            json={
                "idle_timeout_seconds": idle_timeout_seconds,
                "metadata": metadata,
                "members": convert_and_respect_annotation_metadata(
                    object_=members, annotation=typing.Optional[typing.Sequence[LobbyMemberRequest]], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LobbyResponse,
                    parse_obj_as(
                        type_=LobbyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_guild(
        self,
        guild_id: SnowflakeType,
        *,
        with_counts: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GuildWithCountsResponse]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        with_counts : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GuildWithCountsResponse]
            200 response for get_guild
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}",
            method="GET",
            params={
                "with_counts": with_counts,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildWithCountsResponse,
                    parse_obj_as(
                        type_=GuildWithCountsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_guild(
        self, guild_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        guild_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[GuildResponse]:
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
        AsyncHttpResponse[GuildResponse]
            200 response for update_guild
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"guilds/{encode_path_param(guild_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "region": region,
                "icon": icon,
                "verification_level": verification_level,
                "default_message_notifications": default_message_notifications,
                "explicit_content_filter": explicit_content_filter,
                "preferred_locale": preferred_locale,
                "afk_timeout": afk_timeout,
                "afk_channel_id": afk_channel_id,
                "system_channel_id": system_channel_id,
                "owner_id": owner_id,
                "splash": splash,
                "banner": banner,
                "system_channel_flags": system_channel_flags,
                "features": features,
                "discovery_splash": discovery_splash,
                "home_header": home_header,
                "rules_channel_id": rules_channel_id,
                "safety_alerts_channel_id": safety_alerts_channel_id,
                "public_updates_channel_id": public_updates_channel_id,
                "premium_progress_bar_enabled": premium_progress_bar_enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GuildResponse,
                    parse_obj_as(
                        type_=GuildResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_user(
        self, user_id: SnowflakeType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserResponse]:
        """
        Parameters
        ----------
        user_id : SnowflakeType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserResponse]
            200 response for get_user
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserResponse,
                    parse_obj_as(
                        type_=UserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
