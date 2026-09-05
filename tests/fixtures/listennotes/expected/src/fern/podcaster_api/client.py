

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delete_podcast_response import DeletePodcastResponse
from ..types.submit_podcast_response import SubmitPodcastResponse
from .raw_client import AsyncRawPodcasterApiClient, RawPodcasterApiClient


OMIT = typing.cast(typing.Any, ...)


class PodcasterApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPodcasterApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPodcasterApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPodcasterApiClient
        """
        return self._raw_client

    def submit_podcast(
        self, *, rss: str, email: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SubmitPodcastResponse:
        """
        Podcast hosting services can use this endpoint to help your users directly submit a new podcast to Listen Notes database. If the podcast doesn't exist in the database, "status" in the response will be "in review", and we'll review it within 12 hours. If the podcast exists, "status" in the response will be "found". If this submission is rejected, "status" in the response will be "rejected". You can use `POST /podcasts` to check if multiple podcasts exist in the database. If you want to get a notification once the podcast is accepted, you can either specify the "email" parameter or configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks

        Parameters
        ----------
        rss : str
            A valid podcast rss url.

        email : typing.Optional[str]
            A valid email address. If **email** is specified, then we'll notify this email address once the podcast is accepted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubmitPodcastResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.podcaster_api.submit_podcast(
            rss="https://feeds.megaphone.fm/committed",
        )
        """
        _response = self._raw_client.submit_podcast(rss=rss, email=email, request_options=request_options)
        return _response.data

    def delete_podcast_by_id(
        self, id: str, *, reason: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePodcastResponse:
        """
        Podcast hosting services can use this endpoint to streamline the process of podcast deletion on behave of their users (podcasters). We will review the deletion request within 12 hours. If the podcast is already deleted, the "status" field in the response will be "deleted". Otherwise, the status field will be "in review". If you want to get a notification once the podcast is deleted, you can configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks

        Parameters
        ----------
        id : str
            Podcast id. You can get podcast id from using other endpoints, e.g., `GET /search`, `GET /best_podcasts`...

        reason : typing.Optional[str]
            The reason why this podcast should be deleted, e.g., copyright violation, the podcaster wants to delete it... You can put "testing" here to indicate that you are testing this endpoint, so we will not actually delete the podcast.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePodcastResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.podcaster_api.delete_podcast_by_id(
            id="4d3fe717742d4963a85562e9f84d8c79",
            reason="the podcaster wants to delete it",
        )
        """
        _response = self._raw_client.delete_podcast_by_id(id, reason=reason, request_options=request_options)
        return _response.data


class AsyncPodcasterApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPodcasterApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPodcasterApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPodcasterApiClient
        """
        return self._raw_client

    async def submit_podcast(
        self, *, rss: str, email: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SubmitPodcastResponse:
        """
        Podcast hosting services can use this endpoint to help your users directly submit a new podcast to Listen Notes database. If the podcast doesn't exist in the database, "status" in the response will be "in review", and we'll review it within 12 hours. If the podcast exists, "status" in the response will be "found". If this submission is rejected, "status" in the response will be "rejected". You can use `POST /podcasts` to check if multiple podcasts exist in the database. If you want to get a notification once the podcast is accepted, you can either specify the "email" parameter or configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks

        Parameters
        ----------
        rss : str
            A valid podcast rss url.

        email : typing.Optional[str]
            A valid email address. If **email** is specified, then we'll notify this email address once the podcast is accepted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubmitPodcastResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.podcaster_api.submit_podcast(
                rss="https://feeds.megaphone.fm/committed",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_podcast(rss=rss, email=email, request_options=request_options)
        return _response.data

    async def delete_podcast_by_id(
        self, id: str, *, reason: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePodcastResponse:
        """
        Podcast hosting services can use this endpoint to streamline the process of podcast deletion on behave of their users (podcasters). We will review the deletion request within 12 hours. If the podcast is already deleted, the "status" field in the response will be "deleted". Otherwise, the status field will be "in review". If you want to get a notification once the podcast is deleted, you can configure a webhook url in the dashboard: listennotes.com/api/dashboard/#webhooks

        Parameters
        ----------
        id : str
            Podcast id. You can get podcast id from using other endpoints, e.g., `GET /search`, `GET /best_podcasts`...

        reason : typing.Optional[str]
            The reason why this podcast should be deleted, e.g., copyright violation, the podcaster wants to delete it... You can put "testing" here to indicate that you are testing this endpoint, so we will not actually delete the podcast.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePodcastResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.podcaster_api.delete_podcast_by_id(
                id="4d3fe717742d4963a85562e9f84d8c79",
                reason="the podcaster wants to delete it",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_podcast_by_id(id, reason=reason, request_options=request_options)
        return _response.data
