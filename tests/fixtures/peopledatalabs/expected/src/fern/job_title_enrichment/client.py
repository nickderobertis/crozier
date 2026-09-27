

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_title import JobTitle
from .raw_client import AsyncRawJobTitleEnrichmentClient, RawJobTitleEnrichmentClient


OMIT = typing.cast(typing.Any, ...)


class JobTitleEnrichmentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobTitleEnrichmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobTitleEnrichmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobTitleEnrichmentClient
        """
        return self._raw_client

    def job_title_enrich(
        self,
        *,
        job_title: typing.Optional[str] = OMIT,
        titlecase: typing.Optional[bool] = OMIT,
        pretty: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobTitle:
        """
        Parameters
        ----------
        job_title : typing.Optional[str]
            Job title that will be enriched

        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase any records returned

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobTitle
            Job Title enrich completed.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.job_title_enrichment.job_title_enrich()
        """
        _response = self._raw_client.job_title_enrich(
            job_title=job_title, titlecase=titlecase, pretty=pretty, request_options=request_options
        )
        return _response.data


class AsyncJobTitleEnrichmentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobTitleEnrichmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobTitleEnrichmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobTitleEnrichmentClient
        """
        return self._raw_client

    async def job_title_enrich(
        self,
        *,
        job_title: typing.Optional[str] = OMIT,
        titlecase: typing.Optional[bool] = OMIT,
        pretty: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobTitle:
        """
        Parameters
        ----------
        job_title : typing.Optional[str]
            Job title that will be enriched

        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase any records returned

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobTitle
            Job Title enrich completed.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.job_title_enrichment.job_title_enrich()


        asyncio.run(main())
        """
        _response = await self._raw_client.job_title_enrich(
            job_title=job_title, titlecase=titlecase, pretty=pretty, request_options=request_options
        )
        return _response.data
