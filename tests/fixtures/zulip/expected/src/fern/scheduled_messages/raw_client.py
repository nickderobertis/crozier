

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.json_success import JsonSuccess
from ..types.required_content import RequiredContent
from .types.create_scheduled_message_request_to import CreateScheduledMessageRequestTo
from .types.create_scheduled_message_request_type import CreateScheduledMessageRequestType
from .types.create_scheduled_message_response import CreateScheduledMessageResponse
from .types.get_scheduled_messages_response import GetScheduledMessagesResponse
from .types.update_scheduled_message_request_to import UpdateScheduledMessageRequestTo
from .types.update_scheduled_message_request_type import UpdateScheduledMessageRequestType
from .types.update_scheduled_message_response import UpdateScheduledMessageResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawScheduledMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_scheduled_messages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetScheduledMessagesResponse]:
        """
        Fetch all [scheduled messages](/help/schedule-a-message) for
        the current user.

        Scheduled messages are messages the user has scheduled to be
        sent in the future via the send later feature.

        **Changes**: New in Zulip 7.0 (feature level 173).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetScheduledMessagesResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "scheduled_messages",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetScheduledMessagesResponse,
                    parse_obj_as(
                        type_=GetScheduledMessagesResponse,
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

    def create_scheduled_message(
        self,
        *,
        type: CreateScheduledMessageRequestType,
        to: CreateScheduledMessageRequestTo,
        content: RequiredContent,
        scheduled_delivery_timestamp: int,
        topic: typing.Optional[str] = OMIT,
        read_by_sender: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateScheduledMessageResponse]:
        """
        Create a new [scheduled message](/help/schedule-a-message).

        **Changes**: In Zulip 7.0 (feature level 184), moved support for
        [editing a scheduled message](/api/update-scheduled-message) to a
        separate API endpoint, which removed the `scheduled_message_id`
        parameter from this endpoint.

        New in Zulip 7.0 (feature level 179).

        Parameters
        ----------
        type : CreateScheduledMessageRequestType
            The type of scheduled message to be sent. `"direct"` for a direct
            message and `"stream"` or `"channel"` for a channel message.

            Note that, while `"private"` is supported for scheduling direct
            messages, clients are encouraged to use to the modern convention of
            `"direct"` to indicate this message type, because support for
            `"private"` may eventually be removed.

            **Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
            an additional value for this parameter to indicate the type of a channel
            message.

        to : CreateScheduledMessageRequestTo
            The scheduled message's tentative target audience.

            For channel messages, the integer ID of the channel.
            For direct messages, a list containing integer user IDs.

        content : RequiredContent

        scheduled_delivery_timestamp : int
            The UNIX timestamp for when the message will be sent,
            in UTC seconds.

        topic : typing.Optional[str]
            The topic of the message. Only required for channel messages
            (`"type": "stream"` or `"type": "channel"`), ignored otherwise.

            Clients should use the `max_topic_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum topic length.

            Note: When `"(no topic)"` or the value of `realm_empty_topic_display_name`
            found in the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            When [topics are required](/help/require-topics), this parameter can't
            be `"(no topic)"`, an empty string, or the value of `realm_empty_topic_display_name`.

            **Changes**: Before Zulip 10.0 (feature level 370), `"(no topic)"`
            was not interpreted as an empty string.

            Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

        read_by_sender : typing.Optional[bool]
            Whether the message should be initially marked read by its
            sender. If unspecified, the server uses a heuristic based
            on the client name and the recipient.

            **Changes**: New in Zulip 8.0 (feature level 236).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateScheduledMessageResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "scheduled_messages",
            method="POST",
            data={
                "type": type,
                "to": convert_and_respect_annotation_metadata(
                    object_=to, annotation=CreateScheduledMessageRequestTo, direction="write"
                ),
                "content": content,
                "topic": topic,
                "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
                "read_by_sender": read_by_sender,
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
                    CreateScheduledMessageResponse,
                    parse_obj_as(
                        type_=CreateScheduledMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def delete_scheduled_message(
        self, scheduled_message_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Delete, and therefore cancel sending, a previously [scheduled
        message](/help/schedule-a-message).

        **Changes**: New in Zulip 7.0 (feature level 173).

        Parameters
        ----------
        scheduled_message_id : int
            The ID of the scheduled message to delete.

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
            f"scheduled_messages/{encode_path_param(scheduled_message_id)}",
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

    def update_scheduled_message(
        self,
        scheduled_message_id: int,
        *,
        type: typing.Optional[UpdateScheduledMessageRequestType] = OMIT,
        to: typing.Optional[UpdateScheduledMessageRequestTo] = OMIT,
        content: typing.Optional[str] = OMIT,
        topic: typing.Optional[str] = OMIT,
        scheduled_delivery_timestamp: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateScheduledMessageResponse]:
        """
        Edit an existing [scheduled message](/help/schedule-a-message).

        **Changes**: New in Zulip 7.0 (feature level 184).

        Parameters
        ----------
        scheduled_message_id : int
            The ID of the scheduled message to update.

            This is different from the unique ID that the message would have
            after being sent.

        type : typing.Optional[UpdateScheduledMessageRequestType]
            The type of scheduled message to be sent. `"direct"` for a direct
            message and `"stream"` or `"channel"` for a channel message.

            When updating the type of the scheduled message, the `to` parameter
            is required. And, if updating the type of the scheduled message to
            `"stream"`/`"channel"`, then the `topic` parameter is also required.

            Note that, while `"private"` is supported for scheduling direct
            messages, clients are encouraged to use to the modern convention of
            `"direct"` to indicate this message type, because support for
            `"private"` may eventually be removed.

            **Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
            an additional value for this parameter to indicate the type of a channel
            message.

        to : typing.Optional[UpdateScheduledMessageRequestTo]
            The scheduled message's tentative target audience.

            For channel messages, the integer ID of the channel.
            For direct messages, a list containing integer user IDs.

            Required when updating the `type` of the scheduled message.

        content : typing.Optional[str]
            The updated content of the scheduled message.

            Clients should use the `max_message_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum message size.

        topic : typing.Optional[str]
            The updated topic of the scheduled message.

            Required when updating the `type` of the scheduled message to
            `"stream"` or `"channel"`. Ignored when the existing or updated
            `type` of the scheduled message is `"direct"` (or `"private"`).

            Clients should use the `max_topic_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum topic length.

            Note: When `"(no topic)"` or the value of `realm_empty_topic_display_name`
            found in the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            When [topics are required](/help/require-topics), this parameter can't
            be `"(no topic)"`, an empty string, or the value of `realm_empty_topic_display_name`.

            **Changes**: Before Zulip 10.0 (feature level 370), `"(no topic)"`
            was not interpreted as an empty string.

            Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

        scheduled_delivery_timestamp : typing.Optional[int]
            The UNIX timestamp for when the message will be sent,
            in UTC seconds.

            Required when updating a scheduled message that the server
            has already tried and failed to send. This state is indicated
            with `"failed": true` in `scheduled_messages` objects; see
            response description at
            [`GET /scheduled_messages`](/api/get-scheduled-messages#response).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateScheduledMessageResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"scheduled_messages/{encode_path_param(scheduled_message_id)}",
            method="PATCH",
            data={
                "type": type,
                "to": convert_and_respect_annotation_metadata(
                    object_=to, annotation=UpdateScheduledMessageRequestTo, direction="write"
                ),
                "content": content,
                "topic": topic,
                "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
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
                    UpdateScheduledMessageResponse,
                    parse_obj_as(
                        type_=UpdateScheduledMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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


class AsyncRawScheduledMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_scheduled_messages(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetScheduledMessagesResponse]:
        """
        Fetch all [scheduled messages](/help/schedule-a-message) for
        the current user.

        Scheduled messages are messages the user has scheduled to be
        sent in the future via the send later feature.

        **Changes**: New in Zulip 7.0 (feature level 173).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetScheduledMessagesResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "scheduled_messages",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetScheduledMessagesResponse,
                    parse_obj_as(
                        type_=GetScheduledMessagesResponse,
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

    async def create_scheduled_message(
        self,
        *,
        type: CreateScheduledMessageRequestType,
        to: CreateScheduledMessageRequestTo,
        content: RequiredContent,
        scheduled_delivery_timestamp: int,
        topic: typing.Optional[str] = OMIT,
        read_by_sender: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateScheduledMessageResponse]:
        """
        Create a new [scheduled message](/help/schedule-a-message).

        **Changes**: In Zulip 7.0 (feature level 184), moved support for
        [editing a scheduled message](/api/update-scheduled-message) to a
        separate API endpoint, which removed the `scheduled_message_id`
        parameter from this endpoint.

        New in Zulip 7.0 (feature level 179).

        Parameters
        ----------
        type : CreateScheduledMessageRequestType
            The type of scheduled message to be sent. `"direct"` for a direct
            message and `"stream"` or `"channel"` for a channel message.

            Note that, while `"private"` is supported for scheduling direct
            messages, clients are encouraged to use to the modern convention of
            `"direct"` to indicate this message type, because support for
            `"private"` may eventually be removed.

            **Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
            an additional value for this parameter to indicate the type of a channel
            message.

        to : CreateScheduledMessageRequestTo
            The scheduled message's tentative target audience.

            For channel messages, the integer ID of the channel.
            For direct messages, a list containing integer user IDs.

        content : RequiredContent

        scheduled_delivery_timestamp : int
            The UNIX timestamp for when the message will be sent,
            in UTC seconds.

        topic : typing.Optional[str]
            The topic of the message. Only required for channel messages
            (`"type": "stream"` or `"type": "channel"`), ignored otherwise.

            Clients should use the `max_topic_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum topic length.

            Note: When `"(no topic)"` or the value of `realm_empty_topic_display_name`
            found in the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            When [topics are required](/help/require-topics), this parameter can't
            be `"(no topic)"`, an empty string, or the value of `realm_empty_topic_display_name`.

            **Changes**: Before Zulip 10.0 (feature level 370), `"(no topic)"`
            was not interpreted as an empty string.

            Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

        read_by_sender : typing.Optional[bool]
            Whether the message should be initially marked read by its
            sender. If unspecified, the server uses a heuristic based
            on the client name and the recipient.

            **Changes**: New in Zulip 8.0 (feature level 236).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateScheduledMessageResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "scheduled_messages",
            method="POST",
            data={
                "type": type,
                "to": convert_and_respect_annotation_metadata(
                    object_=to, annotation=CreateScheduledMessageRequestTo, direction="write"
                ),
                "content": content,
                "topic": topic,
                "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
                "read_by_sender": read_by_sender,
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
                    CreateScheduledMessageResponse,
                    parse_obj_as(
                        type_=CreateScheduledMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def delete_scheduled_message(
        self, scheduled_message_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Delete, and therefore cancel sending, a previously [scheduled
        message](/help/schedule-a-message).

        **Changes**: New in Zulip 7.0 (feature level 173).

        Parameters
        ----------
        scheduled_message_id : int
            The ID of the scheduled message to delete.

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
            f"scheduled_messages/{encode_path_param(scheduled_message_id)}",
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

    async def update_scheduled_message(
        self,
        scheduled_message_id: int,
        *,
        type: typing.Optional[UpdateScheduledMessageRequestType] = OMIT,
        to: typing.Optional[UpdateScheduledMessageRequestTo] = OMIT,
        content: typing.Optional[str] = OMIT,
        topic: typing.Optional[str] = OMIT,
        scheduled_delivery_timestamp: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateScheduledMessageResponse]:
        """
        Edit an existing [scheduled message](/help/schedule-a-message).

        **Changes**: New in Zulip 7.0 (feature level 184).

        Parameters
        ----------
        scheduled_message_id : int
            The ID of the scheduled message to update.

            This is different from the unique ID that the message would have
            after being sent.

        type : typing.Optional[UpdateScheduledMessageRequestType]
            The type of scheduled message to be sent. `"direct"` for a direct
            message and `"stream"` or `"channel"` for a channel message.

            When updating the type of the scheduled message, the `to` parameter
            is required. And, if updating the type of the scheduled message to
            `"stream"`/`"channel"`, then the `topic` parameter is also required.

            Note that, while `"private"` is supported for scheduling direct
            messages, clients are encouraged to use to the modern convention of
            `"direct"` to indicate this message type, because support for
            `"private"` may eventually be removed.

            **Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
            an additional value for this parameter to indicate the type of a channel
            message.

        to : typing.Optional[UpdateScheduledMessageRequestTo]
            The scheduled message's tentative target audience.

            For channel messages, the integer ID of the channel.
            For direct messages, a list containing integer user IDs.

            Required when updating the `type` of the scheduled message.

        content : typing.Optional[str]
            The updated content of the scheduled message.

            Clients should use the `max_message_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum message size.

        topic : typing.Optional[str]
            The updated topic of the scheduled message.

            Required when updating the `type` of the scheduled message to
            `"stream"` or `"channel"`. Ignored when the existing or updated
            `type` of the scheduled message is `"direct"` (or `"private"`).

            Clients should use the `max_topic_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum topic length.

            Note: When `"(no topic)"` or the value of `realm_empty_topic_display_name`
            found in the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            When [topics are required](/help/require-topics), this parameter can't
            be `"(no topic)"`, an empty string, or the value of `realm_empty_topic_display_name`.

            **Changes**: Before Zulip 10.0 (feature level 370), `"(no topic)"`
            was not interpreted as an empty string.

            Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

        scheduled_delivery_timestamp : typing.Optional[int]
            The UNIX timestamp for when the message will be sent,
            in UTC seconds.

            Required when updating a scheduled message that the server
            has already tried and failed to send. This state is indicated
            with `"failed": true` in `scheduled_messages` objects; see
            response description at
            [`GET /scheduled_messages`](/api/get-scheduled-messages#response).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateScheduledMessageResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"scheduled_messages/{encode_path_param(scheduled_message_id)}",
            method="PATCH",
            data={
                "type": type,
                "to": convert_and_respect_annotation_metadata(
                    object_=to, annotation=UpdateScheduledMessageRequestTo, direction="write"
                ),
                "content": content,
                "topic": topic,
                "scheduled_delivery_timestamp": scheduled_delivery_timestamp,
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
                    UpdateScheduledMessageResponse,
                    parse_obj_as(
                        type_=UpdateScheduledMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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
