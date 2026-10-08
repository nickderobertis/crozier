

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.msg_header_response import MsgHeaderResponse
from ..types.report_response import ReportResponse
from ..types.sms_inbox_response import SmsInboxResponse
from .raw_client import AsyncRawQueriesClient, RawQueriesClient


OMIT = typing.cast(typing.Any, ...)


class QueriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawQueriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawQueriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawQueriesClient
        """
        return self._raw_client

    def get_sms_headers(
        self, *, appname: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> MsgHeaderResponse:
        """
        Get user's SMS headers

        Parameters
        ----------
        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MsgHeaderResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.queries.get_sms_headers()
        """
        _response = self._raw_client.get_sms_headers(appname=appname, request_options=request_options)
        return _response.data

    def get_inbox_messages(
        self,
        *,
        appname: typing.Optional[str] = None,
        startdate: typing.Optional[str] = None,
        stopdate: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SmsInboxResponse:
        """
        List SMS messages received by your subscriber number

        Parameters
        ----------
        appname : typing.Optional[str]
            Application name

        startdate : typing.Optional[str]
            Start date (e.g., ddMMyyyyHHmmss)

        stopdate : typing.Optional[str]
            End date (e.g., ddMMyyyyHHmmss)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SmsInboxResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.queries.get_inbox_messages()
        """
        _response = self._raw_client.get_inbox_messages(
            appname=appname, startdate=startdate, stopdate=stopdate, request_options=request_options
        )
        return _response.data

    def get_sms_report(
        self,
        *,
        startdate: dt.datetime,
        stopdate: dt.datetime,
        jobids: typing.Optional[typing.Sequence[str]] = OMIT,
        pagenumber: typing.Optional[int] = OMIT,
        pagesize: typing.Optional[int] = OMIT,
        appname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportResponse:
        """
        Get delivery status report for sent SMS messages

        Parameters
        ----------
        startdate : dt.datetime
            Start date

        stopdate : dt.datetime
            End date

        jobids : typing.Optional[typing.Sequence[str]]
            Message IDs to query

        pagenumber : typing.Optional[int]
            Page number (starts from 0)

        pagesize : typing.Optional[int]
            Records per page

        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportResponse
            success

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.queries.get_sms_report(
            startdate=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            stopdate=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.get_sms_report(
            startdate=startdate,
            stopdate=stopdate,
            jobids=jobids,
            pagenumber=pagenumber,
            pagesize=pagesize,
            appname=appname,
            request_options=request_options,
        )
        return _response.data


class AsyncQueriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawQueriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawQueriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawQueriesClient
        """
        return self._raw_client

    async def get_sms_headers(
        self, *, appname: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> MsgHeaderResponse:
        """
        Get user's SMS headers

        Parameters
        ----------
        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MsgHeaderResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.queries.get_sms_headers()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sms_headers(appname=appname, request_options=request_options)
        return _response.data

    async def get_inbox_messages(
        self,
        *,
        appname: typing.Optional[str] = None,
        startdate: typing.Optional[str] = None,
        stopdate: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SmsInboxResponse:
        """
        List SMS messages received by your subscriber number

        Parameters
        ----------
        appname : typing.Optional[str]
            Application name

        startdate : typing.Optional[str]
            Start date (e.g., ddMMyyyyHHmmss)

        stopdate : typing.Optional[str]
            End date (e.g., ddMMyyyyHHmmss)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SmsInboxResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.queries.get_inbox_messages()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_inbox_messages(
            appname=appname, startdate=startdate, stopdate=stopdate, request_options=request_options
        )
        return _response.data

    async def get_sms_report(
        self,
        *,
        startdate: dt.datetime,
        stopdate: dt.datetime,
        jobids: typing.Optional[typing.Sequence[str]] = OMIT,
        pagenumber: typing.Optional[int] = OMIT,
        pagesize: typing.Optional[int] = OMIT,
        appname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReportResponse:
        """
        Get delivery status report for sent SMS messages

        Parameters
        ----------
        startdate : dt.datetime
            Start date

        stopdate : dt.datetime
            End date

        jobids : typing.Optional[typing.Sequence[str]]
            Message IDs to query

        pagenumber : typing.Optional[int]
            Page number (starts from 0)

        pagesize : typing.Optional[int]
            Records per page

        appname : typing.Optional[str]
            Application name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReportResponse
            success

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.queries.get_sms_report(
                startdate=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                stopdate=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_sms_report(
            startdate=startdate,
            stopdate=stopdate,
            jobids=jobids,
            pagenumber=pagenumber,
            pagesize=pagesize,
            appname=appname,
            request_options=request_options,
        )
        return _response.data
