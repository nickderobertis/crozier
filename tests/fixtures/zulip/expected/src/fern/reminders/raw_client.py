

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.json_success import JsonSuccess
from .types.create_message_reminder_response import CreateMessageReminderResponse
from .types.get_reminders_response import GetRemindersResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRemindersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_reminders(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetRemindersResponse]:
        """
        Fetch all [reminders](/help/schedule-a-reminder) for the
        current user.

        Reminders are messages the user has scheduled to be sent in the
        future to themself.

        **Changes**: New in Zulip 11.0 (feature level 399).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetRemindersResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "reminders",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRemindersResponse,
                    parse_obj_as(
                        type_=GetRemindersResponse,
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

    def create_message_reminder(
        self,
        *,
        message_id: typing.Optional[int] = OMIT,
        scheduled_delivery_timestamp: typing.Optional[int] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateMessageReminderResponse]:
        """
        Schedule a reminder to be sent to the current user at the specified time. The reminder will link the relevant message.

        **Changes**: New in Zulip 11.0 (feature level 381).

        Parameters
        ----------
        message_id : typing.Optional[int]
            The ID of the previously sent message to reference in the reminder message.

        scheduled_delivery_timestamp : typing.Optional[int]
            The UNIX timestamp for when the reminder will be sent,
            in UTC seconds.

        note : typing.Optional[str]
            A note associated with the reminder shown in the Notification Bot message.

            **Changes**: New in Zulip 11.0 (feature level 415).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateMessageReminderResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "reminders",
            method="POST",
            data={
                "message_id": message_id,
                "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
                "note": note,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateMessageReminderResponse,
                    parse_obj_as(
                        type_=CreateMessageReminderResponse,
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

    def delete_reminder(
        self, reminder_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Delete, and therefore cancel sending, a previously [scheduled
        reminder](/help/schedule-a-reminder).

        **Changes**: New in Zulip 11.0 (feature level 399).

        Parameters
        ----------
        reminder_id : int
            The ID of the reminder to delete.

            This is different from the unique ID that the message would have
            after being sent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"reminders/{encode_path_param(reminder_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawRemindersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_reminders(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetRemindersResponse]:
        """
        Fetch all [reminders](/help/schedule-a-reminder) for the
        current user.

        Reminders are messages the user has scheduled to be sent in the
        future to themself.

        **Changes**: New in Zulip 11.0 (feature level 399).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetRemindersResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "reminders",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetRemindersResponse,
                    parse_obj_as(
                        type_=GetRemindersResponse,
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

    async def create_message_reminder(
        self,
        *,
        message_id: typing.Optional[int] = OMIT,
        scheduled_delivery_timestamp: typing.Optional[int] = OMIT,
        note: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateMessageReminderResponse]:
        """
        Schedule a reminder to be sent to the current user at the specified time. The reminder will link the relevant message.

        **Changes**: New in Zulip 11.0 (feature level 381).

        Parameters
        ----------
        message_id : typing.Optional[int]
            The ID of the previously sent message to reference in the reminder message.

        scheduled_delivery_timestamp : typing.Optional[int]
            The UNIX timestamp for when the reminder will be sent,
            in UTC seconds.

        note : typing.Optional[str]
            A note associated with the reminder shown in the Notification Bot message.

            **Changes**: New in Zulip 11.0 (feature level 415).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateMessageReminderResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "reminders",
            method="POST",
            data={
                "message_id": message_id,
                "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
                "note": note,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateMessageReminderResponse,
                    parse_obj_as(
                        type_=CreateMessageReminderResponse,
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

    async def delete_reminder(
        self, reminder_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Delete, and therefore cancel sending, a previously [scheduled
        reminder](/help/schedule-a-reminder).

        **Changes**: New in Zulip 11.0 (feature level 399).

        Parameters
        ----------
        reminder_id : int
            The ID of the reminder to delete.

            This is different from the unique ID that the message would have
            after being sent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"reminders/{encode_path_param(reminder_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
