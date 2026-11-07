

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
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.entity_audit_events_response_dto import EntityAuditEventsResponseDto
from ..types.error_response_dto import ErrorResponseDto
from ..types.state_machine_finished_dto import StateMachineFinishedDto
from .types.search_entity_audit_events_request_event_type_item import SearchEntityAuditEventsRequestEventTypeItem
from .types.search_entity_audit_events_request_severity import SearchEntityAuditEventsRequestSeverity
from pydantic import ValidationError


class RawEntityAuditClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_entity_audit_events(
        self,
        entity_id: str,
        *,
        event_type: typing.Optional[
            typing.Union[
                SearchEntityAuditEventsRequestEventTypeItem,
                typing.Sequence[SearchEntityAuditEventsRequestEventTypeItem],
            ]
        ] = None,
        severity: typing.Optional[SearchEntityAuditEventsRequestSeverity] = None,
        from_utc_time: typing.Optional[dt.datetime] = None,
        to_utc_time: typing.Optional[dt.datetime] = None,
        transaction_id: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EntityAuditEventsResponseDto]:
        """
        Retrieves audit events for a specific entity with cursor-based pagination.
        Results are ordered by event utc time (newest first).
        Maximum search period is 180 days. Default period is 10 days when one of the boundaries is not defined.

        Parameters
        ----------
        entity_id : str
            Identifier of the entity to retrieve audit events for

        event_type : typing.Optional[typing.Union[SearchEntityAuditEventsRequestEventTypeItem, typing.Sequence[SearchEntityAuditEventsRequestEventTypeItem]]]
            Filter by specific audit event types. If not specified, defaults to all event types except System. Note: Including System events may increase latency and load on the system. Use System events filtering with caution.

        severity : typing.Optional[SearchEntityAuditEventsRequestSeverity]
            Filter by event severity level

        from_utc_time : typing.Optional[dt.datetime]
            Filter events from this timestamp (inclusive)

        to_utc_time : typing.Optional[dt.datetime]
            Filter events until this timestamp (exclusive)

        transaction_id : typing.Optional[str]
            Filter by transaction identifier

        cursor : typing.Optional[str]
            Cursor for pagination. Use the `nextCursor` value from the previous response to fetch the next page of results. Omit for the first page.

        limit : typing.Optional[str]
            Maximum number of audit events to return per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntityAuditEventsResponseDto]
            Audit events retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"audit/entity/{encode_path_param(entity_id)}",
            method="GET",
            params={
                "eventType": event_type,
                "severity": severity,
                "fromUtcTime": serialize_datetime(from_utc_time) if from_utc_time is not None else None,
                "toUtcTime": serialize_datetime(to_utc_time) if to_utc_time is not None else None,
                "transactionId": transaction_id,
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityAuditEventsResponseDto,
                    parse_obj_as(
                        type_=EntityAuditEventsResponseDto,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def get_state_machine_finished_event(
        self, entity_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StateMachineFinishedDto]:
        """
        Retrieves the StateMachine Finished event for a specific entity and transaction.
        This endpoint provides quick access to the workflow outcome for that transaction without needing to
        search through all audit events.

        Both entityId and transactionId must be valid time-based UUIDs (version 1).

        Parameters
        ----------
        entity_id : str
            Identifier of the entity. Must be a valid time-based UUID (version 1).

        transaction_id : str
            Identifier of the transaction. Must be a valid time-based UUID (version 1).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StateMachineFinishedDto]
            Workflow finished event retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"audit/entity/{encode_path_param(entity_id)}/workflow/{encode_path_param(transaction_id)}/finished",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StateMachineFinishedDto,
                    parse_obj_as(
                        type_=StateMachineFinishedDto,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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


class AsyncRawEntityAuditClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_entity_audit_events(
        self,
        entity_id: str,
        *,
        event_type: typing.Optional[
            typing.Union[
                SearchEntityAuditEventsRequestEventTypeItem,
                typing.Sequence[SearchEntityAuditEventsRequestEventTypeItem],
            ]
        ] = None,
        severity: typing.Optional[SearchEntityAuditEventsRequestSeverity] = None,
        from_utc_time: typing.Optional[dt.datetime] = None,
        to_utc_time: typing.Optional[dt.datetime] = None,
        transaction_id: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EntityAuditEventsResponseDto]:
        """
        Retrieves audit events for a specific entity with cursor-based pagination.
        Results are ordered by event utc time (newest first).
        Maximum search period is 180 days. Default period is 10 days when one of the boundaries is not defined.

        Parameters
        ----------
        entity_id : str
            Identifier of the entity to retrieve audit events for

        event_type : typing.Optional[typing.Union[SearchEntityAuditEventsRequestEventTypeItem, typing.Sequence[SearchEntityAuditEventsRequestEventTypeItem]]]
            Filter by specific audit event types. If not specified, defaults to all event types except System. Note: Including System events may increase latency and load on the system. Use System events filtering with caution.

        severity : typing.Optional[SearchEntityAuditEventsRequestSeverity]
            Filter by event severity level

        from_utc_time : typing.Optional[dt.datetime]
            Filter events from this timestamp (inclusive)

        to_utc_time : typing.Optional[dt.datetime]
            Filter events until this timestamp (exclusive)

        transaction_id : typing.Optional[str]
            Filter by transaction identifier

        cursor : typing.Optional[str]
            Cursor for pagination. Use the `nextCursor` value from the previous response to fetch the next page of results. Omit for the first page.

        limit : typing.Optional[str]
            Maximum number of audit events to return per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntityAuditEventsResponseDto]
            Audit events retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"audit/entity/{encode_path_param(entity_id)}",
            method="GET",
            params={
                "eventType": event_type,
                "severity": severity,
                "fromUtcTime": serialize_datetime(from_utc_time) if from_utc_time is not None else None,
                "toUtcTime": serialize_datetime(to_utc_time) if to_utc_time is not None else None,
                "transactionId": transaction_id,
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntityAuditEventsResponseDto,
                    parse_obj_as(
                        type_=EntityAuditEventsResponseDto,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def get_state_machine_finished_event(
        self, entity_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StateMachineFinishedDto]:
        """
        Retrieves the StateMachine Finished event for a specific entity and transaction.
        This endpoint provides quick access to the workflow outcome for that transaction without needing to
        search through all audit events.

        Both entityId and transactionId must be valid time-based UUIDs (version 1).

        Parameters
        ----------
        entity_id : str
            Identifier of the entity. Must be a valid time-based UUID (version 1).

        transaction_id : str
            Identifier of the transaction. Must be a valid time-based UUID (version 1).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StateMachineFinishedDto]
            Workflow finished event retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"audit/entity/{encode_path_param(entity_id)}/workflow/{encode_path_param(transaction_id)}/finished",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StateMachineFinishedDto,
                    parse_obj_as(
                        type_=StateMachineFinishedDto,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
