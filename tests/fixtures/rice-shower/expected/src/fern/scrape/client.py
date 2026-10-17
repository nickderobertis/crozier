

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawScrapeClient, RawScrapeClient
from .types.get_all_scrape_metrics_response_item import GetAllScrapeMetricsResponseItem
from .types.get_all_scrape_status_response_item import GetAllScrapeStatusResponseItem
from .types.get_system_scrape_metrics_response import GetSystemScrapeMetricsResponse
from .types.get_system_scrape_status_response import GetSystemScrapeStatusResponse


class ScrapeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawScrapeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawScrapeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawScrapeClient
        """
        return self._raw_client

    def get_all_scrape_metrics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetAllScrapeMetricsResponseItem]:
        """
        Retrieve scraping metrics for all active systems, including per-system error counts and success totals

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetAllScrapeMetricsResponseItem]
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.scrape.get_all_scrape_metrics()
        """
        _response = self._raw_client.get_all_scrape_metrics(request_options=request_options)
        return _response.data

    def get_system_scrape_metrics(
        self, system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSystemScrapeMetricsResponse:
        """
        Retrieve scraping metrics for a specific system by its ID

        Parameters
        ----------
        system_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSystemScrapeMetricsResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.scrape.get_system_scrape_metrics(
            system_id="systemId",
        )
        """
        _response = self._raw_client.get_system_scrape_metrics(system_id, request_options=request_options)
        return _response.data

    def get_all_scrape_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetAllScrapeStatusResponseItem]:
        """
        Retrieve windowed scrape status (success/error counts in last 1m, 10m, and since start) for all active systems

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetAllScrapeStatusResponseItem]
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.scrape.get_all_scrape_status()
        """
        _response = self._raw_client.get_all_scrape_status(request_options=request_options)
        return _response.data

    def get_system_scrape_status(
        self, system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSystemScrapeStatusResponse:
        """
        Retrieve windowed scrape status for a specific system by its ID

        Parameters
        ----------
        system_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSystemScrapeStatusResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.scrape.get_system_scrape_status(
            system_id="systemId",
        )
        """
        _response = self._raw_client.get_system_scrape_status(system_id, request_options=request_options)
        return _response.data


class AsyncScrapeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawScrapeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawScrapeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawScrapeClient
        """
        return self._raw_client

    async def get_all_scrape_metrics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetAllScrapeMetricsResponseItem]:
        """
        Retrieve scraping metrics for all active systems, including per-system error counts and success totals

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetAllScrapeMetricsResponseItem]
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.scrape.get_all_scrape_metrics()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_scrape_metrics(request_options=request_options)
        return _response.data

    async def get_system_scrape_metrics(
        self, system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSystemScrapeMetricsResponse:
        """
        Retrieve scraping metrics for a specific system by its ID

        Parameters
        ----------
        system_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSystemScrapeMetricsResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.scrape.get_system_scrape_metrics(
                system_id="systemId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_system_scrape_metrics(system_id, request_options=request_options)
        return _response.data

    async def get_all_scrape_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetAllScrapeStatusResponseItem]:
        """
        Retrieve windowed scrape status (success/error counts in last 1m, 10m, and since start) for all active systems

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetAllScrapeStatusResponseItem]
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.scrape.get_all_scrape_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_scrape_status(request_options=request_options)
        return _response.data

    async def get_system_scrape_status(
        self, system_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSystemScrapeStatusResponse:
        """
        Retrieve windowed scrape status for a specific system by its ID

        Parameters
        ----------
        system_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSystemScrapeStatusResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.scrape.get_system_scrape_status(
                system_id="systemId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_system_scrape_status(system_id, request_options=request_options)
        return _response.data
