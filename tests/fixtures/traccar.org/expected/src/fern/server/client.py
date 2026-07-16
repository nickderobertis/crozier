

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.server import Server
from ..types.server_attributes import ServerAttributes
from .raw_client import AsyncRawServerClient, RawServerClient


OMIT = typing.cast(typing.Any, ...)


class ServerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawServerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawServerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawServerClient
        """
        return self._raw_client

    def fetch_server_information(self, *, request_options: typing.Optional[RequestOptions] = None) -> Server:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Server
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.server.fetch_server_information()
        """
        _response = self._raw_client.fetch_server_information(request_options=request_options)
        return _response.data

    def update_server_information(
        self,
        *,
        attributes: typing.Optional[ServerAttributes] = OMIT,
        bing_key: typing.Optional[str] = OMIT,
        coordinate_format: typing.Optional[str] = OMIT,
        device_readonly: typing.Optional[bool] = OMIT,
        force_settings: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        latitude: typing.Optional[float] = OMIT,
        limit_commands: typing.Optional[bool] = OMIT,
        longitude: typing.Optional[float] = OMIT,
        map_: typing.Optional[str] = OMIT,
        map_url: typing.Optional[str] = OMIT,
        poi_layer: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        registration: typing.Optional[bool] = OMIT,
        twelve_hour_format: typing.Optional[bool] = OMIT,
        version: typing.Optional[str] = OMIT,
        zoom: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Server:
        """
        Parameters
        ----------
        attributes : typing.Optional[ServerAttributes]

        bing_key : typing.Optional[str]

        coordinate_format : typing.Optional[str]

        device_readonly : typing.Optional[bool]

        force_settings : typing.Optional[bool]

        id : typing.Optional[int]

        latitude : typing.Optional[float]

        limit_commands : typing.Optional[bool]

        longitude : typing.Optional[float]

        map_ : typing.Optional[str]

        map_url : typing.Optional[str]

        poi_layer : typing.Optional[str]

        readonly : typing.Optional[bool]

        registration : typing.Optional[bool]

        twelve_hour_format : typing.Optional[bool]

        version : typing.Optional[str]

        zoom : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Server
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.server.update_server_information()
        """
        _response = self._raw_client.update_server_information(
            attributes=attributes,
            bing_key=bing_key,
            coordinate_format=coordinate_format,
            device_readonly=device_readonly,
            force_settings=force_settings,
            id=id,
            latitude=latitude,
            limit_commands=limit_commands,
            longitude=longitude,
            map_=map_,
            map_url=map_url,
            poi_layer=poi_layer,
            readonly=readonly,
            registration=registration,
            twelve_hour_format=twelve_hour_format,
            version=version,
            zoom=zoom,
            request_options=request_options,
        )
        return _response.data


class AsyncServerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawServerClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawServerClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawServerClient
        """
        return self._raw_client

    async def fetch_server_information(self, *, request_options: typing.Optional[RequestOptions] = None) -> Server:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Server
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.server.fetch_server_information()


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_server_information(request_options=request_options)
        return _response.data

    async def update_server_information(
        self,
        *,
        attributes: typing.Optional[ServerAttributes] = OMIT,
        bing_key: typing.Optional[str] = OMIT,
        coordinate_format: typing.Optional[str] = OMIT,
        device_readonly: typing.Optional[bool] = OMIT,
        force_settings: typing.Optional[bool] = OMIT,
        id: typing.Optional[int] = OMIT,
        latitude: typing.Optional[float] = OMIT,
        limit_commands: typing.Optional[bool] = OMIT,
        longitude: typing.Optional[float] = OMIT,
        map_: typing.Optional[str] = OMIT,
        map_url: typing.Optional[str] = OMIT,
        poi_layer: typing.Optional[str] = OMIT,
        readonly: typing.Optional[bool] = OMIT,
        registration: typing.Optional[bool] = OMIT,
        twelve_hour_format: typing.Optional[bool] = OMIT,
        version: typing.Optional[str] = OMIT,
        zoom: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Server:
        """
        Parameters
        ----------
        attributes : typing.Optional[ServerAttributes]

        bing_key : typing.Optional[str]

        coordinate_format : typing.Optional[str]

        device_readonly : typing.Optional[bool]

        force_settings : typing.Optional[bool]

        id : typing.Optional[int]

        latitude : typing.Optional[float]

        limit_commands : typing.Optional[bool]

        longitude : typing.Optional[float]

        map_ : typing.Optional[str]

        map_url : typing.Optional[str]

        poi_layer : typing.Optional[str]

        readonly : typing.Optional[bool]

        registration : typing.Optional[bool]

        twelve_hour_format : typing.Optional[bool]

        version : typing.Optional[str]

        zoom : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Server
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.server.update_server_information()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_server_information(
            attributes=attributes,
            bing_key=bing_key,
            coordinate_format=coordinate_format,
            device_readonly=device_readonly,
            force_settings=force_settings,
            id=id,
            latitude=latitude,
            limit_commands=limit_commands,
            longitude=longitude,
            map_=map_,
            map_url=map_url,
            poi_layer=poi_layer,
            readonly=readonly,
            registration=registration,
            twelve_hour_format=twelve_hour_format,
            version=version,
            zoom=zoom,
            request_options=request_options,
        )
        return _response.data
