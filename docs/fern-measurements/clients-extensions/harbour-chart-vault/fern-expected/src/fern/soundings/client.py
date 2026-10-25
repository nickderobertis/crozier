

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSoundingsClient, RawSoundingsClient


class SoundingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSoundingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSoundingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSoundingsClient
        """
        return self._raw_client

    def export_soundings(
        self, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Exports one survey's raw soundings.
        
        Survey logs are archived under G:\\
        
        Parameters
        ----------
        survey_id : str
            The survey whose soundings to export.
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
        
        Returns
        -------
        typing.Iterator[bytes]
            The raw soundings.
        """
        with self._raw_client.export_soundings(survey_id, request_options=request_options) as r:
            yield from r.data


class AsyncSoundingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSoundingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSoundingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSoundingsClient
        """
        return self._raw_client

    async def export_soundings(
        self, survey_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Exports one survey's raw soundings.
        
        Survey logs are archived under G:\\
        
        Parameters
        ----------
        survey_id : str
            The survey whose soundings to export.
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
        
        Returns
        -------
        typing.AsyncIterator[bytes]
            The raw soundings.
        """
        async with self._raw_client.export_soundings(survey_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
