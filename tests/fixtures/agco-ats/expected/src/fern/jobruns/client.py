

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_build_system_shared_dto_job_run import ApiPagedResponseBuildSystemSharedDtoJobRun
from ..types.build_system_shared_dto_activity_run import BuildSystemSharedDtoActivityRun
from ..types.build_system_shared_dto_job_run import BuildSystemSharedDtoJobRun
from ..types.build_system_shared_dto_job_run_status import BuildSystemSharedDtoJobRunStatus
from ..types.build_system_shared_dto_parameter_value import BuildSystemSharedDtoParameterValue
from .raw_client import AsyncRawJobrunsClient, RawJobrunsClient


OMIT = typing.cast(typing.Any, ...)


class JobrunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobrunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobrunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobrunsClient
        """
        return self._raw_client

    def getjobruns(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_activity_run_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseBuildSystemSharedDtoJobRun:
        """
        Gets a collection of JobRuns. When successful, the response is a PagedResponse of JobRuns.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        include_activity_run_details : typing.Optional[bool]
            Optional. Indicates whether to include ActivityRun details.  Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseBuildSystemSharedDtoJobRun
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.jobruns.getjobruns()
        """
        _response = self._raw_client.getjobruns(
            limit=limit,
            offset=offset,
            include_activity_run_details=include_activity_run_details,
            request_options=request_options,
        )
        return _response.data

    def postjobrun(
        self,
        *,
        activity_runs: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[BuildSystemSharedDtoJobRunStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a JobRun.  The body of the POST is the JobRun to create.  The JobRunID will be assigned on
                    creation of the JobRun.  When successful, the response is the JobRunID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        activity_runs : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]]
            The activity runs belonging to this JobRun

        end_date : typing.Optional[dt.datetime]
            The UTC date and time when the job completed

        job_id : typing.Optional[int]
            The ID of the job that defines the run

        job_run_id : typing.Optional[int]
            The ID of this JobRun

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]]
            The parameters used for this run of the job

        start_date : typing.Optional[dt.datetime]
            The UTC date and time when the job started

        status : typing.Optional[BuildSystemSharedDtoJobRunStatus]
            The status of this JobRun

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.jobruns.postjobrun()
        """
        _response = self._raw_client.postjobrun(
            activity_runs=activity_runs,
            end_date=end_date,
            job_id=job_id,
            job_run_id=job_run_id,
            parameters=parameters,
            start_date=start_date,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def getjobrun(
        self,
        job_run_id: int,
        *,
        include_activity_run_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuildSystemSharedDtoJobRun:
        """
        Gets a JobRun by ID. When successful, the response is the requested JobRun.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_run_id : int
            The ID of the JobRun to get.

        include_activity_run_details : typing.Optional[bool]
            Optional. Indicates whether to include ActivityRun details.  Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoJobRun
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.jobruns.getjobrun(
            job_run_id=1,
        )
        """
        _response = self._raw_client.getjobrun(
            job_run_id, include_activity_run_details=include_activity_run_details, request_options=request_options
        )
        return _response.data

    def putjobrun(
        self,
        job_run_id_: int,
        *,
        activity_runs: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[BuildSystemSharedDtoJobRunStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        ///
                    Updates a JobRun.  The body of the PUT is the updated JobRun.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_run_id_ : int
            The id of the JobRun to update

        activity_runs : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]]
            The activity runs belonging to this JobRun

        end_date : typing.Optional[dt.datetime]
            The UTC date and time when the job completed

        job_id : typing.Optional[int]
            The ID of the job that defines the run

        job_run_id : typing.Optional[int]
            The ID of this JobRun

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]]
            The parameters used for this run of the job

        start_date : typing.Optional[dt.datetime]
            The UTC date and time when the job started

        status : typing.Optional[BuildSystemSharedDtoJobRunStatus]
            The status of this JobRun

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.jobruns.putjobrun(
            job_run_id_=1,
        )
        """
        _response = self._raw_client.putjobrun(
            job_run_id_,
            activity_runs=activity_runs,
            end_date=end_date,
            job_id=job_id,
            job_run_id=job_run_id,
            parameters=parameters,
            start_date=start_date,
            status=status,
            request_options=request_options,
        )
        return _response.data

    def deletejobrun(self, job_run_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a JobRun. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        job_run_id : int
            The id of the JobRun to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.jobruns.deletejobrun(
            job_run_id=1,
        )
        """
        _response = self._raw_client.deletejobrun(job_run_id, request_options=request_options)
        return _response.data


class AsyncJobrunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobrunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobrunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobrunsClient
        """
        return self._raw_client

    async def getjobruns(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_activity_run_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseBuildSystemSharedDtoJobRun:
        """
        Gets a collection of JobRuns. When successful, the response is a PagedResponse of JobRuns.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        include_activity_run_details : typing.Optional[bool]
            Optional. Indicates whether to include ActivityRun details.  Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseBuildSystemSharedDtoJobRun
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.jobruns.getjobruns()


        asyncio.run(main())
        """
        _response = await self._raw_client.getjobruns(
            limit=limit,
            offset=offset,
            include_activity_run_details=include_activity_run_details,
            request_options=request_options,
        )
        return _response.data

    async def postjobrun(
        self,
        *,
        activity_runs: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[BuildSystemSharedDtoJobRunStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates a JobRun.  The body of the POST is the JobRun to create.  The JobRunID will be assigned on
                    creation of the JobRun.  When successful, the response is the JobRunID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        activity_runs : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]]
            The activity runs belonging to this JobRun

        end_date : typing.Optional[dt.datetime]
            The UTC date and time when the job completed

        job_id : typing.Optional[int]
            The ID of the job that defines the run

        job_run_id : typing.Optional[int]
            The ID of this JobRun

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]]
            The parameters used for this run of the job

        start_date : typing.Optional[dt.datetime]
            The UTC date and time when the job started

        status : typing.Optional[BuildSystemSharedDtoJobRunStatus]
            The status of this JobRun

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.jobruns.postjobrun()


        asyncio.run(main())
        """
        _response = await self._raw_client.postjobrun(
            activity_runs=activity_runs,
            end_date=end_date,
            job_id=job_id,
            job_run_id=job_run_id,
            parameters=parameters,
            start_date=start_date,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def getjobrun(
        self,
        job_run_id: int,
        *,
        include_activity_run_details: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BuildSystemSharedDtoJobRun:
        """
        Gets a JobRun by ID. When successful, the response is the requested JobRun.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_run_id : int
            The ID of the JobRun to get.

        include_activity_run_details : typing.Optional[bool]
            Optional. Indicates whether to include ActivityRun details.  Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoJobRun
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.jobruns.getjobrun(
                job_run_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getjobrun(
            job_run_id, include_activity_run_details=include_activity_run_details, request_options=request_options
        )
        return _response.data

    async def putjobrun(
        self,
        job_run_id_: int,
        *,
        activity_runs: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        job_id: typing.Optional[int] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        status: typing.Optional[BuildSystemSharedDtoJobRunStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        ///
                    Updates a JobRun.  The body of the PUT is the updated JobRun.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        job_run_id_ : int
            The id of the JobRun to update

        activity_runs : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityRun]]
            The activity runs belonging to this JobRun

        end_date : typing.Optional[dt.datetime]
            The UTC date and time when the job completed

        job_id : typing.Optional[int]
            The ID of the job that defines the run

        job_run_id : typing.Optional[int]
            The ID of this JobRun

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]]
            The parameters used for this run of the job

        start_date : typing.Optional[dt.datetime]
            The UTC date and time when the job started

        status : typing.Optional[BuildSystemSharedDtoJobRunStatus]
            The status of this JobRun

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
            await client.jobruns.putjobrun(
                job_run_id_=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putjobrun(
            job_run_id_,
            activity_runs=activity_runs,
            end_date=end_date,
            job_id=job_id,
            job_run_id=job_run_id,
            parameters=parameters,
            start_date=start_date,
            status=status,
            request_options=request_options,
        )
        return _response.data

    async def deletejobrun(self, job_run_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a JobRun. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        job_run_id : int
            The id of the JobRun to delete

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
            await client.jobruns.deletejobrun(
                job_run_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletejobrun(job_run_id, request_options=request_options)
        return _response.data
