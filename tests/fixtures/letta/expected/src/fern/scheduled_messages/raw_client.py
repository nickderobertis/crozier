

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
from .types.scheduled_messages_delete_scheduled_message_request_body import (
    ScheduledMessagesDeleteScheduledMessageRequestBody,
)
from .types.scheduled_messages_delete_scheduled_message_response import ScheduledMessagesDeleteScheduledMessageResponse
from .types.scheduled_messages_list_scheduled_messages_response import ScheduledMessagesListScheduledMessagesResponse
from .types.scheduled_messages_retrieve_scheduled_message_response import (
    ScheduledMessagesRetrieveScheduledMessageResponse,
)
from .types.scheduled_messages_schedule_agent_message_request_include_return_message_types_item import (
    ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem,
)
from .types.scheduled_messages_schedule_agent_message_request_messages_item import (
    ScheduledMessagesScheduleAgentMessageRequestMessagesItem,
)
from .types.scheduled_messages_schedule_agent_message_request_schedule import (
    ScheduledMessagesScheduleAgentMessageRequestSchedule,
)
from .types.scheduled_messages_schedule_agent_message_response import ScheduledMessagesScheduleAgentMessageResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawScheduledMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def scheduled_messages_list_scheduled_messages(
        self,
        agent_id: str,
        *,
        limit: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScheduledMessagesListScheduledMessagesResponse]:
        """
        List all scheduled messages for a specific agent.

        Parameters
        ----------
        agent_id : str

        limit : typing.Optional[str]

        after : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScheduledMessagesListScheduledMessagesResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/schedule",
            method="GET",
            params={
                "limit": limit,
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduledMessagesListScheduledMessagesResponse,
                    parse_obj_as(
                        type_=ScheduledMessagesListScheduledMessagesResponse,
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

    def scheduled_messages_schedule_agent_message(
        self,
        agent_id: str,
        *,
        messages: typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestMessagesItem],
        schedule: ScheduledMessagesScheduleAgentMessageRequestSchedule,
        max_steps: typing.Optional[float] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[
            typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScheduledMessagesScheduleAgentMessageResponse]:
        """
        Schedule a message to be sent by the agent at a specified time or on a recurring basis.

        Parameters
        ----------
        agent_id : str

        messages : typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestMessagesItem]

        schedule : ScheduledMessagesScheduleAgentMessageRequestSchedule

        max_steps : typing.Optional[float]

        callback_url : typing.Optional[str]

        include_return_message_types : typing.Optional[typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScheduledMessagesScheduleAgentMessageResponse]
            201
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/schedule",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestMessagesItem],
                    direction="write",
                ),
                "max_steps": max_steps,
                "callback_url": callback_url,
                "include_return_message_types": include_return_message_types,
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=ScheduledMessagesScheduleAgentMessageRequestSchedule, direction="write"
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
                    ScheduledMessagesScheduleAgentMessageResponse,
                    parse_obj_as(
                        type_=ScheduledMessagesScheduleAgentMessageResponse,
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

    def scheduled_messages_retrieve_scheduled_message(
        self, agent_id: str, scheduled_message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ScheduledMessagesRetrieveScheduledMessageResponse]:
        """
        Retrieve a scheduled message by its ID for a specific agent.

        Parameters
        ----------
        agent_id : str

        scheduled_message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScheduledMessagesRetrieveScheduledMessageResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/schedule/{encode_path_param(scheduled_message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduledMessagesRetrieveScheduledMessageResponse,
                    parse_obj_as(
                        type_=ScheduledMessagesRetrieveScheduledMessageResponse,
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

    def scheduled_messages_delete_scheduled_message(
        self,
        agent_id: str,
        scheduled_message_id: str,
        *,
        request: typing.Optional[ScheduledMessagesDeleteScheduledMessageRequestBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ScheduledMessagesDeleteScheduledMessageResponse]:
        """
        Delete a scheduled message by its ID for a specific agent.

        Parameters
        ----------
        agent_id : str

        scheduled_message_id : str

        request : typing.Optional[ScheduledMessagesDeleteScheduledMessageRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ScheduledMessagesDeleteScheduledMessageResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/schedule/{encode_path_param(scheduled_message_id)}",
            method="DELETE",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Optional[ScheduledMessagesDeleteScheduledMessageRequestBody],
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduledMessagesDeleteScheduledMessageResponse,
                    parse_obj_as(
                        type_=ScheduledMessagesDeleteScheduledMessageResponse,
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


class AsyncRawScheduledMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def scheduled_messages_list_scheduled_messages(
        self,
        agent_id: str,
        *,
        limit: typing.Optional[str] = None,
        after: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScheduledMessagesListScheduledMessagesResponse]:
        """
        List all scheduled messages for a specific agent.

        Parameters
        ----------
        agent_id : str

        limit : typing.Optional[str]

        after : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScheduledMessagesListScheduledMessagesResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/schedule",
            method="GET",
            params={
                "limit": limit,
                "after": after,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduledMessagesListScheduledMessagesResponse,
                    parse_obj_as(
                        type_=ScheduledMessagesListScheduledMessagesResponse,
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

    async def scheduled_messages_schedule_agent_message(
        self,
        agent_id: str,
        *,
        messages: typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestMessagesItem],
        schedule: ScheduledMessagesScheduleAgentMessageRequestSchedule,
        max_steps: typing.Optional[float] = OMIT,
        callback_url: typing.Optional[str] = OMIT,
        include_return_message_types: typing.Optional[
            typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScheduledMessagesScheduleAgentMessageResponse]:
        """
        Schedule a message to be sent by the agent at a specified time or on a recurring basis.

        Parameters
        ----------
        agent_id : str

        messages : typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestMessagesItem]

        schedule : ScheduledMessagesScheduleAgentMessageRequestSchedule

        max_steps : typing.Optional[float]

        callback_url : typing.Optional[str]

        include_return_message_types : typing.Optional[typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScheduledMessagesScheduleAgentMessageResponse]
            201
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/schedule",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages,
                    annotation=typing.Sequence[ScheduledMessagesScheduleAgentMessageRequestMessagesItem],
                    direction="write",
                ),
                "max_steps": max_steps,
                "callback_url": callback_url,
                "include_return_message_types": include_return_message_types,
                "schedule": convert_and_respect_annotation_metadata(
                    object_=schedule, annotation=ScheduledMessagesScheduleAgentMessageRequestSchedule, direction="write"
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
                    ScheduledMessagesScheduleAgentMessageResponse,
                    parse_obj_as(
                        type_=ScheduledMessagesScheduleAgentMessageResponse,
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

    async def scheduled_messages_retrieve_scheduled_message(
        self, agent_id: str, scheduled_message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ScheduledMessagesRetrieveScheduledMessageResponse]:
        """
        Retrieve a scheduled message by its ID for a specific agent.

        Parameters
        ----------
        agent_id : str

        scheduled_message_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScheduledMessagesRetrieveScheduledMessageResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/schedule/{encode_path_param(scheduled_message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduledMessagesRetrieveScheduledMessageResponse,
                    parse_obj_as(
                        type_=ScheduledMessagesRetrieveScheduledMessageResponse,
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

    async def scheduled_messages_delete_scheduled_message(
        self,
        agent_id: str,
        scheduled_message_id: str,
        *,
        request: typing.Optional[ScheduledMessagesDeleteScheduledMessageRequestBody] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ScheduledMessagesDeleteScheduledMessageResponse]:
        """
        Delete a scheduled message by its ID for a specific agent.

        Parameters
        ----------
        agent_id : str

        scheduled_message_id : str

        request : typing.Optional[ScheduledMessagesDeleteScheduledMessageRequestBody]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ScheduledMessagesDeleteScheduledMessageResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/agents/{encode_path_param(agent_id)}/schedule/{encode_path_param(scheduled_message_id)}",
            method="DELETE",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Optional[ScheduledMessagesDeleteScheduledMessageRequestBody],
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ScheduledMessagesDeleteScheduledMessageResponse,
                    parse_obj_as(
                        type_=ScheduledMessagesDeleteScheduledMessageResponse,
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
