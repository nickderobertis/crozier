

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.json_feed_dto import JsonFeedDto
from .raw_client import AsyncRawAnnouncementsClient, RawAnnouncementsClient


OMIT = typing.cast(typing.Any, ...)


class AnnouncementsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnnouncementsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAnnouncementsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnnouncementsClient
        """
        return self._raw_client

    def get_announcements(self, *, request_options: typing.Optional[RequestOptions] = None) -> JsonFeedDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonFeedDto
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.announcements.get_announcements()
        """
        _response = self._raw_client.get_announcements(request_options=request_options)
        return _response.data

    def mark_announcements_read(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.announcements.mark_announcements_read(
            request=["string"],
        )
        """
        _response = self._raw_client.mark_announcements_read(request=request, request_options=request_options)
        return _response.data


class AsyncAnnouncementsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnnouncementsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAnnouncementsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnnouncementsClient
        """
        return self._raw_client

    async def get_announcements(self, *, request_options: typing.Optional[RequestOptions] = None) -> JsonFeedDto:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JsonFeedDto
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.announcements.get_announcements()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_announcements(request_options=request_options)
        return _response.data

    async def mark_announcements_read(
        self, *, request: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Required role: **ADMIN**

        Parameters
        ----------
        request : typing.Sequence[str]

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.announcements.mark_announcements_read(
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_announcements_read(request=request, request_options=request_options)
        return _response.data
