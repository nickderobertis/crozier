

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.attempt_number import AttemptNumber
from ..types.attempt_stats import AttemptStats
from ..types.attempt_stream_stats import AttemptStreamStats
from ..types.attempt_sync_config import AttemptSyncConfig
from ..types.internal_operation_result import InternalOperationResult
from ..types.job_id import JobId
from ..types.workflow_id import WorkflowId
from .raw_client import AsyncRawAttemptClient, RawAttemptClient


OMIT = typing.cast(typing.Any, ...)


class AttemptClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAttemptClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAttemptClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAttemptClient
        """
        return self._raw_client

    def save_stats(
        self,
        *,
        attempt_number: AttemptNumber,
        job_id: JobId,
        stats: AttemptStats,
        stream_stats: typing.Optional[typing.Sequence[AttemptStreamStats]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InternalOperationResult:
        """
        Parameters
        ----------
        attempt_number : AttemptNumber

        job_id : JobId

        stats : AttemptStats

        stream_stats : typing.Optional[typing.Sequence[AttemptStreamStats]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalOperationResult
            Successful Operation

        Examples
        --------
        from fern import AttemptStats, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.attempt.save_stats(
            attempt_number=1,
            job_id=1000000,
            stats=AttemptStats(),
        )
        """
        _response = self._raw_client.save_stats(
            attempt_number=attempt_number,
            job_id=job_id,
            stats=stats,
            stream_stats=stream_stats,
            request_options=request_options,
        )
        return _response.data

    def save_sync_config(
        self,
        *,
        attempt_number: AttemptNumber,
        job_id: JobId,
        sync_config: AttemptSyncConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InternalOperationResult:
        """
        Parameters
        ----------
        attempt_number : AttemptNumber

        job_id : JobId

        sync_config : AttemptSyncConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalOperationResult
            Successful Operation

        Examples
        --------
        from fern import AttemptSyncConfig, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.attempt.save_sync_config(
            attempt_number=1,
            job_id=1000000,
            sync_config=AttemptSyncConfig(
                destination_configuration={"user": "charles"},
                source_configuration={"user": "charles"},
            ),
        )
        """
        _response = self._raw_client.save_sync_config(
            attempt_number=attempt_number, job_id=job_id, sync_config=sync_config, request_options=request_options
        )
        return _response.data

    def set_workflow_in_attempt(
        self,
        *,
        attempt_number: AttemptNumber,
        job_id: JobId,
        workflow_id: WorkflowId,
        processing_task_queue: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InternalOperationResult:
        """
        Parameters
        ----------
        attempt_number : AttemptNumber

        job_id : JobId

        workflow_id : WorkflowId

        processing_task_queue : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalOperationResult
            Successful Operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.attempt.set_workflow_in_attempt(
            attempt_number=1,
            job_id=1000000,
            workflow_id="workflowId",
        )
        """
        _response = self._raw_client.set_workflow_in_attempt(
            attempt_number=attempt_number,
            job_id=job_id,
            workflow_id=workflow_id,
            processing_task_queue=processing_task_queue,
            request_options=request_options,
        )
        return _response.data


class AsyncAttemptClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAttemptClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAttemptClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAttemptClient
        """
        return self._raw_client

    async def save_stats(
        self,
        *,
        attempt_number: AttemptNumber,
        job_id: JobId,
        stats: AttemptStats,
        stream_stats: typing.Optional[typing.Sequence[AttemptStreamStats]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InternalOperationResult:
        """
        Parameters
        ----------
        attempt_number : AttemptNumber

        job_id : JobId

        stats : AttemptStats

        stream_stats : typing.Optional[typing.Sequence[AttemptStreamStats]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalOperationResult
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, AttemptStats

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.attempt.save_stats(
                attempt_number=1,
                job_id=1000000,
                stats=AttemptStats(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_stats(
            attempt_number=attempt_number,
            job_id=job_id,
            stats=stats,
            stream_stats=stream_stats,
            request_options=request_options,
        )
        return _response.data

    async def save_sync_config(
        self,
        *,
        attempt_number: AttemptNumber,
        job_id: JobId,
        sync_config: AttemptSyncConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InternalOperationResult:
        """
        Parameters
        ----------
        attempt_number : AttemptNumber

        job_id : JobId

        sync_config : AttemptSyncConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalOperationResult
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, AttemptSyncConfig

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.attempt.save_sync_config(
                attempt_number=1,
                job_id=1000000,
                sync_config=AttemptSyncConfig(
                    destination_configuration={"user": "charles"},
                    source_configuration={"user": "charles"},
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.save_sync_config(
            attempt_number=attempt_number, job_id=job_id, sync_config=sync_config, request_options=request_options
        )
        return _response.data

    async def set_workflow_in_attempt(
        self,
        *,
        attempt_number: AttemptNumber,
        job_id: JobId,
        workflow_id: WorkflowId,
        processing_task_queue: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InternalOperationResult:
        """
        Parameters
        ----------
        attempt_number : AttemptNumber

        job_id : JobId

        workflow_id : WorkflowId

        processing_task_queue : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InternalOperationResult
            Successful Operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.attempt.set_workflow_in_attempt(
                attempt_number=1,
                job_id=1000000,
                workflow_id="workflowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_workflow_in_attempt(
            attempt_number=attempt_number,
            job_id=job_id,
            workflow_id=workflow_id,
            processing_task_queue=processing_task_queue,
            request_options=request_options,
        )
        return _response.data
