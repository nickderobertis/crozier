

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.time_entries_response import TimeEntriesResponse
from .raw_client import AsyncRawTimeEntriesClient, RawTimeEntriesClient
from .types.get_time_entries_request_sort_field import GetTimeEntriesRequestSortField
from .types.get_time_entries_request_sort_order import GetTimeEntriesRequestSortOrder


class TimeEntriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTimeEntriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTimeEntriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTimeEntriesClient
        """
        return self._raw_client

    def get_time_entries(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetTimeEntriesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetTimeEntriesRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        filter_locked_only: typing.Optional[bool] = None,
        filter_user_id: typing.Optional[float] = None,
        filter_job_no: typing.Optional[float] = None,
        filter_job_phase_id: typing.Optional[float] = None,
        filter_date_from: typing.Optional[dt.date] = None,
        filter_date_to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TimeEntriesResponse:
        """
        Get all time entries

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetTimeEntriesRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetTimeEntriesRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `user`
            - `employee's username`
            - `jobPhaseTitle`,
            - `jobPhaseDetails`

        filter_locked_only : typing.Optional[bool]

        filter_user_id : typing.Optional[float]
            The user id to filter time entries by

        filter_job_no : typing.Optional[float]
            The job no to filter time entries by

        filter_job_phase_id : typing.Optional[float]
            The job phase id to filter time entries by

        filter_date_from : typing.Optional[dt.date]
            The start date in yyyy-mm-dd format

        filter_date_to : typing.Optional[dt.date]
            The end date in yyyy-mm-dd format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TimeEntriesResponse
            Successful Response

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.time_entries.get_time_entries(
            filter_search_text="John",
            filter_date_from=datetime.date.fromisoformat(
                "2023-01-21",
            ),
            filter_date_to=datetime.date.fromisoformat(
                "2023-01-21",
            ),
        )
        """
        _response = self._raw_client.get_time_entries(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_search_text=filter_search_text,
            filter_locked_only=filter_locked_only,
            filter_user_id=filter_user_id,
            filter_job_no=filter_job_no,
            filter_job_phase_id=filter_job_phase_id,
            filter_date_from=filter_date_from,
            filter_date_to=filter_date_to,
            request_options=request_options,
        )
        return _response.data


class AsyncTimeEntriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTimeEntriesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTimeEntriesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTimeEntriesClient
        """
        return self._raw_client

    async def get_time_entries(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetTimeEntriesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetTimeEntriesRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        filter_locked_only: typing.Optional[bool] = None,
        filter_user_id: typing.Optional[float] = None,
        filter_job_no: typing.Optional[float] = None,
        filter_job_phase_id: typing.Optional[float] = None,
        filter_date_from: typing.Optional[dt.date] = None,
        filter_date_to: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TimeEntriesResponse:
        """
        Get all time entries

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetTimeEntriesRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetTimeEntriesRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `user`
            - `employee's username`
            - `jobPhaseTitle`,
            - `jobPhaseDetails`

        filter_locked_only : typing.Optional[bool]

        filter_user_id : typing.Optional[float]
            The user id to filter time entries by

        filter_job_no : typing.Optional[float]
            The job no to filter time entries by

        filter_job_phase_id : typing.Optional[float]
            The job phase id to filter time entries by

        filter_date_from : typing.Optional[dt.date]
            The start date in yyyy-mm-dd format

        filter_date_to : typing.Optional[dt.date]
            The end date in yyyy-mm-dd format

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TimeEntriesResponse
            Successful Response

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.time_entries.get_time_entries(
                filter_search_text="John",
                filter_date_from=datetime.date.fromisoformat(
                    "2023-01-21",
                ),
                filter_date_to=datetime.date.fromisoformat(
                    "2023-01-21",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_time_entries(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_search_text=filter_search_text,
            filter_locked_only=filter_locked_only,
            filter_user_id=filter_user_id,
            filter_job_no=filter_job_no,
            filter_job_phase_id=filter_job_phase_id,
            filter_date_from=filter_date_from,
            filter_date_to=filter_date_to,
            request_options=request_options,
        )
        return _response.data
