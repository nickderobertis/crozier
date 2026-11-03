

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.snippet import Snippet
from .raw_client import AsyncRawSnippetsClient, RawSnippetsClient


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

    def create_snippet(
        self, space: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> Snippet:
        """
        Parameters
        ----------
        space : str

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snippet
            The stored snippet.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.snippets.create_snippet(
            space="space",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_snippet(space, request=request, request_options=request_options)
        return _response.data

    def create_snippets(
        self,
        space: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Snippet]:
        """
        Parameters
        ----------
        space : str

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Snippet]
            The stored snippets.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.snippets.create_snippets(
            space="space",
            request=[],
        )
        """
        _response = self._raw_client.create_snippets(space, request=request, request_options=request_options)
        return _response.data

    def get_snippet(
        self, space: str, snippet_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Snippet:
        """
        Parameters
        ----------
        space : str

        snippet_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snippet
            One snippet.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.snippets.get_snippet(
            space="space",
            snippet_id="snippetId",
        )
        """
        _response = self._raw_client.get_snippet(space, snippet_id, request_options=request_options)
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

    async def create_snippet(
        self, space: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> Snippet:
        """
        Parameters
        ----------
        space : str

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snippet
            The stored snippet.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.snippets.create_snippet(
                space="space",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_snippet(space, request=request, request_options=request_options)
        return _response.data

    async def create_snippets(
        self,
        space: str,
        *,
        request: typing.Sequence[typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Snippet]:
        """
        Parameters
        ----------
        space : str

        request : typing.Sequence[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Snippet]
            The stored snippets.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.snippets.create_snippets(
                space="space",
                request=[],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_snippets(space, request=request, request_options=request_options)
        return _response.data

    async def get_snippet(
        self, space: str, snippet_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Snippet:
        """
        Parameters
        ----------
        space : str

        snippet_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snippet
            One snippet.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.snippets.get_snippet(
                space="space",
                snippet_id="snippetId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_snippet(space, snippet_id, request_options=request_options)
        return _response.data
