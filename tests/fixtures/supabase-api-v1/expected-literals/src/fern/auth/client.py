

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.auth_config_response_output import AuthConfigResponseOutput
from ..types.create_provider_response_output import CreateProviderResponseOutput
from ..types.delete_provider_response_output import DeleteProviderResponseOutput
from ..types.get_provider_response_output import GetProviderResponseOutput
from ..types.list_providers_response_output import ListProvidersResponseOutput
from ..types.signing_key_response_output import SigningKeyResponseOutput
from ..types.signing_keys_response_output import SigningKeysResponseOutput
from ..types.third_party_auth_output import ThirdPartyAuthOutput
from ..types.update_provider_response_output import UpdateProviderResponseOutput
from .raw_client import AsyncRawAuthClient, RawAuthClient
from .types.create_provider_body_attribute_mapping import CreateProviderBodyAttributeMapping
from .types.create_provider_body_name_id_format import CreateProviderBodyNameIdFormat
from .types.create_provider_body_type import CreateProviderBodyType
from .types.create_signing_key_body_algorithm import CreateSigningKeyBodyAlgorithm
from .types.create_signing_key_body_private_jwk import CreateSigningKeyBodyPrivateJwk
from .types.create_signing_key_body_status import CreateSigningKeyBodyStatus
from .types.update_auth_config_body_db_max_pool_size_unit import UpdateAuthConfigBodyDbMaxPoolSizeUnit
from .types.update_auth_config_body_password_required_characters import UpdateAuthConfigBodyPasswordRequiredCharacters
from .types.update_auth_config_body_security_captcha_provider import UpdateAuthConfigBodySecurityCaptchaProvider
from .types.update_auth_config_body_sms_provider import UpdateAuthConfigBodySmsProvider
from .types.update_provider_body_attribute_mapping import UpdateProviderBodyAttributeMapping
from .types.update_provider_body_name_id_format import UpdateProviderBodyNameIdFormat
from .types.update_signing_key_body_status import UpdateSigningKeyBodyStatus


OMIT = typing.cast(typing.Any, ...)


class AuthClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuthClient
        """
        return self._raw_client

    def v1get_legacy_signing_key(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SigningKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeyResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1get_legacy_signing_key(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_legacy_signing_key(ref, request_options=request_options)
        return _response.data

    def v1create_legacy_signing_key(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SigningKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeyResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1create_legacy_signing_key(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1create_legacy_signing_key(ref, request_options=request_options)
        return _response.data

    def v1get_project_signing_keys(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SigningKeysResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeysResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1get_project_signing_keys(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_project_signing_keys(ref, request_options=request_options)
        return _response.data

    def v1create_project_signing_key(
        self,
        ref: str,
        *,
        algorithm: CreateSigningKeyBodyAlgorithm,
        status: typing.Optional[CreateSigningKeyBodyStatus] = OMIT,
        private_jwk: typing.Optional[CreateSigningKeyBodyPrivateJwk] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SigningKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        algorithm : CreateSigningKeyBodyAlgorithm

        status : typing.Optional[CreateSigningKeyBodyStatus]

        private_jwk : typing.Optional[CreateSigningKeyBodyPrivateJwk]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeyResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1create_project_signing_key(
            ref="abcdefghijklmnopqrst",
            algorithm="RS256",
            status="standby",
        )
        """
        _response = self._raw_client.v1create_project_signing_key(
            ref, algorithm=algorithm, status=status, private_jwk=private_jwk, request_options=request_options
        )
        return _response.data

    def v1get_project_signing_key(
        self, ref: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SigningKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeyResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1get_project_signing_key(
            ref="abcdefghijklmnopqrst",
            id="33333333-3333-4333-8333-333333333333",
        )
        """
        _response = self._raw_client.v1get_project_signing_key(ref, id, request_options=request_options)
        return _response.data

    def v1remove_project_signing_key(
        self, ref: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SigningKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeyResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1remove_project_signing_key(
            ref="abcdefghijklmnopqrst",
            id="33333333-3333-4333-8333-333333333333",
        )
        """
        _response = self._raw_client.v1remove_project_signing_key(ref, id, request_options=request_options)
        return _response.data

    def v1update_project_signing_key(
        self,
        ref: str,
        id: str,
        *,
        status: UpdateSigningKeyBodyStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SigningKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : str

        status : UpdateSigningKeyBodyStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeyResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1update_project_signing_key(
            ref="abcdefghijklmnopqrst",
            id="33333333-3333-4333-8333-333333333333",
            status="standby",
        )
        """
        _response = self._raw_client.v1update_project_signing_key(
            ref, id, status=status, request_options=request_options
        )
        return _response.data

    def v1get_auth_service_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthConfigResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1get_auth_service_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_auth_service_config(ref, request_options=request_options)
        return _response.data

    def v1update_auth_service_config(
        self,
        ref: str,
        *,
        site_url: typing.Optional[str] = OMIT,
        disable_signup: typing.Optional[bool] = OMIT,
        jwt_exp: typing.Optional[int] = OMIT,
        smtp_admin_email: typing.Optional[str] = OMIT,
        smtp_host: typing.Optional[str] = OMIT,
        smtp_port: typing.Optional[str] = OMIT,
        smtp_user: typing.Optional[str] = OMIT,
        smtp_pass: typing.Optional[str] = OMIT,
        smtp_max_frequency: typing.Optional[int] = OMIT,
        smtp_sender_name: typing.Optional[str] = OMIT,
        mailer_allow_unverified_email_sign_ins: typing.Optional[bool] = OMIT,
        mailer_autoconfirm: typing.Optional[bool] = OMIT,
        mailer_subjects_invite: typing.Optional[str] = OMIT,
        mailer_subjects_confirmation: typing.Optional[str] = OMIT,
        mailer_subjects_recovery: typing.Optional[str] = OMIT,
        mailer_subjects_email_change: typing.Optional[str] = OMIT,
        mailer_subjects_magic_link: typing.Optional[str] = OMIT,
        mailer_subjects_reauthentication: typing.Optional[str] = OMIT,
        mailer_subjects_password_changed_notification: typing.Optional[str] = OMIT,
        mailer_subjects_email_changed_notification: typing.Optional[str] = OMIT,
        mailer_subjects_phone_changed_notification: typing.Optional[str] = OMIT,
        mailer_subjects_mfa_factor_enrolled_notification: typing.Optional[str] = OMIT,
        mailer_subjects_mfa_factor_unenrolled_notification: typing.Optional[str] = OMIT,
        mailer_subjects_identity_linked_notification: typing.Optional[str] = OMIT,
        mailer_subjects_identity_unlinked_notification: typing.Optional[str] = OMIT,
        mailer_templates_invite_content: typing.Optional[str] = OMIT,
        mailer_templates_confirmation_content: typing.Optional[str] = OMIT,
        mailer_templates_recovery_content: typing.Optional[str] = OMIT,
        mailer_templates_email_change_content: typing.Optional[str] = OMIT,
        mailer_templates_magic_link_content: typing.Optional[str] = OMIT,
        mailer_templates_reauthentication_content: typing.Optional[str] = OMIT,
        mailer_templates_password_changed_notification_content: typing.Optional[str] = OMIT,
        mailer_templates_email_changed_notification_content: typing.Optional[str] = OMIT,
        mailer_templates_phone_changed_notification_content: typing.Optional[str] = OMIT,
        mailer_templates_mfa_factor_enrolled_notification_content: typing.Optional[str] = OMIT,
        mailer_templates_mfa_factor_unenrolled_notification_content: typing.Optional[str] = OMIT,
        mailer_templates_identity_linked_notification_content: typing.Optional[str] = OMIT,
        mailer_templates_identity_unlinked_notification_content: typing.Optional[str] = OMIT,
        mailer_notifications_password_changed_enabled: typing.Optional[bool] = OMIT,
        mailer_notifications_email_changed_enabled: typing.Optional[bool] = OMIT,
        mailer_notifications_phone_changed_enabled: typing.Optional[bool] = OMIT,
        mailer_notifications_mfa_factor_enrolled_enabled: typing.Optional[bool] = OMIT,
        mailer_notifications_mfa_factor_unenrolled_enabled: typing.Optional[bool] = OMIT,
        mailer_notifications_identity_linked_enabled: typing.Optional[bool] = OMIT,
        mailer_notifications_identity_unlinked_enabled: typing.Optional[bool] = OMIT,
        mfa_max_enrolled_factors: typing.Optional[int] = OMIT,
        uri_allow_list: typing.Optional[str] = OMIT,
        external_anonymous_users_enabled: typing.Optional[bool] = OMIT,
        external_email_enabled: typing.Optional[bool] = OMIT,
        external_phone_enabled: typing.Optional[bool] = OMIT,
        saml_enabled: typing.Optional[bool] = OMIT,
        saml_external_url: typing.Optional[str] = OMIT,
        security_sb_forwarded_for_enabled: typing.Optional[bool] = OMIT,
        security_captcha_enabled: typing.Optional[bool] = OMIT,
        security_captcha_provider: typing.Optional[UpdateAuthConfigBodySecurityCaptchaProvider] = OMIT,
        security_captcha_secret: typing.Optional[str] = OMIT,
        sessions_timebox: typing.Optional[float] = OMIT,
        sessions_inactivity_timeout: typing.Optional[float] = OMIT,
        sessions_single_per_user: typing.Optional[bool] = OMIT,
        sessions_tags: typing.Optional[str] = OMIT,
        rate_limit_anonymous_users: typing.Optional[int] = OMIT,
        rate_limit_email_sent: typing.Optional[int] = OMIT,
        rate_limit_sms_sent: typing.Optional[int] = OMIT,
        rate_limit_verify: typing.Optional[int] = OMIT,
        rate_limit_token_refresh: typing.Optional[int] = OMIT,
        rate_limit_otp: typing.Optional[int] = OMIT,
        rate_limit_web3: typing.Optional[int] = OMIT,
        mailer_secure_email_change_enabled: typing.Optional[bool] = OMIT,
        refresh_token_rotation_enabled: typing.Optional[bool] = OMIT,
        password_hibp_enabled: typing.Optional[bool] = OMIT,
        password_min_length: typing.Optional[int] = OMIT,
        password_required_characters: typing.Optional[UpdateAuthConfigBodyPasswordRequiredCharacters] = OMIT,
        security_manual_linking_enabled: typing.Optional[bool] = OMIT,
        security_update_password_require_reauthentication: typing.Optional[bool] = OMIT,
        security_update_password_require_current_password: typing.Optional[bool] = OMIT,
        security_refresh_token_reuse_interval: typing.Optional[int] = OMIT,
        mailer_otp_exp: typing.Optional[int] = OMIT,
        mailer_otp_length: typing.Optional[int] = OMIT,
        sms_autoconfirm: typing.Optional[bool] = OMIT,
        sms_max_frequency: typing.Optional[int] = OMIT,
        sms_otp_exp: typing.Optional[int] = OMIT,
        sms_otp_length: typing.Optional[int] = OMIT,
        sms_provider: typing.Optional[UpdateAuthConfigBodySmsProvider] = OMIT,
        sms_messagebird_access_key: typing.Optional[str] = OMIT,
        sms_messagebird_originator: typing.Optional[str] = OMIT,
        sms_test_otp: typing.Optional[str] = OMIT,
        sms_test_otp_valid_until: typing.Optional[dt.datetime] = OMIT,
        sms_textlocal_api_key: typing.Optional[str] = OMIT,
        sms_textlocal_sender: typing.Optional[str] = OMIT,
        sms_twilio_account_sid: typing.Optional[str] = OMIT,
        sms_twilio_auth_token: typing.Optional[str] = OMIT,
        sms_twilio_content_sid: typing.Optional[str] = OMIT,
        sms_twilio_message_service_sid: typing.Optional[str] = OMIT,
        sms_twilio_verify_account_sid: typing.Optional[str] = OMIT,
        sms_twilio_verify_auth_token: typing.Optional[str] = OMIT,
        sms_twilio_verify_message_service_sid: typing.Optional[str] = OMIT,
        sms_vonage_api_key: typing.Optional[str] = OMIT,
        sms_vonage_api_secret: typing.Optional[str] = OMIT,
        sms_vonage_from: typing.Optional[str] = OMIT,
        sms_template: typing.Optional[str] = OMIT,
        hook_mfa_verification_attempt_enabled: typing.Optional[bool] = OMIT,
        hook_mfa_verification_attempt_uri: typing.Optional[str] = OMIT,
        hook_mfa_verification_attempt_secrets: typing.Optional[str] = OMIT,
        hook_password_verification_attempt_enabled: typing.Optional[bool] = OMIT,
        hook_password_verification_attempt_uri: typing.Optional[str] = OMIT,
        hook_password_verification_attempt_secrets: typing.Optional[str] = OMIT,
        hook_custom_access_token_enabled: typing.Optional[bool] = OMIT,
        hook_custom_access_token_uri: typing.Optional[str] = OMIT,
        hook_custom_access_token_secrets: typing.Optional[str] = OMIT,
        hook_send_sms_enabled: typing.Optional[bool] = OMIT,
        hook_send_sms_uri: typing.Optional[str] = OMIT,
        hook_send_sms_secrets: typing.Optional[str] = OMIT,
        hook_send_email_enabled: typing.Optional[bool] = OMIT,
        hook_send_email_uri: typing.Optional[str] = OMIT,
        hook_send_email_secrets: typing.Optional[str] = OMIT,
        hook_before_user_created_enabled: typing.Optional[bool] = OMIT,
        hook_before_user_created_uri: typing.Optional[str] = OMIT,
        hook_before_user_created_secrets: typing.Optional[str] = OMIT,
        hook_after_user_created_enabled: typing.Optional[bool] = OMIT,
        hook_after_user_created_uri: typing.Optional[str] = OMIT,
        hook_after_user_created_secrets: typing.Optional[str] = OMIT,
        external_apple_enabled: typing.Optional[bool] = OMIT,
        external_apple_client_id: typing.Optional[str] = OMIT,
        external_apple_email_optional: typing.Optional[bool] = OMIT,
        external_apple_secret: typing.Optional[str] = OMIT,
        external_apple_additional_client_ids: typing.Optional[str] = OMIT,
        external_azure_enabled: typing.Optional[bool] = OMIT,
        external_azure_client_id: typing.Optional[str] = OMIT,
        external_azure_email_optional: typing.Optional[bool] = OMIT,
        external_azure_secret: typing.Optional[str] = OMIT,
        external_azure_url: typing.Optional[str] = OMIT,
        external_bitbucket_enabled: typing.Optional[bool] = OMIT,
        external_bitbucket_client_id: typing.Optional[str] = OMIT,
        external_bitbucket_email_optional: typing.Optional[bool] = OMIT,
        external_bitbucket_secret: typing.Optional[str] = OMIT,
        external_discord_enabled: typing.Optional[bool] = OMIT,
        external_discord_client_id: typing.Optional[str] = OMIT,
        external_discord_email_optional: typing.Optional[bool] = OMIT,
        external_discord_secret: typing.Optional[str] = OMIT,
        external_facebook_enabled: typing.Optional[bool] = OMIT,
        external_facebook_client_id: typing.Optional[str] = OMIT,
        external_facebook_email_optional: typing.Optional[bool] = OMIT,
        external_facebook_secret: typing.Optional[str] = OMIT,
        external_figma_enabled: typing.Optional[bool] = OMIT,
        external_figma_client_id: typing.Optional[str] = OMIT,
        external_figma_email_optional: typing.Optional[bool] = OMIT,
        external_figma_secret: typing.Optional[str] = OMIT,
        external_github_enabled: typing.Optional[bool] = OMIT,
        external_github_client_id: typing.Optional[str] = OMIT,
        external_github_email_optional: typing.Optional[bool] = OMIT,
        external_github_secret: typing.Optional[str] = OMIT,
        external_gitlab_enabled: typing.Optional[bool] = OMIT,
        external_gitlab_client_id: typing.Optional[str] = OMIT,
        external_gitlab_email_optional: typing.Optional[bool] = OMIT,
        external_gitlab_secret: typing.Optional[str] = OMIT,
        external_gitlab_url: typing.Optional[str] = OMIT,
        external_google_enabled: typing.Optional[bool] = OMIT,
        external_google_client_id: typing.Optional[str] = OMIT,
        external_google_email_optional: typing.Optional[bool] = OMIT,
        external_google_secret: typing.Optional[str] = OMIT,
        external_google_additional_client_ids: typing.Optional[str] = OMIT,
        external_google_skip_nonce_check: typing.Optional[bool] = OMIT,
        external_kakao_enabled: typing.Optional[bool] = OMIT,
        external_kakao_client_id: typing.Optional[str] = OMIT,
        external_kakao_email_optional: typing.Optional[bool] = OMIT,
        external_kakao_secret: typing.Optional[str] = OMIT,
        external_keycloak_enabled: typing.Optional[bool] = OMIT,
        external_keycloak_client_id: typing.Optional[str] = OMIT,
        external_keycloak_email_optional: typing.Optional[bool] = OMIT,
        external_keycloak_secret: typing.Optional[str] = OMIT,
        external_keycloak_url: typing.Optional[str] = OMIT,
        external_linkedin_oidc_enabled: typing.Optional[bool] = OMIT,
        external_linkedin_oidc_client_id: typing.Optional[str] = OMIT,
        external_linkedin_oidc_email_optional: typing.Optional[bool] = OMIT,
        external_linkedin_oidc_secret: typing.Optional[str] = OMIT,
        external_slack_oidc_enabled: typing.Optional[bool] = OMIT,
        external_slack_oidc_client_id: typing.Optional[str] = OMIT,
        external_slack_oidc_email_optional: typing.Optional[bool] = OMIT,
        external_slack_oidc_secret: typing.Optional[str] = OMIT,
        external_notion_enabled: typing.Optional[bool] = OMIT,
        external_notion_client_id: typing.Optional[str] = OMIT,
        external_notion_email_optional: typing.Optional[bool] = OMIT,
        external_notion_secret: typing.Optional[str] = OMIT,
        external_slack_enabled: typing.Optional[bool] = OMIT,
        external_slack_client_id: typing.Optional[str] = OMIT,
        external_slack_email_optional: typing.Optional[bool] = OMIT,
        external_slack_secret: typing.Optional[str] = OMIT,
        external_spotify_enabled: typing.Optional[bool] = OMIT,
        external_spotify_client_id: typing.Optional[str] = OMIT,
        external_spotify_email_optional: typing.Optional[bool] = OMIT,
        external_spotify_secret: typing.Optional[str] = OMIT,
        external_twitch_enabled: typing.Optional[bool] = OMIT,
        external_twitch_client_id: typing.Optional[str] = OMIT,
        external_twitch_email_optional: typing.Optional[bool] = OMIT,
        external_twitch_secret: typing.Optional[str] = OMIT,
        external_twitter_enabled: typing.Optional[bool] = OMIT,
        external_twitter_client_id: typing.Optional[str] = OMIT,
        external_twitter_email_optional: typing.Optional[bool] = OMIT,
        external_twitter_secret: typing.Optional[str] = OMIT,
        external_x_enabled: typing.Optional[bool] = OMIT,
        external_x_client_id: typing.Optional[str] = OMIT,
        external_x_email_optional: typing.Optional[bool] = OMIT,
        external_x_secret: typing.Optional[str] = OMIT,
        external_workos_enabled: typing.Optional[bool] = OMIT,
        external_workos_client_id: typing.Optional[str] = OMIT,
        external_workos_secret: typing.Optional[str] = OMIT,
        external_workos_url: typing.Optional[str] = OMIT,
        external_web3solana_enabled: typing.Optional[bool] = OMIT,
        external_web3ethereum_enabled: typing.Optional[bool] = OMIT,
        external_zoom_enabled: typing.Optional[bool] = OMIT,
        external_zoom_client_id: typing.Optional[str] = OMIT,
        external_zoom_email_optional: typing.Optional[bool] = OMIT,
        external_zoom_secret: typing.Optional[str] = OMIT,
        db_max_pool_size: typing.Optional[int] = OMIT,
        db_max_pool_size_unit: typing.Optional[UpdateAuthConfigBodyDbMaxPoolSizeUnit] = OMIT,
        api_max_request_duration: typing.Optional[int] = OMIT,
        mfa_totp_enroll_enabled: typing.Optional[bool] = OMIT,
        mfa_totp_verify_enabled: typing.Optional[bool] = OMIT,
        mfa_web_authn_enroll_enabled: typing.Optional[bool] = OMIT,
        mfa_web_authn_verify_enabled: typing.Optional[bool] = OMIT,
        passkey_enabled: typing.Optional[bool] = OMIT,
        webauthn_rp_display_name: typing.Optional[str] = OMIT,
        webauthn_rp_id: typing.Optional[str] = OMIT,
        webauthn_rp_origins: typing.Optional[str] = OMIT,
        mfa_phone_enroll_enabled: typing.Optional[bool] = OMIT,
        mfa_phone_verify_enabled: typing.Optional[bool] = OMIT,
        mfa_phone_max_frequency: typing.Optional[int] = OMIT,
        mfa_phone_otp_length: typing.Optional[int] = OMIT,
        mfa_phone_template: typing.Optional[str] = OMIT,
        nimbus_oauth_client_id: typing.Optional[str] = OMIT,
        nimbus_oauth_client_secret: typing.Optional[str] = OMIT,
        oauth_server_enabled: typing.Optional[bool] = OMIT,
        oauth_server_allow_dynamic_registration: typing.Optional[bool] = OMIT,
        oauth_server_authorization_path: typing.Optional[str] = OMIT,
        custom_oauth_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        site_url : typing.Optional[str]

        disable_signup : typing.Optional[bool]

        jwt_exp : typing.Optional[int]

        smtp_admin_email : typing.Optional[str]

        smtp_host : typing.Optional[str]

        smtp_port : typing.Optional[str]

        smtp_user : typing.Optional[str]

        smtp_pass : typing.Optional[str]

        smtp_max_frequency : typing.Optional[int]

        smtp_sender_name : typing.Optional[str]

        mailer_allow_unverified_email_sign_ins : typing.Optional[bool]

        mailer_autoconfirm : typing.Optional[bool]

        mailer_subjects_invite : typing.Optional[str]

        mailer_subjects_confirmation : typing.Optional[str]

        mailer_subjects_recovery : typing.Optional[str]

        mailer_subjects_email_change : typing.Optional[str]

        mailer_subjects_magic_link : typing.Optional[str]

        mailer_subjects_reauthentication : typing.Optional[str]

        mailer_subjects_password_changed_notification : typing.Optional[str]

        mailer_subjects_email_changed_notification : typing.Optional[str]

        mailer_subjects_phone_changed_notification : typing.Optional[str]

        mailer_subjects_mfa_factor_enrolled_notification : typing.Optional[str]

        mailer_subjects_mfa_factor_unenrolled_notification : typing.Optional[str]

        mailer_subjects_identity_linked_notification : typing.Optional[str]

        mailer_subjects_identity_unlinked_notification : typing.Optional[str]

        mailer_templates_invite_content : typing.Optional[str]

        mailer_templates_confirmation_content : typing.Optional[str]

        mailer_templates_recovery_content : typing.Optional[str]

        mailer_templates_email_change_content : typing.Optional[str]

        mailer_templates_magic_link_content : typing.Optional[str]

        mailer_templates_reauthentication_content : typing.Optional[str]

        mailer_templates_password_changed_notification_content : typing.Optional[str]

        mailer_templates_email_changed_notification_content : typing.Optional[str]

        mailer_templates_phone_changed_notification_content : typing.Optional[str]

        mailer_templates_mfa_factor_enrolled_notification_content : typing.Optional[str]

        mailer_templates_mfa_factor_unenrolled_notification_content : typing.Optional[str]

        mailer_templates_identity_linked_notification_content : typing.Optional[str]

        mailer_templates_identity_unlinked_notification_content : typing.Optional[str]

        mailer_notifications_password_changed_enabled : typing.Optional[bool]

        mailer_notifications_email_changed_enabled : typing.Optional[bool]

        mailer_notifications_phone_changed_enabled : typing.Optional[bool]

        mailer_notifications_mfa_factor_enrolled_enabled : typing.Optional[bool]

        mailer_notifications_mfa_factor_unenrolled_enabled : typing.Optional[bool]

        mailer_notifications_identity_linked_enabled : typing.Optional[bool]

        mailer_notifications_identity_unlinked_enabled : typing.Optional[bool]

        mfa_max_enrolled_factors : typing.Optional[int]

        uri_allow_list : typing.Optional[str]

        external_anonymous_users_enabled : typing.Optional[bool]

        external_email_enabled : typing.Optional[bool]

        external_phone_enabled : typing.Optional[bool]

        saml_enabled : typing.Optional[bool]

        saml_external_url : typing.Optional[str]

        security_sb_forwarded_for_enabled : typing.Optional[bool]

        security_captcha_enabled : typing.Optional[bool]

        security_captcha_provider : typing.Optional[UpdateAuthConfigBodySecurityCaptchaProvider]

        security_captcha_secret : typing.Optional[str]

        sessions_timebox : typing.Optional[float]
            Session timebox in hours. Maximum 8760 hours (1 year).

        sessions_inactivity_timeout : typing.Optional[float]
            Session inactivity timeout in hours. Maximum 8760 hours (1 year).

        sessions_single_per_user : typing.Optional[bool]

        sessions_tags : typing.Optional[str]

        rate_limit_anonymous_users : typing.Optional[int]

        rate_limit_email_sent : typing.Optional[int]

        rate_limit_sms_sent : typing.Optional[int]

        rate_limit_verify : typing.Optional[int]

        rate_limit_token_refresh : typing.Optional[int]

        rate_limit_otp : typing.Optional[int]

        rate_limit_web3 : typing.Optional[int]

        mailer_secure_email_change_enabled : typing.Optional[bool]

        refresh_token_rotation_enabled : typing.Optional[bool]

        password_hibp_enabled : typing.Optional[bool]

        password_min_length : typing.Optional[int]

        password_required_characters : typing.Optional[UpdateAuthConfigBodyPasswordRequiredCharacters]

        security_manual_linking_enabled : typing.Optional[bool]

        security_update_password_require_reauthentication : typing.Optional[bool]

        security_update_password_require_current_password : typing.Optional[bool]
            Require the user's current password when updating their password.

        security_refresh_token_reuse_interval : typing.Optional[int]
            Refresh token reuse interval in seconds. Maximum 300 seconds (5 minutes).

        mailer_otp_exp : typing.Optional[int]

        mailer_otp_length : typing.Optional[int]

        sms_autoconfirm : typing.Optional[bool]

        sms_max_frequency : typing.Optional[int]

        sms_otp_exp : typing.Optional[int]

        sms_otp_length : typing.Optional[int]

        sms_provider : typing.Optional[UpdateAuthConfigBodySmsProvider]

        sms_messagebird_access_key : typing.Optional[str]

        sms_messagebird_originator : typing.Optional[str]

        sms_test_otp : typing.Optional[str]

        sms_test_otp_valid_until : typing.Optional[dt.datetime]

        sms_textlocal_api_key : typing.Optional[str]

        sms_textlocal_sender : typing.Optional[str]

        sms_twilio_account_sid : typing.Optional[str]

        sms_twilio_auth_token : typing.Optional[str]

        sms_twilio_content_sid : typing.Optional[str]

        sms_twilio_message_service_sid : typing.Optional[str]

        sms_twilio_verify_account_sid : typing.Optional[str]

        sms_twilio_verify_auth_token : typing.Optional[str]

        sms_twilio_verify_message_service_sid : typing.Optional[str]

        sms_vonage_api_key : typing.Optional[str]

        sms_vonage_api_secret : typing.Optional[str]

        sms_vonage_from : typing.Optional[str]

        sms_template : typing.Optional[str]

        hook_mfa_verification_attempt_enabled : typing.Optional[bool]

        hook_mfa_verification_attempt_uri : typing.Optional[str]

        hook_mfa_verification_attempt_secrets : typing.Optional[str]

        hook_password_verification_attempt_enabled : typing.Optional[bool]

        hook_password_verification_attempt_uri : typing.Optional[str]

        hook_password_verification_attempt_secrets : typing.Optional[str]

        hook_custom_access_token_enabled : typing.Optional[bool]

        hook_custom_access_token_uri : typing.Optional[str]

        hook_custom_access_token_secrets : typing.Optional[str]

        hook_send_sms_enabled : typing.Optional[bool]

        hook_send_sms_uri : typing.Optional[str]

        hook_send_sms_secrets : typing.Optional[str]

        hook_send_email_enabled : typing.Optional[bool]

        hook_send_email_uri : typing.Optional[str]

        hook_send_email_secrets : typing.Optional[str]

        hook_before_user_created_enabled : typing.Optional[bool]

        hook_before_user_created_uri : typing.Optional[str]

        hook_before_user_created_secrets : typing.Optional[str]

        hook_after_user_created_enabled : typing.Optional[bool]

        hook_after_user_created_uri : typing.Optional[str]

        hook_after_user_created_secrets : typing.Optional[str]

        external_apple_enabled : typing.Optional[bool]

        external_apple_client_id : typing.Optional[str]

        external_apple_email_optional : typing.Optional[bool]

        external_apple_secret : typing.Optional[str]

        external_apple_additional_client_ids : typing.Optional[str]

        external_azure_enabled : typing.Optional[bool]

        external_azure_client_id : typing.Optional[str]

        external_azure_email_optional : typing.Optional[bool]

        external_azure_secret : typing.Optional[str]

        external_azure_url : typing.Optional[str]

        external_bitbucket_enabled : typing.Optional[bool]

        external_bitbucket_client_id : typing.Optional[str]

        external_bitbucket_email_optional : typing.Optional[bool]

        external_bitbucket_secret : typing.Optional[str]

        external_discord_enabled : typing.Optional[bool]

        external_discord_client_id : typing.Optional[str]

        external_discord_email_optional : typing.Optional[bool]

        external_discord_secret : typing.Optional[str]

        external_facebook_enabled : typing.Optional[bool]

        external_facebook_client_id : typing.Optional[str]

        external_facebook_email_optional : typing.Optional[bool]

        external_facebook_secret : typing.Optional[str]

        external_figma_enabled : typing.Optional[bool]

        external_figma_client_id : typing.Optional[str]

        external_figma_email_optional : typing.Optional[bool]

        external_figma_secret : typing.Optional[str]

        external_github_enabled : typing.Optional[bool]

        external_github_client_id : typing.Optional[str]

        external_github_email_optional : typing.Optional[bool]

        external_github_secret : typing.Optional[str]

        external_gitlab_enabled : typing.Optional[bool]

        external_gitlab_client_id : typing.Optional[str]

        external_gitlab_email_optional : typing.Optional[bool]

        external_gitlab_secret : typing.Optional[str]

        external_gitlab_url : typing.Optional[str]

        external_google_enabled : typing.Optional[bool]

        external_google_client_id : typing.Optional[str]

        external_google_email_optional : typing.Optional[bool]

        external_google_secret : typing.Optional[str]

        external_google_additional_client_ids : typing.Optional[str]

        external_google_skip_nonce_check : typing.Optional[bool]

        external_kakao_enabled : typing.Optional[bool]

        external_kakao_client_id : typing.Optional[str]

        external_kakao_email_optional : typing.Optional[bool]

        external_kakao_secret : typing.Optional[str]

        external_keycloak_enabled : typing.Optional[bool]

        external_keycloak_client_id : typing.Optional[str]

        external_keycloak_email_optional : typing.Optional[bool]

        external_keycloak_secret : typing.Optional[str]

        external_keycloak_url : typing.Optional[str]

        external_linkedin_oidc_enabled : typing.Optional[bool]

        external_linkedin_oidc_client_id : typing.Optional[str]

        external_linkedin_oidc_email_optional : typing.Optional[bool]

        external_linkedin_oidc_secret : typing.Optional[str]

        external_slack_oidc_enabled : typing.Optional[bool]

        external_slack_oidc_client_id : typing.Optional[str]

        external_slack_oidc_email_optional : typing.Optional[bool]

        external_slack_oidc_secret : typing.Optional[str]

        external_notion_enabled : typing.Optional[bool]

        external_notion_client_id : typing.Optional[str]

        external_notion_email_optional : typing.Optional[bool]

        external_notion_secret : typing.Optional[str]

        external_slack_enabled : typing.Optional[bool]

        external_slack_client_id : typing.Optional[str]

        external_slack_email_optional : typing.Optional[bool]

        external_slack_secret : typing.Optional[str]

        external_spotify_enabled : typing.Optional[bool]

        external_spotify_client_id : typing.Optional[str]

        external_spotify_email_optional : typing.Optional[bool]

        external_spotify_secret : typing.Optional[str]

        external_twitch_enabled : typing.Optional[bool]

        external_twitch_client_id : typing.Optional[str]

        external_twitch_email_optional : typing.Optional[bool]

        external_twitch_secret : typing.Optional[str]

        external_twitter_enabled : typing.Optional[bool]

        external_twitter_client_id : typing.Optional[str]

        external_twitter_email_optional : typing.Optional[bool]

        external_twitter_secret : typing.Optional[str]

        external_x_enabled : typing.Optional[bool]

        external_x_client_id : typing.Optional[str]

        external_x_email_optional : typing.Optional[bool]

        external_x_secret : typing.Optional[str]

        external_workos_enabled : typing.Optional[bool]

        external_workos_client_id : typing.Optional[str]

        external_workos_secret : typing.Optional[str]

        external_workos_url : typing.Optional[str]

        external_web3solana_enabled : typing.Optional[bool]

        external_web3ethereum_enabled : typing.Optional[bool]

        external_zoom_enabled : typing.Optional[bool]

        external_zoom_client_id : typing.Optional[str]

        external_zoom_email_optional : typing.Optional[bool]

        external_zoom_secret : typing.Optional[str]

        db_max_pool_size : typing.Optional[int]

        db_max_pool_size_unit : typing.Optional[UpdateAuthConfigBodyDbMaxPoolSizeUnit]

        api_max_request_duration : typing.Optional[int]

        mfa_totp_enroll_enabled : typing.Optional[bool]

        mfa_totp_verify_enabled : typing.Optional[bool]

        mfa_web_authn_enroll_enabled : typing.Optional[bool]

        mfa_web_authn_verify_enabled : typing.Optional[bool]

        passkey_enabled : typing.Optional[bool]

        webauthn_rp_display_name : typing.Optional[str]

        webauthn_rp_id : typing.Optional[str]

        webauthn_rp_origins : typing.Optional[str]

        mfa_phone_enroll_enabled : typing.Optional[bool]

        mfa_phone_verify_enabled : typing.Optional[bool]

        mfa_phone_max_frequency : typing.Optional[int]

        mfa_phone_otp_length : typing.Optional[int]

        mfa_phone_template : typing.Optional[str]

        nimbus_oauth_client_id : typing.Optional[str]

        nimbus_oauth_client_secret : typing.Optional[str]

        oauth_server_enabled : typing.Optional[bool]

        oauth_server_allow_dynamic_registration : typing.Optional[bool]

        oauth_server_authorization_path : typing.Optional[str]

        custom_oauth_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthConfigResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1update_auth_service_config(
            ref="abcdefghijklmnopqrst",
            site_url="https://app.example.com",
            disable_signup=False,
            jwt_exp=3600,
        )
        """
        _response = self._raw_client.v1update_auth_service_config(
            ref,
            site_url=site_url,
            disable_signup=disable_signup,
            jwt_exp=jwt_exp,
            smtp_admin_email=smtp_admin_email,
            smtp_host=smtp_host,
            smtp_port=smtp_port,
            smtp_user=smtp_user,
            smtp_pass=smtp_pass,
            smtp_max_frequency=smtp_max_frequency,
            smtp_sender_name=smtp_sender_name,
            mailer_allow_unverified_email_sign_ins=mailer_allow_unverified_email_sign_ins,
            mailer_autoconfirm=mailer_autoconfirm,
            mailer_subjects_invite=mailer_subjects_invite,
            mailer_subjects_confirmation=mailer_subjects_confirmation,
            mailer_subjects_recovery=mailer_subjects_recovery,
            mailer_subjects_email_change=mailer_subjects_email_change,
            mailer_subjects_magic_link=mailer_subjects_magic_link,
            mailer_subjects_reauthentication=mailer_subjects_reauthentication,
            mailer_subjects_password_changed_notification=mailer_subjects_password_changed_notification,
            mailer_subjects_email_changed_notification=mailer_subjects_email_changed_notification,
            mailer_subjects_phone_changed_notification=mailer_subjects_phone_changed_notification,
            mailer_subjects_mfa_factor_enrolled_notification=mailer_subjects_mfa_factor_enrolled_notification,
            mailer_subjects_mfa_factor_unenrolled_notification=mailer_subjects_mfa_factor_unenrolled_notification,
            mailer_subjects_identity_linked_notification=mailer_subjects_identity_linked_notification,
            mailer_subjects_identity_unlinked_notification=mailer_subjects_identity_unlinked_notification,
            mailer_templates_invite_content=mailer_templates_invite_content,
            mailer_templates_confirmation_content=mailer_templates_confirmation_content,
            mailer_templates_recovery_content=mailer_templates_recovery_content,
            mailer_templates_email_change_content=mailer_templates_email_change_content,
            mailer_templates_magic_link_content=mailer_templates_magic_link_content,
            mailer_templates_reauthentication_content=mailer_templates_reauthentication_content,
            mailer_templates_password_changed_notification_content=mailer_templates_password_changed_notification_content,
            mailer_templates_email_changed_notification_content=mailer_templates_email_changed_notification_content,
            mailer_templates_phone_changed_notification_content=mailer_templates_phone_changed_notification_content,
            mailer_templates_mfa_factor_enrolled_notification_content=mailer_templates_mfa_factor_enrolled_notification_content,
            mailer_templates_mfa_factor_unenrolled_notification_content=mailer_templates_mfa_factor_unenrolled_notification_content,
            mailer_templates_identity_linked_notification_content=mailer_templates_identity_linked_notification_content,
            mailer_templates_identity_unlinked_notification_content=mailer_templates_identity_unlinked_notification_content,
            mailer_notifications_password_changed_enabled=mailer_notifications_password_changed_enabled,
            mailer_notifications_email_changed_enabled=mailer_notifications_email_changed_enabled,
            mailer_notifications_phone_changed_enabled=mailer_notifications_phone_changed_enabled,
            mailer_notifications_mfa_factor_enrolled_enabled=mailer_notifications_mfa_factor_enrolled_enabled,
            mailer_notifications_mfa_factor_unenrolled_enabled=mailer_notifications_mfa_factor_unenrolled_enabled,
            mailer_notifications_identity_linked_enabled=mailer_notifications_identity_linked_enabled,
            mailer_notifications_identity_unlinked_enabled=mailer_notifications_identity_unlinked_enabled,
            mfa_max_enrolled_factors=mfa_max_enrolled_factors,
            uri_allow_list=uri_allow_list,
            external_anonymous_users_enabled=external_anonymous_users_enabled,
            external_email_enabled=external_email_enabled,
            external_phone_enabled=external_phone_enabled,
            saml_enabled=saml_enabled,
            saml_external_url=saml_external_url,
            security_sb_forwarded_for_enabled=security_sb_forwarded_for_enabled,
            security_captcha_enabled=security_captcha_enabled,
            security_captcha_provider=security_captcha_provider,
            security_captcha_secret=security_captcha_secret,
            sessions_timebox=sessions_timebox,
            sessions_inactivity_timeout=sessions_inactivity_timeout,
            sessions_single_per_user=sessions_single_per_user,
            sessions_tags=sessions_tags,
            rate_limit_anonymous_users=rate_limit_anonymous_users,
            rate_limit_email_sent=rate_limit_email_sent,
            rate_limit_sms_sent=rate_limit_sms_sent,
            rate_limit_verify=rate_limit_verify,
            rate_limit_token_refresh=rate_limit_token_refresh,
            rate_limit_otp=rate_limit_otp,
            rate_limit_web3=rate_limit_web3,
            mailer_secure_email_change_enabled=mailer_secure_email_change_enabled,
            refresh_token_rotation_enabled=refresh_token_rotation_enabled,
            password_hibp_enabled=password_hibp_enabled,
            password_min_length=password_min_length,
            password_required_characters=password_required_characters,
            security_manual_linking_enabled=security_manual_linking_enabled,
            security_update_password_require_reauthentication=security_update_password_require_reauthentication,
            security_update_password_require_current_password=security_update_password_require_current_password,
            security_refresh_token_reuse_interval=security_refresh_token_reuse_interval,
            mailer_otp_exp=mailer_otp_exp,
            mailer_otp_length=mailer_otp_length,
            sms_autoconfirm=sms_autoconfirm,
            sms_max_frequency=sms_max_frequency,
            sms_otp_exp=sms_otp_exp,
            sms_otp_length=sms_otp_length,
            sms_provider=sms_provider,
            sms_messagebird_access_key=sms_messagebird_access_key,
            sms_messagebird_originator=sms_messagebird_originator,
            sms_test_otp=sms_test_otp,
            sms_test_otp_valid_until=sms_test_otp_valid_until,
            sms_textlocal_api_key=sms_textlocal_api_key,
            sms_textlocal_sender=sms_textlocal_sender,
            sms_twilio_account_sid=sms_twilio_account_sid,
            sms_twilio_auth_token=sms_twilio_auth_token,
            sms_twilio_content_sid=sms_twilio_content_sid,
            sms_twilio_message_service_sid=sms_twilio_message_service_sid,
            sms_twilio_verify_account_sid=sms_twilio_verify_account_sid,
            sms_twilio_verify_auth_token=sms_twilio_verify_auth_token,
            sms_twilio_verify_message_service_sid=sms_twilio_verify_message_service_sid,
            sms_vonage_api_key=sms_vonage_api_key,
            sms_vonage_api_secret=sms_vonage_api_secret,
            sms_vonage_from=sms_vonage_from,
            sms_template=sms_template,
            hook_mfa_verification_attempt_enabled=hook_mfa_verification_attempt_enabled,
            hook_mfa_verification_attempt_uri=hook_mfa_verification_attempt_uri,
            hook_mfa_verification_attempt_secrets=hook_mfa_verification_attempt_secrets,
            hook_password_verification_attempt_enabled=hook_password_verification_attempt_enabled,
            hook_password_verification_attempt_uri=hook_password_verification_attempt_uri,
            hook_password_verification_attempt_secrets=hook_password_verification_attempt_secrets,
            hook_custom_access_token_enabled=hook_custom_access_token_enabled,
            hook_custom_access_token_uri=hook_custom_access_token_uri,
            hook_custom_access_token_secrets=hook_custom_access_token_secrets,
            hook_send_sms_enabled=hook_send_sms_enabled,
            hook_send_sms_uri=hook_send_sms_uri,
            hook_send_sms_secrets=hook_send_sms_secrets,
            hook_send_email_enabled=hook_send_email_enabled,
            hook_send_email_uri=hook_send_email_uri,
            hook_send_email_secrets=hook_send_email_secrets,
            hook_before_user_created_enabled=hook_before_user_created_enabled,
            hook_before_user_created_uri=hook_before_user_created_uri,
            hook_before_user_created_secrets=hook_before_user_created_secrets,
            hook_after_user_created_enabled=hook_after_user_created_enabled,
            hook_after_user_created_uri=hook_after_user_created_uri,
            hook_after_user_created_secrets=hook_after_user_created_secrets,
            external_apple_enabled=external_apple_enabled,
            external_apple_client_id=external_apple_client_id,
            external_apple_email_optional=external_apple_email_optional,
            external_apple_secret=external_apple_secret,
            external_apple_additional_client_ids=external_apple_additional_client_ids,
            external_azure_enabled=external_azure_enabled,
            external_azure_client_id=external_azure_client_id,
            external_azure_email_optional=external_azure_email_optional,
            external_azure_secret=external_azure_secret,
            external_azure_url=external_azure_url,
            external_bitbucket_enabled=external_bitbucket_enabled,
            external_bitbucket_client_id=external_bitbucket_client_id,
            external_bitbucket_email_optional=external_bitbucket_email_optional,
            external_bitbucket_secret=external_bitbucket_secret,
            external_discord_enabled=external_discord_enabled,
            external_discord_client_id=external_discord_client_id,
            external_discord_email_optional=external_discord_email_optional,
            external_discord_secret=external_discord_secret,
            external_facebook_enabled=external_facebook_enabled,
            external_facebook_client_id=external_facebook_client_id,
            external_facebook_email_optional=external_facebook_email_optional,
            external_facebook_secret=external_facebook_secret,
            external_figma_enabled=external_figma_enabled,
            external_figma_client_id=external_figma_client_id,
            external_figma_email_optional=external_figma_email_optional,
            external_figma_secret=external_figma_secret,
            external_github_enabled=external_github_enabled,
            external_github_client_id=external_github_client_id,
            external_github_email_optional=external_github_email_optional,
            external_github_secret=external_github_secret,
            external_gitlab_enabled=external_gitlab_enabled,
            external_gitlab_client_id=external_gitlab_client_id,
            external_gitlab_email_optional=external_gitlab_email_optional,
            external_gitlab_secret=external_gitlab_secret,
            external_gitlab_url=external_gitlab_url,
            external_google_enabled=external_google_enabled,
            external_google_client_id=external_google_client_id,
            external_google_email_optional=external_google_email_optional,
            external_google_secret=external_google_secret,
            external_google_additional_client_ids=external_google_additional_client_ids,
            external_google_skip_nonce_check=external_google_skip_nonce_check,
            external_kakao_enabled=external_kakao_enabled,
            external_kakao_client_id=external_kakao_client_id,
            external_kakao_email_optional=external_kakao_email_optional,
            external_kakao_secret=external_kakao_secret,
            external_keycloak_enabled=external_keycloak_enabled,
            external_keycloak_client_id=external_keycloak_client_id,
            external_keycloak_email_optional=external_keycloak_email_optional,
            external_keycloak_secret=external_keycloak_secret,
            external_keycloak_url=external_keycloak_url,
            external_linkedin_oidc_enabled=external_linkedin_oidc_enabled,
            external_linkedin_oidc_client_id=external_linkedin_oidc_client_id,
            external_linkedin_oidc_email_optional=external_linkedin_oidc_email_optional,
            external_linkedin_oidc_secret=external_linkedin_oidc_secret,
            external_slack_oidc_enabled=external_slack_oidc_enabled,
            external_slack_oidc_client_id=external_slack_oidc_client_id,
            external_slack_oidc_email_optional=external_slack_oidc_email_optional,
            external_slack_oidc_secret=external_slack_oidc_secret,
            external_notion_enabled=external_notion_enabled,
            external_notion_client_id=external_notion_client_id,
            external_notion_email_optional=external_notion_email_optional,
            external_notion_secret=external_notion_secret,
            external_slack_enabled=external_slack_enabled,
            external_slack_client_id=external_slack_client_id,
            external_slack_email_optional=external_slack_email_optional,
            external_slack_secret=external_slack_secret,
            external_spotify_enabled=external_spotify_enabled,
            external_spotify_client_id=external_spotify_client_id,
            external_spotify_email_optional=external_spotify_email_optional,
            external_spotify_secret=external_spotify_secret,
            external_twitch_enabled=external_twitch_enabled,
            external_twitch_client_id=external_twitch_client_id,
            external_twitch_email_optional=external_twitch_email_optional,
            external_twitch_secret=external_twitch_secret,
            external_twitter_enabled=external_twitter_enabled,
            external_twitter_client_id=external_twitter_client_id,
            external_twitter_email_optional=external_twitter_email_optional,
            external_twitter_secret=external_twitter_secret,
            external_x_enabled=external_x_enabled,
            external_x_client_id=external_x_client_id,
            external_x_email_optional=external_x_email_optional,
            external_x_secret=external_x_secret,
            external_workos_enabled=external_workos_enabled,
            external_workos_client_id=external_workos_client_id,
            external_workos_secret=external_workos_secret,
            external_workos_url=external_workos_url,
            external_web3solana_enabled=external_web3solana_enabled,
            external_web3ethereum_enabled=external_web3ethereum_enabled,
            external_zoom_enabled=external_zoom_enabled,
            external_zoom_client_id=external_zoom_client_id,
            external_zoom_email_optional=external_zoom_email_optional,
            external_zoom_secret=external_zoom_secret,
            db_max_pool_size=db_max_pool_size,
            db_max_pool_size_unit=db_max_pool_size_unit,
            api_max_request_duration=api_max_request_duration,
            mfa_totp_enroll_enabled=mfa_totp_enroll_enabled,
            mfa_totp_verify_enabled=mfa_totp_verify_enabled,
            mfa_web_authn_enroll_enabled=mfa_web_authn_enroll_enabled,
            mfa_web_authn_verify_enabled=mfa_web_authn_verify_enabled,
            passkey_enabled=passkey_enabled,
            webauthn_rp_display_name=webauthn_rp_display_name,
            webauthn_rp_id=webauthn_rp_id,
            webauthn_rp_origins=webauthn_rp_origins,
            mfa_phone_enroll_enabled=mfa_phone_enroll_enabled,
            mfa_phone_verify_enabled=mfa_phone_verify_enabled,
            mfa_phone_max_frequency=mfa_phone_max_frequency,
            mfa_phone_otp_length=mfa_phone_otp_length,
            mfa_phone_template=mfa_phone_template,
            nimbus_oauth_client_id=nimbus_oauth_client_id,
            nimbus_oauth_client_secret=nimbus_oauth_client_secret,
            oauth_server_enabled=oauth_server_enabled,
            oauth_server_allow_dynamic_registration=oauth_server_allow_dynamic_registration,
            oauth_server_authorization_path=oauth_server_authorization_path,
            custom_oauth_enabled=custom_oauth_enabled,
            request_options=request_options,
        )
        return _response.data

    def v1list_project_tpa_integrations(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ThirdPartyAuthOutput]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThirdPartyAuthOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1list_project_tpa_integrations(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_project_tpa_integrations(ref, request_options=request_options)
        return _response.data

    def v1create_project_tpa_integration(
        self,
        ref: str,
        *,
        oidc_issuer_url: typing.Optional[str] = OMIT,
        jwks_url: typing.Optional[str] = OMIT,
        custom_jwks: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThirdPartyAuthOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        oidc_issuer_url : typing.Optional[str]

        jwks_url : typing.Optional[str]

        custom_jwks : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThirdPartyAuthOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1create_project_tpa_integration(
            ref="abcdefghijklmnopqrst",
            oidc_issuer_url="https://login.acme.com",
            jwks_url="https://login.acme.com/.well-known/jwks.json",
        )
        """
        _response = self._raw_client.v1create_project_tpa_integration(
            ref,
            oidc_issuer_url=oidc_issuer_url,
            jwks_url=jwks_url,
            custom_jwks=custom_jwks,
            request_options=request_options,
        )
        return _response.data

    def v1get_project_tpa_integration(
        self, ref: str, tpa_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThirdPartyAuthOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        tpa_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThirdPartyAuthOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1get_project_tpa_integration(
            ref="abcdefghijklmnopqrst",
            tpa_id="88888888-8888-4888-8888-888888888888",
        )
        """
        _response = self._raw_client.v1get_project_tpa_integration(ref, tpa_id, request_options=request_options)
        return _response.data

    def v1delete_project_tpa_integration(
        self, ref: str, tpa_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThirdPartyAuthOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        tpa_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThirdPartyAuthOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1delete_project_tpa_integration(
            ref="abcdefghijklmnopqrst",
            tpa_id="88888888-8888-4888-8888-888888888888",
        )
        """
        _response = self._raw_client.v1delete_project_tpa_integration(ref, tpa_id, request_options=request_options)
        return _response.data

    def v1list_all_sso_provider(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListProvidersResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProvidersResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1list_all_sso_provider(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_all_sso_provider(ref, request_options=request_options)
        return _response.data

    def v1create_a_sso_provider(
        self,
        ref: str,
        *,
        type: CreateProviderBodyType,
        metadata_xml: typing.Optional[str] = OMIT,
        metadata_url: typing.Optional[str] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        attribute_mapping: typing.Optional[CreateProviderBodyAttributeMapping] = OMIT,
        name_id_format: typing.Optional[CreateProviderBodyNameIdFormat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateProviderResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        type : CreateProviderBodyType
            What type of provider will be created

        metadata_xml : typing.Optional[str]

        metadata_url : typing.Optional[str]

        domains : typing.Optional[typing.Sequence[str]]

        attribute_mapping : typing.Optional[CreateProviderBodyAttributeMapping]

        name_id_format : typing.Optional[CreateProviderBodyNameIdFormat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProviderResponseOutput


        Examples
        --------
        from fern.auth import (
            CreateProviderBodyAttributeMapping,
            CreateProviderBodyAttributeMappingKeysValue,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1create_a_sso_provider(
            ref="abcdefghijklmnopqrst",
            type="saml",
            metadata_url="https://sso.acme.com/metadata.xml",
            domains=["acme.com"],
            attribute_mapping=CreateProviderBodyAttributeMapping(
                keys={
                    "email": CreateProviderBodyAttributeMappingKeysValue(
                        name="email",
                    ),
                    "first_name": CreateProviderBodyAttributeMappingKeysValue(
                        name="first_name",
                    ),
                    "last_name": CreateProviderBodyAttributeMappingKeysValue(
                        name="last_name",
                    ),
                },
            ),
        )
        """
        _response = self._raw_client.v1create_a_sso_provider(
            ref,
            type=type,
            metadata_xml=metadata_xml,
            metadata_url=metadata_url,
            domains=domains,
            attribute_mapping=attribute_mapping,
            name_id_format=name_id_format,
            request_options=request_options,
        )
        return _response.data

    def v1get_a_sso_provider(
        self, ref: str, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProviderResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProviderResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1get_a_sso_provider(
            ref="abcdefghijklmnopqrst",
            provider_id="77777777-7777-4777-8777-777777777777",
        )
        """
        _response = self._raw_client.v1get_a_sso_provider(ref, provider_id, request_options=request_options)
        return _response.data

    def v1update_a_sso_provider(
        self,
        ref: str,
        provider_id: str,
        *,
        metadata_xml: typing.Optional[str] = OMIT,
        metadata_url: typing.Optional[str] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        attribute_mapping: typing.Optional[UpdateProviderBodyAttributeMapping] = OMIT,
        name_id_format: typing.Optional[UpdateProviderBodyNameIdFormat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateProviderResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        provider_id : str

        metadata_xml : typing.Optional[str]

        metadata_url : typing.Optional[str]

        domains : typing.Optional[typing.Sequence[str]]

        attribute_mapping : typing.Optional[UpdateProviderBodyAttributeMapping]

        name_id_format : typing.Optional[UpdateProviderBodyNameIdFormat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateProviderResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1update_a_sso_provider(
            ref="abcdefghijklmnopqrst",
            provider_id="77777777-7777-4777-8777-777777777777",
            metadata_url="https://sso.acme.com/metadata.xml",
            domains=["acme.com", "contractors.acme.com"],
        )
        """
        _response = self._raw_client.v1update_a_sso_provider(
            ref,
            provider_id,
            metadata_xml=metadata_xml,
            metadata_url=metadata_url,
            domains=domains,
            attribute_mapping=attribute_mapping,
            name_id_format=name_id_format,
            request_options=request_options,
        )
        return _response.data

    def v1delete_a_sso_provider(
        self, ref: str, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteProviderResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteProviderResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.auth.v1delete_a_sso_provider(
            ref="abcdefghijklmnopqrst",
            provider_id="77777777-7777-4777-8777-777777777777",
        )
        """
        _response = self._raw_client.v1delete_a_sso_provider(ref, provider_id, request_options=request_options)
        return _response.data


class AsyncAuthClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuthClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuthClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuthClient
        """
        return self._raw_client

    async def v1get_legacy_signing_key(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SigningKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeyResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1get_legacy_signing_key(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_legacy_signing_key(ref, request_options=request_options)
        return _response.data

    async def v1create_legacy_signing_key(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SigningKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeyResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1create_legacy_signing_key(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1create_legacy_signing_key(ref, request_options=request_options)
        return _response.data

    async def v1get_project_signing_keys(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SigningKeysResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeysResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1get_project_signing_keys(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_signing_keys(ref, request_options=request_options)
        return _response.data

    async def v1create_project_signing_key(
        self,
        ref: str,
        *,
        algorithm: CreateSigningKeyBodyAlgorithm,
        status: typing.Optional[CreateSigningKeyBodyStatus] = OMIT,
        private_jwk: typing.Optional[CreateSigningKeyBodyPrivateJwk] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SigningKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        algorithm : CreateSigningKeyBodyAlgorithm

        status : typing.Optional[CreateSigningKeyBodyStatus]

        private_jwk : typing.Optional[CreateSigningKeyBodyPrivateJwk]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeyResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1create_project_signing_key(
                ref="abcdefghijklmnopqrst",
                algorithm="RS256",
                status="standby",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1create_project_signing_key(
            ref, algorithm=algorithm, status=status, private_jwk=private_jwk, request_options=request_options
        )
        return _response.data

    async def v1get_project_signing_key(
        self, ref: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SigningKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeyResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1get_project_signing_key(
                ref="abcdefghijklmnopqrst",
                id="33333333-3333-4333-8333-333333333333",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_signing_key(ref, id, request_options=request_options)
        return _response.data

    async def v1remove_project_signing_key(
        self, ref: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SigningKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeyResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1remove_project_signing_key(
                ref="abcdefghijklmnopqrst",
                id="33333333-3333-4333-8333-333333333333",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1remove_project_signing_key(ref, id, request_options=request_options)
        return _response.data

    async def v1update_project_signing_key(
        self,
        ref: str,
        id: str,
        *,
        status: UpdateSigningKeyBodyStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SigningKeyResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : str

        status : UpdateSigningKeyBodyStatus

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SigningKeyResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1update_project_signing_key(
                ref="abcdefghijklmnopqrst",
                id="33333333-3333-4333-8333-333333333333",
                status="standby",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_project_signing_key(
            ref, id, status=status, request_options=request_options
        )
        return _response.data

    async def v1get_auth_service_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AuthConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthConfigResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1get_auth_service_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_auth_service_config(ref, request_options=request_options)
        return _response.data

    async def v1update_auth_service_config(
        self,
        ref: str,
        *,
        site_url: typing.Optional[str] = OMIT,
        disable_signup: typing.Optional[bool] = OMIT,
        jwt_exp: typing.Optional[int] = OMIT,
        smtp_admin_email: typing.Optional[str] = OMIT,
        smtp_host: typing.Optional[str] = OMIT,
        smtp_port: typing.Optional[str] = OMIT,
        smtp_user: typing.Optional[str] = OMIT,
        smtp_pass: typing.Optional[str] = OMIT,
        smtp_max_frequency: typing.Optional[int] = OMIT,
        smtp_sender_name: typing.Optional[str] = OMIT,
        mailer_allow_unverified_email_sign_ins: typing.Optional[bool] = OMIT,
        mailer_autoconfirm: typing.Optional[bool] = OMIT,
        mailer_subjects_invite: typing.Optional[str] = OMIT,
        mailer_subjects_confirmation: typing.Optional[str] = OMIT,
        mailer_subjects_recovery: typing.Optional[str] = OMIT,
        mailer_subjects_email_change: typing.Optional[str] = OMIT,
        mailer_subjects_magic_link: typing.Optional[str] = OMIT,
        mailer_subjects_reauthentication: typing.Optional[str] = OMIT,
        mailer_subjects_password_changed_notification: typing.Optional[str] = OMIT,
        mailer_subjects_email_changed_notification: typing.Optional[str] = OMIT,
        mailer_subjects_phone_changed_notification: typing.Optional[str] = OMIT,
        mailer_subjects_mfa_factor_enrolled_notification: typing.Optional[str] = OMIT,
        mailer_subjects_mfa_factor_unenrolled_notification: typing.Optional[str] = OMIT,
        mailer_subjects_identity_linked_notification: typing.Optional[str] = OMIT,
        mailer_subjects_identity_unlinked_notification: typing.Optional[str] = OMIT,
        mailer_templates_invite_content: typing.Optional[str] = OMIT,
        mailer_templates_confirmation_content: typing.Optional[str] = OMIT,
        mailer_templates_recovery_content: typing.Optional[str] = OMIT,
        mailer_templates_email_change_content: typing.Optional[str] = OMIT,
        mailer_templates_magic_link_content: typing.Optional[str] = OMIT,
        mailer_templates_reauthentication_content: typing.Optional[str] = OMIT,
        mailer_templates_password_changed_notification_content: typing.Optional[str] = OMIT,
        mailer_templates_email_changed_notification_content: typing.Optional[str] = OMIT,
        mailer_templates_phone_changed_notification_content: typing.Optional[str] = OMIT,
        mailer_templates_mfa_factor_enrolled_notification_content: typing.Optional[str] = OMIT,
        mailer_templates_mfa_factor_unenrolled_notification_content: typing.Optional[str] = OMIT,
        mailer_templates_identity_linked_notification_content: typing.Optional[str] = OMIT,
        mailer_templates_identity_unlinked_notification_content: typing.Optional[str] = OMIT,
        mailer_notifications_password_changed_enabled: typing.Optional[bool] = OMIT,
        mailer_notifications_email_changed_enabled: typing.Optional[bool] = OMIT,
        mailer_notifications_phone_changed_enabled: typing.Optional[bool] = OMIT,
        mailer_notifications_mfa_factor_enrolled_enabled: typing.Optional[bool] = OMIT,
        mailer_notifications_mfa_factor_unenrolled_enabled: typing.Optional[bool] = OMIT,
        mailer_notifications_identity_linked_enabled: typing.Optional[bool] = OMIT,
        mailer_notifications_identity_unlinked_enabled: typing.Optional[bool] = OMIT,
        mfa_max_enrolled_factors: typing.Optional[int] = OMIT,
        uri_allow_list: typing.Optional[str] = OMIT,
        external_anonymous_users_enabled: typing.Optional[bool] = OMIT,
        external_email_enabled: typing.Optional[bool] = OMIT,
        external_phone_enabled: typing.Optional[bool] = OMIT,
        saml_enabled: typing.Optional[bool] = OMIT,
        saml_external_url: typing.Optional[str] = OMIT,
        security_sb_forwarded_for_enabled: typing.Optional[bool] = OMIT,
        security_captcha_enabled: typing.Optional[bool] = OMIT,
        security_captcha_provider: typing.Optional[UpdateAuthConfigBodySecurityCaptchaProvider] = OMIT,
        security_captcha_secret: typing.Optional[str] = OMIT,
        sessions_timebox: typing.Optional[float] = OMIT,
        sessions_inactivity_timeout: typing.Optional[float] = OMIT,
        sessions_single_per_user: typing.Optional[bool] = OMIT,
        sessions_tags: typing.Optional[str] = OMIT,
        rate_limit_anonymous_users: typing.Optional[int] = OMIT,
        rate_limit_email_sent: typing.Optional[int] = OMIT,
        rate_limit_sms_sent: typing.Optional[int] = OMIT,
        rate_limit_verify: typing.Optional[int] = OMIT,
        rate_limit_token_refresh: typing.Optional[int] = OMIT,
        rate_limit_otp: typing.Optional[int] = OMIT,
        rate_limit_web3: typing.Optional[int] = OMIT,
        mailer_secure_email_change_enabled: typing.Optional[bool] = OMIT,
        refresh_token_rotation_enabled: typing.Optional[bool] = OMIT,
        password_hibp_enabled: typing.Optional[bool] = OMIT,
        password_min_length: typing.Optional[int] = OMIT,
        password_required_characters: typing.Optional[UpdateAuthConfigBodyPasswordRequiredCharacters] = OMIT,
        security_manual_linking_enabled: typing.Optional[bool] = OMIT,
        security_update_password_require_reauthentication: typing.Optional[bool] = OMIT,
        security_update_password_require_current_password: typing.Optional[bool] = OMIT,
        security_refresh_token_reuse_interval: typing.Optional[int] = OMIT,
        mailer_otp_exp: typing.Optional[int] = OMIT,
        mailer_otp_length: typing.Optional[int] = OMIT,
        sms_autoconfirm: typing.Optional[bool] = OMIT,
        sms_max_frequency: typing.Optional[int] = OMIT,
        sms_otp_exp: typing.Optional[int] = OMIT,
        sms_otp_length: typing.Optional[int] = OMIT,
        sms_provider: typing.Optional[UpdateAuthConfigBodySmsProvider] = OMIT,
        sms_messagebird_access_key: typing.Optional[str] = OMIT,
        sms_messagebird_originator: typing.Optional[str] = OMIT,
        sms_test_otp: typing.Optional[str] = OMIT,
        sms_test_otp_valid_until: typing.Optional[dt.datetime] = OMIT,
        sms_textlocal_api_key: typing.Optional[str] = OMIT,
        sms_textlocal_sender: typing.Optional[str] = OMIT,
        sms_twilio_account_sid: typing.Optional[str] = OMIT,
        sms_twilio_auth_token: typing.Optional[str] = OMIT,
        sms_twilio_content_sid: typing.Optional[str] = OMIT,
        sms_twilio_message_service_sid: typing.Optional[str] = OMIT,
        sms_twilio_verify_account_sid: typing.Optional[str] = OMIT,
        sms_twilio_verify_auth_token: typing.Optional[str] = OMIT,
        sms_twilio_verify_message_service_sid: typing.Optional[str] = OMIT,
        sms_vonage_api_key: typing.Optional[str] = OMIT,
        sms_vonage_api_secret: typing.Optional[str] = OMIT,
        sms_vonage_from: typing.Optional[str] = OMIT,
        sms_template: typing.Optional[str] = OMIT,
        hook_mfa_verification_attempt_enabled: typing.Optional[bool] = OMIT,
        hook_mfa_verification_attempt_uri: typing.Optional[str] = OMIT,
        hook_mfa_verification_attempt_secrets: typing.Optional[str] = OMIT,
        hook_password_verification_attempt_enabled: typing.Optional[bool] = OMIT,
        hook_password_verification_attempt_uri: typing.Optional[str] = OMIT,
        hook_password_verification_attempt_secrets: typing.Optional[str] = OMIT,
        hook_custom_access_token_enabled: typing.Optional[bool] = OMIT,
        hook_custom_access_token_uri: typing.Optional[str] = OMIT,
        hook_custom_access_token_secrets: typing.Optional[str] = OMIT,
        hook_send_sms_enabled: typing.Optional[bool] = OMIT,
        hook_send_sms_uri: typing.Optional[str] = OMIT,
        hook_send_sms_secrets: typing.Optional[str] = OMIT,
        hook_send_email_enabled: typing.Optional[bool] = OMIT,
        hook_send_email_uri: typing.Optional[str] = OMIT,
        hook_send_email_secrets: typing.Optional[str] = OMIT,
        hook_before_user_created_enabled: typing.Optional[bool] = OMIT,
        hook_before_user_created_uri: typing.Optional[str] = OMIT,
        hook_before_user_created_secrets: typing.Optional[str] = OMIT,
        hook_after_user_created_enabled: typing.Optional[bool] = OMIT,
        hook_after_user_created_uri: typing.Optional[str] = OMIT,
        hook_after_user_created_secrets: typing.Optional[str] = OMIT,
        external_apple_enabled: typing.Optional[bool] = OMIT,
        external_apple_client_id: typing.Optional[str] = OMIT,
        external_apple_email_optional: typing.Optional[bool] = OMIT,
        external_apple_secret: typing.Optional[str] = OMIT,
        external_apple_additional_client_ids: typing.Optional[str] = OMIT,
        external_azure_enabled: typing.Optional[bool] = OMIT,
        external_azure_client_id: typing.Optional[str] = OMIT,
        external_azure_email_optional: typing.Optional[bool] = OMIT,
        external_azure_secret: typing.Optional[str] = OMIT,
        external_azure_url: typing.Optional[str] = OMIT,
        external_bitbucket_enabled: typing.Optional[bool] = OMIT,
        external_bitbucket_client_id: typing.Optional[str] = OMIT,
        external_bitbucket_email_optional: typing.Optional[bool] = OMIT,
        external_bitbucket_secret: typing.Optional[str] = OMIT,
        external_discord_enabled: typing.Optional[bool] = OMIT,
        external_discord_client_id: typing.Optional[str] = OMIT,
        external_discord_email_optional: typing.Optional[bool] = OMIT,
        external_discord_secret: typing.Optional[str] = OMIT,
        external_facebook_enabled: typing.Optional[bool] = OMIT,
        external_facebook_client_id: typing.Optional[str] = OMIT,
        external_facebook_email_optional: typing.Optional[bool] = OMIT,
        external_facebook_secret: typing.Optional[str] = OMIT,
        external_figma_enabled: typing.Optional[bool] = OMIT,
        external_figma_client_id: typing.Optional[str] = OMIT,
        external_figma_email_optional: typing.Optional[bool] = OMIT,
        external_figma_secret: typing.Optional[str] = OMIT,
        external_github_enabled: typing.Optional[bool] = OMIT,
        external_github_client_id: typing.Optional[str] = OMIT,
        external_github_email_optional: typing.Optional[bool] = OMIT,
        external_github_secret: typing.Optional[str] = OMIT,
        external_gitlab_enabled: typing.Optional[bool] = OMIT,
        external_gitlab_client_id: typing.Optional[str] = OMIT,
        external_gitlab_email_optional: typing.Optional[bool] = OMIT,
        external_gitlab_secret: typing.Optional[str] = OMIT,
        external_gitlab_url: typing.Optional[str] = OMIT,
        external_google_enabled: typing.Optional[bool] = OMIT,
        external_google_client_id: typing.Optional[str] = OMIT,
        external_google_email_optional: typing.Optional[bool] = OMIT,
        external_google_secret: typing.Optional[str] = OMIT,
        external_google_additional_client_ids: typing.Optional[str] = OMIT,
        external_google_skip_nonce_check: typing.Optional[bool] = OMIT,
        external_kakao_enabled: typing.Optional[bool] = OMIT,
        external_kakao_client_id: typing.Optional[str] = OMIT,
        external_kakao_email_optional: typing.Optional[bool] = OMIT,
        external_kakao_secret: typing.Optional[str] = OMIT,
        external_keycloak_enabled: typing.Optional[bool] = OMIT,
        external_keycloak_client_id: typing.Optional[str] = OMIT,
        external_keycloak_email_optional: typing.Optional[bool] = OMIT,
        external_keycloak_secret: typing.Optional[str] = OMIT,
        external_keycloak_url: typing.Optional[str] = OMIT,
        external_linkedin_oidc_enabled: typing.Optional[bool] = OMIT,
        external_linkedin_oidc_client_id: typing.Optional[str] = OMIT,
        external_linkedin_oidc_email_optional: typing.Optional[bool] = OMIT,
        external_linkedin_oidc_secret: typing.Optional[str] = OMIT,
        external_slack_oidc_enabled: typing.Optional[bool] = OMIT,
        external_slack_oidc_client_id: typing.Optional[str] = OMIT,
        external_slack_oidc_email_optional: typing.Optional[bool] = OMIT,
        external_slack_oidc_secret: typing.Optional[str] = OMIT,
        external_notion_enabled: typing.Optional[bool] = OMIT,
        external_notion_client_id: typing.Optional[str] = OMIT,
        external_notion_email_optional: typing.Optional[bool] = OMIT,
        external_notion_secret: typing.Optional[str] = OMIT,
        external_slack_enabled: typing.Optional[bool] = OMIT,
        external_slack_client_id: typing.Optional[str] = OMIT,
        external_slack_email_optional: typing.Optional[bool] = OMIT,
        external_slack_secret: typing.Optional[str] = OMIT,
        external_spotify_enabled: typing.Optional[bool] = OMIT,
        external_spotify_client_id: typing.Optional[str] = OMIT,
        external_spotify_email_optional: typing.Optional[bool] = OMIT,
        external_spotify_secret: typing.Optional[str] = OMIT,
        external_twitch_enabled: typing.Optional[bool] = OMIT,
        external_twitch_client_id: typing.Optional[str] = OMIT,
        external_twitch_email_optional: typing.Optional[bool] = OMIT,
        external_twitch_secret: typing.Optional[str] = OMIT,
        external_twitter_enabled: typing.Optional[bool] = OMIT,
        external_twitter_client_id: typing.Optional[str] = OMIT,
        external_twitter_email_optional: typing.Optional[bool] = OMIT,
        external_twitter_secret: typing.Optional[str] = OMIT,
        external_x_enabled: typing.Optional[bool] = OMIT,
        external_x_client_id: typing.Optional[str] = OMIT,
        external_x_email_optional: typing.Optional[bool] = OMIT,
        external_x_secret: typing.Optional[str] = OMIT,
        external_workos_enabled: typing.Optional[bool] = OMIT,
        external_workos_client_id: typing.Optional[str] = OMIT,
        external_workos_secret: typing.Optional[str] = OMIT,
        external_workos_url: typing.Optional[str] = OMIT,
        external_web3solana_enabled: typing.Optional[bool] = OMIT,
        external_web3ethereum_enabled: typing.Optional[bool] = OMIT,
        external_zoom_enabled: typing.Optional[bool] = OMIT,
        external_zoom_client_id: typing.Optional[str] = OMIT,
        external_zoom_email_optional: typing.Optional[bool] = OMIT,
        external_zoom_secret: typing.Optional[str] = OMIT,
        db_max_pool_size: typing.Optional[int] = OMIT,
        db_max_pool_size_unit: typing.Optional[UpdateAuthConfigBodyDbMaxPoolSizeUnit] = OMIT,
        api_max_request_duration: typing.Optional[int] = OMIT,
        mfa_totp_enroll_enabled: typing.Optional[bool] = OMIT,
        mfa_totp_verify_enabled: typing.Optional[bool] = OMIT,
        mfa_web_authn_enroll_enabled: typing.Optional[bool] = OMIT,
        mfa_web_authn_verify_enabled: typing.Optional[bool] = OMIT,
        passkey_enabled: typing.Optional[bool] = OMIT,
        webauthn_rp_display_name: typing.Optional[str] = OMIT,
        webauthn_rp_id: typing.Optional[str] = OMIT,
        webauthn_rp_origins: typing.Optional[str] = OMIT,
        mfa_phone_enroll_enabled: typing.Optional[bool] = OMIT,
        mfa_phone_verify_enabled: typing.Optional[bool] = OMIT,
        mfa_phone_max_frequency: typing.Optional[int] = OMIT,
        mfa_phone_otp_length: typing.Optional[int] = OMIT,
        mfa_phone_template: typing.Optional[str] = OMIT,
        nimbus_oauth_client_id: typing.Optional[str] = OMIT,
        nimbus_oauth_client_secret: typing.Optional[str] = OMIT,
        oauth_server_enabled: typing.Optional[bool] = OMIT,
        oauth_server_allow_dynamic_registration: typing.Optional[bool] = OMIT,
        oauth_server_authorization_path: typing.Optional[str] = OMIT,
        custom_oauth_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        site_url : typing.Optional[str]

        disable_signup : typing.Optional[bool]

        jwt_exp : typing.Optional[int]

        smtp_admin_email : typing.Optional[str]

        smtp_host : typing.Optional[str]

        smtp_port : typing.Optional[str]

        smtp_user : typing.Optional[str]

        smtp_pass : typing.Optional[str]

        smtp_max_frequency : typing.Optional[int]

        smtp_sender_name : typing.Optional[str]

        mailer_allow_unverified_email_sign_ins : typing.Optional[bool]

        mailer_autoconfirm : typing.Optional[bool]

        mailer_subjects_invite : typing.Optional[str]

        mailer_subjects_confirmation : typing.Optional[str]

        mailer_subjects_recovery : typing.Optional[str]

        mailer_subjects_email_change : typing.Optional[str]

        mailer_subjects_magic_link : typing.Optional[str]

        mailer_subjects_reauthentication : typing.Optional[str]

        mailer_subjects_password_changed_notification : typing.Optional[str]

        mailer_subjects_email_changed_notification : typing.Optional[str]

        mailer_subjects_phone_changed_notification : typing.Optional[str]

        mailer_subjects_mfa_factor_enrolled_notification : typing.Optional[str]

        mailer_subjects_mfa_factor_unenrolled_notification : typing.Optional[str]

        mailer_subjects_identity_linked_notification : typing.Optional[str]

        mailer_subjects_identity_unlinked_notification : typing.Optional[str]

        mailer_templates_invite_content : typing.Optional[str]

        mailer_templates_confirmation_content : typing.Optional[str]

        mailer_templates_recovery_content : typing.Optional[str]

        mailer_templates_email_change_content : typing.Optional[str]

        mailer_templates_magic_link_content : typing.Optional[str]

        mailer_templates_reauthentication_content : typing.Optional[str]

        mailer_templates_password_changed_notification_content : typing.Optional[str]

        mailer_templates_email_changed_notification_content : typing.Optional[str]

        mailer_templates_phone_changed_notification_content : typing.Optional[str]

        mailer_templates_mfa_factor_enrolled_notification_content : typing.Optional[str]

        mailer_templates_mfa_factor_unenrolled_notification_content : typing.Optional[str]

        mailer_templates_identity_linked_notification_content : typing.Optional[str]

        mailer_templates_identity_unlinked_notification_content : typing.Optional[str]

        mailer_notifications_password_changed_enabled : typing.Optional[bool]

        mailer_notifications_email_changed_enabled : typing.Optional[bool]

        mailer_notifications_phone_changed_enabled : typing.Optional[bool]

        mailer_notifications_mfa_factor_enrolled_enabled : typing.Optional[bool]

        mailer_notifications_mfa_factor_unenrolled_enabled : typing.Optional[bool]

        mailer_notifications_identity_linked_enabled : typing.Optional[bool]

        mailer_notifications_identity_unlinked_enabled : typing.Optional[bool]

        mfa_max_enrolled_factors : typing.Optional[int]

        uri_allow_list : typing.Optional[str]

        external_anonymous_users_enabled : typing.Optional[bool]

        external_email_enabled : typing.Optional[bool]

        external_phone_enabled : typing.Optional[bool]

        saml_enabled : typing.Optional[bool]

        saml_external_url : typing.Optional[str]

        security_sb_forwarded_for_enabled : typing.Optional[bool]

        security_captcha_enabled : typing.Optional[bool]

        security_captcha_provider : typing.Optional[UpdateAuthConfigBodySecurityCaptchaProvider]

        security_captcha_secret : typing.Optional[str]

        sessions_timebox : typing.Optional[float]
            Session timebox in hours. Maximum 8760 hours (1 year).

        sessions_inactivity_timeout : typing.Optional[float]
            Session inactivity timeout in hours. Maximum 8760 hours (1 year).

        sessions_single_per_user : typing.Optional[bool]

        sessions_tags : typing.Optional[str]

        rate_limit_anonymous_users : typing.Optional[int]

        rate_limit_email_sent : typing.Optional[int]

        rate_limit_sms_sent : typing.Optional[int]

        rate_limit_verify : typing.Optional[int]

        rate_limit_token_refresh : typing.Optional[int]

        rate_limit_otp : typing.Optional[int]

        rate_limit_web3 : typing.Optional[int]

        mailer_secure_email_change_enabled : typing.Optional[bool]

        refresh_token_rotation_enabled : typing.Optional[bool]

        password_hibp_enabled : typing.Optional[bool]

        password_min_length : typing.Optional[int]

        password_required_characters : typing.Optional[UpdateAuthConfigBodyPasswordRequiredCharacters]

        security_manual_linking_enabled : typing.Optional[bool]

        security_update_password_require_reauthentication : typing.Optional[bool]

        security_update_password_require_current_password : typing.Optional[bool]
            Require the user's current password when updating their password.

        security_refresh_token_reuse_interval : typing.Optional[int]
            Refresh token reuse interval in seconds. Maximum 300 seconds (5 minutes).

        mailer_otp_exp : typing.Optional[int]

        mailer_otp_length : typing.Optional[int]

        sms_autoconfirm : typing.Optional[bool]

        sms_max_frequency : typing.Optional[int]

        sms_otp_exp : typing.Optional[int]

        sms_otp_length : typing.Optional[int]

        sms_provider : typing.Optional[UpdateAuthConfigBodySmsProvider]

        sms_messagebird_access_key : typing.Optional[str]

        sms_messagebird_originator : typing.Optional[str]

        sms_test_otp : typing.Optional[str]

        sms_test_otp_valid_until : typing.Optional[dt.datetime]

        sms_textlocal_api_key : typing.Optional[str]

        sms_textlocal_sender : typing.Optional[str]

        sms_twilio_account_sid : typing.Optional[str]

        sms_twilio_auth_token : typing.Optional[str]

        sms_twilio_content_sid : typing.Optional[str]

        sms_twilio_message_service_sid : typing.Optional[str]

        sms_twilio_verify_account_sid : typing.Optional[str]

        sms_twilio_verify_auth_token : typing.Optional[str]

        sms_twilio_verify_message_service_sid : typing.Optional[str]

        sms_vonage_api_key : typing.Optional[str]

        sms_vonage_api_secret : typing.Optional[str]

        sms_vonage_from : typing.Optional[str]

        sms_template : typing.Optional[str]

        hook_mfa_verification_attempt_enabled : typing.Optional[bool]

        hook_mfa_verification_attempt_uri : typing.Optional[str]

        hook_mfa_verification_attempt_secrets : typing.Optional[str]

        hook_password_verification_attempt_enabled : typing.Optional[bool]

        hook_password_verification_attempt_uri : typing.Optional[str]

        hook_password_verification_attempt_secrets : typing.Optional[str]

        hook_custom_access_token_enabled : typing.Optional[bool]

        hook_custom_access_token_uri : typing.Optional[str]

        hook_custom_access_token_secrets : typing.Optional[str]

        hook_send_sms_enabled : typing.Optional[bool]

        hook_send_sms_uri : typing.Optional[str]

        hook_send_sms_secrets : typing.Optional[str]

        hook_send_email_enabled : typing.Optional[bool]

        hook_send_email_uri : typing.Optional[str]

        hook_send_email_secrets : typing.Optional[str]

        hook_before_user_created_enabled : typing.Optional[bool]

        hook_before_user_created_uri : typing.Optional[str]

        hook_before_user_created_secrets : typing.Optional[str]

        hook_after_user_created_enabled : typing.Optional[bool]

        hook_after_user_created_uri : typing.Optional[str]

        hook_after_user_created_secrets : typing.Optional[str]

        external_apple_enabled : typing.Optional[bool]

        external_apple_client_id : typing.Optional[str]

        external_apple_email_optional : typing.Optional[bool]

        external_apple_secret : typing.Optional[str]

        external_apple_additional_client_ids : typing.Optional[str]

        external_azure_enabled : typing.Optional[bool]

        external_azure_client_id : typing.Optional[str]

        external_azure_email_optional : typing.Optional[bool]

        external_azure_secret : typing.Optional[str]

        external_azure_url : typing.Optional[str]

        external_bitbucket_enabled : typing.Optional[bool]

        external_bitbucket_client_id : typing.Optional[str]

        external_bitbucket_email_optional : typing.Optional[bool]

        external_bitbucket_secret : typing.Optional[str]

        external_discord_enabled : typing.Optional[bool]

        external_discord_client_id : typing.Optional[str]

        external_discord_email_optional : typing.Optional[bool]

        external_discord_secret : typing.Optional[str]

        external_facebook_enabled : typing.Optional[bool]

        external_facebook_client_id : typing.Optional[str]

        external_facebook_email_optional : typing.Optional[bool]

        external_facebook_secret : typing.Optional[str]

        external_figma_enabled : typing.Optional[bool]

        external_figma_client_id : typing.Optional[str]

        external_figma_email_optional : typing.Optional[bool]

        external_figma_secret : typing.Optional[str]

        external_github_enabled : typing.Optional[bool]

        external_github_client_id : typing.Optional[str]

        external_github_email_optional : typing.Optional[bool]

        external_github_secret : typing.Optional[str]

        external_gitlab_enabled : typing.Optional[bool]

        external_gitlab_client_id : typing.Optional[str]

        external_gitlab_email_optional : typing.Optional[bool]

        external_gitlab_secret : typing.Optional[str]

        external_gitlab_url : typing.Optional[str]

        external_google_enabled : typing.Optional[bool]

        external_google_client_id : typing.Optional[str]

        external_google_email_optional : typing.Optional[bool]

        external_google_secret : typing.Optional[str]

        external_google_additional_client_ids : typing.Optional[str]

        external_google_skip_nonce_check : typing.Optional[bool]

        external_kakao_enabled : typing.Optional[bool]

        external_kakao_client_id : typing.Optional[str]

        external_kakao_email_optional : typing.Optional[bool]

        external_kakao_secret : typing.Optional[str]

        external_keycloak_enabled : typing.Optional[bool]

        external_keycloak_client_id : typing.Optional[str]

        external_keycloak_email_optional : typing.Optional[bool]

        external_keycloak_secret : typing.Optional[str]

        external_keycloak_url : typing.Optional[str]

        external_linkedin_oidc_enabled : typing.Optional[bool]

        external_linkedin_oidc_client_id : typing.Optional[str]

        external_linkedin_oidc_email_optional : typing.Optional[bool]

        external_linkedin_oidc_secret : typing.Optional[str]

        external_slack_oidc_enabled : typing.Optional[bool]

        external_slack_oidc_client_id : typing.Optional[str]

        external_slack_oidc_email_optional : typing.Optional[bool]

        external_slack_oidc_secret : typing.Optional[str]

        external_notion_enabled : typing.Optional[bool]

        external_notion_client_id : typing.Optional[str]

        external_notion_email_optional : typing.Optional[bool]

        external_notion_secret : typing.Optional[str]

        external_slack_enabled : typing.Optional[bool]

        external_slack_client_id : typing.Optional[str]

        external_slack_email_optional : typing.Optional[bool]

        external_slack_secret : typing.Optional[str]

        external_spotify_enabled : typing.Optional[bool]

        external_spotify_client_id : typing.Optional[str]

        external_spotify_email_optional : typing.Optional[bool]

        external_spotify_secret : typing.Optional[str]

        external_twitch_enabled : typing.Optional[bool]

        external_twitch_client_id : typing.Optional[str]

        external_twitch_email_optional : typing.Optional[bool]

        external_twitch_secret : typing.Optional[str]

        external_twitter_enabled : typing.Optional[bool]

        external_twitter_client_id : typing.Optional[str]

        external_twitter_email_optional : typing.Optional[bool]

        external_twitter_secret : typing.Optional[str]

        external_x_enabled : typing.Optional[bool]

        external_x_client_id : typing.Optional[str]

        external_x_email_optional : typing.Optional[bool]

        external_x_secret : typing.Optional[str]

        external_workos_enabled : typing.Optional[bool]

        external_workos_client_id : typing.Optional[str]

        external_workos_secret : typing.Optional[str]

        external_workos_url : typing.Optional[str]

        external_web3solana_enabled : typing.Optional[bool]

        external_web3ethereum_enabled : typing.Optional[bool]

        external_zoom_enabled : typing.Optional[bool]

        external_zoom_client_id : typing.Optional[str]

        external_zoom_email_optional : typing.Optional[bool]

        external_zoom_secret : typing.Optional[str]

        db_max_pool_size : typing.Optional[int]

        db_max_pool_size_unit : typing.Optional[UpdateAuthConfigBodyDbMaxPoolSizeUnit]

        api_max_request_duration : typing.Optional[int]

        mfa_totp_enroll_enabled : typing.Optional[bool]

        mfa_totp_verify_enabled : typing.Optional[bool]

        mfa_web_authn_enroll_enabled : typing.Optional[bool]

        mfa_web_authn_verify_enabled : typing.Optional[bool]

        passkey_enabled : typing.Optional[bool]

        webauthn_rp_display_name : typing.Optional[str]

        webauthn_rp_id : typing.Optional[str]

        webauthn_rp_origins : typing.Optional[str]

        mfa_phone_enroll_enabled : typing.Optional[bool]

        mfa_phone_verify_enabled : typing.Optional[bool]

        mfa_phone_max_frequency : typing.Optional[int]

        mfa_phone_otp_length : typing.Optional[int]

        mfa_phone_template : typing.Optional[str]

        nimbus_oauth_client_id : typing.Optional[str]

        nimbus_oauth_client_secret : typing.Optional[str]

        oauth_server_enabled : typing.Optional[bool]

        oauth_server_allow_dynamic_registration : typing.Optional[bool]

        oauth_server_authorization_path : typing.Optional[str]

        custom_oauth_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthConfigResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1update_auth_service_config(
                ref="abcdefghijklmnopqrst",
                site_url="https://app.example.com",
                disable_signup=False,
                jwt_exp=3600,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_auth_service_config(
            ref,
            site_url=site_url,
            disable_signup=disable_signup,
            jwt_exp=jwt_exp,
            smtp_admin_email=smtp_admin_email,
            smtp_host=smtp_host,
            smtp_port=smtp_port,
            smtp_user=smtp_user,
            smtp_pass=smtp_pass,
            smtp_max_frequency=smtp_max_frequency,
            smtp_sender_name=smtp_sender_name,
            mailer_allow_unverified_email_sign_ins=mailer_allow_unverified_email_sign_ins,
            mailer_autoconfirm=mailer_autoconfirm,
            mailer_subjects_invite=mailer_subjects_invite,
            mailer_subjects_confirmation=mailer_subjects_confirmation,
            mailer_subjects_recovery=mailer_subjects_recovery,
            mailer_subjects_email_change=mailer_subjects_email_change,
            mailer_subjects_magic_link=mailer_subjects_magic_link,
            mailer_subjects_reauthentication=mailer_subjects_reauthentication,
            mailer_subjects_password_changed_notification=mailer_subjects_password_changed_notification,
            mailer_subjects_email_changed_notification=mailer_subjects_email_changed_notification,
            mailer_subjects_phone_changed_notification=mailer_subjects_phone_changed_notification,
            mailer_subjects_mfa_factor_enrolled_notification=mailer_subjects_mfa_factor_enrolled_notification,
            mailer_subjects_mfa_factor_unenrolled_notification=mailer_subjects_mfa_factor_unenrolled_notification,
            mailer_subjects_identity_linked_notification=mailer_subjects_identity_linked_notification,
            mailer_subjects_identity_unlinked_notification=mailer_subjects_identity_unlinked_notification,
            mailer_templates_invite_content=mailer_templates_invite_content,
            mailer_templates_confirmation_content=mailer_templates_confirmation_content,
            mailer_templates_recovery_content=mailer_templates_recovery_content,
            mailer_templates_email_change_content=mailer_templates_email_change_content,
            mailer_templates_magic_link_content=mailer_templates_magic_link_content,
            mailer_templates_reauthentication_content=mailer_templates_reauthentication_content,
            mailer_templates_password_changed_notification_content=mailer_templates_password_changed_notification_content,
            mailer_templates_email_changed_notification_content=mailer_templates_email_changed_notification_content,
            mailer_templates_phone_changed_notification_content=mailer_templates_phone_changed_notification_content,
            mailer_templates_mfa_factor_enrolled_notification_content=mailer_templates_mfa_factor_enrolled_notification_content,
            mailer_templates_mfa_factor_unenrolled_notification_content=mailer_templates_mfa_factor_unenrolled_notification_content,
            mailer_templates_identity_linked_notification_content=mailer_templates_identity_linked_notification_content,
            mailer_templates_identity_unlinked_notification_content=mailer_templates_identity_unlinked_notification_content,
            mailer_notifications_password_changed_enabled=mailer_notifications_password_changed_enabled,
            mailer_notifications_email_changed_enabled=mailer_notifications_email_changed_enabled,
            mailer_notifications_phone_changed_enabled=mailer_notifications_phone_changed_enabled,
            mailer_notifications_mfa_factor_enrolled_enabled=mailer_notifications_mfa_factor_enrolled_enabled,
            mailer_notifications_mfa_factor_unenrolled_enabled=mailer_notifications_mfa_factor_unenrolled_enabled,
            mailer_notifications_identity_linked_enabled=mailer_notifications_identity_linked_enabled,
            mailer_notifications_identity_unlinked_enabled=mailer_notifications_identity_unlinked_enabled,
            mfa_max_enrolled_factors=mfa_max_enrolled_factors,
            uri_allow_list=uri_allow_list,
            external_anonymous_users_enabled=external_anonymous_users_enabled,
            external_email_enabled=external_email_enabled,
            external_phone_enabled=external_phone_enabled,
            saml_enabled=saml_enabled,
            saml_external_url=saml_external_url,
            security_sb_forwarded_for_enabled=security_sb_forwarded_for_enabled,
            security_captcha_enabled=security_captcha_enabled,
            security_captcha_provider=security_captcha_provider,
            security_captcha_secret=security_captcha_secret,
            sessions_timebox=sessions_timebox,
            sessions_inactivity_timeout=sessions_inactivity_timeout,
            sessions_single_per_user=sessions_single_per_user,
            sessions_tags=sessions_tags,
            rate_limit_anonymous_users=rate_limit_anonymous_users,
            rate_limit_email_sent=rate_limit_email_sent,
            rate_limit_sms_sent=rate_limit_sms_sent,
            rate_limit_verify=rate_limit_verify,
            rate_limit_token_refresh=rate_limit_token_refresh,
            rate_limit_otp=rate_limit_otp,
            rate_limit_web3=rate_limit_web3,
            mailer_secure_email_change_enabled=mailer_secure_email_change_enabled,
            refresh_token_rotation_enabled=refresh_token_rotation_enabled,
            password_hibp_enabled=password_hibp_enabled,
            password_min_length=password_min_length,
            password_required_characters=password_required_characters,
            security_manual_linking_enabled=security_manual_linking_enabled,
            security_update_password_require_reauthentication=security_update_password_require_reauthentication,
            security_update_password_require_current_password=security_update_password_require_current_password,
            security_refresh_token_reuse_interval=security_refresh_token_reuse_interval,
            mailer_otp_exp=mailer_otp_exp,
            mailer_otp_length=mailer_otp_length,
            sms_autoconfirm=sms_autoconfirm,
            sms_max_frequency=sms_max_frequency,
            sms_otp_exp=sms_otp_exp,
            sms_otp_length=sms_otp_length,
            sms_provider=sms_provider,
            sms_messagebird_access_key=sms_messagebird_access_key,
            sms_messagebird_originator=sms_messagebird_originator,
            sms_test_otp=sms_test_otp,
            sms_test_otp_valid_until=sms_test_otp_valid_until,
            sms_textlocal_api_key=sms_textlocal_api_key,
            sms_textlocal_sender=sms_textlocal_sender,
            sms_twilio_account_sid=sms_twilio_account_sid,
            sms_twilio_auth_token=sms_twilio_auth_token,
            sms_twilio_content_sid=sms_twilio_content_sid,
            sms_twilio_message_service_sid=sms_twilio_message_service_sid,
            sms_twilio_verify_account_sid=sms_twilio_verify_account_sid,
            sms_twilio_verify_auth_token=sms_twilio_verify_auth_token,
            sms_twilio_verify_message_service_sid=sms_twilio_verify_message_service_sid,
            sms_vonage_api_key=sms_vonage_api_key,
            sms_vonage_api_secret=sms_vonage_api_secret,
            sms_vonage_from=sms_vonage_from,
            sms_template=sms_template,
            hook_mfa_verification_attempt_enabled=hook_mfa_verification_attempt_enabled,
            hook_mfa_verification_attempt_uri=hook_mfa_verification_attempt_uri,
            hook_mfa_verification_attempt_secrets=hook_mfa_verification_attempt_secrets,
            hook_password_verification_attempt_enabled=hook_password_verification_attempt_enabled,
            hook_password_verification_attempt_uri=hook_password_verification_attempt_uri,
            hook_password_verification_attempt_secrets=hook_password_verification_attempt_secrets,
            hook_custom_access_token_enabled=hook_custom_access_token_enabled,
            hook_custom_access_token_uri=hook_custom_access_token_uri,
            hook_custom_access_token_secrets=hook_custom_access_token_secrets,
            hook_send_sms_enabled=hook_send_sms_enabled,
            hook_send_sms_uri=hook_send_sms_uri,
            hook_send_sms_secrets=hook_send_sms_secrets,
            hook_send_email_enabled=hook_send_email_enabled,
            hook_send_email_uri=hook_send_email_uri,
            hook_send_email_secrets=hook_send_email_secrets,
            hook_before_user_created_enabled=hook_before_user_created_enabled,
            hook_before_user_created_uri=hook_before_user_created_uri,
            hook_before_user_created_secrets=hook_before_user_created_secrets,
            hook_after_user_created_enabled=hook_after_user_created_enabled,
            hook_after_user_created_uri=hook_after_user_created_uri,
            hook_after_user_created_secrets=hook_after_user_created_secrets,
            external_apple_enabled=external_apple_enabled,
            external_apple_client_id=external_apple_client_id,
            external_apple_email_optional=external_apple_email_optional,
            external_apple_secret=external_apple_secret,
            external_apple_additional_client_ids=external_apple_additional_client_ids,
            external_azure_enabled=external_azure_enabled,
            external_azure_client_id=external_azure_client_id,
            external_azure_email_optional=external_azure_email_optional,
            external_azure_secret=external_azure_secret,
            external_azure_url=external_azure_url,
            external_bitbucket_enabled=external_bitbucket_enabled,
            external_bitbucket_client_id=external_bitbucket_client_id,
            external_bitbucket_email_optional=external_bitbucket_email_optional,
            external_bitbucket_secret=external_bitbucket_secret,
            external_discord_enabled=external_discord_enabled,
            external_discord_client_id=external_discord_client_id,
            external_discord_email_optional=external_discord_email_optional,
            external_discord_secret=external_discord_secret,
            external_facebook_enabled=external_facebook_enabled,
            external_facebook_client_id=external_facebook_client_id,
            external_facebook_email_optional=external_facebook_email_optional,
            external_facebook_secret=external_facebook_secret,
            external_figma_enabled=external_figma_enabled,
            external_figma_client_id=external_figma_client_id,
            external_figma_email_optional=external_figma_email_optional,
            external_figma_secret=external_figma_secret,
            external_github_enabled=external_github_enabled,
            external_github_client_id=external_github_client_id,
            external_github_email_optional=external_github_email_optional,
            external_github_secret=external_github_secret,
            external_gitlab_enabled=external_gitlab_enabled,
            external_gitlab_client_id=external_gitlab_client_id,
            external_gitlab_email_optional=external_gitlab_email_optional,
            external_gitlab_secret=external_gitlab_secret,
            external_gitlab_url=external_gitlab_url,
            external_google_enabled=external_google_enabled,
            external_google_client_id=external_google_client_id,
            external_google_email_optional=external_google_email_optional,
            external_google_secret=external_google_secret,
            external_google_additional_client_ids=external_google_additional_client_ids,
            external_google_skip_nonce_check=external_google_skip_nonce_check,
            external_kakao_enabled=external_kakao_enabled,
            external_kakao_client_id=external_kakao_client_id,
            external_kakao_email_optional=external_kakao_email_optional,
            external_kakao_secret=external_kakao_secret,
            external_keycloak_enabled=external_keycloak_enabled,
            external_keycloak_client_id=external_keycloak_client_id,
            external_keycloak_email_optional=external_keycloak_email_optional,
            external_keycloak_secret=external_keycloak_secret,
            external_keycloak_url=external_keycloak_url,
            external_linkedin_oidc_enabled=external_linkedin_oidc_enabled,
            external_linkedin_oidc_client_id=external_linkedin_oidc_client_id,
            external_linkedin_oidc_email_optional=external_linkedin_oidc_email_optional,
            external_linkedin_oidc_secret=external_linkedin_oidc_secret,
            external_slack_oidc_enabled=external_slack_oidc_enabled,
            external_slack_oidc_client_id=external_slack_oidc_client_id,
            external_slack_oidc_email_optional=external_slack_oidc_email_optional,
            external_slack_oidc_secret=external_slack_oidc_secret,
            external_notion_enabled=external_notion_enabled,
            external_notion_client_id=external_notion_client_id,
            external_notion_email_optional=external_notion_email_optional,
            external_notion_secret=external_notion_secret,
            external_slack_enabled=external_slack_enabled,
            external_slack_client_id=external_slack_client_id,
            external_slack_email_optional=external_slack_email_optional,
            external_slack_secret=external_slack_secret,
            external_spotify_enabled=external_spotify_enabled,
            external_spotify_client_id=external_spotify_client_id,
            external_spotify_email_optional=external_spotify_email_optional,
            external_spotify_secret=external_spotify_secret,
            external_twitch_enabled=external_twitch_enabled,
            external_twitch_client_id=external_twitch_client_id,
            external_twitch_email_optional=external_twitch_email_optional,
            external_twitch_secret=external_twitch_secret,
            external_twitter_enabled=external_twitter_enabled,
            external_twitter_client_id=external_twitter_client_id,
            external_twitter_email_optional=external_twitter_email_optional,
            external_twitter_secret=external_twitter_secret,
            external_x_enabled=external_x_enabled,
            external_x_client_id=external_x_client_id,
            external_x_email_optional=external_x_email_optional,
            external_x_secret=external_x_secret,
            external_workos_enabled=external_workos_enabled,
            external_workos_client_id=external_workos_client_id,
            external_workos_secret=external_workos_secret,
            external_workos_url=external_workos_url,
            external_web3solana_enabled=external_web3solana_enabled,
            external_web3ethereum_enabled=external_web3ethereum_enabled,
            external_zoom_enabled=external_zoom_enabled,
            external_zoom_client_id=external_zoom_client_id,
            external_zoom_email_optional=external_zoom_email_optional,
            external_zoom_secret=external_zoom_secret,
            db_max_pool_size=db_max_pool_size,
            db_max_pool_size_unit=db_max_pool_size_unit,
            api_max_request_duration=api_max_request_duration,
            mfa_totp_enroll_enabled=mfa_totp_enroll_enabled,
            mfa_totp_verify_enabled=mfa_totp_verify_enabled,
            mfa_web_authn_enroll_enabled=mfa_web_authn_enroll_enabled,
            mfa_web_authn_verify_enabled=mfa_web_authn_verify_enabled,
            passkey_enabled=passkey_enabled,
            webauthn_rp_display_name=webauthn_rp_display_name,
            webauthn_rp_id=webauthn_rp_id,
            webauthn_rp_origins=webauthn_rp_origins,
            mfa_phone_enroll_enabled=mfa_phone_enroll_enabled,
            mfa_phone_verify_enabled=mfa_phone_verify_enabled,
            mfa_phone_max_frequency=mfa_phone_max_frequency,
            mfa_phone_otp_length=mfa_phone_otp_length,
            mfa_phone_template=mfa_phone_template,
            nimbus_oauth_client_id=nimbus_oauth_client_id,
            nimbus_oauth_client_secret=nimbus_oauth_client_secret,
            oauth_server_enabled=oauth_server_enabled,
            oauth_server_allow_dynamic_registration=oauth_server_allow_dynamic_registration,
            oauth_server_authorization_path=oauth_server_authorization_path,
            custom_oauth_enabled=custom_oauth_enabled,
            request_options=request_options,
        )
        return _response.data

    async def v1list_project_tpa_integrations(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ThirdPartyAuthOutput]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ThirdPartyAuthOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1list_project_tpa_integrations(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_project_tpa_integrations(ref, request_options=request_options)
        return _response.data

    async def v1create_project_tpa_integration(
        self,
        ref: str,
        *,
        oidc_issuer_url: typing.Optional[str] = OMIT,
        jwks_url: typing.Optional[str] = OMIT,
        custom_jwks: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThirdPartyAuthOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        oidc_issuer_url : typing.Optional[str]

        jwks_url : typing.Optional[str]

        custom_jwks : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThirdPartyAuthOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1create_project_tpa_integration(
                ref="abcdefghijklmnopqrst",
                oidc_issuer_url="https://login.acme.com",
                jwks_url="https://login.acme.com/.well-known/jwks.json",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1create_project_tpa_integration(
            ref,
            oidc_issuer_url=oidc_issuer_url,
            jwks_url=jwks_url,
            custom_jwks=custom_jwks,
            request_options=request_options,
        )
        return _response.data

    async def v1get_project_tpa_integration(
        self, ref: str, tpa_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThirdPartyAuthOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        tpa_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThirdPartyAuthOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1get_project_tpa_integration(
                ref="abcdefghijklmnopqrst",
                tpa_id="88888888-8888-4888-8888-888888888888",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_tpa_integration(ref, tpa_id, request_options=request_options)
        return _response.data

    async def v1delete_project_tpa_integration(
        self, ref: str, tpa_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThirdPartyAuthOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        tpa_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThirdPartyAuthOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1delete_project_tpa_integration(
                ref="abcdefghijklmnopqrst",
                tpa_id="88888888-8888-4888-8888-888888888888",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1delete_project_tpa_integration(
            ref, tpa_id, request_options=request_options
        )
        return _response.data

    async def v1list_all_sso_provider(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListProvidersResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProvidersResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1list_all_sso_provider(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_all_sso_provider(ref, request_options=request_options)
        return _response.data

    async def v1create_a_sso_provider(
        self,
        ref: str,
        *,
        type: CreateProviderBodyType,
        metadata_xml: typing.Optional[str] = OMIT,
        metadata_url: typing.Optional[str] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        attribute_mapping: typing.Optional[CreateProviderBodyAttributeMapping] = OMIT,
        name_id_format: typing.Optional[CreateProviderBodyNameIdFormat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateProviderResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        type : CreateProviderBodyType
            What type of provider will be created

        metadata_xml : typing.Optional[str]

        metadata_url : typing.Optional[str]

        domains : typing.Optional[typing.Sequence[str]]

        attribute_mapping : typing.Optional[CreateProviderBodyAttributeMapping]

        name_id_format : typing.Optional[CreateProviderBodyNameIdFormat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateProviderResponseOutput


        Examples
        --------
        import asyncio

        from fern.auth import (
            CreateProviderBodyAttributeMapping,
            CreateProviderBodyAttributeMappingKeysValue,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1create_a_sso_provider(
                ref="abcdefghijklmnopqrst",
                type="saml",
                metadata_url="https://sso.acme.com/metadata.xml",
                domains=["acme.com"],
                attribute_mapping=CreateProviderBodyAttributeMapping(
                    keys={
                        "email": CreateProviderBodyAttributeMappingKeysValue(
                            name="email",
                        ),
                        "first_name": CreateProviderBodyAttributeMappingKeysValue(
                            name="first_name",
                        ),
                        "last_name": CreateProviderBodyAttributeMappingKeysValue(
                            name="last_name",
                        ),
                    },
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1create_a_sso_provider(
            ref,
            type=type,
            metadata_xml=metadata_xml,
            metadata_url=metadata_url,
            domains=domains,
            attribute_mapping=attribute_mapping,
            name_id_format=name_id_format,
            request_options=request_options,
        )
        return _response.data

    async def v1get_a_sso_provider(
        self, ref: str, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProviderResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProviderResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1get_a_sso_provider(
                ref="abcdefghijklmnopqrst",
                provider_id="77777777-7777-4777-8777-777777777777",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_a_sso_provider(ref, provider_id, request_options=request_options)
        return _response.data

    async def v1update_a_sso_provider(
        self,
        ref: str,
        provider_id: str,
        *,
        metadata_xml: typing.Optional[str] = OMIT,
        metadata_url: typing.Optional[str] = OMIT,
        domains: typing.Optional[typing.Sequence[str]] = OMIT,
        attribute_mapping: typing.Optional[UpdateProviderBodyAttributeMapping] = OMIT,
        name_id_format: typing.Optional[UpdateProviderBodyNameIdFormat] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateProviderResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        provider_id : str

        metadata_xml : typing.Optional[str]

        metadata_url : typing.Optional[str]

        domains : typing.Optional[typing.Sequence[str]]

        attribute_mapping : typing.Optional[UpdateProviderBodyAttributeMapping]

        name_id_format : typing.Optional[UpdateProviderBodyNameIdFormat]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateProviderResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1update_a_sso_provider(
                ref="abcdefghijklmnopqrst",
                provider_id="77777777-7777-4777-8777-777777777777",
                metadata_url="https://sso.acme.com/metadata.xml",
                domains=["acme.com", "contractors.acme.com"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_a_sso_provider(
            ref,
            provider_id,
            metadata_xml=metadata_xml,
            metadata_url=metadata_url,
            domains=domains,
            attribute_mapping=attribute_mapping,
            name_id_format=name_id_format,
            request_options=request_options,
        )
        return _response.data

    async def v1delete_a_sso_provider(
        self, ref: str, provider_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteProviderResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        provider_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteProviderResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.auth.v1delete_a_sso_provider(
                ref="abcdefghijklmnopqrst",
                provider_id="77777777-7777-4777-8777-777777777777",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1delete_a_sso_provider(ref, provider_id, request_options=request_options)
        return _response.data
