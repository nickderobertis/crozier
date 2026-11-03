

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawCaptionsClient, RawCaptionsClient

if typing.TYPE_CHECKING:
    from .media.client import AsyncMediaClient, MediaClient


class CaptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCaptionsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._media: typing.Optional[MediaClient] = None

    @property
    def with_raw_response(self) -> RawCaptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCaptionsClient
        """
        return self._raw_client

    @property
    def media(self):
        if self._media is None:
            from .media.client import MediaClient

            self._media = MediaClient(client_wrapper=self._client_wrapper)
        return self._media


class AsyncCaptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCaptionsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._media: typing.Optional[AsyncMediaClient] = None

    @property
    def with_raw_response(self) -> AsyncRawCaptionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCaptionsClient
        """
        return self._raw_client

    @property
    def media(self):
        if self._media is None:
            from .media.client import AsyncMediaClient

            self._media = AsyncMediaClient(client_wrapper=self._client_wrapper)
        return self._media
