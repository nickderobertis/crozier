

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCacheClient, RawCacheClient


OMIT = typing.cast(typing.Any, ...)


class CacheClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCacheClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCacheClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCacheClient
        """
        return self._raw_client

    def clear_cache(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Clear cache

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
        client.cache.clear_cache()
        """
        _response = self._raw_client.clear_cache(request_options=request_options)
        return _response.data

    def clear_tokens_cache(
        self, *, tokens: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Clear tokens cache

        Parameters
        ----------
        tokens : typing.Sequence[str]

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
        client.cache.clear_tokens_cache(
            tokens=["bed5d31217596118fb297fd84bf3bd3a"],
        )
        """
        _response = self._raw_client.clear_tokens_cache(tokens=tokens, request_options=request_options)
        return _response.data


class AsyncCacheClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCacheClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCacheClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCacheClient
        """
        return self._raw_client

    async def clear_cache(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Clear cache

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
            await client.cache.clear_cache()


        asyncio.run(main())
        """
        _response = await self._raw_client.clear_cache(request_options=request_options)
        return _response.data

    async def clear_tokens_cache(
        self, *, tokens: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Clear tokens cache

        Parameters
        ----------
        tokens : typing.Sequence[str]

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
            await client.cache.clear_tokens_cache(
                tokens=["bed5d31217596118fb297fd84bf3bd3a"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.clear_tokens_cache(tokens=tokens, request_options=request_options)
        return _response.data
