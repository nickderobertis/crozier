

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.content_too_large_error import ContentTooLargeError
from ..errors.not_found_error import NotFoundError
from ..types.edge_message_dto import EdgeMessageDto
from ..types.entity_transaction_response import EntityTransactionResponse
from ..types.problem_detail import ProblemDetail
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEdgeMessageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def delete_messages(
        self,
        *,
        request: str,
        transaction_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Deletes multiple stored edge messages using their unique identifiers, including the associated payload blobs. Messages are deleted in batches according to the specified transaction size.

        Parameters
        ----------
        request : str

        transaction_size : typing.Optional[int]
            Number of messages to delete per transaction batch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Messages successfully deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            "message",
            method="DELETE",
            params={
                "transactionSize": transaction_size,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    def new_message(
        self,
        subject: str,
        *,
        request: str,
        transaction_timeout_millis: typing.Optional[int] = None,
        message_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        recipient: typing.Optional[str] = None,
        reply_to: typing.Optional[str] = None,
        correlation_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
        """
        Creates and stores a new edge message with the provided payload and AMQP-aligned headers. The message is processed according to the specified parsing configuration and stored with a unique identifier.

        Parameters
        ----------
        subject : str
            Message subject identifier

        request : str

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds to wait for transaction completion

        message_id : typing.Optional[str]
            Custom message identifier

        user_id : typing.Optional[str]
            ID of the message sender

        recipient : typing.Optional[str]
            Intended message recipient

        reply_to : typing.Optional[str]
            Reply-to address for responses

        correlation_id : typing.Optional[str]
            Correlation ID for message tracking

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            Message successfully created and stored
        """
        _response = self._client_wrapper.httpx_client.request(
            f"message/new/{encode_path_param(subject)}",
            method="POST",
            params={
                "transactionTimeoutMillis": transaction_timeout_millis,
            },
            json=request,
            headers={
                "content-type": "application/json",
                "Content-Encoding": "UTF-8",
                "X-Message-ID": str(message_id) if message_id is not None else None,
                "X-User-ID": str(user_id) if user_id is not None else None,
                "X-Recipient": str(recipient) if recipient is not None else None,
                "X-Reply-To": str(reply_to) if reply_to is not None else None,
                "X-Correlation-ID": str(correlation_id) if correlation_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetail,
                        parse_obj_as(
                            type_=ProblemDetail,
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
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EdgeMessageDto]:
        """
        Fetches a stored edge message using its unique identifier, including all message metadata and payload

        Parameters
        ----------
        message_id : str
            Unique identifier of the message to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EdgeMessageDto]
            Message successfully retrieved
        """
        _response = self._client_wrapper.httpx_client.request(
            f"message/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EdgeMessageDto,
                    parse_obj_as(
                        type_=EdgeMessageDto,
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

    def delete_message(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EntityTransactionResponse]:
        """
        Deletes a stored edge message using its unique identifier, including the associated payload blob

        Parameters
        ----------
        message_id : str
            Unique identifier of the message to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntityTransactionResponse]
            Message successfully deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"message/{encode_path_param(message_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityTransactionResponse,
                    parse_obj_as(
                        type_=EntityTransactionResponse,
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


class AsyncRawEdgeMessageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def delete_messages(
        self,
        *,
        request: str,
        transaction_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Deletes multiple stored edge messages using their unique identifiers, including the associated payload blobs. Messages are deleted in batches according to the specified transaction size.

        Parameters
        ----------
        request : str

        transaction_size : typing.Optional[int]
            Number of messages to delete per transaction batch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Messages successfully deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            "message",
            method="DELETE",
            params={
                "transactionSize": transaction_size,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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

    async def new_message(
        self,
        subject: str,
        *,
        request: str,
        transaction_timeout_millis: typing.Optional[int] = None,
        message_id: typing.Optional[str] = None,
        user_id: typing.Optional[str] = None,
        recipient: typing.Optional[str] = None,
        reply_to: typing.Optional[str] = None,
        correlation_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
        """
        Creates and stores a new edge message with the provided payload and AMQP-aligned headers. The message is processed according to the specified parsing configuration and stored with a unique identifier.

        Parameters
        ----------
        subject : str
            Message subject identifier

        request : str

        transaction_timeout_millis : typing.Optional[int]
            Maximum time in milliseconds to wait for transaction completion

        message_id : typing.Optional[str]
            Custom message identifier

        user_id : typing.Optional[str]
            ID of the message sender

        recipient : typing.Optional[str]
            Intended message recipient

        reply_to : typing.Optional[str]
            Reply-to address for responses

        correlation_id : typing.Optional[str]
            Correlation ID for message tracking

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            Message successfully created and stored
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"message/new/{encode_path_param(subject)}",
            method="POST",
            params={
                "transactionTimeoutMillis": transaction_timeout_millis,
            },
            json=request,
            headers={
                "content-type": "application/json",
                "Content-Encoding": "UTF-8",
                "X-Message-ID": str(message_id) if message_id is not None else None,
                "X-User-ID": str(user_id) if user_id is not None else None,
                "X-Recipient": str(recipient) if recipient is not None else None,
                "X-Reply-To": str(reply_to) if reply_to is not None else None,
                "X-Correlation-ID": str(correlation_id) if correlation_id is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
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
            if _response.status_code == 413:
                raise ContentTooLargeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ProblemDetail,
                        parse_obj_as(
                            type_=ProblemDetail,
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
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EdgeMessageDto]:
        """
        Fetches a stored edge message using its unique identifier, including all message metadata and payload

        Parameters
        ----------
        message_id : str
            Unique identifier of the message to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EdgeMessageDto]
            Message successfully retrieved
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"message/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EdgeMessageDto,
                    parse_obj_as(
                        type_=EdgeMessageDto,
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

    async def delete_message(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EntityTransactionResponse]:
        """
        Deletes a stored edge message using its unique identifier, including the associated payload blob

        Parameters
        ----------
        message_id : str
            Unique identifier of the message to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntityTransactionResponse]
            Message successfully deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"message/{encode_path_param(message_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityTransactionResponse,
                    parse_obj_as(
                        type_=EntityTransactionResponse,
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
