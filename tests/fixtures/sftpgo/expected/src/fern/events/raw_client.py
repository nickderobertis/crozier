

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.api_response import ApiResponse
from ..types.event_protocols import EventProtocols
from ..types.fs_event import FsEvent
from ..types.fs_event_action import FsEventAction
from ..types.fs_event_status import FsEventStatus
from ..types.fs_providers import FsProviders
from ..types.log_event import LogEvent
from ..types.log_event_type import LogEventType
from ..types.provider_event import ProviderEvent
from ..types.provider_event_action import ProviderEventAction
from ..types.provider_event_object_type import ProviderEventObjectType
from .types.get_fs_events_request_order import GetFsEventsRequestOrder
from .types.get_log_events_request_order import GetLogEventsRequestOrder
from .types.get_provider_events_request_order import GetProviderEventsRequestOrder
from pydantic import ValidationError


class RawEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_fs_events(
        self,
        *,
        start_timestamp: typing.Optional[int] = None,
        end_timestamp: typing.Optional[int] = None,
        actions: typing.Optional[typing.Union[FsEventAction, typing.Sequence[FsEventAction]]] = None,
        username: typing.Optional[str] = None,
        ip: typing.Optional[str] = None,
        ssh_cmd: typing.Optional[str] = None,
        fs_provider: typing.Optional[FsProviders] = None,
        bucket: typing.Optional[str] = None,
        endpoint: typing.Optional[str] = None,
        protocols: typing.Optional[typing.Union[EventProtocols, typing.Sequence[EventProtocols]]] = None,
        statuses: typing.Optional[typing.Union[FsEventStatus, typing.Sequence[FsEventStatus]]] = None,
        instance_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        csv_export: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetFsEventsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[FsEvent]]:
        """
        Returns an array with one or more filesystem events applying the specified filters. This API is only available if you configure an "eventsearcher" plugin

        Parameters
        ----------
        start_timestamp : typing.Optional[int]
            the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter

        end_timestamp : typing.Optional[int]
            the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter

        actions : typing.Optional[typing.Union[FsEventAction, typing.Sequence[FsEventAction]]]
            the event action must be included among those specified. Empty or missing means omit this filter. Actions must be specified comma separated

        username : typing.Optional[str]
            the event username must be the same as the one specified. Empty or missing means omit this filter

        ip : typing.Optional[str]
            the event IP must be the same as the one specified. Empty or missing means omit this filter

        ssh_cmd : typing.Optional[str]
            the event SSH command must be the same as the one specified. Empty or missing means omit this filter

        fs_provider : typing.Optional[FsProviders]
            the event filesystem provider must be the same as the one specified. Empty or missing means omit this filter

        bucket : typing.Optional[str]
            the bucket must be the same as the one specified. Empty or missing means omit this filter

        endpoint : typing.Optional[str]
            the endpoint must be the same as the one specified. Empty or missing means omit this filter

        protocols : typing.Optional[typing.Union[EventProtocols, typing.Sequence[EventProtocols]]]
            the event protocol must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        statuses : typing.Optional[typing.Union[FsEventStatus, typing.Sequence[FsEventStatus]]]
            the event status must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        instance_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        from_id : typing.Optional[str]
            the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter.

        role : typing.Optional[str]
            User role. Empty or missing means omit this filter. Ignored if the admin has a role

        csv_export : typing.Optional[bool]
            If enabled, events are exported as a CSV file

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 1000, default is 100

        order : typing.Optional[GetFsEventsRequestOrder]
            Ordering events by timestamp. Default DESC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[FsEvent]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "events/fs",
            method="GET",
            params={
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
                "actions": ",".join(map(str, actions)) if isinstance(actions, (list, tuple, set)) else actions,
                "username": username,
                "ip": ip,
                "ssh_cmd": ssh_cmd,
                "fs_provider": fs_provider,
                "bucket": bucket,
                "endpoint": endpoint,
                "protocols": ",".join(map(str, protocols)) if isinstance(protocols, (list, tuple, set)) else protocols,
                "statuses": ",".join(map(str, statuses)) if isinstance(statuses, (list, tuple, set)) else statuses,
                "instance_ids": ",".join(map(str, instance_ids))
                if isinstance(instance_ids, (list, tuple, set))
                else instance_ids,
                "from_id": from_id,
                "role": role,
                "csv_export": csv_export,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FsEvent],
                    parse_obj_as(
                        type_=typing.List[FsEvent],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    def get_provider_events(
        self,
        *,
        start_timestamp: typing.Optional[int] = None,
        end_timestamp: typing.Optional[int] = None,
        actions: typing.Optional[typing.Union[ProviderEventAction, typing.Sequence[ProviderEventAction]]] = None,
        username: typing.Optional[str] = None,
        ip: typing.Optional[str] = None,
        object_name: typing.Optional[str] = None,
        object_types: typing.Optional[
            typing.Union[ProviderEventObjectType, typing.Sequence[ProviderEventObjectType]]
        ] = None,
        instance_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        csv_export: typing.Optional[bool] = None,
        omit_object_data: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetProviderEventsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ProviderEvent]]:
        """
        Returns an array with one or more provider events applying the specified filters. This API is only available if you configure an "eventsearcher" plugin

        Parameters
        ----------
        start_timestamp : typing.Optional[int]
            the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter

        end_timestamp : typing.Optional[int]
            the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter

        actions : typing.Optional[typing.Union[ProviderEventAction, typing.Sequence[ProviderEventAction]]]
            the event action must be included among those specified. Empty or missing means omit this filter. Actions must be specified comma separated

        username : typing.Optional[str]
            the event username must be the same as the one specified. Empty or missing means omit this filter

        ip : typing.Optional[str]
            the event IP must be the same as the one specified. Empty or missing means omit this filter

        object_name : typing.Optional[str]
            the event object name must be the same as the one specified. Empty or missing means omit this filter

        object_types : typing.Optional[typing.Union[ProviderEventObjectType, typing.Sequence[ProviderEventObjectType]]]
            the event object type must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        instance_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        from_id : typing.Optional[str]
            the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter.

        role : typing.Optional[str]
            Admin role. Empty or missing means omit this filter. Ignored if the admin has a role

        csv_export : typing.Optional[bool]
            If enabled, events are exported as a CSV file

        omit_object_data : typing.Optional[bool]
            If enabled, returned events will not contain the `object_data` field

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 1000, default is 100

        order : typing.Optional[GetProviderEventsRequestOrder]
            Ordering events by timestamp. Default DESC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ProviderEvent]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "events/provider",
            method="GET",
            params={
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
                "actions": ",".join(map(str, actions)) if isinstance(actions, (list, tuple, set)) else actions,
                "username": username,
                "ip": ip,
                "object_name": object_name,
                "object_types": ",".join(map(str, object_types))
                if isinstance(object_types, (list, tuple, set))
                else object_types,
                "instance_ids": ",".join(map(str, instance_ids))
                if isinstance(instance_ids, (list, tuple, set))
                else instance_ids,
                "from_id": from_id,
                "role": role,
                "csv_export": csv_export,
                "omit_object_data": omit_object_data,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ProviderEvent],
                    parse_obj_as(
                        type_=typing.List[ProviderEvent],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    def get_log_events(
        self,
        *,
        start_timestamp: typing.Optional[int] = None,
        end_timestamp: typing.Optional[int] = None,
        events: typing.Optional[typing.Union[LogEventType, typing.Sequence[LogEventType]]] = None,
        username: typing.Optional[str] = None,
        ip: typing.Optional[str] = None,
        protocols: typing.Optional[typing.Union[EventProtocols, typing.Sequence[EventProtocols]]] = None,
        instance_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        csv_export: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetLogEventsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[LogEvent]]:
        """
        Returns an array with one or more log events applying the specified filters. This API is only available if you configure an "eventsearcher" plugin

        Parameters
        ----------
        start_timestamp : typing.Optional[int]
            the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter

        end_timestamp : typing.Optional[int]
            the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter

        events : typing.Optional[typing.Union[LogEventType, typing.Sequence[LogEventType]]]
            the log events must be included among those specified. Empty or missing means omit this filter. Events must be specified comma separated

        username : typing.Optional[str]
            the event username must be the same as the one specified. Empty or missing means omit this filter

        ip : typing.Optional[str]
            the event IP must be the same as the one specified. Empty or missing means omit this filter

        protocols : typing.Optional[typing.Union[EventProtocols, typing.Sequence[EventProtocols]]]
            the event protocol must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        instance_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        from_id : typing.Optional[str]
            the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter.

        role : typing.Optional[str]
            User role. Empty or missing means omit this filter. Ignored if the admin has a role

        csv_export : typing.Optional[bool]
            If enabled, events are exported as a CSV file

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 1000, default is 100

        order : typing.Optional[GetLogEventsRequestOrder]
            Ordering events by timestamp. Default DESC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[LogEvent]]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "events/logs",
            method="GET",
            params={
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
                "events": ",".join(map(str, events)) if isinstance(events, (list, tuple, set)) else events,
                "username": username,
                "ip": ip,
                "protocols": ",".join(map(str, protocols)) if isinstance(protocols, (list, tuple, set)) else protocols,
                "instance_ids": ",".join(map(str, instance_ids))
                if isinstance(instance_ids, (list, tuple, set))
                else instance_ids,
                "from_id": from_id,
                "role": role,
                "csv_export": csv_export,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LogEvent],
                    parse_obj_as(
                        type_=typing.List[LogEvent],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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


class AsyncRawEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_fs_events(
        self,
        *,
        start_timestamp: typing.Optional[int] = None,
        end_timestamp: typing.Optional[int] = None,
        actions: typing.Optional[typing.Union[FsEventAction, typing.Sequence[FsEventAction]]] = None,
        username: typing.Optional[str] = None,
        ip: typing.Optional[str] = None,
        ssh_cmd: typing.Optional[str] = None,
        fs_provider: typing.Optional[FsProviders] = None,
        bucket: typing.Optional[str] = None,
        endpoint: typing.Optional[str] = None,
        protocols: typing.Optional[typing.Union[EventProtocols, typing.Sequence[EventProtocols]]] = None,
        statuses: typing.Optional[typing.Union[FsEventStatus, typing.Sequence[FsEventStatus]]] = None,
        instance_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        csv_export: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetFsEventsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[FsEvent]]:
        """
        Returns an array with one or more filesystem events applying the specified filters. This API is only available if you configure an "eventsearcher" plugin

        Parameters
        ----------
        start_timestamp : typing.Optional[int]
            the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter

        end_timestamp : typing.Optional[int]
            the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter

        actions : typing.Optional[typing.Union[FsEventAction, typing.Sequence[FsEventAction]]]
            the event action must be included among those specified. Empty or missing means omit this filter. Actions must be specified comma separated

        username : typing.Optional[str]
            the event username must be the same as the one specified. Empty or missing means omit this filter

        ip : typing.Optional[str]
            the event IP must be the same as the one specified. Empty or missing means omit this filter

        ssh_cmd : typing.Optional[str]
            the event SSH command must be the same as the one specified. Empty or missing means omit this filter

        fs_provider : typing.Optional[FsProviders]
            the event filesystem provider must be the same as the one specified. Empty or missing means omit this filter

        bucket : typing.Optional[str]
            the bucket must be the same as the one specified. Empty or missing means omit this filter

        endpoint : typing.Optional[str]
            the endpoint must be the same as the one specified. Empty or missing means omit this filter

        protocols : typing.Optional[typing.Union[EventProtocols, typing.Sequence[EventProtocols]]]
            the event protocol must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        statuses : typing.Optional[typing.Union[FsEventStatus, typing.Sequence[FsEventStatus]]]
            the event status must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        instance_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        from_id : typing.Optional[str]
            the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter.

        role : typing.Optional[str]
            User role. Empty or missing means omit this filter. Ignored if the admin has a role

        csv_export : typing.Optional[bool]
            If enabled, events are exported as a CSV file

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 1000, default is 100

        order : typing.Optional[GetFsEventsRequestOrder]
            Ordering events by timestamp. Default DESC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[FsEvent]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "events/fs",
            method="GET",
            params={
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
                "actions": ",".join(map(str, actions)) if isinstance(actions, (list, tuple, set)) else actions,
                "username": username,
                "ip": ip,
                "ssh_cmd": ssh_cmd,
                "fs_provider": fs_provider,
                "bucket": bucket,
                "endpoint": endpoint,
                "protocols": ",".join(map(str, protocols)) if isinstance(protocols, (list, tuple, set)) else protocols,
                "statuses": ",".join(map(str, statuses)) if isinstance(statuses, (list, tuple, set)) else statuses,
                "instance_ids": ",".join(map(str, instance_ids))
                if isinstance(instance_ids, (list, tuple, set))
                else instance_ids,
                "from_id": from_id,
                "role": role,
                "csv_export": csv_export,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FsEvent],
                    parse_obj_as(
                        type_=typing.List[FsEvent],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    async def get_provider_events(
        self,
        *,
        start_timestamp: typing.Optional[int] = None,
        end_timestamp: typing.Optional[int] = None,
        actions: typing.Optional[typing.Union[ProviderEventAction, typing.Sequence[ProviderEventAction]]] = None,
        username: typing.Optional[str] = None,
        ip: typing.Optional[str] = None,
        object_name: typing.Optional[str] = None,
        object_types: typing.Optional[
            typing.Union[ProviderEventObjectType, typing.Sequence[ProviderEventObjectType]]
        ] = None,
        instance_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        csv_export: typing.Optional[bool] = None,
        omit_object_data: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetProviderEventsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ProviderEvent]]:
        """
        Returns an array with one or more provider events applying the specified filters. This API is only available if you configure an "eventsearcher" plugin

        Parameters
        ----------
        start_timestamp : typing.Optional[int]
            the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter

        end_timestamp : typing.Optional[int]
            the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter

        actions : typing.Optional[typing.Union[ProviderEventAction, typing.Sequence[ProviderEventAction]]]
            the event action must be included among those specified. Empty or missing means omit this filter. Actions must be specified comma separated

        username : typing.Optional[str]
            the event username must be the same as the one specified. Empty or missing means omit this filter

        ip : typing.Optional[str]
            the event IP must be the same as the one specified. Empty or missing means omit this filter

        object_name : typing.Optional[str]
            the event object name must be the same as the one specified. Empty or missing means omit this filter

        object_types : typing.Optional[typing.Union[ProviderEventObjectType, typing.Sequence[ProviderEventObjectType]]]
            the event object type must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        instance_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        from_id : typing.Optional[str]
            the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter.

        role : typing.Optional[str]
            Admin role. Empty or missing means omit this filter. Ignored if the admin has a role

        csv_export : typing.Optional[bool]
            If enabled, events are exported as a CSV file

        omit_object_data : typing.Optional[bool]
            If enabled, returned events will not contain the `object_data` field

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 1000, default is 100

        order : typing.Optional[GetProviderEventsRequestOrder]
            Ordering events by timestamp. Default DESC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ProviderEvent]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "events/provider",
            method="GET",
            params={
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
                "actions": ",".join(map(str, actions)) if isinstance(actions, (list, tuple, set)) else actions,
                "username": username,
                "ip": ip,
                "object_name": object_name,
                "object_types": ",".join(map(str, object_types))
                if isinstance(object_types, (list, tuple, set))
                else object_types,
                "instance_ids": ",".join(map(str, instance_ids))
                if isinstance(instance_ids, (list, tuple, set))
                else instance_ids,
                "from_id": from_id,
                "role": role,
                "csv_export": csv_export,
                "omit_object_data": omit_object_data,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ProviderEvent],
                    parse_obj_as(
                        type_=typing.List[ProviderEvent],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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

    async def get_log_events(
        self,
        *,
        start_timestamp: typing.Optional[int] = None,
        end_timestamp: typing.Optional[int] = None,
        events: typing.Optional[typing.Union[LogEventType, typing.Sequence[LogEventType]]] = None,
        username: typing.Optional[str] = None,
        ip: typing.Optional[str] = None,
        protocols: typing.Optional[typing.Union[EventProtocols, typing.Sequence[EventProtocols]]] = None,
        instance_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        from_id: typing.Optional[str] = None,
        role: typing.Optional[str] = None,
        csv_export: typing.Optional[bool] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetLogEventsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[LogEvent]]:
        """
        Returns an array with one or more log events applying the specified filters. This API is only available if you configure an "eventsearcher" plugin

        Parameters
        ----------
        start_timestamp : typing.Optional[int]
            the event timestamp, unix timestamp in nanoseconds, must be greater than or equal to the specified one. 0 or missing means omit this filter

        end_timestamp : typing.Optional[int]
            the event timestamp, unix timestamp in nanoseconds, must be less than or equal to the specified one. 0 or missing means omit this filter

        events : typing.Optional[typing.Union[LogEventType, typing.Sequence[LogEventType]]]
            the log events must be included among those specified. Empty or missing means omit this filter. Events must be specified comma separated

        username : typing.Optional[str]
            the event username must be the same as the one specified. Empty or missing means omit this filter

        ip : typing.Optional[str]
            the event IP must be the same as the one specified. Empty or missing means omit this filter

        protocols : typing.Optional[typing.Union[EventProtocols, typing.Sequence[EventProtocols]]]
            the event protocol must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        instance_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            the event instance id must be included among those specified. Empty or missing means omit this filter. Values must be specified comma separated

        from_id : typing.Optional[str]
            the event id to start from. This is useful for cursor based pagination. Empty or missing means omit this filter.

        role : typing.Optional[str]
            User role. Empty or missing means omit this filter. Ignored if the admin has a role

        csv_export : typing.Optional[bool]
            If enabled, events are exported as a CSV file

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 1000, default is 100

        order : typing.Optional[GetLogEventsRequestOrder]
            Ordering events by timestamp. Default DESC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[LogEvent]]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "events/logs",
            method="GET",
            params={
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
                "events": ",".join(map(str, events)) if isinstance(events, (list, tuple, set)) else events,
                "username": username,
                "ip": ip,
                "protocols": ",".join(map(str, protocols)) if isinstance(protocols, (list, tuple, set)) else protocols,
                "instance_ids": ",".join(map(str, instance_ids))
                if isinstance(instance_ids, (list, tuple, set))
                else instance_ids,
                "from_id": from_id,
                "role": role,
                "csv_export": csv_export,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[LogEvent],
                    parse_obj_as(
                        type_=typing.List[LogEvent],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiResponse,
                        parse_obj_as(
                            type_=ApiResponse,
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
