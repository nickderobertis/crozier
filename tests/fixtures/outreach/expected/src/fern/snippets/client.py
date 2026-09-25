

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSnippetsClient, RawSnippetsClient
from .types.snippet_create_request_data import SnippetCreateRequestData


OMIT = typing.cast(typing.Any, ...)


class SnippetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSnippetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSnippetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSnippetsClient
        """
        return self._raw_client

    def list_snippets(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

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
        client.snippets.list_snippets()
        """
        _response = self._raw_client.list_snippets(
            page_offset=page_offset, page_limit=page_limit, request_options=request_options
        )
        return _response.data

    def create_snippet(
        self,
        *,
        data: typing.Optional[SnippetCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Optional[SnippetCreateRequestData]

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
        client.snippets.create_snippet()
        """
        _response = self._raw_client.create_snippet(data=data, request_options=request_options)
        return _response.data


class AsyncSnippetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSnippetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSnippetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSnippetsClient
        """
        return self._raw_client

    async def list_snippets(
        self,
        *,
        page_offset: typing.Optional[int] = None,
        page_limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        page_offset : typing.Optional[int]
            Page offset for pagination

        page_limit : typing.Optional[int]
            Page limit for pagination

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
            await client.snippets.list_snippets()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_snippets(
            page_offset=page_offset, page_limit=page_limit, request_options=request_options
        )
        return _response.data

    async def create_snippet(
        self,
        *,
        data: typing.Optional[SnippetCreateRequestData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        data : typing.Optional[SnippetCreateRequestData]

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
            await client.snippets.create_snippet()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_snippet(data=data, request_options=request_options)
        return _response.data
