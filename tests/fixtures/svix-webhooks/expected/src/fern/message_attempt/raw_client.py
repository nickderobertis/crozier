

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.empty_response import EmptyResponse
from ..types.http_error_out import HttpErrorOut
from ..types.http_validation_error import HttpValidationError
from ..types.list_response_endpoint_message_out import ListResponseEndpointMessageOut
from ..types.list_response_message_attempt_out import ListResponseMessageAttemptOut
from ..types.list_response_message_endpoint_out import ListResponseMessageEndpointOut
from ..types.message_attempt_out import MessageAttemptOut
from ..types.message_status import MessageStatus
from ..types.status_code_class import StatusCodeClass
from pydantic import ValidationError


class RawMessageAttemptClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def v1message_attempt_list_by_endpoint(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        status: typing.Optional[MessageStatus] = None,
        status_code_class: typing.Optional[StatusCodeClass] = None,
        channel: typing.Optional[str] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListResponseMessageAttemptOut]:
        """
        List attempts by endpoint id

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        status : typing.Optional[MessageStatus]
            Filter response based on the delivery status

        status_code_class : typing.Optional[StatusCodeClass]
            Filter response based on the HTTP status code

        channel : typing.Optional[str]
            Filter response based on the channel

        before : typing.Optional[dt.datetime]
            Only include items created before a certain date

        after : typing.Optional[dt.datetime]
            Only include items created after a certain date

        with_content : typing.Optional[bool]
            When `true` attempt content is included in the response

        event_types : typing.Optional[typing.Sequence[str]]
            Filter response based on the event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListResponseMessageAttemptOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/attempt/endpoint/{encode_path_param(endpoint_id)}",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
                "status": status,
                "status_code_class": status_code_class,
                "channel": channel,
                "before": serialize_datetime(before) if before is not None else None,
                "after": serialize_datetime(after) if after is not None else None,
                "with_content": with_content,
                "event_types": event_types,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseMessageAttemptOut,
                    parse_obj_as(
                        type_=ListResponseMessageAttemptOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1message_attempt_list_by_msg(
        self,
        app_id: str,
        msg_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        status: typing.Optional[MessageStatus] = None,
        status_code_class: typing.Optional[StatusCodeClass] = None,
        channel: typing.Optional[str] = None,
        endpoint_id: typing.Optional[str] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListResponseMessageAttemptOut]:
        """
        List attempts by message id

        Parameters
        ----------
        app_id : str

        msg_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        status : typing.Optional[MessageStatus]
            Filter response based on the delivery status

        status_code_class : typing.Optional[StatusCodeClass]
            Filter response based on the HTTP status code

        channel : typing.Optional[str]
            Filter response based on the channel

        endpoint_id : typing.Optional[str]
            Filter the attempts based on the attempted endpoint

        before : typing.Optional[dt.datetime]
            Only include items created before a certain date

        after : typing.Optional[dt.datetime]
            Only include items created after a certain date

        with_content : typing.Optional[bool]
            When `true` attempt content is included in the response

        event_types : typing.Optional[typing.Sequence[str]]
            Filter response based on the event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListResponseMessageAttemptOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/attempt/msg/{encode_path_param(msg_id)}",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
                "status": status,
                "status_code_class": status_code_class,
                "channel": channel,
                "endpoint_id": endpoint_id,
                "before": serialize_datetime(before) if before is not None else None,
                "after": serialize_datetime(after) if after is not None else None,
                "with_content": with_content,
                "event_types": event_types,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseMessageAttemptOut,
                    parse_obj_as(
                        type_=ListResponseMessageAttemptOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1message_attempt_list_attempted_messages(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        status: typing.Optional[MessageStatus] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListResponseEndpointMessageOut]:
        """
        List messages for a particular endpoint. Additionally includes metadata about the latest message attempt.

        The `before` parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        channel : typing.Optional[str]
            Filter response based on the channel

        status : typing.Optional[MessageStatus]
            Filter response based on the delivery status

        before : typing.Optional[dt.datetime]
            Only include items created before a certain date

        after : typing.Optional[dt.datetime]
            Only include items created after a certain date

        with_content : typing.Optional[bool]
            When `true` message payloads are included in the response

        event_types : typing.Optional[typing.Sequence[str]]
            Filter response based on the event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListResponseEndpointMessageOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/msg",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
                "channel": channel,
                "status": status,
                "before": serialize_datetime(before) if before is not None else None,
                "after": serialize_datetime(after) if after is not None else None,
                "with_content": with_content,
                "event_types": event_types,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseEndpointMessageOut,
                    parse_obj_as(
                        type_=ListResponseEndpointMessageOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1message_attempt_get(
        self, app_id: str, msg_id: str, attempt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessageAttemptOut]:
        """
        `msg_id`: Use a message id or a message `eventId`

        Parameters
        ----------
        app_id : str

        msg_id : str

        attempt_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessageAttemptOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/msg/{encode_path_param(msg_id)}/attempt/{encode_path_param(attempt_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageAttemptOut,
                    parse_obj_as(
                        type_=MessageAttemptOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1message_attempt_expunge_content(
        self, app_id: str, msg_id: str, attempt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes the given attempt's response body. Useful when an endpoint accidentally returned sensitive content.

        Parameters
        ----------
        app_id : str

        msg_id : str

        attempt_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/msg/{encode_path_param(msg_id)}/attempt/{encode_path_param(attempt_id)}/content",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1message_attempt_list_attempted_destinations(
        self,
        app_id: str,
        msg_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListResponseMessageEndpointOut]:
        """
        `msg_id`: Use a message id or a message `eventId`

        Parameters
        ----------
        app_id : str

        msg_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListResponseMessageEndpointOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/msg/{encode_path_param(msg_id)}/endpoint",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseMessageEndpointOut,
                    parse_obj_as(
                        type_=ListResponseMessageEndpointOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1message_attempt_resend(
        self,
        app_id: str,
        msg_id: str,
        endpoint_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmptyResponse]:
        """
        Resend a message to the specified endpoint.

        Parameters
        ----------
        app_id : str

        msg_id : str

        endpoint_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/msg/{encode_path_param(msg_id)}/endpoint/{encode_path_param(endpoint_id)}/resend",
            method="POST",
            headers={
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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


class AsyncRawMessageAttemptClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def v1message_attempt_list_by_endpoint(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        status: typing.Optional[MessageStatus] = None,
        status_code_class: typing.Optional[StatusCodeClass] = None,
        channel: typing.Optional[str] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListResponseMessageAttemptOut]:
        """
        List attempts by endpoint id

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        status : typing.Optional[MessageStatus]
            Filter response based on the delivery status

        status_code_class : typing.Optional[StatusCodeClass]
            Filter response based on the HTTP status code

        channel : typing.Optional[str]
            Filter response based on the channel

        before : typing.Optional[dt.datetime]
            Only include items created before a certain date

        after : typing.Optional[dt.datetime]
            Only include items created after a certain date

        with_content : typing.Optional[bool]
            When `true` attempt content is included in the response

        event_types : typing.Optional[typing.Sequence[str]]
            Filter response based on the event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListResponseMessageAttemptOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/attempt/endpoint/{encode_path_param(endpoint_id)}",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
                "status": status,
                "status_code_class": status_code_class,
                "channel": channel,
                "before": serialize_datetime(before) if before is not None else None,
                "after": serialize_datetime(after) if after is not None else None,
                "with_content": with_content,
                "event_types": event_types,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseMessageAttemptOut,
                    parse_obj_as(
                        type_=ListResponseMessageAttemptOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1message_attempt_list_by_msg(
        self,
        app_id: str,
        msg_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        status: typing.Optional[MessageStatus] = None,
        status_code_class: typing.Optional[StatusCodeClass] = None,
        channel: typing.Optional[str] = None,
        endpoint_id: typing.Optional[str] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListResponseMessageAttemptOut]:
        """
        List attempts by message id

        Parameters
        ----------
        app_id : str

        msg_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        status : typing.Optional[MessageStatus]
            Filter response based on the delivery status

        status_code_class : typing.Optional[StatusCodeClass]
            Filter response based on the HTTP status code

        channel : typing.Optional[str]
            Filter response based on the channel

        endpoint_id : typing.Optional[str]
            Filter the attempts based on the attempted endpoint

        before : typing.Optional[dt.datetime]
            Only include items created before a certain date

        after : typing.Optional[dt.datetime]
            Only include items created after a certain date

        with_content : typing.Optional[bool]
            When `true` attempt content is included in the response

        event_types : typing.Optional[typing.Sequence[str]]
            Filter response based on the event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListResponseMessageAttemptOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/attempt/msg/{encode_path_param(msg_id)}",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
                "status": status,
                "status_code_class": status_code_class,
                "channel": channel,
                "endpoint_id": endpoint_id,
                "before": serialize_datetime(before) if before is not None else None,
                "after": serialize_datetime(after) if after is not None else None,
                "with_content": with_content,
                "event_types": event_types,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseMessageAttemptOut,
                    parse_obj_as(
                        type_=ListResponseMessageAttemptOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1message_attempt_list_attempted_messages(
        self,
        app_id: str,
        endpoint_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        channel: typing.Optional[str] = None,
        status: typing.Optional[MessageStatus] = None,
        before: typing.Optional[dt.datetime] = None,
        after: typing.Optional[dt.datetime] = None,
        with_content: typing.Optional[bool] = None,
        event_types: typing.Optional[typing.Sequence[str]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListResponseEndpointMessageOut]:
        """
        List messages for a particular endpoint. Additionally includes metadata about the latest message attempt.

        The `before` parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.

        Parameters
        ----------
        app_id : str

        endpoint_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        channel : typing.Optional[str]
            Filter response based on the channel

        status : typing.Optional[MessageStatus]
            Filter response based on the delivery status

        before : typing.Optional[dt.datetime]
            Only include items created before a certain date

        after : typing.Optional[dt.datetime]
            Only include items created after a certain date

        with_content : typing.Optional[bool]
            When `true` message payloads are included in the response

        event_types : typing.Optional[typing.Sequence[str]]
            Filter response based on the event type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListResponseEndpointMessageOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/endpoint/{encode_path_param(endpoint_id)}/msg",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
                "channel": channel,
                "status": status,
                "before": serialize_datetime(before) if before is not None else None,
                "after": serialize_datetime(after) if after is not None else None,
                "with_content": with_content,
                "event_types": event_types,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseEndpointMessageOut,
                    parse_obj_as(
                        type_=ListResponseEndpointMessageOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1message_attempt_get(
        self, app_id: str, msg_id: str, attempt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessageAttemptOut]:
        """
        `msg_id`: Use a message id or a message `eventId`

        Parameters
        ----------
        app_id : str

        msg_id : str

        attempt_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessageAttemptOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/msg/{encode_path_param(msg_id)}/attempt/{encode_path_param(attempt_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageAttemptOut,
                    parse_obj_as(
                        type_=MessageAttemptOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1message_attempt_expunge_content(
        self, app_id: str, msg_id: str, attempt_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes the given attempt's response body. Useful when an endpoint accidentally returned sensitive content.

        Parameters
        ----------
        app_id : str

        msg_id : str

        attempt_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/msg/{encode_path_param(msg_id)}/attempt/{encode_path_param(attempt_id)}/content",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1message_attempt_list_attempted_destinations(
        self,
        app_id: str,
        msg_id: str,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListResponseMessageEndpointOut]:
        """
        `msg_id`: Use a message id or a message `eventId`

        Parameters
        ----------
        app_id : str

        msg_id : str

        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListResponseMessageEndpointOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/msg/{encode_path_param(msg_id)}/endpoint",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseMessageEndpointOut,
                    parse_obj_as(
                        type_=ListResponseMessageEndpointOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1message_attempt_resend(
        self,
        app_id: str,
        msg_id: str,
        endpoint_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Resend a message to the specified endpoint.

        Parameters
        ----------
        app_id : str

        msg_id : str

        endpoint_id : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}/msg/{encode_path_param(msg_id)}/endpoint/{encode_path_param(endpoint_id)}/resend",
            method="POST",
            headers={
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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
