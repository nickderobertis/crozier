

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.all_server_jobs import AllServerJobs
from ..types.analysis import Analysis
from ..types.get_job_statistics import GetJobStatistics
from ..types.get_scheduler_option import GetSchedulerOption
from ..types.info import Info
from ..types.job import Job
from ..types.license_decider import LicenseDecider
from ..types.reuser import Reuser
from ..types.scancode import Scancode
from ..types.show_job import ShowJob
from .raw_client import AsyncRawJobClient, RawJobClient
from .types.get_all_jobs_request_sort import GetAllJobsRequestSort
from .types.get_all_jobs_request_status import GetAllJobsRequestStatus
from .types.get_jobs_request_sort import GetJobsRequestSort
from .types.get_jobs_request_status import GetJobsRequestStatus
from .types.get_reports_by_upload_request_report_format import GetReportsByUploadRequestReportFormat
from .types.get_scheduler_options_by_operation_request_operation_name import (
    GetSchedulerOptionsByOperationRequestOperationName,
)
from .types.handle_scheduler_run_request_operation import HandleSchedulerRunRequestOperation


OMIT = typing.cast(typing.Any, ...)


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

    def get_jobs(
        self,
        *,
        sort: typing.Optional[GetJobsRequestSort] = None,
        status: typing.Optional[GetJobsRequestStatus] = None,
        upload: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Job]:
        """
        Returns all jobs with their status created by the logged in user

        Parameters
        ----------
        sort : typing.Optional[GetJobsRequestSort]

        status : typing.Optional[GetJobsRequestStatus]
            Returns only jobs with the selected status.

        upload : typing.Optional[int]
            Return jobs for the given upload id only

        group_name : typing.Optional[str]
            The group name to chose while accessing jobs

        limit : typing.Optional[int]

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Job]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.get_jobs()
        """
        _response = self._raw_client.get_jobs(
            sort=sort,
            status=status,
            upload=upload,
            group_name=group_name,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    def start_jobs(
        self,
        *,
        folder_id: int,
        upload_id: int,
        group_name: typing.Optional[str] = None,
        analysis: typing.Optional[Analysis] = OMIT,
        decider: typing.Optional[LicenseDecider] = OMIT,
        reuse: typing.Optional[Reuser] = OMIT,
        scancode: typing.Optional[Scancode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Schedule an Analysis of an existing upload

        Parameters
        ----------
        folder_id : int

        upload_id : int

        group_name : typing.Optional[str]
            The group name to chose while accessing jobs

        analysis : typing.Optional[Analysis]

        decider : typing.Optional[LicenseDecider]

        reuse : typing.Optional[Reuser]

        scancode : typing.Optional[Scancode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Job Scheduled with job id in message

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.start_jobs(
            folder_id=1,
            upload_id=1,
        )
        """
        _response = self._raw_client.start_jobs(
            folder_id=folder_id,
            upload_id=upload_id,
            group_name=group_name,
            analysis=analysis,
            decider=decider,
            reuse=reuse,
            scancode=scancode,
            request_options=request_options,
        )
        return _response.data

    def get_all_jobs(
        self,
        *,
        status: typing.Optional[GetAllJobsRequestStatus] = None,
        sort: typing.Optional[GetAllJobsRequestSort] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Job]:
        """
        Returns all jobs with their status created by every user. This API returns a response only if the requesting user is an Admin.

        Parameters
        ----------
        status : typing.Optional[GetAllJobsRequestStatus]
            Returns only jobs with the selected status.

        sort : typing.Optional[GetAllJobsRequestSort]

        limit : typing.Optional[int]

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Job]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.get_all_jobs()
        """
        _response = self._raw_client.get_all_jobs(
            status=status, sort=sort, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def get_scheduler_options_by_operation(
        self,
        operation_name: GetSchedulerOptionsByOperationRequestOperationName,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSchedulerOption:
        """
        Returns the scheduler options for a specific operation

        Parameters
        ----------
        operation_name : GetSchedulerOptionsByOperationRequestOperationName
            Name of the operation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSchedulerOption
            OK

        Examples
        --------
        from fern.job import GetSchedulerOptionsByOperationRequestOperationName

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.get_scheduler_options_by_operation(
            operation_name=GetSchedulerOptionsByOperationRequestOperationName.STATUS,
        )
        """
        _response = self._raw_client.get_scheduler_options_by_operation(operation_name, request_options=request_options)
        return _response.data

    def handle_scheduler_run(
        self,
        *,
        job: typing.Optional[str] = None,
        level: typing.Optional[str] = None,
        priority: typing.Optional[str] = None,
        operation: typing.Optional[HandleSchedulerRunRequestOperation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Run the scheduler with the selected options from a specific operation

        Parameters
        ----------
        job : typing.Optional[str]
            Name of the selected job

        level : typing.Optional[str]
            Level of the selected verbose

        priority : typing.Optional[str]
            Priority option selected

        operation : typing.Optional[HandleSchedulerRunRequestOperation]
            Operation to be run by the scheduler

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Scheduler run successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.handle_scheduler_run()
        """
        _response = self._raw_client.handle_scheduler_run(
            job=job, level=level, priority=priority, operation=operation, request_options=request_options
        )
        return _response.data

    def get_job_by_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Job:
        """
        Returns job with the status

        Parameters
        ----------
        id : int
            Id of the job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.get_job_by_id(
            id=1,
        )
        """
        _response = self._raw_client.get_job_by_id(id, request_options=request_options)
        return _response.data

    def get_jobs_history_per_upload(
        self, *, upload: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ShowJob]:
        """
        Returns the history of all the jobs queued based on an upload

        Parameters
        ----------
        upload : int
            Return jobs for the given upload id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ShowJob]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.get_jobs_history_per_upload(
            upload=1,
        )
        """
        _response = self._raw_client.get_jobs_history_per_upload(upload=upload, request_options=request_options)
        return _response.data

    def get_job_statistics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetJobStatistics]:
        """
        Returns the statistics of all the jobs for the Admin Dashboard

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetJobStatistics]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.get_job_statistics()
        """
        _response = self._raw_client.get_job_statistics(request_options=request_options)
        return _response.data

    def get_all_server_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> AllServerJobs:
        """
        Returns all jobs with the scheduler status for the Admin Dashboard. This API returns a response only if the requesting user is an Admin.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AllServerJobs
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.get_all_server_jobs()
        """
        _response = self._raw_client.get_all_server_jobs(request_options=request_options)
        return _response.data

    def delete_job(self, id: int, queue: int, *, request_options: typing.Optional[RequestOptions] = None) -> Info:
        """
        Deletes a job queue and all the other job queues depending on it

        Parameters
        ----------
        id : int
            Id of the Job

        queue : int
            Id of the job queue to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Job deleted successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.delete_job(
            id=1,
            queue=1,
        )
        """
        _response = self._raw_client.delete_job(id, queue, request_options=request_options)
        return _response.data

    def get_reports_by_upload(
        self,
        *,
        upload_id: int,
        report_format: GetReportsByUploadRequestReportFormat,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        List all reports available for a given upload

        Parameters
        ----------
        upload_id : int
            Id of the upload to generate the report for

        report_format : GetReportsByUploadRequestReportFormat
            Which report to be genereated

        group_name : typing.Optional[str]
            The group name to chose while generating a report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Report generation is scheduled. Link to download report will be in message

        Examples
        --------
        from fern.job import GetReportsByUploadRequestReportFormat

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.get_reports_by_upload(
            upload_id=1,
            report_format=GetReportsByUploadRequestReportFormat.DEP5,
        )
        """
        _response = self._raw_client.get_reports_by_upload(
            upload_id=upload_id, report_format=report_format, group_name=group_name, request_options=request_options
        )
        return _response.data

    def get_report_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Get a report by id

        Parameters
        ----------
        id : int
            Id the report to download

        group_name : typing.Optional[str]
            The group name to chose while downloading specific report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Required report

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.get_report_by_id(
            id=1,
        )
        """
        with self._raw_client.get_report_by_id(id, group_name=group_name, request_options=request_options) as r:
            yield from r.data


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

    async def get_jobs(
        self,
        *,
        sort: typing.Optional[GetJobsRequestSort] = None,
        status: typing.Optional[GetJobsRequestStatus] = None,
        upload: typing.Optional[int] = None,
        group_name: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Job]:
        """
        Returns all jobs with their status created by the logged in user

        Parameters
        ----------
        sort : typing.Optional[GetJobsRequestSort]

        status : typing.Optional[GetJobsRequestStatus]
            Returns only jobs with the selected status.

        upload : typing.Optional[int]
            Return jobs for the given upload id only

        group_name : typing.Optional[str]
            The group name to chose while accessing jobs

        limit : typing.Optional[int]

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Job]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.get_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs(
            sort=sort,
            status=status,
            upload=upload,
            group_name=group_name,
            limit=limit,
            page=page,
            request_options=request_options,
        )
        return _response.data

    async def start_jobs(
        self,
        *,
        folder_id: int,
        upload_id: int,
        group_name: typing.Optional[str] = None,
        analysis: typing.Optional[Analysis] = OMIT,
        decider: typing.Optional[LicenseDecider] = OMIT,
        reuse: typing.Optional[Reuser] = OMIT,
        scancode: typing.Optional[Scancode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Schedule an Analysis of an existing upload

        Parameters
        ----------
        folder_id : int

        upload_id : int

        group_name : typing.Optional[str]
            The group name to chose while accessing jobs

        analysis : typing.Optional[Analysis]

        decider : typing.Optional[LicenseDecider]

        reuse : typing.Optional[Reuser]

        scancode : typing.Optional[Scancode]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Job Scheduled with job id in message

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.start_jobs(
                folder_id=1,
                upload_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_jobs(
            folder_id=folder_id,
            upload_id=upload_id,
            group_name=group_name,
            analysis=analysis,
            decider=decider,
            reuse=reuse,
            scancode=scancode,
            request_options=request_options,
        )
        return _response.data

    async def get_all_jobs(
        self,
        *,
        status: typing.Optional[GetAllJobsRequestStatus] = None,
        sort: typing.Optional[GetAllJobsRequestSort] = None,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Job]:
        """
        Returns all jobs with their status created by every user. This API returns a response only if the requesting user is an Admin.

        Parameters
        ----------
        status : typing.Optional[GetAllJobsRequestStatus]
            Returns only jobs with the selected status.

        sort : typing.Optional[GetAllJobsRequestSort]

        limit : typing.Optional[int]

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Job]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.get_all_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_jobs(
            status=status, sort=sort, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def get_scheduler_options_by_operation(
        self,
        operation_name: GetSchedulerOptionsByOperationRequestOperationName,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetSchedulerOption:
        """
        Returns the scheduler options for a specific operation

        Parameters
        ----------
        operation_name : GetSchedulerOptionsByOperationRequestOperationName
            Name of the operation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSchedulerOption
            OK

        Examples
        --------
        import asyncio

        from fern.job import GetSchedulerOptionsByOperationRequestOperationName

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.get_scheduler_options_by_operation(
                operation_name=GetSchedulerOptionsByOperationRequestOperationName.STATUS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_scheduler_options_by_operation(
            operation_name, request_options=request_options
        )
        return _response.data

    async def handle_scheduler_run(
        self,
        *,
        job: typing.Optional[str] = None,
        level: typing.Optional[str] = None,
        priority: typing.Optional[str] = None,
        operation: typing.Optional[HandleSchedulerRunRequestOperation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Run the scheduler with the selected options from a specific operation

        Parameters
        ----------
        job : typing.Optional[str]
            Name of the selected job

        level : typing.Optional[str]
            Level of the selected verbose

        priority : typing.Optional[str]
            Priority option selected

        operation : typing.Optional[HandleSchedulerRunRequestOperation]
            Operation to be run by the scheduler

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Scheduler run successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.handle_scheduler_run()


        asyncio.run(main())
        """
        _response = await self._raw_client.handle_scheduler_run(
            job=job, level=level, priority=priority, operation=operation, request_options=request_options
        )
        return _response.data

    async def get_job_by_id(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Job:
        """
        Returns job with the status

        Parameters
        ----------
        id : int
            Id of the job

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Job
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.get_job_by_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_by_id(id, request_options=request_options)
        return _response.data

    async def get_jobs_history_per_upload(
        self, *, upload: int, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ShowJob]:
        """
        Returns the history of all the jobs queued based on an upload

        Parameters
        ----------
        upload : int
            Return jobs for the given upload id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ShowJob]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.get_jobs_history_per_upload(
                upload=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_jobs_history_per_upload(upload=upload, request_options=request_options)
        return _response.data

    async def get_job_statistics(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetJobStatistics]:
        """
        Returns the statistics of all the jobs for the Admin Dashboard

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetJobStatistics]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.get_job_statistics()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_job_statistics(request_options=request_options)
        return _response.data

    async def get_all_server_jobs(self, *, request_options: typing.Optional[RequestOptions] = None) -> AllServerJobs:
        """
        Returns all jobs with the scheduler status for the Admin Dashboard. This API returns a response only if the requesting user is an Admin.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AllServerJobs
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.get_all_server_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_server_jobs(request_options=request_options)
        return _response.data

    async def delete_job(self, id: int, queue: int, *, request_options: typing.Optional[RequestOptions] = None) -> Info:
        """
        Deletes a job queue and all the other job queues depending on it

        Parameters
        ----------
        id : int
            Id of the Job

        queue : int
            Id of the job queue to be deleted

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Job deleted successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.delete_job(
                id=1,
                queue=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_job(id, queue, request_options=request_options)
        return _response.data

    async def get_reports_by_upload(
        self,
        *,
        upload_id: int,
        report_format: GetReportsByUploadRequestReportFormat,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        List all reports available for a given upload

        Parameters
        ----------
        upload_id : int
            Id of the upload to generate the report for

        report_format : GetReportsByUploadRequestReportFormat
            Which report to be genereated

        group_name : typing.Optional[str]
            The group name to chose while generating a report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Report generation is scheduled. Link to download report will be in message

        Examples
        --------
        import asyncio

        from fern.job import GetReportsByUploadRequestReportFormat

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.get_reports_by_upload(
                upload_id=1,
                report_format=GetReportsByUploadRequestReportFormat.DEP5,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_reports_by_upload(
            upload_id=upload_id, report_format=report_format, group_name=group_name, request_options=request_options
        )
        return _response.data

    async def get_report_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Get a report by id

        Parameters
        ----------
        id : int
            Id the report to download

        group_name : typing.Optional[str]
            The group name to chose while downloading specific report

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Required report

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.get_report_by_id(
                id=1,
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_report_by_id(id, group_name=group_name, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
