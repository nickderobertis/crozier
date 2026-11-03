

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawDepotsClient, RawDepotsClient

if typing.TYPE_CHECKING:
    from .sacks.client import AsyncSacksClient, SacksClient


class DepotsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDepotsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._sacks: typing.Optional[SacksClient] = None

    @property
    def with_raw_response(self) -> RawDepotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDepotsClient
        """
        return self._raw_client

    @property
    def sacks(self):
        if self._sacks is None:
            from .sacks.client import SacksClient

            self._sacks = SacksClient(client_wrapper=self._client_wrapper)
        return self._sacks


class AsyncDepotsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDepotsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._sacks: typing.Optional[AsyncSacksClient] = None

    @property
    def with_raw_response(self) -> AsyncRawDepotsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDepotsClient
        """
        return self._raw_client

    @property
    def sacks(self):
        if self._sacks is None:
            from .sacks.client import AsyncSacksClient

            self._sacks = AsyncSacksClient(client_wrapper=self._client_wrapper)
        return self._sacks
