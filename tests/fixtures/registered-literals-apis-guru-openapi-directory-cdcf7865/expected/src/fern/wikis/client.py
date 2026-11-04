

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWikisClient, RawWikisClient
from .types.wiki_read_response import WikiReadResponse


class WikisClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWikisClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWikisClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWikisClient
        """
        return self._raw_client

    def wiki_read(self, wiki_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> WikiReadResponse:
        """
        Retrieves the details about a specific wiki.
        A wiki is a collection of markdown text pages that can be used to describe the project or dataset of contained in the attached node.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested wiki, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        wiki_id : str
            The unique identifier of the wiki.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WikiReadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wikis.wiki_read(
            wiki_id="wiki_id",
        )
        """
        _response = self._raw_client.wiki_read(wiki_id, request_options=request_options)
        return _response.data

    def wiki_content(self, wiki_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Retrieves the plaintext content of a wiki in markdown format.
        #### Returns
        Returns `text/markdown` of the wiki content itself.
        If the request is unsuccessful, plaintext with the error message will be displayed.

        Parameters
        ----------
        wiki_id : str
            The unique identifier of the wiki.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.wikis.wiki_content(
            wiki_id="wiki_id",
        )
        """
        _response = self._raw_client.wiki_content(wiki_id, request_options=request_options)
        return _response.data


class AsyncWikisClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWikisClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWikisClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWikisClient
        """
        return self._raw_client

    async def wiki_read(
        self, wiki_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WikiReadResponse:
        """
        Retrieves the details about a specific wiki.
        A wiki is a collection of markdown text pages that can be used to describe the project or dataset of contained in the attached node.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested wiki, if the request was successful.

        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        wiki_id : str
            The unique identifier of the wiki.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WikiReadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.wikis.wiki_read(
                wiki_id="wiki_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wiki_read(wiki_id, request_options=request_options)
        return _response.data

    async def wiki_content(self, wiki_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Retrieves the plaintext content of a wiki in markdown format.
        #### Returns
        Returns `text/markdown` of the wiki content itself.
        If the request is unsuccessful, plaintext with the error message will be displayed.

        Parameters
        ----------
        wiki_id : str
            The unique identifier of the wiki.

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
            await client.wikis.wiki_content(
                wiki_id="wiki_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wiki_content(wiki_id, request_options=request_options)
        return _response.data
