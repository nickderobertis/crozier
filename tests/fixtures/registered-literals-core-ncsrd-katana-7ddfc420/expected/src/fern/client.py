

from __future__ import annotations

import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .environment import FernApiEnvironment

if typing.TYPE_CHECKING:
    from .base_slice_descriptors.client import AsyncBaseSliceDescriptorsClient, BaseSliceDescriptorsClient
    from .bootstrap_katana.client import AsyncBootstrapKatanaClient, BootstrapKatanaClient
    from .ems.client import AsyncEmsClient, EmsClient
    from .generic_slice_template.client import AsyncGenericSliceTemplateClient, GenericSliceTemplateClient
    from .locations.client import AsyncLocationsClient, LocationsClient
    from .network_functions.client import AsyncNetworkFunctionsClient, NetworkFunctionsClient
    from .network_service_descriptors.client import (
        AsyncNetworkServiceDescriptorsClient,
        NetworkServiceDescriptorsClient,
    )
    from .nfvo.client import AsyncNfvoClient, NfvoClient
    from .policy_mgmt_system.client import AsyncPolicyMgmtSystemClient, PolicyMgmtSystemClient
    from .resources.client import AsyncResourcesClient, ResourcesClient
    from .slice.client import AsyncSliceClient, SliceClient
    from .vim.client import AsyncVimClient, VimClient
    from .wim.client import AsyncWimClient, WimClient


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



    katana_host : typing.Optional[str]
        Server URL variable for 'KATANA_HOST'. Defaults to 'katana.host'.

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

    client = FernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        katana_host: typing.Optional[str] = None,
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
        if katana_host is not None:
            _katana_host = katana_host if katana_host is not None else "katana.host"
            _environment_url_templates = {
                FernApiEnvironment.DEFAULT: "http://{KATANA_HOST}:8000/api",
            }
            _url_template = _environment_url_templates.get(environment, "http://{KATANA_HOST}:8000/api")
            if base_url is None:
                base_url = _url_template.format(KATANA_HOST=_katana_host)
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._slice: typing.Optional[SliceClient] = None
        self._vim: typing.Optional[VimClient] = None
        self._nfvo: typing.Optional[NfvoClient] = None
        self._wim: typing.Optional[WimClient] = None
        self._ems: typing.Optional[EmsClient] = None
        self._policy_mgmt_system: typing.Optional[PolicyMgmtSystemClient] = None
        self._resources: typing.Optional[ResourcesClient] = None
        self._network_functions: typing.Optional[NetworkFunctionsClient] = None
        self._network_service_descriptors: typing.Optional[NetworkServiceDescriptorsClient] = None
        self._generic_slice_template: typing.Optional[GenericSliceTemplateClient] = None
        self._base_slice_descriptors: typing.Optional[BaseSliceDescriptorsClient] = None
        self._bootstrap_katana: typing.Optional[BootstrapKatanaClient] = None
        self._locations: typing.Optional[LocationsClient] = None

    @property
    def slice(self):
        if self._slice is None:
            from .slice.client import SliceClient

            self._slice = SliceClient(client_wrapper=self._client_wrapper)
        return self._slice

    @property
    def vim(self):
        if self._vim is None:
            from .vim.client import VimClient

            self._vim = VimClient(client_wrapper=self._client_wrapper)
        return self._vim

    @property
    def nfvo(self):
        if self._nfvo is None:
            from .nfvo.client import NfvoClient

            self._nfvo = NfvoClient(client_wrapper=self._client_wrapper)
        return self._nfvo

    @property
    def wim(self):
        if self._wim is None:
            from .wim.client import WimClient

            self._wim = WimClient(client_wrapper=self._client_wrapper)
        return self._wim

    @property
    def ems(self):
        if self._ems is None:
            from .ems.client import EmsClient

            self._ems = EmsClient(client_wrapper=self._client_wrapper)
        return self._ems

    @property
    def policy_mgmt_system(self):
        if self._policy_mgmt_system is None:
            from .policy_mgmt_system.client import PolicyMgmtSystemClient

            self._policy_mgmt_system = PolicyMgmtSystemClient(client_wrapper=self._client_wrapper)
        return self._policy_mgmt_system

    @property
    def resources(self):
        if self._resources is None:
            from .resources.client import ResourcesClient

            self._resources = ResourcesClient(client_wrapper=self._client_wrapper)
        return self._resources

    @property
    def network_functions(self):
        if self._network_functions is None:
            from .network_functions.client import NetworkFunctionsClient

            self._network_functions = NetworkFunctionsClient(client_wrapper=self._client_wrapper)
        return self._network_functions

    @property
    def network_service_descriptors(self):
        if self._network_service_descriptors is None:
            from .network_service_descriptors.client import NetworkServiceDescriptorsClient

            self._network_service_descriptors = NetworkServiceDescriptorsClient(client_wrapper=self._client_wrapper)
        return self._network_service_descriptors

    @property
    def generic_slice_template(self):
        if self._generic_slice_template is None:
            from .generic_slice_template.client import GenericSliceTemplateClient

            self._generic_slice_template = GenericSliceTemplateClient(client_wrapper=self._client_wrapper)
        return self._generic_slice_template

    @property
    def base_slice_descriptors(self):
        if self._base_slice_descriptors is None:
            from .base_slice_descriptors.client import BaseSliceDescriptorsClient

            self._base_slice_descriptors = BaseSliceDescriptorsClient(client_wrapper=self._client_wrapper)
        return self._base_slice_descriptors

    @property
    def bootstrap_katana(self):
        if self._bootstrap_katana is None:
            from .bootstrap_katana.client import BootstrapKatanaClient

            self._bootstrap_katana = BootstrapKatanaClient(client_wrapper=self._client_wrapper)
        return self._bootstrap_katana

    @property
    def locations(self):
        if self._locations is None:
            from .locations.client import LocationsClient

            self._locations = LocationsClient(client_wrapper=self._client_wrapper)
        return self._locations


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



    katana_host : typing.Optional[str]
        Server URL variable for 'KATANA_HOST'. Defaults to 'katana.host'.

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

    client = AsyncFernApi()
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        katana_host: typing.Optional[str] = None,
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
        if katana_host is not None:
            _katana_host = katana_host if katana_host is not None else "katana.host"
            _environment_url_templates = {
                FernApiEnvironment.DEFAULT: "http://{KATANA_HOST}:8000/api",
            }
            _url_template = _environment_url_templates.get(environment, "http://{KATANA_HOST}:8000/api")
            if base_url is None:
                base_url = _url_template.format(KATANA_HOST=_katana_host)
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
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
        self._slice: typing.Optional[AsyncSliceClient] = None
        self._vim: typing.Optional[AsyncVimClient] = None
        self._nfvo: typing.Optional[AsyncNfvoClient] = None
        self._wim: typing.Optional[AsyncWimClient] = None
        self._ems: typing.Optional[AsyncEmsClient] = None
        self._policy_mgmt_system: typing.Optional[AsyncPolicyMgmtSystemClient] = None
        self._resources: typing.Optional[AsyncResourcesClient] = None
        self._network_functions: typing.Optional[AsyncNetworkFunctionsClient] = None
        self._network_service_descriptors: typing.Optional[AsyncNetworkServiceDescriptorsClient] = None
        self._generic_slice_template: typing.Optional[AsyncGenericSliceTemplateClient] = None
        self._base_slice_descriptors: typing.Optional[AsyncBaseSliceDescriptorsClient] = None
        self._bootstrap_katana: typing.Optional[AsyncBootstrapKatanaClient] = None
        self._locations: typing.Optional[AsyncLocationsClient] = None

    @property
    def slice(self):
        if self._slice is None:
            from .slice.client import AsyncSliceClient

            self._slice = AsyncSliceClient(client_wrapper=self._client_wrapper)
        return self._slice

    @property
    def vim(self):
        if self._vim is None:
            from .vim.client import AsyncVimClient

            self._vim = AsyncVimClient(client_wrapper=self._client_wrapper)
        return self._vim

    @property
    def nfvo(self):
        if self._nfvo is None:
            from .nfvo.client import AsyncNfvoClient

            self._nfvo = AsyncNfvoClient(client_wrapper=self._client_wrapper)
        return self._nfvo

    @property
    def wim(self):
        if self._wim is None:
            from .wim.client import AsyncWimClient

            self._wim = AsyncWimClient(client_wrapper=self._client_wrapper)
        return self._wim

    @property
    def ems(self):
        if self._ems is None:
            from .ems.client import AsyncEmsClient

            self._ems = AsyncEmsClient(client_wrapper=self._client_wrapper)
        return self._ems

    @property
    def policy_mgmt_system(self):
        if self._policy_mgmt_system is None:
            from .policy_mgmt_system.client import AsyncPolicyMgmtSystemClient

            self._policy_mgmt_system = AsyncPolicyMgmtSystemClient(client_wrapper=self._client_wrapper)
        return self._policy_mgmt_system

    @property
    def resources(self):
        if self._resources is None:
            from .resources.client import AsyncResourcesClient

            self._resources = AsyncResourcesClient(client_wrapper=self._client_wrapper)
        return self._resources

    @property
    def network_functions(self):
        if self._network_functions is None:
            from .network_functions.client import AsyncNetworkFunctionsClient

            self._network_functions = AsyncNetworkFunctionsClient(client_wrapper=self._client_wrapper)
        return self._network_functions

    @property
    def network_service_descriptors(self):
        if self._network_service_descriptors is None:
            from .network_service_descriptors.client import AsyncNetworkServiceDescriptorsClient

            self._network_service_descriptors = AsyncNetworkServiceDescriptorsClient(
                client_wrapper=self._client_wrapper
            )
        return self._network_service_descriptors

    @property
    def generic_slice_template(self):
        if self._generic_slice_template is None:
            from .generic_slice_template.client import AsyncGenericSliceTemplateClient

            self._generic_slice_template = AsyncGenericSliceTemplateClient(client_wrapper=self._client_wrapper)
        return self._generic_slice_template

    @property
    def base_slice_descriptors(self):
        if self._base_slice_descriptors is None:
            from .base_slice_descriptors.client import AsyncBaseSliceDescriptorsClient

            self._base_slice_descriptors = AsyncBaseSliceDescriptorsClient(client_wrapper=self._client_wrapper)
        return self._base_slice_descriptors

    @property
    def bootstrap_katana(self):
        if self._bootstrap_katana is None:
            from .bootstrap_katana.client import AsyncBootstrapKatanaClient

            self._bootstrap_katana = AsyncBootstrapKatanaClient(client_wrapper=self._client_wrapper)
        return self._bootstrap_katana

    @property
    def locations(self):
        if self._locations is None:
            from .locations.client import AsyncLocationsClient

            self._locations = AsyncLocationsClient(client_wrapper=self._client_wrapper)
        return self._locations


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
