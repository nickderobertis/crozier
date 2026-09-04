

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawCatalogClient, RawCatalogClient

if typing.TYPE_CHECKING:
    from .widgets.client import AsyncWidgetsClient, WidgetsClient


class CatalogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCatalogClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._widgets: typing.Optional[WidgetsClient] = None

    @property
    def with_raw_response(self) -> RawCatalogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCatalogClient
        """
        return self._raw_client

    @property
    def widgets(self):
        if self._widgets is None:
            from .widgets.client import WidgetsClient

            self._widgets = WidgetsClient(client_wrapper=self._client_wrapper)
        return self._widgets


class AsyncCatalogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCatalogClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._widgets: typing.Optional[AsyncWidgetsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawCatalogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCatalogClient
        """
        return self._raw_client

    @property
    def widgets(self):
        if self._widgets is None:
            from .widgets.client import AsyncWidgetsClient

            self._widgets = AsyncWidgetsClient(client_wrapper=self._client_wrapper)
        return self._widgets
