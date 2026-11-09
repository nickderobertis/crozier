

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.entity_audit_events_response_dto import EntityAuditEventsResponseDto
from ..types.state_machine_finished_dto import StateMachineFinishedDto
from .raw_client import AsyncRawEntityAuditClient, RawEntityAuditClient
from .types.search_entity_audit_events_request_event_type_item import SearchEntityAuditEventsRequestEventTypeItem
from .types.search_entity_audit_events_request_severity import SearchEntityAuditEventsRequestSeverity


class EntityAuditClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEntityAuditClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEntityAuditClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEntityAuditClient
        """
        return self._raw_client

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
    ) -> EntityAuditEventsResponseDto:
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
        EntityAuditEventsResponseDto
            Audit events retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_audit.search_entity_audit_events(
            entity_id="entityId",
        )
        """
        _response = self._raw_client.search_entity_audit_events(
            entity_id,
            event_type=event_type,
            severity=severity,
            from_utc_time=from_utc_time,
            to_utc_time=to_utc_time,
            transaction_id=transaction_id,
            cursor=cursor,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def get_state_machine_finished_event(
        self, entity_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StateMachineFinishedDto:
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
        StateMachineFinishedDto
            Workflow finished event retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.entity_audit.get_state_machine_finished_event(
            entity_id="entityId",
            transaction_id="transactionId",
        )
        """
        _response = self._raw_client.get_state_machine_finished_event(
            entity_id, transaction_id, request_options=request_options
        )
        return _response.data


class AsyncEntityAuditClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEntityAuditClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEntityAuditClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEntityAuditClient
        """
        return self._raw_client

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
    ) -> EntityAuditEventsResponseDto:
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
        EntityAuditEventsResponseDto
            Audit events retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_audit.search_entity_audit_events(
                entity_id="entityId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_entity_audit_events(
            entity_id,
            event_type=event_type,
            severity=severity,
            from_utc_time=from_utc_time,
            to_utc_time=to_utc_time,
            transaction_id=transaction_id,
            cursor=cursor,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def get_state_machine_finished_event(
        self, entity_id: str, transaction_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StateMachineFinishedDto:
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
        StateMachineFinishedDto
            Workflow finished event retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.entity_audit.get_state_machine_finished_event(
                entity_id="entityId",
                transaction_id="transactionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_state_machine_finished_event(
            entity_id, transaction_id, request_options=request_options
        )
        return _response.data
