

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.otoroshi_health import OtoroshiHealth

if typing.TYPE_CHECKING:
    from .apikeys.client import ApikeysClient, AsyncApikeysClient
    from .auth_config.client import AsyncAuthConfigClient, AuthConfigClient
    from .certificates.client import AsyncCertificatesClient, CertificatesClient
    from .configuration.client import AsyncConfigurationClient, ConfigurationClient
    from .data_exporter_configs.client import AsyncDataExporterConfigsClient, DataExporterConfigsClient
    from .environments.client import AsyncEnvironmentsClient, EnvironmentsClient
    from .groups.client import AsyncGroupsClient, GroupsClient
    from .import_.client import AsyncImportClient, ImportClient
    from .jwt_verifiers.client import AsyncJwtVerifiersClient, JwtVerifiersClient
    from .scripts.client import AsyncScriptsClient, ScriptsClient
    from .services.client import AsyncServicesClient, ServicesClient
    from .snowmonkey.client import AsyncSnowmonkeyClient, SnowmonkeyClient
    from .stats.client import AsyncStatsClient, StatsClient
    from .templates.client import AsyncTemplatesClient, TemplatesClient
    from .validation_authorities.client import AsyncValidationAuthoritiesClient, ValidationAuthoritiesClient


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



    username : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    password : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            username=username,
            password=password,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)
        self._apikeys: typing.Optional[ApikeysClient] = None
        self._auth_config: typing.Optional[AuthConfigClient] = None
        self._certificates: typing.Optional[CertificatesClient] = None
        self._validation_authorities: typing.Optional[ValidationAuthoritiesClient] = None
        self._data_exporter_configs: typing.Optional[DataExporterConfigsClient] = None
        self._configuration: typing.Optional[ConfigurationClient] = None
        self._groups: typing.Optional[GroupsClient] = None
        self._services: typing.Optional[ServicesClient] = None
        self._import_: typing.Optional[ImportClient] = None
        self._stats: typing.Optional[StatsClient] = None
        self._scripts: typing.Optional[ScriptsClient] = None
        self._snowmonkey: typing.Optional[SnowmonkeyClient] = None
        self._jwt_verifiers: typing.Optional[JwtVerifiersClient] = None
        self._environments: typing.Optional[EnvironmentsClient] = None
        self._templates: typing.Optional[TemplatesClient] = None

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> OtoroshiHealth:
        """
        Import the full state of Otoroshi as a file

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiHealth
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.health()
        """
        _response = self._raw_client.health(request_options=request_options)
        return _response.data

    @property
    def apikeys(self):
        if self._apikeys is None:
            from .apikeys.client import ApikeysClient

            self._apikeys = ApikeysClient(client_wrapper=self._client_wrapper)
        return self._apikeys

    @property
    def auth_config(self):
        if self._auth_config is None:
            from .auth_config.client import AuthConfigClient

            self._auth_config = AuthConfigClient(client_wrapper=self._client_wrapper)
        return self._auth_config

    @property
    def certificates(self):
        if self._certificates is None:
            from .certificates.client import CertificatesClient

            self._certificates = CertificatesClient(client_wrapper=self._client_wrapper)
        return self._certificates

    @property
    def validation_authorities(self):
        if self._validation_authorities is None:
            from .validation_authorities.client import ValidationAuthoritiesClient

            self._validation_authorities = ValidationAuthoritiesClient(client_wrapper=self._client_wrapper)
        return self._validation_authorities

    @property
    def data_exporter_configs(self):
        if self._data_exporter_configs is None:
            from .data_exporter_configs.client import DataExporterConfigsClient

            self._data_exporter_configs = DataExporterConfigsClient(client_wrapper=self._client_wrapper)
        return self._data_exporter_configs

    @property
    def configuration(self):
        if self._configuration is None:
            from .configuration.client import ConfigurationClient

            self._configuration = ConfigurationClient(client_wrapper=self._client_wrapper)
        return self._configuration

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import GroupsClient

            self._groups = GroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def services(self):
        if self._services is None:
            from .services.client import ServicesClient

            self._services = ServicesClient(client_wrapper=self._client_wrapper)
        return self._services

    @property
    def import_(self):
        if self._import_ is None:
            from .import_.client import ImportClient

            self._import_ = ImportClient(client_wrapper=self._client_wrapper)
        return self._import_

    @property
    def stats(self):
        if self._stats is None:
            from .stats.client import StatsClient

            self._stats = StatsClient(client_wrapper=self._client_wrapper)
        return self._stats

    @property
    def scripts(self):
        if self._scripts is None:
            from .scripts.client import ScriptsClient

            self._scripts = ScriptsClient(client_wrapper=self._client_wrapper)
        return self._scripts

    @property
    def snowmonkey(self):
        if self._snowmonkey is None:
            from .snowmonkey.client import SnowmonkeyClient

            self._snowmonkey = SnowmonkeyClient(client_wrapper=self._client_wrapper)
        return self._snowmonkey

    @property
    def jwt_verifiers(self):
        if self._jwt_verifiers is None:
            from .jwt_verifiers.client import JwtVerifiersClient

            self._jwt_verifiers = JwtVerifiersClient(client_wrapper=self._client_wrapper)
        return self._jwt_verifiers

    @property
    def environments(self):
        if self._environments is None:
            from .environments.client import EnvironmentsClient

            self._environments = EnvironmentsClient(client_wrapper=self._client_wrapper)
        return self._environments

    @property
    def templates(self):
        if self._templates is None:
            from .templates.client import TemplatesClient

            self._templates = TemplatesClient(client_wrapper=self._client_wrapper)
        return self._templates


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



    username : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    password : typing.Optional[typing.Union[str, typing.Callable[[], str]]]
    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        username: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        password: typing.Optional[typing.Union[str, typing.Callable[[], str]]] = None,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        _defaulted_timeout = (
            timeout if timeout is not None else 60 if httpx_client is None else httpx_client.timeout.read
        )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            username=username,
            password=password,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)
        self._apikeys: typing.Optional[AsyncApikeysClient] = None
        self._auth_config: typing.Optional[AsyncAuthConfigClient] = None
        self._certificates: typing.Optional[AsyncCertificatesClient] = None
        self._validation_authorities: typing.Optional[AsyncValidationAuthoritiesClient] = None
        self._data_exporter_configs: typing.Optional[AsyncDataExporterConfigsClient] = None
        self._configuration: typing.Optional[AsyncConfigurationClient] = None
        self._groups: typing.Optional[AsyncGroupsClient] = None
        self._services: typing.Optional[AsyncServicesClient] = None
        self._import_: typing.Optional[AsyncImportClient] = None
        self._stats: typing.Optional[AsyncStatsClient] = None
        self._scripts: typing.Optional[AsyncScriptsClient] = None
        self._snowmonkey: typing.Optional[AsyncSnowmonkeyClient] = None
        self._jwt_verifiers: typing.Optional[AsyncJwtVerifiersClient] = None
        self._environments: typing.Optional[AsyncEnvironmentsClient] = None
        self._templates: typing.Optional[AsyncTemplatesClient] = None

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def health(self, *, request_options: typing.Optional[RequestOptions] = None) -> OtoroshiHealth:
        """
        Import the full state of Otoroshi as a file

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OtoroshiHealth
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.health()


        asyncio.run(main())
        """
        _response = await self._raw_client.health(request_options=request_options)
        return _response.data

    @property
    def apikeys(self):
        if self._apikeys is None:
            from .apikeys.client import AsyncApikeysClient

            self._apikeys = AsyncApikeysClient(client_wrapper=self._client_wrapper)
        return self._apikeys

    @property
    def auth_config(self):
        if self._auth_config is None:
            from .auth_config.client import AsyncAuthConfigClient

            self._auth_config = AsyncAuthConfigClient(client_wrapper=self._client_wrapper)
        return self._auth_config

    @property
    def certificates(self):
        if self._certificates is None:
            from .certificates.client import AsyncCertificatesClient

            self._certificates = AsyncCertificatesClient(client_wrapper=self._client_wrapper)
        return self._certificates

    @property
    def validation_authorities(self):
        if self._validation_authorities is None:
            from .validation_authorities.client import AsyncValidationAuthoritiesClient

            self._validation_authorities = AsyncValidationAuthoritiesClient(client_wrapper=self._client_wrapper)
        return self._validation_authorities

    @property
    def data_exporter_configs(self):
        if self._data_exporter_configs is None:
            from .data_exporter_configs.client import AsyncDataExporterConfigsClient

            self._data_exporter_configs = AsyncDataExporterConfigsClient(client_wrapper=self._client_wrapper)
        return self._data_exporter_configs

    @property
    def configuration(self):
        if self._configuration is None:
            from .configuration.client import AsyncConfigurationClient

            self._configuration = AsyncConfigurationClient(client_wrapper=self._client_wrapper)
        return self._configuration

    @property
    def groups(self):
        if self._groups is None:
            from .groups.client import AsyncGroupsClient

            self._groups = AsyncGroupsClient(client_wrapper=self._client_wrapper)
        return self._groups

    @property
    def services(self):
        if self._services is None:
            from .services.client import AsyncServicesClient

            self._services = AsyncServicesClient(client_wrapper=self._client_wrapper)
        return self._services

    @property
    def import_(self):
        if self._import_ is None:
            from .import_.client import AsyncImportClient

            self._import_ = AsyncImportClient(client_wrapper=self._client_wrapper)
        return self._import_

    @property
    def stats(self):
        if self._stats is None:
            from .stats.client import AsyncStatsClient

            self._stats = AsyncStatsClient(client_wrapper=self._client_wrapper)
        return self._stats

    @property
    def scripts(self):
        if self._scripts is None:
            from .scripts.client import AsyncScriptsClient

            self._scripts = AsyncScriptsClient(client_wrapper=self._client_wrapper)
        return self._scripts

    @property
    def snowmonkey(self):
        if self._snowmonkey is None:
            from .snowmonkey.client import AsyncSnowmonkeyClient

            self._snowmonkey = AsyncSnowmonkeyClient(client_wrapper=self._client_wrapper)
        return self._snowmonkey

    @property
    def jwt_verifiers(self):
        if self._jwt_verifiers is None:
            from .jwt_verifiers.client import AsyncJwtVerifiersClient

            self._jwt_verifiers = AsyncJwtVerifiersClient(client_wrapper=self._client_wrapper)
        return self._jwt_verifiers

    @property
    def environments(self):
        if self._environments is None:
            from .environments.client import AsyncEnvironmentsClient

            self._environments = AsyncEnvironmentsClient(client_wrapper=self._client_wrapper)
        return self._environments

    @property
    def templates(self):
        if self._templates is None:
            from .templates.client import AsyncTemplatesClient

            self._templates = AsyncTemplatesClient(client_wrapper=self._client_wrapper)
        return self._templates


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
