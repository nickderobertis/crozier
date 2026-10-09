

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawBeaconClient, RawBeaconClient

if typing.TYPE_CHECKING:
    from .api.client import ApiClient, AsyncApiClient


class BeaconClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawBeaconClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._api: typing.Optional[ApiClient] = None

    @property
    def with_raw_response(self) -> RawBeaconClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawBeaconClient
        """
        return self._raw_client

    @property
    def api(self):
        if self._api is None:
            from .api.client import ApiClient

            self._api = ApiClient(client_wrapper=self._client_wrapper)
        return self._api


class AsyncBeaconClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawBeaconClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._api: typing.Optional[AsyncApiClient] = None

    @property
    def with_raw_response(self) -> AsyncRawBeaconClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawBeaconClient
        """
        return self._raw_client

    @property
    def api(self):
        if self._api is None:
            from .api.client import AsyncApiClient

            self._api = AsyncApiClient(client_wrapper=self._client_wrapper)
        return self._api
