

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.types_weather_report import TypesWeatherReport
from .raw_client import AsyncRawEndpointsEnumClient, RawEndpointsEnumClient


OMIT = typing.cast(typing.Any, ...)


class EndpointsEnumClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEndpointsEnumClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEndpointsEnumClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEndpointsEnumClient
        """
        return self._raw_client

    def endpoints_enum_get_and_return_enum(
        self, *, request: TypesWeatherReport, request_options: typing.Optional[RequestOptions] = None
    ) -> TypesWeatherReport:
        """
        Parameters
        ----------
        request : TypesWeatherReport

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TypesWeatherReport


        Examples
        --------
        from fern import FernApi, TypesWeatherReport

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.endpoints_enum.endpoints_enum_get_and_return_enum(
            request=TypesWeatherReport.SUNNY,
        )
        """
        _response = self._raw_client.endpoints_enum_get_and_return_enum(
            request=request, request_options=request_options
        )
        return _response.data


class AsyncEndpointsEnumClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEndpointsEnumClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEndpointsEnumClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEndpointsEnumClient
        """
        return self._raw_client

    async def endpoints_enum_get_and_return_enum(
        self, *, request: TypesWeatherReport, request_options: typing.Optional[RequestOptions] = None
    ) -> TypesWeatherReport:
        """
        Parameters
        ----------
        request : TypesWeatherReport

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TypesWeatherReport


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, TypesWeatherReport

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.endpoints_enum.endpoints_enum_get_and_return_enum(
                request=TypesWeatherReport.SUNNY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.endpoints_enum_get_and_return_enum(
            request=request, request_options=request_options
        )
        return _response.data
