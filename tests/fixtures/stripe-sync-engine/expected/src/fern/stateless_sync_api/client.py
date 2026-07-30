

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.check_output import CheckOutput
from ..types.destination_output import DestinationOutput
from ..types.discover_output import DiscoverOutput
from ..types.eof_payload import EofPayload
from ..types.message import Message
from ..types.pipeline_config import PipelineConfig
from ..types.setup_output import SetupOutput
from ..types.sync_output import SyncOutput
from ..types.sync_state import SyncState
from ..types.teardown_output import TeardownOutput
from .raw_client import AsyncRawStatelessSyncApiClient, RawStatelessSyncApiClient
from .types.pipeline_check_request_only import PipelineCheckRequestOnly
from .types.pipeline_setup_request_only import PipelineSetupRequestOnly
from .types.pipeline_teardown_request_only import PipelineTeardownRequestOnly
from .types.source_discover_request_source import SourceDiscoverRequestSource


OMIT = typing.cast(typing.Any, ...)


class StatelessSyncApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatelessSyncApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatelessSyncApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatelessSyncApiClient
        """
        return self._raw_client

    def pipeline_check(
        self,
        *,
        pipeline: PipelineConfig,
        only: typing.Optional[PipelineCheckRequestOnly] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckOutput:
        """
        Validates the source/destination config and tests connectivity. Streams NDJSON messages (connection_status, log, trace) tagged with _emitted_by. Pass only=source or only=destination to check a single side.

        Parameters
        ----------
        pipeline : PipelineConfig

        only : typing.Optional[PipelineCheckRequestOnly]
            Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckOutput
            NDJSON stream of check messages

        Examples
        --------
        from fern import (
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            FernApi,
            PipelineConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stateless_sync_api.pipeline_check(
            pipeline=PipelineConfig(
                source=SourceConfig_Stripe(
                    stripe=SourceStripeConfig(
                        api_key="api_key",
                    ),
                ),
                destination=DestinationConfig_Postgres(
                    postgres=DestinationPostgresConfig(),
                ),
            ),
        )
        """
        _response = self._raw_client.pipeline_check(pipeline=pipeline, only=only, request_options=request_options)
        return _response.data

    def pipeline_setup(
        self,
        *,
        pipeline: PipelineConfig,
        only: typing.Optional[PipelineSetupRequestOnly] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SetupOutput:
        """
        Creates destination tables and applies migrations. Streams NDJSON messages (control, log, trace) tagged with _emitted_by. Pass only=destination to run destination setup alone (e.g. optimistic table creation) or only=source to isolate the source.

        Parameters
        ----------
        pipeline : PipelineConfig

        only : typing.Optional[PipelineSetupRequestOnly]
            Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetupOutput
            NDJSON stream of setup messages

        Examples
        --------
        from fern import (
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            FernApi,
            PipelineConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stateless_sync_api.pipeline_setup(
            pipeline=PipelineConfig(
                source=SourceConfig_Stripe(
                    stripe=SourceStripeConfig(
                        api_key="api_key",
                    ),
                ),
                destination=DestinationConfig_Postgres(
                    postgres=DestinationPostgresConfig(),
                ),
            ),
        )
        """
        _response = self._raw_client.pipeline_setup(pipeline=pipeline, only=only, request_options=request_options)
        return _response.data

    def pipeline_teardown(
        self,
        *,
        pipeline: PipelineConfig,
        only: typing.Optional[PipelineTeardownRequestOnly] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TeardownOutput:
        """
        Drops destination tables. Streams NDJSON messages (log, trace) tagged with _emitted_by. Pass only=destination or only=source to run a single side.

        Parameters
        ----------
        pipeline : PipelineConfig

        only : typing.Optional[PipelineTeardownRequestOnly]
            Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeardownOutput
            NDJSON stream of teardown messages

        Examples
        --------
        from fern import (
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            FernApi,
            PipelineConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stateless_sync_api.pipeline_teardown(
            pipeline=PipelineConfig(
                source=SourceConfig_Stripe(
                    stripe=SourceStripeConfig(
                        api_key="api_key",
                    ),
                ),
                destination=DestinationConfig_Postgres(
                    postgres=DestinationPostgresConfig(),
                ),
            ),
        )
        """
        _response = self._raw_client.pipeline_teardown(pipeline=pipeline, only=only, request_options=request_options)
        return _response.data

    def source_discover(
        self, *, source: SourceDiscoverRequestSource, request_options: typing.Optional[RequestOptions] = None
    ) -> DiscoverOutput:
        """
        Streams NDJSON messages (catalog, logs, traces) for the configured source.

        Parameters
        ----------
        source : SourceDiscoverRequestSource
            Source config ({ type, ...config })

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DiscoverOutput
            NDJSON stream of discover messages

        Examples
        --------
        from fern.stateless_sync_api import SourceDiscoverRequestSource

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stateless_sync_api.source_discover(
            source=SourceDiscoverRequestSource(
                type="type",
            ),
        )
        """
        _response = self._raw_client.source_discover(source=source, request_options=request_options)
        return _response.data

    def pipeline_read(
        self,
        *,
        pipeline: PipelineConfig,
        time_limit: typing.Optional[float] = OMIT,
        soft_time_limit: typing.Optional[float] = OMIT,
        run_id: typing.Optional[str] = OMIT,
        stdin: typing.Optional[typing.Sequence[Message]] = OMIT,
        state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Message:
        """
        Streams NDJSON messages (records, state, catalog).

        Parameters
        ----------
        pipeline : PipelineConfig

        time_limit : typing.Optional[float]
            Stop streaming after N seconds.

        soft_time_limit : typing.Optional[float]
            Soft wall-clock deadline in seconds. Stops reading from the source between messages; the destination continues to drain and flush until time_limit fires.

        run_id : typing.Optional[str]
            Optional sync run identifier used to track bounded sync progress.

        stdin : typing.Optional[typing.Sequence[Message]]
            Optional array of input messages (push mode). Without stdin, reads from the source connector (backfill mode).

        state : typing.Optional[SyncState]
            SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Message
            NDJSON stream of sync messages

        Examples
        --------
        from fern import (
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            FernApi,
            PipelineConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stateless_sync_api.pipeline_read(
            pipeline=PipelineConfig(
                source=SourceConfig_Stripe(
                    stripe=SourceStripeConfig(
                        api_key="api_key",
                    ),
                ),
                destination=DestinationConfig_Postgres(
                    postgres=DestinationPostgresConfig(),
                ),
            ),
        )
        """
        _response = self._raw_client.pipeline_read(
            pipeline=pipeline,
            time_limit=time_limit,
            soft_time_limit=soft_time_limit,
            run_id=run_id,
            stdin=stdin,
            state=state,
            request_options=request_options,
        )
        return _response.data

    def pipeline_write(
        self,
        *,
        pipeline: PipelineConfig,
        stdin: typing.Sequence[Message],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationOutput:
        """
        Writes messages to the destination. Pass an array of messages in the request body.

        Parameters
        ----------
        pipeline : PipelineConfig

        stdin : typing.Sequence[Message]
            Array of messages to write to the destination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationOutput
            NDJSON stream of write result messages

        Examples
        --------
        import datetime

        from fern import (
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            FernApi,
            Message_Record,
            PipelineConfig,
            RecordMessageRecord,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stateless_sync_api.pipeline_write(
            pipeline=PipelineConfig(
                source=SourceConfig_Stripe(
                    stripe=SourceStripeConfig(
                        api_key="api_key",
                    ),
                ),
                destination=DestinationConfig_Postgres(
                    postgres=DestinationPostgresConfig(),
                ),
            ),
            stdin=[
                Message_Record(
                    record=RecordMessageRecord(
                        stream="stream",
                        data={"key": "value"},
                        emitted_at=datetime.datetime.fromisoformat(
                            "2024-01-15 09:30:00+00:00",
                        ),
                    ),
                )
            ],
        )
        """
        _response = self._raw_client.pipeline_write(pipeline=pipeline, stdin=stdin, request_options=request_options)
        return _response.data

    def pipeline_sync(
        self,
        *,
        pipeline: PipelineConfig,
        time_limit: typing.Optional[float] = OMIT,
        soft_time_limit: typing.Optional[float] = OMIT,
        run_id: typing.Optional[str] = OMIT,
        stdin: typing.Optional[typing.Sequence[Message]] = OMIT,
        state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncOutput:
        """
        Reads from the source connector and writes to the destination (backfill mode).

        Parameters
        ----------
        pipeline : PipelineConfig

        time_limit : typing.Optional[float]
            Stop streaming after N seconds.

        soft_time_limit : typing.Optional[float]
            Soft wall-clock deadline in seconds. Stops reading from the source between messages; the destination continues to drain and flush until time_limit fires.

        run_id : typing.Optional[str]
            Optional sync run identifier used to track bounded sync progress.

        stdin : typing.Optional[typing.Sequence[Message]]
            Optional array of input messages (push mode). Without stdin, reads from the source connector (backfill mode).

        state : typing.Optional[SyncState]
            SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncOutput
            NDJSON stream of sync messages

        Examples
        --------
        from fern import (
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            FernApi,
            PipelineConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stateless_sync_api.pipeline_sync(
            pipeline=PipelineConfig(
                source=SourceConfig_Stripe(
                    stripe=SourceStripeConfig(
                        api_key="api_key",
                    ),
                ),
                destination=DestinationConfig_Postgres(
                    postgres=DestinationPostgresConfig(),
                ),
            ),
        )
        """
        _response = self._raw_client.pipeline_sync(
            pipeline=pipeline,
            time_limit=time_limit,
            soft_time_limit=soft_time_limit,
            run_id=run_id,
            stdin=stdin,
            state=state,
            request_options=request_options,
        )
        return _response.data

    def pipeline_sync_batch(
        self,
        *,
        pipeline: PipelineConfig,
        run_id: typing.Optional[str] = OMIT,
        state_limit: typing.Optional[int] = OMIT,
        state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EofPayload:
        """
        Runs the full read → write pipeline and returns the final EofPayload as a single JSON response.

        Parameters
        ----------
        pipeline : PipelineConfig

        run_id : typing.Optional[str]
            Optional sync run identifier used to track bounded sync progress.

        state_limit : typing.Optional[int]
            Stop after yielding N source_state messages, inclusive.

        state : typing.Optional[SyncState]
            SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EofPayload
            Sync result

        Examples
        --------
        from fern import (
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            FernApi,
            PipelineConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stateless_sync_api.pipeline_sync_batch(
            pipeline=PipelineConfig(
                source=SourceConfig_Stripe(
                    stripe=SourceStripeConfig(
                        api_key="api_key",
                    ),
                ),
                destination=DestinationConfig_Postgres(
                    postgres=DestinationPostgresConfig(),
                ),
            ),
        )
        """
        _response = self._raw_client.pipeline_sync_batch(
            pipeline=pipeline, run_id=run_id, state_limit=state_limit, state=state, request_options=request_options
        )
        return _response.data


class AsyncStatelessSyncApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatelessSyncApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatelessSyncApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatelessSyncApiClient
        """
        return self._raw_client

    async def pipeline_check(
        self,
        *,
        pipeline: PipelineConfig,
        only: typing.Optional[PipelineCheckRequestOnly] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckOutput:
        """
        Validates the source/destination config and tests connectivity. Streams NDJSON messages (connection_status, log, trace) tagged with _emitted_by. Pass only=source or only=destination to check a single side.

        Parameters
        ----------
        pipeline : PipelineConfig

        only : typing.Optional[PipelineCheckRequestOnly]
            Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckOutput
            NDJSON stream of check messages

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            PipelineConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stateless_sync_api.pipeline_check(
                pipeline=PipelineConfig(
                    source=SourceConfig_Stripe(
                        stripe=SourceStripeConfig(
                            api_key="api_key",
                        ),
                    ),
                    destination=DestinationConfig_Postgres(
                        postgres=DestinationPostgresConfig(),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pipeline_check(pipeline=pipeline, only=only, request_options=request_options)
        return _response.data

    async def pipeline_setup(
        self,
        *,
        pipeline: PipelineConfig,
        only: typing.Optional[PipelineSetupRequestOnly] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SetupOutput:
        """
        Creates destination tables and applies migrations. Streams NDJSON messages (control, log, trace) tagged with _emitted_by. Pass only=destination to run destination setup alone (e.g. optimistic table creation) or only=source to isolate the source.

        Parameters
        ----------
        pipeline : PipelineConfig

        only : typing.Optional[PipelineSetupRequestOnly]
            Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SetupOutput
            NDJSON stream of setup messages

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            PipelineConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stateless_sync_api.pipeline_setup(
                pipeline=PipelineConfig(
                    source=SourceConfig_Stripe(
                        stripe=SourceStripeConfig(
                            api_key="api_key",
                        ),
                    ),
                    destination=DestinationConfig_Postgres(
                        postgres=DestinationPostgresConfig(),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pipeline_setup(pipeline=pipeline, only=only, request_options=request_options)
        return _response.data

    async def pipeline_teardown(
        self,
        *,
        pipeline: PipelineConfig,
        only: typing.Optional[PipelineTeardownRequestOnly] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TeardownOutput:
        """
        Drops destination tables. Streams NDJSON messages (log, trace) tagged with _emitted_by. Pass only=destination or only=source to run a single side.

        Parameters
        ----------
        pipeline : PipelineConfig

        only : typing.Optional[PipelineTeardownRequestOnly]
            Run only the source or destination side. Useful for optimistic destination setup or isolating a connector when debugging.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TeardownOutput
            NDJSON stream of teardown messages

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            PipelineConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stateless_sync_api.pipeline_teardown(
                pipeline=PipelineConfig(
                    source=SourceConfig_Stripe(
                        stripe=SourceStripeConfig(
                            api_key="api_key",
                        ),
                    ),
                    destination=DestinationConfig_Postgres(
                        postgres=DestinationPostgresConfig(),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pipeline_teardown(
            pipeline=pipeline, only=only, request_options=request_options
        )
        return _response.data

    async def source_discover(
        self, *, source: SourceDiscoverRequestSource, request_options: typing.Optional[RequestOptions] = None
    ) -> DiscoverOutput:
        """
        Streams NDJSON messages (catalog, logs, traces) for the configured source.

        Parameters
        ----------
        source : SourceDiscoverRequestSource
            Source config ({ type, ...config })

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DiscoverOutput
            NDJSON stream of discover messages

        Examples
        --------
        import asyncio

        from fern.stateless_sync_api import SourceDiscoverRequestSource

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stateless_sync_api.source_discover(
                source=SourceDiscoverRequestSource(
                    type="type",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.source_discover(source=source, request_options=request_options)
        return _response.data

    async def pipeline_read(
        self,
        *,
        pipeline: PipelineConfig,
        time_limit: typing.Optional[float] = OMIT,
        soft_time_limit: typing.Optional[float] = OMIT,
        run_id: typing.Optional[str] = OMIT,
        stdin: typing.Optional[typing.Sequence[Message]] = OMIT,
        state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Message:
        """
        Streams NDJSON messages (records, state, catalog).

        Parameters
        ----------
        pipeline : PipelineConfig

        time_limit : typing.Optional[float]
            Stop streaming after N seconds.

        soft_time_limit : typing.Optional[float]
            Soft wall-clock deadline in seconds. Stops reading from the source between messages; the destination continues to drain and flush until time_limit fires.

        run_id : typing.Optional[str]
            Optional sync run identifier used to track bounded sync progress.

        stdin : typing.Optional[typing.Sequence[Message]]
            Optional array of input messages (push mode). Without stdin, reads from the source connector (backfill mode).

        state : typing.Optional[SyncState]
            SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Message
            NDJSON stream of sync messages

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            PipelineConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stateless_sync_api.pipeline_read(
                pipeline=PipelineConfig(
                    source=SourceConfig_Stripe(
                        stripe=SourceStripeConfig(
                            api_key="api_key",
                        ),
                    ),
                    destination=DestinationConfig_Postgres(
                        postgres=DestinationPostgresConfig(),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pipeline_read(
            pipeline=pipeline,
            time_limit=time_limit,
            soft_time_limit=soft_time_limit,
            run_id=run_id,
            stdin=stdin,
            state=state,
            request_options=request_options,
        )
        return _response.data

    async def pipeline_write(
        self,
        *,
        pipeline: PipelineConfig,
        stdin: typing.Sequence[Message],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DestinationOutput:
        """
        Writes messages to the destination. Pass an array of messages in the request body.

        Parameters
        ----------
        pipeline : PipelineConfig

        stdin : typing.Sequence[Message]
            Array of messages to write to the destination.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DestinationOutput
            NDJSON stream of write result messages

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            Message_Record,
            PipelineConfig,
            RecordMessageRecord,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stateless_sync_api.pipeline_write(
                pipeline=PipelineConfig(
                    source=SourceConfig_Stripe(
                        stripe=SourceStripeConfig(
                            api_key="api_key",
                        ),
                    ),
                    destination=DestinationConfig_Postgres(
                        postgres=DestinationPostgresConfig(),
                    ),
                ),
                stdin=[
                    Message_Record(
                        record=RecordMessageRecord(
                            stream="stream",
                            data={"key": "value"},
                            emitted_at=datetime.datetime.fromisoformat(
                                "2024-01-15 09:30:00+00:00",
                            ),
                        ),
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pipeline_write(
            pipeline=pipeline, stdin=stdin, request_options=request_options
        )
        return _response.data

    async def pipeline_sync(
        self,
        *,
        pipeline: PipelineConfig,
        time_limit: typing.Optional[float] = OMIT,
        soft_time_limit: typing.Optional[float] = OMIT,
        run_id: typing.Optional[str] = OMIT,
        stdin: typing.Optional[typing.Sequence[Message]] = OMIT,
        state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SyncOutput:
        """
        Reads from the source connector and writes to the destination (backfill mode).

        Parameters
        ----------
        pipeline : PipelineConfig

        time_limit : typing.Optional[float]
            Stop streaming after N seconds.

        soft_time_limit : typing.Optional[float]
            Soft wall-clock deadline in seconds. Stops reading from the source between messages; the destination continues to drain and flush until time_limit fires.

        run_id : typing.Optional[str]
            Optional sync run identifier used to track bounded sync progress.

        stdin : typing.Optional[typing.Sequence[Message]]
            Optional array of input messages (push mode). Without stdin, reads from the source connector (backfill mode).

        state : typing.Optional[SyncState]
            SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SyncOutput
            NDJSON stream of sync messages

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            PipelineConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stateless_sync_api.pipeline_sync(
                pipeline=PipelineConfig(
                    source=SourceConfig_Stripe(
                        stripe=SourceStripeConfig(
                            api_key="api_key",
                        ),
                    ),
                    destination=DestinationConfig_Postgres(
                        postgres=DestinationPostgresConfig(),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pipeline_sync(
            pipeline=pipeline,
            time_limit=time_limit,
            soft_time_limit=soft_time_limit,
            run_id=run_id,
            stdin=stdin,
            state=state,
            request_options=request_options,
        )
        return _response.data

    async def pipeline_sync_batch(
        self,
        *,
        pipeline: PipelineConfig,
        run_id: typing.Optional[str] = OMIT,
        state_limit: typing.Optional[int] = OMIT,
        state: typing.Optional[SyncState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EofPayload:
        """
        Runs the full read → write pipeline and returns the final EofPayload as a single JSON response.

        Parameters
        ----------
        pipeline : PipelineConfig

        run_id : typing.Optional[str]
            Optional sync run identifier used to track bounded sync progress.

        state_limit : typing.Optional[int]
            Stop after yielding N source_state messages, inclusive.

        state : typing.Optional[SyncState]
            SyncState ({ source, destination, sync_run }). Falls back to empty state if invalid.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EofPayload
            Sync result

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            DestinationConfig_Postgres,
            DestinationPostgresConfig,
            PipelineConfig,
            SourceConfig_Stripe,
            SourceStripeConfig,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stateless_sync_api.pipeline_sync_batch(
                pipeline=PipelineConfig(
                    source=SourceConfig_Stripe(
                        stripe=SourceStripeConfig(
                            api_key="api_key",
                        ),
                    ),
                    destination=DestinationConfig_Postgres(
                        postgres=DestinationPostgresConfig(),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.pipeline_sync_batch(
            pipeline=pipeline, run_id=run_id, state_limit=state_limit, state=state, request_options=request_options
        )
        return _response.data
