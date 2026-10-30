

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ...types.run_maintenance_request import RunMaintenanceRequest
from ...types.run_maintenance_response import RunMaintenanceResponse
from .raw_client import AsyncRawRunsClient, RawRunsClient


OMIT = typing.cast(typing.Any, ...)


class RunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRunsClient
        """
        return self._raw_client

    def create(
        self,
        namespace_id: str,
        *,
        request: RunMaintenanceRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RunMaintenanceResponse:
        """
        Runs one maintenance job for the namespace. The body's `kind` selects the job, which is one of `metadata`, `gc`, `retention`, `retention_window`, or `recover_administrator`. The response includes the same `kind` and the job's result. A deleted namespace accepts only `gc`. A `metadata` job folds the WAL tail and compacts metadata until nothing is due, or until it publishes 16 compaction units. A compaction unit can take minutes, so the call can too. When the result's `outcome` is `due`, another `metadata` run continues the work. A `gc` job reads the current manifest, lists the pins, and then sweeps every object family to the end. Each listing starts at the beginning, and the job doesn't keep a position to continue from. When the deployment maintains a grep index, the job then deletes aged, unreferenced grep index objects, and the result includes their counts in `extensions.grep`. A `retention` job advances the retention floor to the folded manifest head, or to the one target that `to_seq` or `cutoff_at_ms` sets. A `retention_window` job sets the namespace's retention window to `retention_window_ms`, or clears it when the body doesn't include that field.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request : RunMaintenanceRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunMaintenanceResponse
            Maintenance job completed

        Examples
        --------
        from fern import FernApi, RunMaintenanceRequest_Gc

        client = FernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.maintenance.runs.create(
            namespace_id="namespace_id",
            request=RunMaintenanceRequest_Gc(),
        )
        """
        _response = self._raw_client.create(namespace_id, request=request, request_options=request_options)
        return _response.data


class AsyncRunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRunsClient
        """
        return self._raw_client

    async def create(
        self,
        namespace_id: str,
        *,
        request: RunMaintenanceRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RunMaintenanceResponse:
        """
        Runs one maintenance job for the namespace. The body's `kind` selects the job, which is one of `metadata`, `gc`, `retention`, `retention_window`, or `recover_administrator`. The response includes the same `kind` and the job's result. A deleted namespace accepts only `gc`. A `metadata` job folds the WAL tail and compacts metadata until nothing is due, or until it publishes 16 compaction units. A compaction unit can take minutes, so the call can too. When the result's `outcome` is `due`, another `metadata` run continues the work. A `gc` job reads the current manifest, lists the pins, and then sweeps every object family to the end. Each listing starts at the beginning, and the job doesn't keep a position to continue from. When the deployment maintains a grep index, the job then deletes aged, unreferenced grep index objects, and the result includes their counts in `extensions.grep`. A `retention` job advances the retention floor to the folded manifest head, or to the one target that `to_seq` or `cutoff_at_ms` sets. A `retention_window` job sets the namespace's retention window to `retention_window_ms`, or clears it when the body doesn't include that field.

        Parameters
        ----------
        namespace_id : str
            The namespace ID.

        request : RunMaintenanceRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunMaintenanceResponse
            Maintenance job completed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RunMaintenanceRequest_Gc

        client = AsyncFernApi(
            actor_id="YOUR_ACTOR_ID",
            subject_id="YOUR_SUBJECT_ID",
            principal_scope="YOUR_PRINCIPAL_SCOPE",
            principals="YOUR_PRINCIPALS",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.maintenance.runs.create(
                namespace_id="namespace_id",
                request=RunMaintenanceRequest_Gc(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(namespace_id, request=request, request_options=request_options)
        return _response.data
