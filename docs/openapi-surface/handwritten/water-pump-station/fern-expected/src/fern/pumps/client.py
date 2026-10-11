

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawPumpsClient, RawPumpsClient

if typing.TYPE_CHECKING:
    from .servicing.client import AsyncServicingClient, ServicingClient


class PumpsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPumpsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._servicing: typing.Optional[ServicingClient] = None

    @property
    def with_raw_response(self) -> RawPumpsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPumpsClient
        """
        return self._raw_client

    @property
    def servicing(self):
        if self._servicing is None:
            from .servicing.client import ServicingClient

            self._servicing = ServicingClient(client_wrapper=self._client_wrapper)
        return self._servicing


class AsyncPumpsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPumpsClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._servicing: typing.Optional[AsyncServicingClient] = None

    @property
    def with_raw_response(self) -> AsyncRawPumpsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPumpsClient
        """
        return self._raw_client

    @property
    def servicing(self):
        if self._servicing is None:
            from .servicing.client import AsyncServicingClient

            self._servicing = AsyncServicingClient(client_wrapper=self._client_wrapper)
        return self._servicing
