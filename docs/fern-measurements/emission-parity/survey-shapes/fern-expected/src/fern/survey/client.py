

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.site import Site
from .raw_client import AsyncRawSurveyClient, RawSurveyClient
from .types.amend_site_request_body import AmendSiteRequestBody
from .types.record_sites_request import RecordSitesRequest


OMIT = typing.cast(typing.Any, ...)


class SurveyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSurveyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSurveyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSurveyClient
        """
        return self._raw_client

    def amend_site(
        self, site_id: str, *, request: AmendSiteRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> Site:
        """
        Parameters
        ----------
        site_id : str

        request : AmendSiteRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Site
            The amended site.

        Examples
        --------
        from fern import FernApi, SitePatch

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.survey.amend_site(
            site_id="site_id",
            request=SitePatch(),
        )
        """
        _response = self._raw_client.amend_site(site_id, request=request, request_options=request_options)
        return _response.data

    def record_sites(
        self, *, request: RecordSitesRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : RecordSitesRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.survey import RecordSitesRequest_Site

        from fern import FernApi, SiteType

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.survey.record_sites(
            request=RecordSitesRequest_Site(
                type=SiteType.SITE,
                name="name",
            ),
        )
        """
        _response = self._raw_client.record_sites(request=request, request_options=request_options)
        return _response.data


class AsyncSurveyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSurveyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSurveyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSurveyClient
        """
        return self._raw_client

    async def amend_site(
        self, site_id: str, *, request: AmendSiteRequestBody, request_options: typing.Optional[RequestOptions] = None
    ) -> Site:
        """
        Parameters
        ----------
        site_id : str

        request : AmendSiteRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Site
            The amended site.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SitePatch

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.survey.amend_site(
                site_id="site_id",
                request=SitePatch(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.amend_site(site_id, request=request, request_options=request_options)
        return _response.data

    async def record_sites(
        self, *, request: RecordSitesRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        request : RecordSitesRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.survey import RecordSitesRequest_Site

        from fern import AsyncFernApi, SiteType

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.survey.record_sites(
                request=RecordSitesRequest_Site(
                    type=SiteType.SITE,
                    name="name",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_sites(request=request, request_options=request_options)
        return _response.data
