

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.chat_message import ChatMessage
from ..types.chat_message_attachment import ChatMessageAttachment
from ..types.error import Error
from .types.get_all_messages_for_user_request_model import GetAllMessagesForUserRequestModel
from .types.get_all_messages_for_user_response import GetAllMessagesForUserResponse
from .types.get_chat_message_request_expand import GetChatMessageRequestExpand
from .types.list_chat_messages_response import ListChatMessagesResponse
from .types.send_chat_message_request_body import SendChatMessageRequestBody
from .types.send_chat_message_request_hosted_contents_item import SendChatMessageRequestHostedContentsItem
from .types.send_chat_message_request_importance import SendChatMessageRequestImportance
from .types.send_chat_message_request_mentions_item import SendChatMessageRequestMentionsItem
from .types.update_chat_message_request_body import UpdateChatMessageRequestBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawChatMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_chat_messages(
        self,
        chat_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        orderby: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListChatMessagesResponse]:
        """
        Retrieve the list of messages in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        orderby : typing.Optional[str]
            OData orderby query

        filter : typing.Optional[str]
            OData filter query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListChatMessagesResponse]
            Successfully retrieved chat messages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chats/{encode_path_param(chat_id)}/messages",
            method="GET",
            params={
                "$top": top,
                "$skip": skip,
                "$orderby": orderby,
                "$filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListChatMessagesResponse,
                    parse_obj_as(
                        type_=ListChatMessagesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def send_chat_message(
        self,
        chat_id: str,
        *,
        body: SendChatMessageRequestBody,
        importance: typing.Optional[SendChatMessageRequestImportance] = OMIT,
        mentions: typing.Optional[typing.Sequence[SendChatMessageRequestMentionsItem]] = OMIT,
        attachments: typing.Optional[typing.Sequence[ChatMessageAttachment]] = OMIT,
        hosted_contents: typing.Optional[typing.Sequence[SendChatMessageRequestHostedContentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChatMessage]:
        """
        Send a new message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        body : SendChatMessageRequestBody

        importance : typing.Optional[SendChatMessageRequestImportance]

        mentions : typing.Optional[typing.Sequence[SendChatMessageRequestMentionsItem]]

        attachments : typing.Optional[typing.Sequence[ChatMessageAttachment]]

        hosted_contents : typing.Optional[typing.Sequence[SendChatMessageRequestHostedContentsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChatMessage]
            Message sent successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chats/{encode_path_param(chat_id)}/messages",
            method="POST",
            json={
                "body": convert_and_respect_annotation_metadata(
                    object_=body, annotation=SendChatMessageRequestBody, direction="write"
                ),
                "importance": importance,
                "mentions": convert_and_respect_annotation_metadata(
                    object_=mentions, annotation=typing.Sequence[SendChatMessageRequestMentionsItem], direction="write"
                ),
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments, annotation=typing.Sequence[ChatMessageAttachment], direction="write"
                ),
                "hostedContents": convert_and_respect_annotation_metadata(
                    object_=hosted_contents,
                    annotation=typing.Sequence[SendChatMessageRequestHostedContentsItem],
                    direction="write",
                ),
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
                    ChatMessage,
                    parse_obj_as(
                        type_=ChatMessage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_chat_message(
        self,
        chat_id: str,
        chat_message_id: str,
        *,
        expand: typing.Optional[GetChatMessageRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChatMessage]:
        """
        Retrieve a specific message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        chat_message_id : str
            The unique identifier of the chat message

        expand : typing.Optional[GetChatMessageRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChatMessage]
            Successfully retrieved chat message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chats/{encode_path_param(chat_id)}/messages/{encode_path_param(chat_message_id)}",
            method="GET",
            params={
                "$expand": expand,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChatMessage,
                    parse_obj_as(
                        type_=ChatMessage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def delete_chat_message(
        self, chat_id: str, chat_message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Soft delete a message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        chat_message_id : str
            The unique identifier of the chat message

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chats/{encode_path_param(chat_id)}/messages/{encode_path_param(chat_message_id)}",
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
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def update_chat_message(
        self,
        chat_id: str,
        chat_message_id: str,
        *,
        body: typing.Optional[UpdateChatMessageRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Update a message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        chat_message_id : str
            The unique identifier of the chat message

        body : typing.Optional[UpdateChatMessageRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"chats/{encode_path_param(chat_id)}/messages/{encode_path_param(chat_message_id)}",
            method="PATCH",
            json={
                "body": convert_and_respect_annotation_metadata(
                    object_=body, annotation=UpdateChatMessageRequestBody, direction="write"
                ),
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_all_messages_for_user(
        self,
        *,
        model: typing.Optional[GetAllMessagesForUserRequestModel] = None,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetAllMessagesForUserResponse]:
        """
        Get all messages from all chats that a user is a participant in

        Parameters
        ----------
        model : typing.Optional[GetAllMessagesForUserRequestModel]
            Payment model for metered API

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAllMessagesForUserResponse]
            Successfully retrieved all messages
        """
        _response = self._client_wrapper.httpx_client.request(
            "chats/getAllMessages",
            method="GET",
            params={
                "model": model,
                "$top": top,
                "$skip": skip,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAllMessagesForUserResponse,
                    parse_obj_as(
                        type_=GetAllMessagesForUserResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawChatMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_chat_messages(
        self,
        chat_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        orderby: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListChatMessagesResponse]:
        """
        Retrieve the list of messages in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        orderby : typing.Optional[str]
            OData orderby query

        filter : typing.Optional[str]
            OData filter query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListChatMessagesResponse]
            Successfully retrieved chat messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chats/{encode_path_param(chat_id)}/messages",
            method="GET",
            params={
                "$top": top,
                "$skip": skip,
                "$orderby": orderby,
                "$filter": filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListChatMessagesResponse,
                    parse_obj_as(
                        type_=ListChatMessagesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def send_chat_message(
        self,
        chat_id: str,
        *,
        body: SendChatMessageRequestBody,
        importance: typing.Optional[SendChatMessageRequestImportance] = OMIT,
        mentions: typing.Optional[typing.Sequence[SendChatMessageRequestMentionsItem]] = OMIT,
        attachments: typing.Optional[typing.Sequence[ChatMessageAttachment]] = OMIT,
        hosted_contents: typing.Optional[typing.Sequence[SendChatMessageRequestHostedContentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChatMessage]:
        """
        Send a new message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        body : SendChatMessageRequestBody

        importance : typing.Optional[SendChatMessageRequestImportance]

        mentions : typing.Optional[typing.Sequence[SendChatMessageRequestMentionsItem]]

        attachments : typing.Optional[typing.Sequence[ChatMessageAttachment]]

        hosted_contents : typing.Optional[typing.Sequence[SendChatMessageRequestHostedContentsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChatMessage]
            Message sent successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chats/{encode_path_param(chat_id)}/messages",
            method="POST",
            json={
                "body": convert_and_respect_annotation_metadata(
                    object_=body, annotation=SendChatMessageRequestBody, direction="write"
                ),
                "importance": importance,
                "mentions": convert_and_respect_annotation_metadata(
                    object_=mentions, annotation=typing.Sequence[SendChatMessageRequestMentionsItem], direction="write"
                ),
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments, annotation=typing.Sequence[ChatMessageAttachment], direction="write"
                ),
                "hostedContents": convert_and_respect_annotation_metadata(
                    object_=hosted_contents,
                    annotation=typing.Sequence[SendChatMessageRequestHostedContentsItem],
                    direction="write",
                ),
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
                    ChatMessage,
                    parse_obj_as(
                        type_=ChatMessage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_chat_message(
        self,
        chat_id: str,
        chat_message_id: str,
        *,
        expand: typing.Optional[GetChatMessageRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChatMessage]:
        """
        Retrieve a specific message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        chat_message_id : str
            The unique identifier of the chat message

        expand : typing.Optional[GetChatMessageRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChatMessage]
            Successfully retrieved chat message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chats/{encode_path_param(chat_id)}/messages/{encode_path_param(chat_message_id)}",
            method="GET",
            params={
                "$expand": expand,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChatMessage,
                    parse_obj_as(
                        type_=ChatMessage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def delete_chat_message(
        self, chat_id: str, chat_message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Soft delete a message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        chat_message_id : str
            The unique identifier of the chat message

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chats/{encode_path_param(chat_id)}/messages/{encode_path_param(chat_message_id)}",
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
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def update_chat_message(
        self,
        chat_id: str,
        chat_message_id: str,
        *,
        body: typing.Optional[UpdateChatMessageRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Update a message in a chat

        Parameters
        ----------
        chat_id : str
            The unique identifier of the chat

        chat_message_id : str
            The unique identifier of the chat message

        body : typing.Optional[UpdateChatMessageRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"chats/{encode_path_param(chat_id)}/messages/{encode_path_param(chat_message_id)}",
            method="PATCH",
            json={
                "body": convert_and_respect_annotation_metadata(
                    object_=body, annotation=UpdateChatMessageRequestBody, direction="write"
                ),
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_all_messages_for_user(
        self,
        *,
        model: typing.Optional[GetAllMessagesForUserRequestModel] = None,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetAllMessagesForUserResponse]:
        """
        Get all messages from all chats that a user is a participant in

        Parameters
        ----------
        model : typing.Optional[GetAllMessagesForUserRequestModel]
            Payment model for metered API

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAllMessagesForUserResponse]
            Successfully retrieved all messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "chats/getAllMessages",
            method="GET",
            params={
                "model": model,
                "$top": top,
                "$skip": skip,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAllMessagesForUserResponse,
                    parse_obj_as(
                        type_=GetAllMessagesForUserResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
