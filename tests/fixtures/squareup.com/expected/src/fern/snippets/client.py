

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delete_snippet_response import DeleteSnippetResponse
from ..types.retrieve_snippet_response import RetrieveSnippetResponse
from ..types.snippet import Snippet
from ..types.upsert_snippet_response import UpsertSnippetResponse
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

    def retrieve_snippet(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveSnippetResponse:
        """
        Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.

        You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site that contains the snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveSnippetResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.snippets.retrieve_snippet(
            site_id="site_id",
        )
        """
        _response = self._raw_client.retrieve_snippet(site_id, request_options=request_options)
        return _response.data

    def upsert_snippet(
        self, site_id: str, *, snippet: Snippet, request_options: typing.Optional[RequestOptions] = None
    ) -> UpsertSnippetResponse:
        """
        Adds a snippet to a Square Online site or updates the existing snippet on the site.
        The snippet code is appended to the end of the `head` element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site.

        You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site where you want to add or update the snippet.

        snippet : Snippet

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertSnippetResponse
            Success

        Examples
        --------
        from fern import FernApi, Snippet

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.snippets.upsert_snippet(
            site_id="site_id",
            snippet=Snippet(
                content="content",
            ),
        )
        """
        _response = self._raw_client.upsert_snippet(site_id, snippet=snippet, request_options=request_options)
        return _response.data

    def delete_snippet(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSnippetResponse:
        """
        Removes your snippet from a Square Online site.

        You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site that contains the snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSnippetResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.snippets.delete_snippet(
            site_id="site_id",
        )
        """
        _response = self._raw_client.delete_snippet(site_id, request_options=request_options)
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

    async def retrieve_snippet(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RetrieveSnippetResponse:
        """
        Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.

        You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site that contains the snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RetrieveSnippetResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.snippets.retrieve_snippet(
                site_id="site_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_snippet(site_id, request_options=request_options)
        return _response.data

    async def upsert_snippet(
        self, site_id: str, *, snippet: Snippet, request_options: typing.Optional[RequestOptions] = None
    ) -> UpsertSnippetResponse:
        """
        Adds a snippet to a Square Online site or updates the existing snippet on the site.
        The snippet code is appended to the end of the `head` element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site.

        You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site where you want to add or update the snippet.

        snippet : Snippet

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpsertSnippetResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Snippet

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.snippets.upsert_snippet(
                site_id="site_id",
                snippet=Snippet(
                    content="content",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upsert_snippet(site_id, snippet=snippet, request_options=request_options)
        return _response.data

    async def delete_snippet(
        self, site_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSnippetResponse:
        """
        Removes your snippet from a Square Online site.

        You can call [ListSites](https://developer.squareup.com/reference/square_2021-08-18/sites-api/list-sites) to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

        Parameters
        ----------
        site_id : str
            The ID of the site that contains the snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSnippetResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.snippets.delete_snippet(
                site_id="site_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_snippet(site_id, request_options=request_options)
        return _response.data
