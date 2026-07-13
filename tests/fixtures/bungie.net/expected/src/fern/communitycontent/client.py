

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCommunitycontentClient, RawCommunitycontentClient
from .types.community_content_get_community_content_response import CommunityContentGetCommunityContentResponse


class CommunitycontentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCommunitycontentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCommunitycontentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCommunitycontentClient
        """
        return self._raw_client

    def getcommunitycontent(
        self, sort: int, media_filter: int, page: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommunityContentGetCommunityContentResponse:
        """
        Returns community content.

        Parameters
        ----------
        sort : int
            The sort mode.

        media_filter : int
            The type of media to get

        page : int
            Zero based page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommunityContentGetCommunityContentResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.communitycontent.getcommunitycontent(
            sort=1,
            media_filter=1,
            page=1,
        )
        """
        _response = self._raw_client.getcommunitycontent(sort, media_filter, page, request_options=request_options)
        return _response.data


class AsyncCommunitycontentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCommunitycontentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCommunitycontentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCommunitycontentClient
        """
        return self._raw_client

    async def getcommunitycontent(
        self, sort: int, media_filter: int, page: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CommunityContentGetCommunityContentResponse:
        """
        Returns community content.

        Parameters
        ----------
        sort : int
            The sort mode.

        media_filter : int
            The type of media to get

        page : int
            Zero based page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CommunityContentGetCommunityContentResponse
            Look at the Response property for more information about the nature of this response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.communitycontent.getcommunitycontent(
                sort=1,
                media_filter=1,
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcommunitycontent(
            sort, media_filter, page, request_options=request_options
        )
        return _response.data
