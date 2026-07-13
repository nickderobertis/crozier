

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.device_server_create import DeviceServerCreate
from ..types.device_server_listing import DeviceServerListing
from ..types.device_server_read import DeviceServerRead
from .raw_client import AsyncRawDeviceServerClient, RawDeviceServerClient


OMIT = typing.cast(typing.Any, ...)


class DeviceServerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDeviceServerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDeviceServerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDeviceServerClient
        """
        return self._raw_client

    def list_all_device_server(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeviceServerListing]:
        """
        Get a collection of all the DeviceServers you have created.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeviceServerListing]
            After having created an Installation you can now create a DeviceServer. A DeviceServer is needed to do a login call with session-server.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.device_server.list_all_device_server()
        """
        _response = self._raw_client.list_all_device_server(request_options=request_options)
        return _response.data

    def create_device_server(
        self,
        *,
        description: str,
        secret: str,
        permitted_ips: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeviceServerCreate:
        """
        Create a new DeviceServer providing the installation token in the header and signing the request with the private part of the key you used to create the installation. The API Key that you are using will be bound to the IP address of the DeviceServer which you have created.<br/><br/>Using a Wildcard API Key gives you the freedom to make API calls even if the IP address has changed after the POST device-server.<br/><br/>Find out more at this link <a href="https:/bunq.com/en/apikey-dynamic-ip" target="_blank">https:/bunq.com/en/apikey-dynamic-ip</a>.

        Parameters
        ----------
        description : str
            The description of the DeviceServer. This is only for your own reference when reading the DeviceServer again.

        secret : str
            The API key. You can request an API key in the bunq app.

        permitted_ips : typing.Optional[typing.Sequence[str]]
            An array of IPs (v4 or v6) this DeviceServer will be able to do calls from. These will be linked to the API key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceServerCreate
            After having created an Installation you can now create a DeviceServer. A DeviceServer is needed to do a login call with session-server.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.device_server.create_device_server(
            description="description",
            secret="secret",
        )
        """
        _response = self._raw_client.create_device_server(
            description=description, secret=secret, permitted_ips=permitted_ips, request_options=request_options
        )
        return _response.data

    def read_device_server(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeviceServerRead:
        """
        Get one of your DeviceServers.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceServerRead
            After having created an Installation you can now create a DeviceServer. A DeviceServer is needed to do a login call with session-server.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )
        client.device_server.read_device_server(
            item_id=1,
        )
        """
        _response = self._raw_client.read_device_server(item_id, request_options=request_options)
        return _response.data


class AsyncDeviceServerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDeviceServerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDeviceServerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDeviceServerClient
        """
        return self._raw_client

    async def list_all_device_server(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DeviceServerListing]:
        """
        Get a collection of all the DeviceServers you have created.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DeviceServerListing]
            After having created an Installation you can now create a DeviceServer. A DeviceServer is needed to do a login call with session-server.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.device_server.list_all_device_server()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_device_server(request_options=request_options)
        return _response.data

    async def create_device_server(
        self,
        *,
        description: str,
        secret: str,
        permitted_ips: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DeviceServerCreate:
        """
        Create a new DeviceServer providing the installation token in the header and signing the request with the private part of the key you used to create the installation. The API Key that you are using will be bound to the IP address of the DeviceServer which you have created.<br/><br/>Using a Wildcard API Key gives you the freedom to make API calls even if the IP address has changed after the POST device-server.<br/><br/>Find out more at this link <a href="https:/bunq.com/en/apikey-dynamic-ip" target="_blank">https:/bunq.com/en/apikey-dynamic-ip</a>.

        Parameters
        ----------
        description : str
            The description of the DeviceServer. This is only for your own reference when reading the DeviceServer again.

        secret : str
            The API key. You can request an API key in the bunq app.

        permitted_ips : typing.Optional[typing.Sequence[str]]
            An array of IPs (v4 or v6) this DeviceServer will be able to do calls from. These will be linked to the API key.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceServerCreate
            After having created an Installation you can now create a DeviceServer. A DeviceServer is needed to do a login call with session-server.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.device_server.create_device_server(
                description="description",
                secret="secret",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_device_server(
            description=description, secret=secret, permitted_ips=permitted_ips, request_options=request_options
        )
        return _response.data

    async def read_device_server(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeviceServerRead:
        """
        Get one of your DeviceServers.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeviceServerRead
            After having created an Installation you can now create a DeviceServer. A DeviceServer is needed to do a login call with session-server.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            cache_control="YOUR_CACHE_CONTROL",
            bunq_language="YOUR_BUNQ_LANGUAGE",
            bunq_region="YOUR_BUNQ_REGION",
            bunq_client_request_id="YOUR_BUNQ_CLIENT_REQUEST_ID",
            bunq_geolocation="YOUR_BUNQ_GEOLOCATION",
            bunq_client_authentication="YOUR_BUNQ_CLIENT_AUTHENTICATION",
        )


        async def main() -> None:
            await client.device_server.read_device_server(
                item_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_device_server(item_id, request_options=request_options)
        return _response.data
