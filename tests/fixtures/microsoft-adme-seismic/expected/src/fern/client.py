

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .apps.client import AppsClient, AsyncAppsClient
    from .dataset.client import AsyncDatasetClient, DatasetClient
    from .dataset_deprecated.client import AsyncDatasetDeprecatedClient, DatasetDeprecatedClient
    from .general.client import AsyncGeneralClient, GeneralClient
    from .impersonation_token.client import AsyncImpersonationTokenClient, ImpersonationTokenClient
    from .impersonation_token_obsolete.client import (
        AsyncImpersonationTokenObsoleteClient,
        ImpersonationTokenObsoleteClient,
    )
    from .sub_project.client import AsyncSubProjectClient, SubProjectClient
    from .subproject.client import AsyncSubprojectClient, SubprojectClient
    from .tenant.client import AsyncTenantClient, TenantClient
    from .tenant_obsolete.client import AsyncTenantObsoleteClient, TenantObsoleteClient
    from .users.client import AsyncUsersClient, UsersClient
    from .utility.client import AsyncUtilityClient, UtilityClient


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
        self._general: typing.Optional[GeneralClient] = None
        self._dataset: typing.Optional[DatasetClient] = None
        self._dataset_deprecated: typing.Optional[DatasetDeprecatedClient] = None
        self._utility: typing.Optional[UtilityClient] = None
        self._impersonation_token_obsolete: typing.Optional[ImpersonationTokenObsoleteClient] = None
        self._impersonation_token: typing.Optional[ImpersonationTokenClient] = None
        self._subproject: typing.Optional[SubprojectClient] = None
        self._sub_project: typing.Optional[SubProjectClient] = None
        self._tenant: typing.Optional[TenantClient] = None
        self._tenant_obsolete: typing.Optional[TenantObsoleteClient] = None
        self._users: typing.Optional[UsersClient] = None
        self._apps: typing.Optional[AppsClient] = None

    @property
    def general(self):
        if self._general is None:
            from .general.client import GeneralClient

            self._general = GeneralClient(client_wrapper=self._client_wrapper)
        return self._general

    @property
    def dataset(self):
        if self._dataset is None:
            from .dataset.client import DatasetClient

            self._dataset = DatasetClient(client_wrapper=self._client_wrapper)
        return self._dataset

    @property
    def dataset_deprecated(self):
        if self._dataset_deprecated is None:
            from .dataset_deprecated.client import DatasetDeprecatedClient

            self._dataset_deprecated = DatasetDeprecatedClient(client_wrapper=self._client_wrapper)
        return self._dataset_deprecated

    @property
    def utility(self):
        if self._utility is None:
            from .utility.client import UtilityClient

            self._utility = UtilityClient(client_wrapper=self._client_wrapper)
        return self._utility

    @property
    def impersonation_token_obsolete(self):
        if self._impersonation_token_obsolete is None:
            from .impersonation_token_obsolete.client import ImpersonationTokenObsoleteClient

            self._impersonation_token_obsolete = ImpersonationTokenObsoleteClient(client_wrapper=self._client_wrapper)
        return self._impersonation_token_obsolete

    @property
    def impersonation_token(self):
        if self._impersonation_token is None:
            from .impersonation_token.client import ImpersonationTokenClient

            self._impersonation_token = ImpersonationTokenClient(client_wrapper=self._client_wrapper)
        return self._impersonation_token

    @property
    def subproject(self):
        if self._subproject is None:
            from .subproject.client import SubprojectClient

            self._subproject = SubprojectClient(client_wrapper=self._client_wrapper)
        return self._subproject

    @property
    def sub_project(self):
        if self._sub_project is None:
            from .sub_project.client import SubProjectClient

            self._sub_project = SubProjectClient(client_wrapper=self._client_wrapper)
        return self._sub_project

    @property
    def tenant(self):
        if self._tenant is None:
            from .tenant.client import TenantClient

            self._tenant = TenantClient(client_wrapper=self._client_wrapper)
        return self._tenant

    @property
    def tenant_obsolete(self):
        if self._tenant_obsolete is None:
            from .tenant_obsolete.client import TenantObsoleteClient

            self._tenant_obsolete = TenantObsoleteClient(client_wrapper=self._client_wrapper)
        return self._tenant_obsolete

    @property
    def users(self):
        if self._users is None:
            from .users.client import UsersClient

            self._users = UsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def apps(self):
        if self._apps is None:
            from .apps.client import AppsClient

            self._apps = AppsClient(client_wrapper=self._client_wrapper)
        return self._apps


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
        self._general: typing.Optional[AsyncGeneralClient] = None
        self._dataset: typing.Optional[AsyncDatasetClient] = None
        self._dataset_deprecated: typing.Optional[AsyncDatasetDeprecatedClient] = None
        self._utility: typing.Optional[AsyncUtilityClient] = None
        self._impersonation_token_obsolete: typing.Optional[AsyncImpersonationTokenObsoleteClient] = None
        self._impersonation_token: typing.Optional[AsyncImpersonationTokenClient] = None
        self._subproject: typing.Optional[AsyncSubprojectClient] = None
        self._sub_project: typing.Optional[AsyncSubProjectClient] = None
        self._tenant: typing.Optional[AsyncTenantClient] = None
        self._tenant_obsolete: typing.Optional[AsyncTenantObsoleteClient] = None
        self._users: typing.Optional[AsyncUsersClient] = None
        self._apps: typing.Optional[AsyncAppsClient] = None

    @property
    def general(self):
        if self._general is None:
            from .general.client import AsyncGeneralClient

            self._general = AsyncGeneralClient(client_wrapper=self._client_wrapper)
        return self._general

    @property
    def dataset(self):
        if self._dataset is None:
            from .dataset.client import AsyncDatasetClient

            self._dataset = AsyncDatasetClient(client_wrapper=self._client_wrapper)
        return self._dataset

    @property
    def dataset_deprecated(self):
        if self._dataset_deprecated is None:
            from .dataset_deprecated.client import AsyncDatasetDeprecatedClient

            self._dataset_deprecated = AsyncDatasetDeprecatedClient(client_wrapper=self._client_wrapper)
        return self._dataset_deprecated

    @property
    def utility(self):
        if self._utility is None:
            from .utility.client import AsyncUtilityClient

            self._utility = AsyncUtilityClient(client_wrapper=self._client_wrapper)
        return self._utility

    @property
    def impersonation_token_obsolete(self):
        if self._impersonation_token_obsolete is None:
            from .impersonation_token_obsolete.client import AsyncImpersonationTokenObsoleteClient

            self._impersonation_token_obsolete = AsyncImpersonationTokenObsoleteClient(
                client_wrapper=self._client_wrapper
            )
        return self._impersonation_token_obsolete

    @property
    def impersonation_token(self):
        if self._impersonation_token is None:
            from .impersonation_token.client import AsyncImpersonationTokenClient

            self._impersonation_token = AsyncImpersonationTokenClient(client_wrapper=self._client_wrapper)
        return self._impersonation_token

    @property
    def subproject(self):
        if self._subproject is None:
            from .subproject.client import AsyncSubprojectClient

            self._subproject = AsyncSubprojectClient(client_wrapper=self._client_wrapper)
        return self._subproject

    @property
    def sub_project(self):
        if self._sub_project is None:
            from .sub_project.client import AsyncSubProjectClient

            self._sub_project = AsyncSubProjectClient(client_wrapper=self._client_wrapper)
        return self._sub_project

    @property
    def tenant(self):
        if self._tenant is None:
            from .tenant.client import AsyncTenantClient

            self._tenant = AsyncTenantClient(client_wrapper=self._client_wrapper)
        return self._tenant

    @property
    def tenant_obsolete(self):
        if self._tenant_obsolete is None:
            from .tenant_obsolete.client import AsyncTenantObsoleteClient

            self._tenant_obsolete = AsyncTenantObsoleteClient(client_wrapper=self._client_wrapper)
        return self._tenant_obsolete

    @property
    def users(self):
        if self._users is None:
            from .users.client import AsyncUsersClient

            self._users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        return self._users

    @property
    def apps(self):
        if self._apps is None:
            from .apps.client import AsyncAppsClient

            self._apps = AsyncAppsClient(client_wrapper=self._client_wrapper)
        return self._apps


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
