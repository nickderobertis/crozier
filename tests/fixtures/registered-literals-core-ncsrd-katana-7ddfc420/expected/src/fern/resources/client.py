

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.resources import Resources
from .raw_client import AsyncRawResourcesClient, RawResourcesClient


class ResourcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawResourcesClient
        """
        return self._raw_client

    def returns_information_about_the_platform_resources(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Resources:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Resources
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.resources.returns_information_about_the_platform_resources()
        """
        _response = self._raw_client.returns_information_about_the_platform_resources(request_options=request_options)
        return _response.data

    def returns_information_about_the_platform_resources_on_the_specified_location(
        self, location: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Resources:
        """
        Parameters
        ----------
        location : str
            Specific location of the platform

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Resources
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.resources.returns_information_about_the_platform_resources_on_the_specified_location(
            location="location",
        )
        """
        _response = self._raw_client.returns_information_about_the_platform_resources_on_the_specified_location(
            location, request_options=request_options
        )
        return _response.data


class AsyncResourcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawResourcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawResourcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawResourcesClient
        """
        return self._raw_client

    async def returns_information_about_the_platform_resources(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Resources:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Resources
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.resources.returns_information_about_the_platform_resources()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_information_about_the_platform_resources(
            request_options=request_options
        )
        return _response.data

    async def returns_information_about_the_platform_resources_on_the_specified_location(
        self, location: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Resources:
        """
        Parameters
        ----------
        location : str
            Specific location of the platform

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Resources
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.resources.returns_information_about_the_platform_resources_on_the_specified_location(
                location="location",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_information_about_the_platform_resources_on_the_specified_location(
            location, request_options=request_options
        )
        return _response.data
