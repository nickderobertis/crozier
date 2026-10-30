

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTrackMetadataClient, RawTrackMetadataClient


class TrackMetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTrackMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTrackMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTrackMetadataClient
        """
        return self._raw_client

    def get_meta_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        JSON Response
        {
         "metaData": {
          "album": "Country Heat",
          "title": "Old Dirt Roads",
          "subtitle": "",
          "artist": "Owen Riegling",
          "albumArtURI ": "https://m.media-amazon.com/images/I/51iU0odzJwL.jpg",
          "sampleRate ": "44100",
          "bitDepth": "16",
          "bitRate": "63",
          "trackId": "s6707",
         }
        }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.track_metadata.get_meta_info()
        """
        _response = self._raw_client.get_meta_info(request_options=request_options)
        return _response.data


class AsyncTrackMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTrackMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTrackMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTrackMetadataClient
        """
        return self._raw_client

    async def get_meta_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        JSON Response
        {
         "metaData": {
          "album": "Country Heat",
          "title": "Old Dirt Roads",
          "subtitle": "",
          "artist": "Owen Riegling",
          "albumArtURI ": "https://m.media-amazon.com/images/I/51iU0odzJwL.jpg",
          "sampleRate ": "44100",
          "bitDepth": "16",
          "bitRate": "63",
          "trackId": "s6707",
         }
        }

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.track_metadata.get_meta_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_meta_info(request_options=request_options)
        return _response.data
