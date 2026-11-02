

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.woven_pattern import WovenPattern
from .raw_client import AsyncRawPatternsClient, RawPatternsClient


OMIT = typing.cast(typing.Any, ...)


class PatternsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPatternsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPatternsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPatternsClient
        """
        return self._raw_client

    def weave_pattern(
        self,
        *,
        draft: str,
        incremental: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[WovenPattern]:
        """
        Parameters
        ----------
        draft : str
            The weaving draft, one row per line.

        incremental : typing.Optional[bool]
            Report each row as it is woven.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.Iterator[WovenPattern]
            The finished pattern, when weaving all at once.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        response = client.patterns.weave_pattern(
            draft="draft",
        )
        for chunk in response:
            yield chunk
        """
        with self._raw_client.weave_pattern(draft=draft, incremental=incremental, request_options=request_options) as r:
            yield from r.data

    def get_pattern(self, pattern_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> WovenPattern:
        """
        Parameters
        ----------
        pattern_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WovenPattern
            The pattern.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.patterns.get_pattern(
            pattern_id="patternId",
        )
        """
        _response = self._raw_client.get_pattern(pattern_id, request_options=request_options)
        return _response.data


class AsyncPatternsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPatternsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPatternsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPatternsClient
        """
        return self._raw_client

    async def weave_pattern(
        self,
        *,
        draft: str,
        incremental: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[WovenPattern]:
        """
        Parameters
        ----------
        draft : str
            The weaving draft, one row per line.

        incremental : typing.Optional[bool]
            Report each row as it is woven.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Yields
        ------
        typing.AsyncIterator[WovenPattern]
            The finished pattern, when weaving all at once.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            response = client.patterns.weave_pattern(
                draft="draft",
            )
            async for chunk in response:
                yield chunk


        asyncio.run(main())
        """
        async with self._raw_client.weave_pattern(
            draft=draft, incremental=incremental, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_pattern(
        self, pattern_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WovenPattern:
        """
        Parameters
        ----------
        pattern_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WovenPattern
            The pattern.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.patterns.get_pattern(
                pattern_id="patternId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pattern(pattern_id, request_options=request_options)
        return _response.data
