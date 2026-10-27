

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
from .types.get_channel_message_request_expand import GetChannelMessageRequestExpand
from .types.list_channel_messages_request_expand import ListChannelMessagesRequestExpand
from .types.list_channel_messages_response import ListChannelMessagesResponse
from .types.send_channel_message_request_body import SendChannelMessageRequestBody
from .types.send_channel_message_request_hosted_contents_item import SendChannelMessageRequestHostedContentsItem
from .types.send_channel_message_request_importance import SendChannelMessageRequestImportance
from .types.send_channel_message_request_mentions_item import SendChannelMessageRequestMentionsItem
from .types.update_channel_message_request_body import UpdateChannelMessageRequestBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawChannelMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_channel_messages(
        self,
        team_id: str,
        channel_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        expand: typing.Optional[ListChannelMessagesRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListChannelMessagesResponse]:
        """
        Retrieve the list of messages in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        expand : typing.Optional[ListChannelMessagesRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListChannelMessagesResponse]
            Successfully retrieved channel messages
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/messages",
            method="GET",
            params={
                "$top": top,
                "$skip": skip,
                "$expand": expand,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListChannelMessagesResponse,
                    parse_obj_as(
                        type_=ListChannelMessagesResponse,
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

    def send_channel_message(
        self,
        team_id: str,
        channel_id: str,
        *,
        body: SendChannelMessageRequestBody,
        importance: typing.Optional[SendChannelMessageRequestImportance] = OMIT,
        subject: typing.Optional[str] = OMIT,
        mentions: typing.Optional[typing.Sequence[SendChannelMessageRequestMentionsItem]] = OMIT,
        attachments: typing.Optional[typing.Sequence[ChatMessageAttachment]] = OMIT,
        hosted_contents: typing.Optional[typing.Sequence[SendChannelMessageRequestHostedContentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChatMessage]:
        """
        Send a new message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        body : SendChannelMessageRequestBody

        importance : typing.Optional[SendChannelMessageRequestImportance]

        subject : typing.Optional[str]
            The subject of the channel message

        mentions : typing.Optional[typing.Sequence[SendChannelMessageRequestMentionsItem]]

        attachments : typing.Optional[typing.Sequence[ChatMessageAttachment]]

        hosted_contents : typing.Optional[typing.Sequence[SendChannelMessageRequestHostedContentsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChatMessage]
            Message sent successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/messages",
            method="POST",
            json={
                "body": convert_and_respect_annotation_metadata(
                    object_=body, annotation=SendChannelMessageRequestBody, direction="write"
                ),
                "importance": importance,
                "subject": subject,
                "mentions": convert_and_respect_annotation_metadata(
                    object_=mentions,
                    annotation=typing.Sequence[SendChannelMessageRequestMentionsItem],
                    direction="write",
                ),
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments, annotation=typing.Sequence[ChatMessageAttachment], direction="write"
                ),
                "hostedContents": convert_and_respect_annotation_metadata(
                    object_=hosted_contents,
                    annotation=typing.Sequence[SendChannelMessageRequestHostedContentsItem],
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

    def get_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chat_message_id: str,
        *,
        expand: typing.Optional[GetChannelMessageRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ChatMessage]:
        """
        Retrieve a specific message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        chat_message_id : str
            The unique identifier of the chat message

        expand : typing.Optional[GetChannelMessageRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChatMessage]
            Successfully retrieved channel message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/messages/{encode_path_param(chat_message_id)}",
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

    def delete_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chat_message_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Soft delete a message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        chat_message_id : str
            The unique identifier of the chat message

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/messages/{encode_path_param(chat_message_id)}",
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

    def update_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chat_message_id: str,
        *,
        body: typing.Optional[UpdateChannelMessageRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Update a message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        chat_message_id : str
            The unique identifier of the chat message

        body : typing.Optional[UpdateChannelMessageRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/messages/{encode_path_param(chat_message_id)}",
            method="PATCH",
            json={
                "body": convert_and_respect_annotation_metadata(
                    object_=body, annotation=UpdateChannelMessageRequestBody, direction="write"
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


class AsyncRawChannelMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_channel_messages(
        self,
        team_id: str,
        channel_id: str,
        *,
        top: typing.Optional[int] = None,
        skip: typing.Optional[int] = None,
        expand: typing.Optional[ListChannelMessagesRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListChannelMessagesResponse]:
        """
        Retrieve the list of messages in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        top : typing.Optional[int]
            Number of items to return

        skip : typing.Optional[int]
            Number of items to skip for pagination

        expand : typing.Optional[ListChannelMessagesRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListChannelMessagesResponse]
            Successfully retrieved channel messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/messages",
            method="GET",
            params={
                "$top": top,
                "$skip": skip,
                "$expand": expand,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListChannelMessagesResponse,
                    parse_obj_as(
                        type_=ListChannelMessagesResponse,
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

    async def send_channel_message(
        self,
        team_id: str,
        channel_id: str,
        *,
        body: SendChannelMessageRequestBody,
        importance: typing.Optional[SendChannelMessageRequestImportance] = OMIT,
        subject: typing.Optional[str] = OMIT,
        mentions: typing.Optional[typing.Sequence[SendChannelMessageRequestMentionsItem]] = OMIT,
        attachments: typing.Optional[typing.Sequence[ChatMessageAttachment]] = OMIT,
        hosted_contents: typing.Optional[typing.Sequence[SendChannelMessageRequestHostedContentsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChatMessage]:
        """
        Send a new message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        body : SendChannelMessageRequestBody

        importance : typing.Optional[SendChannelMessageRequestImportance]

        subject : typing.Optional[str]
            The subject of the channel message

        mentions : typing.Optional[typing.Sequence[SendChannelMessageRequestMentionsItem]]

        attachments : typing.Optional[typing.Sequence[ChatMessageAttachment]]

        hosted_contents : typing.Optional[typing.Sequence[SendChannelMessageRequestHostedContentsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChatMessage]
            Message sent successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/messages",
            method="POST",
            json={
                "body": convert_and_respect_annotation_metadata(
                    object_=body, annotation=SendChannelMessageRequestBody, direction="write"
                ),
                "importance": importance,
                "subject": subject,
                "mentions": convert_and_respect_annotation_metadata(
                    object_=mentions,
                    annotation=typing.Sequence[SendChannelMessageRequestMentionsItem],
                    direction="write",
                ),
                "attachments": convert_and_respect_annotation_metadata(
                    object_=attachments, annotation=typing.Sequence[ChatMessageAttachment], direction="write"
                ),
                "hostedContents": convert_and_respect_annotation_metadata(
                    object_=hosted_contents,
                    annotation=typing.Sequence[SendChannelMessageRequestHostedContentsItem],
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

    async def get_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chat_message_id: str,
        *,
        expand: typing.Optional[GetChannelMessageRequestExpand] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ChatMessage]:
        """
        Retrieve a specific message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        chat_message_id : str
            The unique identifier of the chat message

        expand : typing.Optional[GetChannelMessageRequestExpand]
            OData expand query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChatMessage]
            Successfully retrieved channel message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/messages/{encode_path_param(chat_message_id)}",
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

    async def delete_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chat_message_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Soft delete a message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        chat_message_id : str
            The unique identifier of the chat message

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/messages/{encode_path_param(chat_message_id)}",
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

    async def update_channel_message(
        self,
        team_id: str,
        channel_id: str,
        chat_message_id: str,
        *,
        body: typing.Optional[UpdateChannelMessageRequestBody] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Update a message in a channel

        Parameters
        ----------
        team_id : str
            The unique identifier of the team

        channel_id : str
            The unique identifier of the channel

        chat_message_id : str
            The unique identifier of the chat message

        body : typing.Optional[UpdateChannelMessageRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"teams/{encode_path_param(team_id)}/channels/{encode_path_param(channel_id)}/messages/{encode_path_param(chat_message_id)}",
            method="PATCH",
            json={
                "body": convert_and_respect_annotation_metadata(
                    object_=body, annotation=UpdateChannelMessageRequestBody, direction="write"
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
