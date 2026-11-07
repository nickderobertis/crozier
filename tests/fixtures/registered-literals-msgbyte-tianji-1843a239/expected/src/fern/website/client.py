

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWebsiteClient, RawWebsiteClient
from .types.website_add_response import WebsiteAddResponse
from .types.website_all_response_item import WebsiteAllResponseItem
from .types.website_create_or_enable_share_response import WebsiteCreateOrEnableShareResponse
from .types.website_delete_response import WebsiteDeleteResponse
from .types.website_disable_share_response import WebsiteDisableShareResponse
from .types.website_geo_stats_response_item import WebsiteGeoStatsResponseItem
from .types.website_get_lighthouse_report_response import WebsiteGetLighthouseReportResponse
from .types.website_get_public_info_by_share_id_response import WebsiteGetPublicInfoByShareIdResponse
from .types.website_get_public_metrics_by_share_id_request_range import WebsiteGetPublicMetricsByShareIdRequestRange
from .types.website_get_public_metrics_by_share_id_request_type import WebsiteGetPublicMetricsByShareIdRequestType
from .types.website_get_public_metrics_by_share_id_response_item import WebsiteGetPublicMetricsByShareIdResponseItem
from .types.website_get_public_stats_by_share_id_request_range import WebsiteGetPublicStatsByShareIdRequestRange
from .types.website_get_public_stats_by_share_id_response import WebsiteGetPublicStatsByShareIdResponse
from .types.website_info_response import WebsiteInfoResponse
from .types.website_metrics_request_type import WebsiteMetricsRequestType
from .types.website_metrics_response_item import WebsiteMetricsResponseItem
from .types.website_pageviews_response import WebsitePageviewsResponse
from .types.website_stats_response import WebsiteStatsResponse
from .types.website_update_info_response import WebsiteUpdateInfoResponse


OMIT = typing.cast(typing.Any, ...)


class WebsiteClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebsiteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebsiteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebsiteClient
        """
        return self._raw_client

    def onlinecount(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.onlinecount(
            workspace_id="workspaceId",
            website_id="websiteId",
        )
        """
        _response = self._raw_client.onlinecount(workspace_id, website_id, request_options=request_options)
        return _response.data

    def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WebsiteAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WebsiteAllResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.all_(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data

    def alloverview(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, float]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, float]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.alloverview(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.alloverview(workspace_id, request_options=request_options)
        return _response.data

    def info(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[WebsiteInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[WebsiteInfoResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.info(
            workspace_id="workspaceId",
            website_id="websiteId",
        )
        """
        _response = self._raw_client.info(workspace_id, website_id, request_options=request_options)
        return _response.data

    def stats(
        self,
        workspace_id: str,
        website_id: str,
        *,
        start_at: float,
        end_at: float,
        unit: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        os: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebsiteStatsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        start_at : float

        end_at : float

        unit : typing.Optional[str]

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        referrer : typing.Optional[str]

        title : typing.Optional[str]

        os : typing.Optional[str]

        browser : typing.Optional[str]

        device : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteStatsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.stats(
            workspace_id="workspaceId",
            website_id="websiteId",
            start_at=1.1,
            end_at=1.1,
        )
        """
        _response = self._raw_client.stats(
            workspace_id,
            website_id,
            start_at=start_at,
            end_at=end_at,
            unit=unit,
            url=url,
            country=country,
            region=region,
            city=city,
            timezone=timezone,
            referrer=referrer,
            title=title,
            os=os,
            browser=browser,
            device=device,
            request_options=request_options,
        )
        return _response.data

    def geostats(
        self,
        workspace_id: str,
        website_id: str,
        *,
        start_at: float,
        end_at: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[WebsiteGeoStatsResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        start_at : float

        end_at : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WebsiteGeoStatsResponseItem]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.geostats(
            workspace_id="workspaceId",
            website_id="websiteId",
            start_at=1.1,
            end_at=1.1,
        )
        """
        _response = self._raw_client.geostats(
            workspace_id, website_id, start_at=start_at, end_at=end_at, request_options=request_options
        )
        return _response.data

    def pageviews(
        self,
        workspace_id: str,
        website_id: str,
        *,
        start_at: float,
        end_at: float,
        unit: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        os: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebsitePageviewsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        start_at : float

        end_at : float

        unit : typing.Optional[str]

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        referrer : typing.Optional[str]

        title : typing.Optional[str]

        os : typing.Optional[str]

        browser : typing.Optional[str]

        device : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsitePageviewsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.pageviews(
            workspace_id="workspaceId",
            website_id="websiteId",
            start_at=1.1,
            end_at=1.1,
        )
        """
        _response = self._raw_client.pageviews(
            workspace_id,
            website_id,
            start_at=start_at,
            end_at=end_at,
            unit=unit,
            url=url,
            country=country,
            region=region,
            city=city,
            timezone=timezone,
            referrer=referrer,
            title=title,
            os=os,
            browser=browser,
            device=device,
            request_options=request_options,
        )
        return _response.data

    def metrics(
        self,
        workspace_id: str,
        website_id: str,
        *,
        type: WebsiteMetricsRequestType,
        start_at: float,
        end_at: float,
        url: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        os: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        event: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_term: typing.Optional[str] = None,
        utm_content: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[WebsiteMetricsResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        type : WebsiteMetricsRequestType

        start_at : float

        end_at : float

        url : typing.Optional[str]

        referrer : typing.Optional[str]

        title : typing.Optional[str]

        os : typing.Optional[str]

        browser : typing.Optional[str]

        device : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        language : typing.Optional[str]

        event : typing.Optional[str]

        utm_source : typing.Optional[str]

        utm_medium : typing.Optional[str]

        utm_campaign : typing.Optional[str]

        utm_term : typing.Optional[str]

        utm_content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WebsiteMetricsResponseItem]
            Successful response

        Examples
        --------
        from fern.website import WebsiteMetricsRequestType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.metrics(
            workspace_id="workspaceId",
            website_id="websiteId",
            type=WebsiteMetricsRequestType.URL,
            start_at=1.1,
            end_at=1.1,
        )
        """
        _response = self._raw_client.metrics(
            workspace_id,
            website_id,
            type=type,
            start_at=start_at,
            end_at=end_at,
            url=url,
            referrer=referrer,
            title=title,
            os=os,
            browser=browser,
            device=device,
            country=country,
            region=region,
            city=city,
            language=language,
            event=event,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            request_options=request_options,
        )
        return _response.data

    def add(
        self, workspace_id: str, *, name: str, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WebsiteAddResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        domain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteAddResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.add(
            workspace_id="workspaceId",
            name="name",
            domain="domain",
        )
        """
        _response = self._raw_client.add(workspace_id, name=name, domain=domain, request_options=request_options)
        return _response.data

    def delete(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebsiteDeleteResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteDeleteResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.delete(
            workspace_id="workspaceId",
            website_id="websiteId",
        )
        """
        _response = self._raw_client.delete(workspace_id, website_id, request_options=request_options)
        return _response.data

    def updateinfo(
        self,
        workspace_id: str,
        website_id: str,
        *,
        name: str,
        domain: str,
        monitor_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebsiteUpdateInfoResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        name : str

        domain : str

        monitor_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteUpdateInfoResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.updateinfo(
            workspace_id="workspaceId",
            website_id="websiteId",
            name="name",
            domain="domain",
        )
        """
        _response = self._raw_client.updateinfo(
            workspace_id, website_id, name=name, domain=domain, monitor_id=monitor_id, request_options=request_options
        )
        return _response.data

    def generatelighthousereport(
        self, workspace_id: str, website_id: str, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.generatelighthousereport(
            workspace_id="workspaceId",
            website_id="websiteId",
            url="url",
        )
        """
        _response = self._raw_client.generatelighthousereport(
            workspace_id, website_id, url=url, request_options=request_options
        )
        return _response.data

    def getlighthousereport(
        self,
        workspace_id: str,
        website_id: str,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebsiteGetLighthouseReportResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        limit : typing.Optional[float]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteGetLighthouseReportResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.getlighthousereport(
            workspace_id="workspaceId",
            website_id="websiteId",
        )
        """
        _response = self._raw_client.getlighthousereport(
            workspace_id, website_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    def getlighthousejson(
        self, lighthouse_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        lighthouse_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.getlighthousejson(
            lighthouse_id="lighthouseId",
        )
        """
        _response = self._raw_client.getlighthousejson(lighthouse_id, request_options=request_options)
        return _response.data

    def getpublicinfobyshareid(
        self, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebsiteGetPublicInfoByShareIdResponse:
        """
        Parameters
        ----------
        share_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteGetPublicInfoByShareIdResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.getpublicinfobyshareid(
            share_id="shareId",
        )
        """
        _response = self._raw_client.getpublicinfobyshareid(share_id, request_options=request_options)
        return _response.data

    def getpublicstatsbyshareid(
        self,
        share_id: str,
        *,
        range: typing.Optional[WebsiteGetPublicStatsByShareIdRequestRange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebsiteGetPublicStatsByShareIdResponse:
        """
        Parameters
        ----------
        share_id : str

        range : typing.Optional[WebsiteGetPublicStatsByShareIdRequestRange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteGetPublicStatsByShareIdResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.getpublicstatsbyshareid(
            share_id="shareId",
        )
        """
        _response = self._raw_client.getpublicstatsbyshareid(share_id, range=range, request_options=request_options)
        return _response.data

    def getpublicmetricsbyshareid(
        self,
        share_id: str,
        *,
        type: WebsiteGetPublicMetricsByShareIdRequestType,
        range: typing.Optional[WebsiteGetPublicMetricsByShareIdRequestRange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[WebsiteGetPublicMetricsByShareIdResponseItem]:
        """
        Parameters
        ----------
        share_id : str

        type : WebsiteGetPublicMetricsByShareIdRequestType

        range : typing.Optional[WebsiteGetPublicMetricsByShareIdRequestRange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WebsiteGetPublicMetricsByShareIdResponseItem]
            Successful response

        Examples
        --------
        from fern.website import WebsiteGetPublicMetricsByShareIdRequestType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.getpublicmetricsbyshareid(
            share_id="shareId",
            type=WebsiteGetPublicMetricsByShareIdRequestType.URL,
        )
        """
        _response = self._raw_client.getpublicmetricsbyshareid(
            share_id, type=type, range=range, request_options=request_options
        )
        return _response.data

    def createorenableshare(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebsiteCreateOrEnableShareResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteCreateOrEnableShareResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.createorenableshare(
            workspace_id="workspaceId",
            website_id="websiteId",
        )
        """
        _response = self._raw_client.createorenableshare(workspace_id, website_id, request_options=request_options)
        return _response.data

    def disableshare(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebsiteDisableShareResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteDisableShareResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.website.disableshare(
            workspace_id="workspaceId",
            website_id="websiteId",
        )
        """
        _response = self._raw_client.disableshare(workspace_id, website_id, request_options=request_options)
        return _response.data


class AsyncWebsiteClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebsiteClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebsiteClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebsiteClient
        """
        return self._raw_client

    async def onlinecount(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> float:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.onlinecount(
                workspace_id="workspaceId",
                website_id="websiteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.onlinecount(workspace_id, website_id, request_options=request_options)
        return _response.data

    async def all_(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[WebsiteAllResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WebsiteAllResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.all_(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.all_(workspace_id, request_options=request_options)
        return _response.data

    async def alloverview(
        self, workspace_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, float]:
        """
        Parameters
        ----------
        workspace_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, float]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.alloverview(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.alloverview(workspace_id, request_options=request_options)
        return _response.data

    async def info(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[WebsiteInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[WebsiteInfoResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.info(
                workspace_id="workspaceId",
                website_id="websiteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.info(workspace_id, website_id, request_options=request_options)
        return _response.data

    async def stats(
        self,
        workspace_id: str,
        website_id: str,
        *,
        start_at: float,
        end_at: float,
        unit: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        os: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebsiteStatsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        start_at : float

        end_at : float

        unit : typing.Optional[str]

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        referrer : typing.Optional[str]

        title : typing.Optional[str]

        os : typing.Optional[str]

        browser : typing.Optional[str]

        device : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteStatsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.stats(
                workspace_id="workspaceId",
                website_id="websiteId",
                start_at=1.1,
                end_at=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stats(
            workspace_id,
            website_id,
            start_at=start_at,
            end_at=end_at,
            unit=unit,
            url=url,
            country=country,
            region=region,
            city=city,
            timezone=timezone,
            referrer=referrer,
            title=title,
            os=os,
            browser=browser,
            device=device,
            request_options=request_options,
        )
        return _response.data

    async def geostats(
        self,
        workspace_id: str,
        website_id: str,
        *,
        start_at: float,
        end_at: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[WebsiteGeoStatsResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        start_at : float

        end_at : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WebsiteGeoStatsResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.geostats(
                workspace_id="workspaceId",
                website_id="websiteId",
                start_at=1.1,
                end_at=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.geostats(
            workspace_id, website_id, start_at=start_at, end_at=end_at, request_options=request_options
        )
        return _response.data

    async def pageviews(
        self,
        workspace_id: str,
        website_id: str,
        *,
        start_at: float,
        end_at: float,
        unit: typing.Optional[str] = None,
        url: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        timezone: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        os: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebsitePageviewsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        start_at : float

        end_at : float

        unit : typing.Optional[str]

        url : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        timezone : typing.Optional[str]

        referrer : typing.Optional[str]

        title : typing.Optional[str]

        os : typing.Optional[str]

        browser : typing.Optional[str]

        device : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsitePageviewsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.pageviews(
                workspace_id="workspaceId",
                website_id="websiteId",
                start_at=1.1,
                end_at=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pageviews(
            workspace_id,
            website_id,
            start_at=start_at,
            end_at=end_at,
            unit=unit,
            url=url,
            country=country,
            region=region,
            city=city,
            timezone=timezone,
            referrer=referrer,
            title=title,
            os=os,
            browser=browser,
            device=device,
            request_options=request_options,
        )
        return _response.data

    async def metrics(
        self,
        workspace_id: str,
        website_id: str,
        *,
        type: WebsiteMetricsRequestType,
        start_at: float,
        end_at: float,
        url: typing.Optional[str] = None,
        referrer: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
        os: typing.Optional[str] = None,
        browser: typing.Optional[str] = None,
        device: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        city: typing.Optional[str] = None,
        language: typing.Optional[str] = None,
        event: typing.Optional[str] = None,
        utm_source: typing.Optional[str] = None,
        utm_medium: typing.Optional[str] = None,
        utm_campaign: typing.Optional[str] = None,
        utm_term: typing.Optional[str] = None,
        utm_content: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[WebsiteMetricsResponseItem]:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        type : WebsiteMetricsRequestType

        start_at : float

        end_at : float

        url : typing.Optional[str]

        referrer : typing.Optional[str]

        title : typing.Optional[str]

        os : typing.Optional[str]

        browser : typing.Optional[str]

        device : typing.Optional[str]

        country : typing.Optional[str]

        region : typing.Optional[str]

        city : typing.Optional[str]

        language : typing.Optional[str]

        event : typing.Optional[str]

        utm_source : typing.Optional[str]

        utm_medium : typing.Optional[str]

        utm_campaign : typing.Optional[str]

        utm_term : typing.Optional[str]

        utm_content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WebsiteMetricsResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern.website import WebsiteMetricsRequestType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.metrics(
                workspace_id="workspaceId",
                website_id="websiteId",
                type=WebsiteMetricsRequestType.URL,
                start_at=1.1,
                end_at=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.metrics(
            workspace_id,
            website_id,
            type=type,
            start_at=start_at,
            end_at=end_at,
            url=url,
            referrer=referrer,
            title=title,
            os=os,
            browser=browser,
            device=device,
            country=country,
            region=region,
            city=city,
            language=language,
            event=event,
            utm_source=utm_source,
            utm_medium=utm_medium,
            utm_campaign=utm_campaign,
            utm_term=utm_term,
            utm_content=utm_content,
            request_options=request_options,
        )
        return _response.data

    async def add(
        self, workspace_id: str, *, name: str, domain: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WebsiteAddResponse:
        """
        Parameters
        ----------
        workspace_id : str

        name : str

        domain : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteAddResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.add(
                workspace_id="workspaceId",
                name="name",
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(workspace_id, name=name, domain=domain, request_options=request_options)
        return _response.data

    async def delete(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebsiteDeleteResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.delete(
                workspace_id="workspaceId",
                website_id="websiteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(workspace_id, website_id, request_options=request_options)
        return _response.data

    async def updateinfo(
        self,
        workspace_id: str,
        website_id: str,
        *,
        name: str,
        domain: str,
        monitor_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebsiteUpdateInfoResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        name : str

        domain : str

        monitor_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteUpdateInfoResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.updateinfo(
                workspace_id="workspaceId",
                website_id="websiteId",
                name="name",
                domain="domain",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateinfo(
            workspace_id, website_id, name=name, domain=domain, monitor_id=monitor_id, request_options=request_options
        )
        return _response.data

    async def generatelighthousereport(
        self, workspace_id: str, website_id: str, *, url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        url : str

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

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.generatelighthousereport(
                workspace_id="workspaceId",
                website_id="websiteId",
                url="url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generatelighthousereport(
            workspace_id, website_id, url=url, request_options=request_options
        )
        return _response.data

    async def getlighthousereport(
        self,
        workspace_id: str,
        website_id: str,
        *,
        limit: typing.Optional[float] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebsiteGetLighthouseReportResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        limit : typing.Optional[float]

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteGetLighthouseReportResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.getlighthousereport(
                workspace_id="workspaceId",
                website_id="websiteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getlighthousereport(
            workspace_id, website_id, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def getlighthousejson(
        self, lighthouse_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        lighthouse_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.getlighthousejson(
                lighthouse_id="lighthouseId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getlighthousejson(lighthouse_id, request_options=request_options)
        return _response.data

    async def getpublicinfobyshareid(
        self, share_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebsiteGetPublicInfoByShareIdResponse:
        """
        Parameters
        ----------
        share_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteGetPublicInfoByShareIdResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.getpublicinfobyshareid(
                share_id="shareId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpublicinfobyshareid(share_id, request_options=request_options)
        return _response.data

    async def getpublicstatsbyshareid(
        self,
        share_id: str,
        *,
        range: typing.Optional[WebsiteGetPublicStatsByShareIdRequestRange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebsiteGetPublicStatsByShareIdResponse:
        """
        Parameters
        ----------
        share_id : str

        range : typing.Optional[WebsiteGetPublicStatsByShareIdRequestRange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteGetPublicStatsByShareIdResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.getpublicstatsbyshareid(
                share_id="shareId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpublicstatsbyshareid(
            share_id, range=range, request_options=request_options
        )
        return _response.data

    async def getpublicmetricsbyshareid(
        self,
        share_id: str,
        *,
        type: WebsiteGetPublicMetricsByShareIdRequestType,
        range: typing.Optional[WebsiteGetPublicMetricsByShareIdRequestRange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[WebsiteGetPublicMetricsByShareIdResponseItem]:
        """
        Parameters
        ----------
        share_id : str

        type : WebsiteGetPublicMetricsByShareIdRequestType

        range : typing.Optional[WebsiteGetPublicMetricsByShareIdRequestRange]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WebsiteGetPublicMetricsByShareIdResponseItem]
            Successful response

        Examples
        --------
        import asyncio

        from fern.website import WebsiteGetPublicMetricsByShareIdRequestType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.getpublicmetricsbyshareid(
                share_id="shareId",
                type=WebsiteGetPublicMetricsByShareIdRequestType.URL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpublicmetricsbyshareid(
            share_id, type=type, range=range, request_options=request_options
        )
        return _response.data

    async def createorenableshare(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebsiteCreateOrEnableShareResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteCreateOrEnableShareResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.createorenableshare(
                workspace_id="workspaceId",
                website_id="websiteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createorenableshare(
            workspace_id, website_id, request_options=request_options
        )
        return _response.data

    async def disableshare(
        self, workspace_id: str, website_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebsiteDisableShareResponse:
        """
        Parameters
        ----------
        workspace_id : str

        website_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebsiteDisableShareResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.website.disableshare(
                workspace_id="workspaceId",
                website_id="websiteId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.disableshare(workspace_id, website_id, request_options=request_options)
        return _response.data
