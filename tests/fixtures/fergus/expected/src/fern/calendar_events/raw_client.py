

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.calendar_event_by_id_response import CalendarEventByIdResponse
from ..types.calendar_events_response import CalendarEventsResponse
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCalendarEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[CalendarEventsResponse]:
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
        HttpResponse[CalendarEventsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "calendarEvents",
            method="GET",
            params={
                "filterCalendarEventType": filter_calendar_event_type,
                "filterUserId": filter_user_id,
                "filterJobId": filter_job_id,
                "filterJobPhaseId": filter_job_phase_id,
                "filterJobEventsOnly": filter_job_events_only,
                "filterNonJobEventsOnly": filter_non_job_events_only,
                "filterUnassignedEventsOnly": filter_unassigned_events_only,
                "filterActiveOnly": filter_active_only,
                "filterDateFrom": serialize_datetime(filter_date_from) if filter_date_from is not None else None,
                "filterCalendarRange": filter_calendar_range,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CalendarEventsResponse,
                    parse_obj_as(
                        type_=CalendarEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[CalendarEventsResponse]:
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
        HttpResponse[CalendarEventsResponse]
            Resource created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "calendarEvents",
            method="POST",
            json={
                "userId": user_id,
                "linkedUserIds": linked_user_ids,
                "startTime": start_time,
                "endTime": end_time,
                "jobId": job_id,
                "jobPhaseId": job_phase_id,
                "eventTitle": event_title,
                "eventType": event_type,
                "description": description,
                "frequency": frequency,
                "interval": interval,
                "repeatEndType": repeat_end_type,
                "repeatEndDate": repeat_end_date,
                "repeatCount": repeat_count,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CalendarEventsResponse,
                    parse_obj_as(
                        type_=CalendarEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_calendar_events_calendar_event_id(
        self, calendar_event_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CalendarEventByIdResponse]:
        """
        Returns a CalendarEvent by ID.

        Parameters
        ----------
        calendar_event_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CalendarEventByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"calendarEvents/{encode_path_param(calendar_event_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CalendarEventByIdResponse,
                    parse_obj_as(
                        type_=CalendarEventByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[CalendarEventsResponse]:
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
        HttpResponse[CalendarEventsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"calendarEvents/{encode_path_param(calendar_event_id)}",
            method="POST",
            json={
                "startTime": start_time,
                "endTime": end_time,
                "eventTitle": event_title,
                "description": description,
                "userId": user_id,
                "linkedUserIds": linked_user_ids,
                "frequency": frequency,
                "interval": interval,
                "repeatEndType": repeat_end_type,
                "repeatEndDate": repeat_end_date,
                "repeatCount": repeat_count,
                "repeatSplitOnDate": repeat_split_on_date,
                "updateAllRecurring": update_all_recurring,
                "updateAllGrouped": update_all_grouped,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CalendarEventsResponse,
                    parse_obj_as(
                        type_=CalendarEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_calendar_events_calendar_event_id(
        self,
        calendar_event_id: float,
        *,
        delete_on_date: typing.Optional[dt.datetime] = OMIT,
        delete_all_recurring: typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring] = OMIT,
        delete_all_grouped: typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"calendarEvents/{encode_path_param(calendar_event_id)}",
            method="DELETE",
            json={
                "deleteOnDate": delete_on_date,
                "deleteAllRecurring": delete_all_recurring,
                "deleteAllGrouped": delete_all_grouped,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCalendarEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[CalendarEventsResponse]:
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
        AsyncHttpResponse[CalendarEventsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "calendarEvents",
            method="GET",
            params={
                "filterCalendarEventType": filter_calendar_event_type,
                "filterUserId": filter_user_id,
                "filterJobId": filter_job_id,
                "filterJobPhaseId": filter_job_phase_id,
                "filterJobEventsOnly": filter_job_events_only,
                "filterNonJobEventsOnly": filter_non_job_events_only,
                "filterUnassignedEventsOnly": filter_unassigned_events_only,
                "filterActiveOnly": filter_active_only,
                "filterDateFrom": serialize_datetime(filter_date_from) if filter_date_from is not None else None,
                "filterCalendarRange": filter_calendar_range,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CalendarEventsResponse,
                    parse_obj_as(
                        type_=CalendarEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[CalendarEventsResponse]:
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
        AsyncHttpResponse[CalendarEventsResponse]
            Resource created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "calendarEvents",
            method="POST",
            json={
                "userId": user_id,
                "linkedUserIds": linked_user_ids,
                "startTime": start_time,
                "endTime": end_time,
                "jobId": job_id,
                "jobPhaseId": job_phase_id,
                "eventTitle": event_title,
                "eventType": event_type,
                "description": description,
                "frequency": frequency,
                "interval": interval,
                "repeatEndType": repeat_end_type,
                "repeatEndDate": repeat_end_date,
                "repeatCount": repeat_count,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CalendarEventsResponse,
                    parse_obj_as(
                        type_=CalendarEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_calendar_events_calendar_event_id(
        self, calendar_event_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CalendarEventByIdResponse]:
        """
        Returns a CalendarEvent by ID.

        Parameters
        ----------
        calendar_event_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CalendarEventByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"calendarEvents/{encode_path_param(calendar_event_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CalendarEventByIdResponse,
                    parse_obj_as(
                        type_=CalendarEventByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[CalendarEventsResponse]:
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
        AsyncHttpResponse[CalendarEventsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"calendarEvents/{encode_path_param(calendar_event_id)}",
            method="POST",
            json={
                "startTime": start_time,
                "endTime": end_time,
                "eventTitle": event_title,
                "description": description,
                "userId": user_id,
                "linkedUserIds": linked_user_ids,
                "frequency": frequency,
                "interval": interval,
                "repeatEndType": repeat_end_type,
                "repeatEndDate": repeat_end_date,
                "repeatCount": repeat_count,
                "repeatSplitOnDate": repeat_split_on_date,
                "updateAllRecurring": update_all_recurring,
                "updateAllGrouped": update_all_grouped,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CalendarEventsResponse,
                    parse_obj_as(
                        type_=CalendarEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_calendar_events_calendar_event_id(
        self,
        calendar_event_id: float,
        *,
        delete_on_date: typing.Optional[dt.datetime] = OMIT,
        delete_all_recurring: typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring] = OMIT,
        delete_all_grouped: typing.Optional[DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"calendarEvents/{encode_path_param(calendar_event_id)}",
            method="DELETE",
            json={
                "deleteOnDate": delete_on_date,
                "deleteAllRecurring": delete_all_recurring,
                "deleteAllGrouped": delete_all_grouped,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
