

import datetime as dt
import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from .raw_client import AsyncRawAuditLogsClient, RawAuditLogsClient
from .types.get_workspace_audit_logs_audit_logs_request_event_type import GetWorkspaceAuditLogsAuditLogsRequestEventType
from .types.get_workspace_audit_logs_audit_logs_request_sort_order import GetWorkspaceAuditLogsAuditLogsRequestSortOrder
from .types.get_workspace_audit_logs_audit_logs_response import GetWorkspaceAuditLogsAuditLogsResponse


class AuditLogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAuditLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAuditLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAuditLogsClient
        """
        return self._raw_client

    def get_workspace_audit_logs(
        self,
        workspace_id_or_slug: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort_order: typing.Optional[GetWorkspaceAuditLogsAuditLogsRequestSortOrder] = None,
        event_type: typing.Optional[GetWorkspaceAuditLogsAuditLogsRequestEventType] = None,
        from_: typing.Optional[dt.datetime] = None,
        to: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetWorkspaceAuditLogsAuditLogsResponse:
        """
        Get audit logs for a workspace.

        <Warning title="Enterprise & workspace API token only">This endpoint requires an Enterprise workspace and a workspace token with the `workspace_activity:read` scope. Create a workspace token from your workspace dashboard integrations page to use this endpoint.</Warning>

        Required scope | `workspace_activity:read`

        Parameters
        ----------
        workspace_id_or_slug : str
            Unique identifier or slug for a Workspace

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        sort_order : typing.Optional[GetWorkspaceAuditLogsAuditLogsRequestSortOrder]
            Sorts the results by asc or desc

        event_type : typing.Optional[GetWorkspaceAuditLogsAuditLogsRequestEventType]
            The event type to filter by

        from_ : typing.Optional[dt.datetime]
            The start date to filter by

        to : typing.Optional[dt.datetime]
            The end date to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWorkspaceAuditLogsAuditLogsResponse
            A list of workspace audit logs

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.workspaces.audit_logs.get_workspace_audit_logs(
            workspace_id_or_slug="hitchhikers-workspace",
            from_=datetime.datetime.fromisoformat(
                "2025-06-22 16:00:31+00:00",
            ),
            to=datetime.datetime.fromisoformat(
                "2025-07-22 16:00:31+00:00",
            ),
        )
        """
        _response = self._raw_client.get_workspace_audit_logs(
            workspace_id_or_slug,
            limit=limit,
            offset=offset,
            sort_order=sort_order,
            event_type=event_type,
            from_=from_,
            to=to,
            request_options=request_options,
        )
        return _response.data


class AsyncAuditLogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAuditLogsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAuditLogsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAuditLogsClient
        """
        return self._raw_client

    async def get_workspace_audit_logs(
        self,
        workspace_id_or_slug: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        sort_order: typing.Optional[GetWorkspaceAuditLogsAuditLogsRequestSortOrder] = None,
        event_type: typing.Optional[GetWorkspaceAuditLogsAuditLogsRequestEventType] = None,
        from_: typing.Optional[dt.datetime] = None,
        to: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetWorkspaceAuditLogsAuditLogsResponse:
        """
        Get audit logs for a workspace.

        <Warning title="Enterprise & workspace API token only">This endpoint requires an Enterprise workspace and a workspace token with the `workspace_activity:read` scope. Create a workspace token from your workspace dashboard integrations page to use this endpoint.</Warning>

        Required scope | `workspace_activity:read`

        Parameters
        ----------
        workspace_id_or_slug : str
            Unique identifier or slug for a Workspace

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        sort_order : typing.Optional[GetWorkspaceAuditLogsAuditLogsRequestSortOrder]
            Sorts the results by asc or desc

        event_type : typing.Optional[GetWorkspaceAuditLogsAuditLogsRequestEventType]
            The event type to filter by

        from_ : typing.Optional[dt.datetime]
            The start date to filter by

        to : typing.Optional[dt.datetime]
            The end date to filter by

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWorkspaceAuditLogsAuditLogsResponse
            A list of workspace audit logs

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.workspaces.audit_logs.get_workspace_audit_logs(
                workspace_id_or_slug="hitchhikers-workspace",
                from_=datetime.datetime.fromisoformat(
                    "2025-06-22 16:00:31+00:00",
                ),
                to=datetime.datetime.fromisoformat(
                    "2025-07-22 16:00:31+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_workspace_audit_logs(
            workspace_id_or_slug,
            limit=limit,
            offset=offset,
            sort_order=sort_order,
            event_type=event_type,
            from_=from_,
            to=to,
            request_options=request_options,
        )
        return _response.data
