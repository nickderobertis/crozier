

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .companies.client import AsyncCompaniesClient, CompaniesClient
    from .departments.client import AsyncDepartmentsClient, DepartmentsClient
    from .employee_payrolls.client import AsyncEmployeePayrollsClient, EmployeePayrollsClient
    from .employee_schedules.client import AsyncEmployeeSchedulesClient, EmployeeSchedulesClient
    from .employees.client import AsyncEmployeesClient, EmployeesClient
    from .jobs.client import AsyncJobsClient, JobsClient
    from .payrolls.client import AsyncPayrollsClient, PayrollsClient
    from .time_off_requests.client import AsyncTimeOffRequestsClient, TimeOffRequestsClient


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



    apideck_consumer_id : str
    apideck_app_id : str
    apideck_service_id : typing.Optional[str]
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
        apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
        apideck_app_id="YOUR_APIDECK_APP_ID",
        apideck_service_id="YOUR_APIDECK_SERVICE_ID",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        apideck_consumer_id: str,
        apideck_app_id: str,
        apideck_service_id: typing.Optional[str] = None,
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
            apideck_consumer_id=apideck_consumer_id,
            apideck_app_id=apideck_app_id,
            apideck_service_id=apideck_service_id,
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
        self._companies: typing.Optional[CompaniesClient] = None
        self._departments: typing.Optional[DepartmentsClient] = None
        self._employees: typing.Optional[EmployeesClient] = None
        self._jobs: typing.Optional[JobsClient] = None
        self._payrolls: typing.Optional[PayrollsClient] = None
        self._employee_payrolls: typing.Optional[EmployeePayrollsClient] = None
        self._employee_schedules: typing.Optional[EmployeeSchedulesClient] = None
        self._time_off_requests: typing.Optional[TimeOffRequestsClient] = None

    @property
    def companies(self):
        if self._companies is None:
            from .companies.client import CompaniesClient

            self._companies = CompaniesClient(client_wrapper=self._client_wrapper)
        return self._companies

    @property
    def departments(self):
        if self._departments is None:
            from .departments.client import DepartmentsClient

            self._departments = DepartmentsClient(client_wrapper=self._client_wrapper)
        return self._departments

    @property
    def employees(self):
        if self._employees is None:
            from .employees.client import EmployeesClient

            self._employees = EmployeesClient(client_wrapper=self._client_wrapper)
        return self._employees

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import JobsClient

            self._jobs = JobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def payrolls(self):
        if self._payrolls is None:
            from .payrolls.client import PayrollsClient

            self._payrolls = PayrollsClient(client_wrapper=self._client_wrapper)
        return self._payrolls

    @property
    def employee_payrolls(self):
        if self._employee_payrolls is None:
            from .employee_payrolls.client import EmployeePayrollsClient

            self._employee_payrolls = EmployeePayrollsClient(client_wrapper=self._client_wrapper)
        return self._employee_payrolls

    @property
    def employee_schedules(self):
        if self._employee_schedules is None:
            from .employee_schedules.client import EmployeeSchedulesClient

            self._employee_schedules = EmployeeSchedulesClient(client_wrapper=self._client_wrapper)
        return self._employee_schedules

    @property
    def time_off_requests(self):
        if self._time_off_requests is None:
            from .time_off_requests.client import TimeOffRequestsClient

            self._time_off_requests = TimeOffRequestsClient(client_wrapper=self._client_wrapper)
        return self._time_off_requests


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



    apideck_consumer_id : str
    apideck_app_id : str
    apideck_service_id : typing.Optional[str]
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
        apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
        apideck_app_id="YOUR_APIDECK_APP_ID",
        apideck_service_id="YOUR_APIDECK_SERVICE_ID",
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        apideck_consumer_id: str,
        apideck_app_id: str,
        apideck_service_id: typing.Optional[str] = None,
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
            apideck_consumer_id=apideck_consumer_id,
            apideck_app_id=apideck_app_id,
            apideck_service_id=apideck_service_id,
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
        self._companies: typing.Optional[AsyncCompaniesClient] = None
        self._departments: typing.Optional[AsyncDepartmentsClient] = None
        self._employees: typing.Optional[AsyncEmployeesClient] = None
        self._jobs: typing.Optional[AsyncJobsClient] = None
        self._payrolls: typing.Optional[AsyncPayrollsClient] = None
        self._employee_payrolls: typing.Optional[AsyncEmployeePayrollsClient] = None
        self._employee_schedules: typing.Optional[AsyncEmployeeSchedulesClient] = None
        self._time_off_requests: typing.Optional[AsyncTimeOffRequestsClient] = None

    @property
    def companies(self):
        if self._companies is None:
            from .companies.client import AsyncCompaniesClient

            self._companies = AsyncCompaniesClient(client_wrapper=self._client_wrapper)
        return self._companies

    @property
    def departments(self):
        if self._departments is None:
            from .departments.client import AsyncDepartmentsClient

            self._departments = AsyncDepartmentsClient(client_wrapper=self._client_wrapper)
        return self._departments

    @property
    def employees(self):
        if self._employees is None:
            from .employees.client import AsyncEmployeesClient

            self._employees = AsyncEmployeesClient(client_wrapper=self._client_wrapper)
        return self._employees

    @property
    def jobs(self):
        if self._jobs is None:
            from .jobs.client import AsyncJobsClient

            self._jobs = AsyncJobsClient(client_wrapper=self._client_wrapper)
        return self._jobs

    @property
    def payrolls(self):
        if self._payrolls is None:
            from .payrolls.client import AsyncPayrollsClient

            self._payrolls = AsyncPayrollsClient(client_wrapper=self._client_wrapper)
        return self._payrolls

    @property
    def employee_payrolls(self):
        if self._employee_payrolls is None:
            from .employee_payrolls.client import AsyncEmployeePayrollsClient

            self._employee_payrolls = AsyncEmployeePayrollsClient(client_wrapper=self._client_wrapper)
        return self._employee_payrolls

    @property
    def employee_schedules(self):
        if self._employee_schedules is None:
            from .employee_schedules.client import AsyncEmployeeSchedulesClient

            self._employee_schedules = AsyncEmployeeSchedulesClient(client_wrapper=self._client_wrapper)
        return self._employee_schedules

    @property
    def time_off_requests(self):
        if self._time_off_requests is None:
            from .time_off_requests.client import AsyncTimeOffRequestsClient

            self._time_off_requests = AsyncTimeOffRequestsClient(client_wrapper=self._client_wrapper)
        return self._time_off_requests


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
