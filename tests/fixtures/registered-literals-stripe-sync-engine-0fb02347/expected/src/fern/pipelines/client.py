

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.destination_config import DestinationConfig
from ..types.eof_payload import EofPayload
from ..types.pipeline import Pipeline
from ..types.source_config import SourceConfig
from ..types.sync_state import SyncState
from .raw_client import AsyncRawPipelinesClient, RawPipelinesClient
from .types.pipelines_check_request_only import PipelinesCheckRequestOnly
from .types.pipelines_create_request_streams_item import PipelinesCreateRequestStreamsItem
from .types.pipelines_delete_response import PipelinesDeleteResponse
from .types.pipelines_list_response import PipelinesListResponse
from .types.pipelines_setup_request_only import PipelinesSetupRequestOnly
from .types.pipelines_sync_batch_request_streams_item import PipelinesSyncBatchRequestStreamsItem
from .types.pipelines_sync_request_streams_item import PipelinesSyncRequestStreamsItem
from .types.pipelines_sync_workflow_test_response import PipelinesSyncWorkflowTestResponse
from .types.pipelines_teardown_request_only import PipelinesTeardownRequestOnly
from .types.pipelines_update_request_desired_status import PipelinesUpdateRequestDesiredStatus
from .types.pipelines_update_request_streams_item import PipelinesUpdateRequestStreamsItem


OMIT = typing.cast(typing.Any, ...)


class PipelinesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPipelinesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPipelinesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPipelinesClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> PipelinesListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesListResponse
            List of pipelines

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        source: SourceConfig,
        destination: DestinationConfig,
        skip_check: typing.Optional[bool] = None,
        id: typing.Optional[str] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesCreateRequestStreamsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pipeline:
        """
        Parameters
        ----------
        source : SourceConfig

        destination : DestinationConfig

        skip_check : typing.Optional[bool]
            Skip connector validation checks

        id : typing.Optional[str]
            Optional pipeline identifier. If omitted, the service generates one (e.g. pipe_abc123).

        streams : typing.Optional[typing.Sequence[PipelinesCreateRequestStreamsItem]]
            Selected streams to sync. All streams synced if omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pipeline
            Created pipeline

        Examples
        --------
        from fern import (
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            FernApi,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.create(
            source=SourceConfig_Stripe(
                stripe=SourceStripeConfig(
                    api_key="api_key",
                ),
            ),
            destination=DestinationConfig_Postgres(
                postgres=DestinationPostgresConfig(),
            ),
        )
        """
        _response = self._raw_client.create(
            source=source,
            destination=destination,
            skip_check=skip_check,
            id=id,
            streams=streams,
            request_options=request_options,
        )
        return _response.data

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Pipeline:
        """
        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pipeline
            Retrieved pipeline with status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.get(
            id="pipe_abc123",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> PipelinesDeleteResponse:
        """
        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesDeleteResponse
            Deleted pipeline

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.delete(
            id="pipe_abc123",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def update(
        self,
        id_path_param: str,
        *,
        id: typing.Optional[str] = OMIT,
        source: typing.Optional[SourceConfig] = OMIT,
        destination: typing.Optional[DestinationConfig] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesUpdateRequestStreamsItem]] = OMIT,
        desired_status: typing.Optional[PipelinesUpdateRequestDesiredStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pipeline:
        """
        Parameters
        ----------
        id_path_param : str
            Unique pipeline identifier (e.g. pipe_abc123).

        id : typing.Optional[str]
            Optional pipeline identifier. If omitted, the service generates one (e.g. pipe_abc123).

        source : typing.Optional[SourceConfig]

        destination : typing.Optional[DestinationConfig]

        streams : typing.Optional[typing.Sequence[PipelinesUpdateRequestStreamsItem]]
            Selected streams to sync. All streams synced if omitted.

        desired_status : typing.Optional[PipelinesUpdateRequestDesiredStatus]
            Set to "paused" to pause, "active" to resume, "deleted" to tear down.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pipeline
            Updated pipeline

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.update(
            id_path_param="pipe_abc123",
        )
        """
        _response = self._raw_client.update(
            id_path_param,
            id=id,
            source=source,
            destination=destination,
            streams=streams,
            desired_status=desired_status,
            request_options=request_options,
        )
        return _response.data

    def sync(
        self,
        id: str,
        *,
        time_limit: typing.Optional[float] = None,
        run_id: typing.Optional[str] = None,
        reset_state: typing.Optional[bool] = None,
        source: typing.Optional[SourceConfig] = OMIT,
        destination: typing.Optional[DestinationConfig] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesSyncRequestStreamsItem]] = OMIT,
        sync_state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Triggers an ad-hoc sync run for the pipeline and streams NDJSON messages (records, state, progress, eof) back to the client. Persists the ending sync_state on the pipeline so the next run resumes where this one left off.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        time_limit : typing.Optional[float]
            Stop after N seconds

        run_id : typing.Optional[str]
            Sync run identifier (resumes or starts fresh)

        reset_state : typing.Optional[bool]
            Ignore persisted sync state and start fresh (ending state is still saved)

        source : typing.Optional[SourceConfig]

        destination : typing.Optional[DestinationConfig]

        streams : typing.Optional[typing.Sequence[PipelinesSyncRequestStreamsItem]]

        sync_state : typing.Optional[SyncState]
            Explicit sync checkpoint override for resumed ad-hoc runs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Streaming NDJSON sync output

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.sync(
            id="pipe_abc123",
        )
        """
        _response = self._raw_client.sync(
            id,
            time_limit=time_limit,
            run_id=run_id,
            reset_state=reset_state,
            source=source,
            destination=destination,
            streams=streams,
            sync_state=sync_state,
            request_options=request_options,
        )
        return _response.data

    def sync_batch(
        self,
        id: str,
        *,
        state_limit: typing.Optional[int] = None,
        run_id: typing.Optional[str] = None,
        reset_state: typing.Optional[bool] = None,
        source: typing.Optional[SourceConfig] = OMIT,
        destination: typing.Optional[DestinationConfig] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesSyncBatchRequestStreamsItem]] = OMIT,
        sync_state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EofPayload:
        """
        Runs the full sync pipeline and returns the final EofPayload as a single JSON response. Persists the ending sync_state on the pipeline so the next run resumes where this one left off.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        state_limit : typing.Optional[int]
            Stop after N source_state messages

        run_id : typing.Optional[str]
            Sync run identifier (resumes or starts fresh)

        reset_state : typing.Optional[bool]
            Ignore persisted sync state and start fresh (ending state is still saved)

        source : typing.Optional[SourceConfig]

        destination : typing.Optional[DestinationConfig]

        streams : typing.Optional[typing.Sequence[PipelinesSyncBatchRequestStreamsItem]]

        sync_state : typing.Optional[SyncState]
            Explicit sync checkpoint override for resumed ad-hoc runs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EofPayload
            Sync result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.sync_batch(
            id="pipe_abc123",
        )
        """
        _response = self._raw_client.sync_batch(
            id,
            state_limit=state_limit,
            run_id=run_id,
            reset_state=reset_state,
            source=source,
            destination=destination,
            streams=streams,
            sync_state=sync_state,
            request_options=request_options,
        )
        return _response.data

    def check(
        self,
        id: str,
        *,
        only: typing.Optional[PipelinesCheckRequestOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Runs the `check()` method on source and/or destination connectors and streams back NDJSON messages (connection_status, log, trace). Pass ?only=source or ?only=destination to check a single side.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        only : typing.Optional[PipelinesCheckRequestOnly]
            Run only the source or destination side

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Streaming NDJSON check output

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.check(
            id="pipe_abc123",
        )
        """
        _response = self._raw_client.check(id, only=only, request_options=request_options)
        return _response.data

    def setup(
        self,
        id: str,
        *,
        only: typing.Optional[PipelinesSetupRequestOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Runs the `setup()` method on source and/or destination connectors (e.g. creating destination tables). Streams NDJSON messages (control, log, trace). Pass ?only=source or ?only=destination to run a single side.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        only : typing.Optional[PipelinesSetupRequestOnly]
            Run only the source or destination side

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Streaming NDJSON setup output

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.setup(
            id="pipe_abc123",
        )
        """
        _response = self._raw_client.setup(id, only=only, request_options=request_options)
        return _response.data

    def teardown(
        self,
        id: str,
        *,
        only: typing.Optional[PipelinesTeardownRequestOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Runs the `teardown()` method on source and/or destination connectors (e.g. dropping destination tables). Streams NDJSON messages (log, trace). Pass ?only=source or ?only=destination to run a single side.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        only : typing.Optional[PipelinesTeardownRequestOnly]
            Run only the source or destination side

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Streaming NDJSON teardown output

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.teardown(
            id="pipe_abc123",
        )
        """
        _response = self._raw_client.teardown(id, only=only, request_options=request_options)
        return _response.data

    def simulate_webhook_sync(
        self,
        id: str,
        *,
        created_after: typing.Optional[float] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Fetches events from /v1/events using the pipeline's Stripe API key, then pipes them as input into the sync engine's push mode. This exercises the same code path as real webhooks without needing webhook delivery.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        created_after : typing.Optional[float]
            Only fetch events created after this Unix timestamp (default: 24 hours ago)

        limit : typing.Optional[int]
            Max events to fetch (default: all)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Streaming NDJSON sync output

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.simulate_webhook_sync(
            id="pipe_abc123",
        )
        """
        _response = self._raw_client.simulate_webhook_sync(
            id, created_after=created_after, limit=limit, request_options=request_options
        )
        return _response.data

    def sync_workflow_test(
        self,
        id: str,
        *,
        time_limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelinesSyncWorkflowTestResponse:
        """
        Exercises the same backfill loop code that the Temporal workflow uses, but runs inline without a Temporal server. Useful for testing the full workflow logic end-to-end.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        time_limit : typing.Optional[float]
            Time limit per iteration (seconds)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesSyncWorkflowTestResponse
            Backfill result with final eof and sync state

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pipelines.sync_workflow_test(
            id="pipe_abc123",
        )
        """
        _response = self._raw_client.sync_workflow_test(id, time_limit=time_limit, request_options=request_options)
        return _response.data


class AsyncPipelinesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPipelinesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPipelinesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPipelinesClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> PipelinesListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesListResponse
            List of pipelines

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipelines.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        source: SourceConfig,
        destination: DestinationConfig,
        skip_check: typing.Optional[bool] = None,
        id: typing.Optional[str] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesCreateRequestStreamsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pipeline:
        """
        Parameters
        ----------
        source : SourceConfig

        destination : DestinationConfig

        skip_check : typing.Optional[bool]
            Skip connector validation checks

        id : typing.Optional[str]
            Optional pipeline identifier. If omitted, the service generates one (e.g. pipe_abc123).

        streams : typing.Optional[typing.Sequence[PipelinesCreateRequestStreamsItem]]
            Selected streams to sync. All streams synced if omitted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pipeline
            Created pipeline

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipelines.create(
                source=SourceConfig_Stripe(
                    stripe=SourceStripeConfig(
                        api_key="api_key",
                    ),
                ),
                destination=DestinationConfig_Postgres(
                    postgres=DestinationPostgresConfig(),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            source=source,
            destination=destination,
            skip_check=skip_check,
            id=id,
            streams=streams,
            request_options=request_options,
        )
        return _response.data

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Pipeline:
        """
        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pipeline
            Retrieved pipeline with status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipelines.get(
                id="pipe_abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def delete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PipelinesDeleteResponse:
        """
        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesDeleteResponse
            Deleted pipeline

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipelines.delete(
                id="pipe_abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data

    async def update(
        self,
        id_path_param: str,
        *,
        id: typing.Optional[str] = OMIT,
        source: typing.Optional[SourceConfig] = OMIT,
        destination: typing.Optional[DestinationConfig] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesUpdateRequestStreamsItem]] = OMIT,
        desired_status: typing.Optional[PipelinesUpdateRequestDesiredStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Pipeline:
        """
        Parameters
        ----------
        id_path_param : str
            Unique pipeline identifier (e.g. pipe_abc123).

        id : typing.Optional[str]
            Optional pipeline identifier. If omitted, the service generates one (e.g. pipe_abc123).

        source : typing.Optional[SourceConfig]

        destination : typing.Optional[DestinationConfig]

        streams : typing.Optional[typing.Sequence[PipelinesUpdateRequestStreamsItem]]
            Selected streams to sync. All streams synced if omitted.

        desired_status : typing.Optional[PipelinesUpdateRequestDesiredStatus]
            Set to "paused" to pause, "active" to resume, "deleted" to tear down.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Pipeline
            Updated pipeline

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipelines.update(
                id_path_param="pipe_abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id_path_param,
            id=id,
            source=source,
            destination=destination,
            streams=streams,
            desired_status=desired_status,
            request_options=request_options,
        )
        return _response.data

    async def sync(
        self,
        id: str,
        *,
        time_limit: typing.Optional[float] = None,
        run_id: typing.Optional[str] = None,
        reset_state: typing.Optional[bool] = None,
        source: typing.Optional[SourceConfig] = OMIT,
        destination: typing.Optional[DestinationConfig] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesSyncRequestStreamsItem]] = OMIT,
        sync_state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Triggers an ad-hoc sync run for the pipeline and streams NDJSON messages (records, state, progress, eof) back to the client. Persists the ending sync_state on the pipeline so the next run resumes where this one left off.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        time_limit : typing.Optional[float]
            Stop after N seconds

        run_id : typing.Optional[str]
            Sync run identifier (resumes or starts fresh)

        reset_state : typing.Optional[bool]
            Ignore persisted sync state and start fresh (ending state is still saved)

        source : typing.Optional[SourceConfig]

        destination : typing.Optional[DestinationConfig]

        streams : typing.Optional[typing.Sequence[PipelinesSyncRequestStreamsItem]]

        sync_state : typing.Optional[SyncState]
            Explicit sync checkpoint override for resumed ad-hoc runs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Streaming NDJSON sync output

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipelines.sync(
                id="pipe_abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sync(
            id,
            time_limit=time_limit,
            run_id=run_id,
            reset_state=reset_state,
            source=source,
            destination=destination,
            streams=streams,
            sync_state=sync_state,
            request_options=request_options,
        )
        return _response.data

    async def sync_batch(
        self,
        id: str,
        *,
        state_limit: typing.Optional[int] = None,
        run_id: typing.Optional[str] = None,
        reset_state: typing.Optional[bool] = None,
        source: typing.Optional[SourceConfig] = OMIT,
        destination: typing.Optional[DestinationConfig] = OMIT,
        streams: typing.Optional[typing.Sequence[PipelinesSyncBatchRequestStreamsItem]] = OMIT,
        sync_state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EofPayload:
        """
        Runs the full sync pipeline and returns the final EofPayload as a single JSON response. Persists the ending sync_state on the pipeline so the next run resumes where this one left off.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        state_limit : typing.Optional[int]
            Stop after N source_state messages

        run_id : typing.Optional[str]
            Sync run identifier (resumes or starts fresh)

        reset_state : typing.Optional[bool]
            Ignore persisted sync state and start fresh (ending state is still saved)

        source : typing.Optional[SourceConfig]

        destination : typing.Optional[DestinationConfig]

        streams : typing.Optional[typing.Sequence[PipelinesSyncBatchRequestStreamsItem]]

        sync_state : typing.Optional[SyncState]
            Explicit sync checkpoint override for resumed ad-hoc runs

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EofPayload
            Sync result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipelines.sync_batch(
                id="pipe_abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sync_batch(
            id,
            state_limit=state_limit,
            run_id=run_id,
            reset_state=reset_state,
            source=source,
            destination=destination,
            streams=streams,
            sync_state=sync_state,
            request_options=request_options,
        )
        return _response.data

    async def check(
        self,
        id: str,
        *,
        only: typing.Optional[PipelinesCheckRequestOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Runs the `check()` method on source and/or destination connectors and streams back NDJSON messages (connection_status, log, trace). Pass ?only=source or ?only=destination to check a single side.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        only : typing.Optional[PipelinesCheckRequestOnly]
            Run only the source or destination side

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Streaming NDJSON check output

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipelines.check(
                id="pipe_abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check(id, only=only, request_options=request_options)
        return _response.data

    async def setup(
        self,
        id: str,
        *,
        only: typing.Optional[PipelinesSetupRequestOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Runs the `setup()` method on source and/or destination connectors (e.g. creating destination tables). Streams NDJSON messages (control, log, trace). Pass ?only=source or ?only=destination to run a single side.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        only : typing.Optional[PipelinesSetupRequestOnly]
            Run only the source or destination side

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Streaming NDJSON setup output

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipelines.setup(
                id="pipe_abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.setup(id, only=only, request_options=request_options)
        return _response.data

    async def teardown(
        self,
        id: str,
        *,
        only: typing.Optional[PipelinesTeardownRequestOnly] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Runs the `teardown()` method on source and/or destination connectors (e.g. dropping destination tables). Streams NDJSON messages (log, trace). Pass ?only=source or ?only=destination to run a single side.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        only : typing.Optional[PipelinesTeardownRequestOnly]
            Run only the source or destination side

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Streaming NDJSON teardown output

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipelines.teardown(
                id="pipe_abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.teardown(id, only=only, request_options=request_options)
        return _response.data

    async def simulate_webhook_sync(
        self,
        id: str,
        *,
        created_after: typing.Optional[float] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Fetches events from /v1/events using the pipeline's Stripe API key, then pipes them as input into the sync engine's push mode. This exercises the same code path as real webhooks without needing webhook delivery.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        created_after : typing.Optional[float]
            Only fetch events created after this Unix timestamp (default: 24 hours ago)

        limit : typing.Optional[int]
            Max events to fetch (default: all)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Streaming NDJSON sync output

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipelines.simulate_webhook_sync(
                id="pipe_abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.simulate_webhook_sync(
            id, created_after=created_after, limit=limit, request_options=request_options
        )
        return _response.data

    async def sync_workflow_test(
        self,
        id: str,
        *,
        time_limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PipelinesSyncWorkflowTestResponse:
        """
        Exercises the same backfill loop code that the Temporal workflow uses, but runs inline without a Temporal server. Useful for testing the full workflow logic end-to-end.

        Parameters
        ----------
        id : str
            Unique pipeline identifier (e.g. pipe_abc123).

        time_limit : typing.Optional[float]
            Time limit per iteration (seconds)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PipelinesSyncWorkflowTestResponse
            Backfill result with final eof and sync state

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pipelines.sync_workflow_test(
                id="pipe_abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sync_workflow_test(
            id, time_limit=time_limit, request_options=request_options
        )
        return _response.data
