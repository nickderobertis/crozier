

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.anchor import Anchor
from ..types.emoji_code import EmojiCode
from ..types.json_success import JsonSuccess
from ..types.optional_content import OptionalContent
from ..types.reaction_type import ReactionType
from ..types.required_content import RequiredContent
from .types.check_messages_match_narrow_response import CheckMessagesMatchNarrowResponse
from .types.check_thumbnail_status_response import CheckThumbnailStatusResponse
from .types.get_file_temporary_url_response import GetFileTemporaryUrlResponse
from .types.get_message_history_response import GetMessageHistoryResponse
from .types.get_message_response import GetMessageResponse
from .types.get_messages_response import GetMessagesResponse
from .types.get_read_receipts_response import GetReadReceiptsResponse
from .types.mark_all_as_read_response import MarkAllAsReadResponse
from .types.render_message_response import RenderMessageResponse
from .types.send_message_request_to import SendMessageRequestTo
from .types.send_message_request_type import SendMessageRequestType
from .types.send_message_response import SendMessageResponse
from .types.update_message_flags_for_narrow_request_narrow_item import UpdateMessageFlagsForNarrowRequestNarrowItem
from .types.update_message_flags_for_narrow_request_op import UpdateMessageFlagsForNarrowRequestOp
from .types.update_message_flags_for_narrow_response import UpdateMessageFlagsForNarrowResponse
from .types.update_message_flags_request_op import UpdateMessageFlagsRequestOp
from .types.update_message_flags_response import UpdateMessageFlagsResponse
from .types.update_message_request_propagate_mode import UpdateMessageRequestPropagateMode
from .types.update_message_response import UpdateMessageResponse
from .types.upload_file_response import UploadFileResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def mark_all_as_read(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MarkAllAsReadResponse]:
        """
        Marks all of the current user's unread messages as read.

        Because this endpoint marks messages as read in batches, it is possible
        for the request to time out after only marking some messages as read.
        When this happens, the `complete` boolean field in the success response
        will be `false`. Clients should repeat the request when handling such a
        response. If all messages were marked as read, then the success response
        will return `"complete": true`.

        **Changes**: Deprecated; clients should use the [update personal message
        flags for narrow](/api/update-message-flags-for-narrow) endpoint instead
        as this endpoint will be removed in a future release.

        Before Zulip 8.0 (feature level 211), if the server's
        processing was interrupted by a timeout, but some messages were marked
        as read, then it would return `"result": "partially_completed"`, along
        with a `code` field for an error string, in the success response to
        indicate that there was a timeout and that the client should repeat the
        request.

        Before Zulip 6.0 (feature level 153), this request did a single atomic
        operation, which could time out with 10,000s of unread messages to mark
        as read. As of this feature level, messages are marked as read in
        batches, starting with the newest messages, so that progress is made
        even if the request times out. And, instead of returning an error when
        the request times out and some messages have been marked as read, a
        success response with `"result": "partially_completed"` is returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MarkAllAsReadResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "mark_all_as_read",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarkAllAsReadResponse,
                    parse_obj_as(
                        type_=MarkAllAsReadResponse,
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

    def mark_stream_as_read(
        self, *, stream_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Mark all the unread messages in a channel as read.

        **Changes**: Deprecated; clients should use the [update personal message
        flags for narrow](/api/update-message-flags-for-narrow) endpoint instead
        as this endpoint will be removed in a future release.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "mark_stream_as_read",
            method="POST",
            data={
                "stream_id": stream_id,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    def mark_topic_as_read(
        self, *, stream_id: int, topic_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Mark all the unread messages in a topic as read.

        **Changes**: Deprecated; clients should use the [update personal message
        flags for narrow](/api/update-message-flags-for-narrow) endpoint instead
        as this endpoint will be removed in a future release.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        topic_name : str
            The name of the topic whose messages should be marked as read.

            Note: When the value of `realm_empty_topic_display_name` found in
            the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            **Changes**: Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "mark_topic_as_read",
            method="POST",
            data={
                "stream_id": stream_id,
                "topic_name": topic_name,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    def get_messages(
        self,
        *,
        anchor: typing.Optional[Anchor] = None,
        include_anchor: typing.Optional[bool] = None,
        anchor_date: typing.Optional[str] = None,
        num_before: typing.Optional[int] = None,
        num_after: typing.Optional[int] = None,
        narrow: typing.Optional[str] = None,
        client_gravatar: typing.Optional[bool] = None,
        apply_markdown: typing.Optional[bool] = None,
        use_first_unread_anchor: typing.Optional[bool] = None,
        message_ids: typing.Optional[str] = None,
        allow_empty_topic_name: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetMessagesResponse]:
        """
        This endpoint is the primary way to fetch messages. It is used by all official
        Zulip clients (e.g. the web, desktop, mobile, and terminal clients) as well as
        many bots, API clients, backup scripts, etc.

        Most queries will specify a [narrow filter](/api/get-messages#parameter-narrow),
        to fetch the messages matching any supported [search
        query](/help/search-for-messages). If not specified, it will return messages
        corresponding to the user's [combined feed](/help/combined-feed). There are two
        ways to specify which messages matching the narrow filter to fetch:

        - A range of messages, described by an `anchor` message ID (or a string-format
          specification of how the server should computer an anchor to use) and a maximum
          number of messages in each direction from that anchor.

        - A rarely used variant (`message_ids`) where the client specifies the message IDs
          to fetch.

        The server returns the matching messages, sorted by message ID, as well as some
        metadata that makes it easy for a client to determine whether there are more
        messages matching the query that were not returned due to the `num_before` and
        `num_after` limits.

        Note that a user's message history does not contain messages sent to
        channels before they [subscribe](/api/subscribe), and newly created
        bot users are not usually subscribed to any channels.

        We recommend requesting at most 1000 messages in a batch, to avoid generating very
        large HTTP responses. A maximum of 5000 messages can be obtained per request;
        attempting to exceed this will result in an error.

        **Changes**: The `message_ids` option is new in Zulip 10.0 (feature level 300).

        Parameters
        ----------
        anchor : typing.Optional[Anchor]
            Integer message ID to anchor fetching of new messages. Supports special
            string values for when the client wants the server to compute the anchor
            to use:

            - `newest`: The most recent message.
            - `oldest`: The oldest message.
            - `first_unread`: The oldest unread message matching the
              query, if any; otherwise, the most recent message.
            - `date`: The first message on or after the datetime indicated by the
              [`anchor_date`](#parameter-anchor_date), if any; otherwise, the most
              recent message.

            **Changes**: The `date` value is new in Zulip 12.0 (feature level 445).

            String values are new in Zulip 3.0 (feature level 1). The
            `first_unread` functionality was supported in Zulip 2.1.x
            and older by not sending `anchor` and using `use_first_unread_anchor`.

            In Zulip 2.1.x and older, `oldest` can be emulated with
            `"anchor": 0`, and `newest` with `"anchor": 10000000000000000`
            (that specific large value works around a bug in Zulip
            2.1.x and older in the `found_newest` return value).

        include_anchor : typing.Optional[bool]
            Whether a message with the specified ID matching the narrow
            should be included.

            **Changes**: New in Zulip 6.0 (feature level 155).

        anchor_date : typing.Optional[str]
            The date or datetime to use for finding the anchor message when `anchor` is
            `date`. Accepted formats include ISO 8601 date-only strings
            (e.g. `2005-04-18`) as well as full datetime strings
            (e.g. `2005-04-18T12:34:56Z`). If only a date is provided, the datetime is set to
            midnight (00:00) on that day in UTC. If no timezone is provided, UTC is
            assumed.

            **Changes**: New in Zulip 12.0 (feature level 445).

        num_before : typing.Optional[int]
            The number of messages with IDs less than the anchor to retrieve.
            Required if `message_ids` is not provided.

        num_after : typing.Optional[int]
            The number of messages with IDs greater than the anchor to retrieve.
            Required if `message_ids` is not provided.

        narrow : typing.Optional[str]
            The narrow where you want to fetch the messages from. See how to
            [construct a narrow](/api/construct-narrow).

            Note that many narrows, including all that lack a `channel`, `channels`,
            `stream`, or `streams` operator, search the user's personal message
            history. See [searching shared
            history](/help/search-for-messages#search-shared-history)
            for details.

            For example, if you would like to fetch messages from all public channels instead
            of only the user's message history, then a specific narrow for
            messages sent to all public channels can be used:
            `{"operator": "channels", "operand": "public"}`.

            Newly created bot users are not usually subscribed to any
            channels, so bots using this API should either be
            subscribed to appropriate channels or use a shared history
            search narrow with this endpoint.

            **Changes**: See [changes section](/api/construct-narrow#changes)
            of search/narrow filter documentation.

        client_gravatar : typing.Optional[bool]
            Whether the client supports computing gravatars URLs. If
            enabled, `avatar_url` will be included in the response only
            if there is a Zulip avatar, and will be `null` for users who
            are using gravatar as their avatar. This option
            significantly reduces the compressed size of user data,
            since gravatar URLs are long, random strings and thus do not
            compress well. The `client_gravatar` field is set to `true` if
            clients can compute their own gravatars.

            **Changes**: The default value of this parameter was `false`
            prior to Zulip 5.0 (feature level 92).

        apply_markdown : typing.Optional[bool]
            If `true`, message content is returned in the rendered HTML
            format. If `false`, message content is returned in the raw
            Markdown-format text that user entered.

            See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.

        use_first_unread_anchor : typing.Optional[bool]
            Legacy way to specify `"anchor": "first_unread"` in Zulip 2.1.x and older.

            Whether to use the (computed by the server) first unread message
            matching the narrow as the `anchor`. Mutually exclusive with `anchor`.

            **Changes**: Deprecated in Zulip 3.0 (feature level 1) and replaced by
            `"anchor": "first_unread"`.

        message_ids : typing.Optional[str]
            A list of message IDs to fetch. The server will return messages corresponding to the
            subset of the requested message IDs that exist and the current user has access to,
            potentially filtered by the narrow (if that parameter is provided).

            It is an error to pass this parameter as well as any of the parameters involved in
            specifying a range of messages: `anchor`, `include_anchor`, `use_first_unread_anchor`,
            `num_before`, and `num_after`.

            **Changes**: New in Zulip 10.0 (feature level 300). Previously, there was
            no way to request a specific set of messages IDs.

        allow_empty_topic_name : typing.Optional[bool]
            Whether the client supports processing the empty string as a topic in the
            topic name fields in the returned data, including in returned edit_history data.

            If `false`, the server will use the value of `realm_empty_topic_display_name`
            found in the [`POST /register`](/api/register-queue) response instead of empty string
            to represent the empty string topic in its response.

            **Changes**: New in Zulip 10.0 (feature level 334). Previously, the empty string
            was not a valid topic.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMessagesResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "messages",
            method="GET",
            params={
                "anchor": anchor,
                "include_anchor": include_anchor,
                "anchor_date": anchor_date,
                "num_before": num_before,
                "num_after": num_after,
                "narrow": narrow,
                "client_gravatar": client_gravatar,
                "apply_markdown": apply_markdown,
                "use_first_unread_anchor": use_first_unread_anchor,
                "message_ids": message_ids,
                "allow_empty_topic_name": allow_empty_topic_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMessagesResponse,
                    parse_obj_as(
                        type_=GetMessagesResponse,
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

    def send_message(
        self,
        *,
        type: SendMessageRequestType,
        to: SendMessageRequestTo,
        content: RequiredContent,
        topic: typing.Optional[str] = OMIT,
        queue_id: typing.Optional[str] = OMIT,
        local_id: typing.Optional[str] = OMIT,
        read_by_sender: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SendMessageResponse]:
        """
        Send a [channel message](/help/introduction-to-topics) or a
        [direct message](/help/direct-messages).

        Parameters
        ----------
        type : SendMessageRequestType
            The type of message to be sent.

            `"direct"` for a direct message and `"stream"` or `"channel"` for a
            channel message.

            **Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
            an additional value for this parameter to request a channel message.

            In Zulip 7.0 (feature level 174), `"direct"` was added as
            the preferred way to request a direct message, deprecating the original
            `"private"`. While `"private"` is still supported for requesting direct
            messages, clients are encouraged to use to the modern convention with
            servers that support it, because support for `"private"` will eventually
            be removed.

        to : SendMessageRequestTo
            The channel or users receiving the message.

            For channel messages, this is either the name or integer ID of the
            channel.

            For direct messages, this is either a list containing integer user IDs or
            a list containing string Zulip API email addresses. The ID or email
            address of the user sending the message can be included in the list, but
            will be ignored by the server, unless the user sending the message is the
            only recipient of the message.

            **Changes**: In Zulip 2.0.0, support for using user/channel IDs was added.

        content : RequiredContent

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

            New in Zulip 2.0.0. Previous Zulip releases encoded
            this as `subject`, which is currently a deprecated alias.

        queue_id : typing.Optional[str]
            For clients supporting
            [local echo](https://zulip.readthedocs.io/en/latest/subsystems/sending-messages.html#local-echo),
            the [event queue](/api/register-queue) ID for the client.

            If passed, `local_id` is required.

            If the message is successfully sent, the server will include
            `local_message_id` in the [`message` event](/api/get-events#message) that
            the client with this `queue_id` will receive.

        local_id : typing.Optional[str]
            For clients supporting
            [local echo](https://zulip.readthedocs.io/en/latest/subsystems/sending-messages.html#local-echo),
            a unique string-format identifier chosen freely by the client.

            If passed, `queue_id` is required.

            If the message is successfully sent, the server will pass it back to
            the client without inspecting it as `local_message_id` in the
            [`message` event](/api/get-events#message) that the client with the
            above `queue_id` will receive.

        read_by_sender : typing.Optional[bool]
            Whether the message should be initially marked read by its
            sender. If unspecified, the server uses a heuristic based
            on the client name.

            **Changes**: New in Zulip 8.0 (feature level 236).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SendMessageResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "messages",
            method="POST",
            data={
                "type": type,
                "to": convert_and_respect_annotation_metadata(
                    object_=to, annotation=SendMessageRequestTo, direction="write"
                ),
                "content": content,
                "topic": topic,
                "queue_id": queue_id,
                "local_id": local_id,
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
                    SendMessageResponse,
                    parse_obj_as(
                        type_=SendMessageResponse,
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

    def get_message_history(
        self,
        message_id: int,
        *,
        allow_empty_topic_name: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetMessageHistoryResponse]:
        """
        Fetch the message edit history of a previously edited message.

        Note that edit history may be disabled in some organizations; see the
        [Zulip help center documentation on editing messages][edit-settings].

        [edit-settings]: /help/view-a-messages-edit-history

        Parameters
        ----------
        message_id : int
            The target message's ID.

        allow_empty_topic_name : typing.Optional[bool]
            Whether the topic names i.e. `topic` and `prev_topic` fields in
            the `message_history` objects returned can be empty string.

            If `false`, the value of `realm_empty_topic_display_name`
            found in the [`POST /register`](/api/register-queue) response is
            returned replacing the empty string as the topic name.

            **Changes**: New in Zulip 10.0 (feature level 334).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMessageHistoryResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}/history",
            method="GET",
            params={
                "allow_empty_topic_name": allow_empty_topic_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMessageHistoryResponse,
                    parse_obj_as(
                        type_=GetMessageHistoryResponse,
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

    def update_message_flags(
        self,
        *,
        messages: typing.Sequence[int],
        op: UpdateMessageFlagsRequestOp,
        flag: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateMessageFlagsResponse]:
        """
        Add or remove personal message flags like `read` and `starred`
        on a collection of message IDs.

        See also the endpoint for [updating flags on a range of
        messages within a narrow](/api/update-message-flags-for-narrow).

        Parameters
        ----------
        messages : typing.Sequence[int]
            An array containing the IDs of the target messages.

        op : UpdateMessageFlagsRequestOp
            Whether to `add` the flag or `remove` it.

        flag : str
            The flag that should be added/removed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateMessageFlagsResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "messages/flags",
            method="POST",
            data={
                "messages": messages,
                "op": op,
                "flag": flag,
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
                    UpdateMessageFlagsResponse,
                    parse_obj_as(
                        type_=UpdateMessageFlagsResponse,
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

    def update_message_flags_for_narrow(
        self,
        *,
        anchor: str,
        num_before: int,
        num_after: int,
        narrow: typing.Sequence[UpdateMessageFlagsForNarrowRequestNarrowItem],
        op: UpdateMessageFlagsForNarrowRequestOp,
        flag: str,
        include_anchor: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateMessageFlagsForNarrowResponse]:
        """
        Add or remove personal message flags like `read` and `starred`
        on a range of messages within a narrow.

        See also [the endpoint for updating flags on specific message
        IDs](/api/update-message-flags).

        **Changes**: New in Zulip 6.0 (feature level 155).

        Parameters
        ----------
        anchor : str
            Integer message ID to anchor updating of flags. Supports special
            string values for when the client wants the server to compute the anchor
            to use:

            - `newest`: The most recent message.
            - `oldest`: The oldest message.
            - `first_unread`: The oldest unread message matching the
              query, if any; otherwise, the most recent message.

        num_before : int
            Limit the number of messages preceding the anchor in the
            update range. The server may decrease this to bound
            transaction sizes.

        num_after : int
            Limit the number of messages following the anchor in the
            update range. The server may decrease this to bound
            transaction sizes.

        narrow : typing.Sequence[UpdateMessageFlagsForNarrowRequestNarrowItem]
            The narrow you want update flags within. See how to
            [construct a narrow](/api/construct-narrow).

            Note that, when adding the `read` flag to messages, clients should
            consider including a narrow with the `is:unread` filter as an
            optimization. Including that filter takes advantage of the fact that
            the server has a database index for unread messages.

            **Changes**: See [changes section](/api/construct-narrow#changes)
            of search/narrow filter documentation.

        op : UpdateMessageFlagsForNarrowRequestOp
            Whether to `add` the flag or `remove` it.

        flag : str
            The flag that should be added/removed. See [available
            flags](/api/update-message-flags#available-flags).

        include_anchor : typing.Optional[bool]
            Whether a message with the specified ID matching the narrow
            should be included in the update range.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateMessageFlagsForNarrowResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "messages/flags/narrow",
            method="POST",
            data={
                "anchor": anchor,
                "include_anchor": include_anchor,
                "num_before": num_before,
                "num_after": num_after,
                "narrow": convert_and_respect_annotation_metadata(
                    object_=narrow,
                    annotation=typing.Sequence[UpdateMessageFlagsForNarrowRequestNarrowItem],
                    direction="write",
                ),
                "op": op,
                "flag": flag,
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
                    UpdateMessageFlagsForNarrowResponse,
                    parse_obj_as(
                        type_=UpdateMessageFlagsForNarrowResponse,
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

    def render_message(
        self, *, content: RequiredContent, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RenderMessageResponse]:
        """
        Render a message to HTML.

        Parameters
        ----------
        content : RequiredContent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RenderMessageResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "messages/render",
            method="POST",
            data={
                "content": content,
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
                    RenderMessageResponse,
                    parse_obj_as(
                        type_=RenderMessageResponse,
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

    def add_reaction(
        self,
        message_id: int,
        *,
        emoji_name: str,
        emoji_code: typing.Optional[EmojiCode] = OMIT,
        reaction_type: typing.Optional[ReactionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JsonSuccess]:
        """
        Add an [emoji reaction](/help/emoji-reactions) to a message.

        Parameters
        ----------
        message_id : int
            The target message's ID.

        emoji_name : str
            The target emoji's human-readable name.

            To find an emoji's name, hover over a message to reveal
            three icons on the right, then click the smiley face icon.
            Images of available reaction emojis appear. Hover over the
            emoji you want, and note that emoji's text name.

        emoji_code : typing.Optional[EmojiCode]

        reaction_type : typing.Optional[ReactionType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}/reactions",
            method="POST",
            data={
                "emoji_name": emoji_name,
                "emoji_code": emoji_code,
                "reaction_type": reaction_type,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    def remove_reaction(
        self,
        message_id: int,
        *,
        emoji_name: typing.Optional[str] = OMIT,
        emoji_code: typing.Optional[EmojiCode] = OMIT,
        reaction_type: typing.Optional[ReactionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JsonSuccess]:
        """
        Remove an [emoji reaction](/help/emoji-reactions) from a message.

        Parameters
        ----------
        message_id : int
            The target message's ID.

        emoji_name : typing.Optional[str]
            The target emoji's human-readable name.

            To find an emoji's name, hover over a message to reveal
            three icons on the right, then click the smiley face icon.
            Images of available reaction emojis appear. Hover over the
            emoji you want, and note that emoji's text name.

        emoji_code : typing.Optional[EmojiCode]

        reaction_type : typing.Optional[ReactionType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}/reactions",
            method="DELETE",
            data={
                "emoji_name": emoji_name,
                "emoji_code": emoji_code,
                "reaction_type": reaction_type,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    def get_read_receipts(
        self, message_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetReadReceiptsResponse]:
        """
        Returns a list containing the IDs for all users who have
        marked the message as read (and whose privacy settings allow
        sharing that information).

        The list of users IDs will include any bots who have marked
        the message as read via the API (providing a way for bots to
        indicate whether they have processed a message successfully in
        a way that can be easily inspected in a Zulip client). Bots
        for which this behavior is not desired may disable the
        `send_read_receipts` setting via the API.

        It will never contain the message's sender.

        **Changes**: New in Zulip 6.0 (feature level 137).

        Parameters
        ----------
        message_id : int
            The target message's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetReadReceiptsResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}/read_receipts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetReadReceiptsResponse,
                    parse_obj_as(
                        type_=GetReadReceiptsResponse,
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

    def check_messages_match_narrow(
        self, *, msg_ids: str, narrow: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CheckMessagesMatchNarrowResponse]:
        """
        Check whether a set of messages match a [narrow](/api/construct-narrow).

        For many common narrows (e.g. a topic), clients can write an efficient
        client-side check to determine whether a newly arrived message belongs
        in the view.

        This endpoint is designed to allow clients to handle more complex narrows
        for which the client does not (or in the case of full-text search, cannot)
        implement this check.

        The format of the `match_subject` and `match_content` objects is designed
        to match those returned by the [`GET /messages`](/api/get-messages#response)
        endpoint, so that a client can splice these fields into a `message` object
        received from [`GET /events`](/api/get-events#message) and end up with an
        extended message object identical to how a [`GET /messages`](/api/get-messages)
        request for the current narrow would have returned the message.

        Parameters
        ----------
        msg_ids : str
            List of IDs for the messages to check.

        narrow : str
            A structure defining the narrow to check against. See how to
            [construct a narrow](/api/construct-narrow).

            **Changes**: See [changes section](/api/construct-narrow#changes)
            of search/narrow filter documentation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckMessagesMatchNarrowResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "messages/matches_narrow",
            method="GET",
            params={
                "msg_ids": msg_ids,
                "narrow": narrow,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckMessagesMatchNarrowResponse,
                    parse_obj_as(
                        type_=CheckMessagesMatchNarrowResponse,
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

    def get_message(
        self,
        message_id: int,
        *,
        apply_markdown: typing.Optional[bool] = None,
        allow_empty_topic_name: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetMessageResponse]:
        """
        Given a message ID, return the message object.

        Additionally, a `raw_content` field is included. This field is
        useful for clients that primarily work with HTML-rendered
        messages but might need to occasionally fetch the message's
        raw [Zulip-flavored Markdown](/help/format-your-message-using-markdown) (e.g. for [view
        source](/help/view-the-markdown-source-of-a-message) or
        prefilling a message edit textarea).

        **Changes**: Before Zulip 5.0 (feature level 120), this
        endpoint only returned the `raw_content` field.

        Parameters
        ----------
        message_id : int
            The target message's ID.

        apply_markdown : typing.Optional[bool]
            If `true`, message content is returned in the rendered HTML
            format. If `false`, message content is returned in the raw
            [Zulip-flavored Markdown format](/help/format-your-message-using-markdown) text that user entered.

            **Changes**: New in Zulip 5.0 (feature level 120).

        allow_empty_topic_name : typing.Optional[bool]
            Whether the client supports processing the empty string as a topic in the
            topic name fields in the returned data, including in returned edit_history data.

            If `false`, the server will use the value of `realm_empty_topic_display_name`
            found in the [`POST /register`](/api/register-queue) response instead of empty string
            to represent the empty string topic in its response.

            **Changes**: New in Zulip 10.0 (feature level 334). Previously, the empty string
            was not a valid topic.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetMessageResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}",
            method="GET",
            params={
                "apply_markdown": apply_markdown,
                "allow_empty_topic_name": allow_empty_topic_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMessageResponse,
                    parse_obj_as(
                        type_=GetMessageResponse,
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

    def delete_message(
        self, message_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Permanently delete a message.

        This API corresponds to the [delete a message completely][delete-completely]
        feature documented in the Zulip help center.

        A user must be able to access the content of a message in order to delete it.
        See [channel permissions](/help/channel-permissions) for more information
        about content access for channel messages. For direct messages, the user
        must have received or sent the direct message to have content access.

        See [restricting message deletion](/help/restrict-message-editing-and-deletion)
        for documentation on when users are allowed to delete messages.

        The relevant realm settings in the API that are related to the above linked
        documentation on when users are allowed to delete messages are:

        - `realm_can_delete_any_message_group`
        - `realm_can_delete_own_message_group`
        - `realm_can_set_delete_message_policy_group`
        - `realm_message_content_delete_limit_seconds`

        The relevant per-channel permission settings in the API that are related to the
        above linked documentation on when users are allowed to delete messages in a
        specific channel are:

        - `can_delete_any_message_group`
        - `can_delete_own_message_group`

        More details about these realm and channel settings can be found in the
        [`POST /register`](/api/register-queue) response.

        **Changes**: Prior to Zulip 10.0 (feature level 281), only organization
        administrators had permission to permanently delete a message.

        [delete-completely]: /help/delete-a-message#delete-a-message-completely

        Parameters
        ----------
        message_id : int
            The target message's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}",
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

    def update_message(
        self,
        message_id: int,
        *,
        topic: typing.Optional[str] = OMIT,
        propagate_mode: typing.Optional[UpdateMessageRequestPropagateMode] = OMIT,
        send_notification_to_old_thread: typing.Optional[bool] = OMIT,
        send_notification_to_new_thread: typing.Optional[bool] = OMIT,
        content: typing.Optional[OptionalContent] = OMIT,
        prev_content_sha256: typing.Optional[str] = OMIT,
        stream_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateMessageResponse]:
        """
        Update the content, topic, or channel of the message with the specified
        ID.

        You can [resolve topics](/help/resolve-a-topic) by editing the topic to
        `✔ {original_topic}` with the `propagate_mode` parameter set to
        `"change_all"`.

        See [configuring message editing][config-message-editing] for detailed
        documentation on when users are allowed to edit message content, and
        [restricting moving messages][restrict-move-messages] for detailed
        documentation on when users are allowed to change a message's topic
        and/or channel.

        The relevant realm settings in the API that are related to the above
        linked documentation on when users are allowed to update messages are:

        - `allow_message_editing`
        - `can_resolve_topics_group`
        - `can_move_messages_between_channels_group`
        - `can_move_messages_between_topics_group`
        - `message_content_edit_limit_seconds`
        - `move_messages_within_stream_limit_seconds`
        - `move_messages_between_streams_limit_seconds`

        More details about these realm settings can be found in the
        [`POST /register`](/api/register-queue) response or in the documentation
        of the [`realm op: update_dict`](/api/get-events#realm-update_dict)
        event in [`GET /events`](/api/get-events).

        **Changes**: Prior to Zulip 10.0 (feature level 367), the permission for
        resolving a topic was managed by `can_move_messages_between_topics_group`.
        As of this feature level, users belonging to the `can_resolve_topics_group`
        will have the permission to [resolve topics](/help/resolve-a-topic) in the organization.

        In Zulip 10.0 (feature level 316), `edit_topic_policy`
        was removed and replaced by `can_move_messages_between_topics_group`
        realm setting.

        **Changes**: In Zulip 10.0 (feature level 310), `move_messages_between_streams_policy`
        was removed and replaced by `can_move_messages_between_channels_group`
        realm setting.

        Prior to Zulip 7.0 (feature level 172), anyone could add a
        topic to channel messages without a topic, regardless of the organization's
        [topic editing permissions](/help/restrict-moving-messages). As of this
        feature level, messages without topics have the same restrictions for
        topic edits as messages with topics.

        Before Zulip 7.0 (feature level 172), by using the `change_all` value for
        the `propagate_mode` parameter, users could move messages after the
        organization's configured time limits for changing a message's topic or
        channel had passed. As of this feature level, the server will [return an
        error](/api/update-message#response) with `"code":
        "MOVE_MESSAGES_TIME_LIMIT_EXCEEDED"` if users, other than organization
        administrators or moderators, try to move messages after these time
        limits have passed.

        Before Zulip 7.0 (feature level 162), users who were not administrators or
        moderators could only edit topics if the target message was sent within the
        last 3 days. As of this feature level, that time limit is now controlled by
        the realm setting `move_messages_within_stream_limit_seconds`. Also at this
        feature level, a similar time limit for moving messages between channels was
        added, controlled by the realm setting
        `move_messages_between_streams_limit_seconds`. Previously, all users who
        had permission to move messages between channels did not have any time limit
        restrictions when doing so.

        Before Zulip 7.0 (feature level 159), editing channels and topics of messages
        was forbidden if the realm setting for `allow_message_editing` was `false`,
        regardless of an organization's configuration for the realm settings
        `edit_topic_policy` or `move_messages_between_streams_policy`.

        Before Zulip 7.0 (feature level 159), message senders were allowed to edit
        the topic of their messages indefinitely.

        In Zulip 5.0 (feature level 75), the `edit_topic_policy` realm setting
        was added, replacing the `allow_community_topic_editing` boolean.

        In Zulip 4.0 (feature level 56), the `move_messages_between_streams_policy`
        realm setting was added.

        [config-message-editing]: /help/restrict-message-editing-and-deletion
        [restrict-move-messages]: /help/restrict-moving-messages

        Parameters
        ----------
        message_id : int
            The target message's ID.

        topic : typing.Optional[str]
            The topic to move the message(s) to, to request changing the topic.

            Clients should use the `max_topic_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum topic length

            Should only be sent when changing the topic, and will throw an error
            if the target message is not a channel message.

            Note: When the value of `realm_empty_topic_display_name` found in
            the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            When [topics are required](/help/require-topics), this parameter can't
            be `"(no topic)"`, an empty string, or the value of `realm_empty_topic_display_name`.

            You can [resolve topics](/help/resolve-a-topic) by editing the topic to
            `✔ {original_topic}` with the `propagate_mode` parameter set to
            `"change_all"`. The empty string topic cannot be marked as resolved.

            **Changes**: Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

            New in Zulip 2.0.0. Previous Zulip releases encoded this as `subject`,
            which is currently a deprecated alias.

        propagate_mode : typing.Optional[UpdateMessageRequestPropagateMode]
            Which message(s) should be edited:

            - `"change_later"`: The target message and all following messages.
            - `"change_one"`: Only the target message.
            - `"change_all"`: All messages in this topic.

            Only the default value of `"change_one"` is valid when editing
            only the content of a message.

            This parameter determines both which messages get moved and also whether
            clients that are currently narrowed to the topic containing the message
            should navigate or adjust their compose box recipient to point to the
            post-edit channel/topic.

        send_notification_to_old_thread : typing.Optional[bool]
            Whether to send an automated message to the old topic to
            notify users where the messages were moved to.

            **Changes**: Before Zulip 6.0 (feature level 152), this parameter
            had a default of `true` and was ignored unless the channel was changed.

            New in Zulip 3.0 (feature level 9).

        send_notification_to_new_thread : typing.Optional[bool]
            Whether to send an automated message to the new topic to
            notify users where the messages came from.

            If the move is just [resolving/unresolving a topic](/help/resolve-a-topic),
            this parameter will not trigger an additional notification.

            **Changes**: Before Zulip 6.0 (feature level 152), this parameter
            was ignored unless the channel was changed.

            New in Zulip 3.0 (feature level 9).

        content : typing.Optional[OptionalContent]

        prev_content_sha256 : typing.Optional[str]
            An optional SHA-256 hash of the previous raw content of the message
            that the client has at the time of the request.

            If provided, the server will return an error if it does not match the
            SHA-256 hash of the message's content stored in the database.

            Clients can use this feature to prevent races where multiple clients
            save conflicting edits to a message.

            **Changes**: New in Zulip 11.0 (feature level 379).

        stream_id : typing.Optional[int]
            The channel ID to move the message(s) to, to request moving
            messages to another channel.

            Should only be sent when changing the channel. Will throw an error
            if the target message is not a channel message.

            Note that a message's content and channel cannot be changed at the
            same time, so sending both `content` and `stream_id` parameters will
            throw an error.

            **Changes**: Prior to Zulip 13.0 (feature level 509), passing the channel
            ID that the target message is currently in was processed as a successful
            channel move, even if the target message was not moved (i.e., neither its
            channel nor topic were changed).

            New in Zulip 3.0 (feature level 1).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateMessageResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}",
            method="PATCH",
            data={
                "topic": topic,
                "propagate_mode": propagate_mode,
                "send_notification_to_old_thread": send_notification_to_old_thread,
                "send_notification_to_new_thread": send_notification_to_new_thread,
                "content": content,
                "prev_content_sha256": prev_content_sha256,
                "stream_id": stream_id,
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
                    UpdateMessageResponse,
                    parse_obj_as(
                        type_=UpdateMessageResponse,
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

    def report_message(
        self,
        message_id: int,
        *,
        report_type: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JsonSuccess]:
        """
        Sends a notification to the organization's [moderation request
        channel](/help/enable-moderation-requests), if it is configured, that
        reports the targeted message for [review and moderation](/help/report-a-message).

        Clients should check the `moderation_request_channel` realm setting to
        decide whether to show the option to report messages in the UI.

        If the `report_type` parameter value is `"other"`, the `description`
        parameter is required. Clients should also enforce and communicate this
        behavior in the UI.

        **Changes**: Before Zulip 13.0 (feature level 511), this endpoint
        did not return an error if the message report failed to be sent to the
        moderation request channel.

        New in Zulip 11.0 (feature level 382). This API builds on the
        `moderation_request_channel` realm setting, which was added in
        feature level 331.

        Parameters
        ----------
        message_id : int
            The target message's ID.

        report_type : str
            The reason that best describes why the current user is reporting the
            target message for moderation.

            Must be one of the `key` values in the `server_report_message_types`
            field in the [`POST /register`](/api/register-queue) response.

            **Changes**: Prior to Zulip 12.0 (feature level 435), the allowed
            values for this parameter were limited to: `"harassment"`,
            `"inappropriate"`, `"norms"`, `"other"`, `"spam"`.

        description : typing.Optional[str]
            A short description with additional context about why the current user
            is reporting the target message for moderation.

            Clients should limit this string to 1000 Unicode code points.

            If the `report_type` parameter is `"other"`, this parameter is required,
            and its value cannot be an empty string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}/report",
            method="POST",
            data={
                "report_type": report_type,
                "description": description,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    def upload_file(
        self, *, filename: typing.Optional[core.File] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UploadFileResponse]:
        """
        [Upload](/help/share-and-upload-files) a single file and get the corresponding URL.

        Initially, only you will be able to access the link. To share the
        uploaded file, you'll need to [send a message][send-message]
        containing the resulting link. Users who can already access the link
        can reshare it with other users by sending additional Zulip messages
        containing the link.

        The maximum allowed file size is available in the `max_file_upload_size_mib`
        field in the [`POST /register`](/api/register-queue) response. Note that
        large files (25MB+) may fail to upload using this API endpoint due to
        network-layer timeouts, depending on the quality of your connection to the
        Zulip server.

        For uploading larger files, `/api/v1/tus` is an endpoint implementing the
        [`tus` resumable upload protocol](https://tus.io/protocols/resumable-upload),
        which supports uploading arbitrarily large files limited only by the server's
        `max_file_upload_size_mib` (Configured via `MAX_FILE_UPLOAD_SIZE` in
        `/etc/zulip/settings.py`). Clients which send authenticated credentials
        (either via browser-based cookies, or API key via `Authorization` header) may
        use this endpoint to upload files.

        **Changes**: The `api/v1/tus` endpoint supporting resumable uploads was
        introduced in Zulip 10.0 (feature level 296). Previously,
        `max_file_upload_size_mib` was typically 25MB.

        [uploaded-files]: /help/manage-your-uploaded-files
        [send-message]: /api/send-message

        Parameters
        ----------
        filename : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadFileResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "user_uploads",
            method="POST",
            data={},
            files={
                **({"filename": filename} if filename is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadFileResponse,
                    parse_obj_as(
                        type_=UploadFileResponse,
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

    def check_thumbnail_status(
        self, realm_id_str: int, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CheckThumbnailStatusResponse]:
        """
        Check whether a thumbnail exists for a specific file uploaded by a user.
        This endpoint is intended to be polled by clients to determine when
        thumbnail generation is complete.

        **Changes**: New in Zulip 12.0 (feature level 479).

        Parameters
        ----------
        realm_id_str : int
            The realm ID component of the file's `path_id`. If the `path_id` is
            `1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`, the `realm_id_str` would be `1`.

        filename : str
            The file path component of the file's `path_id` (everything
            after the first `/`). If the `path_id` is
            `1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`, the `filename`
            would be `4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckThumbnailStatusResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"thumbnail/status/{encode_path_param(realm_id_str)}/{encode_path_param(filename)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckThumbnailStatusResponse,
                    parse_obj_as(
                        type_=CheckThumbnailStatusResponse,
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

    def get_file_temporary_url(
        self, realm_id_str: int, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetFileTemporaryUrlResponse]:
        """
        Get a temporary URL for access to an [uploaded file](/api/upload-file)
        that doesn't require authentication.

        The `SIGNED_ACCESS_TOKEN_VALIDITY_IN_SECONDS` server setting controls
        the valid length of time for temporary access, which generally is set
        to a default of 60 seconds. Consumers of this API are expected to
        immediately request the URL that it returns, and should not store it
        in any way.

        **Changes**: New in Zulip 3.0 (feature level 1).

        Parameters
        ----------
        realm_id_str : int
            The realm ID component of the file's `path_id`. If the `path_id` is
            `1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`, the `realm_id_str` would be `1`.

        filename : str
            The file path component of the file's `path_id` (everything
            after the first `/`). If the `path_id` is
            `1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`, the `filename`
            would be `4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetFileTemporaryUrlResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user_uploads/{encode_path_param(realm_id_str)}/{encode_path_param(filename)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFileTemporaryUrlResponse,
                    parse_obj_as(
                        type_=GetFileTemporaryUrlResponse,
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


class AsyncRawMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def mark_all_as_read(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MarkAllAsReadResponse]:
        """
        Marks all of the current user's unread messages as read.

        Because this endpoint marks messages as read in batches, it is possible
        for the request to time out after only marking some messages as read.
        When this happens, the `complete` boolean field in the success response
        will be `false`. Clients should repeat the request when handling such a
        response. If all messages were marked as read, then the success response
        will return `"complete": true`.

        **Changes**: Deprecated; clients should use the [update personal message
        flags for narrow](/api/update-message-flags-for-narrow) endpoint instead
        as this endpoint will be removed in a future release.

        Before Zulip 8.0 (feature level 211), if the server's
        processing was interrupted by a timeout, but some messages were marked
        as read, then it would return `"result": "partially_completed"`, along
        with a `code` field for an error string, in the success response to
        indicate that there was a timeout and that the client should repeat the
        request.

        Before Zulip 6.0 (feature level 153), this request did a single atomic
        operation, which could time out with 10,000s of unread messages to mark
        as read. As of this feature level, messages are marked as read in
        batches, starting with the newest messages, so that progress is made
        even if the request times out. And, instead of returning an error when
        the request times out and some messages have been marked as read, a
        success response with `"result": "partially_completed"` is returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MarkAllAsReadResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mark_all_as_read",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MarkAllAsReadResponse,
                    parse_obj_as(
                        type_=MarkAllAsReadResponse,
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

    async def mark_stream_as_read(
        self, *, stream_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Mark all the unread messages in a channel as read.

        **Changes**: Deprecated; clients should use the [update personal message
        flags for narrow](/api/update-message-flags-for-narrow) endpoint instead
        as this endpoint will be removed in a future release.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mark_stream_as_read",
            method="POST",
            data={
                "stream_id": stream_id,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    async def mark_topic_as_read(
        self, *, stream_id: int, topic_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Mark all the unread messages in a topic as read.

        **Changes**: Deprecated; clients should use the [update personal message
        flags for narrow](/api/update-message-flags-for-narrow) endpoint instead
        as this endpoint will be removed in a future release.

        Parameters
        ----------
        stream_id : int
            The ID of the channel to access.

        topic_name : str
            The name of the topic whose messages should be marked as read.

            Note: When the value of `realm_empty_topic_display_name` found in
            the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            **Changes**: Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mark_topic_as_read",
            method="POST",
            data={
                "stream_id": stream_id,
                "topic_name": topic_name,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    async def get_messages(
        self,
        *,
        anchor: typing.Optional[Anchor] = None,
        include_anchor: typing.Optional[bool] = None,
        anchor_date: typing.Optional[str] = None,
        num_before: typing.Optional[int] = None,
        num_after: typing.Optional[int] = None,
        narrow: typing.Optional[str] = None,
        client_gravatar: typing.Optional[bool] = None,
        apply_markdown: typing.Optional[bool] = None,
        use_first_unread_anchor: typing.Optional[bool] = None,
        message_ids: typing.Optional[str] = None,
        allow_empty_topic_name: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetMessagesResponse]:
        """
        This endpoint is the primary way to fetch messages. It is used by all official
        Zulip clients (e.g. the web, desktop, mobile, and terminal clients) as well as
        many bots, API clients, backup scripts, etc.

        Most queries will specify a [narrow filter](/api/get-messages#parameter-narrow),
        to fetch the messages matching any supported [search
        query](/help/search-for-messages). If not specified, it will return messages
        corresponding to the user's [combined feed](/help/combined-feed). There are two
        ways to specify which messages matching the narrow filter to fetch:

        - A range of messages, described by an `anchor` message ID (or a string-format
          specification of how the server should computer an anchor to use) and a maximum
          number of messages in each direction from that anchor.

        - A rarely used variant (`message_ids`) where the client specifies the message IDs
          to fetch.

        The server returns the matching messages, sorted by message ID, as well as some
        metadata that makes it easy for a client to determine whether there are more
        messages matching the query that were not returned due to the `num_before` and
        `num_after` limits.

        Note that a user's message history does not contain messages sent to
        channels before they [subscribe](/api/subscribe), and newly created
        bot users are not usually subscribed to any channels.

        We recommend requesting at most 1000 messages in a batch, to avoid generating very
        large HTTP responses. A maximum of 5000 messages can be obtained per request;
        attempting to exceed this will result in an error.

        **Changes**: The `message_ids` option is new in Zulip 10.0 (feature level 300).

        Parameters
        ----------
        anchor : typing.Optional[Anchor]
            Integer message ID to anchor fetching of new messages. Supports special
            string values for when the client wants the server to compute the anchor
            to use:

            - `newest`: The most recent message.
            - `oldest`: The oldest message.
            - `first_unread`: The oldest unread message matching the
              query, if any; otherwise, the most recent message.
            - `date`: The first message on or after the datetime indicated by the
              [`anchor_date`](#parameter-anchor_date), if any; otherwise, the most
              recent message.

            **Changes**: The `date` value is new in Zulip 12.0 (feature level 445).

            String values are new in Zulip 3.0 (feature level 1). The
            `first_unread` functionality was supported in Zulip 2.1.x
            and older by not sending `anchor` and using `use_first_unread_anchor`.

            In Zulip 2.1.x and older, `oldest` can be emulated with
            `"anchor": 0`, and `newest` with `"anchor": 10000000000000000`
            (that specific large value works around a bug in Zulip
            2.1.x and older in the `found_newest` return value).

        include_anchor : typing.Optional[bool]
            Whether a message with the specified ID matching the narrow
            should be included.

            **Changes**: New in Zulip 6.0 (feature level 155).

        anchor_date : typing.Optional[str]
            The date or datetime to use for finding the anchor message when `anchor` is
            `date`. Accepted formats include ISO 8601 date-only strings
            (e.g. `2005-04-18`) as well as full datetime strings
            (e.g. `2005-04-18T12:34:56Z`). If only a date is provided, the datetime is set to
            midnight (00:00) on that day in UTC. If no timezone is provided, UTC is
            assumed.

            **Changes**: New in Zulip 12.0 (feature level 445).

        num_before : typing.Optional[int]
            The number of messages with IDs less than the anchor to retrieve.
            Required if `message_ids` is not provided.

        num_after : typing.Optional[int]
            The number of messages with IDs greater than the anchor to retrieve.
            Required if `message_ids` is not provided.

        narrow : typing.Optional[str]
            The narrow where you want to fetch the messages from. See how to
            [construct a narrow](/api/construct-narrow).

            Note that many narrows, including all that lack a `channel`, `channels`,
            `stream`, or `streams` operator, search the user's personal message
            history. See [searching shared
            history](/help/search-for-messages#search-shared-history)
            for details.

            For example, if you would like to fetch messages from all public channels instead
            of only the user's message history, then a specific narrow for
            messages sent to all public channels can be used:
            `{"operator": "channels", "operand": "public"}`.

            Newly created bot users are not usually subscribed to any
            channels, so bots using this API should either be
            subscribed to appropriate channels or use a shared history
            search narrow with this endpoint.

            **Changes**: See [changes section](/api/construct-narrow#changes)
            of search/narrow filter documentation.

        client_gravatar : typing.Optional[bool]
            Whether the client supports computing gravatars URLs. If
            enabled, `avatar_url` will be included in the response only
            if there is a Zulip avatar, and will be `null` for users who
            are using gravatar as their avatar. This option
            significantly reduces the compressed size of user data,
            since gravatar URLs are long, random strings and thus do not
            compress well. The `client_gravatar` field is set to `true` if
            clients can compute their own gravatars.

            **Changes**: The default value of this parameter was `false`
            prior to Zulip 5.0 (feature level 92).

        apply_markdown : typing.Optional[bool]
            If `true`, message content is returned in the rendered HTML
            format. If `false`, message content is returned in the raw
            Markdown-format text that user entered.

            See [Markdown message formatting](/api/message-formatting) for details on Zulip's HTML format.

        use_first_unread_anchor : typing.Optional[bool]
            Legacy way to specify `"anchor": "first_unread"` in Zulip 2.1.x and older.

            Whether to use the (computed by the server) first unread message
            matching the narrow as the `anchor`. Mutually exclusive with `anchor`.

            **Changes**: Deprecated in Zulip 3.0 (feature level 1) and replaced by
            `"anchor": "first_unread"`.

        message_ids : typing.Optional[str]
            A list of message IDs to fetch. The server will return messages corresponding to the
            subset of the requested message IDs that exist and the current user has access to,
            potentially filtered by the narrow (if that parameter is provided).

            It is an error to pass this parameter as well as any of the parameters involved in
            specifying a range of messages: `anchor`, `include_anchor`, `use_first_unread_anchor`,
            `num_before`, and `num_after`.

            **Changes**: New in Zulip 10.0 (feature level 300). Previously, there was
            no way to request a specific set of messages IDs.

        allow_empty_topic_name : typing.Optional[bool]
            Whether the client supports processing the empty string as a topic in the
            topic name fields in the returned data, including in returned edit_history data.

            If `false`, the server will use the value of `realm_empty_topic_display_name`
            found in the [`POST /register`](/api/register-queue) response instead of empty string
            to represent the empty string topic in its response.

            **Changes**: New in Zulip 10.0 (feature level 334). Previously, the empty string
            was not a valid topic.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMessagesResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "messages",
            method="GET",
            params={
                "anchor": anchor,
                "include_anchor": include_anchor,
                "anchor_date": anchor_date,
                "num_before": num_before,
                "num_after": num_after,
                "narrow": narrow,
                "client_gravatar": client_gravatar,
                "apply_markdown": apply_markdown,
                "use_first_unread_anchor": use_first_unread_anchor,
                "message_ids": message_ids,
                "allow_empty_topic_name": allow_empty_topic_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMessagesResponse,
                    parse_obj_as(
                        type_=GetMessagesResponse,
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

    async def send_message(
        self,
        *,
        type: SendMessageRequestType,
        to: SendMessageRequestTo,
        content: RequiredContent,
        topic: typing.Optional[str] = OMIT,
        queue_id: typing.Optional[str] = OMIT,
        local_id: typing.Optional[str] = OMIT,
        read_by_sender: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SendMessageResponse]:
        """
        Send a [channel message](/help/introduction-to-topics) or a
        [direct message](/help/direct-messages).

        Parameters
        ----------
        type : SendMessageRequestType
            The type of message to be sent.

            `"direct"` for a direct message and `"stream"` or `"channel"` for a
            channel message.

            **Changes**: In Zulip 9.0 (feature level 248), `"channel"` was added as
            an additional value for this parameter to request a channel message.

            In Zulip 7.0 (feature level 174), `"direct"` was added as
            the preferred way to request a direct message, deprecating the original
            `"private"`. While `"private"` is still supported for requesting direct
            messages, clients are encouraged to use to the modern convention with
            servers that support it, because support for `"private"` will eventually
            be removed.

        to : SendMessageRequestTo
            The channel or users receiving the message.

            For channel messages, this is either the name or integer ID of the
            channel.

            For direct messages, this is either a list containing integer user IDs or
            a list containing string Zulip API email addresses. The ID or email
            address of the user sending the message can be included in the list, but
            will be ignored by the server, unless the user sending the message is the
            only recipient of the message.

            **Changes**: In Zulip 2.0.0, support for using user/channel IDs was added.

        content : RequiredContent

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

            New in Zulip 2.0.0. Previous Zulip releases encoded
            this as `subject`, which is currently a deprecated alias.

        queue_id : typing.Optional[str]
            For clients supporting
            [local echo](https://zulip.readthedocs.io/en/latest/subsystems/sending-messages.html#local-echo),
            the [event queue](/api/register-queue) ID for the client.

            If passed, `local_id` is required.

            If the message is successfully sent, the server will include
            `local_message_id` in the [`message` event](/api/get-events#message) that
            the client with this `queue_id` will receive.

        local_id : typing.Optional[str]
            For clients supporting
            [local echo](https://zulip.readthedocs.io/en/latest/subsystems/sending-messages.html#local-echo),
            a unique string-format identifier chosen freely by the client.

            If passed, `queue_id` is required.

            If the message is successfully sent, the server will pass it back to
            the client without inspecting it as `local_message_id` in the
            [`message` event](/api/get-events#message) that the client with the
            above `queue_id` will receive.

        read_by_sender : typing.Optional[bool]
            Whether the message should be initially marked read by its
            sender. If unspecified, the server uses a heuristic based
            on the client name.

            **Changes**: New in Zulip 8.0 (feature level 236).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SendMessageResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "messages",
            method="POST",
            data={
                "type": type,
                "to": convert_and_respect_annotation_metadata(
                    object_=to, annotation=SendMessageRequestTo, direction="write"
                ),
                "content": content,
                "topic": topic,
                "queue_id": queue_id,
                "local_id": local_id,
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
                    SendMessageResponse,
                    parse_obj_as(
                        type_=SendMessageResponse,
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

    async def get_message_history(
        self,
        message_id: int,
        *,
        allow_empty_topic_name: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetMessageHistoryResponse]:
        """
        Fetch the message edit history of a previously edited message.

        Note that edit history may be disabled in some organizations; see the
        [Zulip help center documentation on editing messages][edit-settings].

        [edit-settings]: /help/view-a-messages-edit-history

        Parameters
        ----------
        message_id : int
            The target message's ID.

        allow_empty_topic_name : typing.Optional[bool]
            Whether the topic names i.e. `topic` and `prev_topic` fields in
            the `message_history` objects returned can be empty string.

            If `false`, the value of `realm_empty_topic_display_name`
            found in the [`POST /register`](/api/register-queue) response is
            returned replacing the empty string as the topic name.

            **Changes**: New in Zulip 10.0 (feature level 334).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMessageHistoryResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}/history",
            method="GET",
            params={
                "allow_empty_topic_name": allow_empty_topic_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMessageHistoryResponse,
                    parse_obj_as(
                        type_=GetMessageHistoryResponse,
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

    async def update_message_flags(
        self,
        *,
        messages: typing.Sequence[int],
        op: UpdateMessageFlagsRequestOp,
        flag: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateMessageFlagsResponse]:
        """
        Add or remove personal message flags like `read` and `starred`
        on a collection of message IDs.

        See also the endpoint for [updating flags on a range of
        messages within a narrow](/api/update-message-flags-for-narrow).

        Parameters
        ----------
        messages : typing.Sequence[int]
            An array containing the IDs of the target messages.

        op : UpdateMessageFlagsRequestOp
            Whether to `add` the flag or `remove` it.

        flag : str
            The flag that should be added/removed.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateMessageFlagsResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "messages/flags",
            method="POST",
            data={
                "messages": messages,
                "op": op,
                "flag": flag,
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
                    UpdateMessageFlagsResponse,
                    parse_obj_as(
                        type_=UpdateMessageFlagsResponse,
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

    async def update_message_flags_for_narrow(
        self,
        *,
        anchor: str,
        num_before: int,
        num_after: int,
        narrow: typing.Sequence[UpdateMessageFlagsForNarrowRequestNarrowItem],
        op: UpdateMessageFlagsForNarrowRequestOp,
        flag: str,
        include_anchor: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateMessageFlagsForNarrowResponse]:
        """
        Add or remove personal message flags like `read` and `starred`
        on a range of messages within a narrow.

        See also [the endpoint for updating flags on specific message
        IDs](/api/update-message-flags).

        **Changes**: New in Zulip 6.0 (feature level 155).

        Parameters
        ----------
        anchor : str
            Integer message ID to anchor updating of flags. Supports special
            string values for when the client wants the server to compute the anchor
            to use:

            - `newest`: The most recent message.
            - `oldest`: The oldest message.
            - `first_unread`: The oldest unread message matching the
              query, if any; otherwise, the most recent message.

        num_before : int
            Limit the number of messages preceding the anchor in the
            update range. The server may decrease this to bound
            transaction sizes.

        num_after : int
            Limit the number of messages following the anchor in the
            update range. The server may decrease this to bound
            transaction sizes.

        narrow : typing.Sequence[UpdateMessageFlagsForNarrowRequestNarrowItem]
            The narrow you want update flags within. See how to
            [construct a narrow](/api/construct-narrow).

            Note that, when adding the `read` flag to messages, clients should
            consider including a narrow with the `is:unread` filter as an
            optimization. Including that filter takes advantage of the fact that
            the server has a database index for unread messages.

            **Changes**: See [changes section](/api/construct-narrow#changes)
            of search/narrow filter documentation.

        op : UpdateMessageFlagsForNarrowRequestOp
            Whether to `add` the flag or `remove` it.

        flag : str
            The flag that should be added/removed. See [available
            flags](/api/update-message-flags#available-flags).

        include_anchor : typing.Optional[bool]
            Whether a message with the specified ID matching the narrow
            should be included in the update range.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateMessageFlagsForNarrowResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "messages/flags/narrow",
            method="POST",
            data={
                "anchor": anchor,
                "include_anchor": include_anchor,
                "num_before": num_before,
                "num_after": num_after,
                "narrow": convert_and_respect_annotation_metadata(
                    object_=narrow,
                    annotation=typing.Sequence[UpdateMessageFlagsForNarrowRequestNarrowItem],
                    direction="write",
                ),
                "op": op,
                "flag": flag,
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
                    UpdateMessageFlagsForNarrowResponse,
                    parse_obj_as(
                        type_=UpdateMessageFlagsForNarrowResponse,
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

    async def render_message(
        self, *, content: RequiredContent, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RenderMessageResponse]:
        """
        Render a message to HTML.

        Parameters
        ----------
        content : RequiredContent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RenderMessageResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "messages/render",
            method="POST",
            data={
                "content": content,
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
                    RenderMessageResponse,
                    parse_obj_as(
                        type_=RenderMessageResponse,
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

    async def add_reaction(
        self,
        message_id: int,
        *,
        emoji_name: str,
        emoji_code: typing.Optional[EmojiCode] = OMIT,
        reaction_type: typing.Optional[ReactionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Add an [emoji reaction](/help/emoji-reactions) to a message.

        Parameters
        ----------
        message_id : int
            The target message's ID.

        emoji_name : str
            The target emoji's human-readable name.

            To find an emoji's name, hover over a message to reveal
            three icons on the right, then click the smiley face icon.
            Images of available reaction emojis appear. Hover over the
            emoji you want, and note that emoji's text name.

        emoji_code : typing.Optional[EmojiCode]

        reaction_type : typing.Optional[ReactionType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}/reactions",
            method="POST",
            data={
                "emoji_name": emoji_name,
                "emoji_code": emoji_code,
                "reaction_type": reaction_type,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    async def remove_reaction(
        self,
        message_id: int,
        *,
        emoji_name: typing.Optional[str] = OMIT,
        emoji_code: typing.Optional[EmojiCode] = OMIT,
        reaction_type: typing.Optional[ReactionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Remove an [emoji reaction](/help/emoji-reactions) from a message.

        Parameters
        ----------
        message_id : int
            The target message's ID.

        emoji_name : typing.Optional[str]
            The target emoji's human-readable name.

            To find an emoji's name, hover over a message to reveal
            three icons on the right, then click the smiley face icon.
            Images of available reaction emojis appear. Hover over the
            emoji you want, and note that emoji's text name.

        emoji_code : typing.Optional[EmojiCode]

        reaction_type : typing.Optional[ReactionType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}/reactions",
            method="DELETE",
            data={
                "emoji_name": emoji_name,
                "emoji_code": emoji_code,
                "reaction_type": reaction_type,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    async def get_read_receipts(
        self, message_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetReadReceiptsResponse]:
        """
        Returns a list containing the IDs for all users who have
        marked the message as read (and whose privacy settings allow
        sharing that information).

        The list of users IDs will include any bots who have marked
        the message as read via the API (providing a way for bots to
        indicate whether they have processed a message successfully in
        a way that can be easily inspected in a Zulip client). Bots
        for which this behavior is not desired may disable the
        `send_read_receipts` setting via the API.

        It will never contain the message's sender.

        **Changes**: New in Zulip 6.0 (feature level 137).

        Parameters
        ----------
        message_id : int
            The target message's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetReadReceiptsResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}/read_receipts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetReadReceiptsResponse,
                    parse_obj_as(
                        type_=GetReadReceiptsResponse,
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

    async def check_messages_match_narrow(
        self, *, msg_ids: str, narrow: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CheckMessagesMatchNarrowResponse]:
        """
        Check whether a set of messages match a [narrow](/api/construct-narrow).

        For many common narrows (e.g. a topic), clients can write an efficient
        client-side check to determine whether a newly arrived message belongs
        in the view.

        This endpoint is designed to allow clients to handle more complex narrows
        for which the client does not (or in the case of full-text search, cannot)
        implement this check.

        The format of the `match_subject` and `match_content` objects is designed
        to match those returned by the [`GET /messages`](/api/get-messages#response)
        endpoint, so that a client can splice these fields into a `message` object
        received from [`GET /events`](/api/get-events#message) and end up with an
        extended message object identical to how a [`GET /messages`](/api/get-messages)
        request for the current narrow would have returned the message.

        Parameters
        ----------
        msg_ids : str
            List of IDs for the messages to check.

        narrow : str
            A structure defining the narrow to check against. See how to
            [construct a narrow](/api/construct-narrow).

            **Changes**: See [changes section](/api/construct-narrow#changes)
            of search/narrow filter documentation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckMessagesMatchNarrowResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "messages/matches_narrow",
            method="GET",
            params={
                "msg_ids": msg_ids,
                "narrow": narrow,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckMessagesMatchNarrowResponse,
                    parse_obj_as(
                        type_=CheckMessagesMatchNarrowResponse,
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

    async def get_message(
        self,
        message_id: int,
        *,
        apply_markdown: typing.Optional[bool] = None,
        allow_empty_topic_name: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetMessageResponse]:
        """
        Given a message ID, return the message object.

        Additionally, a `raw_content` field is included. This field is
        useful for clients that primarily work with HTML-rendered
        messages but might need to occasionally fetch the message's
        raw [Zulip-flavored Markdown](/help/format-your-message-using-markdown) (e.g. for [view
        source](/help/view-the-markdown-source-of-a-message) or
        prefilling a message edit textarea).

        **Changes**: Before Zulip 5.0 (feature level 120), this
        endpoint only returned the `raw_content` field.

        Parameters
        ----------
        message_id : int
            The target message's ID.

        apply_markdown : typing.Optional[bool]
            If `true`, message content is returned in the rendered HTML
            format. If `false`, message content is returned in the raw
            [Zulip-flavored Markdown format](/help/format-your-message-using-markdown) text that user entered.

            **Changes**: New in Zulip 5.0 (feature level 120).

        allow_empty_topic_name : typing.Optional[bool]
            Whether the client supports processing the empty string as a topic in the
            topic name fields in the returned data, including in returned edit_history data.

            If `false`, the server will use the value of `realm_empty_topic_display_name`
            found in the [`POST /register`](/api/register-queue) response instead of empty string
            to represent the empty string topic in its response.

            **Changes**: New in Zulip 10.0 (feature level 334). Previously, the empty string
            was not a valid topic.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetMessageResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}",
            method="GET",
            params={
                "apply_markdown": apply_markdown,
                "allow_empty_topic_name": allow_empty_topic_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetMessageResponse,
                    parse_obj_as(
                        type_=GetMessageResponse,
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

    async def delete_message(
        self, message_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Permanently delete a message.

        This API corresponds to the [delete a message completely][delete-completely]
        feature documented in the Zulip help center.

        A user must be able to access the content of a message in order to delete it.
        See [channel permissions](/help/channel-permissions) for more information
        about content access for channel messages. For direct messages, the user
        must have received or sent the direct message to have content access.

        See [restricting message deletion](/help/restrict-message-editing-and-deletion)
        for documentation on when users are allowed to delete messages.

        The relevant realm settings in the API that are related to the above linked
        documentation on when users are allowed to delete messages are:

        - `realm_can_delete_any_message_group`
        - `realm_can_delete_own_message_group`
        - `realm_can_set_delete_message_policy_group`
        - `realm_message_content_delete_limit_seconds`

        The relevant per-channel permission settings in the API that are related to the
        above linked documentation on when users are allowed to delete messages in a
        specific channel are:

        - `can_delete_any_message_group`
        - `can_delete_own_message_group`

        More details about these realm and channel settings can be found in the
        [`POST /register`](/api/register-queue) response.

        **Changes**: Prior to Zulip 10.0 (feature level 281), only organization
        administrators had permission to permanently delete a message.

        [delete-completely]: /help/delete-a-message#delete-a-message-completely

        Parameters
        ----------
        message_id : int
            The target message's ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}",
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

    async def update_message(
        self,
        message_id: int,
        *,
        topic: typing.Optional[str] = OMIT,
        propagate_mode: typing.Optional[UpdateMessageRequestPropagateMode] = OMIT,
        send_notification_to_old_thread: typing.Optional[bool] = OMIT,
        send_notification_to_new_thread: typing.Optional[bool] = OMIT,
        content: typing.Optional[OptionalContent] = OMIT,
        prev_content_sha256: typing.Optional[str] = OMIT,
        stream_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateMessageResponse]:
        """
        Update the content, topic, or channel of the message with the specified
        ID.

        You can [resolve topics](/help/resolve-a-topic) by editing the topic to
        `✔ {original_topic}` with the `propagate_mode` parameter set to
        `"change_all"`.

        See [configuring message editing][config-message-editing] for detailed
        documentation on when users are allowed to edit message content, and
        [restricting moving messages][restrict-move-messages] for detailed
        documentation on when users are allowed to change a message's topic
        and/or channel.

        The relevant realm settings in the API that are related to the above
        linked documentation on when users are allowed to update messages are:

        - `allow_message_editing`
        - `can_resolve_topics_group`
        - `can_move_messages_between_channels_group`
        - `can_move_messages_between_topics_group`
        - `message_content_edit_limit_seconds`
        - `move_messages_within_stream_limit_seconds`
        - `move_messages_between_streams_limit_seconds`

        More details about these realm settings can be found in the
        [`POST /register`](/api/register-queue) response or in the documentation
        of the [`realm op: update_dict`](/api/get-events#realm-update_dict)
        event in [`GET /events`](/api/get-events).

        **Changes**: Prior to Zulip 10.0 (feature level 367), the permission for
        resolving a topic was managed by `can_move_messages_between_topics_group`.
        As of this feature level, users belonging to the `can_resolve_topics_group`
        will have the permission to [resolve topics](/help/resolve-a-topic) in the organization.

        In Zulip 10.0 (feature level 316), `edit_topic_policy`
        was removed and replaced by `can_move_messages_between_topics_group`
        realm setting.

        **Changes**: In Zulip 10.0 (feature level 310), `move_messages_between_streams_policy`
        was removed and replaced by `can_move_messages_between_channels_group`
        realm setting.

        Prior to Zulip 7.0 (feature level 172), anyone could add a
        topic to channel messages without a topic, regardless of the organization's
        [topic editing permissions](/help/restrict-moving-messages). As of this
        feature level, messages without topics have the same restrictions for
        topic edits as messages with topics.

        Before Zulip 7.0 (feature level 172), by using the `change_all` value for
        the `propagate_mode` parameter, users could move messages after the
        organization's configured time limits for changing a message's topic or
        channel had passed. As of this feature level, the server will [return an
        error](/api/update-message#response) with `"code":
        "MOVE_MESSAGES_TIME_LIMIT_EXCEEDED"` if users, other than organization
        administrators or moderators, try to move messages after these time
        limits have passed.

        Before Zulip 7.0 (feature level 162), users who were not administrators or
        moderators could only edit topics if the target message was sent within the
        last 3 days. As of this feature level, that time limit is now controlled by
        the realm setting `move_messages_within_stream_limit_seconds`. Also at this
        feature level, a similar time limit for moving messages between channels was
        added, controlled by the realm setting
        `move_messages_between_streams_limit_seconds`. Previously, all users who
        had permission to move messages between channels did not have any time limit
        restrictions when doing so.

        Before Zulip 7.0 (feature level 159), editing channels and topics of messages
        was forbidden if the realm setting for `allow_message_editing` was `false`,
        regardless of an organization's configuration for the realm settings
        `edit_topic_policy` or `move_messages_between_streams_policy`.

        Before Zulip 7.0 (feature level 159), message senders were allowed to edit
        the topic of their messages indefinitely.

        In Zulip 5.0 (feature level 75), the `edit_topic_policy` realm setting
        was added, replacing the `allow_community_topic_editing` boolean.

        In Zulip 4.0 (feature level 56), the `move_messages_between_streams_policy`
        realm setting was added.

        [config-message-editing]: /help/restrict-message-editing-and-deletion
        [restrict-move-messages]: /help/restrict-moving-messages

        Parameters
        ----------
        message_id : int
            The target message's ID.

        topic : typing.Optional[str]
            The topic to move the message(s) to, to request changing the topic.

            Clients should use the `max_topic_length` returned by the
            [`POST /register`](/api/register-queue) endpoint to determine
            the maximum topic length

            Should only be sent when changing the topic, and will throw an error
            if the target message is not a channel message.

            Note: When the value of `realm_empty_topic_display_name` found in
            the [POST /register](/api/register-queue) response is used for this
            parameter, it is interpreted as an empty string.

            When [topics are required](/help/require-topics), this parameter can't
            be `"(no topic)"`, an empty string, or the value of `realm_empty_topic_display_name`.

            You can [resolve topics](/help/resolve-a-topic) by editing the topic to
            `✔ {original_topic}` with the `propagate_mode` parameter set to
            `"change_all"`. The empty string topic cannot be marked as resolved.

            **Changes**: Before Zulip 10.0 (feature level 334), empty string
            was not a valid topic name for channel messages.

            New in Zulip 2.0.0. Previous Zulip releases encoded this as `subject`,
            which is currently a deprecated alias.

        propagate_mode : typing.Optional[UpdateMessageRequestPropagateMode]
            Which message(s) should be edited:

            - `"change_later"`: The target message and all following messages.
            - `"change_one"`: Only the target message.
            - `"change_all"`: All messages in this topic.

            Only the default value of `"change_one"` is valid when editing
            only the content of a message.

            This parameter determines both which messages get moved and also whether
            clients that are currently narrowed to the topic containing the message
            should navigate or adjust their compose box recipient to point to the
            post-edit channel/topic.

        send_notification_to_old_thread : typing.Optional[bool]
            Whether to send an automated message to the old topic to
            notify users where the messages were moved to.

            **Changes**: Before Zulip 6.0 (feature level 152), this parameter
            had a default of `true` and was ignored unless the channel was changed.

            New in Zulip 3.0 (feature level 9).

        send_notification_to_new_thread : typing.Optional[bool]
            Whether to send an automated message to the new topic to
            notify users where the messages came from.

            If the move is just [resolving/unresolving a topic](/help/resolve-a-topic),
            this parameter will not trigger an additional notification.

            **Changes**: Before Zulip 6.0 (feature level 152), this parameter
            was ignored unless the channel was changed.

            New in Zulip 3.0 (feature level 9).

        content : typing.Optional[OptionalContent]

        prev_content_sha256 : typing.Optional[str]
            An optional SHA-256 hash of the previous raw content of the message
            that the client has at the time of the request.

            If provided, the server will return an error if it does not match the
            SHA-256 hash of the message's content stored in the database.

            Clients can use this feature to prevent races where multiple clients
            save conflicting edits to a message.

            **Changes**: New in Zulip 11.0 (feature level 379).

        stream_id : typing.Optional[int]
            The channel ID to move the message(s) to, to request moving
            messages to another channel.

            Should only be sent when changing the channel. Will throw an error
            if the target message is not a channel message.

            Note that a message's content and channel cannot be changed at the
            same time, so sending both `content` and `stream_id` parameters will
            throw an error.

            **Changes**: Prior to Zulip 13.0 (feature level 509), passing the channel
            ID that the target message is currently in was processed as a successful
            channel move, even if the target message was not moved (i.e., neither its
            channel nor topic were changed).

            New in Zulip 3.0 (feature level 1).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateMessageResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}",
            method="PATCH",
            data={
                "topic": topic,
                "propagate_mode": propagate_mode,
                "send_notification_to_old_thread": send_notification_to_old_thread,
                "send_notification_to_new_thread": send_notification_to_new_thread,
                "content": content,
                "prev_content_sha256": prev_content_sha256,
                "stream_id": stream_id,
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
                    UpdateMessageResponse,
                    parse_obj_as(
                        type_=UpdateMessageResponse,
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

    async def report_message(
        self,
        message_id: int,
        *,
        report_type: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Sends a notification to the organization's [moderation request
        channel](/help/enable-moderation-requests), if it is configured, that
        reports the targeted message for [review and moderation](/help/report-a-message).

        Clients should check the `moderation_request_channel` realm setting to
        decide whether to show the option to report messages in the UI.

        If the `report_type` parameter value is `"other"`, the `description`
        parameter is required. Clients should also enforce and communicate this
        behavior in the UI.

        **Changes**: Before Zulip 13.0 (feature level 511), this endpoint
        did not return an error if the message report failed to be sent to the
        moderation request channel.

        New in Zulip 11.0 (feature level 382). This API builds on the
        `moderation_request_channel` realm setting, which was added in
        feature level 331.

        Parameters
        ----------
        message_id : int
            The target message's ID.

        report_type : str
            The reason that best describes why the current user is reporting the
            target message for moderation.

            Must be one of the `key` values in the `server_report_message_types`
            field in the [`POST /register`](/api/register-queue) response.

            **Changes**: Prior to Zulip 12.0 (feature level 435), the allowed
            values for this parameter were limited to: `"harassment"`,
            `"inappropriate"`, `"norms"`, `"other"`, `"spam"`.

        description : typing.Optional[str]
            A short description with additional context about why the current user
            is reporting the target message for moderation.

            Clients should limit this string to 1000 Unicode code points.

            If the `report_type` parameter is `"other"`, this parameter is required,
            and its value cannot be an empty string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(message_id)}/report",
            method="POST",
            data={
                "report_type": report_type,
                "description": description,
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
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
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

    async def upload_file(
        self, *, filename: typing.Optional[core.File] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UploadFileResponse]:
        """
        [Upload](/help/share-and-upload-files) a single file and get the corresponding URL.

        Initially, only you will be able to access the link. To share the
        uploaded file, you'll need to [send a message][send-message]
        containing the resulting link. Users who can already access the link
        can reshare it with other users by sending additional Zulip messages
        containing the link.

        The maximum allowed file size is available in the `max_file_upload_size_mib`
        field in the [`POST /register`](/api/register-queue) response. Note that
        large files (25MB+) may fail to upload using this API endpoint due to
        network-layer timeouts, depending on the quality of your connection to the
        Zulip server.

        For uploading larger files, `/api/v1/tus` is an endpoint implementing the
        [`tus` resumable upload protocol](https://tus.io/protocols/resumable-upload),
        which supports uploading arbitrarily large files limited only by the server's
        `max_file_upload_size_mib` (Configured via `MAX_FILE_UPLOAD_SIZE` in
        `/etc/zulip/settings.py`). Clients which send authenticated credentials
        (either via browser-based cookies, or API key via `Authorization` header) may
        use this endpoint to upload files.

        **Changes**: The `api/v1/tus` endpoint supporting resumable uploads was
        introduced in Zulip 10.0 (feature level 296). Previously,
        `max_file_upload_size_mib` was typically 25MB.

        [uploaded-files]: /help/manage-your-uploaded-files
        [send-message]: /api/send-message

        Parameters
        ----------
        filename : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadFileResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "user_uploads",
            method="POST",
            data={},
            files={
                **({"filename": filename} if filename is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadFileResponse,
                    parse_obj_as(
                        type_=UploadFileResponse,
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

    async def check_thumbnail_status(
        self, realm_id_str: int, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CheckThumbnailStatusResponse]:
        """
        Check whether a thumbnail exists for a specific file uploaded by a user.
        This endpoint is intended to be polled by clients to determine when
        thumbnail generation is complete.

        **Changes**: New in Zulip 12.0 (feature level 479).

        Parameters
        ----------
        realm_id_str : int
            The realm ID component of the file's `path_id`. If the `path_id` is
            `1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`, the `realm_id_str` would be `1`.

        filename : str
            The file path component of the file's `path_id` (everything
            after the first `/`). If the `path_id` is
            `1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`, the `filename`
            would be `4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckThumbnailStatusResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"thumbnail/status/{encode_path_param(realm_id_str)}/{encode_path_param(filename)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckThumbnailStatusResponse,
                    parse_obj_as(
                        type_=CheckThumbnailStatusResponse,
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

    async def get_file_temporary_url(
        self, realm_id_str: int, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetFileTemporaryUrlResponse]:
        """
        Get a temporary URL for access to an [uploaded file](/api/upload-file)
        that doesn't require authentication.

        The `SIGNED_ACCESS_TOKEN_VALIDITY_IN_SECONDS` server setting controls
        the valid length of time for temporary access, which generally is set
        to a default of 60 seconds. Consumers of this API are expected to
        immediately request the URL that it returns, and should not store it
        in any way.

        **Changes**: New in Zulip 3.0 (feature level 1).

        Parameters
        ----------
        realm_id_str : int
            The realm ID component of the file's `path_id`. If the `path_id` is
            `1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`, the `realm_id_str` would be `1`.

        filename : str
            The file path component of the file's `path_id` (everything
            after the first `/`). If the `path_id` is
            `1/4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`, the `filename`
            would be `4e/m2A3MSqFnWRLUf9SaPzQ0Up_/zulip.txt`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetFileTemporaryUrlResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user_uploads/{encode_path_param(realm_id_str)}/{encode_path_param(filename)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFileTemporaryUrlResponse,
                    parse_obj_as(
                        type_=GetFileTemporaryUrlResponse,
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
