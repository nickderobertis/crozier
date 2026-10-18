

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .auth_config_response_output_db_max_pool_size_unit import AuthConfigResponseOutputDbMaxPoolSizeUnit
from .auth_config_response_output_password_required_characters import AuthConfigResponseOutputPasswordRequiredCharacters
from .auth_config_response_output_security_captcha_provider import AuthConfigResponseOutputSecurityCaptchaProvider
from .auth_config_response_output_sms_provider import AuthConfigResponseOutputSmsProvider


class AuthConfigResponseOutput(UniversalBaseModel):
    api_max_request_duration: typing.Optional[int] = None
    db_max_pool_size: typing.Optional[int] = None
    db_max_pool_size_unit: typing.Optional[AuthConfigResponseOutputDbMaxPoolSizeUnit] = None
    disable_signup: typing.Optional[bool] = None
    external_anonymous_users_enabled: typing.Optional[bool] = None
    external_apple_additional_client_ids: typing.Optional[str] = None
    external_apple_client_id: typing.Optional[str] = None
    external_apple_email_optional: typing.Optional[bool] = None
    external_apple_enabled: typing.Optional[bool] = None
    external_apple_secret: typing.Optional[str] = None
    external_azure_client_id: typing.Optional[str] = None
    external_azure_email_optional: typing.Optional[bool] = None
    external_azure_enabled: typing.Optional[bool] = None
    external_azure_secret: typing.Optional[str] = None
    external_azure_url: typing.Optional[str] = None
    external_bitbucket_client_id: typing.Optional[str] = None
    external_bitbucket_email_optional: typing.Optional[bool] = None
    external_bitbucket_enabled: typing.Optional[bool] = None
    external_bitbucket_secret: typing.Optional[str] = None
    external_discord_client_id: typing.Optional[str] = None
    external_discord_email_optional: typing.Optional[bool] = None
    external_discord_enabled: typing.Optional[bool] = None
    external_discord_secret: typing.Optional[str] = None
    external_email_enabled: typing.Optional[bool] = None
    external_facebook_client_id: typing.Optional[str] = None
    external_facebook_email_optional: typing.Optional[bool] = None
    external_facebook_enabled: typing.Optional[bool] = None
    external_facebook_secret: typing.Optional[str] = None
    external_figma_client_id: typing.Optional[str] = None
    external_figma_email_optional: typing.Optional[bool] = None
    external_figma_enabled: typing.Optional[bool] = None
    external_figma_secret: typing.Optional[str] = None
    external_github_client_id: typing.Optional[str] = None
    external_github_email_optional: typing.Optional[bool] = None
    external_github_enabled: typing.Optional[bool] = None
    external_github_secret: typing.Optional[str] = None
    external_gitlab_client_id: typing.Optional[str] = None
    external_gitlab_email_optional: typing.Optional[bool] = None
    external_gitlab_enabled: typing.Optional[bool] = None
    external_gitlab_secret: typing.Optional[str] = None
    external_gitlab_url: typing.Optional[str] = None
    external_google_additional_client_ids: typing.Optional[str] = None
    external_google_client_id: typing.Optional[str] = None
    external_google_email_optional: typing.Optional[bool] = None
    external_google_enabled: typing.Optional[bool] = None
    external_google_secret: typing.Optional[str] = None
    external_google_skip_nonce_check: typing.Optional[bool] = None
    external_kakao_client_id: typing.Optional[str] = None
    external_kakao_email_optional: typing.Optional[bool] = None
    external_kakao_enabled: typing.Optional[bool] = None
    external_kakao_secret: typing.Optional[str] = None
    external_keycloak_client_id: typing.Optional[str] = None
    external_keycloak_email_optional: typing.Optional[bool] = None
    external_keycloak_enabled: typing.Optional[bool] = None
    external_keycloak_secret: typing.Optional[str] = None
    external_keycloak_url: typing.Optional[str] = None
    external_linkedin_oidc_client_id: typing.Optional[str] = None
    external_linkedin_oidc_email_optional: typing.Optional[bool] = None
    external_linkedin_oidc_enabled: typing.Optional[bool] = None
    external_linkedin_oidc_secret: typing.Optional[str] = None
    external_slack_oidc_client_id: typing.Optional[str] = None
    external_slack_oidc_email_optional: typing.Optional[bool] = None
    external_slack_oidc_enabled: typing.Optional[bool] = None
    external_slack_oidc_secret: typing.Optional[str] = None
    external_notion_client_id: typing.Optional[str] = None
    external_notion_email_optional: typing.Optional[bool] = None
    external_notion_enabled: typing.Optional[bool] = None
    external_notion_secret: typing.Optional[str] = None
    external_phone_enabled: typing.Optional[bool] = None
    external_slack_client_id: typing.Optional[str] = None
    external_slack_email_optional: typing.Optional[bool] = None
    external_slack_enabled: typing.Optional[bool] = None
    external_slack_secret: typing.Optional[str] = None
    external_spotify_client_id: typing.Optional[str] = None
    external_spotify_email_optional: typing.Optional[bool] = None
    external_spotify_enabled: typing.Optional[bool] = None
    external_spotify_secret: typing.Optional[str] = None
    external_twitch_client_id: typing.Optional[str] = None
    external_twitch_email_optional: typing.Optional[bool] = None
    external_twitch_enabled: typing.Optional[bool] = None
    external_twitch_secret: typing.Optional[str] = None
    external_twitter_client_id: typing.Optional[str] = None
    external_twitter_email_optional: typing.Optional[bool] = None
    external_twitter_enabled: typing.Optional[bool] = None
    external_twitter_secret: typing.Optional[str] = None
    external_x_client_id: typing.Optional[str] = None
    external_x_email_optional: typing.Optional[bool] = None
    external_x_enabled: typing.Optional[bool] = None
    external_x_secret: typing.Optional[str] = None
    external_workos_client_id: typing.Optional[str] = None
    external_workos_enabled: typing.Optional[bool] = None
    external_workos_secret: typing.Optional[str] = None
    external_workos_url: typing.Optional[str] = None
    external_web3solana_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="external_web3_solana_enabled"),
        pydantic.Field(alias="external_web3_solana_enabled"),
    ] = None
    external_web3ethereum_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="external_web3_ethereum_enabled"),
        pydantic.Field(alias="external_web3_ethereum_enabled"),
    ] = None
    external_zoom_client_id: typing.Optional[str] = None
    external_zoom_email_optional: typing.Optional[bool] = None
    external_zoom_enabled: typing.Optional[bool] = None
    external_zoom_secret: typing.Optional[str] = None
    hook_custom_access_token_enabled: typing.Optional[bool] = None
    hook_custom_access_token_uri: typing.Optional[str] = None
    hook_custom_access_token_secrets: typing.Optional[str] = None
    hook_mfa_verification_attempt_enabled: typing.Optional[bool] = None
    hook_mfa_verification_attempt_uri: typing.Optional[str] = None
    hook_mfa_verification_attempt_secrets: typing.Optional[str] = None
    hook_password_verification_attempt_enabled: typing.Optional[bool] = None
    hook_password_verification_attempt_uri: typing.Optional[str] = None
    hook_password_verification_attempt_secrets: typing.Optional[str] = None
    hook_send_sms_enabled: typing.Optional[bool] = None
    hook_send_sms_uri: typing.Optional[str] = None
    hook_send_sms_secrets: typing.Optional[str] = None
    hook_send_email_enabled: typing.Optional[bool] = None
    hook_send_email_uri: typing.Optional[str] = None
    hook_send_email_secrets: typing.Optional[str] = None
    hook_before_user_created_enabled: typing.Optional[bool] = None
    hook_before_user_created_uri: typing.Optional[str] = None
    hook_before_user_created_secrets: typing.Optional[str] = None
    hook_after_user_created_enabled: typing.Optional[bool] = None
    hook_after_user_created_uri: typing.Optional[str] = None
    hook_after_user_created_secrets: typing.Optional[str] = None
    jwt_exp: typing.Optional[int] = None
    mailer_allow_unverified_email_sign_ins: typing.Optional[bool] = None
    mailer_autoconfirm: typing.Optional[bool] = None
    mailer_otp_exp: int
    mailer_otp_length: typing.Optional[int] = None
    mailer_secure_email_change_enabled: typing.Optional[bool] = None
    mailer_subjects_confirmation: typing.Optional[str] = None
    mailer_subjects_email_change: typing.Optional[str] = None
    mailer_subjects_invite: typing.Optional[str] = None
    mailer_subjects_magic_link: typing.Optional[str] = None
    mailer_subjects_reauthentication: typing.Optional[str] = None
    mailer_subjects_recovery: typing.Optional[str] = None
    mailer_subjects_password_changed_notification: typing.Optional[str] = None
    mailer_subjects_email_changed_notification: typing.Optional[str] = None
    mailer_subjects_phone_changed_notification: typing.Optional[str] = None
    mailer_subjects_mfa_factor_enrolled_notification: typing.Optional[str] = None
    mailer_subjects_mfa_factor_unenrolled_notification: typing.Optional[str] = None
    mailer_subjects_identity_linked_notification: typing.Optional[str] = None
    mailer_subjects_identity_unlinked_notification: typing.Optional[str] = None
    mailer_templates_confirmation_content: typing.Optional[str] = None
    mailer_templates_email_change_content: typing.Optional[str] = None
    mailer_templates_invite_content: typing.Optional[str] = None
    mailer_templates_magic_link_content: typing.Optional[str] = None
    mailer_templates_reauthentication_content: typing.Optional[str] = None
    mailer_templates_recovery_content: typing.Optional[str] = None
    mailer_templates_password_changed_notification_content: typing.Optional[str] = None
    mailer_templates_email_changed_notification_content: typing.Optional[str] = None
    mailer_templates_phone_changed_notification_content: typing.Optional[str] = None
    mailer_templates_mfa_factor_enrolled_notification_content: typing.Optional[str] = None
    mailer_templates_mfa_factor_unenrolled_notification_content: typing.Optional[str] = None
    mailer_templates_identity_linked_notification_content: typing.Optional[str] = None
    mailer_templates_identity_unlinked_notification_content: typing.Optional[str] = None
    mailer_notifications_password_changed_enabled: typing.Optional[bool] = None
    mailer_notifications_email_changed_enabled: typing.Optional[bool] = None
    mailer_notifications_phone_changed_enabled: typing.Optional[bool] = None
    mailer_notifications_mfa_factor_enrolled_enabled: typing.Optional[bool] = None
    mailer_notifications_mfa_factor_unenrolled_enabled: typing.Optional[bool] = None
    mailer_notifications_identity_linked_enabled: typing.Optional[bool] = None
    mailer_notifications_identity_unlinked_enabled: typing.Optional[bool] = None
    mfa_max_enrolled_factors: typing.Optional[int] = None
    mfa_totp_enroll_enabled: typing.Optional[bool] = None
    mfa_totp_verify_enabled: typing.Optional[bool] = None
    mfa_phone_enroll_enabled: typing.Optional[bool] = None
    mfa_phone_verify_enabled: typing.Optional[bool] = None
    mfa_web_authn_enroll_enabled: typing.Optional[bool] = None
    mfa_web_authn_verify_enabled: typing.Optional[bool] = None
    passkey_enabled: bool
    webauthn_rp_display_name: typing.Optional[str] = None
    webauthn_rp_id: typing.Optional[str] = None
    webauthn_rp_origins: typing.Optional[str] = None
    mfa_phone_otp_length: int
    mfa_phone_template: typing.Optional[str] = None
    mfa_phone_max_frequency: typing.Optional[int] = None
    nimbus_oauth_client_id: typing.Optional[str] = None
    nimbus_oauth_email_optional: typing.Optional[bool] = None
    nimbus_oauth_client_secret: typing.Optional[str] = None
    password_hibp_enabled: typing.Optional[bool] = None
    password_min_length: typing.Optional[int] = None
    password_required_characters: typing.Optional[AuthConfigResponseOutputPasswordRequiredCharacters] = None
    rate_limit_anonymous_users: typing.Optional[int] = None
    rate_limit_email_sent: typing.Optional[int] = None
    rate_limit_sms_sent: typing.Optional[int] = None
    rate_limit_token_refresh: typing.Optional[int] = None
    rate_limit_verify: typing.Optional[int] = None
    rate_limit_otp: typing.Optional[int] = None
    rate_limit_web3: typing.Optional[int] = None
    refresh_token_rotation_enabled: typing.Optional[bool] = None
    saml_enabled: typing.Optional[bool] = None
    saml_external_url: typing.Optional[str] = None
    saml_allow_encrypted_assertions: typing.Optional[bool] = None
    security_sb_forwarded_for_enabled: typing.Optional[bool] = None
    security_captcha_enabled: typing.Optional[bool] = None
    security_captcha_provider: typing.Optional[AuthConfigResponseOutputSecurityCaptchaProvider] = None
    security_captcha_secret: typing.Optional[str] = None
    security_manual_linking_enabled: typing.Optional[bool] = None
    security_refresh_token_reuse_interval: typing.Optional[int] = None
    security_update_password_require_current_password: typing.Optional[bool] = None
    security_update_password_require_reauthentication: typing.Optional[bool] = None
    sessions_inactivity_timeout: typing.Optional[float] = None
    sessions_single_per_user: typing.Optional[bool] = None
    sessions_tags: typing.Optional[str] = None
    sessions_timebox: typing.Optional[float] = None
    site_url: typing.Optional[str] = None
    sms_autoconfirm: typing.Optional[bool] = None
    sms_max_frequency: typing.Optional[int] = None
    sms_messagebird_access_key: typing.Optional[str] = None
    sms_messagebird_originator: typing.Optional[str] = None
    sms_otp_exp: typing.Optional[int] = None
    sms_otp_length: int
    sms_provider: typing.Optional[AuthConfigResponseOutputSmsProvider] = None
    sms_template: typing.Optional[str] = None
    sms_test_otp: typing.Optional[str] = None
    sms_test_otp_valid_until: typing.Optional[dt.datetime] = None
    sms_textlocal_api_key: typing.Optional[str] = None
    sms_textlocal_sender: typing.Optional[str] = None
    sms_twilio_account_sid: typing.Optional[str] = None
    sms_twilio_auth_token: typing.Optional[str] = None
    sms_twilio_content_sid: typing.Optional[str] = None
    sms_twilio_message_service_sid: typing.Optional[str] = None
    sms_twilio_verify_account_sid: typing.Optional[str] = None
    sms_twilio_verify_auth_token: typing.Optional[str] = None
    sms_twilio_verify_message_service_sid: typing.Optional[str] = None
    sms_vonage_api_key: typing.Optional[str] = None
    sms_vonage_api_secret: typing.Optional[str] = None
    sms_vonage_from: typing.Optional[str] = None
    smtp_admin_email: typing.Optional[str] = None
    smtp_host: typing.Optional[str] = None
    smtp_max_frequency: typing.Optional[int] = None
    smtp_pass: typing.Optional[str] = None
    smtp_port: typing.Optional[str] = None
    smtp_sender_name: typing.Optional[str] = None
    smtp_user: typing.Optional[str] = None
    uri_allow_list: typing.Optional[str] = None
    oauth_server_enabled: bool
    oauth_server_allow_dynamic_registration: bool
    oauth_server_authorization_path: typing.Optional[str] = None
    custom_oauth_enabled: bool
    custom_oauth_max_providers: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
