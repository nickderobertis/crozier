

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.event_body import EventBody
from ..types.event_retrieved import EventRetrieved
from ..types.event_type import EventType
from ..types.member_id import MemberId
from .types.create_event_response import CreateEventResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEventClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_events(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[EventRetrieved]]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/events](/api/conversation.v2#get-events).

        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[EventRetrieved]]
            Retrieve Events Response Payload Object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/events",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[EventRetrieved],
                    parse_obj_as(
                        type_=typing.List[EventRetrieved],
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

    def create_event(
        self,
        conversation_id: str,
        *,
        from_: MemberId,
        type: EventType,
        body: typing.Optional[EventBody] = OMIT,
        to: typing.Optional[MemberId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateEventResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        from_ : MemberId

        type : EventType

        body : typing.Optional[EventBody]

        to : typing.Optional[MemberId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateEventResponse]
            Create New Event Response Payload Object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/events",
            method="POST",
            json={
                "body": body,
                "from": from_,
                "to": to,
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
                    CreateEventResponse,
                    parse_obj_as(
                        type_=CreateEventResponse,
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

    def get_event(
        self, conversation_id: str, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EventRetrieved]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        event_id : str
            Event ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EventRetrieved]
            Retrieve an event Content Payload
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/events/{encode_path_param(event_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EventRetrieved,
                    parse_obj_as(
                        type_=EventRetrieved,
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

    def delete_event(
        self, conversation_id: str, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        event_id : str
            Event ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Success response with empty JSON
        """
        _response = self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/events/{encode_path_param(event_id)}",
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


class AsyncRawEventClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_events(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[EventRetrieved]]:
        """
        This endpoint is **DEPRECATED**. Please use [/v0.2/events](/api/conversation.v2#get-events).

        Parameters
        ----------
        conversation_id : str
            Conversation ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[EventRetrieved]]
            Retrieve Events Response Payload Object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/events",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[EventRetrieved],
                    parse_obj_as(
                        type_=typing.List[EventRetrieved],
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

    async def create_event(
        self,
        conversation_id: str,
        *,
        from_: MemberId,
        type: EventType,
        body: typing.Optional[EventBody] = OMIT,
        to: typing.Optional[MemberId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateEventResponse]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        from_ : MemberId

        type : EventType

        body : typing.Optional[EventBody]

        to : typing.Optional[MemberId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateEventResponse]
            Create New Event Response Payload Object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/events",
            method="POST",
            json={
                "body": body,
                "from": from_,
                "to": to,
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
                    CreateEventResponse,
                    parse_obj_as(
                        type_=CreateEventResponse,
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

    async def get_event(
        self, conversation_id: str, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EventRetrieved]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        event_id : str
            Event ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EventRetrieved]
            Retrieve an event Content Payload
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/events/{encode_path_param(event_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EventRetrieved,
                    parse_obj_as(
                        type_=EventRetrieved,
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

    async def delete_event(
        self, conversation_id: str, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Parameters
        ----------
        conversation_id : str
            Conversation ID

        event_id : str
            Event ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Success response with empty JSON
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"conversations/{encode_path_param(conversation_id)}/events/{encode_path_param(event_id)}",
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
