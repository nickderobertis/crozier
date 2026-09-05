

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.endpoint_get_markdown_emoticons import EndpointGetMarkdownEmoticons
from ..types.endpoint_post_markdown import EndpointPostMarkdown
from .raw_client import AsyncRawMarkdownClient, RawMarkdownClient


OMIT = typing.cast(typing.Any, ...)


class MarkdownClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMarkdownClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMarkdownClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMarkdownClient
        """
        return self._raw_client

    def post_markdown(
        self,
        *,
        text_raw: str,
        text_emoticons: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostMarkdown:
        """
        Parameters
        ----------
        text_raw : str

        text_emoticons : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostMarkdown
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.markdown.post_markdown(
            text_raw="text_raw",
        )
        """
        _response = self._raw_client.post_markdown(
            text_raw=text_raw, text_emoticons=text_emoticons, request_options=request_options
        )
        return _response.data

    def get_markdown_emoticons(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetMarkdownEmoticons:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetMarkdownEmoticons
            Valid Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.markdown.get_markdown_emoticons()
        """
        _response = self._raw_client.get_markdown_emoticons(request_options=request_options)
        return _response.data


class AsyncMarkdownClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMarkdownClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMarkdownClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMarkdownClient
        """
        return self._raw_client

    async def post_markdown(
        self,
        *,
        text_raw: str,
        text_emoticons: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EndpointPostMarkdown:
        """
        Parameters
        ----------
        text_raw : str

        text_emoticons : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointPostMarkdown
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.markdown.post_markdown(
                text_raw="text_raw",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_markdown(
            text_raw=text_raw, text_emoticons=text_emoticons, request_options=request_options
        )
        return _response.data

    async def get_markdown_emoticons(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EndpointGetMarkdownEmoticons:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EndpointGetMarkdownEmoticons
            Valid Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.markdown.get_markdown_emoticons()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_markdown_emoticons(request_options=request_options)
        return _response.data
