

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.disk_usage import DiskUsage
from ..types.get_active_query import GetActiveQuery
from ..types.get_database_content import GetDatabaseContent
from ..types.get_database_metric import GetDatabaseMetric
from ..types.get_php_info import GetPhpInfo
from .raw_client import AsyncRawOverviewClient, RawOverviewClient


class OverviewClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOverviewClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOverviewClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOverviewClient
        """
        return self._raw_client

    def get_database_contents(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetDatabaseContent]:
        """
        Get database contents for the dashboard display.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetDatabaseContent]
            List of the database contents

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.overview.get_database_contents()
        """
        _response = self._raw_client.get_database_contents(request_options=request_options)
        return _response.data

    def get_php_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetPhpInfo:
        """
        Get PHP info

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPhpInfo
            PHP info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.overview.get_php_info()
        """
        _response = self._raw_client.get_php_info(request_options=request_options)
        return _response.data

    def get_disk_usage(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[DiskUsage]:
        """
        Get disk usage

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DiskUsage]
            Disk usage response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.overview.get_disk_usage()
        """
        _response = self._raw_client.get_disk_usage(request_options=request_options)
        return _response.data

    def get_database_metrics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetDatabaseMetric]:
        """
        Get database metrics for the dashboard display.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetDatabaseMetric]
            List of the database metrics

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.overview.get_database_metrics()
        """
        _response = self._raw_client.get_database_metrics(request_options=request_options)
        return _response.data

    def get_active_queries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetActiveQuery]:
        """
        Get a list of active queries from the database.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetActiveQuery]
            List of active queries

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.overview.get_active_queries()
        """
        _response = self._raw_client.get_active_queries(request_options=request_options)
        return _response.data


class AsyncOverviewClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOverviewClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOverviewClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOverviewClient
        """
        return self._raw_client

    async def get_database_contents(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetDatabaseContent]:
        """
        Get database contents for the dashboard display.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetDatabaseContent]
            List of the database contents

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.overview.get_database_contents()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_database_contents(request_options=request_options)
        return _response.data

    async def get_php_info(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetPhpInfo:
        """
        Get PHP info

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPhpInfo
            PHP info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.overview.get_php_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_php_info(request_options=request_options)
        return _response.data

    async def get_disk_usage(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[DiskUsage]:
        """
        Get disk usage

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[DiskUsage]
            Disk usage response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.overview.get_disk_usage()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_disk_usage(request_options=request_options)
        return _response.data

    async def get_database_metrics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetDatabaseMetric]:
        """
        Get database metrics for the dashboard display.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetDatabaseMetric]
            List of the database metrics

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.overview.get_database_metrics()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_database_metrics(request_options=request_options)
        return _response.data

    async def get_active_queries(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetActiveQuery]:
        """
        Get a list of active queries from the database.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetActiveQuery]
            List of active queries

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.overview.get_active_queries()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_active_queries(request_options=request_options)
        return _response.data
