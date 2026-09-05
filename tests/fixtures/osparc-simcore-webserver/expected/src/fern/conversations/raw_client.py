

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.conversation_message_type import ConversationMessageType
from ..types.conversation_name import ConversationName
from ..types.conversation_status import ConversationStatus
from ..types.conversation_type import ConversationType
from ..types.envelope_conversation_message_rest_get import EnvelopeConversationMessageRestGet
from ..types.envelope_conversation_rest_get import EnvelopeConversationRestGet
from ..types.page_conversation_message_rest_get import PageConversationMessageRestGet
from ..types.page_conversation_rest_get import PageConversationRestGet
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConversationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_conversations(
        self,
        *,
        type: ConversationType,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[ConversationStatus] = None,
        is_read_by_user: typing.Optional[bool] = None,
        is_read_by_support: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageConversationRestGet]:
        """
        Parameters
        ----------
        type : ConversationType

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[ConversationStatus]

        is_read_by_user : typing.Optional[bool]

        is_read_by_support : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageConversationRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/conversations",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "type": type,
                "status": status,
                "is_read_by_user": is_read_by_user,
                "is_read_by_support": is_read_by_support,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageConversationRestGet,
                    parse_obj_as(
                        type_=PageConversationRestGet,
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
        type: ConversationType,
        name: typing.Optional[ConversationName] = OMIT,
        extra_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeConversationRestGet]:
        """
        Parameters
        ----------
        type : ConversationType

        name : typing.Optional[ConversationName]

        extra_context : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeConversationRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/conversations",
            method="POST",
            json={
                "name": name,
                "type": type,
                "extraContext": extra_context,
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
                    EnvelopeConversationRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationRestGet,
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

    def get_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeConversationRestGet]:
        """
        Parameters
        ----------
        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeConversationRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeConversationRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationRestGet,
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
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}",
            method="DELETE",
            request_options=request_options,
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

    def update_conversation(
        self,
        conversation_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        extra_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        is_read_by_user: typing.Optional[bool] = OMIT,
        is_read_by_support: typing.Optional[bool] = OMIT,
        status: typing.Optional[ConversationStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeConversationRestGet]:
        """
        Parameters
        ----------
        conversation_id : str

        name : typing.Optional[str]

        extra_context : typing.Optional[typing.Dict[str, typing.Any]]

        is_read_by_user : typing.Optional[bool]

        is_read_by_support : typing.Optional[bool]

        status : typing.Optional[ConversationStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeConversationRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}",
            method="PATCH",
            json={
                "name": name,
                "extraContext": extra_context,
                "isReadByUser": is_read_by_user,
                "isReadBySupport": is_read_by_support,
                "status": status,
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
                    EnvelopeConversationRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationRestGet,
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

    def list_conversation_messages(
        self,
        conversation_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageConversationMessageRestGet]:
        """
        Parameters
        ----------
        conversation_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageConversationMessageRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}/messages",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageConversationMessageRestGet,
                    parse_obj_as(
                        type_=PageConversationMessageRestGet,
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

    def create_conversation_message(
        self,
        conversation_id: str,
        *,
        content: str,
        type: ConversationMessageType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeConversationMessageRestGet]:
        """
        Parameters
        ----------
        conversation_id : str

        content : str

        type : ConversationMessageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeConversationMessageRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}/messages",
            method="POST",
            json={
                "content": content,
                "type": type,
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
                    EnvelopeConversationMessageRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationMessageRestGet,
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

    def get_conversation_message(
        self, conversation_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeConversationMessageRestGet]:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeConversationMessageRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeConversationMessageRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationMessageRestGet,
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

    def update_conversation_message(
        self,
        conversation_id: str,
        message_id: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeConversationMessageRestGet]:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeConversationMessageRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}",
            method="PUT",
            json={
                "content": content,
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
                    EnvelopeConversationMessageRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationMessageRestGet,
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

    def delete_conversation_message(
        self, conversation_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}",
            method="DELETE",
            request_options=request_options,
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

    def trigger_chatbot_processing(
        self, conversation_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}:trigger-chatbot",
            method="POST",
            request_options=request_options,
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


class AsyncRawConversationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_conversations(
        self,
        *,
        type: ConversationType,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[ConversationStatus] = None,
        is_read_by_user: typing.Optional[bool] = None,
        is_read_by_support: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageConversationRestGet]:
        """
        Parameters
        ----------
        type : ConversationType

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        status : typing.Optional[ConversationStatus]

        is_read_by_user : typing.Optional[bool]

        is_read_by_support : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageConversationRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/conversations",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "type": type,
                "status": status,
                "is_read_by_user": is_read_by_user,
                "is_read_by_support": is_read_by_support,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageConversationRestGet,
                    parse_obj_as(
                        type_=PageConversationRestGet,
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
        type: ConversationType,
        name: typing.Optional[ConversationName] = OMIT,
        extra_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeConversationRestGet]:
        """
        Parameters
        ----------
        type : ConversationType

        name : typing.Optional[ConversationName]

        extra_context : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeConversationRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/conversations",
            method="POST",
            json={
                "name": name,
                "type": type,
                "extraContext": extra_context,
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
                    EnvelopeConversationRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationRestGet,
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

    async def get_conversation(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeConversationRestGet]:
        """
        Parameters
        ----------
        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeConversationRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeConversationRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationRestGet,
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
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        conversation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}",
            method="DELETE",
            request_options=request_options,
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

    async def update_conversation(
        self,
        conversation_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        extra_context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        is_read_by_user: typing.Optional[bool] = OMIT,
        is_read_by_support: typing.Optional[bool] = OMIT,
        status: typing.Optional[ConversationStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeConversationRestGet]:
        """
        Parameters
        ----------
        conversation_id : str

        name : typing.Optional[str]

        extra_context : typing.Optional[typing.Dict[str, typing.Any]]

        is_read_by_user : typing.Optional[bool]

        is_read_by_support : typing.Optional[bool]

        status : typing.Optional[ConversationStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeConversationRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}",
            method="PATCH",
            json={
                "name": name,
                "extraContext": extra_context,
                "isReadByUser": is_read_by_user,
                "isReadBySupport": is_read_by_support,
                "status": status,
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
                    EnvelopeConversationRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationRestGet,
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

    async def list_conversation_messages(
        self,
        conversation_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageConversationMessageRestGet]:
        """
        Parameters
        ----------
        conversation_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageConversationMessageRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}/messages",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageConversationMessageRestGet,
                    parse_obj_as(
                        type_=PageConversationMessageRestGet,
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

    async def create_conversation_message(
        self,
        conversation_id: str,
        *,
        content: str,
        type: ConversationMessageType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeConversationMessageRestGet]:
        """
        Parameters
        ----------
        conversation_id : str

        content : str

        type : ConversationMessageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeConversationMessageRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}/messages",
            method="POST",
            json={
                "content": content,
                "type": type,
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
                    EnvelopeConversationMessageRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationMessageRestGet,
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

    async def get_conversation_message(
        self, conversation_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeConversationMessageRestGet]:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeConversationMessageRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeConversationMessageRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationMessageRestGet,
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

    async def update_conversation_message(
        self,
        conversation_id: str,
        message_id: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeConversationMessageRestGet]:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        content : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeConversationMessageRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}",
            method="PUT",
            json={
                "content": content,
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
                    EnvelopeConversationMessageRestGet,
                    parse_obj_as(
                        type_=EnvelopeConversationMessageRestGet,
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

    async def delete_conversation_message(
        self, conversation_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}",
            method="DELETE",
            request_options=request_options,
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

    async def trigger_chatbot_processing(
        self, conversation_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        conversation_id : str

        message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/conversations/{encode_path_param(conversation_id)}/messages/{encode_path_param(message_id)}:trigger-chatbot",
            method="POST",
            request_options=request_options,
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
