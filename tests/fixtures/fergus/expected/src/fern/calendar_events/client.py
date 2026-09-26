

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.calendar_event_by_id_response import CalendarEventByIdResponse
from ..types.calendar_events_response import CalendarEventsResponse
from .raw_client import AsyncRawCalendarEventsClient, RawCalendarEventsClient
from .types.delete_calendar_events_calendar_event_id_request_delete_all_grouped import (
    DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped,
)
from .types.delete_calendar_events_calendar_event_id_request_delete_all_recurring import (
    DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring,
)
from .types.get_calendar_events_request_filter_calendar_event_type import (
    GetCalendarEventsRequestFilterCalendarEventType,
)
from .types.get_calendar_events_request_filter_calendar_range import GetCalendarEventsRequestFilterCalendarRange
from .types.post_calendar_events_calendar_event_id_request_frequency import (
    PostCalendarEventsCalendarEventIdRequestFrequency,
)
from .types.post_calendar_events_calendar_event_id_request_repeat_end_type import (
    PostCalendarEventsCalendarEventIdRequestRepeatEndType,
)
from .types.post_calendar_events_calendar_event_id_request_update_all_grouped import (
    PostCalendarEventsCalendarEventIdRequestUpdateAllGrouped,
)
from .types.post_calendar_events_calendar_event_id_request_update_all_recurring import (
    PostCalendarEventsCalendarEventIdRequestUpdateAllRecurring,
)
from .types.post_calendar_events_request_event_type import PostCalendarEventsRequestEventType
from .types.post_calendar_events_request_frequency import PostCalendarEventsRequestFrequency
from .types.post_calendar_events_request_repeat_end_type import PostCalendarEventsRequestRepeatEndType


OMIT = typing.cast(typing.Any, ...)


class CalendarEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCalendarEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCalendarEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCalendarEventsClient
        """
        return self._raw_client

    def get_calendar_events(
        self,
        *,
        filter_calendar_event_type: typing.Optional[GetCalendarEventsRequestFilterCalendarEventType] = None,
        filter_user_id: typing.Optional[float] = None,
        filter_job_id: typing.Optional[float] = None,
        filter_job_phase_id: typing.Optional[float] = None,
        filter_job_events_only: typing.Optional[bool] = None,
        filter_non_job_events_only: typing.Optional[bool] = None,
        filter_unassigned_events_only: typing.Optional[bool] = None,
        filter_active_only: typing.Optional[bool] = None,
        filter_date_from: typing.Optional[dt.datetime] = None,
        filter_calendar_range: typing.Optional[GetCalendarEventsRequestFilterCalendarRange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CalendarEventsResponse:
        """
        Returns a list of CalendarEvents. The list can be filtered by user name, event type or active events only.

        Parameters
        ----------
        filter_calendar_event_type : typing.Optional[GetCalendarEventsRequestFilterCalendarEventType]

        filter_user_id : typing.Optional[float]

        filter_job_id : typing.Optional[float]

        filter_job_phase_id : typing.Optional[float]

        filter_job_events_only : typing.Optional[bool]

        filter_non_job_events_only : typing.Optional[bool]

        filter_unassigned_events_only : typing.Optional[bool]

        filter_active_only : typing.Optional[bool]

        filter_date_from : typing.Optional[dt.datetime]
            The start date for filtering calendar events, in ISO 8601 format.

            - The time portion is discarded only the date is used.

            - A timezone offset (+/-HH:MM or +/-HHMM) is expected to ensure accurate timezone interpretation.

            - If none is provided, the value will be treated as UTC.

        filter_calendar_range : typing.Optional[GetCalendarEventsRequestFilterCalendarRange]
            The filterDateFrom (or currentDate if not provided) sets the start of the period.

            - For DAY and THREE_DAY options, it's that exact date.

            - For WEEK and MONTH options, it's the week or month that includes that date (weeks run Monday to Sunday).

            - For FORTNIGHT option, it starts at the Monday of the week that contains that date.

            This defaults to WEEK if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalendarEventsResponse
            Successful Response

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.calendar_events.get_calendar_events(
            filter_date_from=datetime.datetime.fromisoformat(
                "2025-12-01 11:00:00+00:00",
            ),
        )
        """
        _response = self._raw_client.get_calendar_events(
            filter_calendar_event_type=filter_calendar_event_type,
            filter_user_id=filter_user_id,
            filter_job_id=filter_job_id,
            filter_job_phase_id=filter_job_phase_id,
            filter_job_events_only=filter_job_events_only,
            filter_non_job_events_only=filter_non_job_events_only,
            filter_unassigned_events_only=filter_unassigned_events_only,
            filter_active_only=filter_active_only,
            filter_date_from=filter_date_from,
            filter_calendar_range=filter_calendar_range,
            request_options=request_options,
        )
        return _response.data

    def post_calendar_events(
        self,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        event_title: str,
        event_type: PostCalendarEventsRequestEventType,
        user_id: typing.Optional[float] = OMIT,
        linked_user_ids: typing.Optional[typing.Sequence[float]] = OMIT,
        job_id: typing.Optional[float] = OMIT,
        job_phase_id: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        frequency: typing.Optional[PostCalendarEventsRequestFrequency] = OMIT,
        interval: typing.Optional[float] = OMIT,
        repeat_end_type: typing.Optional[PostCalendarEventsRequestRepeatEndType] = OMIT,
        repeat_end_date: typing.Optional[dt.date] = OMIT,
        repeat_count: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CalendarEventsResponse:
        """
        Creates a new calendar event.
          - **eventType** must be one of : `JOB_PHASE`, `QUOTE`, `ESTIMATE`, `OTHER`.
            - **JOB_PHASE**: Event type for a job phase. `jobPhaseId` must be provided.
            - **QUOTE**: Event type for a quote. `jobId` must be provided.
            - **ESTIMATE**: Event type for an estimate. `jobId` must be provided.
            - **OTHER**: General event type. Default value.
          - **frequency** must be one of : `DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`, `NEVER`.
            - **DAILY**: Repeats every day.
            - **WEEKLY**: Repeats every week.
            - **MONTHLY**: Repeats every month.
            - **YEARLY**: Repeats every year.
            - **NEVER**: Does not repeat. Default value.
          - If the event is recurring, **frequency** is ***not*** `NEVER`.
            - **interval** controls how often the event repeats,
              - Example:  `WEEKLY` with an `interval = 2`, the event repeats every 2 weeks.
              - Default is `1`.
            - **repeatEndType** must be one of:
              - `NEVER`: Repeats indefinitely. Default value.
              - `ON_DATE`: Repeats until the specified **repeatEndDate**.
              - `AFTER`: Repeats for the specified **repeatCount** number of occurrences.
            - If `repeatEndType = ON_DATE`, the **repeatEndDate** must be provided.
            - If `repeatEndType = AFTER`, the **repeatCount** must be provided.
          - If **userId** or **linkedUserIds** is provided, the event is assigned to those user(s). Otherwise, the event is unassigned.


        Parameters
        ----------
        start_time : dt.datetime

        end_time : dt.datetime

        event_title : str

        event_type : PostCalendarEventsRequestEventType

        user_id : typing.Optional[float]

        linked_user_ids : typing.Optional[typing.Sequence[float]]

        job_id : typing.Optional[float]

        job_phase_id : typing.Optional[float]

        description : typing.Optional[str]

        frequency : typing.Optional[PostCalendarEventsRequestFrequency]

        interval : typing.Optional[float]

        repeat_end_type : typing.Optional[PostCalendarEventsRequestRepeatEndType]

        repeat_end_date : typing.Optional[dt.date]

        repeat_count : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalendarEventsResponse
            Resource created successfully

        Examples
        --------
        import datetime

        from fern.calendar_events import PostCalendarEventsRequestEventType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.calendar_events.post_calendar_events(
            start_time=datetime.datetime.fromisoformat(
                "2021-01-01 07:00:00+00:00",
            ),
            end_time=datetime.datetime.fromisoformat(
                "2021-01-01 17:00:00+00:00",
            ),
            event_title="eventTitle",
            event_type=PostCalendarEventsRequestEventType.JOB_PHASE,
        )
        """
        _response = self._raw_client.post_calendar_events(
            start_time=start_time,
            end_time=end_time,
            event_title=event_title,
            event_type=event_type,
            user_id=user_id,
            linked_user_ids=linked_user_ids,
            job_id=job_id,
            job_phase_id=job_phase_id,
            description=description,
            frequency=frequency,
            interval=interval,
            repeat_end_type=repeat_end_type,
            repeat_end_date=repeat_end_date,
            repeat_count=repeat_count,
            request_options=request_options,
        )
        return _response.data

    def get_calendar_events_calendar_event_id(
        self, calendar_event_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CalendarEventByIdResponse:
        """
        Returns a CalendarEvent by ID.

        Parameters
        ----------
        calendar_event_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalendarEventByIdResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.calendar_events.get_calendar_events_calendar_event_id(
            calendar_event_id=1.1,
        )
        """
        _response = self._raw_client.get_calendar_events_calendar_event_id(
            calendar_event_id, request_options=request_options
        )
        return _response.data

    def post_calendar_events_calendar_event_id(
        self,
        calendar_event_id: float,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        event_title: str,
        description: typing.Optional[str] = OMIT,
        user_id: typing.Optional[float] = OMIT,
        linked_user_ids: typing.Optional[typing.Sequence[float]] = OMIT,
        frequency: typing.Optional[PostCalendarEventsCalendarEventIdRequestFrequency] = OMIT,
        interval: typing.Optional[float] = OMIT,
        repeat_end_type: typing.Optional[PostCalendarEventsCalendarEventIdRequestRepeatEndType] = OMIT,
        repeat_end_date: typing.Optional[dt.date] = OMIT,
        repeat_count: typing.Optional[float] = OMIT,
        repeat_split_on_date: typing.Optional[dt.datetime] = OMIT,
        update_all_recurring: typing.Optional[PostCalendarEventsCalendarEventIdRequestUpdateAllRecurring] = OMIT,
        update_all_grouped: typing.Optional[PostCalendarEventsCalendarEventIdRequestUpdateAllGrouped] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CalendarEventsResponse:
        """
        Updates a calendar event.
          - To set the event to update to recurring, **frequency** must be set to a value other than `NEVER`.
            - **interval** controls how often the event repeats,
              - Example:  `WEEKLY` with an `interval = 2`, the event repeats every 2 weeks.
              - Default is `1`.
            - **repeatEndType** must be one of:
              - `NEVER`: Repeats indefinitely. Default value.
              - `ON_DATE`: Repeats until the specified **repeatEndDate**.
              - `AFTER`: Repeats for the specified **repeatCount** number of occurrences.
            - If `repeatEndType = ON_DATE`, the **repeatEndDate** must be provided.
            - If `repeatEndType = AFTER`, the **repeatCount** must be provided.
          - If the event to update is recurring, **updateAllRecurring** must be specified:
            - If **updateAllRecurring** is true, all future occurrences of the current event are updated.
            - If **updateAllRecurring** is false, only the current event is updated and future occurrences are not updated.
              - An optional **repeatSplitOnDate** can be provided and the event is only updated on the specified date and future occurrences are not updated.
              - if the **repeatSplitOnDate** is not provided, this is set to the event's **startTime** value.
          - If the event to update is assigned to a group, **updateAllGrouped** must be specified:
            - If **updateAllGrouped** is true, all events in the group are updated otherwise only the current event is updated.
          - To assign the event to update, **userId** or **linkedUserIds** can be provided, and the event is assigned to those user(s). Otherwise, the event is unassigned.
            - When assigning to a group, i.e. the **linkedUserIds** is provided, the **updateAllGrouped** property must be set to true.


        Parameters
        ----------
        calendar_event_id : float

        start_time : dt.datetime

        end_time : dt.datetime

        event_title : str

        description : typing.Optional[str]

        user_id : typing.Optional[float]

        linked_user_ids : typing.Optional[typing.Sequence[float]]

        frequency : typing.Optional[PostCalendarEventsCalendarEventIdRequestFrequency]

        interval : typing.Optional[float]

        repeat_end_type : typing.Optional[PostCalendarEventsCalendarEventIdRequestRepeatEndType]

        repeat_end_date : typing.Optional[dt.date]

        repeat_count : typing.Optional[float]

        repeat_split_on_date : typing.Optional[dt.datetime]

        update_all_recurring : typing.Optional[PostCalendarEventsCalendarEventIdRequestUpdateAllRecurring]

        update_all_grouped : typing.Optional[PostCalendarEventsCalendarEventIdRequestUpdateAllGrouped]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalendarEventsResponse
            Successful Response

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.calendar_events.post_calendar_events_calendar_event_id(
            calendar_event_id=1.1,
            start_time=datetime.datetime.fromisoformat(
                "2021-01-01 07:00:00+00:00",
            ),
            end_time=datetime.datetime.fromisoformat(
                "2021-01-01 17:00:00+00:00",
            ),
            event_title="eventTitle",
        )
        """
        _response = self._raw_client.post_calendar_events_calendar_event_id(
            calendar_event_id,
            start_time=start_time,
            end_time=end_time,
            event_title=event_title,
            description=description,
            user_id=user_id,
            linked_user_ids=linked_user_ids,
            frequency=frequency,
            interval=interval,
            repeat_end_type=repeat_end_type,
            repeat_end_date=repeat_end_date,
            repeat_count=repeat_count,
            repeat_split_on_date=repeat_split_on_date,
            update_all_recurring=update_all_recurring,
            update_all_grouped=update_all_grouped,
            request_options=request_options,
        )
        return _response.data

    def delete_calendar_events_calendar_event_id(
        self,
        calendar_event_id: float,
        *,
        delete_on_date: typing.Optional[dt.datetime] = OMIT,
        delete_all_recurring: typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring] = OMIT,
        delete_all_grouped: typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a calendar event.
          - If the event to delete is recurring, **deleteAllRecurring** must be specified:
            - If **deleteAllRecurring** is true, all future occurrences of the event are deleted
            - If **deleteAllRecurring** is false, an optional **deleteOnDate** can be provided.
              - if **deleteOnDate** is provided, the event is split and the event is only deleted on the specified date and previous or future events are not deleted.
              - if the **deleteOnDate** is not provided, this is set to the event's **startTime** value.
          - If the event to delete is assigned to a group, **deleteAllGrouped** must be specified:
            - If **deleteAllGrouped** is true, all events in the group are deleted otherwise only the current event is deleted.


        Parameters
        ----------
        calendar_event_id : float

        delete_on_date : typing.Optional[dt.datetime]

        delete_all_recurring : typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring]

        delete_all_grouped : typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.calendar_events.delete_calendar_events_calendar_event_id(
            calendar_event_id=1.1,
        )
        """
        _response = self._raw_client.delete_calendar_events_calendar_event_id(
            calendar_event_id,
            delete_on_date=delete_on_date,
            delete_all_recurring=delete_all_recurring,
            delete_all_grouped=delete_all_grouped,
            request_options=request_options,
        )
        return _response.data


class AsyncCalendarEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCalendarEventsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCalendarEventsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCalendarEventsClient
        """
        return self._raw_client

    async def get_calendar_events(
        self,
        *,
        filter_calendar_event_type: typing.Optional[GetCalendarEventsRequestFilterCalendarEventType] = None,
        filter_user_id: typing.Optional[float] = None,
        filter_job_id: typing.Optional[float] = None,
        filter_job_phase_id: typing.Optional[float] = None,
        filter_job_events_only: typing.Optional[bool] = None,
        filter_non_job_events_only: typing.Optional[bool] = None,
        filter_unassigned_events_only: typing.Optional[bool] = None,
        filter_active_only: typing.Optional[bool] = None,
        filter_date_from: typing.Optional[dt.datetime] = None,
        filter_calendar_range: typing.Optional[GetCalendarEventsRequestFilterCalendarRange] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CalendarEventsResponse:
        """
        Returns a list of CalendarEvents. The list can be filtered by user name, event type or active events only.

        Parameters
        ----------
        filter_calendar_event_type : typing.Optional[GetCalendarEventsRequestFilterCalendarEventType]

        filter_user_id : typing.Optional[float]

        filter_job_id : typing.Optional[float]

        filter_job_phase_id : typing.Optional[float]

        filter_job_events_only : typing.Optional[bool]

        filter_non_job_events_only : typing.Optional[bool]

        filter_unassigned_events_only : typing.Optional[bool]

        filter_active_only : typing.Optional[bool]

        filter_date_from : typing.Optional[dt.datetime]
            The start date for filtering calendar events, in ISO 8601 format.

            - The time portion is discarded only the date is used.

            - A timezone offset (+/-HH:MM or +/-HHMM) is expected to ensure accurate timezone interpretation.

            - If none is provided, the value will be treated as UTC.

        filter_calendar_range : typing.Optional[GetCalendarEventsRequestFilterCalendarRange]
            The filterDateFrom (or currentDate if not provided) sets the start of the period.

            - For DAY and THREE_DAY options, it's that exact date.

            - For WEEK and MONTH options, it's the week or month that includes that date (weeks run Monday to Sunday).

            - For FORTNIGHT option, it starts at the Monday of the week that contains that date.

            This defaults to WEEK if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalendarEventsResponse
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
            await client.calendar_events.get_calendar_events(
                filter_date_from=datetime.datetime.fromisoformat(
                    "2025-12-01 11:00:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_calendar_events(
            filter_calendar_event_type=filter_calendar_event_type,
            filter_user_id=filter_user_id,
            filter_job_id=filter_job_id,
            filter_job_phase_id=filter_job_phase_id,
            filter_job_events_only=filter_job_events_only,
            filter_non_job_events_only=filter_non_job_events_only,
            filter_unassigned_events_only=filter_unassigned_events_only,
            filter_active_only=filter_active_only,
            filter_date_from=filter_date_from,
            filter_calendar_range=filter_calendar_range,
            request_options=request_options,
        )
        return _response.data

    async def post_calendar_events(
        self,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        event_title: str,
        event_type: PostCalendarEventsRequestEventType,
        user_id: typing.Optional[float] = OMIT,
        linked_user_ids: typing.Optional[typing.Sequence[float]] = OMIT,
        job_id: typing.Optional[float] = OMIT,
        job_phase_id: typing.Optional[float] = OMIT,
        description: typing.Optional[str] = OMIT,
        frequency: typing.Optional[PostCalendarEventsRequestFrequency] = OMIT,
        interval: typing.Optional[float] = OMIT,
        repeat_end_type: typing.Optional[PostCalendarEventsRequestRepeatEndType] = OMIT,
        repeat_end_date: typing.Optional[dt.date] = OMIT,
        repeat_count: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CalendarEventsResponse:
        """
        Creates a new calendar event.
          - **eventType** must be one of : `JOB_PHASE`, `QUOTE`, `ESTIMATE`, `OTHER`.
            - **JOB_PHASE**: Event type for a job phase. `jobPhaseId` must be provided.
            - **QUOTE**: Event type for a quote. `jobId` must be provided.
            - **ESTIMATE**: Event type for an estimate. `jobId` must be provided.
            - **OTHER**: General event type. Default value.
          - **frequency** must be one of : `DAILY`, `WEEKLY`, `MONTHLY`, `YEARLY`, `NEVER`.
            - **DAILY**: Repeats every day.
            - **WEEKLY**: Repeats every week.
            - **MONTHLY**: Repeats every month.
            - **YEARLY**: Repeats every year.
            - **NEVER**: Does not repeat. Default value.
          - If the event is recurring, **frequency** is ***not*** `NEVER`.
            - **interval** controls how often the event repeats,
              - Example:  `WEEKLY` with an `interval = 2`, the event repeats every 2 weeks.
              - Default is `1`.
            - **repeatEndType** must be one of:
              - `NEVER`: Repeats indefinitely. Default value.
              - `ON_DATE`: Repeats until the specified **repeatEndDate**.
              - `AFTER`: Repeats for the specified **repeatCount** number of occurrences.
            - If `repeatEndType = ON_DATE`, the **repeatEndDate** must be provided.
            - If `repeatEndType = AFTER`, the **repeatCount** must be provided.
          - If **userId** or **linkedUserIds** is provided, the event is assigned to those user(s). Otherwise, the event is unassigned.


        Parameters
        ----------
        start_time : dt.datetime

        end_time : dt.datetime

        event_title : str

        event_type : PostCalendarEventsRequestEventType

        user_id : typing.Optional[float]

        linked_user_ids : typing.Optional[typing.Sequence[float]]

        job_id : typing.Optional[float]

        job_phase_id : typing.Optional[float]

        description : typing.Optional[str]

        frequency : typing.Optional[PostCalendarEventsRequestFrequency]

        interval : typing.Optional[float]

        repeat_end_type : typing.Optional[PostCalendarEventsRequestRepeatEndType]

        repeat_end_date : typing.Optional[dt.date]

        repeat_count : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalendarEventsResponse
            Resource created successfully

        Examples
        --------
        import asyncio
        import datetime

        from fern.calendar_events import PostCalendarEventsRequestEventType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calendar_events.post_calendar_events(
                start_time=datetime.datetime.fromisoformat(
                    "2021-01-01 07:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2021-01-01 17:00:00+00:00",
                ),
                event_title="eventTitle",
                event_type=PostCalendarEventsRequestEventType.JOB_PHASE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_calendar_events(
            start_time=start_time,
            end_time=end_time,
            event_title=event_title,
            event_type=event_type,
            user_id=user_id,
            linked_user_ids=linked_user_ids,
            job_id=job_id,
            job_phase_id=job_phase_id,
            description=description,
            frequency=frequency,
            interval=interval,
            repeat_end_type=repeat_end_type,
            repeat_end_date=repeat_end_date,
            repeat_count=repeat_count,
            request_options=request_options,
        )
        return _response.data

    async def get_calendar_events_calendar_event_id(
        self, calendar_event_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CalendarEventByIdResponse:
        """
        Returns a CalendarEvent by ID.

        Parameters
        ----------
        calendar_event_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalendarEventByIdResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calendar_events.get_calendar_events_calendar_event_id(
                calendar_event_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_calendar_events_calendar_event_id(
            calendar_event_id, request_options=request_options
        )
        return _response.data

    async def post_calendar_events_calendar_event_id(
        self,
        calendar_event_id: float,
        *,
        start_time: dt.datetime,
        end_time: dt.datetime,
        event_title: str,
        description: typing.Optional[str] = OMIT,
        user_id: typing.Optional[float] = OMIT,
        linked_user_ids: typing.Optional[typing.Sequence[float]] = OMIT,
        frequency: typing.Optional[PostCalendarEventsCalendarEventIdRequestFrequency] = OMIT,
        interval: typing.Optional[float] = OMIT,
        repeat_end_type: typing.Optional[PostCalendarEventsCalendarEventIdRequestRepeatEndType] = OMIT,
        repeat_end_date: typing.Optional[dt.date] = OMIT,
        repeat_count: typing.Optional[float] = OMIT,
        repeat_split_on_date: typing.Optional[dt.datetime] = OMIT,
        update_all_recurring: typing.Optional[PostCalendarEventsCalendarEventIdRequestUpdateAllRecurring] = OMIT,
        update_all_grouped: typing.Optional[PostCalendarEventsCalendarEventIdRequestUpdateAllGrouped] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CalendarEventsResponse:
        """
        Updates a calendar event.
          - To set the event to update to recurring, **frequency** must be set to a value other than `NEVER`.
            - **interval** controls how often the event repeats,
              - Example:  `WEEKLY` with an `interval = 2`, the event repeats every 2 weeks.
              - Default is `1`.
            - **repeatEndType** must be one of:
              - `NEVER`: Repeats indefinitely. Default value.
              - `ON_DATE`: Repeats until the specified **repeatEndDate**.
              - `AFTER`: Repeats for the specified **repeatCount** number of occurrences.
            - If `repeatEndType = ON_DATE`, the **repeatEndDate** must be provided.
            - If `repeatEndType = AFTER`, the **repeatCount** must be provided.
          - If the event to update is recurring, **updateAllRecurring** must be specified:
            - If **updateAllRecurring** is true, all future occurrences of the current event are updated.
            - If **updateAllRecurring** is false, only the current event is updated and future occurrences are not updated.
              - An optional **repeatSplitOnDate** can be provided and the event is only updated on the specified date and future occurrences are not updated.
              - if the **repeatSplitOnDate** is not provided, this is set to the event's **startTime** value.
          - If the event to update is assigned to a group, **updateAllGrouped** must be specified:
            - If **updateAllGrouped** is true, all events in the group are updated otherwise only the current event is updated.
          - To assign the event to update, **userId** or **linkedUserIds** can be provided, and the event is assigned to those user(s). Otherwise, the event is unassigned.
            - When assigning to a group, i.e. the **linkedUserIds** is provided, the **updateAllGrouped** property must be set to true.


        Parameters
        ----------
        calendar_event_id : float

        start_time : dt.datetime

        end_time : dt.datetime

        event_title : str

        description : typing.Optional[str]

        user_id : typing.Optional[float]

        linked_user_ids : typing.Optional[typing.Sequence[float]]

        frequency : typing.Optional[PostCalendarEventsCalendarEventIdRequestFrequency]

        interval : typing.Optional[float]

        repeat_end_type : typing.Optional[PostCalendarEventsCalendarEventIdRequestRepeatEndType]

        repeat_end_date : typing.Optional[dt.date]

        repeat_count : typing.Optional[float]

        repeat_split_on_date : typing.Optional[dt.datetime]

        update_all_recurring : typing.Optional[PostCalendarEventsCalendarEventIdRequestUpdateAllRecurring]

        update_all_grouped : typing.Optional[PostCalendarEventsCalendarEventIdRequestUpdateAllGrouped]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CalendarEventsResponse
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
            await client.calendar_events.post_calendar_events_calendar_event_id(
                calendar_event_id=1.1,
                start_time=datetime.datetime.fromisoformat(
                    "2021-01-01 07:00:00+00:00",
                ),
                end_time=datetime.datetime.fromisoformat(
                    "2021-01-01 17:00:00+00:00",
                ),
                event_title="eventTitle",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_calendar_events_calendar_event_id(
            calendar_event_id,
            start_time=start_time,
            end_time=end_time,
            event_title=event_title,
            description=description,
            user_id=user_id,
            linked_user_ids=linked_user_ids,
            frequency=frequency,
            interval=interval,
            repeat_end_type=repeat_end_type,
            repeat_end_date=repeat_end_date,
            repeat_count=repeat_count,
            repeat_split_on_date=repeat_split_on_date,
            update_all_recurring=update_all_recurring,
            update_all_grouped=update_all_grouped,
            request_options=request_options,
        )
        return _response.data

    async def delete_calendar_events_calendar_event_id(
        self,
        calendar_event_id: float,
        *,
        delete_on_date: typing.Optional[dt.datetime] = OMIT,
        delete_all_recurring: typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring] = OMIT,
        delete_all_grouped: typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a calendar event.
          - If the event to delete is recurring, **deleteAllRecurring** must be specified:
            - If **deleteAllRecurring** is true, all future occurrences of the event are deleted
            - If **deleteAllRecurring** is false, an optional **deleteOnDate** can be provided.
              - if **deleteOnDate** is provided, the event is split and the event is only deleted on the specified date and previous or future events are not deleted.
              - if the **deleteOnDate** is not provided, this is set to the event's **startTime** value.
          - If the event to delete is assigned to a group, **deleteAllGrouped** must be specified:
            - If **deleteAllGrouped** is true, all events in the group are deleted otherwise only the current event is deleted.


        Parameters
        ----------
        calendar_event_id : float

        delete_on_date : typing.Optional[dt.datetime]

        delete_all_recurring : typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring]

        delete_all_grouped : typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calendar_events.delete_calendar_events_calendar_event_id(
                calendar_event_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_calendar_events_calendar_event_id(
            calendar_event_id,
            delete_on_date=delete_on_date,
            delete_all_recurring=delete_all_recurring,
            delete_all_grouped=delete_all_grouped,
            request_options=request_options,
        )
        return _response.data
