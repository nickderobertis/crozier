

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .attorney_analytics_api.client import AsyncAttorneyAnalyticsApiClient, AttorneyAnalyticsApiClient
    from .authentication_api.client import AsyncAuthenticationApiClient, AuthenticationApiClient
    from .callback_api.client import AsyncCallbackApiClient, CallbackApiClient
    from .case_analytics_api.client import AsyncCaseAnalyticsApiClient, CaseAnalyticsApiClient
    from .case_docket_api.client import AsyncCaseDocketApiClient, CaseDocketApiClient
    from .case_documents_api.client import AsyncCaseDocumentsApiClient, CaseDocumentsApiClient
    from .case_export_api.client import AsyncCaseExportApiClient, CaseExportApiClient
    from .case_search_api.client import AsyncCaseSearchApiClient, CaseSearchApiClient
    from .case_tracking_api.client import AsyncCaseTrackingApiClient, CaseTrackingApiClient
    from .case_update_api.client import AsyncCaseUpdateApiClient, CaseUpdateApiClient
    from .court_availability_api.client import AsyncCourtAvailabilityApiClient, CourtAvailabilityApiClient
    from .court_standards_api.client import AsyncCourtStandardsApiClient, CourtStandardsApiClient
    from .judge_analytics_api.client import AsyncJudgeAnalyticsApiClient, JudgeAnalyticsApiClient
    from .law_firm_analytics_api.client import AsyncLawFirmAnalyticsApiClient, LawFirmAnalyticsApiClient
    from .pacer_api.client import AsyncPacerApiClient, PacerApiClient
    from .pacer_credential_api.client import AsyncPacerCredentialApiClient, PacerCredentialApiClient
    from .party_analytics_api.client import AsyncPartyAnalyticsApiClient, PartyAnalyticsApiClient
    from .usage_api.client import AsyncUsageApiClient, UsageApiClient


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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._case_docket_api: typing.Optional[CaseDocketApiClient] = None
        self._usage_api: typing.Optional[UsageApiClient] = None
        self._callback_api: typing.Optional[CallbackApiClient] = None
        self._case_documents_api: typing.Optional[CaseDocumentsApiClient] = None
        self._case_analytics_api: typing.Optional[CaseAnalyticsApiClient] = None
        self._case_export_api: typing.Optional[CaseExportApiClient] = None
        self._case_search_api: typing.Optional[CaseSearchApiClient] = None
        self._case_tracking_api: typing.Optional[CaseTrackingApiClient] = None
        self._case_update_api: typing.Optional[CaseUpdateApiClient] = None
        self._court_availability_api: typing.Optional[CourtAvailabilityApiClient] = None
        self._authentication_api: typing.Optional[AuthenticationApiClient] = None
        self._court_standards_api: typing.Optional[CourtStandardsApiClient] = None
        self._attorney_analytics_api: typing.Optional[AttorneyAnalyticsApiClient] = None
        self._judge_analytics_api: typing.Optional[JudgeAnalyticsApiClient] = None
        self._law_firm_analytics_api: typing.Optional[LawFirmAnalyticsApiClient] = None
        self._party_analytics_api: typing.Optional[PartyAnalyticsApiClient] = None
        self._pacer_api: typing.Optional[PacerApiClient] = None
        self._pacer_credential_api: typing.Optional[PacerCredentialApiClient] = None

    @property
    def case_docket_api(self):
        if self._case_docket_api is None:
            from .case_docket_api.client import CaseDocketApiClient

            self._case_docket_api = CaseDocketApiClient(client_wrapper=self._client_wrapper)
        return self._case_docket_api

    @property
    def usage_api(self):
        if self._usage_api is None:
            from .usage_api.client import UsageApiClient

            self._usage_api = UsageApiClient(client_wrapper=self._client_wrapper)
        return self._usage_api

    @property
    def callback_api(self):
        if self._callback_api is None:
            from .callback_api.client import CallbackApiClient

            self._callback_api = CallbackApiClient(client_wrapper=self._client_wrapper)
        return self._callback_api

    @property
    def case_documents_api(self):
        if self._case_documents_api is None:
            from .case_documents_api.client import CaseDocumentsApiClient

            self._case_documents_api = CaseDocumentsApiClient(client_wrapper=self._client_wrapper)
        return self._case_documents_api

    @property
    def case_analytics_api(self):
        if self._case_analytics_api is None:
            from .case_analytics_api.client import CaseAnalyticsApiClient

            self._case_analytics_api = CaseAnalyticsApiClient(client_wrapper=self._client_wrapper)
        return self._case_analytics_api

    @property
    def case_export_api(self):
        if self._case_export_api is None:
            from .case_export_api.client import CaseExportApiClient

            self._case_export_api = CaseExportApiClient(client_wrapper=self._client_wrapper)
        return self._case_export_api

    @property
    def case_search_api(self):
        if self._case_search_api is None:
            from .case_search_api.client import CaseSearchApiClient

            self._case_search_api = CaseSearchApiClient(client_wrapper=self._client_wrapper)
        return self._case_search_api

    @property
    def case_tracking_api(self):
        if self._case_tracking_api is None:
            from .case_tracking_api.client import CaseTrackingApiClient

            self._case_tracking_api = CaseTrackingApiClient(client_wrapper=self._client_wrapper)
        return self._case_tracking_api

    @property
    def case_update_api(self):
        if self._case_update_api is None:
            from .case_update_api.client import CaseUpdateApiClient

            self._case_update_api = CaseUpdateApiClient(client_wrapper=self._client_wrapper)
        return self._case_update_api

    @property
    def court_availability_api(self):
        if self._court_availability_api is None:
            from .court_availability_api.client import CourtAvailabilityApiClient

            self._court_availability_api = CourtAvailabilityApiClient(client_wrapper=self._client_wrapper)
        return self._court_availability_api

    @property
    def authentication_api(self):
        if self._authentication_api is None:
            from .authentication_api.client import AuthenticationApiClient

            self._authentication_api = AuthenticationApiClient(client_wrapper=self._client_wrapper)
        return self._authentication_api

    @property
    def court_standards_api(self):
        if self._court_standards_api is None:
            from .court_standards_api.client import CourtStandardsApiClient

            self._court_standards_api = CourtStandardsApiClient(client_wrapper=self._client_wrapper)
        return self._court_standards_api

    @property
    def attorney_analytics_api(self):
        if self._attorney_analytics_api is None:
            from .attorney_analytics_api.client import AttorneyAnalyticsApiClient

            self._attorney_analytics_api = AttorneyAnalyticsApiClient(client_wrapper=self._client_wrapper)
        return self._attorney_analytics_api

    @property
    def judge_analytics_api(self):
        if self._judge_analytics_api is None:
            from .judge_analytics_api.client import JudgeAnalyticsApiClient

            self._judge_analytics_api = JudgeAnalyticsApiClient(client_wrapper=self._client_wrapper)
        return self._judge_analytics_api

    @property
    def law_firm_analytics_api(self):
        if self._law_firm_analytics_api is None:
            from .law_firm_analytics_api.client import LawFirmAnalyticsApiClient

            self._law_firm_analytics_api = LawFirmAnalyticsApiClient(client_wrapper=self._client_wrapper)
        return self._law_firm_analytics_api

    @property
    def party_analytics_api(self):
        if self._party_analytics_api is None:
            from .party_analytics_api.client import PartyAnalyticsApiClient

            self._party_analytics_api = PartyAnalyticsApiClient(client_wrapper=self._client_wrapper)
        return self._party_analytics_api

    @property
    def pacer_api(self):
        if self._pacer_api is None:
            from .pacer_api.client import PacerApiClient

            self._pacer_api = PacerApiClient(client_wrapper=self._client_wrapper)
        return self._pacer_api

    @property
    def pacer_credential_api(self):
        if self._pacer_credential_api is None:
            from .pacer_credential_api.client import PacerCredentialApiClient

            self._pacer_credential_api = PacerCredentialApiClient(client_wrapper=self._client_wrapper)
        return self._pacer_credential_api


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
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
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
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._case_docket_api: typing.Optional[AsyncCaseDocketApiClient] = None
        self._usage_api: typing.Optional[AsyncUsageApiClient] = None
        self._callback_api: typing.Optional[AsyncCallbackApiClient] = None
        self._case_documents_api: typing.Optional[AsyncCaseDocumentsApiClient] = None
        self._case_analytics_api: typing.Optional[AsyncCaseAnalyticsApiClient] = None
        self._case_export_api: typing.Optional[AsyncCaseExportApiClient] = None
        self._case_search_api: typing.Optional[AsyncCaseSearchApiClient] = None
        self._case_tracking_api: typing.Optional[AsyncCaseTrackingApiClient] = None
        self._case_update_api: typing.Optional[AsyncCaseUpdateApiClient] = None
        self._court_availability_api: typing.Optional[AsyncCourtAvailabilityApiClient] = None
        self._authentication_api: typing.Optional[AsyncAuthenticationApiClient] = None
        self._court_standards_api: typing.Optional[AsyncCourtStandardsApiClient] = None
        self._attorney_analytics_api: typing.Optional[AsyncAttorneyAnalyticsApiClient] = None
        self._judge_analytics_api: typing.Optional[AsyncJudgeAnalyticsApiClient] = None
        self._law_firm_analytics_api: typing.Optional[AsyncLawFirmAnalyticsApiClient] = None
        self._party_analytics_api: typing.Optional[AsyncPartyAnalyticsApiClient] = None
        self._pacer_api: typing.Optional[AsyncPacerApiClient] = None
        self._pacer_credential_api: typing.Optional[AsyncPacerCredentialApiClient] = None

    @property
    def case_docket_api(self):
        if self._case_docket_api is None:
            from .case_docket_api.client import AsyncCaseDocketApiClient

            self._case_docket_api = AsyncCaseDocketApiClient(client_wrapper=self._client_wrapper)
        return self._case_docket_api

    @property
    def usage_api(self):
        if self._usage_api is None:
            from .usage_api.client import AsyncUsageApiClient

            self._usage_api = AsyncUsageApiClient(client_wrapper=self._client_wrapper)
        return self._usage_api

    @property
    def callback_api(self):
        if self._callback_api is None:
            from .callback_api.client import AsyncCallbackApiClient

            self._callback_api = AsyncCallbackApiClient(client_wrapper=self._client_wrapper)
        return self._callback_api

    @property
    def case_documents_api(self):
        if self._case_documents_api is None:
            from .case_documents_api.client import AsyncCaseDocumentsApiClient

            self._case_documents_api = AsyncCaseDocumentsApiClient(client_wrapper=self._client_wrapper)
        return self._case_documents_api

    @property
    def case_analytics_api(self):
        if self._case_analytics_api is None:
            from .case_analytics_api.client import AsyncCaseAnalyticsApiClient

            self._case_analytics_api = AsyncCaseAnalyticsApiClient(client_wrapper=self._client_wrapper)
        return self._case_analytics_api

    @property
    def case_export_api(self):
        if self._case_export_api is None:
            from .case_export_api.client import AsyncCaseExportApiClient

            self._case_export_api = AsyncCaseExportApiClient(client_wrapper=self._client_wrapper)
        return self._case_export_api

    @property
    def case_search_api(self):
        if self._case_search_api is None:
            from .case_search_api.client import AsyncCaseSearchApiClient

            self._case_search_api = AsyncCaseSearchApiClient(client_wrapper=self._client_wrapper)
        return self._case_search_api

    @property
    def case_tracking_api(self):
        if self._case_tracking_api is None:
            from .case_tracking_api.client import AsyncCaseTrackingApiClient

            self._case_tracking_api = AsyncCaseTrackingApiClient(client_wrapper=self._client_wrapper)
        return self._case_tracking_api

    @property
    def case_update_api(self):
        if self._case_update_api is None:
            from .case_update_api.client import AsyncCaseUpdateApiClient

            self._case_update_api = AsyncCaseUpdateApiClient(client_wrapper=self._client_wrapper)
        return self._case_update_api

    @property
    def court_availability_api(self):
        if self._court_availability_api is None:
            from .court_availability_api.client import AsyncCourtAvailabilityApiClient

            self._court_availability_api = AsyncCourtAvailabilityApiClient(client_wrapper=self._client_wrapper)
        return self._court_availability_api

    @property
    def authentication_api(self):
        if self._authentication_api is None:
            from .authentication_api.client import AsyncAuthenticationApiClient

            self._authentication_api = AsyncAuthenticationApiClient(client_wrapper=self._client_wrapper)
        return self._authentication_api

    @property
    def court_standards_api(self):
        if self._court_standards_api is None:
            from .court_standards_api.client import AsyncCourtStandardsApiClient

            self._court_standards_api = AsyncCourtStandardsApiClient(client_wrapper=self._client_wrapper)
        return self._court_standards_api

    @property
    def attorney_analytics_api(self):
        if self._attorney_analytics_api is None:
            from .attorney_analytics_api.client import AsyncAttorneyAnalyticsApiClient

            self._attorney_analytics_api = AsyncAttorneyAnalyticsApiClient(client_wrapper=self._client_wrapper)
        return self._attorney_analytics_api

    @property
    def judge_analytics_api(self):
        if self._judge_analytics_api is None:
            from .judge_analytics_api.client import AsyncJudgeAnalyticsApiClient

            self._judge_analytics_api = AsyncJudgeAnalyticsApiClient(client_wrapper=self._client_wrapper)
        return self._judge_analytics_api

    @property
    def law_firm_analytics_api(self):
        if self._law_firm_analytics_api is None:
            from .law_firm_analytics_api.client import AsyncLawFirmAnalyticsApiClient

            self._law_firm_analytics_api = AsyncLawFirmAnalyticsApiClient(client_wrapper=self._client_wrapper)
        return self._law_firm_analytics_api

    @property
    def party_analytics_api(self):
        if self._party_analytics_api is None:
            from .party_analytics_api.client import AsyncPartyAnalyticsApiClient

            self._party_analytics_api = AsyncPartyAnalyticsApiClient(client_wrapper=self._client_wrapper)
        return self._party_analytics_api

    @property
    def pacer_api(self):
        if self._pacer_api is None:
            from .pacer_api.client import AsyncPacerApiClient

            self._pacer_api = AsyncPacerApiClient(client_wrapper=self._client_wrapper)
        return self._pacer_api

    @property
    def pacer_credential_api(self):
        if self._pacer_credential_api is None:
            from .pacer_credential_api.client import AsyncPacerCredentialApiClient

            self._pacer_credential_api = AsyncPacerCredentialApiClient(client_wrapper=self._client_wrapper)
        return self._pacer_credential_api


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
