

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawReportsClient, RawReportsClient


class ReportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReportsClient
        """
        return self._raw_client

    def get_testresults_report(
        self,
        *,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Returns a csv report detailing all artefacts within a given date range. Together
        with their test executions and test results in csv format.

        Parameters
        ----------
        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.reports.get_testresults_report()
        """
        _response = self._raw_client.get_testresults_report(
            start_date=start_date, end_date=end_date, request_options=request_options
        )
        return _response.data

    def get_test_execution_reports(
        self,
        *,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Returns a csv report detailing all test executions within a given date range.
        Together with their artefact and environment details in csv format.

        Parameters
        ----------
        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.reports.get_test_execution_reports()
        """
        _response = self._raw_client.get_test_execution_reports(
            start_date=start_date, end_date=end_date, request_options=request_options
        )
        return _response.data


class AsyncReportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReportsClient
        """
        return self._raw_client

    async def get_testresults_report(
        self,
        *,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Returns a csv report detailing all artefacts within a given date range. Together
        with their test executions and test results in csv format.

        Parameters
        ----------
        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.reports.get_testresults_report()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_testresults_report(
            start_date=start_date, end_date=end_date, request_options=request_options
        )
        return _response.data

    async def get_test_execution_reports(
        self,
        *,
        start_date: typing.Optional[dt.datetime] = None,
        end_date: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Returns a csv report detailing all test executions within a given date range.
        Together with their artefact and environment details in csv format.

        Parameters
        ----------
        start_date : typing.Optional[dt.datetime]

        end_date : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.reports.get_test_execution_reports()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_test_execution_reports(
            start_date=start_date, end_date=end_date, request_options=request_options
        )
        return _response.data
