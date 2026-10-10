

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper


class RawBeaconClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper


class AsyncRawBeaconClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
