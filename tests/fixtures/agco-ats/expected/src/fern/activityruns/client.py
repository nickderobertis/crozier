

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_build_system_shared_dto_activity_run import (
    ApiPagedResponseBuildSystemSharedDtoActivityRun,
)
from ..types.build_system_shared_dto_activity_run import BuildSystemSharedDtoActivityRun
from ..types.build_system_shared_dto_activity_run_status import BuildSystemSharedDtoActivityRunStatus
from ..types.build_system_shared_dto_activity_run_status_status import BuildSystemSharedDtoActivityRunStatusStatus
from ..types.build_system_shared_dto_activity_step import BuildSystemSharedDtoActivityStep
from ..types.build_system_shared_dto_parameter_value import BuildSystemSharedDtoParameterValue
from .raw_client import AsyncRawActivityrunsClient, RawActivityrunsClient
from .types.activity_runs_get_activity_runs_request_status import ActivityRunsGetActivityRunsRequestStatus


OMIT = typing.cast(typing.Any, ...)


class ActivityrunsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawActivityrunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawActivityrunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawActivityrunsClient
        """
        return self._raw_client

    def getactivityruns(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[ActivityRunsGetActivityRunsRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseBuildSystemSharedDtoActivityRun:
        """
        Gets a collection of ActivityRuns. When successful, the response is a PagedResponse of ActivityRuns.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        status : typing.Optional[ActivityRunsGetActivityRunsRequestStatus]
            Optional. Filter activity runs by status.  Value should be a comma separated list of status to include.
                        If not specified, the default status filter is “InProgress”.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseBuildSystemSharedDtoActivityRun
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.activityruns.getactivityruns()
        """
        _response = self._raw_client.getactivityruns(
            limit=limit, offset=offset, status=status, request_options=request_options
        )
        return _response.data

    def getactivityrun(
        self, activity_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BuildSystemSharedDtoActivityRun:
        """
        Gets an ActivityRun by ID. When successful, the response is the requested ActivityRun.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id : int
            The ID of the ActivityRun to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoActivityRun
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.activityruns.getactivityrun(
            activity_run_id=1,
        )
        """
        _response = self._raw_client.getactivityrun(activity_run_id, request_options=request_options)
        return _response.data

    def putactivityrun(
        self,
        activity_run_id_: int,
        *,
        status: BuildSystemSharedDtoActivityRunStatus,
        activity_run_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        job_activity_id: typing.Optional[int] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        steps: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id_ : int
            The ID of the ActivityRun to update ActivityRunStatus for.

        status : BuildSystemSharedDtoActivityRunStatus
            The status of this ActivityRun

        activity_run_id : typing.Optional[int]
            The identifier for the ActivityRun

        end_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time when the activity completed

        job_activity_id : typing.Optional[int]
            Read Only. The ID of the Job Activity that defines this activity run

        job_run_id : typing.Optional[int]
            Read Only. The ID of the JobRun under which this ActivityRun is executing

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]]
            The parameters used for this run of the activity.  Parameters cannot be added or removed, but output parameter values may be updated.

        start_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time when the activity started

        steps : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]]
            Read Only. The steps to be executed for the activity.  These steps come from the relationship through JobActivity down to ActivityStep

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import BuildSystemSharedDtoActivityRunStatus, FernApi

        client = FernApi()
        client.activityruns.putactivityrun(
            activity_run_id_=1,
            status=BuildSystemSharedDtoActivityRunStatus(),
        )
        """
        _response = self._raw_client.putactivityrun(
            activity_run_id_,
            status=status,
            activity_run_id=activity_run_id,
            end_date=end_date,
            job_activity_id=job_activity_id,
            job_run_id=job_run_id,
            parameters=parameters,
            start_date=start_date,
            steps=steps,
            request_options=request_options,
        )
        return _response.data

    def getactivityrunstatus(
        self, activity_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BuildSystemSharedDtoActivityRunStatus:
        """
        Gets the ActivityRunStatus of an ActivityRun.  When successful, the response is the requested ActivityRunStatus.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id : int
            The ID of the ActivityRun to get ActivityRunStatus for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoActivityRunStatus
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.activityruns.getactivityrunstatus(
            activity_run_id=1,
        )
        """
        _response = self._raw_client.getactivityrunstatus(activity_run_id, request_options=request_options)
        return _response.data

    def putactivityrunstatus(
        self,
        activity_run_id: int,
        *,
        current_step: typing.Optional[int] = OMIT,
        status: typing.Optional[BuildSystemSharedDtoActivityRunStatusStatus] = OMIT,
        step_progress: typing.Optional[int] = OMIT,
        step_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id : int
            The ID of the ActivityRun to update ActivityRunStatus for.

        current_step : typing.Optional[int]
            The activity step currently executing, indicated by numeric order

        status : typing.Optional[BuildSystemSharedDtoActivityRunStatusStatus]
            The status of the ActivityRun

        step_progress : typing.Optional[int]
            The percent progress from the currently executing step.  This value shall be null if progress is not available

        step_status : typing.Optional[str]
            The status text from the currently executing step

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.activityruns.putactivityrunstatus(
            activity_run_id=1,
        )
        """
        _response = self._raw_client.putactivityrunstatus(
            activity_run_id,
            current_step=current_step,
            status=status,
            step_progress=step_progress,
            step_status=step_status,
            request_options=request_options,
        )
        return _response.data


class AsyncActivityrunsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawActivityrunsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawActivityrunsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawActivityrunsClient
        """
        return self._raw_client

    async def getactivityruns(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        status: typing.Optional[ActivityRunsGetActivityRunsRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseBuildSystemSharedDtoActivityRun:
        """
        Gets a collection of ActivityRuns. When successful, the response is a PagedResponse of ActivityRuns.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        status : typing.Optional[ActivityRunsGetActivityRunsRequestStatus]
            Optional. Filter activity runs by status.  Value should be a comma separated list of status to include.
                        If not specified, the default status filter is “InProgress”.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseBuildSystemSharedDtoActivityRun
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.activityruns.getactivityruns()


        asyncio.run(main())
        """
        _response = await self._raw_client.getactivityruns(
            limit=limit, offset=offset, status=status, request_options=request_options
        )
        return _response.data

    async def getactivityrun(
        self, activity_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BuildSystemSharedDtoActivityRun:
        """
        Gets an ActivityRun by ID. When successful, the response is the requested ActivityRun.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id : int
            The ID of the ActivityRun to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoActivityRun
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.activityruns.getactivityrun(
                activity_run_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getactivityrun(activity_run_id, request_options=request_options)
        return _response.data

    async def putactivityrun(
        self,
        activity_run_id_: int,
        *,
        status: BuildSystemSharedDtoActivityRunStatus,
        activity_run_id: typing.Optional[int] = OMIT,
        end_date: typing.Optional[dt.datetime] = OMIT,
        job_activity_id: typing.Optional[int] = OMIT,
        job_run_id: typing.Optional[int] = OMIT,
        parameters: typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]] = OMIT,
        start_date: typing.Optional[dt.datetime] = OMIT,
        steps: typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id_ : int
            The ID of the ActivityRun to update ActivityRunStatus for.

        status : BuildSystemSharedDtoActivityRunStatus
            The status of this ActivityRun

        activity_run_id : typing.Optional[int]
            The identifier for the ActivityRun

        end_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time when the activity completed

        job_activity_id : typing.Optional[int]
            Read Only. The ID of the Job Activity that defines this activity run

        job_run_id : typing.Optional[int]
            Read Only. The ID of the JobRun under which this ActivityRun is executing

        parameters : typing.Optional[typing.Sequence[BuildSystemSharedDtoParameterValue]]
            The parameters used for this run of the activity.  Parameters cannot be added or removed, but output parameter values may be updated.

        start_date : typing.Optional[dt.datetime]
            Read Only. The UTC date and time when the activity started

        steps : typing.Optional[typing.Sequence[BuildSystemSharedDtoActivityStep]]
            Read Only. The steps to be executed for the activity.  These steps come from the relationship through JobActivity down to ActivityStep

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BuildSystemSharedDtoActivityRunStatus

        client = AsyncFernApi()


        async def main() -> None:
            await client.activityruns.putactivityrun(
                activity_run_id_=1,
                status=BuildSystemSharedDtoActivityRunStatus(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putactivityrun(
            activity_run_id_,
            status=status,
            activity_run_id=activity_run_id,
            end_date=end_date,
            job_activity_id=job_activity_id,
            job_run_id=job_run_id,
            parameters=parameters,
            start_date=start_date,
            steps=steps,
            request_options=request_options,
        )
        return _response.data

    async def getactivityrunstatus(
        self, activity_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BuildSystemSharedDtoActivityRunStatus:
        """
        Gets the ActivityRunStatus of an ActivityRun.  When successful, the response is the requested ActivityRunStatus.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id : int
            The ID of the ActivityRun to get ActivityRunStatus for.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoActivityRunStatus
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.activityruns.getactivityrunstatus(
                activity_run_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getactivityrunstatus(activity_run_id, request_options=request_options)
        return _response.data

    async def putactivityrunstatus(
        self,
        activity_run_id: int,
        *,
        current_step: typing.Optional[int] = OMIT,
        status: typing.Optional[BuildSystemSharedDtoActivityRunStatusStatus] = OMIT,
        step_progress: typing.Optional[int] = OMIT,
        step_status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the ActivityRunStatus of an ActivityRun.  The body of the PUT is the updated ActivityRunStatus.
                    When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        activity_run_id : int
            The ID of the ActivityRun to update ActivityRunStatus for.

        current_step : typing.Optional[int]
            The activity step currently executing, indicated by numeric order

        status : typing.Optional[BuildSystemSharedDtoActivityRunStatusStatus]
            The status of the ActivityRun

        step_progress : typing.Optional[int]
            The percent progress from the currently executing step.  This value shall be null if progress is not available

        step_status : typing.Optional[str]
            The status text from the currently executing step

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
            await client.activityruns.putactivityrunstatus(
                activity_run_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putactivityrunstatus(
            activity_run_id,
            current_step=current_step,
            status=status,
            step_progress=step_progress,
            step_status=step_status,
            request_options=request_options,
        )
        return _response.data
