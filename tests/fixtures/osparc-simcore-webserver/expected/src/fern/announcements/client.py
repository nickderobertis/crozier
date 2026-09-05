

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_list_announcement import EnvelopeListAnnouncement
from .raw_client import AsyncRawAnnouncementsClient, RawAnnouncementsClient


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

    def list_announcements(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListAnnouncement:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListAnnouncement
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.announcements.list_announcements()
        """
        _response = self._raw_client.list_announcements(request_options=request_options)
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

    async def list_announcements(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListAnnouncement:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListAnnouncement
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.announcements.list_announcements()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_announcements(request_options=request_options)
        return _response.data
