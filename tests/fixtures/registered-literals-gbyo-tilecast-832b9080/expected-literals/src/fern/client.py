

import datetime as dt
import typing

import httpx
from . import core
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.apply_display_group_control_request_command_type import ApplyDisplayGroupControlRequestCommandType
from .types.asset_status import AssetStatus
from .types.asset_type import AssetType
from .types.brand_bug_input_background_style import BrandBugInputBackgroundStyle
from .types.brand_bug_input_corner import BrandBugInputCorner
from .types.brand_bug_input_target_scope import BrandBugInputTargetScope
from .types.campaign_snapshot import CampaignSnapshot
from .types.compare_publications_request_type import ComparePublicationsRequestType
from .types.compare_publications_response import ComparePublicationsResponse
from .types.countdown_bar_input_display_mode import CountdownBarInputDisplayMode
from .types.countdown_bar_input_progress_fill import CountdownBarInputProgressFill
from .types.countdown_bar_input_schedule_type import CountdownBarInputScheduleType
from .types.countdown_bar_input_target_scope import CountdownBarInputTargetScope
from .types.create_campaign_response import CreateCampaignResponse
from .types.create_playlist_request_source_type import CreatePlaylistRequestSourceType
from .types.data_source_provider import DataSourceProvider
from .types.export_noise_meter_history_request_granularity import ExportNoiseMeterHistoryRequestGranularity
from .types.export_noise_meter_history_request_range import ExportNoiseMeterHistoryRequestRange
from .types.get_api_v1player_updates_release_id_response import GetApiV1PlayerUpdatesReleaseIdResponse
from .types.get_campaign_response import GetCampaignResponse
from .types.get_content_submission_response import GetContentSubmissionResponse
from .types.get_dependency_graph_response import GetDependencyGraphResponse
from .types.inspect_data_source_request_provider import InspectDataSourceRequestProvider
from .types.install_plugin_response import InstallPluginResponse
from .types.list_assets_request_sort import ListAssetsRequestSort
from .types.list_campaign_releases_response import ListCampaignReleasesResponse
from .types.list_campaigns_response import ListCampaignsResponse
from .types.list_content_submissions_request_state import ListContentSubmissionsRequestState
from .types.list_content_submissions_response import ListContentSubmissionsResponse
from .types.list_form_records_request_sort import ListFormRecordsRequestSort
from .types.list_plugins_response import ListPluginsResponse
from .types.list_publication_history_request_type import ListPublicationHistoryRequestType
from .types.list_publication_history_response import ListPublicationHistoryResponse
from .types.manifest_response import ManifestResponse
from .types.noise_meter_history_daily_request_range import NoiseMeterHistoryDailyRequestRange
from .types.noise_meter_history_screens_request_range import NoiseMeterHistoryScreensRequestRange
from .types.noise_meter_history_series_request_range import NoiseMeterHistorySeriesRequestRange
from .types.noise_meter_history_summary_request_range import NoiseMeterHistorySummaryRequestRange
from .types.noise_meter_input_display_mode import NoiseMeterInputDisplayMode
from .types.noise_meter_input_target_scope import NoiseMeterInputTargetScope
from .types.player_heartbeat_noise_meter import PlayerHeartbeatNoiseMeter
from .types.playlist_bulk_item_input import PlaylistBulkItemInput
from .types.playlist_item_input import PlaylistItemInput
from .types.playlist_tag_rule_input_match import PlaylistTagRuleInputMatch
from .types.post_api_v1player_releases_upload_response import PostApiV1PlayerReleasesUploadResponse
from .types.post_api_v1player_update_deployments_deployment_id_status_request_state import (
    PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState,
)
from .types.preflight_campaign_response import PreflightCampaignResponse
from .types.presentation_network_assignment_response import PresentationNetworkAssignmentResponse
from .types.presentation_network_assignments_response import PresentationNetworkAssignmentsResponse
from .types.presentation_network_detail_response import PresentationNetworkDetailResponse
from .types.presentation_network_list_response import PresentationNetworkListResponse
from .types.presentation_network_provisioning_response import PresentationNetworkProvisioningResponse
from .types.presentation_network_readiness_response import PresentationNetworkReadinessResponse
from .types.presentation_network_response import PresentationNetworkResponse
from .types.presentation_network_secret import PresentationNetworkSecret
from .types.presentation_network_security import PresentationNetworkSecurity
from .types.presentation_network_test_response import PresentationNetworkTestResponse
from .types.presentation_override_input_after_action import PresentationOverrideInputAfterAction
from .types.presentation_override_input_content_type import PresentationOverrideInputContentType
from .types.presentation_override_input_target_type import PresentationOverrideInputTargetType
from .types.presentation_reference import PresentationReference
from .types.preview_data_source_request_provider import PreviewDataSourceRequestProvider
from .types.preview_display_group_control_request_command_type import PreviewDisplayGroupControlRequestCommandType
from .types.reset_demo_request_scenario import ResetDemoRequestScenario
from .types.restore_campaign_release_response import RestoreCampaignReleaseResponse
from .types.restore_publication_as_draft_request_type import RestorePublicationAsDraftRequestType
from .types.rollback_publication_request_type import RollbackPublicationRequestType
from .types.span_geometry_input_canvas import SpanGeometryInputCanvas
from .types.span_geometry_input_display_mode import SpanGeometryInputDisplayMode
from .types.span_panel import SpanPanel
from .types.submit_content_draft_request_type import SubmitContentDraftRequestType
from .types.update_campaign_draft_response import UpdateCampaignDraftResponse
from .types.web_authn_assertion_authenticator_attachment import WebAuthnAssertionAuthenticatorAttachment
from .types.web_authn_assertion_response import WebAuthnAssertionResponse
from .types.web_authn_assertion_type import WebAuthnAssertionType
from .types.web_authn_credential_authenticator_attachment import WebAuthnCredentialAuthenticatorAttachment
from .types.web_authn_credential_response import WebAuthnCredentialResponse
from .types.web_authn_credential_type import WebAuthnCredentialType
from .types.widget_input_preset_id import WidgetInputPresetId
from .types.widget_provider import WidgetProvider


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
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
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
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
            base_url=base_url,
            token=token,
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

    def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.health()
        """
        _response = self._raw_client.health(request_options=request_options)
        return _response.data

    def install_linux_player_script(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Public, rate-limited Linux Player provisioning script with this server's URL embedded.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.install_linux_player_script()
        """
        _response = self._raw_client.install_linux_player_script(request_options=request_options)
        return _response.data

    def install_air_play_script(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Public, rate-limited AirPlay provisioning script with this server's URL embedded.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.install_air_play_script()
        """
        _response = self._raw_client.install_air_play_script(request_options=request_options)
        return _response.data

    def install_linux_player_service(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.install_linux_player_service()
        """
        _response = self._raw_client.install_linux_player_service(request_options=request_options)
        return _response.data

    def ready(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.ready()
        """
        _response = self._raw_client.ready(request_options=request_options)
        return _response.data

    def installable_linux_player_release(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.installable_linux_player_release()
        """
        _response = self._raw_client.installable_linux_player_release(request_options=request_options)
        return _response.data

    def installable_linux_player_artifact(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.installable_linux_player_artifact()
        """
        _response = self._raw_client.installable_linux_player_artifact(request_options=request_options)
        return _response.data

    def head_installable_linux_player_artifact(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.head_installable_linux_player_artifact()
        """
        _response = self._raw_client.head_installable_linux_player_artifact(request_options=request_options)
        return _response.headers

    def installable_ux_play_artifact(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Public, rate-limited, pinned UxPlay 1.73.6 source archive embedded in Tilecast Server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.installable_ux_play_artifact()
        """
        _response = self._raw_client.installable_ux_play_artifact(request_options=request_options)
        return _response.data

    def head_installable_ux_play_artifact(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.head_installable_ux_play_artifact()
        """
        _response = self._raw_client.head_installable_ux_play_artifact(request_options=request_options)
        return _response.headers

    def installable_ux_play_checksum(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.installable_ux_play_checksum()
        """
        _response = self._raw_client.installable_ux_play_checksum(request_options=request_options)
        return _response.data

    def auth_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.auth_status()
        """
        _response = self._raw_client.auth_status(request_options=request_options)
        return _response.data

    def demo_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Registered only when TILECAST_ENV is demo. Returns the seeded scenario and the state of each simulated player.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.demo_state()
        """
        _response = self._raw_client.demo_state(request_options=request_options)
        return _response.data

    def reset_demo(
        self,
        *,
        scenario: typing.Optional[ResetDemoRequestScenario] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Registered only when TILECAST_ENV is demo. Replaces all data with a scenario and returns once its simulated players have connected. Requires the Owner role and X-CSRF-Token.

        Parameters
        ----------
        scenario : typing.Optional[ResetDemoRequestScenario]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.reset_demo()
        """
        _response = self._raw_client.reset_demo(scenario=scenario, request_options=request_options)
        return _response.data

    def initial_setup(
        self,
        *,
        organization_name: str,
        owner_name: str,
        username: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organization_name : str

        owner_name : str

        username : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.initial_setup(
            organization_name="organizationName",
            owner_name="ownerName",
            username="username",
            password="password",
        )
        """
        _response = self._raw_client.initial_setup(
            organization_name=organization_name,
            owner_name=owner_name,
            username=username,
            password=password,
            request_options=request_options,
        )
        return _response.data

    def login(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.login()
        """
        _response = self._raw_client.login(request_options=request_options)
        return _response.data

    def verify_multi_factor(
        self, *, challenge_token: str, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Completes a pending sign-in with an authenticator or recovery code.

        Parameters
        ----------
        challenge_token : str

        code : str
            An authenticator code or a recovery code. The server decides which by shape; six digits are never matched against recovery codes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.verify_multi_factor(
            challenge_token="challengeToken",
            code="code",
        )
        """
        _response = self._raw_client.verify_multi_factor(
            challenge_token=challenge_token, code=code, request_options=request_options
        )
        return _response.data

    def multi_factor_passkey_options(
        self, *, challenge_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Exchanges a pending challenge for a WebAuthn assertion request.

        Parameters
        ----------
        challenge_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.multi_factor_passkey_options(
            challenge_token="challengeToken",
        )
        """
        _response = self._raw_client.multi_factor_passkey_options(
            challenge_token=challenge_token, request_options=request_options
        )
        return _response.data

    def passkey_login_options(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Starts a discoverable, username-free WebAuthn ceremony.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.passkey_login_options()
        """
        _response = self._raw_client.passkey_login_options(request_options=request_options)
        return _response.data

    def passkey_login(
        self,
        *,
        mfa_challenge: str,
        id: str,
        raw_id: str,
        type: WebAuthnAssertionType,
        response: WebAuthnAssertionResponse,
        authenticator_attachment: typing.Optional[WebAuthnAssertionAuthenticatorAttachment] = OMIT,
        client_extension_results: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Posts the raw WebAuthn assertion. A verified passkey satisfies multi-factor authentication on its own.

        Parameters
        ----------
        mfa_challenge : str

        id : str

        raw_id : str
            base64url

        type : WebAuthnAssertionType

        response : WebAuthnAssertionResponse

        authenticator_attachment : typing.Optional[WebAuthnAssertionAuthenticatorAttachment]

        client_extension_results : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, WebAuthnAssertionResponse

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.passkey_login(
            mfa_challenge="X-MFA-Challenge",
            id="id",
            raw_id="rawId",
            type="public-key",
            response=WebAuthnAssertionResponse(
                client_data_json="clientDataJSON",
                authenticator_data="authenticatorData",
                signature="signature",
            ),
        )
        """
        _response = self._raw_client.passkey_login(
            mfa_challenge=mfa_challenge,
            id=id,
            raw_id=raw_id,
            type=type,
            response=response,
            authenticator_attachment=authenticator_attachment,
            client_extension_results=client_extension_results,
            request_options=request_options,
        )
        return _response.data

    def security_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.security_status()
        """
        _response = self._raw_client.security_status(request_options=request_options)
        return _response.data

    def begin_authenticator_enrollment(
        self, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.begin_authenticator_enrollment(
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.begin_authenticator_enrollment(
            csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def confirm_authenticator_enrollment(
        self, *, csrf_token: str, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        code : str
            The six-digit authenticator code.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.confirm_authenticator_enrollment(
            csrf_token="X-CSRF-Token",
            code="code",
        )
        """
        _response = self._raw_client.confirm_authenticator_enrollment(
            csrf_token=csrf_token, code=code, request_options=request_options
        )
        return _response.data

    def remove_authenticator(
        self, *, csrf_token: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Requires the account password in the body.

        Parameters
        ----------
        csrf_token : str

        password : str
            The account password, reverified so a borrowed session cannot weaken sign-in security on its own.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.remove_authenticator(
            csrf_token="X-CSRF-Token",
            password="password",
        )
        """
        _response = self._raw_client.remove_authenticator(
            csrf_token=csrf_token, password=password, request_options=request_options
        )
        return _response.data

    def generate_recovery_codes(
        self, *, csrf_token: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Replaces every unused code. Requires the account password. The plain codes are returned exactly once.

        Parameters
        ----------
        csrf_token : str

        password : str
            The account password, reverified so a borrowed session cannot weaken sign-in security on its own.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.generate_recovery_codes(
            csrf_token="X-CSRF-Token",
            password="password",
        )
        """
        _response = self._raw_client.generate_recovery_codes(
            csrf_token=csrf_token, password=password, request_options=request_options
        )
        return _response.data

    def passkey_registration_options(
        self, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.passkey_registration_options(
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.passkey_registration_options(
            csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def register_passkey(
        self,
        *,
        csrf_token: str,
        mfa_challenge: str,
        id: str,
        raw_id: str,
        type: WebAuthnCredentialType,
        response: WebAuthnCredentialResponse,
        authenticator_attachment: typing.Optional[WebAuthnCredentialAuthenticatorAttachment] = OMIT,
        client_extension_results: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The passkey is named from the authenticator's AAGUID; no name is accepted here. Use the rename endpoint to change it.

        Parameters
        ----------
        csrf_token : str

        mfa_challenge : str

        id : str

        raw_id : str
            base64url

        type : WebAuthnCredentialType

        response : WebAuthnCredentialResponse

        authenticator_attachment : typing.Optional[WebAuthnCredentialAuthenticatorAttachment]

        client_extension_results : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, WebAuthnCredentialResponse

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.register_passkey(
            csrf_token="X-CSRF-Token",
            mfa_challenge="X-MFA-Challenge",
            id="id",
            raw_id="rawId",
            type="public-key",
            response=WebAuthnCredentialResponse(
                client_data_json="clientDataJSON",
                attestation_object="attestationObject",
            ),
        )
        """
        _response = self._raw_client.register_passkey(
            csrf_token=csrf_token,
            mfa_challenge=mfa_challenge,
            id=id,
            raw_id=raw_id,
            type=type,
            response=response,
            authenticator_attachment=authenticator_attachment,
            client_extension_results=client_extension_results,
            request_options=request_options,
        )
        return _response.data

    def rename_passkey(
        self, id: str, *, csrf_token: str, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.rename_passkey(
            id="id",
            csrf_token="X-CSRF-Token",
            name="name",
        )
        """
        _response = self._raw_client.rename_passkey(
            id, csrf_token=csrf_token, name=name, request_options=request_options
        )
        return _response.data

    def remove_passkey(
        self, id: str, *, csrf_token: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Requires the account password in the body.

        Parameters
        ----------
        id : str

        csrf_token : str

        password : str
            The account password, reverified so a borrowed session cannot weaken sign-in security on its own.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.remove_passkey(
            id="id",
            csrf_token="X-CSRF-Token",
            password="password",
        )
        """
        _response = self._raw_client.remove_passkey(
            id, csrf_token=csrf_token, password=password, request_options=request_options
        )
        return _response.data

    def reset_user_security(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Owner/Administrator recovery path. Clears every factor, revokes the account's sessions, and records an audit entry.

        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.reset_user_security(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.reset_user_security(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def permanently_delete_user(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Permanently removes an inactive user account. Account-owned preferences, sessions, grants, and security credentials are removed; retained records keep their history with user attribution cleared.

        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.permanently_delete_user(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.permanently_delete_user(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def logout(self, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.logout(
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.logout(csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def installation_identity(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.installation_identity()
        """
        _response = self._raw_client.installation_identity(request_options=request_options)
        return _response.data

    def list_content_folders(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_content_folders()
        """
        _response = self._raw_client.list_content_folders(request_options=request_options)
        return _response.data

    def create_content_folder(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_content_folder()
        """
        _response = self._raw_client.create_content_folder(request_options=request_options)
        return _response.data

    def list_content_collections(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_content_collections()
        """
        _response = self._raw_client.list_content_collections(request_options=request_options)
        return _response.data

    def create_content_collection(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_content_collection()
        """
        _response = self._raw_client.create_content_collection(request_options=request_options)
        return _response.data

    def list_content_tags(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_content_tags()
        """
        _response = self._raw_client.list_content_tags(request_options=request_options)
        return _response.data

    def create_content_tag(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_content_tag()
        """
        _response = self._raw_client.create_content_tag(request_options=request_options)
        return _response.data

    def bulk_organize_assets(
        self,
        *,
        asset_ids: typing.Sequence[str],
        set_folder: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        add_tag_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        remove_tag_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        add_collection_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        remove_collection_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        asset_ids : typing.Sequence[str]

        set_folder : typing.Optional[bool]

        folder_id : typing.Optional[str]

        add_tag_ids : typing.Optional[typing.Sequence[str]]

        remove_tag_ids : typing.Optional[typing.Sequence[str]]

        add_collection_ids : typing.Optional[typing.Sequence[str]]

        remove_collection_ids : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.bulk_organize_assets(
            asset_ids=["assetIds"],
        )
        """
        _response = self._raw_client.bulk_organize_assets(
            asset_ids=asset_ids,
            set_folder=set_folder,
            folder_id=folder_id,
            add_tag_ids=add_tag_ids,
            remove_tag_ids=remove_tag_ids,
            add_collection_ids=add_collection_ids,
            remove_collection_ids=remove_collection_ids,
            request_options=request_options,
        )
        return _response.data

    def create_pairing_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_pairing_session()
        """
        _response = self._raw_client.create_pairing_session(request_options=request_options)
        return _response.data

    def poll_pairing_session(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.poll_pairing_session(
            id="id",
        )
        """
        _response = self._raw_client.poll_pairing_session(id, request_options=request_options)
        return _response.data

    def enroll_player(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.enroll_player()
        """
        _response = self._raw_client.enroll_player(request_options=request_options)
        return _response.data

    def player_heartbeat(
        self,
        *,
        player_family: typing.Optional[str] = OMIT,
        player_architecture: typing.Optional[str] = OMIT,
        noise_meter: typing.Optional[PlayerHeartbeatNoiseMeter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Accepts the authenticated Player heartbeat. Optional Linux Display Control fields report detected providers, independent capabilities, display power observations, and policy state. They do not determine Player online status; command acknowledgement and display state confirmation remain separate.

        The optional `noiseMeter` object carries the Noise Meter plugin's live state and its completed ten-second history buckets. It is derived numbers only — no audio, waveform, or sample is exchanged in either direction. The screen is taken from the authenticated device credential, never from the body, and a batch is bounded to 120 records. Storage is idempotent on screen plus bucket start, so a retried heartbeat cannot duplicate history.

        Parameters
        ----------
        player_family : typing.Optional[str]
            `android`, `electron-linux` or `edge`. The server keeps only these values; another value is recorded as absent.

        player_architecture : typing.Optional[str]
            `x86_64` or `aarch64`, kept only with `playerFamily: edge`. An Edge screen without a known architecture is `incompatible` for Edge deployments.

        noise_meter : typing.Optional[PlayerHeartbeatNoiseMeter]
            Noise Meter plugin state. Contains no audio, waveform, or sample, and levels are the relative 0-100 Tilecast scale rather than dB, dBA, or SPL.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.player_heartbeat()
        """
        _response = self._raw_client.player_heartbeat(
            player_family=player_family,
            player_architecture=player_architecture,
            noise_meter=noise_meter,
            request_options=request_options,
        )
        return _response.data

    def player_liveness(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Records authenticated Player contact for background liveness. This endpoint intentionally accepts no playback snapshot and cannot change the current manifest, content, version, cache policy, or playback state.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.player_liveness(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.player_liveness(request=request, request_options=request_options)
        return _response.data

    def player_socket(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.player_socket()
        """
        _response = self._raw_client.player_socket(request_options=request_options)
        return _response.data

    def list_screens(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_screens()
        """
        _response = self._raw_client.list_screens(request_options=request_options)
        return _response.data

    def get_screen(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_screen(
            id="id",
        )
        """
        _response = self._raw_client.get_screen(id, request_options=request_options)
        return _response.data

    def update_screen(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_screen(
            id="id",
        )
        """
        _response = self._raw_client.update_screen(id, request_options=request_options)
        return _response.data

    def list_screen_player_history(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_screen_player_history(
            id="id",
        )
        """
        _response = self._raw_client.list_screen_player_history(id, request_options=request_options)
        return _response.data

    def resolve_pairing_code(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.resolve_pairing_code()
        """
        _response = self._raw_client.resolve_pairing_code(request_options=request_options)
        return _response.data

    def approve_pairing(
        self,
        id: str,
        *,
        name: str,
        room_name: str,
        room_number: str,
        description: str,
        location_id: typing.Optional[str] = OMIT,
        replace_existing_credential: typing.Optional[bool] = OMIT,
        replace_hardware: typing.Optional[bool] = OMIT,
        replacement_screen_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        name : str

        room_name : str

        room_number : str

        description : str

        location_id : typing.Optional[str]

        replace_existing_credential : typing.Optional[bool]
            Explicitly authorizes credential rotation after successful enrollment.

        replace_hardware : typing.Optional[bool]
            Assigns the new player to an existing logical screen without changing its content or policy relationships.

        replacement_screen_id : typing.Optional[str]
            Required when replaceHardware is true.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.approve_pairing(
            id="id",
            name="name",
            room_name="roomName",
            room_number="roomNumber",
            description="description",
        )
        """
        _response = self._raw_client.approve_pairing(
            id,
            name=name,
            room_name=room_name,
            room_number=room_number,
            description=description,
            location_id=location_id,
            replace_existing_credential=replace_existing_credential,
            replace_hardware=replace_hardware,
            replacement_screen_id=replacement_screen_id,
            request_options=request_options,
        )
        return _response.data

    def list_locations(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_locations()
        """
        _response = self._raw_client.list_locations(request_options=request_options)
        return _response.data

    def create_location(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_location()
        """
        _response = self._raw_client.create_location(request_options=request_options)
        return _response.data

    def delete_location(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_location(
            id="id",
        )
        """
        _response = self._raw_client.delete_location(id, request_options=request_options)
        return _response.data

    def update_location(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_location(
            id="id",
        )
        """
        _response = self._raw_client.update_location(id, request_options=request_options)
        return _response.data

    def list_plugins(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListPluginsResponse:
        """
        Every plugin the running release offers, joined with this installation's state. Readable by any signed-in account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPluginsResponse
            Plugin catalog

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_plugins()
        """
        _response = self._raw_client.list_plugins(request_options=request_options)
        return _response.data

    def install_plugin(
        self, plugin_id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InstallPluginResponse:
        """
        Records a release-owned plugin as installed. Idempotent. Never downloads or runs code.

        Parameters
        ----------
        plugin_id : str
            Registry identifier such as noise_meter.

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstallPluginResponse
            Plugin installed by this request

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.install_plugin(
            plugin_id="pluginId",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.install_plugin(plugin_id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def remove_plugin(
        self, plugin_id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the installation record. Never deletes plugin data; refuses while plugin-owned resources remain. Idempotent for a plugin that is not installed. An installation row for a plugin this release does not know may also be removed; only the row is deleted.

        Parameters
        ----------
        plugin_id : str
            Registry identifier such as noise_meter.

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.remove_plugin(
            plugin_id="pluginId",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.remove_plugin(plugin_id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def get_dependency_graph(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDependencyGraphResponse:
        """
        Returns the current content and delivery topology. Directed edges run from a dependency to the record that consumes it. Dependency Graph is a Studio system tool, not an installable plugin.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDependencyGraphResponse
            Typed dependency nodes and directed consumer edges

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_dependency_graph()
        """
        _response = self._raw_client.get_dependency_graph(request_options=request_options)
        return _response.data

    def list_countdown_bar_instances(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_countdown_bar_instances()
        """
        _response = self._raw_client.list_countdown_bar_instances(request_options=request_options)
        return _response.data

    def create_countdown_bar_instance(
        self,
        *,
        csrf_token: str,
        name: str,
        message: str,
        schedule_type: CountdownBarInputScheduleType,
        days_of_week: typing.Sequence[int],
        timezone: str,
        lead_time_seconds: int,
        completion_text: str,
        show_confetti: bool,
        display_mode: CountdownBarInputDisplayMode,
        height_px: int,
        urgency_enabled: bool,
        starting_soon_seconds: int,
        urgent_seconds: int,
        pulse_seconds: int,
        enabled: bool,
        priority: int,
        target_scope: CountdownBarInputTargetScope,
        target_ids: typing.Sequence[str],
        target_time: typing.Optional[str] = OMIT,
        one_time_at: typing.Optional[dt.datetime] = OMIT,
        progress_fill: typing.Optional[CountdownBarInputProgressFill] = OMIT,
        content_padding: typing.Optional[int] = OMIT,
        text_scale: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        name : str

        message : str

        schedule_type : CountdownBarInputScheduleType

        days_of_week : typing.Sequence[int]

        timezone : str

        lead_time_seconds : int

        completion_text : str

        show_confetti : bool
            Show a short confetti fall from the top of the Player when the countdown reaches zero. This does not require completion text.

        display_mode : CountdownBarInputDisplayMode

        height_px : int

        urgency_enabled : bool
            Enable automatic starting-soon, urgent, and final pulse stages.

        starting_soon_seconds : int

        urgent_seconds : int

        pulse_seconds : int
            Final seconds during which the urgent bar pulses and grows by 25 percent.

        enabled : bool

        priority : int

        target_scope : CountdownBarInputTargetScope

        target_ids : typing.Sequence[str]

        target_time : typing.Optional[str]

        one_time_at : typing.Optional[dt.datetime]

        progress_fill : typing.Optional[CountdownBarInputProgressFill]
            Background treatment behind the bar text. "drain" starts the bar fully tinted when the lead window opens and retreats the tint leftward as the target approaches, leaving only the bar background at zero. Omitted means "none".

        content_padding : typing.Optional[int]
            Share of each side left as a gutter, as a percentage of the bar width. Lowering it gives a long message or a larger type size more room. The default 4 matches the bar's original gutters.

        text_scale : typing.Optional[int]
            Percentage applied to the height-derived type size, so a bar can carry larger text without changing its height. 100 is the original appearance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_countdown_bar_instance(
            csrf_token="X-CSRF-Token",
            name="name",
            message="message",
            schedule_type="weekly",
            days_of_week=[1],
            timezone="timezone",
            lead_time_seconds=1,
            completion_text="completionText",
            show_confetti=True,
            display_mode="overlay",
            height_px=1,
            urgency_enabled=True,
            starting_soon_seconds=1,
            urgent_seconds=1,
            pulse_seconds=1,
            enabled=True,
            priority=1,
            target_scope="all",
            target_ids=["targetIds"],
        )
        """
        _response = self._raw_client.create_countdown_bar_instance(
            csrf_token=csrf_token,
            name=name,
            message=message,
            schedule_type=schedule_type,
            days_of_week=days_of_week,
            timezone=timezone,
            lead_time_seconds=lead_time_seconds,
            completion_text=completion_text,
            show_confetti=show_confetti,
            display_mode=display_mode,
            height_px=height_px,
            urgency_enabled=urgency_enabled,
            starting_soon_seconds=starting_soon_seconds,
            urgent_seconds=urgent_seconds,
            pulse_seconds=pulse_seconds,
            enabled=enabled,
            priority=priority,
            target_scope=target_scope,
            target_ids=target_ids,
            target_time=target_time,
            one_time_at=one_time_at,
            progress_fill=progress_fill,
            content_padding=content_padding,
            text_scale=text_scale,
            request_options=request_options,
        )
        return _response.data

    def get_countdown_bar_instance(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_countdown_bar_instance(
            id="id",
        )
        """
        _response = self._raw_client.get_countdown_bar_instance(id, request_options=request_options)
        return _response.data

    def update_countdown_bar_instance(
        self,
        id: str,
        *,
        csrf_token: str,
        name: str,
        message: str,
        schedule_type: CountdownBarInputScheduleType,
        days_of_week: typing.Sequence[int],
        timezone: str,
        lead_time_seconds: int,
        completion_text: str,
        show_confetti: bool,
        display_mode: CountdownBarInputDisplayMode,
        height_px: int,
        urgency_enabled: bool,
        starting_soon_seconds: int,
        urgent_seconds: int,
        pulse_seconds: int,
        enabled: bool,
        priority: int,
        target_scope: CountdownBarInputTargetScope,
        target_ids: typing.Sequence[str],
        target_time: typing.Optional[str] = OMIT,
        one_time_at: typing.Optional[dt.datetime] = OMIT,
        progress_fill: typing.Optional[CountdownBarInputProgressFill] = OMIT,
        content_padding: typing.Optional[int] = OMIT,
        text_scale: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        name : str

        message : str

        schedule_type : CountdownBarInputScheduleType

        days_of_week : typing.Sequence[int]

        timezone : str

        lead_time_seconds : int

        completion_text : str

        show_confetti : bool
            Show a short confetti fall from the top of the Player when the countdown reaches zero. This does not require completion text.

        display_mode : CountdownBarInputDisplayMode

        height_px : int

        urgency_enabled : bool
            Enable automatic starting-soon, urgent, and final pulse stages.

        starting_soon_seconds : int

        urgent_seconds : int

        pulse_seconds : int
            Final seconds during which the urgent bar pulses and grows by 25 percent.

        enabled : bool

        priority : int

        target_scope : CountdownBarInputTargetScope

        target_ids : typing.Sequence[str]

        target_time : typing.Optional[str]

        one_time_at : typing.Optional[dt.datetime]

        progress_fill : typing.Optional[CountdownBarInputProgressFill]
            Background treatment behind the bar text. "drain" starts the bar fully tinted when the lead window opens and retreats the tint leftward as the target approaches, leaving only the bar background at zero. Omitted means "none".

        content_padding : typing.Optional[int]
            Share of each side left as a gutter, as a percentage of the bar width. Lowering it gives a long message or a larger type size more room. The default 4 matches the bar's original gutters.

        text_scale : typing.Optional[int]
            Percentage applied to the height-derived type size, so a bar can carry larger text without changing its height. 100 is the original appearance.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_countdown_bar_instance(
            id="id",
            csrf_token="X-CSRF-Token",
            name="name",
            message="message",
            schedule_type="weekly",
            days_of_week=[1],
            timezone="timezone",
            lead_time_seconds=1,
            completion_text="completionText",
            show_confetti=True,
            display_mode="overlay",
            height_px=1,
            urgency_enabled=True,
            starting_soon_seconds=1,
            urgent_seconds=1,
            pulse_seconds=1,
            enabled=True,
            priority=1,
            target_scope="all",
            target_ids=["targetIds"],
        )
        """
        _response = self._raw_client.update_countdown_bar_instance(
            id,
            csrf_token=csrf_token,
            name=name,
            message=message,
            schedule_type=schedule_type,
            days_of_week=days_of_week,
            timezone=timezone,
            lead_time_seconds=lead_time_seconds,
            completion_text=completion_text,
            show_confetti=show_confetti,
            display_mode=display_mode,
            height_px=height_px,
            urgency_enabled=urgency_enabled,
            starting_soon_seconds=starting_soon_seconds,
            urgent_seconds=urgent_seconds,
            pulse_seconds=pulse_seconds,
            enabled=enabled,
            priority=priority,
            target_scope=target_scope,
            target_ids=target_ids,
            target_time=target_time,
            one_time_at=one_time_at,
            progress_fill=progress_fill,
            content_padding=content_padding,
            text_scale=text_scale,
            request_options=request_options,
        )
        return _response.data

    def delete_countdown_bar_instance(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_countdown_bar_instance(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.delete_countdown_bar_instance(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def list_brand_bug_instances(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_brand_bug_instances()
        """
        _response = self._raw_client.list_brand_bug_instances(request_options=request_options)
        return _response.data

    def create_brand_bug_instance(
        self,
        *,
        csrf_token: str,
        name: str,
        corner: BrandBugInputCorner,
        text: str,
        width_percent: int,
        text_size_percent: int,
        opacity_percent: int,
        margin_percent: int,
        text_color: str,
        background_style: BrandBugInputBackgroundStyle,
        enabled: bool,
        priority: int,
        target_scope: BrandBugInputTargetScope,
        target_ids: typing.Sequence[str],
        image_asset_id: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[dt.datetime] = OMIT,
        ends_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        name : str

        corner : BrandBugInputCorner

        text : str

        width_percent : int

        text_size_percent : int

        opacity_percent : int

        margin_percent : int

        text_color : str

        background_style : BrandBugInputBackgroundStyle

        enabled : bool

        priority : int

        target_scope : BrandBugInputTargetScope

        target_ids : typing.Sequence[str]

        image_asset_id : typing.Optional[str]
            A ready image in the Media library.

        starts_at : typing.Optional[dt.datetime]

        ends_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_brand_bug_instance(
            csrf_token="X-CSRF-Token",
            name="name",
            corner="top_left",
            text="text",
            width_percent=1,
            text_size_percent=1,
            opacity_percent=1,
            margin_percent=1,
            text_color="textColor",
            background_style="none",
            enabled=True,
            priority=1,
            target_scope="all",
            target_ids=["targetIds"],
        )
        """
        _response = self._raw_client.create_brand_bug_instance(
            csrf_token=csrf_token,
            name=name,
            corner=corner,
            text=text,
            width_percent=width_percent,
            text_size_percent=text_size_percent,
            opacity_percent=opacity_percent,
            margin_percent=margin_percent,
            text_color=text_color,
            background_style=background_style,
            enabled=enabled,
            priority=priority,
            target_scope=target_scope,
            target_ids=target_ids,
            image_asset_id=image_asset_id,
            starts_at=starts_at,
            ends_at=ends_at,
            request_options=request_options,
        )
        return _response.data

    def get_brand_bug_instance(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_brand_bug_instance(
            id="id",
        )
        """
        _response = self._raw_client.get_brand_bug_instance(id, request_options=request_options)
        return _response.data

    def update_brand_bug_instance(
        self,
        id: str,
        *,
        csrf_token: str,
        name: str,
        corner: BrandBugInputCorner,
        text: str,
        width_percent: int,
        text_size_percent: int,
        opacity_percent: int,
        margin_percent: int,
        text_color: str,
        background_style: BrandBugInputBackgroundStyle,
        enabled: bool,
        priority: int,
        target_scope: BrandBugInputTargetScope,
        target_ids: typing.Sequence[str],
        image_asset_id: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[dt.datetime] = OMIT,
        ends_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        name : str

        corner : BrandBugInputCorner

        text : str

        width_percent : int

        text_size_percent : int

        opacity_percent : int

        margin_percent : int

        text_color : str

        background_style : BrandBugInputBackgroundStyle

        enabled : bool

        priority : int

        target_scope : BrandBugInputTargetScope

        target_ids : typing.Sequence[str]

        image_asset_id : typing.Optional[str]
            A ready image in the Media library.

        starts_at : typing.Optional[dt.datetime]

        ends_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_brand_bug_instance(
            id="id",
            csrf_token="X-CSRF-Token",
            name="name",
            corner="top_left",
            text="text",
            width_percent=1,
            text_size_percent=1,
            opacity_percent=1,
            margin_percent=1,
            text_color="textColor",
            background_style="none",
            enabled=True,
            priority=1,
            target_scope="all",
            target_ids=["targetIds"],
        )
        """
        _response = self._raw_client.update_brand_bug_instance(
            id,
            csrf_token=csrf_token,
            name=name,
            corner=corner,
            text=text,
            width_percent=width_percent,
            text_size_percent=text_size_percent,
            opacity_percent=opacity_percent,
            margin_percent=margin_percent,
            text_color=text_color,
            background_style=background_style,
            enabled=enabled,
            priority=priority,
            target_scope=target_scope,
            target_ids=target_ids,
            image_asset_id=image_asset_id,
            starts_at=starts_at,
            ends_at=ends_at,
            request_options=request_options,
        )
        return _response.data

    def delete_brand_bug_instance(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_brand_bug_instance(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.delete_brand_bug_instance(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def list_noise_meter_instances(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_noise_meter_instances()
        """
        _response = self._raw_client.list_noise_meter_instances(request_options=request_options)
        return _response.data

    def create_noise_meter_instance(
        self,
        *,
        csrf_token: str,
        name: str,
        message: str,
        warning_level: int,
        loud_level: int,
        sensitivity: int,
        trigger_hold_ms: int,
        clear_hold_ms: int,
        display_mode: NoiseMeterInputDisplayMode,
        height_px: int,
        enabled: bool,
        target_scope: NoiseMeterInputTargetScope,
        target_ids: typing.Sequence[str],
        schedule_enabled: typing.Optional[bool] = OMIT,
        schedule_days_of_week: typing.Optional[typing.Sequence[int]] = OMIT,
        schedule_start_time: typing.Optional[str] = OMIT,
        schedule_end_time: typing.Optional[str] = OMIT,
        schedule_timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        name : str

        message : str
            Replaces the bar's own TOO LOUD label. Empty is allowed.

        warning_level : int
            Where the yellow zone begins, and the level the room must stay below before the bar hides.

        loud_level : int
            Where the red zone begins and the bar can appear.

        sensitivity : int
            Percentage applied to the captured signal before normalization, for a microphone that reads quiet or hot. Not a calibration.

        trigger_hold_ms : int
            How long the room must stay loud before the bar appears.

        clear_hold_ms : int
            How long it must stay below warningLevel before the bar hides.

        display_mode : NoiseMeterInputDisplayMode

        height_px : int

        enabled : bool

        target_scope : NoiseMeterInputTargetScope

        target_ids : typing.Sequence[str]

        schedule_enabled : typing.Optional[bool]
            When false the bar may show whenever the room is too loud. A window governs the bar alone; the room is measured either way.

        schedule_days_of_week : typing.Optional[typing.Sequence[int]]
            Days the window may start on, Sunday 0 through Saturday 6.

        schedule_start_time : typing.Optional[str]

        schedule_end_time : typing.Optional[str]
            At or before the start is an overnight window belonging to the start day. The window is half-open, so the end minute is outside it.

        schedule_timezone : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_noise_meter_instance(
            csrf_token="X-CSRF-Token",
            name="name",
            message="message",
            warning_level=1,
            loud_level=1,
            sensitivity=1,
            trigger_hold_ms=1,
            clear_hold_ms=1,
            display_mode="overlay",
            height_px=1,
            enabled=True,
            target_scope="all",
            target_ids=["targetIds"],
        )
        """
        _response = self._raw_client.create_noise_meter_instance(
            csrf_token=csrf_token,
            name=name,
            message=message,
            warning_level=warning_level,
            loud_level=loud_level,
            sensitivity=sensitivity,
            trigger_hold_ms=trigger_hold_ms,
            clear_hold_ms=clear_hold_ms,
            display_mode=display_mode,
            height_px=height_px,
            enabled=enabled,
            target_scope=target_scope,
            target_ids=target_ids,
            schedule_enabled=schedule_enabled,
            schedule_days_of_week=schedule_days_of_week,
            schedule_start_time=schedule_start_time,
            schedule_end_time=schedule_end_time,
            schedule_timezone=schedule_timezone,
            request_options=request_options,
        )
        return _response.data

    def get_noise_meter_instance(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_noise_meter_instance(
            id="id",
        )
        """
        _response = self._raw_client.get_noise_meter_instance(id, request_options=request_options)
        return _response.data

    def update_noise_meter_instance(
        self,
        id: str,
        *,
        csrf_token: str,
        name: str,
        message: str,
        warning_level: int,
        loud_level: int,
        sensitivity: int,
        trigger_hold_ms: int,
        clear_hold_ms: int,
        display_mode: NoiseMeterInputDisplayMode,
        height_px: int,
        enabled: bool,
        target_scope: NoiseMeterInputTargetScope,
        target_ids: typing.Sequence[str],
        schedule_enabled: typing.Optional[bool] = OMIT,
        schedule_days_of_week: typing.Optional[typing.Sequence[int]] = OMIT,
        schedule_start_time: typing.Optional[str] = OMIT,
        schedule_end_time: typing.Optional[str] = OMIT,
        schedule_timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        name : str

        message : str
            Replaces the bar's own TOO LOUD label. Empty is allowed.

        warning_level : int
            Where the yellow zone begins, and the level the room must stay below before the bar hides.

        loud_level : int
            Where the red zone begins and the bar can appear.

        sensitivity : int
            Percentage applied to the captured signal before normalization, for a microphone that reads quiet or hot. Not a calibration.

        trigger_hold_ms : int
            How long the room must stay loud before the bar appears.

        clear_hold_ms : int
            How long it must stay below warningLevel before the bar hides.

        display_mode : NoiseMeterInputDisplayMode

        height_px : int

        enabled : bool

        target_scope : NoiseMeterInputTargetScope

        target_ids : typing.Sequence[str]

        schedule_enabled : typing.Optional[bool]
            When false the bar may show whenever the room is too loud. A window governs the bar alone; the room is measured either way.

        schedule_days_of_week : typing.Optional[typing.Sequence[int]]
            Days the window may start on, Sunday 0 through Saturday 6.

        schedule_start_time : typing.Optional[str]

        schedule_end_time : typing.Optional[str]
            At or before the start is an overnight window belonging to the start day. The window is half-open, so the end minute is outside it.

        schedule_timezone : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_noise_meter_instance(
            id="id",
            csrf_token="X-CSRF-Token",
            name="name",
            message="message",
            warning_level=1,
            loud_level=1,
            sensitivity=1,
            trigger_hold_ms=1,
            clear_hold_ms=1,
            display_mode="overlay",
            height_px=1,
            enabled=True,
            target_scope="all",
            target_ids=["targetIds"],
        )
        """
        _response = self._raw_client.update_noise_meter_instance(
            id,
            csrf_token=csrf_token,
            name=name,
            message=message,
            warning_level=warning_level,
            loud_level=loud_level,
            sensitivity=sensitivity,
            trigger_hold_ms=trigger_hold_ms,
            clear_hold_ms=clear_hold_ms,
            display_mode=display_mode,
            height_px=height_px,
            enabled=enabled,
            target_scope=target_scope,
            target_ids=target_ids,
            schedule_enabled=schedule_enabled,
            schedule_days_of_week=schedule_days_of_week,
            schedule_start_time=schedule_start_time,
            schedule_end_time=schedule_end_time,
            schedule_timezone=schedule_timezone,
            request_options=request_options,
        )
        return _response.data

    def delete_noise_meter_instance(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_noise_meter_instance(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.delete_noise_meter_instance(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def noise_meter_history_summary(
        self,
        id: str,
        *,
        range: typing.Optional[NoiseMeterHistorySummaryRequestRange] = None,
        screen_id: typing.Optional[str] = None,
        tz: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Descriptive statistics for the selected range: average and peak relative level, time in each band, warning events counted by the Player, the longest continuous loud run, and the loudest fifteen minutes. Screens are resolved from the caller's own scope.

        Parameters
        ----------
        id : str

        range : typing.Optional[NoiseMeterHistorySummaryRequestRange]

        screen_id : typing.Optional[str]
            One screen, authorized with the same screen scope as every other screen operation. Omitted means every screen the account may see.

        tz : typing.Optional[str]
            IANA timezone for day boundaries. Unreadable values fall back to UTC.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.noise_meter_history_summary(
            id="id",
        )
        """
        _response = self._raw_client.noise_meter_history_summary(
            id, range=range, screen_id=screen_id, tz=tz, request_options=request_options
        )
        return _response.data

    def noise_meter_history_series(
        self,
        id: str,
        *,
        range: typing.Optional[NoiseMeterHistorySeriesRequestRange] = None,
        screen_id: typing.Optional[str] = None,
        tz: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Timeline points at the range's presentation resolution — one minute for a day, fifteen minutes for a week, an hour for a month. Averages are weighted by monitored time, peaks keep the maximum, durations sum, and a period with no records is omitted rather than returned as zero.

        Parameters
        ----------
        id : str

        range : typing.Optional[NoiseMeterHistorySeriesRequestRange]

        screen_id : typing.Optional[str]
            One screen, authorized with the same screen scope as every other screen operation. Omitted means every screen the account may see.

        tz : typing.Optional[str]
            IANA timezone for day boundaries. Unreadable values fall back to UTC.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.noise_meter_history_series(
            id="id",
        )
        """
        _response = self._raw_client.noise_meter_history_series(
            id, range=range, screen_id=screen_id, tz=tz, request_options=request_options
        )
        return _response.data

    def noise_meter_history_daily(
        self,
        id: str,
        *,
        range: typing.Optional[NoiseMeterHistoryDailyRequestRange] = None,
        screen_id: typing.Optional[str] = None,
        tz: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Per-day rollups. Days without monitoring are absent, never zero.

        Parameters
        ----------
        id : str

        range : typing.Optional[NoiseMeterHistoryDailyRequestRange]

        screen_id : typing.Optional[str]
            One screen, authorized with the same screen scope as every other screen operation. Omitted means every screen the account may see.

        tz : typing.Optional[str]
            IANA timezone for day boundaries. Unreadable values fall back to UTC.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.noise_meter_history_daily(
            id="id",
        )
        """
        _response = self._raw_client.noise_meter_history_daily(
            id, range=range, screen_id=screen_id, tz=tz, request_options=request_options
        )
        return _response.data

    def noise_meter_history_screens(
        self,
        id: str,
        *,
        range: typing.Optional[NoiseMeterHistoryScreensRequestRange] = None,
        tz: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Which of the caller's screens hold history for this meter in the range, so History shows one screen directly and offers a selector only when there is something to select.

        Parameters
        ----------
        id : str

        range : typing.Optional[NoiseMeterHistoryScreensRequestRange]

        tz : typing.Optional[str]
            IANA timezone for day boundaries. Unreadable values fall back to UTC.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.noise_meter_history_screens(
            id="id",
        )
        """
        _response = self._raw_client.noise_meter_history_screens(
            id, range=range, tz=tz, request_options=request_options
        )
        return _response.data

    def export_noise_meter_history(
        self,
        id: str,
        *,
        range: typing.Optional[ExportNoiseMeterHistoryRequestRange] = None,
        screen_id: typing.Optional[str] = None,
        tz: typing.Optional[str] = None,
        granularity: typing.Optional[ExportNoiseMeterHistoryRequestGranularity] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        CSV of the selected range and screens, streamed server-side. Granularity is the stored ten-second records, one-minute summaries, or daily summaries.

        Parameters
        ----------
        id : str

        range : typing.Optional[ExportNoiseMeterHistoryRequestRange]

        screen_id : typing.Optional[str]
            One screen, authorized with the same screen scope as every other screen operation. Omitted means every screen the account may see.

        tz : typing.Optional[str]
            IANA timezone for day boundaries. Unreadable values fall back to UTC.

        granularity : typing.Optional[ExportNoiseMeterHistoryRequestGranularity]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.export_noise_meter_history(
            id="id",
        )
        """
        _response = self._raw_client.export_noise_meter_history(
            id, range=range, screen_id=screen_id, tz=tz, granularity=granularity, request_options=request_options
        )
        return _response.data

    def reject_pairing(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.reject_pairing(
            id="id",
        )
        """
        _response = self._raw_client.reject_pairing(id, request_options=request_options)
        return _response.data

    def disable_screen(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.disable_screen(
            id="id",
        )
        """
        _response = self._raw_client.disable_screen(id, request_options=request_options)
        return _response.data

    def enable_screen(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.enable_screen(
            id="id",
        )
        """
        _response = self._raw_client.enable_screen(id, request_options=request_options)
        return _response.data

    def revoke_screen_credential(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.revoke_screen_credential(
            id="id",
        )
        """
        _response = self._raw_client.revoke_screen_credential(id, request_options=request_options)
        return _response.data

    def create_upload_session(
        self,
        *,
        csrf_token: str,
        filename: str,
        mime_type: str,
        size_bytes: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        filename : str

        mime_type : str

        size_bytes : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_upload_session(
            csrf_token="X-CSRF-Token",
            filename="filename",
            mime_type="mimeType",
            size_bytes=1000000,
        )
        """
        _response = self._raw_client.create_upload_session(
            csrf_token=csrf_token,
            filename=filename,
            mime_type=mime_type,
            size_bytes=size_bytes,
            request_options=request_options,
        )
        return _response.data

    def cancel_upload(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cancel_upload(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.cancel_upload(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def append_upload_bytes(
        self, id: str, *, csrf_token: str, upload_offset: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        upload_offset : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.append_upload_bytes(
            id="id",
            csrf_token="X-CSRF-Token",
            upload_offset=1000000,
        )
        """
        _response = self._raw_client.append_upload_bytes(
            id, csrf_token=csrf_token, upload_offset=upload_offset, request_options=request_options
        )
        return _response.data

    def inspect_upload_session(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inspect_upload_session(
            id="id",
        )
        """
        _response = self._raw_client.inspect_upload_session(id, request_options=request_options)
        return _response.headers

    def complete_upload(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.complete_upload(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.complete_upload(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def list_assets(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        type: typing.Optional[AssetType] = None,
        status: typing.Optional[AssetStatus] = None,
        sort: typing.Optional[ListAssetsRequestSort] = None,
        archived: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        page_size : typing.Optional[int]

        search : typing.Optional[str]

        type : typing.Optional[AssetType]

        status : typing.Optional[AssetStatus]

        sort : typing.Optional[ListAssetsRequestSort]

        archived : typing.Optional[bool]
            Return manually archived and automatically expired library content instead of active content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_assets()
        """
        _response = self._raw_client.list_assets(
            page=page,
            page_size=page_size,
            search=search,
            type=type,
            status=status,
            sort=sort,
            archived=archived,
            request_options=request_options,
        )
        return _response.data

    def archive_assets(
        self,
        *,
        csrf_token: str,
        asset_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        asset_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.archive_assets(
            csrf_token="X-CSRF-Token",
            asset_ids=["assetIds"],
        )
        """
        _response = self._raw_client.archive_assets(
            csrf_token=csrf_token, asset_ids=asset_ids, request_options=request_options
        )
        return _response.data

    def restore_assets(
        self,
        *,
        csrf_token: str,
        asset_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        asset_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.restore_assets(
            csrf_token="X-CSRF-Token",
            asset_ids=["assetIds"],
        )
        """
        _response = self._raw_client.restore_assets(
            csrf_token=csrf_token, asset_ids=asset_ids, request_options=request_options
        )
        return _response.data

    def get_asset(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_asset(
            id="id",
        )
        """
        _response = self._raw_client.get_asset(id, request_options=request_options)
        return _response.data

    def delete_asset(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_asset(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.delete_asset(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def update_asset(
        self,
        id: str,
        *,
        csrf_token: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        availability_set: typing.Optional[bool] = OMIT,
        available_from: typing.Optional[dt.datetime] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        availability_set : typing.Optional[bool]

        available_from : typing.Optional[dt.datetime]

        expires_at : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_asset(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.update_asset(
            id,
            csrf_token=csrf_token,
            name=name,
            description=description,
            availability_set=availability_set,
            available_from=available_from,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data

    def retry_asset_processing(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.retry_asset_processing(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.retry_asset_processing(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def get_asset_thumbnail(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_asset_thumbnail(
            id="id",
        )
        """
        _response = self._raw_client.get_asset_thumbnail(id, request_options=request_options)
        return _response.data

    def get_asset_playback_preview(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_asset_playback_preview(
            id="id",
        )
        """
        _response = self._raw_client.get_asset_playback_preview(id, request_options=request_options)
        return _response.data

    def head_asset_playback_preview(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.head_asset_playback_preview(
            id="id",
        )
        """
        _response = self._raw_client.head_asset_playback_preview(id, request_options=request_options)
        return _response.headers

    def download_player_variant(
        self,
        asset_id: str,
        variant_id: str,
        *,
        range: typing.Optional[str] = None,
        if_range: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        asset_id : str

        variant_id : str

        range : typing.Optional[str]

        if_range : typing.Optional[str]

        if_none_match : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.download_player_variant(
            asset_id="assetId",
            variant_id="variantId",
            range="bytes=0-1048575",
        )
        """
        _response = self._raw_client.download_player_variant(
            asset_id,
            variant_id,
            range=range,
            if_range=if_range,
            if_none_match=if_none_match,
            request_options=request_options,
        )
        return _response.data

    def inspect_player_variant(
        self, asset_id: str, variant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        asset_id : str

        variant_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inspect_player_variant(
            asset_id="assetId",
            variant_id="variantId",
        )
        """
        _response = self._raw_client.inspect_player_variant(asset_id, variant_id, request_options=request_options)
        return _response.headers

    def list_playlists(
        self,
        *,
        search: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_playlists()
        """
        _response = self._raw_client.list_playlists(
            search=search, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def create_playlist(
        self,
        *,
        csrf_token: str,
        name: str,
        description: str,
        source_type: CreatePlaylistRequestSourceType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        name : str

        description : str

        source_type : CreatePlaylistRequestSourceType
            static creates a manually ordered timeline; tag creates an initially empty tag-driven playlist

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_playlist(
            csrf_token="X-CSRF-Token",
            name="name",
            description="description",
            source_type="static",
        )
        """
        _response = self._raw_client.create_playlist(
            csrf_token=csrf_token,
            name=name,
            description=description,
            source_type=source_type,
            request_options=request_options,
        )
        return _response.data

    def get_playlist(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_playlist(
            id="id",
        )
        """
        _response = self._raw_client.get_playlist(id, request_options=request_options)
        return _response.data

    def delete_playlist(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_playlist(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.delete_playlist(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def update_playlist(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_playlist(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.update_playlist(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def add_playlist_item(
        self,
        id: str,
        *,
        csrf_token: str,
        request: PlaylistItemInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request : PlaylistItemInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.add_playlist_item(
            id="id",
            csrf_token="csrfToken",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.add_playlist_item(
            id, csrf_token=csrf_token, request=request, request_options=request_options
        )
        return _response.data

    def reorder_playlist_items(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.reorder_playlist_items(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.reorder_playlist_items(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def bulk_update_playlist_items(
        self,
        id: str,
        *,
        csrf_token: str,
        request: PlaylistBulkItemInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request : PlaylistBulkItemInput

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.bulk_update_playlist_items(
            id="id",
            csrf_token="csrfToken",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.bulk_update_playlist_items(
            id, csrf_token=csrf_token, request=request, request_options=request_options
        )
        return _response.data

    def set_playlist_tag_rule(
        self,
        id: str,
        *,
        csrf_token: str,
        enabled: bool,
        match: PlaylistTagRuleInputMatch,
        image_duration_ms: int,
        tag_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        enabled : bool

        match : PlaylistTagRuleInputMatch

        image_duration_ms : int

        tag_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.set_playlist_tag_rule(
            id="id",
            csrf_token="X-CSRF-Token",
            enabled=True,
            match="any",
            image_duration_ms=1,
            tag_ids=["tagIds"],
        )
        """
        _response = self._raw_client.set_playlist_tag_rule(
            id,
            csrf_token=csrf_token,
            enabled=enabled,
            match=match,
            image_duration_ms=image_duration_ms,
            tag_ids=tag_ids,
            request_options=request_options,
        )
        return _response.data

    def delete_playlist_item(
        self, id: str, item_id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        item_id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_playlist_item(
            id="id",
            item_id="itemId",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.delete_playlist_item(
            id, item_id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def update_playlist_item(
        self, id: str, item_id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        item_id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_playlist_item(
            id="id",
            item_id="itemId",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.update_playlist_item(
            id, item_id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def get_playlist_assignment(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_playlist_assignment(
            id="id",
        )
        """
        _response = self._raw_client.get_playlist_assignment(id, request_options=request_options)
        return _response.data

    def assign_presentation(
        self,
        id: str,
        *,
        csrf_token: str,
        request: PresentationReference,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request : PresentationReference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, PresentationReferencePlaylistId

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.assign_presentation(
            id="id",
            csrf_token="X-CSRF-Token",
            request=PresentationReferencePlaylistId(
                playlist_id="playlistId",
            ),
        )
        """
        _response = self._raw_client.assign_presentation(
            id, csrf_token=csrf_token, request=request, request_options=request_options
        )
        return _response.data

    def remove_playlist_assignment(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.remove_playlist_assignment(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.remove_playlist_assignment(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def get_player_manifest(
        self, *, if_none_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ManifestResponse:
        """
        Parameters
        ----------
        if_none_match : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ManifestResponse
            Stable screen-specific manifest or no-assignment manifest

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_player_manifest()
        """
        _response = self._raw_client.get_player_manifest(if_none_match=if_none_match, request_options=request_options)
        return _response.data

    def get_player_span_panel(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_player_span_panel(
            id="id",
        )
        """
        _response = self._raw_client.get_player_span_panel(id, request_options=request_options)
        return _response.data

    def head_player_span_panel(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.head_player_span_panel(
            id="id",
        )
        """
        _response = self._raw_client.head_player_span_panel(id, request_options=request_options)
        return _response.headers

    def list_screen_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_screen_groups()
        """
        _response = self._raw_client.list_screen_groups(request_options=request_options)
        return _response.data

    def create_screen_group(self, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_screen_group(
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.create_screen_group(csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def get_screen_group(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_screen_group(
            id="id",
        )
        """
        _response = self._raw_client.get_screen_group(id, request_options=request_options)
        return _response.data

    def delete_screen_group(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_screen_group(
            id="id",
        )
        """
        _response = self._raw_client.delete_screen_group(id, request_options=request_options)
        return _response.data

    def update_screen_group(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_screen_group(
            id="id",
        )
        """
        _response = self._raw_client.update_screen_group(id, request_options=request_options)
        return _response.data

    def get_span_geometry_and_preparation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_span_geometry_and_preparation(
            id="id",
        )
        """
        _response = self._raw_client.get_span_geometry_and_preparation(id, request_options=request_options)
        return _response.data

    def update_span_geometry(
        self,
        id: str,
        *,
        csrf_token: str,
        display_mode: typing.Optional[SpanGeometryInputDisplayMode] = OMIT,
        canvas: typing.Optional[SpanGeometryInputCanvas] = OMIT,
        panels: typing.Optional[typing.Sequence[SpanPanel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        display_mode : typing.Optional[SpanGeometryInputDisplayMode]

        canvas : typing.Optional[SpanGeometryInputCanvas]

        panels : typing.Optional[typing.Sequence[SpanPanel]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_span_geometry(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.update_span_geometry(
            id,
            csrf_token=csrf_token,
            display_mode=display_mode,
            canvas=canvas,
            panels=panels,
            request_options=request_options,
        )
        return _response.data

    def preview_display_group_control(
        self,
        id: str,
        *,
        command_type: PreviewDisplayGroupControlRequestCommandType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        command_type : PreviewDisplayGroupControlRequestCommandType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.preview_display_group_control(
            id="id",
            command_type="display_power_on",
        )
        """
        _response = self._raw_client.preview_display_group_control(
            id, command_type=command_type, request_options=request_options
        )
        return _response.data

    def apply_display_group_control(
        self,
        id: str,
        *,
        csrf_token: str,
        command_type: ApplyDisplayGroupControlRequestCommandType,
        fingerprint: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        command_type : ApplyDisplayGroupControlRequestCommandType

        fingerprint : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.apply_display_group_control(
            id="id",
            csrf_token="X-CSRF-Token",
            command_type="display_power_on",
            fingerprint="fingerprint",
        )
        """
        _response = self._raw_client.apply_display_group_control(
            id,
            csrf_token=csrf_token,
            command_type=command_type,
            fingerprint=fingerprint,
            request_options=request_options,
        )
        return _response.data

    def add_screen_group_member(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.add_screen_group_member(
            id="id",
        )
        """
        _response = self._raw_client.add_screen_group_member(id, request_options=request_options)
        return _response.data

    def remove_screen_group_member(
        self, id: str, screen_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        screen_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.remove_screen_group_member(
            id="id",
            screen_id="screenId",
        )
        """
        _response = self._raw_client.remove_screen_group_member(id, screen_id, request_options=request_options)
        return _response.data

    def assign_sync_group_presentation(
        self, id: str, *, request: PresentationReference, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request : PresentationReference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, PresentationReferencePlaylistId

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.assign_sync_group_presentation(
            id="id",
            request=PresentationReferencePlaylistId(
                playlist_id="playlistId",
            ),
        )
        """
        _response = self._raw_client.assign_sync_group_presentation(
            id, request=request, request_options=request_options
        )
        return _response.data

    def unassign_sync_group_playlist(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.unassign_sync_group_playlist(
            id="id",
        )
        """
        _response = self._raw_client.unassign_sync_group_playlist(id, request_options=request_options)
        return _response.data

    def list_schedules(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_schedules()
        """
        _response = self._raw_client.list_schedules(request_options=request_options)
        return _response.data

    def create_schedule(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        The request contains exactly one of playlistId, layoutId, or displayAction. Display Control actions use the closed typed command registry; display_probe is not schedulable.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_schedule()
        """
        _response = self._raw_client.create_schedule(request_options=request_options)
        return _response.data

    def get_schedule(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_schedule(
            id="id",
        )
        """
        _response = self._raw_client.get_schedule(id, request_options=request_options)
        return _response.data

    def delete_schedule(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_schedule(
            id="id",
        )
        """
        _response = self._raw_client.delete_schedule(id, request_options=request_options)
        return _response.data

    def update_schedule(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_schedule(
            id="id",
        )
        """
        _response = self._raw_client.update_schedule(id, request_options=request_options)
        return _response.data

    def enable_schedule(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.enable_schedule(
            id="id",
        )
        """
        _response = self._raw_client.enable_schedule(id, request_options=request_options)
        return _response.data

    def disable_schedule(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.disable_schedule(
            id="id",
        )
        """
        _response = self._raw_client.disable_schedule(id, request_options=request_options)
        return _response.data

    def preview_schedule(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.preview_schedule()
        """
        _response = self._raw_client.preview_schedule(request_options=request_options)
        return _response.data

    def create_website_asset(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Creates configuration-only public website content without fetching the page.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_website_asset()
        """
        _response = self._raw_client.create_website_asset(request_options=request_options)
        return _response.data

    def update_website_asset(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_website_asset(
            id="id",
        )
        """
        _response = self._raw_client.update_website_asset(id, request_options=request_options)
        return _response.data

    def website_diagnostics(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.website_diagnostics(
            id="id",
        )
        """
        _response = self._raw_client.website_diagnostics(id, request_options=request_options)
        return _response.data

    def create_widget(
        self,
        *,
        provider: WidgetProvider,
        name: str,
        configuration: typing.Dict[str, typing.Any],
        preset_id: typing.Optional[WidgetInputPresetId] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a reusable Widget or catalog App. An App recipe may atomically provision one hidden managed Data Source while preserving normal dependency and manifest behavior.

        Parameters
        ----------
        provider : WidgetProvider

        name : str

        configuration : typing.Dict[str, typing.Any]
            Provider-specific configuration. Native text Widgets omit textScale for automatic bounds-first sizing or use 25–500 percent; contentPadding defaults to 10 percent per edge and accepts 0–40.

        preset_id : typing.Optional[WidgetInputPresetId]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_widget(
            provider="provider",
            name="name",
            configuration={"key": "value"},
        )
        """
        _response = self._raw_client.create_widget(
            provider=provider,
            name=name,
            configuration=configuration,
            preset_id=preset_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def provider_catalog(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.provider_catalog()
        """
        _response = self._raw_client.provider_catalog(request_options=request_options)
        return _response.data

    def content_definitions(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.content_definitions()
        """
        _response = self._raw_client.content_definitions(request_options=request_options)
        return _response.data

    def compile_widget_preview(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.compile_widget_preview()
        """
        _response = self._raw_client.compile_widget_preview(request_options=request_options)
        return _response.data

    def update_widget(
        self,
        id: str,
        *,
        provider: WidgetProvider,
        name: str,
        configuration: typing.Dict[str, typing.Any],
        preset_id: typing.Optional[WidgetInputPresetId] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        provider : WidgetProvider

        name : str

        configuration : typing.Dict[str, typing.Any]
            Provider-specific configuration. Native text Widgets omit textScale for automatic bounds-first sizing or use 25–500 percent; contentPadding defaults to 10 percent per edge and accepts 0–40.

        preset_id : typing.Optional[WidgetInputPresetId]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_widget(
            id="id",
            provider="provider",
            name="name",
            configuration={"key": "value"},
        )
        """
        _response = self._raw_client.update_widget(
            id,
            provider=provider,
            name=name,
            configuration=configuration,
            preset_id=preset_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def update_widget_preview_image(
        self,
        id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Stores the frozen image captured from the actual Widget editor render. Requires an editor-capable dashboard session and CSRF token. The server accepts only a 960 by 540 JPEG no larger than 500 KB; Widget configuration updates clear the prior snapshot so stale renders are never shown.

        Parameters
        ----------
        id : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = self._raw_client.update_widget_preview_image(id, request=request, request_options=request_options)
        return _response.data

    def duplicate_widget(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.duplicate_widget(
            id="id",
        )
        """
        _response = self._raw_client.duplicate_widget(id, request_options=request_options)
        return _response.data

    def list_data_sources(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_data_sources()
        """
        _response = self._raw_client.list_data_sources(request_options=request_options)
        return _response.data

    def create_data_source(
        self,
        *,
        provider: DataSourceProvider,
        name: str,
        configuration: typing.Dict[str, typing.Any],
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a reusable provider-neutral Data Source. Supported providers include calendar, structured feeds, Manual Table, Weather, Transit, CAP Alerts, and Air Quality. Data Sources are not assets and cannot be placed in playlists or Layouts.

        Parameters
        ----------
        provider : DataSourceProvider

        name : str

        configuration : typing.Dict[str, typing.Any]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_data_source(
            provider="calendar",
            name="name",
            configuration={"key": "value"},
        )
        """
        _response = self._raw_client.create_data_source(
            provider=provider,
            name=name,
            configuration=configuration,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def get_data_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_data_source(
            id="id",
        )
        """
        _response = self._raw_client.get_data_source(id, request_options=request_options)
        return _response.data

    def delete_data_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_data_source(
            id="id",
        )
        """
        _response = self._raw_client.delete_data_source(id, request_options=request_options)
        return _response.data

    def update_data_source(
        self,
        id: str,
        *,
        provider: DataSourceProvider,
        name: str,
        configuration: typing.Dict[str, typing.Any],
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        provider : DataSourceProvider

        name : str

        configuration : typing.Dict[str, typing.Any]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_data_source(
            id="id",
            provider="calendar",
            name="name",
            configuration={"key": "value"},
        )
        """
        _response = self._raw_client.update_data_source(
            id,
            provider=provider,
            name=name,
            configuration=configuration,
            description=description,
            request_options=request_options,
        )
        return _response.data

    def duplicate_data_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.duplicate_data_source(
            id="id",
        )
        """
        _response = self._raw_client.duplicate_data_source(id, request_options=request_options)
        return _response.data

    def data_source_refresh_diagnostics(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.data_source_refresh_diagnostics(
            id="id",
        )
        """
        _response = self._raw_client.data_source_refresh_diagnostics(id, request_options=request_options)
        return _response.data

    def preview_data_source(
        self,
        provider: PreviewDataSourceRequestProvider,
        *,
        configuration: typing.Dict[str, typing.Any],
        preview_date: typing.Optional[dt.date] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Fetches and parses a candidate Data Source configuration under the safe fetch policy without saving raw data. A previewDate exercises date-aware selection.

        Parameters
        ----------
        provider : PreviewDataSourceRequestProvider

        configuration : typing.Dict[str, typing.Any]

        preview_date : typing.Optional[dt.date]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.preview_data_source(
            provider="calendar",
            configuration={"key": "value"},
        )
        """
        _response = self._raw_client.preview_data_source(
            provider, configuration=configuration, preview_date=preview_date, request_options=request_options
        )
        return _response.data

    def inspect_saved_data_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Detects fields for a saved RSS, Atom, JSON, or CSV Source using its stored configuration, including uploaded CSV bytes that detail responses strip. Same response shape as the provider inspect route.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inspect_saved_data_source(
            id="id",
        )
        """
        _response = self._raw_client.inspect_saved_data_source(id, request_options=request_options)
        return _response.data

    def inspect_data_source(
        self,
        provider: InspectDataSourceRequestProvider,
        *,
        configuration: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Reports the fields a candidate RSS, Atom, JSON, or CSV connection contains, with a few sample values per field, a suggested field mapping, and which record fields the Source can fill. Runs under the same safe fetch policy as preview and deliberately does not require a mapping, because the mapping is what it exists to produce.

        Parameters
        ----------
        provider : InspectDataSourceRequestProvider

        configuration : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inspect_data_source(
            provider="rss",
            configuration={"key": "value"},
        )
        """
        _response = self._raw_client.inspect_data_source(
            provider, configuration=configuration, request_options=request_options
        )
        return _response.data

    def list_forms(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns every Form Data Source the current user can access, each with name, description, published revision number, the caller's effective capabilities, and the caller's own submission counts (drafts, submitted, changes requested). A global Owner sees all forms; everyone else sees forms they created or hold a grant on. Backs the Forms portal and operator navigation.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_forms()
        """
        _response = self._raw_client.list_forms(request_options=request_options)
        return _response.data

    def create_form(
        self,
        *,
        name: str,
        draft_schema: typing.Dict[str, typing.Any],
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a Form Data Source (a Data Source provider). The server publishes the supplied draft schema as the form's first immutable revision and the creator becomes its manager. Requires the editor+ global role.

        Parameters
        ----------
        name : str

        draft_schema : typing.Dict[str, typing.Any]

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_form(
            name="name",
            draft_schema={"key": "value"},
        )
        """
        _response = self._raw_client.create_form(
            name=name, draft_schema=draft_schema, description=description, request_options=request_options
        )
        return _response.data

    def get_form(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns the Form detail with draft schema, published revision, workflow, saved views, and the caller's granted capabilities. Each workflow state carries recordCount and a removable flag (false once any record or saved view references it) so the Workflow editor can lock keys/deletion. Non-managers receive the published schema as the visible draft schema so unpublished edits are never exposed.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_form(
            id="id",
        )
        """
        _response = self._raw_client.get_form(id, request_options=request_options)
        return _response.data

    def update_form_metadata(
        self,
        id: str,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates only the parent Data Source name and description. An omitted description preserves the stored value; provider and configuration cannot be changed here. Requires the manage capability.

        Parameters
        ----------
        id : str

        name : str

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_form_metadata(
            id="id",
            name="name",
        )
        """
        _response = self._raw_client.update_form_metadata(
            id, name=name, description=description, request_options=request_options
        )
        return _response.data

    def update_form_draft(
        self, id: str, *, schema: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Replaces the editable draft schema without publishing. Existing submissions are untouched. Requires the manage capability.

        Parameters
        ----------
        id : str

        schema : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_form_draft(
            id="id",
            schema={"key": "value"},
        )
        """
        _response = self._raw_client.update_form_draft(id, schema=schema, request_options=request_options)
        return _response.data

    def publish_form(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Snapshots the current draft into a new immutable revision after conservative compatibility checks (a previously published output field cannot be removed or change its output type). Existing submissions remain tied to their original revisions. Requires the manage capability.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.publish_form(
            id="id",
        )
        """
        _response = self._raw_client.publish_form(id, request_options=request_options)
        return _response.data

    def configure_form_workflow(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Reconciles the form's bounded, script-free approval workflow in place. State keys referenced by existing records are immutable; transitions are replaced wholesale. Requires the manage capability.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.configure_form_workflow(
            id="id",
        )
        """
        _response = self._raw_client.configure_form_workflow(id, request_options=request_options)
        return _response.data

    def list_form_records(
        self,
        id: str,
        *,
        states: typing.Optional[str] = None,
        mine: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        sort: typing.Optional[ListFormRecordsRequestSort] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Returns a filtered, paginated page of a form's records. Callers with view_all, review, approve, or manage see every record; a submitter without those sees only their own submissions. `mine=true` scopes the page to the caller's own submissions even for privileged callers (the Forms portal's "your submissions"). Supports states, search, sort, mine, page, and pageSize query parameters.

        Parameters
        ----------
        id : str

        states : typing.Optional[str]
            Comma-separated workflow state keys

        mine : typing.Optional[bool]
            Scope to the caller's own submissions

        search : typing.Optional[str]

        sort : typing.Optional[ListFormRecordsRequestSort]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_form_records(
            id="id",
        )
        """
        _response = self._raw_client.list_form_records(
            id,
            states=states,
            mine=mine,
            search=search,
            sort=sort,
            page=page,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    def create_form_record(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Creates a draft submission bound to the form's current published revision. Requires the submit capability. Image field values are never accepted here — they are set only by the attachment upload/remove endpoints — and a client-supplied image value is rejected. Display metadata dates are tri-state (omitted preserves, null clears, a value sets).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_form_record(
            id="id",
        )
        """
        _response = self._raw_client.create_form_record(id, request_options=request_options)
        return _response.data

    def get_form_record(
        self, id: str, record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a record with its immutable revision schema, history, comments, attachments, and the server-calculated actions the caller may take (canEdit, canComment, canDelete, and availableTransitions with destination, label, required capability, and whether a note is required). Authorization is resolved server-side so clients never re-implement it. Visible only to a manager, reviewer/approver, view_all holder, or the record's own submitter.

        Parameters
        ----------
        id : str

        record_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_form_record(
            id="id",
            record_id="recordId",
        )
        """
        _response = self._raw_client.get_form_record(id, record_id, request_options=request_options)
        return _response.data

    def delete_form_record(
        self, id: str, record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Soft-deletes a record. Requires the manage capability.

        Parameters
        ----------
        id : str

        record_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_form_record(
            id="id",
            record_id="recordId",
        )
        """
        _response = self._raw_client.delete_form_record(id, record_id, request_options=request_options)
        return _response.data

    def update_form_record(
        self, id: str, record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Edits a record's values and display metadata under optimistic concurrency (a version is required). Image field values are preserved server-side and cannot be changed here (a client-supplied image value is rejected); only the attachment endpoints modify them. Display dates are tri-state. A manager may edit any record; a submitter may edit their own record only while it is in a submitter-editable state.

        Parameters
        ----------
        id : str

        record_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_form_record(
            id="id",
            record_id="recordId",
        )
        """
        _response = self._raw_client.update_form_record(id, record_id, request_options=request_options)
        return _response.data

    def transition_form_record(
        self, id: str, record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Moves a record to a new workflow state, enforcing the configured transition, per-form capability and record ownership, optimistic concurrency (version), and required-field completeness (including required images, satisfied only by a bound attachment) before any submit transition or any transition into an output-eligible state. A note is recorded as a comment; a transition that requires a note (the default changes_requested path, derived from the workflow) is rejected with 422 when the note is empty. A 409 means the record changed; reload, preserving any unsent note.

        Parameters
        ----------
        id : str

        record_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.transition_form_record(
            id="id",
            record_id="recordId",
        )
        """
        _response = self._raw_client.transition_form_record(id, record_id, request_options=request_options)
        return _response.data

    def add_form_record_comment(
        self, id: str, record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Adds a reviewer or submitter comment. Available to a reviewer/approver or the record's own submitter.

        Parameters
        ----------
        id : str

        record_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.add_form_record_comment(
            id="id",
            record_id="recordId",
        )
        """
        _response = self._raw_client.add_form_record_comment(id, record_id, request_options=request_options)
        return _response.data

    def upload_form_record_attachment(
        self,
        id: str,
        record_id: str,
        *,
        field_key: str,
        data: str,
        version: int,
        file_name: typing.Optional[str] = OMIT,
        content_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Uploads a base64-encoded image as a dedicated form attachment bound to an image field, returning the updated record detail with its incremented version. Uses optimistic concurrency — the request body must carry the record's current `version`, and a mismatch returns 409. Because image fields are single-valued, uploading to a field that already has an attachment replaces it. Authorization matches record editing. Form attachments are never exposed through the general Media library.

        Parameters
        ----------
        id : str

        record_id : str

        field_key : str

        data : str
            base64-encoded image bytes

        version : int
            The record's current version

        file_name : typing.Optional[str]

        content_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.upload_form_record_attachment(
            id="id",
            record_id="recordId",
            field_key="fieldKey",
            data="data",
            version=1,
        )
        """
        _response = self._raw_client.upload_form_record_attachment(
            id,
            record_id,
            field_key=field_key,
            data=data,
            version=version,
            file_name=file_name,
            content_type=content_type,
            request_options=request_options,
        )
        return _response.data

    def remove_form_record_attachment(
        self,
        id: str,
        record_id: str,
        attachment_id: str,
        *,
        version: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Unbinds an attachment, clears the field value it backed, and soft-deletes the underlying asset. Uses optimistic concurrency — the record's current `version` is required as a query parameter and a mismatch returns 409. Authorization matches record editing. Returns the updated record detail.

        Parameters
        ----------
        id : str

        record_id : str

        attachment_id : str

        version : int
            The record's current version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.remove_form_record_attachment(
            id="id",
            record_id="recordId",
            attachment_id="attachmentId",
            version=1,
        )
        """
        _response = self._raw_client.remove_form_record_attachment(
            id, record_id, attachment_id, version=version, request_options=request_options
        )
        return _response.data

    def serve_form_record_attachment(
        self, id: str, record_id: str, attachment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Streams a record's image attachment through this form-record-authorized endpoint (the only way to view a form attachment; they are never served from the Media library). Applies the same visibility rules as reading the record.

        Parameters
        ----------
        id : str

        record_id : str

        attachment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.serve_form_record_attachment(
            id="id",
            record_id="recordId",
            attachment_id="attachmentId",
        )
        """
        _response = self._raw_client.serve_form_record_attachment(
            id, record_id, attachment_id, request_options=request_options
        )
        return _response.data

    def list_approvals(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Returns a paginated page of records awaiting a review decision across every Form the user may review, approve, or manage. A record is pending when its current state has an outgoing transition requiring the review or approve capability. Paginated (page, pageSize) with a total rather than silently capped.

        Parameters
        ----------
        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_approvals()
        """
        _response = self._raw_client.list_approvals(page=page, page_size=page_size, request_options=request_options)
        return _response.data

    def preview_form_view(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Projects an unsaved, proposed saved view and returns the resulting typed dataset without persisting anything or altering the cached projection. Only output-eligible records in the view's included states are returned, so a preview never exposes unapproved records. Requires the manage capability.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.preview_form_view(
            id="id",
        )
        """
        _response = self._raw_client.preview_form_view(id, request_options=request_options)
        return _response.data

    def get_form_outputs(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns the generated dataset for each saved view (dataset key, output fields and types, current record count, preview records) plus form-level projection status (last successful projection, next scheduled refresh/time-window boundary, using-cached/stale flag, projection error) and per-view Widget usage. Preview records come from the cached payload, so only output-eligible records appear. Available to view_all or manage.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_form_outputs(
            id="id",
        )
        """
        _response = self._raw_client.get_form_outputs(id, request_options=request_options)
        return _response.data

    def rebuild_form_outputs(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Manually re-runs the form projection and returns the refreshed Outputs status. Invalidates affected manifests. Requires the manage capability and CSRF.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.rebuild_form_outputs(
            id="id",
        )
        """
        _response = self._raw_client.rebuild_form_outputs(id, request_options=request_options)
        return _response.data

    def list_form_access(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns one entry per user with effective access to the form — the creator and all active global Owners as implicit, uneditable managers, followed by each granted user with their collapsed (non-redundant) capability set. Requires the manage capability.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_form_access(
            id="id",
        )
        """
        _response = self._raw_client.list_form_access(id, request_options=request_options)
        return _response.data

    def replace_form_grants(
        self,
        id: str,
        user_id: str,
        *,
        capabilities: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Atomically replaces one user's grants on the form with the supplied capabilities (submit, view_own, view_all, review, approve, manage), collapsing implied capabilities to a minimal set, in a single transaction with an audit entry. The form creator and global Owners cannot be edited here, and a manager cannot remove their own only management path. Requires the manage capability and CSRF.

        Parameters
        ----------
        id : str

        user_id : str

        capabilities : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.replace_form_grants(
            id="id",
            user_id="userId",
            capabilities=["capabilities"],
        )
        """
        _response = self._raw_client.replace_form_grants(
            id, user_id, capabilities=capabilities, request_options=request_options
        )
        return _response.data

    def search_form_users(
        self,
        id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        A bounded, manager-safe user directory for granting form access, returning only id, name, username, and global role for active users. Authorized to the form's managers (per-form), never the Owner/Admin-only user administration API.

        Parameters
        ----------
        id : str

        search : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.search_form_users(
            id="id",
        )
        """
        _response = self._raw_client.search_form_users(id, search=search, limit=limit, request_options=request_options)
        return _response.data

    def list_layouts(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Layout summaries include hasUnpublishedChanges, computed by comparing the current draft document with the published document rather than by comparing their independent revision counters.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_layouts()
        """
        _response = self._raw_client.list_layouts(request_options=request_options)
        return _response.data

    def create_layout(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_layout()
        """
        _response = self._raw_client.create_layout(request_options=request_options)
        return _response.data

    def get_layout(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_layout(
            id="id",
        )
        """
        _response = self._raw_client.get_layout(id, request_options=request_options)
        return _response.data

    def delete_layout(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_layout(
            id="id",
        )
        """
        _response = self._raw_client.delete_layout(id, request_options=request_options)
        return _response.data

    def update_layout(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_layout(
            id="id",
        )
        """
        _response = self._raw_client.update_layout(id, request_options=request_options)
        return _response.data

    def save_layout_draft(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Saves a validated draft using expectedDraftRevision optimistic concurrency.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.save_layout_draft(
            id="id",
        )
        """
        _response = self._raw_client.save_layout_draft(id, request_options=request_options)
        return _response.data

    def get_layout_preview_image(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Serves the authenticated, frozen JPEG captured from the real Layout editor canvas.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_layout_preview_image(
            id="id",
        )
        """
        _response = self._raw_client.get_layout_preview_image(id, request_options=request_options)
        return _response.data

    def update_layout_preview_image(
        self, id: str, *, draft_revision: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Stores an aspect-preserving JPEG of at most 500 KB when draftRevision still matches the current Layout draft.

        Parameters
        ----------
        id : str

        draft_revision : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_layout_preview_image(
            id="id",
            draft_revision=1000000,
        )
        """
        _response = self._raw_client.update_layout_preview_image(
            id, draft_revision=draft_revision, request_options=request_options
        )
        return _response.data

    def publish_layout(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.publish_layout(
            id="id",
        )
        """
        _response = self._raw_client.publish_layout(id, request_options=request_options)
        return _response.data

    def duplicate_layout(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.duplicate_layout(
            id="id",
        )
        """
        _response = self._raw_client.duplicate_layout(id, request_options=request_options)
        return _response.data

    def list_layout_revisions(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_layout_revisions(
            id="id",
        )
        """
        _response = self._raw_client.list_layout_revisions(id, request_options=request_options)
        return _response.data

    def restore_layout_revision(
        self, id: str, revision_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        revision_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.restore_layout_revision(
            id="id",
            revision_id="revisionId",
        )
        """
        _response = self._raw_client.restore_layout_revision(id, revision_id, request_options=request_options)
        return _response.data

    def list_content_submissions(
        self,
        *,
        state: typing.Optional[ListContentSubmissionsRequestState] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListContentSubmissionsResponse:
        """
        Lists immutable Playlist, Layout, and Campaign submissions. A submission snapshot is not changed by later draft edits.

        Parameters
        ----------
        state : typing.Optional[ListContentSubmissionsRequestState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListContentSubmissionsResponse
            Submission list and current review policy

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_content_submissions()
        """
        _response = self._raw_client.list_content_submissions(state=state, request_options=request_options)
        return _response.data

    def get_content_submission(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetContentSubmissionResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContentSubmissionResponse
            Exact immutable submission snapshot

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_content_submission(
            id="id",
        )
        """
        _response = self._raw_client.get_content_submission(id, request_options=request_options)
        return _response.data

    def submit_content_draft(
        self,
        type: SubmitContentDraftRequestType,
        id: str,
        *,
        csrf_token: str,
        requested_publication_at: typing.Optional[dt.datetime] = OMIT,
        expected_revision: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Freezes the current working draft. expectedRevision is optional optimistic concurrency protection.

        Parameters
        ----------
        type : SubmitContentDraftRequestType

        id : str

        csrf_token : str

        requested_publication_at : typing.Optional[dt.datetime]

        expected_revision : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.submit_content_draft(
            type="playlist",
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.submit_content_draft(
            type,
            id,
            csrf_token=csrf_token,
            requested_publication_at=requested_publication_at,
            expected_revision=expected_revision,
            request_options=request_options,
        )
        return _response.data

    def approve_content_submission(
        self,
        id: str,
        *,
        csrf_token: str,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        note : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.approve_content_submission(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.approve_content_submission(
            id, csrf_token=csrf_token, note=note, request_options=request_options
        )
        return _response.data

    def request_content_changes(
        self, id: str, *, csrf_token: str, note: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        note : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.request_content_changes(
            id="id",
            csrf_token="X-CSRF-Token",
            note="note",
        )
        """
        _response = self._raw_client.request_content_changes(
            id, csrf_token=csrf_token, note=note, request_options=request_options
        )
        return _response.data

    def publish_content_submission(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.publish_content_submission(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.publish_content_submission(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def schedule_content_publication(
        self,
        id: str,
        *,
        csrf_token: str,
        requested_publication_at: dt.datetime,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        requested_publication_at : dt.datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.schedule_content_publication(
            id="id",
            csrf_token="X-CSRF-Token",
            requested_publication_at=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.schedule_content_publication(
            id,
            csrf_token=csrf_token,
            requested_publication_at=requested_publication_at,
            request_options=request_options,
        )
        return _response.data

    def cancel_content_publication_schedule(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cancel_content_publication_schedule(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.cancel_content_publication_schedule(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def list_publication_history(
        self,
        type: ListPublicationHistoryRequestType,
        id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPublicationHistoryResponse:
        """
        Parameters
        ----------
        type : ListPublicationHistoryRequestType

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPublicationHistoryResponse
            Immutable publication checkpoints, newest first

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_publication_history(
            type="playlist",
            id="id",
        )
        """
        _response = self._raw_client.list_publication_history(type, id, request_options=request_options)
        return _response.data

    def compare_publications(
        self,
        type: ComparePublicationsRequestType,
        id: str,
        *,
        from_publication_id: str,
        to_publication_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ComparePublicationsResponse:
        """
        Parameters
        ----------
        type : ComparePublicationsRequestType

        id : str

        from_publication_id : str

        to_publication_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComparePublicationsResponse
            Semantic publication differences

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.compare_publications(
            type="playlist",
            id="id",
            from_publication_id="fromPublicationId",
            to_publication_id="toPublicationId",
        )
        """
        _response = self._raw_client.compare_publications(
            type,
            id,
            from_publication_id=from_publication_id,
            to_publication_id=to_publication_id,
            request_options=request_options,
        )
        return _response.data

    def restore_publication_as_draft(
        self,
        type: RestorePublicationAsDraftRequestType,
        id: str,
        publication_id: str,
        *,
        csrf_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        type : RestorePublicationAsDraftRequestType

        id : str

        publication_id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.restore_publication_as_draft(
            type="playlist",
            id="id",
            publication_id="publicationId",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.restore_publication_as_draft(
            type, id, publication_id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def rollback_publication(
        self,
        type: RollbackPublicationRequestType,
        id: str,
        publication_id: str,
        *,
        csrf_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        type : RollbackPublicationRequestType

        id : str

        publication_id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.rollback_publication(
            type="playlist",
            id="id",
            publication_id="publicationId",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.rollback_publication(
            type, id, publication_id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def list_campaigns(
        self,
        *,
        search: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCampaignsResponse:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCampaignsResponse
            Campaign library

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_campaigns()
        """
        _response = self._raw_client.list_campaigns(
            search=search, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    def create_campaign(
        self,
        *,
        csrf_token: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCampaignResponse:
        """
        Parameters
        ----------
        csrf_token : str

        name : str

        description : typing.Optional[str]

        timezone : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCampaignResponse
            Campaign draft created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_campaign(
            csrf_token="X-CSRF-Token",
            name="name",
        )
        """
        _response = self._raw_client.create_campaign(
            csrf_token=csrf_token,
            name=name,
            description=description,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    def get_campaign(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetCampaignResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCampaignResponse
            Campaign draft and lifecycle state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_campaign(
            id="id",
        )
        """
        _response = self._raw_client.get_campaign(id, request_options=request_options)
        return _response.data

    def archive_campaign(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.archive_campaign(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.archive_campaign(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    def update_campaign_draft(
        self,
        id: str,
        *,
        csrf_token: str,
        expected_draft_revision: int,
        draft: CampaignSnapshot,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCampaignDraftResponse:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        expected_draft_revision : int

        draft : CampaignSnapshot

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCampaignDraftResponse
            Campaign draft saved

        Examples
        --------
        from fern import CampaignBlock, CampaignDestination, CampaignSnapshot, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_campaign_draft(
            id="id",
            csrf_token="X-CSRF-Token",
            expected_draft_revision=1000000,
            draft=CampaignSnapshot(
                name="name",
                description="description",
                timezone="timezone",
                destinations=[
                    CampaignDestination(
                        type="screen",
                        id="id",
                    )
                ],
                blocks=[
                    CampaignBlock(
                        id="id",
                        name="name",
                        content_type="playlist",
                        content_id="contentId",
                        priority=1,
                        type="one_time",
                        timezone="timezone",
                        enabled=True,
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.update_campaign_draft(
            id,
            csrf_token=csrf_token,
            expected_draft_revision=expected_draft_revision,
            draft=draft,
            request_options=request_options,
        )
        return _response.data

    def preflight_campaign(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreflightCampaignResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreflightCampaignResponse
            Readiness, target, revision, and schedule preflight

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.preflight_campaign(
            id="id",
        )
        """
        _response = self._raw_client.preflight_campaign(id, request_options=request_options)
        return _response.data

    def list_campaign_releases(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListCampaignReleasesResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCampaignReleasesResponse
            Immutable Campaign release history

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_campaign_releases(
            id="id",
        )
        """
        _response = self._raw_client.list_campaign_releases(id, request_options=request_options)
        return _response.data

    def restore_campaign_release(
        self, id: str, release_id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RestoreCampaignReleaseResponse:
        """
        Parameters
        ----------
        id : str

        release_id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RestoreCampaignReleaseResponse
            Release copied into the working Campaign draft

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.restore_campaign_release(
            id="id",
            release_id="releaseId",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.restore_campaign_release(
            id, release_id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def publish_campaign(
        self,
        id: str,
        *,
        csrf_token: str,
        expected_draft_revision: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Publishes one immutable Campaign release by atomically materializing ordinary scheduler rows; Players do not receive a Campaign type.

        Parameters
        ----------
        id : str

        csrf_token : str

        expected_draft_revision : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.publish_campaign(
            id="id",
            csrf_token="X-CSRF-Token",
            expected_draft_revision=1000000,
        )
        """
        _response = self._raw_client.publish_campaign(
            id, csrf_token=csrf_token, expected_draft_revision=expected_draft_revision, request_options=request_options
        )
        return _response.data

    def list_takeovers(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_takeovers()
        """
        _response = self._raw_client.list_takeovers(request_options=request_options)
        return _response.data

    def activate_a_takeover(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.activate_a_takeover()
        """
        _response = self._raw_client.activate_a_takeover(request_options=request_options)
        return _response.data

    def read_takeover_and_per_screen_state(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.read_takeover_and_per_screen_state(
            id="id",
        )
        """
        _response = self._raw_client.read_takeover_and_per_screen_state(id, request_options=request_options)
        return _response.data

    def cancel_an_active_takeover(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cancel_an_active_takeover(
            id="id",
        )
        """
        _response = self._raw_client.cancel_an_active_takeover(id, request_options=request_options)
        return _response.data

    def list_presentation_networks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkListResponse:
        """
        Owner and Administrator read. Responses include only redacted network metadata and credentialSet; encrypted credentials and plaintext secrets are never returned to Studio.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkListResponse
            Presentation Networks and supported authentication types

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_presentation_networks()
        """
        _response = self._raw_client.list_presentation_networks(request_options=request_options)
        return _response.data

    def create_presentation_network(
        self,
        *,
        csrf_token: str,
        name: str,
        ssid: str,
        hidden: bool,
        security: PresentationNetworkSecurity,
        secret: PresentationNetworkSecret,
        identity: typing.Optional[str] = OMIT,
        anonymous_identity: typing.Optional[str] = OMIT,
        ca_certificate_pem: typing.Optional[str] = OMIT,
        domain_suffix_match: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PresentationNetworkResponse:
        """
        Parameters
        ----------
        csrf_token : str

        name : str

        ssid : str

        hidden : bool

        security : PresentationNetworkSecurity

        secret : PresentationNetworkSecret

        identity : typing.Optional[str]

        anonymous_identity : typing.Optional[str]

        ca_certificate_pem : typing.Optional[str]

        domain_suffix_match : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkResponse
            Network created; the credential is accepted but not returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_presentation_network(
            csrf_token="X-CSRF-Token",
            name="name",
            ssid="ssid",
            hidden=True,
            security="wpa_psk",
            secret="secret",
        )
        """
        _response = self._raw_client.create_presentation_network(
            csrf_token=csrf_token,
            name=name,
            ssid=ssid,
            hidden=hidden,
            security=security,
            secret=secret,
            identity=identity,
            anonymous_identity=anonymous_identity,
            ca_certificate_pem=ca_certificate_pem,
            domain_suffix_match=domain_suffix_match,
            request_options=request_options,
        )
        return _response.data

    def get_presentation_network(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkDetailResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkDetailResponse
            Network metadata and assigned Linux screens

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_presentation_network(
            id="id",
        )
        """
        _response = self._raw_client.get_presentation_network(id, request_options=request_options)
        return _response.data

    def delete_presentation_network(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkResponse:
        """
        Assignments cascade and affected screens receive a durable configuration bump.

        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkResponse
            Deleted redacted network

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_presentation_network(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.delete_presentation_network(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def update_presentation_network(
        self,
        id: str,
        *,
        csrf_token: str,
        name: str,
        ssid: str,
        hidden: bool,
        security: PresentationNetworkSecurity,
        secret: typing.Optional[PresentationNetworkSecret] = OMIT,
        identity: typing.Optional[str] = OMIT,
        anonymous_identity: typing.Optional[str] = OMIT,
        ca_certificate_pem: typing.Optional[str] = OMIT,
        domain_suffix_match: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PresentationNetworkResponse:
        """
        The secret field is write-only. Omitting it retains the saved credential; providing a new value rotates it and increments configRevision. No response contains the secret or ciphertext.

        Parameters
        ----------
        id : str

        csrf_token : str

        name : str

        ssid : str

        hidden : bool

        security : PresentationNetworkSecurity

        secret : typing.Optional[PresentationNetworkSecret]

        identity : typing.Optional[str]

        anonymous_identity : typing.Optional[str]

        ca_certificate_pem : typing.Optional[str]

        domain_suffix_match : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkResponse
            Redacted network after the update

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_presentation_network(
            id="id",
            csrf_token="X-CSRF-Token",
            name="name",
            ssid="ssid",
            hidden=True,
            security="wpa_psk",
        )
        """
        _response = self._raw_client.update_presentation_network(
            id,
            csrf_token=csrf_token,
            name=name,
            ssid=ssid,
            hidden=hidden,
            security=security,
            secret=secret,
            identity=identity,
            anonymous_identity=anonymous_identity,
            ca_certificate_pem=ca_certificate_pem,
            domain_suffix_match=domain_suffix_match,
            request_options=request_options,
        )
        return _response.data

    def replace_presentation_network_assignments(
        self,
        id: str,
        *,
        csrf_token: str,
        screen_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PresentationNetworkAssignmentsResponse:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        screen_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkAssignmentsResponse
            Exact assignment set after replacement

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.replace_presentation_network_assignments(
            id="id",
            csrf_token="X-CSRF-Token",
            screen_ids=["screenIds"],
        )
        """
        _response = self._raw_client.replace_presentation_network_assignments(
            id, csrf_token=csrf_token, screen_ids=screen_ids, request_options=request_options
        )
        return _response.data

    def test_presentation_network(
        self, id: str, *, csrf_token: str, screen_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkTestResponse:
        """
        The selected assigned Linux player joins and leaves the network without starting AirPlay. The durable command contains only the network ID and timeout; credentials are fetched separately by the authenticated player.

        Parameters
        ----------
        id : str

        csrf_token : str

        screen_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkTestResponse
            Connection test command queued

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.test_presentation_network(
            id="id",
            csrf_token="X-CSRF-Token",
            screen_id="screenId",
        )
        """
        _response = self._raw_client.test_presentation_network(
            id, csrf_token=csrf_token, screen_id=screen_id, request_options=request_options
        )
        return _response.data

    def get_screen_presentation_network(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkReadinessResponse:
        """
        Readiness is server-derived from the assignment and the player's reported helper, NetworkManager, Wi-Fi, revision, and connection facts.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkReadinessResponse
            Assignment and operator-facing readiness state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_screen_presentation_network(
            id="id",
        )
        """
        _response = self._raw_client.get_screen_presentation_network(id, request_options=request_options)
        return _response.data

    def assign_screen_presentation_network(
        self,
        id: str,
        *,
        csrf_token: str,
        presentation_network_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PresentationNetworkAssignmentResponse:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        presentation_network_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkAssignmentResponse
            Assignment after replacement

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.assign_screen_presentation_network(
            id="id",
            csrf_token="X-CSRF-Token",
            presentation_network_id="presentationNetworkId",
        )
        """
        _response = self._raw_client.assign_screen_presentation_network(
            id, csrf_token=csrf_token, presentation_network_id=presentation_network_id, request_options=request_options
        )
        return _response.data

    def unassign_screen_presentation_network(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkAssignmentResponse:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkAssignmentResponse
            Screen assignment after removal

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.unassign_screen_presentation_network(
            id="id",
            csrf_token="X-CSRF-Token",
        )
        """
        _response = self._raw_client.unassign_screen_presentation_network(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    def get_player_presentation_network(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkProvisioningResponse:
        """
        Device-authenticated only. The server derives the assignment from the authenticated screen and accepts no network ID. The response is marked Cache-Control: no-store and contains the plaintext credential only for the player to build its temporary NetworkManager profile.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkProvisioningResponse
            Assigned network and credential; never log or persist this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_player_presentation_network()
        """
        _response = self._raw_client.get_player_presentation_network(request_options=request_options)
        return _response.data

    def list_presentation_overrides(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_presentation_overrides()
        """
        _response = self._raw_client.list_presentation_overrides(request_options=request_options)
        return _response.data

    def create_presentation_override(
        self,
        *,
        target_type: PresentationOverrideInputTargetType,
        target_id: str,
        content_type: PresentationOverrideInputContentType,
        content_id: str,
        duration_minutes: int,
        after_action: PresentationOverrideInputAfterAction,
        wake_display: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        target_type : PresentationOverrideInputTargetType

        target_id : str

        content_type : PresentationOverrideInputContentType

        content_id : str

        duration_minutes : int

        after_action : PresentationOverrideInputAfterAction

        wake_display : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_presentation_override(
            target_type="screen",
            target_id="targetId",
            content_type="playlist",
            content_id="contentId",
            duration_minutes=1,
            after_action="resume",
            wake_display=True,
        )
        """
        _response = self._raw_client.create_presentation_override(
            target_type=target_type,
            target_id=target_id,
            content_type=content_type,
            content_id=content_id,
            duration_minutes=duration_minutes,
            after_action=after_action,
            wake_display=wake_display,
            request_options=request_options,
        )
        return _response.data

    def stop_presentation_override(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.stop_presentation_override(
            id="id",
        )
        """
        _response = self._raw_client.stop_presentation_override(id, request_options=request_options)
        return _response.data

    def read_the_nws_monitor_rules_active_matches_and_poll_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.read_the_nws_monitor_rules_active_matches_and_poll_health()
        """
        _response = self._raw_client.read_the_nws_monitor_rules_active_matches_and_poll_health(
            request_options=request_options
        )
        return _response.data

    def list_official_nws_counties_and_forecast_zones_for_an_area(
        self, *, area: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        area : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_official_nws_counties_and_forecast_zones_for_an_area(
            area="area",
        )
        """
        _response = self._raw_client.list_official_nws_counties_and_forecast_zones_for_an_area(
            area=area, request_options=request_options
        )
        return _response.data

    def configure_nws_area_and_zone_monitoring(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.configure_nws_area_and_zone_monitoring()
        """
        _response = self._raw_client.configure_nws_area_and_zone_monitoring(request_options=request_options)
        return _response.data

    def retrieve_and_apply_active_nws_alerts_now(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.retrieve_and_apply_active_nws_alerts_now()
        """
        _response = self._raw_client.retrieve_and_apply_active_nws_alerts_now(request_options=request_options)
        return _response.data

    def create_an_automatic_nws_rule_answering_with_a_takeover_or_a_ticker_bar(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_an_automatic_nws_rule_answering_with_a_takeover_or_a_ticker_bar()
        """
        _response = self._raw_client.create_an_automatic_nws_rule_answering_with_a_takeover_or_a_ticker_bar(
            request_options=request_options
        )
        return _response.data

    def replace_an_automatic_nws_rule(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.replace_an_automatic_nws_rule(
            id="id",
        )
        """
        _response = self._raw_client.replace_an_automatic_nws_rule(id, request_options=request_options)
        return _response.data

    def delete_a_rule_ending_takeovers_it_raised_and_withdrawing_its_ticker(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_a_rule_ending_takeovers_it_raised_and_withdrawing_its_ticker(
            id="id",
        )
        """
        _response = self._raw_client.delete_a_rule_ending_takeovers_it_raised_and_withdrawing_its_ticker(
            id, request_options=request_options
        )
        return _response.data

    def list_recent_screen_commands(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_recent_screen_commands(
            id="id",
        )
        """
        _response = self._raw_client.list_recent_screen_commands(id, request_options=request_options)
        return _response.data

    def queue_a_typed_operational_display_control_or_bounded_player_recovery_command(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Display Control command types are display_power_on, display_power_off, display_set_input, display_set_volume, display_mute, display_unmute, display_set_brightness, and display_probe. They are capability-gated by the target Player.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.queue_a_typed_operational_display_control_or_bounded_player_recovery_command(
            id="id",
        )
        """
        _response = self._raw_client.queue_a_typed_operational_display_control_or_bounded_player_recovery_command(
            id, request_options=request_options
        )
        return _response.data

    def retrieve_executable_commands_for_the_authenticated_player(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.retrieve_executable_commands_for_the_authenticated_player()
        """
        _response = self._raw_client.retrieve_executable_commands_for_the_authenticated_player(
            request_options=request_options
        )
        return _response.data

    def acknowledge_a_player_command(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.acknowledge_a_player_command(
            id="id",
        )
        """
        _response = self._raw_client.acknowledge_a_player_command(id, request_options=request_options)
        return _response.data

    def report_a_safe_command_result(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.report_a_safe_command_result(
            id="id",
        )
        """
        _response = self._raw_client.report_a_safe_command_result(id, request_options=request_options)
        return _response.data

    def read_typed_organization_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.read_typed_organization_settings()
        """
        _response = self._raw_client.read_typed_organization_settings(request_options=request_options)
        return _response.data

    def update_settings_with_optimistic_revision(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_settings_with_optimistic_revision()
        """
        _response = self._raw_client.update_settings_with_optimistic_revision(request_options=request_options)
        return _response.data

    def read_current_user_preferences(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.read_current_user_preferences()
        """
        _response = self._raw_client.read_current_user_preferences(request_options=request_options)
        return _response.data

    def update_current_user_preferences(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.update_current_user_preferences()
        """
        _response = self._raw_client.update_current_user_preferences(request_options=request_options)
        return _response.data

    def read_group_player_policy(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.read_group_player_policy(
            id="id",
        )
        """
        _response = self._raw_client.read_group_player_policy(id, request_options=request_options)
        return _response.data

    def replace_typed_group_policy(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.replace_typed_group_policy(
            id="id",
        )
        """
        _response = self._raw_client.replace_typed_group_policy(id, request_options=request_options)
        return _response.data

    def reset_group_policy(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.reset_group_policy(
            id="id",
        )
        """
        _response = self._raw_client.reset_group_policy(id, request_options=request_options)
        return _response.data

    def read_screen_player_policy(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.read_screen_player_policy(
            id="id",
        )
        """
        _response = self._raw_client.read_screen_player_policy(id, request_options=request_options)
        return _response.data

    def replace_typed_screen_policy(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.replace_typed_screen_policy(
            id="id",
        )
        """
        _response = self._raw_client.replace_typed_screen_policy(id, request_options=request_options)
        return _response.data

    def reset_screen_policy(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.reset_screen_policy(
            id="id",
        )
        """
        _response = self._raw_client.reset_screen_policy(id, request_options=request_options)
        return _response.data

    def inspect_effective_values_and_inheritance_sources(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inspect_effective_values_and_inheritance_sources(
            id="id",
        )
        """
        _response = self._raw_client.inspect_effective_values_and_inheritance_sources(
            id, request_options=request_options
        )
        return _response.data

    def read_commissioning_zero_touch_readiness_android_reliability_and_power_assist_state(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.read_commissioning_zero_touch_readiness_android_reliability_and_power_assist_state(
            id="id",
        )
        """
        _response = self._raw_client.read_commissioning_zero_touch_readiness_android_reliability_and_power_assist_state(
            id, request_options=request_options
        )
        return _response.data

    def store_administrator_confirmed_sleep_wake_cec_input_and_startup_test_results(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.store_administrator_confirmed_sleep_wake_cec_input_and_startup_test_results(
            id="id",
        )
        """
        _response = self._raw_client.store_administrator_confirmed_sleep_wake_cec_input_and_startup_test_results(
            id, request_options=request_options
        )
        return _response.data

    def retrieve_effective_player_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.retrieve_effective_player_configuration()
        """
        _response = self._raw_client.retrieve_effective_player_configuration(request_options=request_options)
        return _response.data

    def safe_system_diagnostics(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.safe_system_diagnostics()
        """
        _response = self._raw_client.safe_system_diagnostics(request_options=request_options)
        return _response.data

    def run_a_fixed_safe_maintenance_action(
        self, action: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        action : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.run_a_fixed_safe_maintenance_action(
            action="action",
        )
        """
        _response = self._raw_client.run_a_fixed_safe_maintenance_action(action, request_options=request_options)
        return _response.data

    def export_non_secret_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.export_non_secret_settings()
        """
        _response = self._raw_client.export_non_secret_settings(request_options=request_options)
        return _response.data

    def validate_settings_import_without_applying(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.validate_settings_import_without_applying()
        """
        _response = self._raw_client.validate_settings_import_without_applying(request_options=request_options)
        return _response.data

    def apply_confirmed_settings_import(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.apply_confirmed_settings_import()
        """
        _response = self._raw_client.apply_confirmed_settings_import(request_options=request_options)
        return _response.data

    def list_fixed_repository_tilecast_player_releases_and_verification_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_fixed_repository_tilecast_player_releases_and_verification_state()
        """
        _response = self._raw_client.list_fixed_repository_tilecast_player_releases_and_verification_state(
            request_options=request_options
        )
        return _response.data

    def check_gibsonmb71tilecast_git_hub_releases(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.check_gibsonmb71tilecast_git_hub_releases()
        """
        _response = self._raw_client.check_gibsonmb71tilecast_git_hub_releases(request_options=request_options)
        return _response.data

    def start_owner_authorized_git_hub_o_auth_device_flow(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.start_owner_authorized_git_hub_o_auth_device_flow()
        """
        _response = self._raw_client.start_owner_authorized_git_hub_o_auth_device_flow(request_options=request_options)
        return _response.data

    def poll_an_active_git_hub_o_auth_device_flow(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.poll_an_active_git_hub_o_auth_device_flow()
        """
        _response = self._raw_client.poll_an_active_git_hub_o_auth_device_flow(request_options=request_options)
        return _response.data

    def remove_a_device_authorized_git_hub_credential_from_tilecast_server(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.remove_a_device_authorized_git_hub_credential_from_tilecast_server()
        """
        _response = self._raw_client.remove_a_device_authorized_git_hub_credential_from_tilecast_server(
            request_options=request_options
        )
        return _response.data

    def upload_and_verify_a_signed_tilecast_player_release_bundle(
        self, *, files: typing.List[core.File], request_options: typing.Optional[RequestOptions] = None
    ) -> PostApiV1PlayerReleasesUploadResponse:
        """
        Accepts one release's three files as multipart files: the artifact, the signed update manifest and its signature. The file names select the family: `tilecast-player.apk` with `tilecast-player-update.json` (Android), `tilecast-player.AppImage` with `tilecast-player-update-linux.json` (Electron Linux), or `tilecast-edge-<version>-<arch>.tar.zst` with the signed envelope `tilecast-edge-update.json` (Tilecast Edge). Owner session plus CSRF or a configured release-publishing bearer token is required.

        Parameters
        ----------
        files : typing.List[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiV1PlayerReleasesUploadResponse
            Release fully verified and cached

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.upload_and_verify_a_signed_tilecast_player_release_bundle()
        """
        _response = self._raw_client.upload_and_verify_a_signed_tilecast_player_release_bundle(
            files=files, request_options=request_options
        )
        return _response.data

    def download_and_verify_a_signed_player_apk_into_private_cache(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.download_and_verify_a_signed_player_apk_into_private_cache(
            id="id",
        )
        """
        _response = self._raw_client.download_and_verify_a_signed_player_apk_into_private_cache(
            id, request_options=request_options
        )
        return _response.data

    def list_player_update_deployments_narrowed_to_the_callers_screen_scope(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.list_player_update_deployments_narrowed_to_the_callers_screen_scope()
        """
        _response = self._raw_client.list_player_update_deployments_narrowed_to_the_callers_screen_scope(
            request_options=request_options
        )
        return _response.data

    def create_a_deduplicated_screen_and_group_deployment_with_an_optional_canary_cohort(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_a_deduplicated_screen_and_group_deployment_with_an_optional_canary_cohort()
        """
        _response = self._raw_client.create_a_deduplicated_screen_and_group_deployment_with_an_optional_canary_cohort(
            request_options=request_options
        )
        return _response.data

    def read_the_deployment_header_release_artifact_size_and_per_screen_update_state_for_the_screens_in_the_callers_scope(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.read_the_deployment_header_release_artifact_size_and_per_screen_update_state_for_the_screens_in_the_callers_scope(
            id="id",
        )
        """
        _response = self._raw_client.read_the_deployment_header_release_artifact_size_and_per_screen_update_state_for_the_screens_in_the_callers_scope(
            id, request_options=request_options
        )
        return _response.data

    def cancel_pending_update_work_on_every_screen_the_deployment_reaches(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.cancel_pending_update_work_on_every_screen_the_deployment_reaches(
            id="id",
        )
        """
        _response = self._raw_client.cancel_pending_update_work_on_every_screen_the_deployment_reaches(
            id, request_options=request_options
        )
        return _response.data

    def retry_a_failed_screen_update_idempotently(
        self, id: str, screen_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        screen_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.retry_a_failed_screen_update_idempotently(
            id="id",
            screen_id="screenId",
        )
        """
        _response = self._raw_client.retry_a_failed_screen_update_idempotently(
            id, screen_id, request_options=request_options
        )
        return _response.data

    def get_targeted_verified_player_update_metadata(
        self, release_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiV1PlayerUpdatesReleaseIdResponse:
        """
        Parameters
        ----------
        release_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV1PlayerUpdatesReleaseIdResponse
            Update metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_targeted_verified_player_update_metadata(
            release_id="releaseId",
        )
        """
        _response = self._raw_client.get_targeted_verified_player_update_metadata(
            release_id, request_options=request_options
        )
        return _response.data

    def download_or_resume_the_authenticated_cached_release_artifact(
        self, release_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        The artifact of every family (the AppImage, the APK or the Tilecast Edge archive), with `Accept-Ranges: bytes`, a strong `ETag` of its SHA-256, and range requests. Only a screen targeted by an active deployment of the release may read it.

        Parameters
        ----------
        release_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.download_or_resume_the_authenticated_cached_release_artifact(
            release_id="releaseId",
        )
        """
        _response = self._raw_client.download_or_resume_the_authenticated_cached_release_artifact(
            release_id, request_options=request_options
        )
        return _response.data

    def download_or_resume_authenticated_cached_apk(
        self, release_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        release_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.download_or_resume_authenticated_cached_apk(
            release_id="releaseId",
        )
        """
        _response = self._raw_client.download_or_resume_authenticated_cached_apk(
            release_id, request_options=request_options
        )
        return _response.data

    def inspect_authenticated_apk_range_metadata(
        self, release_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        release_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.inspect_authenticated_apk_range_metadata(
            release_id="releaseId",
        )
        """
        _response = self._raw_client.inspect_authenticated_apk_range_metadata(
            release_id, request_options=request_options
        )
        return _response.headers

    def report_bounded_player_update_preparation_and_installer_status(
        self,
        deployment_id: str,
        *,
        state: PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState,
        downloaded_bytes: typing.Optional[int] = OMIT,
        permission_status: typing.Optional[str] = OMIT,
        installer_status: typing.Optional[str] = OMIT,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        deployment_id : str

        state : PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState
            `succeeded` is accepted only for a Tilecast Edge release: it is the screen's explicit confirmation that the provisional release passed its health checks, and the only way an Edge target settles. Other families settle from the heartbeat.

        downloaded_bytes : typing.Optional[int]

        permission_status : typing.Optional[str]

        installer_status : typing.Optional[str]
            Tilecast Edge sends `provisional` with `reconnecting`, `confirmed` with `succeeded`, and `rolled_back` with a `failed` report of a release that was activated and then rolled back.

        error : typing.Optional[str]
            A bounded reason code, never free text from a server response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.report_bounded_player_update_preparation_and_installer_status(
            deployment_id="deploymentId",
            state="downloading",
        )
        """
        _response = self._raw_client.report_bounded_player_update_preparation_and_installer_status(
            deployment_id,
            state=state,
            downloaded_bytes=downloaded_bytes,
            permission_status=permission_status,
            installer_status=installer_status,
            error=error,
            request_options=request_options,
        )
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
    base_url : str
        The base url to use for requests from the client.

    token : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    async_token : typing.Optional[typing.Callable[[], typing.Awaitable[str]]]
        An async callable that returns a bearer token. Use this when token acquisition involves async I/O (e.g., refreshing tokens via an async HTTP client). When provided, this is used instead of the synchronous token for async requests.

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
        token="YOUR_TOKEN",
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        token: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        async_token: typing.Optional[typing.Callable[[], typing.Awaitable[str]]] = None,
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
            base_url=base_url,
            token=token,
            headers=headers,
            async_token=async_token,
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

    async def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.health()


        asyncio.run(main())
        """
        _response = await self._raw_client.health(request_options=request_options)
        return _response.data

    async def install_linux_player_script(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Public, rate-limited Linux Player provisioning script with this server's URL embedded.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.install_linux_player_script()


        asyncio.run(main())
        """
        _response = await self._raw_client.install_linux_player_script(request_options=request_options)
        return _response.data

    async def install_air_play_script(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Public, rate-limited AirPlay provisioning script with this server's URL embedded.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.install_air_play_script()


        asyncio.run(main())
        """
        _response = await self._raw_client.install_air_play_script(request_options=request_options)
        return _response.data

    async def install_linux_player_service(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.install_linux_player_service()


        asyncio.run(main())
        """
        _response = await self._raw_client.install_linux_player_service(request_options=request_options)
        return _response.data

    async def ready(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ready()


        asyncio.run(main())
        """
        _response = await self._raw_client.ready(request_options=request_options)
        return _response.data

    async def installable_linux_player_release(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.installable_linux_player_release()


        asyncio.run(main())
        """
        _response = await self._raw_client.installable_linux_player_release(request_options=request_options)
        return _response.data

    async def installable_linux_player_artifact(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.installable_linux_player_artifact()


        asyncio.run(main())
        """
        _response = await self._raw_client.installable_linux_player_artifact(request_options=request_options)
        return _response.data

    async def head_installable_linux_player_artifact(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.head_installable_linux_player_artifact()


        asyncio.run(main())
        """
        _response = await self._raw_client.head_installable_linux_player_artifact(request_options=request_options)
        return _response.headers

    async def installable_ux_play_artifact(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Public, rate-limited, pinned UxPlay 1.73.6 source archive embedded in Tilecast Server.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.installable_ux_play_artifact()


        asyncio.run(main())
        """
        _response = await self._raw_client.installable_ux_play_artifact(request_options=request_options)
        return _response.data

    async def head_installable_ux_play_artifact(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.head_installable_ux_play_artifact()


        asyncio.run(main())
        """
        _response = await self._raw_client.head_installable_ux_play_artifact(request_options=request_options)
        return _response.headers

    async def installable_ux_play_checksum(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.installable_ux_play_checksum()


        asyncio.run(main())
        """
        _response = await self._raw_client.installable_ux_play_checksum(request_options=request_options)
        return _response.data

    async def auth_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.auth_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.auth_status(request_options=request_options)
        return _response.data

    async def demo_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Registered only when TILECAST_ENV is demo. Returns the seeded scenario and the state of each simulated player.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.demo_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.demo_state(request_options=request_options)
        return _response.data

    async def reset_demo(
        self,
        *,
        scenario: typing.Optional[ResetDemoRequestScenario] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Registered only when TILECAST_ENV is demo. Replaces all data with a scenario and returns once its simulated players have connected. Requires the Owner role and X-CSRF-Token.

        Parameters
        ----------
        scenario : typing.Optional[ResetDemoRequestScenario]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.reset_demo()


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_demo(scenario=scenario, request_options=request_options)
        return _response.data

    async def initial_setup(
        self,
        *,
        organization_name: str,
        owner_name: str,
        username: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        organization_name : str

        owner_name : str

        username : str

        password : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.initial_setup(
                organization_name="organizationName",
                owner_name="ownerName",
                username="username",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.initial_setup(
            organization_name=organization_name,
            owner_name=owner_name,
            username=username,
            password=password,
            request_options=request_options,
        )
        return _response.data

    async def login(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.login()


        asyncio.run(main())
        """
        _response = await self._raw_client.login(request_options=request_options)
        return _response.data

    async def verify_multi_factor(
        self, *, challenge_token: str, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Completes a pending sign-in with an authenticator or recovery code.

        Parameters
        ----------
        challenge_token : str

        code : str
            An authenticator code or a recovery code. The server decides which by shape; six digits are never matched against recovery codes.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.verify_multi_factor(
                challenge_token="challengeToken",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_multi_factor(
            challenge_token=challenge_token, code=code, request_options=request_options
        )
        return _response.data

    async def multi_factor_passkey_options(
        self, *, challenge_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Exchanges a pending challenge for a WebAuthn assertion request.

        Parameters
        ----------
        challenge_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.multi_factor_passkey_options(
                challenge_token="challengeToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.multi_factor_passkey_options(
            challenge_token=challenge_token, request_options=request_options
        )
        return _response.data

    async def passkey_login_options(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Starts a discoverable, username-free WebAuthn ceremony.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.passkey_login_options()


        asyncio.run(main())
        """
        _response = await self._raw_client.passkey_login_options(request_options=request_options)
        return _response.data

    async def passkey_login(
        self,
        *,
        mfa_challenge: str,
        id: str,
        raw_id: str,
        type: WebAuthnAssertionType,
        response: WebAuthnAssertionResponse,
        authenticator_attachment: typing.Optional[WebAuthnAssertionAuthenticatorAttachment] = OMIT,
        client_extension_results: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Posts the raw WebAuthn assertion. A verified passkey satisfies multi-factor authentication on its own.

        Parameters
        ----------
        mfa_challenge : str

        id : str

        raw_id : str
            base64url

        type : WebAuthnAssertionType

        response : WebAuthnAssertionResponse

        authenticator_attachment : typing.Optional[WebAuthnAssertionAuthenticatorAttachment]

        client_extension_results : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WebAuthnAssertionResponse

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.passkey_login(
                mfa_challenge="X-MFA-Challenge",
                id="id",
                raw_id="rawId",
                type="public-key",
                response=WebAuthnAssertionResponse(
                    client_data_json="clientDataJSON",
                    authenticator_data="authenticatorData",
                    signature="signature",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.passkey_login(
            mfa_challenge=mfa_challenge,
            id=id,
            raw_id=raw_id,
            type=type,
            response=response,
            authenticator_attachment=authenticator_attachment,
            client_extension_results=client_extension_results,
            request_options=request_options,
        )
        return _response.data

    async def security_status(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.security_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.security_status(request_options=request_options)
        return _response.data

    async def begin_authenticator_enrollment(
        self, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.begin_authenticator_enrollment(
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.begin_authenticator_enrollment(
            csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def confirm_authenticator_enrollment(
        self, *, csrf_token: str, code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        code : str
            The six-digit authenticator code.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.confirm_authenticator_enrollment(
                csrf_token="X-CSRF-Token",
                code="code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.confirm_authenticator_enrollment(
            csrf_token=csrf_token, code=code, request_options=request_options
        )
        return _response.data

    async def remove_authenticator(
        self, *, csrf_token: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Requires the account password in the body.

        Parameters
        ----------
        csrf_token : str

        password : str
            The account password, reverified so a borrowed session cannot weaken sign-in security on its own.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.remove_authenticator(
                csrf_token="X-CSRF-Token",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_authenticator(
            csrf_token=csrf_token, password=password, request_options=request_options
        )
        return _response.data

    async def generate_recovery_codes(
        self, *, csrf_token: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Replaces every unused code. Requires the account password. The plain codes are returned exactly once.

        Parameters
        ----------
        csrf_token : str

        password : str
            The account password, reverified so a borrowed session cannot weaken sign-in security on its own.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.generate_recovery_codes(
                csrf_token="X-CSRF-Token",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_recovery_codes(
            csrf_token=csrf_token, password=password, request_options=request_options
        )
        return _response.data

    async def passkey_registration_options(
        self, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.passkey_registration_options(
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.passkey_registration_options(
            csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def register_passkey(
        self,
        *,
        csrf_token: str,
        mfa_challenge: str,
        id: str,
        raw_id: str,
        type: WebAuthnCredentialType,
        response: WebAuthnCredentialResponse,
        authenticator_attachment: typing.Optional[WebAuthnCredentialAuthenticatorAttachment] = OMIT,
        client_extension_results: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        The passkey is named from the authenticator's AAGUID; no name is accepted here. Use the rename endpoint to change it.

        Parameters
        ----------
        csrf_token : str

        mfa_challenge : str

        id : str

        raw_id : str
            base64url

        type : WebAuthnCredentialType

        response : WebAuthnCredentialResponse

        authenticator_attachment : typing.Optional[WebAuthnCredentialAuthenticatorAttachment]

        client_extension_results : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WebAuthnCredentialResponse

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.register_passkey(
                csrf_token="X-CSRF-Token",
                mfa_challenge="X-MFA-Challenge",
                id="id",
                raw_id="rawId",
                type="public-key",
                response=WebAuthnCredentialResponse(
                    client_data_json="clientDataJSON",
                    attestation_object="attestationObject",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_passkey(
            csrf_token=csrf_token,
            mfa_challenge=mfa_challenge,
            id=id,
            raw_id=raw_id,
            type=type,
            response=response,
            authenticator_attachment=authenticator_attachment,
            client_extension_results=client_extension_results,
            request_options=request_options,
        )
        return _response.data

    async def rename_passkey(
        self, id: str, *, csrf_token: str, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        name : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rename_passkey(
                id="id",
                csrf_token="X-CSRF-Token",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rename_passkey(
            id, csrf_token=csrf_token, name=name, request_options=request_options
        )
        return _response.data

    async def remove_passkey(
        self, id: str, *, csrf_token: str, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Requires the account password in the body.

        Parameters
        ----------
        id : str

        csrf_token : str

        password : str
            The account password, reverified so a borrowed session cannot weaken sign-in security on its own.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.remove_passkey(
                id="id",
                csrf_token="X-CSRF-Token",
                password="password",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_passkey(
            id, csrf_token=csrf_token, password=password, request_options=request_options
        )
        return _response.data

    async def reset_user_security(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Owner/Administrator recovery path. Clears every factor, revokes the account's sessions, and records an audit entry.

        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.reset_user_security(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_user_security(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def permanently_delete_user(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Permanently removes an inactive user account. Account-owned preferences, sessions, grants, and security credentials are removed; retained records keep their history with user attribution cleared.

        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.permanently_delete_user(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.permanently_delete_user(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def logout(self, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.logout(
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.logout(csrf_token=csrf_token, request_options=request_options)
        return _response.data

    async def installation_identity(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.installation_identity()


        asyncio.run(main())
        """
        _response = await self._raw_client.installation_identity(request_options=request_options)
        return _response.data

    async def list_content_folders(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_content_folders()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_content_folders(request_options=request_options)
        return _response.data

    async def create_content_folder(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_content_folder()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_content_folder(request_options=request_options)
        return _response.data

    async def list_content_collections(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_content_collections()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_content_collections(request_options=request_options)
        return _response.data

    async def create_content_collection(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_content_collection()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_content_collection(request_options=request_options)
        return _response.data

    async def list_content_tags(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_content_tags()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_content_tags(request_options=request_options)
        return _response.data

    async def create_content_tag(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_content_tag()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_content_tag(request_options=request_options)
        return _response.data

    async def bulk_organize_assets(
        self,
        *,
        asset_ids: typing.Sequence[str],
        set_folder: typing.Optional[bool] = OMIT,
        folder_id: typing.Optional[str] = OMIT,
        add_tag_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        remove_tag_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        add_collection_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        remove_collection_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        asset_ids : typing.Sequence[str]

        set_folder : typing.Optional[bool]

        folder_id : typing.Optional[str]

        add_tag_ids : typing.Optional[typing.Sequence[str]]

        remove_tag_ids : typing.Optional[typing.Sequence[str]]

        add_collection_ids : typing.Optional[typing.Sequence[str]]

        remove_collection_ids : typing.Optional[typing.Sequence[str]]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.bulk_organize_assets(
                asset_ids=["assetIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_organize_assets(
            asset_ids=asset_ids,
            set_folder=set_folder,
            folder_id=folder_id,
            add_tag_ids=add_tag_ids,
            remove_tag_ids=remove_tag_ids,
            add_collection_ids=add_collection_ids,
            remove_collection_ids=remove_collection_ids,
            request_options=request_options,
        )
        return _response.data

    async def create_pairing_session(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_pairing_session()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_pairing_session(request_options=request_options)
        return _response.data

    async def poll_pairing_session(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.poll_pairing_session(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.poll_pairing_session(id, request_options=request_options)
        return _response.data

    async def enroll_player(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.enroll_player()


        asyncio.run(main())
        """
        _response = await self._raw_client.enroll_player(request_options=request_options)
        return _response.data

    async def player_heartbeat(
        self,
        *,
        player_family: typing.Optional[str] = OMIT,
        player_architecture: typing.Optional[str] = OMIT,
        noise_meter: typing.Optional[PlayerHeartbeatNoiseMeter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Accepts the authenticated Player heartbeat. Optional Linux Display Control fields report detected providers, independent capabilities, display power observations, and policy state. They do not determine Player online status; command acknowledgement and display state confirmation remain separate.

        The optional `noiseMeter` object carries the Noise Meter plugin's live state and its completed ten-second history buckets. It is derived numbers only — no audio, waveform, or sample is exchanged in either direction. The screen is taken from the authenticated device credential, never from the body, and a batch is bounded to 120 records. Storage is idempotent on screen plus bucket start, so a retried heartbeat cannot duplicate history.

        Parameters
        ----------
        player_family : typing.Optional[str]
            `android`, `electron-linux` or `edge`. The server keeps only these values; another value is recorded as absent.

        player_architecture : typing.Optional[str]
            `x86_64` or `aarch64`, kept only with `playerFamily: edge`. An Edge screen without a known architecture is `incompatible` for Edge deployments.

        noise_meter : typing.Optional[PlayerHeartbeatNoiseMeter]
            Noise Meter plugin state. Contains no audio, waveform, or sample, and levels are the relative 0-100 Tilecast scale rather than dB, dBA, or SPL.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.player_heartbeat()


        asyncio.run(main())
        """
        _response = await self._raw_client.player_heartbeat(
            player_family=player_family,
            player_architecture=player_architecture,
            noise_meter=noise_meter,
            request_options=request_options,
        )
        return _response.data

    async def player_liveness(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Records authenticated Player contact for background liveness. This endpoint intentionally accepts no playback snapshot and cannot change the current manifest, content, version, cache policy, or playback state.

        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.player_liveness(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.player_liveness(request=request, request_options=request_options)
        return _response.data

    async def player_socket(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.player_socket()


        asyncio.run(main())
        """
        _response = await self._raw_client.player_socket(request_options=request_options)
        return _response.data

    async def list_screens(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_screens()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_screens(request_options=request_options)
        return _response.data

    async def get_screen(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_screen(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_screen(id, request_options=request_options)
        return _response.data

    async def update_screen(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_screen(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_screen(id, request_options=request_options)
        return _response.data

    async def list_screen_player_history(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_screen_player_history(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_screen_player_history(id, request_options=request_options)
        return _response.data

    async def resolve_pairing_code(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.resolve_pairing_code()


        asyncio.run(main())
        """
        _response = await self._raw_client.resolve_pairing_code(request_options=request_options)
        return _response.data

    async def approve_pairing(
        self,
        id: str,
        *,
        name: str,
        room_name: str,
        room_number: str,
        description: str,
        location_id: typing.Optional[str] = OMIT,
        replace_existing_credential: typing.Optional[bool] = OMIT,
        replace_hardware: typing.Optional[bool] = OMIT,
        replacement_screen_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        name : str

        room_name : str

        room_number : str

        description : str

        location_id : typing.Optional[str]

        replace_existing_credential : typing.Optional[bool]
            Explicitly authorizes credential rotation after successful enrollment.

        replace_hardware : typing.Optional[bool]
            Assigns the new player to an existing logical screen without changing its content or policy relationships.

        replacement_screen_id : typing.Optional[str]
            Required when replaceHardware is true.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.approve_pairing(
                id="id",
                name="name",
                room_name="roomName",
                room_number="roomNumber",
                description="description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.approve_pairing(
            id,
            name=name,
            room_name=room_name,
            room_number=room_number,
            description=description,
            location_id=location_id,
            replace_existing_credential=replace_existing_credential,
            replace_hardware=replace_hardware,
            replacement_screen_id=replacement_screen_id,
            request_options=request_options,
        )
        return _response.data

    async def list_locations(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_locations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_locations(request_options=request_options)
        return _response.data

    async def create_location(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_location()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_location(request_options=request_options)
        return _response.data

    async def delete_location(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_location(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_location(id, request_options=request_options)
        return _response.data

    async def update_location(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_location(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_location(id, request_options=request_options)
        return _response.data

    async def list_plugins(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListPluginsResponse:
        """
        Every plugin the running release offers, joined with this installation's state. Readable by any signed-in account.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPluginsResponse
            Plugin catalog

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_plugins()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_plugins(request_options=request_options)
        return _response.data

    async def install_plugin(
        self, plugin_id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InstallPluginResponse:
        """
        Records a release-owned plugin as installed. Idempotent. Never downloads or runs code.

        Parameters
        ----------
        plugin_id : str
            Registry identifier such as noise_meter.

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InstallPluginResponse
            Plugin installed by this request

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.install_plugin(
                plugin_id="pluginId",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.install_plugin(
            plugin_id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def remove_plugin(
        self, plugin_id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the installation record. Never deletes plugin data; refuses while plugin-owned resources remain. Idempotent for a plugin that is not installed. An installation row for a plugin this release does not know may also be removed; only the row is deleted.

        Parameters
        ----------
        plugin_id : str
            Registry identifier such as noise_meter.

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.remove_plugin(
                plugin_id="pluginId",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_plugin(
            plugin_id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def get_dependency_graph(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDependencyGraphResponse:
        """
        Returns the current content and delivery topology. Directed edges run from a dependency to the record that consumes it. Dependency Graph is a Studio system tool, not an installable plugin.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDependencyGraphResponse
            Typed dependency nodes and directed consumer edges

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_dependency_graph()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dependency_graph(request_options=request_options)
        return _response.data

    async def list_countdown_bar_instances(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_countdown_bar_instances()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_countdown_bar_instances(request_options=request_options)
        return _response.data

    async def create_countdown_bar_instance(
        self,
        *,
        csrf_token: str,
        name: str,
        message: str,
        schedule_type: CountdownBarInputScheduleType,
        days_of_week: typing.Sequence[int],
        timezone: str,
        lead_time_seconds: int,
        completion_text: str,
        show_confetti: bool,
        display_mode: CountdownBarInputDisplayMode,
        height_px: int,
        urgency_enabled: bool,
        starting_soon_seconds: int,
        urgent_seconds: int,
        pulse_seconds: int,
        enabled: bool,
        priority: int,
        target_scope: CountdownBarInputTargetScope,
        target_ids: typing.Sequence[str],
        target_time: typing.Optional[str] = OMIT,
        one_time_at: typing.Optional[dt.datetime] = OMIT,
        progress_fill: typing.Optional[CountdownBarInputProgressFill] = OMIT,
        content_padding: typing.Optional[int] = OMIT,
        text_scale: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        name : str

        message : str

        schedule_type : CountdownBarInputScheduleType

        days_of_week : typing.Sequence[int]

        timezone : str

        lead_time_seconds : int

        completion_text : str

        show_confetti : bool
            Show a short confetti fall from the top of the Player when the countdown reaches zero. This does not require completion text.

        display_mode : CountdownBarInputDisplayMode

        height_px : int

        urgency_enabled : bool
            Enable automatic starting-soon, urgent, and final pulse stages.

        starting_soon_seconds : int

        urgent_seconds : int

        pulse_seconds : int
            Final seconds during which the urgent bar pulses and grows by 25 percent.

        enabled : bool

        priority : int

        target_scope : CountdownBarInputTargetScope

        target_ids : typing.Sequence[str]

        target_time : typing.Optional[str]

        one_time_at : typing.Optional[dt.datetime]

        progress_fill : typing.Optional[CountdownBarInputProgressFill]
            Background treatment behind the bar text. "drain" starts the bar fully tinted when the lead window opens and retreats the tint leftward as the target approaches, leaving only the bar background at zero. Omitted means "none".

        content_padding : typing.Optional[int]
            Share of each side left as a gutter, as a percentage of the bar width. Lowering it gives a long message or a larger type size more room. The default 4 matches the bar's original gutters.

        text_scale : typing.Optional[int]
            Percentage applied to the height-derived type size, so a bar can carry larger text without changing its height. 100 is the original appearance.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_countdown_bar_instance(
                csrf_token="X-CSRF-Token",
                name="name",
                message="message",
                schedule_type="weekly",
                days_of_week=[1],
                timezone="timezone",
                lead_time_seconds=1,
                completion_text="completionText",
                show_confetti=True,
                display_mode="overlay",
                height_px=1,
                urgency_enabled=True,
                starting_soon_seconds=1,
                urgent_seconds=1,
                pulse_seconds=1,
                enabled=True,
                priority=1,
                target_scope="all",
                target_ids=["targetIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_countdown_bar_instance(
            csrf_token=csrf_token,
            name=name,
            message=message,
            schedule_type=schedule_type,
            days_of_week=days_of_week,
            timezone=timezone,
            lead_time_seconds=lead_time_seconds,
            completion_text=completion_text,
            show_confetti=show_confetti,
            display_mode=display_mode,
            height_px=height_px,
            urgency_enabled=urgency_enabled,
            starting_soon_seconds=starting_soon_seconds,
            urgent_seconds=urgent_seconds,
            pulse_seconds=pulse_seconds,
            enabled=enabled,
            priority=priority,
            target_scope=target_scope,
            target_ids=target_ids,
            target_time=target_time,
            one_time_at=one_time_at,
            progress_fill=progress_fill,
            content_padding=content_padding,
            text_scale=text_scale,
            request_options=request_options,
        )
        return _response.data

    async def get_countdown_bar_instance(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_countdown_bar_instance(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_countdown_bar_instance(id, request_options=request_options)
        return _response.data

    async def update_countdown_bar_instance(
        self,
        id: str,
        *,
        csrf_token: str,
        name: str,
        message: str,
        schedule_type: CountdownBarInputScheduleType,
        days_of_week: typing.Sequence[int],
        timezone: str,
        lead_time_seconds: int,
        completion_text: str,
        show_confetti: bool,
        display_mode: CountdownBarInputDisplayMode,
        height_px: int,
        urgency_enabled: bool,
        starting_soon_seconds: int,
        urgent_seconds: int,
        pulse_seconds: int,
        enabled: bool,
        priority: int,
        target_scope: CountdownBarInputTargetScope,
        target_ids: typing.Sequence[str],
        target_time: typing.Optional[str] = OMIT,
        one_time_at: typing.Optional[dt.datetime] = OMIT,
        progress_fill: typing.Optional[CountdownBarInputProgressFill] = OMIT,
        content_padding: typing.Optional[int] = OMIT,
        text_scale: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        name : str

        message : str

        schedule_type : CountdownBarInputScheduleType

        days_of_week : typing.Sequence[int]

        timezone : str

        lead_time_seconds : int

        completion_text : str

        show_confetti : bool
            Show a short confetti fall from the top of the Player when the countdown reaches zero. This does not require completion text.

        display_mode : CountdownBarInputDisplayMode

        height_px : int

        urgency_enabled : bool
            Enable automatic starting-soon, urgent, and final pulse stages.

        starting_soon_seconds : int

        urgent_seconds : int

        pulse_seconds : int
            Final seconds during which the urgent bar pulses and grows by 25 percent.

        enabled : bool

        priority : int

        target_scope : CountdownBarInputTargetScope

        target_ids : typing.Sequence[str]

        target_time : typing.Optional[str]

        one_time_at : typing.Optional[dt.datetime]

        progress_fill : typing.Optional[CountdownBarInputProgressFill]
            Background treatment behind the bar text. "drain" starts the bar fully tinted when the lead window opens and retreats the tint leftward as the target approaches, leaving only the bar background at zero. Omitted means "none".

        content_padding : typing.Optional[int]
            Share of each side left as a gutter, as a percentage of the bar width. Lowering it gives a long message or a larger type size more room. The default 4 matches the bar's original gutters.

        text_scale : typing.Optional[int]
            Percentage applied to the height-derived type size, so a bar can carry larger text without changing its height. 100 is the original appearance.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_countdown_bar_instance(
                id="id",
                csrf_token="X-CSRF-Token",
                name="name",
                message="message",
                schedule_type="weekly",
                days_of_week=[1],
                timezone="timezone",
                lead_time_seconds=1,
                completion_text="completionText",
                show_confetti=True,
                display_mode="overlay",
                height_px=1,
                urgency_enabled=True,
                starting_soon_seconds=1,
                urgent_seconds=1,
                pulse_seconds=1,
                enabled=True,
                priority=1,
                target_scope="all",
                target_ids=["targetIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_countdown_bar_instance(
            id,
            csrf_token=csrf_token,
            name=name,
            message=message,
            schedule_type=schedule_type,
            days_of_week=days_of_week,
            timezone=timezone,
            lead_time_seconds=lead_time_seconds,
            completion_text=completion_text,
            show_confetti=show_confetti,
            display_mode=display_mode,
            height_px=height_px,
            urgency_enabled=urgency_enabled,
            starting_soon_seconds=starting_soon_seconds,
            urgent_seconds=urgent_seconds,
            pulse_seconds=pulse_seconds,
            enabled=enabled,
            priority=priority,
            target_scope=target_scope,
            target_ids=target_ids,
            target_time=target_time,
            one_time_at=one_time_at,
            progress_fill=progress_fill,
            content_padding=content_padding,
            text_scale=text_scale,
            request_options=request_options,
        )
        return _response.data

    async def delete_countdown_bar_instance(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_countdown_bar_instance(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_countdown_bar_instance(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def list_brand_bug_instances(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_brand_bug_instances()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_brand_bug_instances(request_options=request_options)
        return _response.data

    async def create_brand_bug_instance(
        self,
        *,
        csrf_token: str,
        name: str,
        corner: BrandBugInputCorner,
        text: str,
        width_percent: int,
        text_size_percent: int,
        opacity_percent: int,
        margin_percent: int,
        text_color: str,
        background_style: BrandBugInputBackgroundStyle,
        enabled: bool,
        priority: int,
        target_scope: BrandBugInputTargetScope,
        target_ids: typing.Sequence[str],
        image_asset_id: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[dt.datetime] = OMIT,
        ends_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        name : str

        corner : BrandBugInputCorner

        text : str

        width_percent : int

        text_size_percent : int

        opacity_percent : int

        margin_percent : int

        text_color : str

        background_style : BrandBugInputBackgroundStyle

        enabled : bool

        priority : int

        target_scope : BrandBugInputTargetScope

        target_ids : typing.Sequence[str]

        image_asset_id : typing.Optional[str]
            A ready image in the Media library.

        starts_at : typing.Optional[dt.datetime]

        ends_at : typing.Optional[dt.datetime]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_brand_bug_instance(
                csrf_token="X-CSRF-Token",
                name="name",
                corner="top_left",
                text="text",
                width_percent=1,
                text_size_percent=1,
                opacity_percent=1,
                margin_percent=1,
                text_color="textColor",
                background_style="none",
                enabled=True,
                priority=1,
                target_scope="all",
                target_ids=["targetIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_brand_bug_instance(
            csrf_token=csrf_token,
            name=name,
            corner=corner,
            text=text,
            width_percent=width_percent,
            text_size_percent=text_size_percent,
            opacity_percent=opacity_percent,
            margin_percent=margin_percent,
            text_color=text_color,
            background_style=background_style,
            enabled=enabled,
            priority=priority,
            target_scope=target_scope,
            target_ids=target_ids,
            image_asset_id=image_asset_id,
            starts_at=starts_at,
            ends_at=ends_at,
            request_options=request_options,
        )
        return _response.data

    async def get_brand_bug_instance(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_brand_bug_instance(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_brand_bug_instance(id, request_options=request_options)
        return _response.data

    async def update_brand_bug_instance(
        self,
        id: str,
        *,
        csrf_token: str,
        name: str,
        corner: BrandBugInputCorner,
        text: str,
        width_percent: int,
        text_size_percent: int,
        opacity_percent: int,
        margin_percent: int,
        text_color: str,
        background_style: BrandBugInputBackgroundStyle,
        enabled: bool,
        priority: int,
        target_scope: BrandBugInputTargetScope,
        target_ids: typing.Sequence[str],
        image_asset_id: typing.Optional[str] = OMIT,
        starts_at: typing.Optional[dt.datetime] = OMIT,
        ends_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        name : str

        corner : BrandBugInputCorner

        text : str

        width_percent : int

        text_size_percent : int

        opacity_percent : int

        margin_percent : int

        text_color : str

        background_style : BrandBugInputBackgroundStyle

        enabled : bool

        priority : int

        target_scope : BrandBugInputTargetScope

        target_ids : typing.Sequence[str]

        image_asset_id : typing.Optional[str]
            A ready image in the Media library.

        starts_at : typing.Optional[dt.datetime]

        ends_at : typing.Optional[dt.datetime]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_brand_bug_instance(
                id="id",
                csrf_token="X-CSRF-Token",
                name="name",
                corner="top_left",
                text="text",
                width_percent=1,
                text_size_percent=1,
                opacity_percent=1,
                margin_percent=1,
                text_color="textColor",
                background_style="none",
                enabled=True,
                priority=1,
                target_scope="all",
                target_ids=["targetIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_brand_bug_instance(
            id,
            csrf_token=csrf_token,
            name=name,
            corner=corner,
            text=text,
            width_percent=width_percent,
            text_size_percent=text_size_percent,
            opacity_percent=opacity_percent,
            margin_percent=margin_percent,
            text_color=text_color,
            background_style=background_style,
            enabled=enabled,
            priority=priority,
            target_scope=target_scope,
            target_ids=target_ids,
            image_asset_id=image_asset_id,
            starts_at=starts_at,
            ends_at=ends_at,
            request_options=request_options,
        )
        return _response.data

    async def delete_brand_bug_instance(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_brand_bug_instance(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_brand_bug_instance(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def list_noise_meter_instances(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_noise_meter_instances()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_noise_meter_instances(request_options=request_options)
        return _response.data

    async def create_noise_meter_instance(
        self,
        *,
        csrf_token: str,
        name: str,
        message: str,
        warning_level: int,
        loud_level: int,
        sensitivity: int,
        trigger_hold_ms: int,
        clear_hold_ms: int,
        display_mode: NoiseMeterInputDisplayMode,
        height_px: int,
        enabled: bool,
        target_scope: NoiseMeterInputTargetScope,
        target_ids: typing.Sequence[str],
        schedule_enabled: typing.Optional[bool] = OMIT,
        schedule_days_of_week: typing.Optional[typing.Sequence[int]] = OMIT,
        schedule_start_time: typing.Optional[str] = OMIT,
        schedule_end_time: typing.Optional[str] = OMIT,
        schedule_timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        name : str

        message : str
            Replaces the bar's own TOO LOUD label. Empty is allowed.

        warning_level : int
            Where the yellow zone begins, and the level the room must stay below before the bar hides.

        loud_level : int
            Where the red zone begins and the bar can appear.

        sensitivity : int
            Percentage applied to the captured signal before normalization, for a microphone that reads quiet or hot. Not a calibration.

        trigger_hold_ms : int
            How long the room must stay loud before the bar appears.

        clear_hold_ms : int
            How long it must stay below warningLevel before the bar hides.

        display_mode : NoiseMeterInputDisplayMode

        height_px : int

        enabled : bool

        target_scope : NoiseMeterInputTargetScope

        target_ids : typing.Sequence[str]

        schedule_enabled : typing.Optional[bool]
            When false the bar may show whenever the room is too loud. A window governs the bar alone; the room is measured either way.

        schedule_days_of_week : typing.Optional[typing.Sequence[int]]
            Days the window may start on, Sunday 0 through Saturday 6.

        schedule_start_time : typing.Optional[str]

        schedule_end_time : typing.Optional[str]
            At or before the start is an overnight window belonging to the start day. The window is half-open, so the end minute is outside it.

        schedule_timezone : typing.Optional[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_noise_meter_instance(
                csrf_token="X-CSRF-Token",
                name="name",
                message="message",
                warning_level=1,
                loud_level=1,
                sensitivity=1,
                trigger_hold_ms=1,
                clear_hold_ms=1,
                display_mode="overlay",
                height_px=1,
                enabled=True,
                target_scope="all",
                target_ids=["targetIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_noise_meter_instance(
            csrf_token=csrf_token,
            name=name,
            message=message,
            warning_level=warning_level,
            loud_level=loud_level,
            sensitivity=sensitivity,
            trigger_hold_ms=trigger_hold_ms,
            clear_hold_ms=clear_hold_ms,
            display_mode=display_mode,
            height_px=height_px,
            enabled=enabled,
            target_scope=target_scope,
            target_ids=target_ids,
            schedule_enabled=schedule_enabled,
            schedule_days_of_week=schedule_days_of_week,
            schedule_start_time=schedule_start_time,
            schedule_end_time=schedule_end_time,
            schedule_timezone=schedule_timezone,
            request_options=request_options,
        )
        return _response.data

    async def get_noise_meter_instance(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_noise_meter_instance(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_noise_meter_instance(id, request_options=request_options)
        return _response.data

    async def update_noise_meter_instance(
        self,
        id: str,
        *,
        csrf_token: str,
        name: str,
        message: str,
        warning_level: int,
        loud_level: int,
        sensitivity: int,
        trigger_hold_ms: int,
        clear_hold_ms: int,
        display_mode: NoiseMeterInputDisplayMode,
        height_px: int,
        enabled: bool,
        target_scope: NoiseMeterInputTargetScope,
        target_ids: typing.Sequence[str],
        schedule_enabled: typing.Optional[bool] = OMIT,
        schedule_days_of_week: typing.Optional[typing.Sequence[int]] = OMIT,
        schedule_start_time: typing.Optional[str] = OMIT,
        schedule_end_time: typing.Optional[str] = OMIT,
        schedule_timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        name : str

        message : str
            Replaces the bar's own TOO LOUD label. Empty is allowed.

        warning_level : int
            Where the yellow zone begins, and the level the room must stay below before the bar hides.

        loud_level : int
            Where the red zone begins and the bar can appear.

        sensitivity : int
            Percentage applied to the captured signal before normalization, for a microphone that reads quiet or hot. Not a calibration.

        trigger_hold_ms : int
            How long the room must stay loud before the bar appears.

        clear_hold_ms : int
            How long it must stay below warningLevel before the bar hides.

        display_mode : NoiseMeterInputDisplayMode

        height_px : int

        enabled : bool

        target_scope : NoiseMeterInputTargetScope

        target_ids : typing.Sequence[str]

        schedule_enabled : typing.Optional[bool]
            When false the bar may show whenever the room is too loud. A window governs the bar alone; the room is measured either way.

        schedule_days_of_week : typing.Optional[typing.Sequence[int]]
            Days the window may start on, Sunday 0 through Saturday 6.

        schedule_start_time : typing.Optional[str]

        schedule_end_time : typing.Optional[str]
            At or before the start is an overnight window belonging to the start day. The window is half-open, so the end minute is outside it.

        schedule_timezone : typing.Optional[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_noise_meter_instance(
                id="id",
                csrf_token="X-CSRF-Token",
                name="name",
                message="message",
                warning_level=1,
                loud_level=1,
                sensitivity=1,
                trigger_hold_ms=1,
                clear_hold_ms=1,
                display_mode="overlay",
                height_px=1,
                enabled=True,
                target_scope="all",
                target_ids=["targetIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_noise_meter_instance(
            id,
            csrf_token=csrf_token,
            name=name,
            message=message,
            warning_level=warning_level,
            loud_level=loud_level,
            sensitivity=sensitivity,
            trigger_hold_ms=trigger_hold_ms,
            clear_hold_ms=clear_hold_ms,
            display_mode=display_mode,
            height_px=height_px,
            enabled=enabled,
            target_scope=target_scope,
            target_ids=target_ids,
            schedule_enabled=schedule_enabled,
            schedule_days_of_week=schedule_days_of_week,
            schedule_start_time=schedule_start_time,
            schedule_end_time=schedule_end_time,
            schedule_timezone=schedule_timezone,
            request_options=request_options,
        )
        return _response.data

    async def delete_noise_meter_instance(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_noise_meter_instance(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_noise_meter_instance(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def noise_meter_history_summary(
        self,
        id: str,
        *,
        range: typing.Optional[NoiseMeterHistorySummaryRequestRange] = None,
        screen_id: typing.Optional[str] = None,
        tz: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Descriptive statistics for the selected range: average and peak relative level, time in each band, warning events counted by the Player, the longest continuous loud run, and the loudest fifteen minutes. Screens are resolved from the caller's own scope.

        Parameters
        ----------
        id : str

        range : typing.Optional[NoiseMeterHistorySummaryRequestRange]

        screen_id : typing.Optional[str]
            One screen, authorized with the same screen scope as every other screen operation. Omitted means every screen the account may see.

        tz : typing.Optional[str]
            IANA timezone for day boundaries. Unreadable values fall back to UTC.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.noise_meter_history_summary(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.noise_meter_history_summary(
            id, range=range, screen_id=screen_id, tz=tz, request_options=request_options
        )
        return _response.data

    async def noise_meter_history_series(
        self,
        id: str,
        *,
        range: typing.Optional[NoiseMeterHistorySeriesRequestRange] = None,
        screen_id: typing.Optional[str] = None,
        tz: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Timeline points at the range's presentation resolution — one minute for a day, fifteen minutes for a week, an hour for a month. Averages are weighted by monitored time, peaks keep the maximum, durations sum, and a period with no records is omitted rather than returned as zero.

        Parameters
        ----------
        id : str

        range : typing.Optional[NoiseMeterHistorySeriesRequestRange]

        screen_id : typing.Optional[str]
            One screen, authorized with the same screen scope as every other screen operation. Omitted means every screen the account may see.

        tz : typing.Optional[str]
            IANA timezone for day boundaries. Unreadable values fall back to UTC.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.noise_meter_history_series(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.noise_meter_history_series(
            id, range=range, screen_id=screen_id, tz=tz, request_options=request_options
        )
        return _response.data

    async def noise_meter_history_daily(
        self,
        id: str,
        *,
        range: typing.Optional[NoiseMeterHistoryDailyRequestRange] = None,
        screen_id: typing.Optional[str] = None,
        tz: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Per-day rollups. Days without monitoring are absent, never zero.

        Parameters
        ----------
        id : str

        range : typing.Optional[NoiseMeterHistoryDailyRequestRange]

        screen_id : typing.Optional[str]
            One screen, authorized with the same screen scope as every other screen operation. Omitted means every screen the account may see.

        tz : typing.Optional[str]
            IANA timezone for day boundaries. Unreadable values fall back to UTC.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.noise_meter_history_daily(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.noise_meter_history_daily(
            id, range=range, screen_id=screen_id, tz=tz, request_options=request_options
        )
        return _response.data

    async def noise_meter_history_screens(
        self,
        id: str,
        *,
        range: typing.Optional[NoiseMeterHistoryScreensRequestRange] = None,
        tz: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Which of the caller's screens hold history for this meter in the range, so History shows one screen directly and offers a selector only when there is something to select.

        Parameters
        ----------
        id : str

        range : typing.Optional[NoiseMeterHistoryScreensRequestRange]

        tz : typing.Optional[str]
            IANA timezone for day boundaries. Unreadable values fall back to UTC.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.noise_meter_history_screens(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.noise_meter_history_screens(
            id, range=range, tz=tz, request_options=request_options
        )
        return _response.data

    async def export_noise_meter_history(
        self,
        id: str,
        *,
        range: typing.Optional[ExportNoiseMeterHistoryRequestRange] = None,
        screen_id: typing.Optional[str] = None,
        tz: typing.Optional[str] = None,
        granularity: typing.Optional[ExportNoiseMeterHistoryRequestGranularity] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        CSV of the selected range and screens, streamed server-side. Granularity is the stored ten-second records, one-minute summaries, or daily summaries.

        Parameters
        ----------
        id : str

        range : typing.Optional[ExportNoiseMeterHistoryRequestRange]

        screen_id : typing.Optional[str]
            One screen, authorized with the same screen scope as every other screen operation. Omitted means every screen the account may see.

        tz : typing.Optional[str]
            IANA timezone for day boundaries. Unreadable values fall back to UTC.

        granularity : typing.Optional[ExportNoiseMeterHistoryRequestGranularity]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.export_noise_meter_history(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_noise_meter_history(
            id, range=range, screen_id=screen_id, tz=tz, granularity=granularity, request_options=request_options
        )
        return _response.data

    async def reject_pairing(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.reject_pairing(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reject_pairing(id, request_options=request_options)
        return _response.data

    async def disable_screen(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.disable_screen(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_screen(id, request_options=request_options)
        return _response.data

    async def enable_screen(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.enable_screen(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_screen(id, request_options=request_options)
        return _response.data

    async def revoke_screen_credential(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.revoke_screen_credential(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.revoke_screen_credential(id, request_options=request_options)
        return _response.data

    async def create_upload_session(
        self,
        *,
        csrf_token: str,
        filename: str,
        mime_type: str,
        size_bytes: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        filename : str

        mime_type : str

        size_bytes : int

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_upload_session(
                csrf_token="X-CSRF-Token",
                filename="filename",
                mime_type="mimeType",
                size_bytes=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_upload_session(
            csrf_token=csrf_token,
            filename=filename,
            mime_type=mime_type,
            size_bytes=size_bytes,
            request_options=request_options,
        )
        return _response.data

    async def cancel_upload(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cancel_upload(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_upload(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    async def append_upload_bytes(
        self, id: str, *, csrf_token: str, upload_offset: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        upload_offset : int

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.append_upload_bytes(
                id="id",
                csrf_token="X-CSRF-Token",
                upload_offset=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.append_upload_bytes(
            id, csrf_token=csrf_token, upload_offset=upload_offset, request_options=request_options
        )
        return _response.data

    async def inspect_upload_session(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inspect_upload_session(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_upload_session(id, request_options=request_options)
        return _response.headers

    async def complete_upload(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.complete_upload(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_upload(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    async def list_assets(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        type: typing.Optional[AssetType] = None,
        status: typing.Optional[AssetStatus] = None,
        sort: typing.Optional[ListAssetsRequestSort] = None,
        archived: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        page_size : typing.Optional[int]

        search : typing.Optional[str]

        type : typing.Optional[AssetType]

        status : typing.Optional[AssetStatus]

        sort : typing.Optional[ListAssetsRequestSort]

        archived : typing.Optional[bool]
            Return manually archived and automatically expired library content instead of active content

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_assets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_assets(
            page=page,
            page_size=page_size,
            search=search,
            type=type,
            status=status,
            sort=sort,
            archived=archived,
            request_options=request_options,
        )
        return _response.data

    async def archive_assets(
        self,
        *,
        csrf_token: str,
        asset_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        asset_ids : typing.Sequence[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.archive_assets(
                csrf_token="X-CSRF-Token",
                asset_ids=["assetIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.archive_assets(
            csrf_token=csrf_token, asset_ids=asset_ids, request_options=request_options
        )
        return _response.data

    async def restore_assets(
        self,
        *,
        csrf_token: str,
        asset_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        asset_ids : typing.Sequence[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.restore_assets(
                csrf_token="X-CSRF-Token",
                asset_ids=["assetIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_assets(
            csrf_token=csrf_token, asset_ids=asset_ids, request_options=request_options
        )
        return _response.data

    async def get_asset(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_asset(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_asset(id, request_options=request_options)
        return _response.data

    async def delete_asset(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_asset(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_asset(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    async def update_asset(
        self,
        id: str,
        *,
        csrf_token: str,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        availability_set: typing.Optional[bool] = OMIT,
        available_from: typing.Optional[dt.datetime] = OMIT,
        expires_at: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        name : typing.Optional[str]

        description : typing.Optional[str]

        availability_set : typing.Optional[bool]

        available_from : typing.Optional[dt.datetime]

        expires_at : typing.Optional[dt.datetime]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_asset(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_asset(
            id,
            csrf_token=csrf_token,
            name=name,
            description=description,
            availability_set=availability_set,
            available_from=available_from,
            expires_at=expires_at,
            request_options=request_options,
        )
        return _response.data

    async def retry_asset_processing(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.retry_asset_processing(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retry_asset_processing(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def get_asset_thumbnail(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_asset_thumbnail(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_asset_thumbnail(id, request_options=request_options)
        return _response.data

    async def get_asset_playback_preview(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_asset_playback_preview(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_asset_playback_preview(id, request_options=request_options)
        return _response.data

    async def head_asset_playback_preview(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.head_asset_playback_preview(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_asset_playback_preview(id, request_options=request_options)
        return _response.headers

    async def download_player_variant(
        self,
        asset_id: str,
        variant_id: str,
        *,
        range: typing.Optional[str] = None,
        if_range: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        asset_id : str

        variant_id : str

        range : typing.Optional[str]

        if_range : typing.Optional[str]

        if_none_match : typing.Optional[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.download_player_variant(
                asset_id="assetId",
                variant_id="variantId",
                range="bytes=0-1048575",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_player_variant(
            asset_id,
            variant_id,
            range=range,
            if_range=if_range,
            if_none_match=if_none_match,
            request_options=request_options,
        )
        return _response.data

    async def inspect_player_variant(
        self, asset_id: str, variant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        asset_id : str

        variant_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inspect_player_variant(
                asset_id="assetId",
                variant_id="variantId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_player_variant(asset_id, variant_id, request_options=request_options)
        return _response.headers

    async def list_playlists(
        self,
        *,
        search: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_playlists()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_playlists(
            search=search, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_playlist(
        self,
        *,
        csrf_token: str,
        name: str,
        description: str,
        source_type: CreatePlaylistRequestSourceType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

        name : str

        description : str

        source_type : CreatePlaylistRequestSourceType
            static creates a manually ordered timeline; tag creates an initially empty tag-driven playlist

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_playlist(
                csrf_token="X-CSRF-Token",
                name="name",
                description="description",
                source_type="static",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_playlist(
            csrf_token=csrf_token,
            name=name,
            description=description,
            source_type=source_type,
            request_options=request_options,
        )
        return _response.data

    async def get_playlist(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_playlist(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_playlist(id, request_options=request_options)
        return _response.data

    async def delete_playlist(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_playlist(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_playlist(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    async def update_playlist(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_playlist(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_playlist(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    async def add_playlist_item(
        self,
        id: str,
        *,
        csrf_token: str,
        request: PlaylistItemInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request : PlaylistItemInput

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.add_playlist_item(
                id="id",
                csrf_token="csrfToken",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_playlist_item(
            id, csrf_token=csrf_token, request=request, request_options=request_options
        )
        return _response.data

    async def reorder_playlist_items(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.reorder_playlist_items(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reorder_playlist_items(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def bulk_update_playlist_items(
        self,
        id: str,
        *,
        csrf_token: str,
        request: PlaylistBulkItemInput,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request : PlaylistBulkItemInput

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.bulk_update_playlist_items(
                id="id",
                csrf_token="csrfToken",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bulk_update_playlist_items(
            id, csrf_token=csrf_token, request=request, request_options=request_options
        )
        return _response.data

    async def set_playlist_tag_rule(
        self,
        id: str,
        *,
        csrf_token: str,
        enabled: bool,
        match: PlaylistTagRuleInputMatch,
        image_duration_ms: int,
        tag_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        enabled : bool

        match : PlaylistTagRuleInputMatch

        image_duration_ms : int

        tag_ids : typing.Sequence[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.set_playlist_tag_rule(
                id="id",
                csrf_token="X-CSRF-Token",
                enabled=True,
                match="any",
                image_duration_ms=1,
                tag_ids=["tagIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_playlist_tag_rule(
            id,
            csrf_token=csrf_token,
            enabled=enabled,
            match=match,
            image_duration_ms=image_duration_ms,
            tag_ids=tag_ids,
            request_options=request_options,
        )
        return _response.data

    async def delete_playlist_item(
        self, id: str, item_id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        item_id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_playlist_item(
                id="id",
                item_id="itemId",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_playlist_item(
            id, item_id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def update_playlist_item(
        self, id: str, item_id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        item_id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_playlist_item(
                id="id",
                item_id="itemId",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_playlist_item(
            id, item_id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def get_playlist_assignment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_playlist_assignment(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_playlist_assignment(id, request_options=request_options)
        return _response.data

    async def assign_presentation(
        self,
        id: str,
        *,
        csrf_token: str,
        request: PresentationReference,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request : PresentationReference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PresentationReferencePlaylistId

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assign_presentation(
                id="id",
                csrf_token="X-CSRF-Token",
                request=PresentationReferencePlaylistId(
                    playlist_id="playlistId",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.assign_presentation(
            id, csrf_token=csrf_token, request=request, request_options=request_options
        )
        return _response.data

    async def remove_playlist_assignment(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.remove_playlist_assignment(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_playlist_assignment(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def get_player_manifest(
        self, *, if_none_match: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ManifestResponse:
        """
        Parameters
        ----------
        if_none_match : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ManifestResponse
            Stable screen-specific manifest or no-assignment manifest

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_player_manifest()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_player_manifest(
            if_none_match=if_none_match, request_options=request_options
        )
        return _response.data

    async def get_player_span_panel(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_player_span_panel(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_player_span_panel(id, request_options=request_options)
        return _response.data

    async def head_player_span_panel(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.head_player_span_panel(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_player_span_panel(id, request_options=request_options)
        return _response.headers

    async def list_screen_groups(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_screen_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_screen_groups(request_options=request_options)
        return _response.data

    async def create_screen_group(
        self, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_screen_group(
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_screen_group(csrf_token=csrf_token, request_options=request_options)
        return _response.data

    async def get_screen_group(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_screen_group(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_screen_group(id, request_options=request_options)
        return _response.data

    async def delete_screen_group(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_screen_group(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_screen_group(id, request_options=request_options)
        return _response.data

    async def update_screen_group(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_screen_group(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_screen_group(id, request_options=request_options)
        return _response.data

    async def get_span_geometry_and_preparation(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_span_geometry_and_preparation(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_span_geometry_and_preparation(id, request_options=request_options)
        return _response.data

    async def update_span_geometry(
        self,
        id: str,
        *,
        csrf_token: str,
        display_mode: typing.Optional[SpanGeometryInputDisplayMode] = OMIT,
        canvas: typing.Optional[SpanGeometryInputCanvas] = OMIT,
        panels: typing.Optional[typing.Sequence[SpanPanel]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        display_mode : typing.Optional[SpanGeometryInputDisplayMode]

        canvas : typing.Optional[SpanGeometryInputCanvas]

        panels : typing.Optional[typing.Sequence[SpanPanel]]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_span_geometry(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_span_geometry(
            id,
            csrf_token=csrf_token,
            display_mode=display_mode,
            canvas=canvas,
            panels=panels,
            request_options=request_options,
        )
        return _response.data

    async def preview_display_group_control(
        self,
        id: str,
        *,
        command_type: PreviewDisplayGroupControlRequestCommandType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        command_type : PreviewDisplayGroupControlRequestCommandType

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.preview_display_group_control(
                id="id",
                command_type="display_power_on",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_display_group_control(
            id, command_type=command_type, request_options=request_options
        )
        return _response.data

    async def apply_display_group_control(
        self,
        id: str,
        *,
        csrf_token: str,
        command_type: ApplyDisplayGroupControlRequestCommandType,
        fingerprint: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        command_type : ApplyDisplayGroupControlRequestCommandType

        fingerprint : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.apply_display_group_control(
                id="id",
                csrf_token="X-CSRF-Token",
                command_type="display_power_on",
                fingerprint="fingerprint",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.apply_display_group_control(
            id,
            csrf_token=csrf_token,
            command_type=command_type,
            fingerprint=fingerprint,
            request_options=request_options,
        )
        return _response.data

    async def add_screen_group_member(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.add_screen_group_member(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_screen_group_member(id, request_options=request_options)
        return _response.data

    async def remove_screen_group_member(
        self, id: str, screen_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        screen_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.remove_screen_group_member(
                id="id",
                screen_id="screenId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_screen_group_member(id, screen_id, request_options=request_options)
        return _response.data

    async def assign_sync_group_presentation(
        self, id: str, *, request: PresentationReference, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        request : PresentationReference

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PresentationReferencePlaylistId

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assign_sync_group_presentation(
                id="id",
                request=PresentationReferencePlaylistId(
                    playlist_id="playlistId",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.assign_sync_group_presentation(
            id, request=request, request_options=request_options
        )
        return _response.data

    async def unassign_sync_group_playlist(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.unassign_sync_group_playlist(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unassign_sync_group_playlist(id, request_options=request_options)
        return _response.data

    async def list_schedules(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_schedules()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_schedules(request_options=request_options)
        return _response.data

    async def create_schedule(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        The request contains exactly one of playlistId, layoutId, or displayAction. Display Control actions use the closed typed command registry; display_probe is not schedulable.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_schedule()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_schedule(request_options=request_options)
        return _response.data

    async def get_schedule(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_schedule(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_schedule(id, request_options=request_options)
        return _response.data

    async def delete_schedule(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_schedule(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_schedule(id, request_options=request_options)
        return _response.data

    async def update_schedule(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_schedule(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_schedule(id, request_options=request_options)
        return _response.data

    async def enable_schedule(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.enable_schedule(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.enable_schedule(id, request_options=request_options)
        return _response.data

    async def disable_schedule(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.disable_schedule(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disable_schedule(id, request_options=request_options)
        return _response.data

    async def preview_schedule(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.preview_schedule()


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_schedule(request_options=request_options)
        return _response.data

    async def create_website_asset(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Creates configuration-only public website content without fetching the page.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_website_asset()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_website_asset(request_options=request_options)
        return _response.data

    async def update_website_asset(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_website_asset(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_website_asset(id, request_options=request_options)
        return _response.data

    async def website_diagnostics(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.website_diagnostics(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.website_diagnostics(id, request_options=request_options)
        return _response.data

    async def create_widget(
        self,
        *,
        provider: WidgetProvider,
        name: str,
        configuration: typing.Dict[str, typing.Any],
        preset_id: typing.Optional[WidgetInputPresetId] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a reusable Widget or catalog App. An App recipe may atomically provision one hidden managed Data Source while preserving normal dependency and manifest behavior.

        Parameters
        ----------
        provider : WidgetProvider

        name : str

        configuration : typing.Dict[str, typing.Any]
            Provider-specific configuration. Native text Widgets omit textScale for automatic bounds-first sizing or use 25–500 percent; contentPadding defaults to 10 percent per edge and accepts 0–40.

        preset_id : typing.Optional[WidgetInputPresetId]

        description : typing.Optional[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_widget(
                provider="provider",
                name="name",
                configuration={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_widget(
            provider=provider,
            name=name,
            configuration=configuration,
            preset_id=preset_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def provider_catalog(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.provider_catalog()


        asyncio.run(main())
        """
        _response = await self._raw_client.provider_catalog(request_options=request_options)
        return _response.data

    async def content_definitions(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.content_definitions()


        asyncio.run(main())
        """
        _response = await self._raw_client.content_definitions(request_options=request_options)
        return _response.data

    async def compile_widget_preview(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.compile_widget_preview()


        asyncio.run(main())
        """
        _response = await self._raw_client.compile_widget_preview(request_options=request_options)
        return _response.data

    async def update_widget(
        self,
        id: str,
        *,
        provider: WidgetProvider,
        name: str,
        configuration: typing.Dict[str, typing.Any],
        preset_id: typing.Optional[WidgetInputPresetId] = OMIT,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        provider : WidgetProvider

        name : str

        configuration : typing.Dict[str, typing.Any]
            Provider-specific configuration. Native text Widgets omit textScale for automatic bounds-first sizing or use 25–500 percent; contentPadding defaults to 10 percent per edge and accepts 0–40.

        preset_id : typing.Optional[WidgetInputPresetId]

        description : typing.Optional[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_widget(
                id="id",
                provider="provider",
                name="name",
                configuration={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_widget(
            id,
            provider=provider,
            name=name,
            configuration=configuration,
            preset_id=preset_id,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def update_widget_preview_image(
        self,
        id: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Stores the frozen image captured from the actual Widget editor render. Requires an editor-capable dashboard session and CSRF token. The server accepts only a 960 by 540 JPEG no larger than 500 KB; Widget configuration updates clear the prior snapshot so stale renders are never shown.

        Parameters
        ----------
        id : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = await self._raw_client.update_widget_preview_image(
            id, request=request, request_options=request_options
        )
        return _response.data

    async def duplicate_widget(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.duplicate_widget(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.duplicate_widget(id, request_options=request_options)
        return _response.data

    async def list_data_sources(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_data_sources()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_data_sources(request_options=request_options)
        return _response.data

    async def create_data_source(
        self,
        *,
        provider: DataSourceProvider,
        name: str,
        configuration: typing.Dict[str, typing.Any],
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a reusable provider-neutral Data Source. Supported providers include calendar, structured feeds, Manual Table, Weather, Transit, CAP Alerts, and Air Quality. Data Sources are not assets and cannot be placed in playlists or Layouts.

        Parameters
        ----------
        provider : DataSourceProvider

        name : str

        configuration : typing.Dict[str, typing.Any]

        description : typing.Optional[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_data_source(
                provider="calendar",
                name="name",
                configuration={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_data_source(
            provider=provider,
            name=name,
            configuration=configuration,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def get_data_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_data_source(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_data_source(id, request_options=request_options)
        return _response.data

    async def delete_data_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_data_source(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_data_source(id, request_options=request_options)
        return _response.data

    async def update_data_source(
        self,
        id: str,
        *,
        provider: DataSourceProvider,
        name: str,
        configuration: typing.Dict[str, typing.Any],
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        provider : DataSourceProvider

        name : str

        configuration : typing.Dict[str, typing.Any]

        description : typing.Optional[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_data_source(
                id="id",
                provider="calendar",
                name="name",
                configuration={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_data_source(
            id,
            provider=provider,
            name=name,
            configuration=configuration,
            description=description,
            request_options=request_options,
        )
        return _response.data

    async def duplicate_data_source(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.duplicate_data_source(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.duplicate_data_source(id, request_options=request_options)
        return _response.data

    async def data_source_refresh_diagnostics(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.data_source_refresh_diagnostics(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.data_source_refresh_diagnostics(id, request_options=request_options)
        return _response.data

    async def preview_data_source(
        self,
        provider: PreviewDataSourceRequestProvider,
        *,
        configuration: typing.Dict[str, typing.Any],
        preview_date: typing.Optional[dt.date] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Fetches and parses a candidate Data Source configuration under the safe fetch policy without saving raw data. A previewDate exercises date-aware selection.

        Parameters
        ----------
        provider : PreviewDataSourceRequestProvider

        configuration : typing.Dict[str, typing.Any]

        preview_date : typing.Optional[dt.date]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.preview_data_source(
                provider="calendar",
                configuration={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_data_source(
            provider, configuration=configuration, preview_date=preview_date, request_options=request_options
        )
        return _response.data

    async def inspect_saved_data_source(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Detects fields for a saved RSS, Atom, JSON, or CSV Source using its stored configuration, including uploaded CSV bytes that detail responses strip. Same response shape as the provider inspect route.

        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inspect_saved_data_source(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_saved_data_source(id, request_options=request_options)
        return _response.data

    async def inspect_data_source(
        self,
        provider: InspectDataSourceRequestProvider,
        *,
        configuration: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Reports the fields a candidate RSS, Atom, JSON, or CSV connection contains, with a few sample values per field, a suggested field mapping, and which record fields the Source can fill. Runs under the same safe fetch policy as preview and deliberately does not require a mapping, because the mapping is what it exists to produce.

        Parameters
        ----------
        provider : InspectDataSourceRequestProvider

        configuration : typing.Dict[str, typing.Any]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inspect_data_source(
                provider="rss",
                configuration={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_data_source(
            provider, configuration=configuration, request_options=request_options
        )
        return _response.data

    async def list_forms(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns every Form Data Source the current user can access, each with name, description, published revision number, the caller's effective capabilities, and the caller's own submission counts (drafts, submitted, changes requested). A global Owner sees all forms; everyone else sees forms they created or hold a grant on. Backs the Forms portal and operator navigation.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_forms()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_forms(request_options=request_options)
        return _response.data

    async def create_form(
        self,
        *,
        name: str,
        draft_schema: typing.Dict[str, typing.Any],
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a Form Data Source (a Data Source provider). The server publishes the supplied draft schema as the form's first immutable revision and the creator becomes its manager. Requires the editor+ global role.

        Parameters
        ----------
        name : str

        draft_schema : typing.Dict[str, typing.Any]

        description : typing.Optional[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_form(
                name="name",
                draft_schema={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_form(
            name=name, draft_schema=draft_schema, description=description, request_options=request_options
        )
        return _response.data

    async def get_form(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns the Form detail with draft schema, published revision, workflow, saved views, and the caller's granted capabilities. Each workflow state carries recordCount and a removable flag (false once any record or saved view references it) so the Workflow editor can lock keys/deletion. Non-managers receive the published schema as the visible draft schema so unpublished edits are never exposed.

        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_form(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_form(id, request_options=request_options)
        return _response.data

    async def update_form_metadata(
        self,
        id: str,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates only the parent Data Source name and description. An omitted description preserves the stored value; provider and configuration cannot be changed here. Requires the manage capability.

        Parameters
        ----------
        id : str

        name : str

        description : typing.Optional[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_form_metadata(
                id="id",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_form_metadata(
            id, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def update_form_draft(
        self, id: str, *, schema: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Replaces the editable draft schema without publishing. Existing submissions are untouched. Requires the manage capability.

        Parameters
        ----------
        id : str

        schema : typing.Dict[str, typing.Any]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_form_draft(
                id="id",
                schema={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_form_draft(id, schema=schema, request_options=request_options)
        return _response.data

    async def publish_form(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Snapshots the current draft into a new immutable revision after conservative compatibility checks (a previously published output field cannot be removed or change its output type). Existing submissions remain tied to their original revisions. Requires the manage capability.

        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.publish_form(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_form(id, request_options=request_options)
        return _response.data

    async def configure_form_workflow(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Reconciles the form's bounded, script-free approval workflow in place. State keys referenced by existing records are immutable; transitions are replaced wholesale. Requires the manage capability.

        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.configure_form_workflow(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.configure_form_workflow(id, request_options=request_options)
        return _response.data

    async def list_form_records(
        self,
        id: str,
        *,
        states: typing.Optional[str] = None,
        mine: typing.Optional[bool] = None,
        search: typing.Optional[str] = None,
        sort: typing.Optional[ListFormRecordsRequestSort] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Returns a filtered, paginated page of a form's records. Callers with view_all, review, approve, or manage see every record; a submitter without those sees only their own submissions. `mine=true` scopes the page to the caller's own submissions even for privileged callers (the Forms portal's "your submissions"). Supports states, search, sort, mine, page, and pageSize query parameters.

        Parameters
        ----------
        id : str

        states : typing.Optional[str]
            Comma-separated workflow state keys

        mine : typing.Optional[bool]
            Scope to the caller's own submissions

        search : typing.Optional[str]

        sort : typing.Optional[ListFormRecordsRequestSort]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_form_records(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_form_records(
            id,
            states=states,
            mine=mine,
            search=search,
            sort=sort,
            page=page,
            page_size=page_size,
            request_options=request_options,
        )
        return _response.data

    async def create_form_record(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Creates a draft submission bound to the form's current published revision. Requires the submit capability. Image field values are never accepted here — they are set only by the attachment upload/remove endpoints — and a client-supplied image value is rejected. Display metadata dates are tri-state (omitted preserves, null clears, a value sets).

        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_form_record(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_form_record(id, request_options=request_options)
        return _response.data

    async def get_form_record(
        self, id: str, record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a record with its immutable revision schema, history, comments, attachments, and the server-calculated actions the caller may take (canEdit, canComment, canDelete, and availableTransitions with destination, label, required capability, and whether a note is required). Authorization is resolved server-side so clients never re-implement it. Visible only to a manager, reviewer/approver, view_all holder, or the record's own submitter.

        Parameters
        ----------
        id : str

        record_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_form_record(
                id="id",
                record_id="recordId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_form_record(id, record_id, request_options=request_options)
        return _response.data

    async def delete_form_record(
        self, id: str, record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Soft-deletes a record. Requires the manage capability.

        Parameters
        ----------
        id : str

        record_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_form_record(
                id="id",
                record_id="recordId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_form_record(id, record_id, request_options=request_options)
        return _response.data

    async def update_form_record(
        self, id: str, record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Edits a record's values and display metadata under optimistic concurrency (a version is required). Image field values are preserved server-side and cannot be changed here (a client-supplied image value is rejected); only the attachment endpoints modify them. Display dates are tri-state. A manager may edit any record; a submitter may edit their own record only while it is in a submitter-editable state.

        Parameters
        ----------
        id : str

        record_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_form_record(
                id="id",
                record_id="recordId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_form_record(id, record_id, request_options=request_options)
        return _response.data

    async def transition_form_record(
        self, id: str, record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Moves a record to a new workflow state, enforcing the configured transition, per-form capability and record ownership, optimistic concurrency (version), and required-field completeness (including required images, satisfied only by a bound attachment) before any submit transition or any transition into an output-eligible state. A note is recorded as a comment; a transition that requires a note (the default changes_requested path, derived from the workflow) is rejected with 422 when the note is empty. A 409 means the record changed; reload, preserving any unsent note.

        Parameters
        ----------
        id : str

        record_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.transition_form_record(
                id="id",
                record_id="recordId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transition_form_record(id, record_id, request_options=request_options)
        return _response.data

    async def add_form_record_comment(
        self, id: str, record_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Adds a reviewer or submitter comment. Available to a reviewer/approver or the record's own submitter.

        Parameters
        ----------
        id : str

        record_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.add_form_record_comment(
                id="id",
                record_id="recordId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_form_record_comment(id, record_id, request_options=request_options)
        return _response.data

    async def upload_form_record_attachment(
        self,
        id: str,
        record_id: str,
        *,
        field_key: str,
        data: str,
        version: int,
        file_name: typing.Optional[str] = OMIT,
        content_type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Uploads a base64-encoded image as a dedicated form attachment bound to an image field, returning the updated record detail with its incremented version. Uses optimistic concurrency — the request body must carry the record's current `version`, and a mismatch returns 409. Because image fields are single-valued, uploading to a field that already has an attachment replaces it. Authorization matches record editing. Form attachments are never exposed through the general Media library.

        Parameters
        ----------
        id : str

        record_id : str

        field_key : str

        data : str
            base64-encoded image bytes

        version : int
            The record's current version

        file_name : typing.Optional[str]

        content_type : typing.Optional[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.upload_form_record_attachment(
                id="id",
                record_id="recordId",
                field_key="fieldKey",
                data="data",
                version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_form_record_attachment(
            id,
            record_id,
            field_key=field_key,
            data=data,
            version=version,
            file_name=file_name,
            content_type=content_type,
            request_options=request_options,
        )
        return _response.data

    async def remove_form_record_attachment(
        self,
        id: str,
        record_id: str,
        attachment_id: str,
        *,
        version: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Unbinds an attachment, clears the field value it backed, and soft-deletes the underlying asset. Uses optimistic concurrency — the record's current `version` is required as a query parameter and a mismatch returns 409. Authorization matches record editing. Returns the updated record detail.

        Parameters
        ----------
        id : str

        record_id : str

        attachment_id : str

        version : int
            The record's current version

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.remove_form_record_attachment(
                id="id",
                record_id="recordId",
                attachment_id="attachmentId",
                version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_form_record_attachment(
            id, record_id, attachment_id, version=version, request_options=request_options
        )
        return _response.data

    async def serve_form_record_attachment(
        self, id: str, record_id: str, attachment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Streams a record's image attachment through this form-record-authorized endpoint (the only way to view a form attachment; they are never served from the Media library). Applies the same visibility rules as reading the record.

        Parameters
        ----------
        id : str

        record_id : str

        attachment_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.serve_form_record_attachment(
                id="id",
                record_id="recordId",
                attachment_id="attachmentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.serve_form_record_attachment(
            id, record_id, attachment_id, request_options=request_options
        )
        return _response.data

    async def list_approvals(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Returns a paginated page of records awaiting a review decision across every Form the user may review, approve, or manage. A record is pending when its current state has an outgoing transition requiring the review or approve capability. Paginated (page, pageSize) with a total rather than silently capped.

        Parameters
        ----------
        page : typing.Optional[int]

        page_size : typing.Optional[int]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_approvals()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_approvals(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def preview_form_view(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Projects an unsaved, proposed saved view and returns the resulting typed dataset without persisting anything or altering the cached projection. Only output-eligible records in the view's included states are returned, so a preview never exposes unapproved records. Requires the manage capability.

        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.preview_form_view(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_form_view(id, request_options=request_options)
        return _response.data

    async def get_form_outputs(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns the generated dataset for each saved view (dataset key, output fields and types, current record count, preview records) plus form-level projection status (last successful projection, next scheduled refresh/time-window boundary, using-cached/stale flag, projection error) and per-view Widget usage. Preview records come from the cached payload, so only output-eligible records appear. Available to view_all or manage.

        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_form_outputs(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_form_outputs(id, request_options=request_options)
        return _response.data

    async def rebuild_form_outputs(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Manually re-runs the form projection and returns the refreshed Outputs status. Invalidates affected manifests. Requires the manage capability and CSRF.

        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rebuild_form_outputs(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rebuild_form_outputs(id, request_options=request_options)
        return _response.data

    async def list_form_access(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns one entry per user with effective access to the form — the creator and all active global Owners as implicit, uneditable managers, followed by each granted user with their collapsed (non-redundant) capability set. Requires the manage capability.

        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_form_access(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_form_access(id, request_options=request_options)
        return _response.data

    async def replace_form_grants(
        self,
        id: str,
        user_id: str,
        *,
        capabilities: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Atomically replaces one user's grants on the form with the supplied capabilities (submit, view_own, view_all, review, approve, manage), collapsing implied capabilities to a minimal set, in a single transaction with an audit entry. The form creator and global Owners cannot be edited here, and a manager cannot remove their own only management path. Requires the manage capability and CSRF.

        Parameters
        ----------
        id : str

        user_id : str

        capabilities : typing.Sequence[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.replace_form_grants(
                id="id",
                user_id="userId",
                capabilities=["capabilities"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_form_grants(
            id, user_id, capabilities=capabilities, request_options=request_options
        )
        return _response.data

    async def search_form_users(
        self,
        id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        A bounded, manager-safe user directory for granting form access, returning only id, name, username, and global role for active users. Authorized to the form's managers (per-form), never the Owner/Admin-only user administration API.

        Parameters
        ----------
        id : str

        search : typing.Optional[str]

        limit : typing.Optional[int]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.search_form_users(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_form_users(
            id, search=search, limit=limit, request_options=request_options
        )
        return _response.data

    async def list_layouts(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Layout summaries include hasUnpublishedChanges, computed by comparing the current draft document with the published document rather than by comparing their independent revision counters.

        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_layouts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_layouts(request_options=request_options)
        return _response.data

    async def create_layout(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_layout()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_layout(request_options=request_options)
        return _response.data

    async def get_layout(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_layout(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_layout(id, request_options=request_options)
        return _response.data

    async def delete_layout(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_layout(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_layout(id, request_options=request_options)
        return _response.data

    async def update_layout(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_layout(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_layout(id, request_options=request_options)
        return _response.data

    async def save_layout_draft(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Saves a validated draft using expectedDraftRevision optimistic concurrency.

        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.save_layout_draft(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_layout_draft(id, request_options=request_options)
        return _response.data

    async def get_layout_preview_image(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Serves the authenticated, frozen JPEG captured from the real Layout editor canvas.

        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_layout_preview_image(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_layout_preview_image(id, request_options=request_options)
        return _response.data

    async def update_layout_preview_image(
        self, id: str, *, draft_revision: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Stores an aspect-preserving JPEG of at most 500 KB when draftRevision still matches the current Layout draft.

        Parameters
        ----------
        id : str

        draft_revision : int

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_layout_preview_image(
                id="id",
                draft_revision=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_layout_preview_image(
            id, draft_revision=draft_revision, request_options=request_options
        )
        return _response.data

    async def publish_layout(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.publish_layout(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_layout(id, request_options=request_options)
        return _response.data

    async def duplicate_layout(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.duplicate_layout(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.duplicate_layout(id, request_options=request_options)
        return _response.data

    async def list_layout_revisions(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_layout_revisions(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_layout_revisions(id, request_options=request_options)
        return _response.data

    async def restore_layout_revision(
        self, id: str, revision_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        revision_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.restore_layout_revision(
                id="id",
                revision_id="revisionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_layout_revision(id, revision_id, request_options=request_options)
        return _response.data

    async def list_content_submissions(
        self,
        *,
        state: typing.Optional[ListContentSubmissionsRequestState] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListContentSubmissionsResponse:
        """
        Lists immutable Playlist, Layout, and Campaign submissions. A submission snapshot is not changed by later draft edits.

        Parameters
        ----------
        state : typing.Optional[ListContentSubmissionsRequestState]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListContentSubmissionsResponse
            Submission list and current review policy

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_content_submissions()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_content_submissions(state=state, request_options=request_options)
        return _response.data

    async def get_content_submission(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetContentSubmissionResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetContentSubmissionResponse
            Exact immutable submission snapshot

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_content_submission(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_content_submission(id, request_options=request_options)
        return _response.data

    async def submit_content_draft(
        self,
        type: SubmitContentDraftRequestType,
        id: str,
        *,
        csrf_token: str,
        requested_publication_at: typing.Optional[dt.datetime] = OMIT,
        expected_revision: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Freezes the current working draft. expectedRevision is optional optimistic concurrency protection.

        Parameters
        ----------
        type : SubmitContentDraftRequestType

        id : str

        csrf_token : str

        requested_publication_at : typing.Optional[dt.datetime]

        expected_revision : typing.Optional[int]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.submit_content_draft(
                type="playlist",
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_content_draft(
            type,
            id,
            csrf_token=csrf_token,
            requested_publication_at=requested_publication_at,
            expected_revision=expected_revision,
            request_options=request_options,
        )
        return _response.data

    async def approve_content_submission(
        self,
        id: str,
        *,
        csrf_token: str,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        note : typing.Optional[str]

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.approve_content_submission(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.approve_content_submission(
            id, csrf_token=csrf_token, note=note, request_options=request_options
        )
        return _response.data

    async def request_content_changes(
        self, id: str, *, csrf_token: str, note: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        note : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.request_content_changes(
                id="id",
                csrf_token="X-CSRF-Token",
                note="note",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.request_content_changes(
            id, csrf_token=csrf_token, note=note, request_options=request_options
        )
        return _response.data

    async def publish_content_submission(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.publish_content_submission(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_content_submission(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def schedule_content_publication(
        self,
        id: str,
        *,
        csrf_token: str,
        requested_publication_at: dt.datetime,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        requested_publication_at : dt.datetime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.schedule_content_publication(
                id="id",
                csrf_token="X-CSRF-Token",
                requested_publication_at=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.schedule_content_publication(
            id,
            csrf_token=csrf_token,
            requested_publication_at=requested_publication_at,
            request_options=request_options,
        )
        return _response.data

    async def cancel_content_publication_schedule(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cancel_content_publication_schedule(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_content_publication_schedule(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def list_publication_history(
        self,
        type: ListPublicationHistoryRequestType,
        id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPublicationHistoryResponse:
        """
        Parameters
        ----------
        type : ListPublicationHistoryRequestType

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPublicationHistoryResponse
            Immutable publication checkpoints, newest first

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_publication_history(
                type="playlist",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_publication_history(type, id, request_options=request_options)
        return _response.data

    async def compare_publications(
        self,
        type: ComparePublicationsRequestType,
        id: str,
        *,
        from_publication_id: str,
        to_publication_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ComparePublicationsResponse:
        """
        Parameters
        ----------
        type : ComparePublicationsRequestType

        id : str

        from_publication_id : str

        to_publication_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ComparePublicationsResponse
            Semantic publication differences

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.compare_publications(
                type="playlist",
                id="id",
                from_publication_id="fromPublicationId",
                to_publication_id="toPublicationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.compare_publications(
            type,
            id,
            from_publication_id=from_publication_id,
            to_publication_id=to_publication_id,
            request_options=request_options,
        )
        return _response.data

    async def restore_publication_as_draft(
        self,
        type: RestorePublicationAsDraftRequestType,
        id: str,
        publication_id: str,
        *,
        csrf_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        type : RestorePublicationAsDraftRequestType

        id : str

        publication_id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.restore_publication_as_draft(
                type="playlist",
                id="id",
                publication_id="publicationId",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_publication_as_draft(
            type, id, publication_id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def rollback_publication(
        self,
        type: RollbackPublicationRequestType,
        id: str,
        publication_id: str,
        *,
        csrf_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        type : RollbackPublicationRequestType

        id : str

        publication_id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.rollback_publication(
                type="playlist",
                id="id",
                publication_id="publicationId",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rollback_publication(
            type, id, publication_id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def list_campaigns(
        self,
        *,
        search: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListCampaignsResponse:
        """
        Parameters
        ----------
        search : typing.Optional[str]

        page : typing.Optional[int]

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCampaignsResponse
            Campaign library

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_campaigns()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_campaigns(
            search=search, page=page, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def create_campaign(
        self,
        *,
        csrf_token: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        timezone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateCampaignResponse:
        """
        Parameters
        ----------
        csrf_token : str

        name : str

        description : typing.Optional[str]

        timezone : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateCampaignResponse
            Campaign draft created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_campaign(
                csrf_token="X-CSRF-Token",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_campaign(
            csrf_token=csrf_token,
            name=name,
            description=description,
            timezone=timezone,
            request_options=request_options,
        )
        return _response.data

    async def get_campaign(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetCampaignResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetCampaignResponse
            Campaign draft and lifecycle state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_campaign(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_campaign(id, request_options=request_options)
        return _response.data

    async def archive_campaign(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.archive_campaign(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.archive_campaign(id, csrf_token=csrf_token, request_options=request_options)
        return _response.data

    async def update_campaign_draft(
        self,
        id: str,
        *,
        csrf_token: str,
        expected_draft_revision: int,
        draft: CampaignSnapshot,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateCampaignDraftResponse:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        expected_draft_revision : int

        draft : CampaignSnapshot

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateCampaignDraftResponse
            Campaign draft saved

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            CampaignBlock,
            CampaignDestination,
            CampaignSnapshot,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_campaign_draft(
                id="id",
                csrf_token="X-CSRF-Token",
                expected_draft_revision=1000000,
                draft=CampaignSnapshot(
                    name="name",
                    description="description",
                    timezone="timezone",
                    destinations=[
                        CampaignDestination(
                            type="screen",
                            id="id",
                        )
                    ],
                    blocks=[
                        CampaignBlock(
                            id="id",
                            name="name",
                            content_type="playlist",
                            content_id="contentId",
                            priority=1,
                            type="one_time",
                            timezone="timezone",
                            enabled=True,
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_campaign_draft(
            id,
            csrf_token=csrf_token,
            expected_draft_revision=expected_draft_revision,
            draft=draft,
            request_options=request_options,
        )
        return _response.data

    async def preflight_campaign(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreflightCampaignResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreflightCampaignResponse
            Readiness, target, revision, and schedule preflight

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.preflight_campaign(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preflight_campaign(id, request_options=request_options)
        return _response.data

    async def list_campaign_releases(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListCampaignReleasesResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListCampaignReleasesResponse
            Immutable Campaign release history

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_campaign_releases(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_campaign_releases(id, request_options=request_options)
        return _response.data

    async def restore_campaign_release(
        self, id: str, release_id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> RestoreCampaignReleaseResponse:
        """
        Parameters
        ----------
        id : str

        release_id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RestoreCampaignReleaseResponse
            Release copied into the working Campaign draft

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.restore_campaign_release(
                id="id",
                release_id="releaseId",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_campaign_release(
            id, release_id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def publish_campaign(
        self,
        id: str,
        *,
        csrf_token: str,
        expected_draft_revision: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Publishes one immutable Campaign release by atomically materializing ordinary scheduler rows; Players do not receive a Campaign type.

        Parameters
        ----------
        id : str

        csrf_token : str

        expected_draft_revision : int

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.publish_campaign(
                id="id",
                csrf_token="X-CSRF-Token",
                expected_draft_revision=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_campaign(
            id, csrf_token=csrf_token, expected_draft_revision=expected_draft_revision, request_options=request_options
        )
        return _response.data

    async def list_takeovers(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_takeovers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_takeovers(request_options=request_options)
        return _response.data

    async def activate_a_takeover(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.activate_a_takeover()


        asyncio.run(main())
        """
        _response = await self._raw_client.activate_a_takeover(request_options=request_options)
        return _response.data

    async def read_takeover_and_per_screen_state(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.read_takeover_and_per_screen_state(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_takeover_and_per_screen_state(id, request_options=request_options)
        return _response.data

    async def cancel_an_active_takeover(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cancel_an_active_takeover(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_an_active_takeover(id, request_options=request_options)
        return _response.data

    async def list_presentation_networks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkListResponse:
        """
        Owner and Administrator read. Responses include only redacted network metadata and credentialSet; encrypted credentials and plaintext secrets are never returned to Studio.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkListResponse
            Presentation Networks and supported authentication types

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_presentation_networks()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_presentation_networks(request_options=request_options)
        return _response.data

    async def create_presentation_network(
        self,
        *,
        csrf_token: str,
        name: str,
        ssid: str,
        hidden: bool,
        security: PresentationNetworkSecurity,
        secret: PresentationNetworkSecret,
        identity: typing.Optional[str] = OMIT,
        anonymous_identity: typing.Optional[str] = OMIT,
        ca_certificate_pem: typing.Optional[str] = OMIT,
        domain_suffix_match: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PresentationNetworkResponse:
        """
        Parameters
        ----------
        csrf_token : str

        name : str

        ssid : str

        hidden : bool

        security : PresentationNetworkSecurity

        secret : PresentationNetworkSecret

        identity : typing.Optional[str]

        anonymous_identity : typing.Optional[str]

        ca_certificate_pem : typing.Optional[str]

        domain_suffix_match : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkResponse
            Network created; the credential is accepted but not returned

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_presentation_network(
                csrf_token="X-CSRF-Token",
                name="name",
                ssid="ssid",
                hidden=True,
                security="wpa_psk",
                secret="secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_presentation_network(
            csrf_token=csrf_token,
            name=name,
            ssid=ssid,
            hidden=hidden,
            security=security,
            secret=secret,
            identity=identity,
            anonymous_identity=anonymous_identity,
            ca_certificate_pem=ca_certificate_pem,
            domain_suffix_match=domain_suffix_match,
            request_options=request_options,
        )
        return _response.data

    async def get_presentation_network(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkDetailResponse:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkDetailResponse
            Network metadata and assigned Linux screens

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_presentation_network(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_presentation_network(id, request_options=request_options)
        return _response.data

    async def delete_presentation_network(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkResponse:
        """
        Assignments cascade and affected screens receive a durable configuration bump.

        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkResponse
            Deleted redacted network

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_presentation_network(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_presentation_network(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def update_presentation_network(
        self,
        id: str,
        *,
        csrf_token: str,
        name: str,
        ssid: str,
        hidden: bool,
        security: PresentationNetworkSecurity,
        secret: typing.Optional[PresentationNetworkSecret] = OMIT,
        identity: typing.Optional[str] = OMIT,
        anonymous_identity: typing.Optional[str] = OMIT,
        ca_certificate_pem: typing.Optional[str] = OMIT,
        domain_suffix_match: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PresentationNetworkResponse:
        """
        The secret field is write-only. Omitting it retains the saved credential; providing a new value rotates it and increments configRevision. No response contains the secret or ciphertext.

        Parameters
        ----------
        id : str

        csrf_token : str

        name : str

        ssid : str

        hidden : bool

        security : PresentationNetworkSecurity

        secret : typing.Optional[PresentationNetworkSecret]

        identity : typing.Optional[str]

        anonymous_identity : typing.Optional[str]

        ca_certificate_pem : typing.Optional[str]

        domain_suffix_match : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkResponse
            Redacted network after the update

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_presentation_network(
                id="id",
                csrf_token="X-CSRF-Token",
                name="name",
                ssid="ssid",
                hidden=True,
                security="wpa_psk",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_presentation_network(
            id,
            csrf_token=csrf_token,
            name=name,
            ssid=ssid,
            hidden=hidden,
            security=security,
            secret=secret,
            identity=identity,
            anonymous_identity=anonymous_identity,
            ca_certificate_pem=ca_certificate_pem,
            domain_suffix_match=domain_suffix_match,
            request_options=request_options,
        )
        return _response.data

    async def replace_presentation_network_assignments(
        self,
        id: str,
        *,
        csrf_token: str,
        screen_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PresentationNetworkAssignmentsResponse:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        screen_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkAssignmentsResponse
            Exact assignment set after replacement

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.replace_presentation_network_assignments(
                id="id",
                csrf_token="X-CSRF-Token",
                screen_ids=["screenIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_presentation_network_assignments(
            id, csrf_token=csrf_token, screen_ids=screen_ids, request_options=request_options
        )
        return _response.data

    async def test_presentation_network(
        self, id: str, *, csrf_token: str, screen_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkTestResponse:
        """
        The selected assigned Linux player joins and leaves the network without starting AirPlay. The durable command contains only the network ID and timeout; credentials are fetched separately by the authenticated player.

        Parameters
        ----------
        id : str

        csrf_token : str

        screen_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkTestResponse
            Connection test command queued

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.test_presentation_network(
                id="id",
                csrf_token="X-CSRF-Token",
                screen_id="screenId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.test_presentation_network(
            id, csrf_token=csrf_token, screen_id=screen_id, request_options=request_options
        )
        return _response.data

    async def get_screen_presentation_network(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkReadinessResponse:
        """
        Readiness is server-derived from the assignment and the player's reported helper, NetworkManager, Wi-Fi, revision, and connection facts.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkReadinessResponse
            Assignment and operator-facing readiness state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_screen_presentation_network(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_screen_presentation_network(id, request_options=request_options)
        return _response.data

    async def assign_screen_presentation_network(
        self,
        id: str,
        *,
        csrf_token: str,
        presentation_network_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PresentationNetworkAssignmentResponse:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        presentation_network_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkAssignmentResponse
            Assignment after replacement

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.assign_screen_presentation_network(
                id="id",
                csrf_token="X-CSRF-Token",
                presentation_network_id="presentationNetworkId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.assign_screen_presentation_network(
            id, csrf_token=csrf_token, presentation_network_id=presentation_network_id, request_options=request_options
        )
        return _response.data

    async def unassign_screen_presentation_network(
        self, id: str, *, csrf_token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkAssignmentResponse:
        """
        Parameters
        ----------
        id : str

        csrf_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkAssignmentResponse
            Screen assignment after removal

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.unassign_screen_presentation_network(
                id="id",
                csrf_token="X-CSRF-Token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unassign_screen_presentation_network(
            id, csrf_token=csrf_token, request_options=request_options
        )
        return _response.data

    async def get_player_presentation_network(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PresentationNetworkProvisioningResponse:
        """
        Device-authenticated only. The server derives the assignment from the authenticated screen and accepts no network ID. The response is marked Cache-Control: no-store and contains the plaintext credential only for the player to build its temporary NetworkManager profile.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PresentationNetworkProvisioningResponse
            Assigned network and credential; never log or persist this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_player_presentation_network()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_player_presentation_network(request_options=request_options)
        return _response.data

    async def list_presentation_overrides(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_presentation_overrides()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_presentation_overrides(request_options=request_options)
        return _response.data

    async def create_presentation_override(
        self,
        *,
        target_type: PresentationOverrideInputTargetType,
        target_id: str,
        content_type: PresentationOverrideInputContentType,
        content_id: str,
        duration_minutes: int,
        after_action: PresentationOverrideInputAfterAction,
        wake_display: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        target_type : PresentationOverrideInputTargetType

        target_id : str

        content_type : PresentationOverrideInputContentType

        content_id : str

        duration_minutes : int

        after_action : PresentationOverrideInputAfterAction

        wake_display : bool

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_presentation_override(
                target_type="screen",
                target_id="targetId",
                content_type="playlist",
                content_id="contentId",
                duration_minutes=1,
                after_action="resume",
                wake_display=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_presentation_override(
            target_type=target_type,
            target_id=target_id,
            content_type=content_type,
            content_id=content_id,
            duration_minutes=duration_minutes,
            after_action=after_action,
            wake_display=wake_display,
            request_options=request_options,
        )
        return _response.data

    async def stop_presentation_override(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stop_presentation_override(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_presentation_override(id, request_options=request_options)
        return _response.data

    async def read_the_nws_monitor_rules_active_matches_and_poll_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.read_the_nws_monitor_rules_active_matches_and_poll_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_the_nws_monitor_rules_active_matches_and_poll_health(
            request_options=request_options
        )
        return _response.data

    async def list_official_nws_counties_and_forecast_zones_for_an_area(
        self, *, area: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        area : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_official_nws_counties_and_forecast_zones_for_an_area(
                area="area",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_official_nws_counties_and_forecast_zones_for_an_area(
            area=area, request_options=request_options
        )
        return _response.data

    async def configure_nws_area_and_zone_monitoring(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.configure_nws_area_and_zone_monitoring()


        asyncio.run(main())
        """
        _response = await self._raw_client.configure_nws_area_and_zone_monitoring(request_options=request_options)
        return _response.data

    async def retrieve_and_apply_active_nws_alerts_now(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.retrieve_and_apply_active_nws_alerts_now()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_and_apply_active_nws_alerts_now(request_options=request_options)
        return _response.data

    async def create_an_automatic_nws_rule_answering_with_a_takeover_or_a_ticker_bar(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_an_automatic_nws_rule_answering_with_a_takeover_or_a_ticker_bar()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_an_automatic_nws_rule_answering_with_a_takeover_or_a_ticker_bar(
            request_options=request_options
        )
        return _response.data

    async def replace_an_automatic_nws_rule(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.replace_an_automatic_nws_rule(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_an_automatic_nws_rule(id, request_options=request_options)
        return _response.data

    async def delete_a_rule_ending_takeovers_it_raised_and_withdrawing_its_ticker(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_a_rule_ending_takeovers_it_raised_and_withdrawing_its_ticker(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_rule_ending_takeovers_it_raised_and_withdrawing_its_ticker(
            id, request_options=request_options
        )
        return _response.data

    async def list_recent_screen_commands(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_recent_screen_commands(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_recent_screen_commands(id, request_options=request_options)
        return _response.data

    async def queue_a_typed_operational_display_control_or_bounded_player_recovery_command(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Display Control command types are display_power_on, display_power_off, display_set_input, display_set_volume, display_mute, display_unmute, display_set_brightness, and display_probe. They are capability-gated by the target Player.

        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.queue_a_typed_operational_display_control_or_bounded_player_recovery_command(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.queue_a_typed_operational_display_control_or_bounded_player_recovery_command(
            id, request_options=request_options
        )
        return _response.data

    async def retrieve_executable_commands_for_the_authenticated_player(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.retrieve_executable_commands_for_the_authenticated_player()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_executable_commands_for_the_authenticated_player(
            request_options=request_options
        )
        return _response.data

    async def acknowledge_a_player_command(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.acknowledge_a_player_command(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.acknowledge_a_player_command(id, request_options=request_options)
        return _response.data

    async def report_a_safe_command_result(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.report_a_safe_command_result(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.report_a_safe_command_result(id, request_options=request_options)
        return _response.data

    async def read_typed_organization_settings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.read_typed_organization_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_typed_organization_settings(request_options=request_options)
        return _response.data

    async def update_settings_with_optimistic_revision(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_settings_with_optimistic_revision()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_settings_with_optimistic_revision(request_options=request_options)
        return _response.data

    async def read_current_user_preferences(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.read_current_user_preferences()


        asyncio.run(main())
        """
        _response = await self._raw_client.read_current_user_preferences(request_options=request_options)
        return _response.data

    async def update_current_user_preferences(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.update_current_user_preferences()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_current_user_preferences(request_options=request_options)
        return _response.data

    async def read_group_player_policy(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.read_group_player_policy(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_group_player_policy(id, request_options=request_options)
        return _response.data

    async def replace_typed_group_policy(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.replace_typed_group_policy(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_typed_group_policy(id, request_options=request_options)
        return _response.data

    async def reset_group_policy(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.reset_group_policy(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_group_policy(id, request_options=request_options)
        return _response.data

    async def read_screen_player_policy(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.read_screen_player_policy(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_screen_player_policy(id, request_options=request_options)
        return _response.data

    async def replace_typed_screen_policy(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.replace_typed_screen_policy(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_typed_screen_policy(id, request_options=request_options)
        return _response.data

    async def reset_screen_policy(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.reset_screen_policy(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.reset_screen_policy(id, request_options=request_options)
        return _response.data

    async def inspect_effective_values_and_inheritance_sources(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inspect_effective_values_and_inheritance_sources(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_effective_values_and_inheritance_sources(
            id, request_options=request_options
        )
        return _response.data

    async def read_commissioning_zero_touch_readiness_android_reliability_and_power_assist_state(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.read_commissioning_zero_touch_readiness_android_reliability_and_power_assist_state(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.read_commissioning_zero_touch_readiness_android_reliability_and_power_assist_state(
                id, request_options=request_options
            )
        )
        return _response.data

    async def store_administrator_confirmed_sleep_wake_cec_input_and_startup_test_results(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.store_administrator_confirmed_sleep_wake_cec_input_and_startup_test_results(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.store_administrator_confirmed_sleep_wake_cec_input_and_startup_test_results(
            id, request_options=request_options
        )
        return _response.data

    async def retrieve_effective_player_configuration(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.retrieve_effective_player_configuration()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_effective_player_configuration(request_options=request_options)
        return _response.data

    async def safe_system_diagnostics(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.safe_system_diagnostics()


        asyncio.run(main())
        """
        _response = await self._raw_client.safe_system_diagnostics(request_options=request_options)
        return _response.data

    async def run_a_fixed_safe_maintenance_action(
        self, action: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        action : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.run_a_fixed_safe_maintenance_action(
                action="action",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_a_fixed_safe_maintenance_action(action, request_options=request_options)
        return _response.data

    async def export_non_secret_settings(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.export_non_secret_settings()


        asyncio.run(main())
        """
        _response = await self._raw_client.export_non_secret_settings(request_options=request_options)
        return _response.data

    async def validate_settings_import_without_applying(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.validate_settings_import_without_applying()


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_settings_import_without_applying(request_options=request_options)
        return _response.data

    async def apply_confirmed_settings_import(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.apply_confirmed_settings_import()


        asyncio.run(main())
        """
        _response = await self._raw_client.apply_confirmed_settings_import(request_options=request_options)
        return _response.data

    async def list_fixed_repository_tilecast_player_releases_and_verification_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_fixed_repository_tilecast_player_releases_and_verification_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_fixed_repository_tilecast_player_releases_and_verification_state(
            request_options=request_options
        )
        return _response.data

    async def check_gibsonmb71tilecast_git_hub_releases(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.check_gibsonmb71tilecast_git_hub_releases()


        asyncio.run(main())
        """
        _response = await self._raw_client.check_gibsonmb71tilecast_git_hub_releases(request_options=request_options)
        return _response.data

    async def start_owner_authorized_git_hub_o_auth_device_flow(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.start_owner_authorized_git_hub_o_auth_device_flow()


        asyncio.run(main())
        """
        _response = await self._raw_client.start_owner_authorized_git_hub_o_auth_device_flow(
            request_options=request_options
        )
        return _response.data

    async def poll_an_active_git_hub_o_auth_device_flow(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.poll_an_active_git_hub_o_auth_device_flow()


        asyncio.run(main())
        """
        _response = await self._raw_client.poll_an_active_git_hub_o_auth_device_flow(request_options=request_options)
        return _response.data

    async def remove_a_device_authorized_git_hub_credential_from_tilecast_server(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.remove_a_device_authorized_git_hub_credential_from_tilecast_server()


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_a_device_authorized_git_hub_credential_from_tilecast_server(
            request_options=request_options
        )
        return _response.data

    async def upload_and_verify_a_signed_tilecast_player_release_bundle(
        self, *, files: typing.List[core.File], request_options: typing.Optional[RequestOptions] = None
    ) -> PostApiV1PlayerReleasesUploadResponse:
        """
        Accepts one release's three files as multipart files: the artifact, the signed update manifest and its signature. The file names select the family: `tilecast-player.apk` with `tilecast-player-update.json` (Android), `tilecast-player.AppImage` with `tilecast-player-update-linux.json` (Electron Linux), or `tilecast-edge-<version>-<arch>.tar.zst` with the signed envelope `tilecast-edge-update.json` (Tilecast Edge). Owner session plus CSRF or a configured release-publishing bearer token is required.

        Parameters
        ----------
        files : typing.List[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostApiV1PlayerReleasesUploadResponse
            Release fully verified and cached

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.upload_and_verify_a_signed_tilecast_player_release_bundle()


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_and_verify_a_signed_tilecast_player_release_bundle(
            files=files, request_options=request_options
        )
        return _response.data

    async def download_and_verify_a_signed_player_apk_into_private_cache(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.download_and_verify_a_signed_player_apk_into_private_cache(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_and_verify_a_signed_player_apk_into_private_cache(
            id, request_options=request_options
        )
        return _response.data

    async def list_player_update_deployments_narrowed_to_the_callers_screen_scope(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.list_player_update_deployments_narrowed_to_the_callers_screen_scope()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_player_update_deployments_narrowed_to_the_callers_screen_scope(
            request_options=request_options
        )
        return _response.data

    async def create_a_deduplicated_screen_and_group_deployment_with_an_optional_canary_cohort(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_a_deduplicated_screen_and_group_deployment_with_an_optional_canary_cohort()


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.create_a_deduplicated_screen_and_group_deployment_with_an_optional_canary_cohort(
                request_options=request_options
            )
        )
        return _response.data

    async def read_the_deployment_header_release_artifact_size_and_per_screen_update_state_for_the_screens_in_the_callers_scope(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.read_the_deployment_header_release_artifact_size_and_per_screen_update_state_for_the_screens_in_the_callers_scope(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_the_deployment_header_release_artifact_size_and_per_screen_update_state_for_the_screens_in_the_callers_scope(
            id, request_options=request_options
        )
        return _response.data

    async def cancel_pending_update_work_on_every_screen_the_deployment_reaches(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.cancel_pending_update_work_on_every_screen_the_deployment_reaches(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_pending_update_work_on_every_screen_the_deployment_reaches(
            id, request_options=request_options
        )
        return _response.data

    async def retry_a_failed_screen_update_idempotently(
        self, id: str, screen_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str

        screen_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.retry_a_failed_screen_update_idempotently(
                id="id",
                screen_id="screenId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retry_a_failed_screen_update_idempotently(
            id, screen_id, request_options=request_options
        )
        return _response.data

    async def get_targeted_verified_player_update_metadata(
        self, release_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetApiV1PlayerUpdatesReleaseIdResponse:
        """
        Parameters
        ----------
        release_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetApiV1PlayerUpdatesReleaseIdResponse
            Update metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_targeted_verified_player_update_metadata(
                release_id="releaseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_targeted_verified_player_update_metadata(
            release_id, request_options=request_options
        )
        return _response.data

    async def download_or_resume_the_authenticated_cached_release_artifact(
        self, release_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        The artifact of every family (the AppImage, the APK or the Tilecast Edge archive), with `Accept-Ranges: bytes`, a strong `ETag` of its SHA-256, and range requests. Only a screen targeted by an active deployment of the release may read it.

        Parameters
        ----------
        release_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.download_or_resume_the_authenticated_cached_release_artifact(
                release_id="releaseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_or_resume_the_authenticated_cached_release_artifact(
            release_id, request_options=request_options
        )
        return _response.data

    async def download_or_resume_authenticated_cached_apk(
        self, release_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        release_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.download_or_resume_authenticated_cached_apk(
                release_id="releaseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.download_or_resume_authenticated_cached_apk(
            release_id, request_options=request_options
        )
        return _response.data

    async def inspect_authenticated_apk_range_metadata(
        self, release_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Parameters
        ----------
        release_id : str

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.inspect_authenticated_apk_range_metadata(
                release_id="releaseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inspect_authenticated_apk_range_metadata(
            release_id, request_options=request_options
        )
        return _response.headers

    async def report_bounded_player_update_preparation_and_installer_status(
        self,
        deployment_id: str,
        *,
        state: PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState,
        downloaded_bytes: typing.Optional[int] = OMIT,
        permission_status: typing.Optional[str] = OMIT,
        installer_status: typing.Optional[str] = OMIT,
        error: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        deployment_id : str

        state : PostApiV1PlayerUpdateDeploymentsDeploymentIdStatusRequestState
            `succeeded` is accepted only for a Tilecast Edge release: it is the screen's explicit confirmation that the provisional release passed its health checks, and the only way an Edge target settles. Other families settle from the heartbeat.

        downloaded_bytes : typing.Optional[int]

        permission_status : typing.Optional[str]

        installer_status : typing.Optional[str]
            Tilecast Edge sends `provisional` with `reconnecting`, `confirmed` with `succeeded`, and `rolled_back` with a `failed` report of a release that was activated and then rolled back.

        error : typing.Optional[str]
            A bounded reason code, never free text from a server response.

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
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.report_bounded_player_update_preparation_and_installer_status(
                deployment_id="deploymentId",
                state="downloading",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.report_bounded_player_update_preparation_and_installer_status(
            deployment_id,
            state=state,
            downloaded_bytes=downloaded_bytes,
            permission_status=permission_status,
            installer_status=installer_status,
            error=error,
            request_options=request_options,
        )
        return _response.data
