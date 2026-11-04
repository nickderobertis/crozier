

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCompatibilityClient, RawCompatibilityClient


class CompatibilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCompatibilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCompatibilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCompatibilityClient
        """
        return self._raw_client

    def compatibility(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.compatibility.compatibility()
        """
        _response = self._raw_client.compatibility(request_options=request_options)
        return _response.data


class AsyncCompatibilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCompatibilityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCompatibilityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCompatibilityClient
        """
        return self._raw_client

    async def compatibility(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.compatibility.compatibility()


        asyncio.run(main())
        """
        _response = await self._raw_client.compatibility(request_options=request_options)
        return _response.data
