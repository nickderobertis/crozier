

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ap_iinfo import ApIinfo
from ..types.api_info import ApiInfo
from ..types.health_info import HealthInfo
from .raw_client import AsyncRawInfoClient, RawInfoClient


class InfoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInfoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInfoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInfoClient
        """
        return self._raw_client

    def get_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiInfo:
        """
        Get the current API version, supported authentication methods and description

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiInfo
            The API information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.info.get_info()
        """
        _response = self._raw_client.get_info(request_options=request_options)
        return _response.data

    def get_open_api(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApIinfo:
        """
        Get the current API documentation as a response with content negotiation.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApIinfo
            The API documentation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.info.get_open_api()
        """
        _response = self._raw_client.get_open_api(request_options=request_options)
        return _response.data

    def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthInfo:
        """
        Check if API is ready to accept requests or not

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthInfo
            The API information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.info.get_health()
        """
        _response = self._raw_client.get_health(request_options=request_options)
        return _response.data

    def get_banner_message(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Returns the Banner message from the server

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Banner message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.info.get_banner_message()
        """
        _response = self._raw_client.get_banner_message(request_options=request_options)
        return _response.data


class AsyncInfoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInfoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInfoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInfoClient
        """
        return self._raw_client

    async def get_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApiInfo:
        """
        Get the current API version, supported authentication methods and description

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiInfo
            The API information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.info.get_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_info(request_options=request_options)
        return _response.data

    async def get_open_api(self, *, request_options: typing.Optional[RequestOptions] = None) -> ApIinfo:
        """
        Get the current API documentation as a response with content negotiation.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApIinfo
            The API documentation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.info.get_open_api()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_open_api(request_options=request_options)
        return _response.data

    async def get_health(self, *, request_options: typing.Optional[RequestOptions] = None) -> HealthInfo:
        """
        Check if API is ready to accept requests or not

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HealthInfo
            The API information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.info.get_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_health(request_options=request_options)
        return _response.data

    async def get_banner_message(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Returns the Banner message from the server

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Banner message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.info.get_banner_message()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_banner_message(request_options=request_options)
        return _response.data
