

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.episode_detail_response import EpisodeDetailResponse
from .raw_client import AsyncRawEpisodesClient, RawEpisodesClient


class EpisodesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEpisodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEpisodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEpisodesClient
        """
        return self._raw_client

    def get_episode(
        self, episode_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EpisodeDetailResponse:
        """
        Parameters
        ----------
        episode_id : int
            Episode numeric id, as observed in live Kodi API responses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EpisodeDetailResponse
            Episode playback detail.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.episodes.get_episode(
            episode_id=1,
        )
        """
        _response = self._raw_client.get_episode(episode_id, request_options=request_options)
        return _response.data


class AsyncEpisodesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEpisodesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEpisodesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEpisodesClient
        """
        return self._raw_client

    async def get_episode(
        self, episode_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EpisodeDetailResponse:
        """
        Parameters
        ----------
        episode_id : int
            Episode numeric id, as observed in live Kodi API responses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EpisodeDetailResponse
            Episode playback detail.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.episodes.get_episode(
                episode_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_episode(episode_id, request_options=request_options)
        return _response.data
