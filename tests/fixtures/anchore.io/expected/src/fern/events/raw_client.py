

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..types.event_response import EventResponse
from ..types.event_types_list import EventTypesList
from ..types.events_list import EventsList


class RawEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_event_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EventTypesList]:
        """
        Returns list of event types in the category hierarchy

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EventTypesList]
            List of event types
        """
        _response = self._client_wrapper.httpx_client.request(
            "event_types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EventTypesList,
                    parse_obj_as(
                        type_=EventTypesList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_events(
        self,
        *,
        source_servicename: typing.Optional[str] = None,
        source_hostid: typing.Optional[str] = None,
        event_type: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        level: typing.Optional[str] = None,
        since: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EventsList]:
        """
        Returns a paginated list of events in the descending order of their occurrence. Optional query parameters may be used for filtering results

        Parameters
        ----------
        source_servicename : typing.Optional[str]
            Filter events by the originating service

        source_hostid : typing.Optional[str]
            Filter events by the originating host ID

        event_type : typing.Optional[str]
            Filter events by a prefix match on the event type (e.g. "user.image.")

        resource_type : typing.Optional[str]
            Filter events by the type of resource - tag, imageDigest, repository etc

        resource_id : typing.Optional[str]
            Filter events by the id of the resource

        level : typing.Optional[str]
            Filter events by the level - INFO or ERROR

        since : typing.Optional[str]
            Return events that occurred after the timestamp

        before : typing.Optional[str]
            Return events that occurred before the timestamp

        page : typing.Optional[int]
            Pagination controls - return the nth page of results. Defaults to first page if left empty

        limit : typing.Optional[int]
            Number of events in the result set. Defaults to 100 if left empty

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EventsList]
            Paginated list of event records and the next token
        """
        _response = self._client_wrapper.httpx_client.request(
            "events",
            method="GET",
            params={
                "source_servicename": source_servicename,
                "source_hostid": source_hostid,
                "event_type": event_type,
                "resource_type": resource_type,
                "resource_id": resource_id,
                "level": level,
                "since": since,
                "before": before,
                "page": page,
                "limit": limit,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EventsList,
                    parse_obj_as(
                        type_=EventsList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_events(
        self,
        *,
        before: typing.Optional[str] = None,
        since: typing.Optional[str] = None,
        level: typing.Optional[str] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[str]]:
        """
        Delete all or a subset of events filtered using the optional query parameters

        Parameters
        ----------
        before : typing.Optional[str]
            Delete events that occurred before the timestamp

        since : typing.Optional[str]
            Delete events that occurred after the timestamp

        level : typing.Optional[str]
            Delete events that match the level - INFO or ERROR

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            List of deleted event IDs
        """
        _response = self._client_wrapper.httpx_client.request(
            "events",
            method="DELETE",
            params={
                "before": before,
                "since": since,
                "level": level,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_event(
        self,
        event_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EventResponse]:
        """
        Lookup an event by its event ID

        Parameters
        ----------
        event_id : str
            Event ID of the event for lookup

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EventResponse]
            Single event record
        """
        _response = self._client_wrapper.httpx_client.request(
            f"events/{jsonable_encoder(event_id)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EventResponse,
                    parse_obj_as(
                        type_=EventResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_event(
        self,
        event_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Delete an event by its event ID

        Parameters
        ----------
        event_id : str
            Event ID of the event to be deleted

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"events/{jsonable_encoder(event_id)}",
            method="DELETE",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_event_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EventTypesList]:
        """
        Returns list of event types in the category hierarchy

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EventTypesList]
            List of event types
        """
        _response = await self._client_wrapper.httpx_client.request(
            "event_types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EventTypesList,
                    parse_obj_as(
                        type_=EventTypesList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_events(
        self,
        *,
        source_servicename: typing.Optional[str] = None,
        source_hostid: typing.Optional[str] = None,
        event_type: typing.Optional[str] = None,
        resource_type: typing.Optional[str] = None,
        resource_id: typing.Optional[str] = None,
        level: typing.Optional[str] = None,
        since: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EventsList]:
        """
        Returns a paginated list of events in the descending order of their occurrence. Optional query parameters may be used for filtering results

        Parameters
        ----------
        source_servicename : typing.Optional[str]
            Filter events by the originating service

        source_hostid : typing.Optional[str]
            Filter events by the originating host ID

        event_type : typing.Optional[str]
            Filter events by a prefix match on the event type (e.g. "user.image.")

        resource_type : typing.Optional[str]
            Filter events by the type of resource - tag, imageDigest, repository etc

        resource_id : typing.Optional[str]
            Filter events by the id of the resource

        level : typing.Optional[str]
            Filter events by the level - INFO or ERROR

        since : typing.Optional[str]
            Return events that occurred after the timestamp

        before : typing.Optional[str]
            Return events that occurred before the timestamp

        page : typing.Optional[int]
            Pagination controls - return the nth page of results. Defaults to first page if left empty

        limit : typing.Optional[int]
            Number of events in the result set. Defaults to 100 if left empty

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EventsList]
            Paginated list of event records and the next token
        """
        _response = await self._client_wrapper.httpx_client.request(
            "events",
            method="GET",
            params={
                "source_servicename": source_servicename,
                "source_hostid": source_hostid,
                "event_type": event_type,
                "resource_type": resource_type,
                "resource_id": resource_id,
                "level": level,
                "since": since,
                "before": before,
                "page": page,
                "limit": limit,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EventsList,
                    parse_obj_as(
                        type_=EventsList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_events(
        self,
        *,
        before: typing.Optional[str] = None,
        since: typing.Optional[str] = None,
        level: typing.Optional[str] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        Delete all or a subset of events filtered using the optional query parameters

        Parameters
        ----------
        before : typing.Optional[str]
            Delete events that occurred before the timestamp

        since : typing.Optional[str]
            Delete events that occurred after the timestamp

        level : typing.Optional[str]
            Delete events that match the level - INFO or ERROR

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            List of deleted event IDs
        """
        _response = await self._client_wrapper.httpx_client.request(
            "events",
            method="DELETE",
            params={
                "before": before,
                "since": since,
                "level": level,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_event(
        self,
        event_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EventResponse]:
        """
        Lookup an event by its event ID

        Parameters
        ----------
        event_id : str
            Event ID of the event for lookup

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EventResponse]
            Single event record
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"events/{jsonable_encoder(event_id)}",
            method="GET",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EventResponse,
                    parse_obj_as(
                        type_=EventResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_event(
        self,
        event_id: str,
        *,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Delete an event by its event ID

        Parameters
        ----------
        event_id : str
            Event ID of the event to be deleted

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"events/{jsonable_encoder(event_id)}",
            method="DELETE",
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
