

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.method import Method
from .raw_client import AsyncRawPealsClient, RawPealsClient


OMIT = typing.cast(typing.Any, ...)


class PealsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPealsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPealsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPealsClient
        """
        return self._raw_client

    def ring_peal(self, *, request: Method, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : Method

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.peals.ring_peal(
            request="grandsire",
        )
        """
        _response = self._raw_client.ring_peal(request=request, request_options=request_options)
        return _response.data


class AsyncPealsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPealsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPealsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPealsClient
        """
        return self._raw_client

    async def ring_peal(self, *, request: Method, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request : Method

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.peals.ring_peal(
                request="grandsire",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ring_peal(request=request, request_options=request_options)
        return _response.data
