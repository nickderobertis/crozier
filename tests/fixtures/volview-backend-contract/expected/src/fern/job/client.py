

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.job_history_detail import JobHistoryDetail
from ..types.job_results import JobResults
from ..types.neutral_job_status import NeutralJobStatus
from .raw_client import AsyncRawJobClient, RawJobClient


class JobClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobClient
        """
        return self._raw_client

    def get_job_history_detail(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobHistoryDetail:
        """
        Parameters
        ----------
        job_id : str
            Opaque job identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobHistoryDetail
            The detail-only job fields.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.job.get_job_history_detail(
            job_id="jobId",
        )
        """
        _response = self._raw_client.get_job_history_detail(job_id, request_options=request_options)
        return _response.data

    def get_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> NeutralJobStatus:
        """
        Parameters
        ----------
        job_id : str
            Opaque job identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NeutralJobStatus
            The neutral job status.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.job.get_job(
            job_id="jobId",
        )
        """
        _response = self._raw_client.get_job(job_id, request_options=request_options)
        return _response.data

    def delete_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletion is CASCADING, and the cascade is normative: removing the execution record also removes the results it produced and any staged inputs it still owns. A conforming backend MUST NOT retain results for a deleted record, so a client may truthfully tell the user that deleting the job deletes its results. Only a terminal (success / error / cancelled) job is deletable; a non-terminal job is refused with 409 — cancel it and delete once it settles.

        Parameters
        ----------
        job_id : str
            Opaque job identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.job.delete_job(
            job_id="jobId",
        )
        """
        _response = self._raw_client.delete_job(job_id, request_options=request_options)
        return _response.data

    def get_job_results(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> JobResults:
        """
        Parameters
        ----------
        job_id : str
            Opaque job identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResults
            The resolved results as the { resultState, intents, missing } envelope (JobResults). Each entry of `intents` is a ResultIntent — a result row carrying a required `id` display key and required `name`/`url`, plus optional/null `mimeType`/`size` file metadata. `missing` counts declared outputs that never arrived plus recorded outputs that cannot be read. Total loss is a valid incomplete response with an empty intents array.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.job.get_job_results(
            job_id="jobId",
        )
        """
        _response = self._raw_client.get_job_results(job_id, request_options=request_options)
        return _response.data

    def cancel_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> NeutralJobStatus:
        """
        Parameters
        ----------
        job_id : str
            Opaque job identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NeutralJobStatus
            The projected job status after the cancel attempt.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.job.cancel_job(
            job_id="jobId",
        )
        """
        _response = self._raw_client.cancel_job(job_id, request_options=request_options)
        return _response.data


class AsyncJobClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobClient
        """
        return self._raw_client

    async def get_job_history_detail(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobHistoryDetail:
        """
        Parameters
        ----------
        job_id : str
            Opaque job identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobHistoryDetail
            The detail-only job fields.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.job.get_job_history_detail(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_history_detail(job_id, request_options=request_options)
        return _response.data

    async def get_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NeutralJobStatus:
        """
        Parameters
        ----------
        job_id : str
            Opaque job identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NeutralJobStatus
            The neutral job status.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.job.get_job(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job(job_id, request_options=request_options)
        return _response.data

    async def delete_job(self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletion is CASCADING, and the cascade is normative: removing the execution record also removes the results it produced and any staged inputs it still owns. A conforming backend MUST NOT retain results for a deleted record, so a client may truthfully tell the user that deleting the job deletes its results. Only a terminal (success / error / cancelled) job is deletable; a non-terminal job is refused with 409 — cancel it and delete once it settles.

        Parameters
        ----------
        job_id : str
            Opaque job identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.job.delete_job(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_job(job_id, request_options=request_options)
        return _response.data

    async def get_job_results(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobResults:
        """
        Parameters
        ----------
        job_id : str
            Opaque job identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobResults
            The resolved results as the { resultState, intents, missing } envelope (JobResults). Each entry of `intents` is a ResultIntent — a result row carrying a required `id` display key and required `name`/`url`, plus optional/null `mimeType`/`size` file metadata. `missing` counts declared outputs that never arrived plus recorded outputs that cannot be read. Total loss is a valid incomplete response with an empty intents array.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.job.get_job_results(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_results(job_id, request_options=request_options)
        return _response.data

    async def cancel_job(
        self, job_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> NeutralJobStatus:
        """
        Parameters
        ----------
        job_id : str
            Opaque job identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        NeutralJobStatus
            The projected job status after the cancel attempt.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.job.cancel_job(
                job_id="jobId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_job(job_id, request_options=request_options)
        return _response.data
