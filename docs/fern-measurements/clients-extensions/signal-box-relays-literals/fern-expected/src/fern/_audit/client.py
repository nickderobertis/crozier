

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawAuditClient, RawAuditClient

if typing.TYPE_CHECKING:
    from ._trail.client import AsyncTrailClient, TrailClient


class AuditClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuditClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self.__trail: typing.Optional[TrailClient] = None

    @property
    def with_raw_response(self) -> RawAuditClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuditClient
        """
        return self._raw_client

    @property
    def _trail(self):
        if self.__trail is None:
            from ._trail.client import TrailClient

            self.__trail = TrailClient(client_wrapper=self._client_wrapper)
        return self.__trail


class AsyncAuditClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuditClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self.__trail: typing.Optional[AsyncTrailClient] = None

    @property
    def with_raw_response(self) -> AsyncRawAuditClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuditClient
        """
        return self._raw_client

    @property
    def _trail(self):
        if self.__trail is None:
            from ._trail.client import AsyncTrailClient

            self.__trail = AsyncTrailClient(client_wrapper=self._client_wrapper)
        return self.__trail
