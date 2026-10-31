

import datetime as dt
import typing

import httpx
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .environment import FernApiEnvironment
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.address_info import AddressInfo
from .types.alert import Alert
from .types.alert_list import AlertList
from .types.device import Device
from .types.device_list import DeviceList
from .types.link import Link
from .types.service_provider import ServiceProvider
from .types.service_provider_list import ServiceProviderList
from .types.session_list import SessionList
from .types.sparkplug_name import SparkplugName
from .types.uuid_list import UuidList


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



    username : typing.Union[str, typing.Callable[[], str]]
    password : typing.Union[str, typing.Callable[[], str]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
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
            username=username,
            password=password,
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

    def search(self, *, request_options: typing.Optional[RequestOptions] = None) -> DeviceList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceList
            List of matching devices.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.search()
        """
        _response = self._raw_client.search(request_options=request_options)
        return _response.data

    def get_information_about_the_known_sparkplug_group_i_ds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AddressInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressInfo
            Sparkplug Group-IDs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.get_information_about_the_known_sparkplug_group_i_ds()
        """
        _response = self._raw_client.get_information_about_the_known_sparkplug_group_i_ds(
            request_options=request_options
        )
        return _response.data

    def get_information_about_nodes_in_a_given_group(
        self, group: SparkplugName, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AddressInfo:
        """
        Parameters
        ----------
        group : SparkplugName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressInfo
            Sparkplug Node-IDs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.get_information_about_nodes_in_a_given_group(
            group="group",
        )
        """
        _response = self._raw_client.get_information_about_nodes_in_a_given_group(
            group, request_options=request_options
        )
        return _response.data

    def get_information_about_devices_under_a_given_node(
        self, group: SparkplugName, node: SparkplugName, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AddressInfo:
        """
        Parameters
        ----------
        group : SparkplugName

        node : SparkplugName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressInfo
            Information about a Sparkplug Node.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.get_information_about_devices_under_a_given_node(
            group="group",
            node="node",
        )
        """
        _response = self._raw_client.get_information_about_devices_under_a_given_node(
            group, node, request_options=request_options
        )
        return _response.data

    def get_information_about_a_particular_device(
        self,
        group: SparkplugName,
        node: SparkplugName,
        device: SparkplugName,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddressInfo:
        """
        Parameters
        ----------
        group : SparkplugName

        node : SparkplugName

        device : SparkplugName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressInfo
            Information about a Sparkplug Device.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.get_information_about_a_particular_device(
            group="group",
            node="node",
            device="device",
        )
        """
        _response = self._raw_client.get_information_about_a_particular_device(
            group, node, device, request_options=request_options
        )
        return _response.data

    def list_all_known_alerts(self, *, request_options: typing.Optional[RequestOptions] = None) -> AlertList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertList
            Information about available alerts.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_all_known_alerts()
        """
        _response = self._raw_client.list_all_known_alerts(request_options=request_options)
        return _response.data

    def list_all_currently_active_alerts(self, *, request_options: typing.Optional[RequestOptions] = None) -> AlertList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertList
            Information about active alerts.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_all_currently_active_alerts()
        """
        _response = self._raw_client.list_all_currently_active_alerts(request_options=request_options)
        return _response.data

    def list_all_alerts_of_the_given_type(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertList:
        """
        Parameters
        ----------
        type : str
            The UUID of an alert type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertList
            Active alerts.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_all_alerts_of_the_given_type(
            type="type",
        )
        """
        _response = self._raw_client.list_all_alerts_of_the_given_type(type, request_options=request_options)
        return _response.data

    def list_all_active_alerts_of_the_given_type(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertList:
        """
        Parameters
        ----------
        type : str
            The UUID of an alert type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertList
            Active alerts of the given type.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_all_active_alerts_of_the_given_type(
            type="type",
        )
        """
        _response = self._raw_client.list_all_active_alerts_of_the_given_type(type, request_options=request_options)
        return _response.data

    def return_the_status_of_a_particular_alert(
        self, alert: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Alert:
        """
        Parameters
        ----------
        alert : str
            The UUID of an individual alert.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Alert
            Status of the given alert.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.return_the_status_of_a_particular_alert(
            alert="alert",
        )
        """
        _response = self._raw_client.return_the_status_of_a_particular_alert(alert, request_options=request_options)
        return _response.data

    def list_all_known_devices(self, *, request_options: typing.Optional[RequestOptions] = None) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList
            A list of all known device UUIDs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_all_known_devices()
        """
        _response = self._raw_client.list_all_known_devices(request_options=request_options)
        return _response.data

    def device(self, device: str, *, request_options: typing.Optional[RequestOptions] = None) -> Device:
        """
        Parameters
        ----------
        device : str
            The UUID of the device we are querying.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Device
            Information about the device.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.device(
            device="device",
        )
        """
        _response = self._raw_client.device(device, request_options=request_options)
        return _response.data

    def device_history(
        self,
        device: str,
        *,
        start: typing.Optional[dt.datetime] = None,
        finish: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionList:
        """
        Retrieve the history of this device's online/offline status. If start date is omitted, go back as far as we have records of this device. If end date is omitted, return up to the most recent birth or death.

        Parameters
        ----------
        device : str
            The UUID of the device we are querying.

        start : typing.Optional[dt.datetime]
            Include records on or after this time.

        finish : typing.Optional[dt.datetime]
            Include records on or before this time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionList
            The requested history of the device.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.device_history(
            device="device",
        )
        """
        _response = self._raw_client.device_history(device, start=start, finish=finish, request_options=request_options)
        return _response.data

    def list_all_known_links(self, *, request_options: typing.Optional[RequestOptions] = None) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_all_known_links()
        """
        _response = self._raw_client.list_all_known_links(request_options=request_options)
        return _response.data

    def list_the_links_published_by_a_given_device(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_the_links_published_by_a_given_device()
        """
        _response = self._raw_client.list_the_links_published_by_a_given_device(request_options=request_options)
        return _response.data

    def list_the_links_from_a_given_object(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_the_links_from_a_given_object()
        """
        _response = self._raw_client.list_the_links_from_a_given_object(request_options=request_options)
        return _response.data

    def list_the_links_to_a_given_object(self, *, request_options: typing.Optional[RequestOptions] = None) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_the_links_to_a_given_object()
        """
        _response = self._raw_client.list_the_links_to_a_given_object(request_options=request_options)
        return _response.data

    def list_the_links_using_a_given_link_relation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_the_links_using_a_given_link_relation()
        """
        _response = self._raw_client.list_the_links_using_a_given_link_relation(request_options=request_options)
        return _response.data

    def fetch_the_details_of_a_particular_link(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Link:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Link

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_the_details_of_a_particular_link()
        """
        _response = self._raw_client.fetch_the_details_of_a_particular_link(request_options=request_options)
        return _response.data

    def list_all_the_known_schema_uui_ds(self, *, request_options: typing.Optional[RequestOptions] = None) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList
            A list of the known schemas.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_all_the_known_schema_uui_ds()
        """
        _response = self._raw_client.list_all_the_known_schema_uui_ds(request_options=request_options)
        return _response.data

    def list_all_devices_currently_using_this_schema(
        self, schema: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UuidList:
        """
        Retrieve a list of UUID of the devices that currently advertise this schema in their birth certificate. This will include devices that are currently offline, but will not include devices that have used this schema in the past but which did not use it in their most recent birth certificate.

        Parameters
        ----------
        schema : str
            The UUID of the schema we are querying.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList
            A list of device UUIDs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_all_devices_currently_using_this_schema(
            schema="schema",
        )
        """
        _response = self._raw_client.list_all_devices_currently_using_this_schema(
            schema, request_options=request_options
        )
        return _response.data

    def list_all_the_known_service_uui_ds(self, *, request_options: typing.Optional[RequestOptions] = None) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList
            A list of the known services.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.list_all_the_known_service_uui_ds()
        """
        _response = self._raw_client.list_all_the_known_service_uui_ds(request_options=request_options)
        return _response.data

    def return_a_list_of_devices_providing_this_service(
        self, service: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceProviderList:
        """
        Parameters
        ----------
        service : str
            The UUID of the service we are querying.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceProviderList
            A list of service providers.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.return_a_list_of_devices_providing_this_service(
            service="service",
        )
        """
        _response = self._raw_client.return_a_list_of_devices_providing_this_service(
            service, request_options=request_options
        )
        return _response.data

    def fetch_my_service_advertisment(
        self, service: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceProvider:
        """
        Parameters
        ----------
        service : str
            The UUID of the service we are querying.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceProvider
            Current service advertisment.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_my_service_advertisment(
            service="service",
        )
        """
        _response = self._raw_client.fetch_my_service_advertisment(service, request_options=request_options)
        return _response.data

    def advertise_a_service(
        self,
        service: str,
        owner: str,
        *,
        device: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        service : str
            The UUID of the service we are querying.

        owner : str
            The provider of the service.

        device : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.advertise_a_service(
            service="service",
            owner="owner",
        )
        """
        _response = self._raw_client.advertise_a_service(
            service, owner, device=device, url=url, request_options=request_options
        )
        return _response.data

    def remove_a_service_advertisment(
        self, service: str, owner: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        service : str
            The UUID of the service we are querying.

        owner : str
            The provider of the service.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.remove_a_service_advertisment(
            service="service",
            owner="owner",
        )
        """
        _response = self._raw_client.remove_a_service_advertisment(service, owner, request_options=request_options)
        return _response.data

    def fetch_a_service_advertisment(
        self, service: str, owner: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceProvider:
        """
        Parameters
        ----------
        service : str
            The UUID of the service we are querying.

        owner : str
            The provider of the service.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceProvider
            Current service advertisment.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.fetch_a_service_advertisment(
            service="service",
            owner="owner",
        )
        """
        _response = self._raw_client.fetch_a_service_advertisment(service, owner, request_options=request_options)
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



    username : typing.Union[str, typing.Callable[[], str]]
    password : typing.Union[str, typing.Callable[[], str]]
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
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: FernApiEnvironment = FernApiEnvironment.DEFAULT,
        username: typing.Union[str, typing.Callable[[], str]],
        password: typing.Union[str, typing.Callable[[], str]],
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
            username=username,
            password=password,
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

    async def search(self, *, request_options: typing.Optional[RequestOptions] = None) -> DeviceList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceList
            List of matching devices.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.search()


        asyncio.run(main())
        """
        _response = await self._raw_client.search(request_options=request_options)
        return _response.data

    async def get_information_about_the_known_sparkplug_group_i_ds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AddressInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressInfo
            Sparkplug Group-IDs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.get_information_about_the_known_sparkplug_group_i_ds()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_information_about_the_known_sparkplug_group_i_ds(
            request_options=request_options
        )
        return _response.data

    async def get_information_about_nodes_in_a_given_group(
        self, group: SparkplugName, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AddressInfo:
        """
        Parameters
        ----------
        group : SparkplugName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressInfo
            Sparkplug Node-IDs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.get_information_about_nodes_in_a_given_group(
                group="group",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_information_about_nodes_in_a_given_group(
            group, request_options=request_options
        )
        return _response.data

    async def get_information_about_devices_under_a_given_node(
        self, group: SparkplugName, node: SparkplugName, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AddressInfo:
        """
        Parameters
        ----------
        group : SparkplugName

        node : SparkplugName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressInfo
            Information about a Sparkplug Node.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.get_information_about_devices_under_a_given_node(
                group="group",
                node="node",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_information_about_devices_under_a_given_node(
            group, node, request_options=request_options
        )
        return _response.data

    async def get_information_about_a_particular_device(
        self,
        group: SparkplugName,
        node: SparkplugName,
        device: SparkplugName,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AddressInfo:
        """
        Parameters
        ----------
        group : SparkplugName

        node : SparkplugName

        device : SparkplugName

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AddressInfo
            Information about a Sparkplug Device.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.get_information_about_a_particular_device(
                group="group",
                node="node",
                device="device",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_information_about_a_particular_device(
            group, node, device, request_options=request_options
        )
        return _response.data

    async def list_all_known_alerts(self, *, request_options: typing.Optional[RequestOptions] = None) -> AlertList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertList
            Information about available alerts.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_all_known_alerts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_known_alerts(request_options=request_options)
        return _response.data

    async def list_all_currently_active_alerts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertList
            Information about active alerts.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_all_currently_active_alerts()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_currently_active_alerts(request_options=request_options)
        return _response.data

    async def list_all_alerts_of_the_given_type(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertList:
        """
        Parameters
        ----------
        type : str
            The UUID of an alert type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertList
            Active alerts.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_all_alerts_of_the_given_type(
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_alerts_of_the_given_type(type, request_options=request_options)
        return _response.data

    async def list_all_active_alerts_of_the_given_type(
        self, type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AlertList:
        """
        Parameters
        ----------
        type : str
            The UUID of an alert type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AlertList
            Active alerts of the given type.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_all_active_alerts_of_the_given_type(
                type="type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_active_alerts_of_the_given_type(
            type, request_options=request_options
        )
        return _response.data

    async def return_the_status_of_a_particular_alert(
        self, alert: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Alert:
        """
        Parameters
        ----------
        alert : str
            The UUID of an individual alert.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Alert
            Status of the given alert.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.return_the_status_of_a_particular_alert(
                alert="alert",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_the_status_of_a_particular_alert(
            alert, request_options=request_options
        )
        return _response.data

    async def list_all_known_devices(self, *, request_options: typing.Optional[RequestOptions] = None) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList
            A list of all known device UUIDs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_all_known_devices()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_known_devices(request_options=request_options)
        return _response.data

    async def device(self, device: str, *, request_options: typing.Optional[RequestOptions] = None) -> Device:
        """
        Parameters
        ----------
        device : str
            The UUID of the device we are querying.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Device
            Information about the device.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.device(
                device="device",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.device(device, request_options=request_options)
        return _response.data

    async def device_history(
        self,
        device: str,
        *,
        start: typing.Optional[dt.datetime] = None,
        finish: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SessionList:
        """
        Retrieve the history of this device's online/offline status. If start date is omitted, go back as far as we have records of this device. If end date is omitted, return up to the most recent birth or death.

        Parameters
        ----------
        device : str
            The UUID of the device we are querying.

        start : typing.Optional[dt.datetime]
            Include records on or after this time.

        finish : typing.Optional[dt.datetime]
            Include records on or before this time.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SessionList
            The requested history of the device.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.device_history(
                device="device",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.device_history(
            device, start=start, finish=finish, request_options=request_options
        )
        return _response.data

    async def list_all_known_links(self, *, request_options: typing.Optional[RequestOptions] = None) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_all_known_links()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_known_links(request_options=request_options)
        return _response.data

    async def list_the_links_published_by_a_given_device(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_the_links_published_by_a_given_device()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_the_links_published_by_a_given_device(request_options=request_options)
        return _response.data

    async def list_the_links_from_a_given_object(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_the_links_from_a_given_object()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_the_links_from_a_given_object(request_options=request_options)
        return _response.data

    async def list_the_links_to_a_given_object(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_the_links_to_a_given_object()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_the_links_to_a_given_object(request_options=request_options)
        return _response.data

    async def list_the_links_using_a_given_link_relation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_the_links_using_a_given_link_relation()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_the_links_using_a_given_link_relation(request_options=request_options)
        return _response.data

    async def fetch_the_details_of_a_particular_link(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Link:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Link

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fetch_the_details_of_a_particular_link()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_the_details_of_a_particular_link(request_options=request_options)
        return _response.data

    async def list_all_the_known_schema_uui_ds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList
            A list of the known schemas.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_all_the_known_schema_uui_ds()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_the_known_schema_uui_ds(request_options=request_options)
        return _response.data

    async def list_all_devices_currently_using_this_schema(
        self, schema: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UuidList:
        """
        Retrieve a list of UUID of the devices that currently advertise this schema in their birth certificate. This will include devices that are currently offline, but will not include devices that have used this schema in the past but which did not use it in their most recent birth certificate.

        Parameters
        ----------
        schema : str
            The UUID of the schema we are querying.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList
            A list of device UUIDs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_all_devices_currently_using_this_schema(
                schema="schema",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_devices_currently_using_this_schema(
            schema, request_options=request_options
        )
        return _response.data

    async def list_all_the_known_service_uui_ds(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UuidList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UuidList
            A list of the known services.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.list_all_the_known_service_uui_ds()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_the_known_service_uui_ds(request_options=request_options)
        return _response.data

    async def return_a_list_of_devices_providing_this_service(
        self, service: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceProviderList:
        """
        Parameters
        ----------
        service : str
            The UUID of the service we are querying.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceProviderList
            A list of service providers.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.return_a_list_of_devices_providing_this_service(
                service="service",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_a_list_of_devices_providing_this_service(
            service, request_options=request_options
        )
        return _response.data

    async def fetch_my_service_advertisment(
        self, service: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceProvider:
        """
        Parameters
        ----------
        service : str
            The UUID of the service we are querying.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceProvider
            Current service advertisment.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fetch_my_service_advertisment(
                service="service",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_my_service_advertisment(service, request_options=request_options)
        return _response.data

    async def advertise_a_service(
        self,
        service: str,
        owner: str,
        *,
        device: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        service : str
            The UUID of the service we are querying.

        owner : str
            The provider of the service.

        device : typing.Optional[str]

        url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.advertise_a_service(
                service="service",
                owner="owner",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.advertise_a_service(
            service, owner, device=device, url=url, request_options=request_options
        )
        return _response.data

    async def remove_a_service_advertisment(
        self, service: str, owner: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        service : str
            The UUID of the service we are querying.

        owner : str
            The provider of the service.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.remove_a_service_advertisment(
                service="service",
                owner="owner",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_a_service_advertisment(
            service, owner, request_options=request_options
        )
        return _response.data

    async def fetch_a_service_advertisment(
        self, service: str, owner: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceProvider:
        """
        Parameters
        ----------
        service : str
            The UUID of the service we are querying.

        owner : str
            The provider of the service.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceProvider
            Current service advertisment.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.fetch_a_service_advertisment(
                service="service",
                owner="owner",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_service_advertisment(service, owner, request_options=request_options)
        return _response.data


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: FernApiEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
