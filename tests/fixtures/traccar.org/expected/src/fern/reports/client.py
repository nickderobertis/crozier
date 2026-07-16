

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.event import Event
from ..types.position import Position
from ..types.report_stops import ReportStops
from ..types.report_summary import ReportSummary
from ..types.report_trips import ReportTrips
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

    def fetch_a_list_of_events_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Event]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        type : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            % can be used to return events of all types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Event]
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.reports.fetch_a_list_of_events_within_the_time_period_for_the_devices_or_groups(
            from_=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            to=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.fetch_a_list_of_events_within_the_time_period_for_the_devices_or_groups(
            from_=from_, to=to, device_id=device_id, group_id=group_id, type=type, request_options=request_options
        )
        return _response.data

    def fetch_a_list_of_positions_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Position]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Position]
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.reports.fetch_a_list_of_positions_within_the_time_period_for_the_devices_or_groups(
            from_=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            to=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.fetch_a_list_of_positions_within_the_time_period_for_the_devices_or_groups(
            from_=from_, to=to, device_id=device_id, group_id=group_id, request_options=request_options
        )
        return _response.data

    def fetch_a_list_of_report_stops_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ReportStops]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReportStops]
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.reports.fetch_a_list_of_report_stops_within_the_time_period_for_the_devices_or_groups(
            from_=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            to=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.fetch_a_list_of_report_stops_within_the_time_period_for_the_devices_or_groups(
            from_=from_, to=to, device_id=device_id, group_id=group_id, request_options=request_options
        )
        return _response.data

    def fetch_a_list_of_report_summary_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ReportSummary]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReportSummary]
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.reports.fetch_a_list_of_report_summary_within_the_time_period_for_the_devices_or_groups(
            from_=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            to=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.fetch_a_list_of_report_summary_within_the_time_period_for_the_devices_or_groups(
            from_=from_, to=to, device_id=device_id, group_id=group_id, request_options=request_options
        )
        return _response.data

    def fetch_a_list_of_report_trips_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ReportTrips]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReportTrips]
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.reports.fetch_a_list_of_report_trips_within_the_time_period_for_the_devices_or_groups(
            from_=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            to=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.fetch_a_list_of_report_trips_within_the_time_period_for_the_devices_or_groups(
            from_=from_, to=to, device_id=device_id, group_id=group_id, request_options=request_options
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

    async def fetch_a_list_of_events_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        type: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Event]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        type : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            % can be used to return events of all types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Event]
            OK

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
            await client.reports.fetch_a_list_of_events_within_the_time_period_for_the_devices_or_groups(
                from_=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                to=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_events_within_the_time_period_for_the_devices_or_groups(
            from_=from_, to=to, device_id=device_id, group_id=group_id, type=type, request_options=request_options
        )
        return _response.data

    async def fetch_a_list_of_positions_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Position]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Position]
            OK

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
            await client.reports.fetch_a_list_of_positions_within_the_time_period_for_the_devices_or_groups(
                from_=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                to=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_list_of_positions_within_the_time_period_for_the_devices_or_groups(
            from_=from_, to=to, device_id=device_id, group_id=group_id, request_options=request_options
        )
        return _response.data

    async def fetch_a_list_of_report_stops_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ReportStops]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReportStops]
            OK

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
            await client.reports.fetch_a_list_of_report_stops_within_the_time_period_for_the_devices_or_groups(
                from_=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                to=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.fetch_a_list_of_report_stops_within_the_time_period_for_the_devices_or_groups(
                from_=from_, to=to, device_id=device_id, group_id=group_id, request_options=request_options
            )
        )
        return _response.data

    async def fetch_a_list_of_report_summary_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ReportSummary]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReportSummary]
            OK

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
            await client.reports.fetch_a_list_of_report_summary_within_the_time_period_for_the_devices_or_groups(
                from_=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                to=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.fetch_a_list_of_report_summary_within_the_time_period_for_the_devices_or_groups(
                from_=from_, to=to, device_id=device_id, group_id=group_id, request_options=request_options
            )
        )
        return _response.data

    async def fetch_a_list_of_report_trips_within_the_time_period_for_the_devices_or_groups(
        self,
        *,
        from_: dt.datetime,
        to: dt.datetime,
        device_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        group_id: typing.Optional[typing.Union[int, typing.Sequence[int]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ReportTrips]:
        """
        At least one _deviceId_ or one _groupId_ must be passed

        Parameters
        ----------
        from_ : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        to : dt.datetime
            in IS0 8601 format. eg. `1963-11-22T18:30:00Z`

        device_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        group_id : typing.Optional[typing.Union[int, typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ReportTrips]
            OK

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
            await client.reports.fetch_a_list_of_report_trips_within_the_time_period_for_the_devices_or_groups(
                from_=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                to=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.fetch_a_list_of_report_trips_within_the_time_period_for_the_devices_or_groups(
                from_=from_, to=to, device_id=device_id, group_id=group_id, request_options=request_options
            )
        )
        return _response.data
