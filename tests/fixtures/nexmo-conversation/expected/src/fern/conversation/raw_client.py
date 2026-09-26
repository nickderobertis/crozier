

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
from ..types.action import Action
from ..types.display_name import DisplayName
from ..types.event_method import EventMethod
from ..types.event_url import EventUrl
from ..types.format import Format
from ..types.image_url import ImageUrl
from ..types.name_conversation import NameConversation
from ..types.page_size import PageSize
from ..types.record_index import RecordIndex
from ..types.split import Split
from .types.create_conversation_request_properties import CreateConversationRequestProperties
from .types.create_conversation_response import CreateConversationResponse
from .types.list_conversations_request_order import ListConversationsRequestOrder
from .types.list_conversations_response import ListConversationsResponse
from .types.replace_conversation_request_properties import ReplaceConversationRequestProperties
from .types.replace_conversation_response import ReplaceConversationResponse
from .types.retrieve_conversation_response import RetrieveConversationResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConversationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_conversations(
        self,
        *,
        date_start: typing.Optional[str] = None,
        date_end: typing.Optional[str] = None,
        page_size: typing.Optional[PageSize] = None,
        record_index: typing.Optional[RecordIndex] = None,
        order: typing.Optional[ListConversationsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListConversationsResponse]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/conversations](/api/conversation.v2#get-conversations).

        List all conversations associated with your application. This endpoint required an admin JWT. To find all conversations for the currently logged in user, see [GET /users/:id/conversations](#getuserConversations)

        Parameters
        ----------
        date_start : typing.Optional[str]
            Return the records that occurred after this point in time.

        date_end : typing.Optional[str]
            Return the records that occurred before this point in time.

        page_size : typing.Optional[PageSize]
            Return this amount of records in the response

        record_index : typing.Optional[RecordIndex]
            Return calls from this index in the response

        order : typing.Optional[ListConversationsRequestOrder]
            Return the records in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListConversationsResponse]
            List Conversations Response Payload Object.
        """
        _response = self._client_wrapper.httpx_client.request(
            "conversations",
            method="GET",
            params={
                "date_start": date_start,
                "date_end": date_end,
                "page_size": page_size,
                "record_index": record_index,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListConversationsResponse,
                    parse_obj_as(
                        type_=ListConversationsResponse,
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

    def create_conversation(
        self,
        *,
        display_name: typing.Optional[DisplayName] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameConversation] = OMIT,
        properties: typing.Optional[CreateConversationRequestProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateConversationResponse]:
        """
        Parameters
        ----------
        display_name : typing.Optional[DisplayName]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameConversation]

        properties : typing.Optional[CreateConversationRequestProperties]
            Conversation properties

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateConversationResponse]
            Create / Update Conversation Response Payload Object
        """
        _response = self._client_wrapper.httpx_client.request(
            "conversations",
            method="POST",
            json={
                "display_name": display_name,
                "image_url": image_url,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=CreateConversationRequestProperties, direction="write"
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
                    CreateConversationResponse,
                    parse_obj_as(
                        type_=CreateConversationResponse,
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

    def retrieve_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveConversationResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveConversationResponse]
            Retrieve a conversation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveConversationResponse,
                    parse_obj_as(
                        type_=RetrieveConversationResponse,
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

    def replace_conversation(
        self,
        conversation_id: str,
        *,
        display_name: typing.Optional[DisplayName] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameConversation] = OMIT,
        properties: typing.Optional[ReplaceConversationRequestProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ReplaceConversationResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        display_name : typing.Optional[DisplayName]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameConversation]

        properties : typing.Optional[ReplaceConversationRequestProperties]
            Conversation properties

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReplaceConversationResponse]
            Create / Update Conversation Response Payload Object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}",
            method="PUT",
            json={
                "display_name": display_name,
                "image_url": image_url,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=ReplaceConversationRequestProperties, direction="write"
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
                    ReplaceConversationResponse,
                    parse_obj_as(
                        type_=ReplaceConversationResponse,
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

    def delete_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Success response with empty JSON
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def record_conversation(
        self,
        conversation_id: str,
        *,
        action: Action,
        event_method: typing.Optional[EventMethod] = OMIT,
        event_url: typing.Optional[EventUrl] = OMIT,
        format: typing.Optional[Format] = OMIT,
        split: typing.Optional[Split] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        action : Action

        event_method : typing.Optional[EventMethod]

        event_url : typing.Optional[EventUrl]

        format : typing.Optional[Format]

        split : typing.Optional[Split]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/record",
            method="PUT",
            json={
                "action": action,
                "event_method": event_method,
                "event_url": event_url,
                "format": format,
                "split": split,
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


class AsyncRawConversationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_conversations(
        self,
        *,
        date_start: typing.Optional[str] = None,
        date_end: typing.Optional[str] = None,
        page_size: typing.Optional[PageSize] = None,
        record_index: typing.Optional[RecordIndex] = None,
        order: typing.Optional[ListConversationsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListConversationsResponse]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/conversations](/api/conversation.v2#get-conversations).

        List all conversations associated with your application. This endpoint required an admin JWT. To find all conversations for the currently logged in user, see [GET /users/:id/conversations](#getuserConversations)

        Parameters
        ----------
        date_start : typing.Optional[str]
            Return the records that occurred after this point in time.

        date_end : typing.Optional[str]
            Return the records that occurred before this point in time.

        page_size : typing.Optional[PageSize]
            Return this amount of records in the response

        record_index : typing.Optional[RecordIndex]
            Return calls from this index in the response

        order : typing.Optional[ListConversationsRequestOrder]
            Return the records in ascending or descending order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListConversationsResponse]
            List Conversations Response Payload Object.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "conversations",
            method="GET",
            params={
                "date_start": date_start,
                "date_end": date_end,
                "page_size": page_size,
                "record_index": record_index,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListConversationsResponse,
                    parse_obj_as(
                        type_=ListConversationsResponse,
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

    async def create_conversation(
        self,
        *,
        display_name: typing.Optional[DisplayName] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameConversation] = OMIT,
        properties: typing.Optional[CreateConversationRequestProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateConversationResponse]:
        """
        Parameters
        ----------
        display_name : typing.Optional[DisplayName]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameConversation]

        properties : typing.Optional[CreateConversationRequestProperties]
            Conversation properties

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateConversationResponse]
            Create / Update Conversation Response Payload Object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "conversations",
            method="POST",
            json={
                "display_name": display_name,
                "image_url": image_url,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=CreateConversationRequestProperties, direction="write"
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
                    CreateConversationResponse,
                    parse_obj_as(
                        type_=CreateConversationResponse,
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

    async def retrieve_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveConversationResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveConversationResponse]
            Retrieve a conversation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveConversationResponse,
                    parse_obj_as(
                        type_=RetrieveConversationResponse,
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

    async def replace_conversation(
        self,
        conversation_id: str,
        *,
        display_name: typing.Optional[DisplayName] = OMIT,
        image_url: typing.Optional[ImageUrl] = OMIT,
        name: typing.Optional[NameConversation] = OMIT,
        properties: typing.Optional[ReplaceConversationRequestProperties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ReplaceConversationResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        display_name : typing.Optional[DisplayName]

        image_url : typing.Optional[ImageUrl]

        name : typing.Optional[NameConversation]

        properties : typing.Optional[ReplaceConversationRequestProperties]
            Conversation properties

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReplaceConversationResponse]
            Create / Update Conversation Response Payload Object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}",
            method="PUT",
            json={
                "display_name": display_name,
                "image_url": image_url,
                "name": name,
                "properties": convert_and_respect_annotation_metadata(
                    object_=properties, annotation=ReplaceConversationRequestProperties, direction="write"
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
                    ReplaceConversationResponse,
                    parse_obj_as(
                        type_=ReplaceConversationResponse,
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

    async def delete_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Success response with empty JSON
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def record_conversation(
        self,
        conversation_id: str,
        *,
        action: Action,
        event_method: typing.Optional[EventMethod] = OMIT,
        event_url: typing.Optional[EventUrl] = OMIT,
        format: typing.Optional[Format] = OMIT,
        split: typing.Optional[Split] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        action : Action

        event_method : typing.Optional[EventMethod]

        event_url : typing.Optional[EventUrl]

        format : typing.Optional[Format]

        split : typing.Optional[Split]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/record",
            method="PUT",
            json={
                "action": action,
                "event_method": event_method,
                "event_url": event_url,
                "format": format,
                "split": split,
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
