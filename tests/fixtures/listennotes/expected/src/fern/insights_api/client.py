

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.podcast_audience_response import PodcastAudienceResponse
from ..types.podcast_domain_response import PodcastDomainResponse
from .raw_client import AsyncRawInsightsApiClient, RawInsightsApiClient


class InsightsApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInsightsApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInsightsApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInsightsApiClient
        """
        return self._raw_client

    def get_podcasts_by_domain_name(
        self,
        domain_name: str,
        *,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PodcastDomainResponse:
        """
        Fetch podcasts by a publisher's domain name, e.g., nytimes.com, wondery.com, npr.org...
        Each request will return up to 10 podcasts. You can use the `page` parameter to paginate.

        Parameters
        ----------
        domain_name : str
            A publisher's domain name, e.g., nytimes.com, wondery.com, npr.org...

        page : typing.Optional[int]
            Page number of the podcasts from this domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PodcastDomainResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.insights_api.get_podcasts_by_domain_name(
            domain_name="nytimes.com",
            page=1,
        )
        """
        _response = self._raw_client.get_podcasts_by_domain_name(
            domain_name, page=page, request_options=request_options
        )
        return _response.data

    def get_podcast_audience(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PodcastAudienceResponse:
        """
        Fetch audience demographics for a podcast - 1) directly measured on the Listen Notes platform; 2) only supports audience breakdown by regions for now; 3) not every podcast has data.

        Parameters
        ----------
        id : str
            Podcast id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PodcastAudienceResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )
        client.insights_api.get_podcast_audience(
            id="25212ac3c53240a880dd5032e547047b",
        )
        """
        _response = self._raw_client.get_podcast_audience(id, request_options=request_options)
        return _response.data


class AsyncInsightsApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInsightsApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInsightsApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInsightsApiClient
        """
        return self._raw_client

    async def get_podcasts_by_domain_name(
        self,
        domain_name: str,
        *,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PodcastDomainResponse:
        """
        Fetch podcasts by a publisher's domain name, e.g., nytimes.com, wondery.com, npr.org...
        Each request will return up to 10 podcasts. You can use the `page` parameter to paginate.

        Parameters
        ----------
        domain_name : str
            A publisher's domain name, e.g., nytimes.com, wondery.com, npr.org...

        page : typing.Optional[int]
            Page number of the podcasts from this domain name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PodcastDomainResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.insights_api.get_podcasts_by_domain_name(
                domain_name="nytimes.com",
                page=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_podcasts_by_domain_name(
            domain_name, page=page, request_options=request_options
        )
        return _response.data

    async def get_podcast_audience(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PodcastAudienceResponse:
        """
        Fetch audience demographics for a podcast - 1) directly measured on the Listen Notes platform; 2) only supports audience breakdown by regions for now; 3) not every podcast has data.

        Parameters
        ----------
        id : str
            Podcast id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PodcastAudienceResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            listen_api_key="YOUR_LISTEN_API_KEY",
        )


        async def main() -> None:
            await client.insights_api.get_podcast_audience(
                id="25212ac3c53240a880dd5032e547047b",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_podcast_audience(id, request_options=request_options)
        return _response.data
