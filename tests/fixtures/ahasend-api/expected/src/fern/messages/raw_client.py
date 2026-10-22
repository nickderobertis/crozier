

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
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.address import Address
from ..types.attachment import Attachment
from ..types.create_message_response import CreateMessageResponse
from ..types.error_response import ErrorResponse
from ..types.message import Message
from ..types.message_schedule import MessageSchedule
from ..types.paginated_messages_response import PaginatedMessagesResponse
from ..types.recipient import Recipient
from ..types.retention import Retention
from ..types.success_response import SuccessResponse
from ..types.tracking import Tracking
from .types.create_conversation_message_request_sandbox_result import CreateConversationMessageRequestSandboxResult
from .types.create_message_request_sandbox_result import CreateMessageRequestSandboxResult
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_messages(
        self,
        account_id: str,
        *,
        status: typing.Optional[str] = None,
        sender: typing.Optional[str] = None,
        recipient: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message_id_header: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedMessagesResponse]:
        """
        Returns a list of message summaries for the account. Can be filtered by various parameters.

        `messages:read:all` can read across the account. Domain-scoped keys see
        only messages for domains authorized by their matching read roles.

        Parameters
        ----------
        account_id : str
            Account ID

        status : typing.Optional[str]
            Filter by comma-separated list of message statuses. Allowed values are:
            `Received`, `Delivered`, `Deferred`, `Bounced`, `Failed`, `Suppressed`,
            `Sandbox Delivered`, `Sandbox Deferred`, `Sandbox Failed`, `Sandbox Bounced`,
            and `Sandbox Suppressed`.

        sender : typing.Optional[str]
            Sender email address (must be from domain in API key scopes)

        recipient : typing.Optional[str]
            Recipient email address

        subject : typing.Optional[str]
            Filter by subject text

        message_id_header : typing.Optional[str]
            Filter by message ID header (same ID returned by CreateMessage API)

        tags : typing.Optional[str]
            Filter by comma-separated list of tags (max 20)

        from_time : typing.Optional[dt.datetime]
            Filter messages created after this time (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter messages created before this time (RFC3339 format)

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedMessagesResponse]
            List of messages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/messages",
            method="GET",
            params={
                "status": status,
                "sender": sender,
                "recipient": recipient,
                "subject": subject,
                "message_id_header": message_id_header,
                "tags": tags,
                "from_time": serialize_datetime(from_time) if from_time is not None else None,
                "to_time": serialize_datetime(to_time) if to_time is not None else None,
                "limit": limit,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedMessagesResponse,
                    parse_obj_as(
                        type_=PaginatedMessagesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def create_message(
        self,
        account_id: str,
        *,
        from_: Address,
        recipients: typing.Sequence[Recipient],
        subject: str,
        idempotency_key: typing.Optional[str] = None,
        reply_to: typing.Optional[Address] = OMIT,
        text_content: typing.Optional[str] = OMIT,
        html_content: typing.Optional[str] = OMIT,
        amp_content: typing.Optional[str] = OMIT,
        attachments: typing.Optional[typing.Sequence[Attachment]] = OMIT,
        headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        substitutions: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        sandbox: typing.Optional[bool] = OMIT,
        sandbox_result: typing.Optional[CreateMessageRequestSandboxResult] = OMIT,
        tracking: typing.Optional[Tracking] = OMIT,
        retention: typing.Optional[Retention] = OMIT,
        schedule: typing.Optional[MessageSchedule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateMessageResponse]:
        """
        Creates and sends a message to one or more recipients. This API cannot be used if you want to send a conversational/P2P message and set CC or BCC. Use [Create Conversation Message](https://ahasend.com/docs/api-reference/messages/create-conversation) instead.

        **Validation Requirements:**
        - Either `text_content` or `html_content` is required
        - `from.email` must be from a domain you own with valid DNS records
        - `retention.metadata` must be between 1 and 30 days
        - `retention.data` must be between 0 and 30 days
        - If `reply_to` is provided, do not include `reply-to` in headers
        - `message-id` header will be ignored and automatically generated
        - Schedule times must be in RFC3339 format
        - `schedule.first_attempt` must be in the future and within 7 days of the request
        - `schedule.expires` must be in the future and within 8 days of the request

        Authorization uses the domain in `from.email`: either
        `messages:send:all` or the matching domain-specific send role is
        sufficient.

        Parameters
        ----------
        account_id : str
            Account ID

        from_ : Address

        recipients : typing.Sequence[Recipient]
            This does not set the To header to multiple addresses, it sends a separate message for each recipient

        subject : str
            Email subject line

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        reply_to : typing.Optional[Address]
            If provided, the reply-to header in headers array must not be provided

        text_content : typing.Optional[str]
            Plain text content. Required if html_content is empty

        html_content : typing.Optional[str]
            HTML content. Required if text_content is empty

        amp_content : typing.Optional[str]
            AMP HTML content

        attachments : typing.Optional[typing.Sequence[Attachment]]
            File attachments. For inline images, set the attachment's `content_id` to a value wrapped in angle brackets (e.g. `<image1@example.com>`) and reference it from `html_content` with `cid:` (e.g. `<img src="cid:image1@example.com">`).

        headers : typing.Optional[typing.Dict[str, str]]
            Custom email headers. reply-to header cannot be provided if reply_to is provided, message-id will be ignored and automatically generated

        substitutions : typing.Optional[typing.Dict[str, typing.Any]]
            Global substitutions, recipient substitutions override global

        tags : typing.Optional[typing.Sequence[str]]
            Tags for categorizing messages

        sandbox : typing.Optional[bool]
            If true, the message will be sent to the sandbox environment

        sandbox_result : typing.Optional[CreateMessageRequestSandboxResult]
            The result of the sandbox send

        tracking : typing.Optional[Tracking]
            Tracking settings for the message, overrides default account settings

        retention : typing.Optional[Retention]
            Retention settings for the message, overrides default account settings

        schedule : typing.Optional[MessageSchedule]
            Schedule for message delivery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateMessageResponse]
            Message created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/messages",
            method="POST",
            json={
                "from": convert_and_respect_annotation_metadata(object_=from_, annotation=Address, direction="write"),
                "recipients": convert_and_respect_annotation_metadata(
                    object_=recipients, annotation=typing.Sequence[Recipient], direction="write"
                ),
                "reply_to": convert_and_respect_annotation_metadata(
                    object_=reply_to, annotation=Address, direction="write"
                ),
                "subject": subject,
                "text_content": text_content,
                "html_content": html_content,
                "amp_content": amp_content,
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments, annotation=typing.Sequence[Attachment], direction="write"
                ),
                "headers": headers,
                "substitutions": substitutions,
                "tags": tags,
                "sandbox": sandbox,
                "sandbox_result": sandbox_result,
                "tracking": convert_and_respect_annotation_metadata(
                    object_=tracking, annotation=typing.Optional[Tracking], direction="write"
                ),
                "retention": convert_and_respect_annotation_metadata(
                    object_=retention, annotation=typing.Optional[Retention], direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=MessageSchedule, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateMessageResponse,
                    parse_obj_as(
                        type_=CreateMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def create_conversation_message(
        self,
        account_id: str,
        *,
        from_: Address,
        to: typing.Sequence[Address],
        subject: str,
        idempotency_key: typing.Optional[str] = None,
        cc: typing.Optional[typing.Sequence[Address]] = OMIT,
        bcc: typing.Optional[typing.Sequence[Address]] = OMIT,
        reply_to: typing.Optional[Address] = OMIT,
        text_content: typing.Optional[str] = OMIT,
        html_content: typing.Optional[str] = OMIT,
        amp_content: typing.Optional[str] = OMIT,
        attachments: typing.Optional[typing.Sequence[Attachment]] = OMIT,
        headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        sandbox: typing.Optional[bool] = OMIT,
        sandbox_result: typing.Optional[CreateConversationMessageRequestSandboxResult] = OMIT,
        tracking: typing.Optional[Tracking] = OMIT,
        retention: typing.Optional[Retention] = OMIT,
        schedule: typing.Optional[MessageSchedule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateMessageResponse]:
        """
        Creates and sends a conversational message (with support for CC and BCC) to one or more recipients. This API does not support template substitutions, use [Create Message](https://ahasend.com/docs/api-reference/messages/create-message) instead if you need substitutions.

        **Validation Requirements:**
        - Either `text_content` or `html_content` is required
        - `from.email` must be from a domain you own with valid DNS records
        - `retention.metadata` must be between 1 and 30 days
        - `retention.data` must be between 0 and 30 days
        - If the `reply_to` parameter is provided, do not include `reply-to` in headers
        - If the `cc` parameter is provided, do not include `cc` in headers
        - `message-id` header will be ignored and automatically generated
        - Schedule times must be in RFC3339 format
        - `schedule.first_attempt` must be in the future and within 7 days of the request
        - `schedule.expires` must be in the future and within 8 days of the request

        Authorization uses the domain in `from.email`: either
        `messages:send:all` or the matching domain-specific send role is
        sufficient.

        Parameters
        ----------
        account_id : str
            Account ID

        from_ : Address

        to : typing.Sequence[Address]
            This parameter can set the `To` header to multiple addresses. The combined to, cc, and bcc recipient count must not exceed 50.

        subject : str
            Email subject line

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        cc : typing.Optional[typing.Sequence[Address]]
            This parameter can set the `CC` header to multiple addresses. Do not include `cc` in the headers array. The combined to, cc, and bcc recipient count must not exceed 50.

        bcc : typing.Optional[typing.Sequence[Address]]
            This parameter can set the `To` header to multiple addresses. The combined to, cc, and bcc recipient count must not exceed 50.

        reply_to : typing.Optional[Address]
            If provided, the reply-to header in headers array must not be provided

        text_content : typing.Optional[str]
            Plain text content. Required if html_content is empty

        html_content : typing.Optional[str]
            HTML content. Required if text_content is empty

        amp_content : typing.Optional[str]
            AMP HTML content

        attachments : typing.Optional[typing.Sequence[Attachment]]
            File attachments. For inline images, set the attachment's `content_id` to a value wrapped in angle brackets (e.g. `<image1@example.com>`) and reference it from `html_content` with `cid:` (e.g. `<img src="cid:image1@example.com">`).

        headers : typing.Optional[typing.Dict[str, str]]
            Custom email headers. `cc` and `reply-to` headers cannot be provided if `reply_to` or `cc` parameters are provided, message-id will be ignored and automatically generated

        tags : typing.Optional[typing.Sequence[str]]
            Tags for categorizing messages

        sandbox : typing.Optional[bool]
            If true, the message will be sent to the sandbox environment

        sandbox_result : typing.Optional[CreateConversationMessageRequestSandboxResult]
            The result of the sandbox send

        tracking : typing.Optional[Tracking]
            Tracking settings for the message, overrides default account settings

        retention : typing.Optional[Retention]
            Retention settings for the message, overrides default account settings

        schedule : typing.Optional[MessageSchedule]
            Schedule for message delivery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateMessageResponse]
            Message created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/messages/conversation",
            method="POST",
            json={
                "from": convert_and_respect_annotation_metadata(object_=from_, annotation=Address, direction="write"),
                "to": convert_and_respect_annotation_metadata(
                    object_=to, annotation=typing.Sequence[Address], direction="write"
                ),
                "cc": convert_and_respect_annotation_metadata(
                    object_=cc, annotation=typing.Sequence[Address], direction="write"
                ),
                "bcc": convert_and_respect_annotation_metadata(
                    object_=bcc, annotation=typing.Sequence[Address], direction="write"
                ),
                "reply_to": convert_and_respect_annotation_metadata(
                    object_=reply_to, annotation=Address, direction="write"
                ),
                "subject": subject,
                "text_content": text_content,
                "html_content": html_content,
                "amp_content": amp_content,
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments, annotation=typing.Sequence[Attachment], direction="write"
                ),
                "headers": headers,
                "tags": tags,
                "sandbox": sandbox,
                "sandbox_result": sandbox_result,
                "tracking": convert_and_respect_annotation_metadata(
                    object_=tracking, annotation=typing.Optional[Tracking], direction="write"
                ),
                "retention": convert_and_respect_annotation_metadata(
                    object_=retention, annotation=typing.Optional[Retention], direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=MessageSchedule, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateMessageResponse,
                    parse_obj_as(
                        type_=CreateMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_message(
        self, account_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Message]:
        """
        Returns the complete message by its ID, including raw content and parsed content structure.
        Access requires `messages:read:all` or a read role matching the
        message's sender domain.

        Parameters
        ----------
        account_id : str
            Account ID

        message_id : str
            Message API ID. Accepts the generated Message-ID returned by [Create Message API](https://ahasend.com/docs/api-reference/messages/create-message), for example `<uuid@example.com>`, or the bare UUID portion.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Message]
            Message details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Message,
                    parse_obj_as(
                        type_=Message,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def cancel_message(
        self, account_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SuccessResponse]:
        """
        Cancels a scheduled message. Access requires `messages:cancel:all` or a
        cancel role matching the message's sender domain.

        Parameters
        ----------
        account_id : str
            Account ID

        message_id : str
            Message API ID. Accepts the generated Message-ID returned by [Create Message API](https://ahasend.com/docs/api-reference/messages/create-message), for example `<uuid@example.com>`, or the bare UUID portion.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Scheduled message is cancelled
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/messages/{encode_path_param(message_id)}/cancel",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_messages(
        self,
        account_id: str,
        *,
        status: typing.Optional[str] = None,
        sender: typing.Optional[str] = None,
        recipient: typing.Optional[str] = None,
        subject: typing.Optional[str] = None,
        message_id_header: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedMessagesResponse]:
        """
        Returns a list of message summaries for the account. Can be filtered by various parameters.

        `messages:read:all` can read across the account. Domain-scoped keys see
        only messages for domains authorized by their matching read roles.

        Parameters
        ----------
        account_id : str
            Account ID

        status : typing.Optional[str]
            Filter by comma-separated list of message statuses. Allowed values are:
            `Received`, `Delivered`, `Deferred`, `Bounced`, `Failed`, `Suppressed`,
            `Sandbox Delivered`, `Sandbox Deferred`, `Sandbox Failed`, `Sandbox Bounced`,
            and `Sandbox Suppressed`.

        sender : typing.Optional[str]
            Sender email address (must be from domain in API key scopes)

        recipient : typing.Optional[str]
            Recipient email address

        subject : typing.Optional[str]
            Filter by subject text

        message_id_header : typing.Optional[str]
            Filter by message ID header (same ID returned by CreateMessage API)

        tags : typing.Optional[str]
            Filter by comma-separated list of tags (max 20)

        from_time : typing.Optional[dt.datetime]
            Filter messages created after this time (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter messages created before this time (RFC3339 format)

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedMessagesResponse]
            List of messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/messages",
            method="GET",
            params={
                "status": status,
                "sender": sender,
                "recipient": recipient,
                "subject": subject,
                "message_id_header": message_id_header,
                "tags": tags,
                "from_time": serialize_datetime(from_time) if from_time is not None else None,
                "to_time": serialize_datetime(to_time) if to_time is not None else None,
                "limit": limit,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedMessagesResponse,
                    parse_obj_as(
                        type_=PaginatedMessagesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def create_message(
        self,
        account_id: str,
        *,
        from_: Address,
        recipients: typing.Sequence[Recipient],
        subject: str,
        idempotency_key: typing.Optional[str] = None,
        reply_to: typing.Optional[Address] = OMIT,
        text_content: typing.Optional[str] = OMIT,
        html_content: typing.Optional[str] = OMIT,
        amp_content: typing.Optional[str] = OMIT,
        attachments: typing.Optional[typing.Sequence[Attachment]] = OMIT,
        headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        substitutions: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        sandbox: typing.Optional[bool] = OMIT,
        sandbox_result: typing.Optional[CreateMessageRequestSandboxResult] = OMIT,
        tracking: typing.Optional[Tracking] = OMIT,
        retention: typing.Optional[Retention] = OMIT,
        schedule: typing.Optional[MessageSchedule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateMessageResponse]:
        """
        Creates and sends a message to one or more recipients. This API cannot be used if you want to send a conversational/P2P message and set CC or BCC. Use [Create Conversation Message](https://ahasend.com/docs/api-reference/messages/create-conversation) instead.

        **Validation Requirements:**
        - Either `text_content` or `html_content` is required
        - `from.email` must be from a domain you own with valid DNS records
        - `retention.metadata` must be between 1 and 30 days
        - `retention.data` must be between 0 and 30 days
        - If `reply_to` is provided, do not include `reply-to` in headers
        - `message-id` header will be ignored and automatically generated
        - Schedule times must be in RFC3339 format
        - `schedule.first_attempt` must be in the future and within 7 days of the request
        - `schedule.expires` must be in the future and within 8 days of the request

        Authorization uses the domain in `from.email`: either
        `messages:send:all` or the matching domain-specific send role is
        sufficient.

        Parameters
        ----------
        account_id : str
            Account ID

        from_ : Address

        recipients : typing.Sequence[Recipient]
            This does not set the To header to multiple addresses, it sends a separate message for each recipient

        subject : str
            Email subject line

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        reply_to : typing.Optional[Address]
            If provided, the reply-to header in headers array must not be provided

        text_content : typing.Optional[str]
            Plain text content. Required if html_content is empty

        html_content : typing.Optional[str]
            HTML content. Required if text_content is empty

        amp_content : typing.Optional[str]
            AMP HTML content

        attachments : typing.Optional[typing.Sequence[Attachment]]
            File attachments. For inline images, set the attachment's `content_id` to a value wrapped in angle brackets (e.g. `<image1@example.com>`) and reference it from `html_content` with `cid:` (e.g. `<img src="cid:image1@example.com">`).

        headers : typing.Optional[typing.Dict[str, str]]
            Custom email headers. reply-to header cannot be provided if reply_to is provided, message-id will be ignored and automatically generated

        substitutions : typing.Optional[typing.Dict[str, typing.Any]]
            Global substitutions, recipient substitutions override global

        tags : typing.Optional[typing.Sequence[str]]
            Tags for categorizing messages

        sandbox : typing.Optional[bool]
            If true, the message will be sent to the sandbox environment

        sandbox_result : typing.Optional[CreateMessageRequestSandboxResult]
            The result of the sandbox send

        tracking : typing.Optional[Tracking]
            Tracking settings for the message, overrides default account settings

        retention : typing.Optional[Retention]
            Retention settings for the message, overrides default account settings

        schedule : typing.Optional[MessageSchedule]
            Schedule for message delivery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateMessageResponse]
            Message created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/messages",
            method="POST",
            json={
                "from": convert_and_respect_annotation_metadata(object_=from_, annotation=Address, direction="write"),
                "recipients": convert_and_respect_annotation_metadata(
                    object_=recipients, annotation=typing.Sequence[Recipient], direction="write"
                ),
                "reply_to": convert_and_respect_annotation_metadata(
                    object_=reply_to, annotation=Address, direction="write"
                ),
                "subject": subject,
                "text_content": text_content,
                "html_content": html_content,
                "amp_content": amp_content,
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments, annotation=typing.Sequence[Attachment], direction="write"
                ),
                "headers": headers,
                "substitutions": substitutions,
                "tags": tags,
                "sandbox": sandbox,
                "sandbox_result": sandbox_result,
                "tracking": convert_and_respect_annotation_metadata(
                    object_=tracking, annotation=typing.Optional[Tracking], direction="write"
                ),
                "retention": convert_and_respect_annotation_metadata(
                    object_=retention, annotation=typing.Optional[Retention], direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=MessageSchedule, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateMessageResponse,
                    parse_obj_as(
                        type_=CreateMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def create_conversation_message(
        self,
        account_id: str,
        *,
        from_: Address,
        to: typing.Sequence[Address],
        subject: str,
        idempotency_key: typing.Optional[str] = None,
        cc: typing.Optional[typing.Sequence[Address]] = OMIT,
        bcc: typing.Optional[typing.Sequence[Address]] = OMIT,
        reply_to: typing.Optional[Address] = OMIT,
        text_content: typing.Optional[str] = OMIT,
        html_content: typing.Optional[str] = OMIT,
        amp_content: typing.Optional[str] = OMIT,
        attachments: typing.Optional[typing.Sequence[Attachment]] = OMIT,
        headers: typing.Optional[typing.Dict[str, str]] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        sandbox: typing.Optional[bool] = OMIT,
        sandbox_result: typing.Optional[CreateConversationMessageRequestSandboxResult] = OMIT,
        tracking: typing.Optional[Tracking] = OMIT,
        retention: typing.Optional[Retention] = OMIT,
        schedule: typing.Optional[MessageSchedule] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateMessageResponse]:
        """
        Creates and sends a conversational message (with support for CC and BCC) to one or more recipients. This API does not support template substitutions, use [Create Message](https://ahasend.com/docs/api-reference/messages/create-message) instead if you need substitutions.

        **Validation Requirements:**
        - Either `text_content` or `html_content` is required
        - `from.email` must be from a domain you own with valid DNS records
        - `retention.metadata` must be between 1 and 30 days
        - `retention.data` must be between 0 and 30 days
        - If the `reply_to` parameter is provided, do not include `reply-to` in headers
        - If the `cc` parameter is provided, do not include `cc` in headers
        - `message-id` header will be ignored and automatically generated
        - Schedule times must be in RFC3339 format
        - `schedule.first_attempt` must be in the future and within 7 days of the request
        - `schedule.expires` must be in the future and within 8 days of the request

        Authorization uses the domain in `from.email`: either
        `messages:send:all` or the matching domain-specific send role is
        sufficient.

        Parameters
        ----------
        account_id : str
            Account ID

        from_ : Address

        to : typing.Sequence[Address]
            This parameter can set the `To` header to multiple addresses. The combined to, cc, and bcc recipient count must not exceed 50.

        subject : str
            Email subject line

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        cc : typing.Optional[typing.Sequence[Address]]
            This parameter can set the `CC` header to multiple addresses. Do not include `cc` in the headers array. The combined to, cc, and bcc recipient count must not exceed 50.

        bcc : typing.Optional[typing.Sequence[Address]]
            This parameter can set the `To` header to multiple addresses. The combined to, cc, and bcc recipient count must not exceed 50.

        reply_to : typing.Optional[Address]
            If provided, the reply-to header in headers array must not be provided

        text_content : typing.Optional[str]
            Plain text content. Required if html_content is empty

        html_content : typing.Optional[str]
            HTML content. Required if text_content is empty

        amp_content : typing.Optional[str]
            AMP HTML content

        attachments : typing.Optional[typing.Sequence[Attachment]]
            File attachments. For inline images, set the attachment's `content_id` to a value wrapped in angle brackets (e.g. `<image1@example.com>`) and reference it from `html_content` with `cid:` (e.g. `<img src="cid:image1@example.com">`).

        headers : typing.Optional[typing.Dict[str, str]]
            Custom email headers. `cc` and `reply-to` headers cannot be provided if `reply_to` or `cc` parameters are provided, message-id will be ignored and automatically generated

        tags : typing.Optional[typing.Sequence[str]]
            Tags for categorizing messages

        sandbox : typing.Optional[bool]
            If true, the message will be sent to the sandbox environment

        sandbox_result : typing.Optional[CreateConversationMessageRequestSandboxResult]
            The result of the sandbox send

        tracking : typing.Optional[Tracking]
            Tracking settings for the message, overrides default account settings

        retention : typing.Optional[Retention]
            Retention settings for the message, overrides default account settings

        schedule : typing.Optional[MessageSchedule]
            Schedule for message delivery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateMessageResponse]
            Message created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/messages/conversation",
            method="POST",
            json={
                "from": convert_and_respect_annotation_metadata(object_=from_, annotation=Address, direction="write"),
                "to": convert_and_respect_annotation_metadata(
                    object_=to, annotation=typing.Sequence[Address], direction="write"
                ),
                "cc": convert_and_respect_annotation_metadata(
                    object_=cc, annotation=typing.Sequence[Address], direction="write"
                ),
                "bcc": convert_and_respect_annotation_metadata(
                    object_=bcc, annotation=typing.Sequence[Address], direction="write"
                ),
                "reply_to": convert_and_respect_annotation_metadata(
                    object_=reply_to, annotation=Address, direction="write"
                ),
                "subject": subject,
                "text_content": text_content,
                "html_content": html_content,
                "amp_content": amp_content,
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments, annotation=typing.Sequence[Attachment], direction="write"
                ),
                "headers": headers,
                "tags": tags,
                "sandbox": sandbox,
                "sandbox_result": sandbox_result,
                "tracking": convert_and_respect_annotation_metadata(
                    object_=tracking, annotation=typing.Optional[Tracking], direction="write"
                ),
                "retention": convert_and_respect_annotation_metadata(
                    object_=retention, annotation=typing.Optional[Retention], direction="write"
                ),
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=MessageSchedule, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateMessageResponse,
                    parse_obj_as(
                        type_=CreateMessageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_message(
        self, account_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Message]:
        """
        Returns the complete message by its ID, including raw content and parsed content structure.
        Access requires `messages:read:all` or a read role matching the
        message's sender domain.

        Parameters
        ----------
        account_id : str
            Account ID

        message_id : str
            Message API ID. Accepts the generated Message-ID returned by [Create Message API](https://ahasend.com/docs/api-reference/messages/create-message), for example `<uuid@example.com>`, or the bare UUID portion.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Message]
            Message details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Message,
                    parse_obj_as(
                        type_=Message,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def cancel_message(
        self, account_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Cancels a scheduled message. Access requires `messages:cancel:all` or a
        cancel role matching the message's sender domain.

        Parameters
        ----------
        account_id : str
            Account ID

        message_id : str
            Message API ID. Accepts the generated Message-ID returned by [Create Message API](https://ahasend.com/docs/api-reference/messages/create-message), for example `<uuid@example.com>`, or the bare UUID portion.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Scheduled message is cancelled
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/messages/{encode_path_param(message_id)}/cancel",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
