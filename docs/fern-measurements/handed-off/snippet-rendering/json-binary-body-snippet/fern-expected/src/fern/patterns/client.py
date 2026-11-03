

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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

    def replace_draft(
        self, pattern_id: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        pattern_id : str

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.patterns.replace_draft(
            pattern_id="patternId",
            request="string",
        )
        """
        _response = self._raw_client.replace_draft(pattern_id, request=request, request_options=request_options)
        return _response.data

    def replace_chart(
        self, pattern_id: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        pattern_id : str

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.patterns.replace_chart(
            pattern_id="patternId",
            request="string",
        )
        """
        _response = self._raw_client.replace_chart(pattern_id, request=request, request_options=request_options)
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

    async def replace_draft(
        self, pattern_id: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        pattern_id : str

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.patterns.replace_draft(
                pattern_id="patternId",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_draft(pattern_id, request=request, request_options=request_options)
        return _response.data

    async def replace_chart(
        self, pattern_id: str, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        pattern_id : str

        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.patterns.replace_chart(
                pattern_id="patternId",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.replace_chart(pattern_id, request=request, request_options=request_options)
        return _response.data
