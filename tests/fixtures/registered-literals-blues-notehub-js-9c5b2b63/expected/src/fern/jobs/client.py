

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.batch_job_requests import BatchJobRequests
from ..types.job_definition_report_options import JobDefinitionReportOptions
from ..types.job_definition_select import JobDefinitionSelect
from ..types.job_detail import JobDetail
from ..types.job_run import JobRun
from .raw_client import AsyncRawJobsClient, RawJobsClient
from .types.cancel_job_run_response import CancelJobRunResponse
from .types.create_job_response import CreateJobResponse
from .types.delete_job_response import DeleteJobResponse
from .types.get_job_run_request_view import GetJobRunRequestView
from .types.get_job_runs_response import GetJobRunsResponse
from .types.get_jobs_response import GetJobsResponse
from .types.run_job_response import RunJobResponse


OMIT = typing.cast(typing.Any, ...)


class JobsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobsClient
        """
        return self._raw_client

    def get_jobs(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetJobsResponse:
        """
        List all batch jobs for a project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetJobsResponse
            List of batch jobs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_jobs(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_jobs(project_or_product_uid, request_options=request_options)
        return _response.data

    def create_job(
        self,
        project_or_product_uid: str,
        *,
        name: str,
        comment: typing.Optional[str] = OMIT,
        default_requests: typing.Optional[BatchJobRequests] = OMIT,
        device_requests: typing.Optional[typing.Dict[str, BatchJobRequests]] = OMIT,
        report_options: typing.Optional[JobDefinitionReportOptions] = OMIT,
        select: typing.Optional[JobDefinitionSelect] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateJobResponse:
        """
        Create a new batch job with an optional name

        Parameters
        ----------
        project_or_product_uid : str

        name : str
            Name for the job

        comment : typing.Optional[str]
            Human-readable description of the job

        default_requests : typing.Optional[BatchJobRequests]

        device_requests : typing.Optional[typing.Dict[str, BatchJobRequests]]
            Device-specific request overrides, keyed by device UID

        report_options : typing.Optional[JobDefinitionReportOptions]
            Controls what data is included in the job report

        select : typing.Optional[JobDefinitionSelect]
            Device selection criteria

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateJobResponse
            Job created successfully

        Examples
        --------
        from fern import BatchJobRequests, FernApi, JobDefinitionSelect

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.create_job(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            name="name",
            comment="Set environment variables on all devices in a fleet",
            default_requests=BatchJobRequests(
                vars_to_set={"firmware_channel": "production", "log_level": "1"},
            ),
            select=JobDefinitionSelect(
                devices_in_fleets=["fleet:00000000-0000-0000-0000-000000000000"],
            ),
        )
        """
        _response = self._raw_client.create_job(
            project_or_product_uid,
            name=name,
            comment=comment,
            default_requests=default_requests,
            device_requests=device_requests,
            report_options=report_options,
            select=select,
            request_options=request_options,
        )
        return _response.data

    def get_job(
        self, project_or_product_uid: str, job_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobDetail:
        """
        Get a specific batch job definition

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobDetail
            Batch job details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_job(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            job_uid="my-reconciliation-job",
        )
        """
        _response = self._raw_client.get_job(project_or_product_uid, job_uid, request_options=request_options)
        return _response.data

    def delete_job(
        self, project_or_product_uid: str, job_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteJobResponse:
        """
        Delete a batch job

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteJobResponse
            Job deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.delete_job(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            job_uid="my-reconciliation-job",
        )
        """
        _response = self._raw_client.delete_job(project_or_product_uid, job_uid, request_options=request_options)
        return _response.data

    def run_job(
        self,
        project_or_product_uid: str,
        job_uid: str,
        *,
        dry_run: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RunJobResponse:
        """
        Execute a batch job

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        dry_run : typing.Optional[bool]
            Run job in dry-run mode without making actual changes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunJobResponse
            Job execution started

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.run_job(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            job_uid="my-reconciliation-job",
        )
        """
        _response = self._raw_client.run_job(
            project_or_product_uid, job_uid, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    def get_job_runs(
        self,
        project_or_product_uid: str,
        job_uid: str,
        *,
        status: typing.Optional[str] = None,
        dry_run: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetJobRunsResponse:
        """
        List all runs for a specific job

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        status : typing.Optional[str]
            Filter runs by status

        dry_run : typing.Optional[bool]
            Filter runs by dry run flag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetJobRunsResponse
            List of job runs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_job_runs(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            job_uid="my-reconciliation-job",
        )
        """
        _response = self._raw_client.get_job_runs(
            project_or_product_uid, job_uid, status=status, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    def get_job_run(
        self,
        project_or_product_uid: str,
        report_uid: str,
        *,
        view: typing.Optional[GetJobRunRequestView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobRun:
        """
        Get the result of a job execution

        Parameters
        ----------
        project_or_product_uid : str

        report_uid : str
            Unique identifier for a job run report

        view : typing.Optional[GetJobRunRequestView]
            Controls the level of detail returned: 'summary' returns metadata only, 'detail' returns the full result payload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobRun
            Job run details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.get_job_run(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            report_uid="my-reconciliation-job-1707654321000",
        )
        """
        _response = self._raw_client.get_job_run(
            project_or_product_uid, report_uid, view=view, request_options=request_options
        )
        return _response.data

    def delete_job_run(
        self, project_or_product_uid: str, report_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the results of a job run

        Parameters
        ----------
        project_or_product_uid : str

        report_uid : str
            Unique identifier for a job run report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.delete_job_run(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            report_uid="my-reconciliation-job-1707654321000",
        )
        """
        _response = self._raw_client.delete_job_run(project_or_product_uid, report_uid, request_options=request_options)
        return _response.data

    def cancel_job_run(
        self, project_or_product_uid: str, report_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelJobRunResponse:
        """
        Cancel a running job execution

        Parameters
        ----------
        project_or_product_uid : str

        report_uid : str
            Unique identifier for a job run report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelJobRunResponse
            Cancel operation completed

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs.cancel_job_run(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            report_uid="my-reconciliation-job-1707654321000",
        )
        """
        _response = self._raw_client.cancel_job_run(project_or_product_uid, report_uid, request_options=request_options)
        return _response.data


class AsyncJobsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobsClient
        """
        return self._raw_client

    async def get_jobs(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetJobsResponse:
        """
        List all batch jobs for a project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetJobsResponse
            List of batch jobs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_jobs(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs(project_or_product_uid, request_options=request_options)
        return _response.data

    async def create_job(
        self,
        project_or_product_uid: str,
        *,
        name: str,
        comment: typing.Optional[str] = OMIT,
        default_requests: typing.Optional[BatchJobRequests] = OMIT,
        device_requests: typing.Optional[typing.Dict[str, BatchJobRequests]] = OMIT,
        report_options: typing.Optional[JobDefinitionReportOptions] = OMIT,
        select: typing.Optional[JobDefinitionSelect] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateJobResponse:
        """
        Create a new batch job with an optional name

        Parameters
        ----------
        project_or_product_uid : str

        name : str
            Name for the job

        comment : typing.Optional[str]
            Human-readable description of the job

        default_requests : typing.Optional[BatchJobRequests]

        device_requests : typing.Optional[typing.Dict[str, BatchJobRequests]]
            Device-specific request overrides, keyed by device UID

        report_options : typing.Optional[JobDefinitionReportOptions]
            Controls what data is included in the job report

        select : typing.Optional[JobDefinitionSelect]
            Device selection criteria

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateJobResponse
            Job created successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BatchJobRequests, JobDefinitionSelect

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.create_job(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                name="name",
                comment="Set environment variables on all devices in a fleet",
                default_requests=BatchJobRequests(
                    vars_to_set={"firmware_channel": "production", "log_level": "1"},
                ),
                select=JobDefinitionSelect(
                    devices_in_fleets=["fleet:00000000-0000-0000-0000-000000000000"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_job(
            project_or_product_uid,
            name=name,
            comment=comment,
            default_requests=default_requests,
            device_requests=device_requests,
            report_options=report_options,
            select=select,
            request_options=request_options,
        )
        return _response.data

    async def get_job(
        self, project_or_product_uid: str, job_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JobDetail:
        """
        Get a specific batch job definition

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobDetail
            Batch job details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_job(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                job_uid="my-reconciliation-job",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job(project_or_product_uid, job_uid, request_options=request_options)
        return _response.data

    async def delete_job(
        self, project_or_product_uid: str, job_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteJobResponse:
        """
        Delete a batch job

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteJobResponse
            Job deleted successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.delete_job(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                job_uid="my-reconciliation-job",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_job(project_or_product_uid, job_uid, request_options=request_options)
        return _response.data

    async def run_job(
        self,
        project_or_product_uid: str,
        job_uid: str,
        *,
        dry_run: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RunJobResponse:
        """
        Execute a batch job

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        dry_run : typing.Optional[bool]
            Run job in dry-run mode without making actual changes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RunJobResponse
            Job execution started

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.run_job(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                job_uid="my-reconciliation-job",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_job(
            project_or_product_uid, job_uid, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    async def get_job_runs(
        self,
        project_or_product_uid: str,
        job_uid: str,
        *,
        status: typing.Optional[str] = None,
        dry_run: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetJobRunsResponse:
        """
        List all runs for a specific job

        Parameters
        ----------
        project_or_product_uid : str

        job_uid : str
            Unique identifier for a batch job

        status : typing.Optional[str]
            Filter runs by status

        dry_run : typing.Optional[bool]
            Filter runs by dry run flag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetJobRunsResponse
            List of job runs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_job_runs(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                job_uid="my-reconciliation-job",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_runs(
            project_or_product_uid, job_uid, status=status, dry_run=dry_run, request_options=request_options
        )
        return _response.data

    async def get_job_run(
        self,
        project_or_product_uid: str,
        report_uid: str,
        *,
        view: typing.Optional[GetJobRunRequestView] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JobRun:
        """
        Get the result of a job execution

        Parameters
        ----------
        project_or_product_uid : str

        report_uid : str
            Unique identifier for a job run report

        view : typing.Optional[GetJobRunRequestView]
            Controls the level of detail returned: 'summary' returns metadata only, 'detail' returns the full result payload

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JobRun
            Job run details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.get_job_run(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                report_uid="my-reconciliation-job-1707654321000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_run(
            project_or_product_uid, report_uid, view=view, request_options=request_options
        )
        return _response.data

    async def delete_job_run(
        self, project_or_product_uid: str, report_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete the results of a job run

        Parameters
        ----------
        project_or_product_uid : str

        report_uid : str
            Unique identifier for a job run report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.delete_job_run(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                report_uid="my-reconciliation-job-1707654321000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_job_run(
            project_or_product_uid, report_uid, request_options=request_options
        )
        return _response.data

    async def cancel_job_run(
        self, project_or_product_uid: str, report_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelJobRunResponse:
        """
        Cancel a running job execution

        Parameters
        ----------
        project_or_product_uid : str

        report_uid : str
            Unique identifier for a job run report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelJobRunResponse
            Cancel operation completed

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs.cancel_job_run(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                report_uid="my-reconciliation-job-1707654321000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_job_run(
            project_or_product_uid, report_uid, request_options=request_options
        )
        return _response.data
