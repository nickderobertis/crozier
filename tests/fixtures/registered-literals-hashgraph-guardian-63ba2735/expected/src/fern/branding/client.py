

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawBrandingClient, RawBrandingClient


class BrandingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBrandingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawBrandingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBrandingClient
        """
        return self._raw_client

    def branding_api_get_branding(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.branding.branding_api_get_branding()
        """
        _response = self._raw_client.branding_api_get_branding(request_options=request_options)
        return _response.data

    def branding_api_set_branding(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.branding.branding_api_set_branding()
        """
        _response = self._raw_client.branding_api_set_branding(request_options=request_options)
        return _response.data


class AsyncBrandingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBrandingClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawBrandingClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBrandingClient
        """
        return self._raw_client

    async def branding_api_get_branding(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.branding.branding_api_get_branding()


        asyncio.run(main())
        """
        _response = await self._raw_client.branding_api_get_branding(request_options=request_options)
        return _response.data

    async def branding_api_set_branding(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.branding.branding_api_set_branding()


        asyncio.run(main())
        """
        _response = await self._raw_client.branding_api_set_branding(request_options=request_options)
        return _response.data
