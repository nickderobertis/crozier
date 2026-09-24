

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_permissions_response import ListPermissionsResponse
from ..types.permission_resource_type import PermissionResourceType
from .raw_client import AsyncRawInternalClient, RawInternalClient

if typing.TYPE_CHECKING:
    from .agents.client import AgentsClient, AsyncAgentsClient
    from .metrics.client import AsyncMetricsClient, MetricsClient
    from .schedules.client import AsyncSchedulesClient, SchedulesClient
    from .sessions.client import AsyncSessionsClient, SessionsClient

OMIT = typing.cast(typing.Any, ...)


class InternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._metrics: typing.Optional[MetricsClient] = None
        self._schedules: typing.Optional[SchedulesClient] = None
        self._sessions: typing.Optional[SessionsClient] = None
        self._agents: typing.Optional[AgentsClient] = None

    @property
    def with_raw_response(self) -> RawInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalClient
        """
        return self._raw_client

    def list_permissions(
        self,
        *,
        resource_ids: typing.Sequence[str],
        resource_type: PermissionResourceType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPermissionsResponse:
        """
        Return granted actions for the requested resources.

        Parameters
        ----------
        resource_ids : typing.Sequence[str]
            Resource ids of `resource_type` to evaluate.

        resource_type : PermissionResourceType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPermissionsResponse
            Permissions envelope: `{ type, permissions }`.

        Examples
        --------
        from fern import FernApi, PermissionResourceType

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.internal.list_permissions(
            resource_ids=["resource_ids"],
            resource_type=PermissionResourceType.AGENT,
        )
        """
        _response = self._raw_client.list_permissions(
            resource_ids=resource_ids, resource_type=resource_type, request_options=request_options
        )
        return _response.data

    @property
    def metrics(self):
        if self._metrics is None:
            from .metrics.client import MetricsClient

            self._metrics = MetricsClient(client_wrapper=self._client_wrapper)
        return self._metrics

    @property
    def schedules(self):
        if self._schedules is None:
            from .schedules.client import SchedulesClient

            self._schedules = SchedulesClient(client_wrapper=self._client_wrapper)
        return self._schedules

    @property
    def sessions(self):
        if self._sessions is None:
            from .sessions.client import SessionsClient

            self._sessions = SessionsClient(client_wrapper=self._client_wrapper)
        return self._sessions

    @property
    def agents(self):
        if self._agents is None:
            from .agents.client import AgentsClient

            self._agents = AgentsClient(client_wrapper=self._client_wrapper)
        return self._agents


class AsyncInternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._metrics: typing.Optional[AsyncMetricsClient] = None
        self._schedules: typing.Optional[AsyncSchedulesClient] = None
        self._sessions: typing.Optional[AsyncSessionsClient] = None
        self._agents: typing.Optional[AsyncAgentsClient] = None

    @property
    def with_raw_response(self) -> AsyncRawInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalClient
        """
        return self._raw_client

    async def list_permissions(
        self,
        *,
        resource_ids: typing.Sequence[str],
        resource_type: PermissionResourceType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListPermissionsResponse:
        """
        Return granted actions for the requested resources.

        Parameters
        ----------
        resource_ids : typing.Sequence[str]
            Resource ids of `resource_type` to evaluate.

        resource_type : PermissionResourceType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPermissionsResponse
            Permissions envelope: `{ type, permissions }`.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PermissionResourceType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.internal.list_permissions(
                resource_ids=["resource_ids"],
                resource_type=PermissionResourceType.AGENT,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_permissions(
            resource_ids=resource_ids, resource_type=resource_type, request_options=request_options
        )
        return _response.data

    @property
    def metrics(self):
        if self._metrics is None:
            from .metrics.client import AsyncMetricsClient

            self._metrics = AsyncMetricsClient(client_wrapper=self._client_wrapper)
        return self._metrics

    @property
    def schedules(self):
        if self._schedules is None:
            from .schedules.client import AsyncSchedulesClient

            self._schedules = AsyncSchedulesClient(client_wrapper=self._client_wrapper)
        return self._schedules

    @property
    def sessions(self):
        if self._sessions is None:
            from .sessions.client import AsyncSessionsClient

            self._sessions = AsyncSessionsClient(client_wrapper=self._client_wrapper)
        return self._sessions

    @property
    def agents(self):
        if self._agents is None:
            from .agents.client import AsyncAgentsClient

            self._agents = AsyncAgentsClient(client_wrapper=self._client_wrapper)
        return self._agents
