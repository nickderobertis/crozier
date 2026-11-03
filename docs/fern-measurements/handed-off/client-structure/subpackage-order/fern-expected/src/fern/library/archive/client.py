

from __future__ import annotations

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawArchiveClient, RawArchiveClient

if typing.TYPE_CHECKING:
    from .boxes.client import AsyncBoxesClient, BoxesClient


class ArchiveClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArchiveClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._boxes: typing.Optional[BoxesClient] = None

    @property
    def with_raw_response(self) -> RawArchiveClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArchiveClient
        """
        return self._raw_client

    @property
    def boxes(self):
        if self._boxes is None:
            from .boxes.client import BoxesClient

            self._boxes = BoxesClient(client_wrapper=self._client_wrapper)
        return self._boxes


class AsyncArchiveClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArchiveClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._boxes: typing.Optional[AsyncBoxesClient] = None

    @property
    def with_raw_response(self) -> AsyncRawArchiveClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArchiveClient
        """
        return self._raw_client

    @property
    def boxes(self):
        if self._boxes is None:
            from .boxes.client import AsyncBoxesClient

            self._boxes = AsyncBoxesClient(client_wrapper=self._client_wrapper)
        return self._boxes
