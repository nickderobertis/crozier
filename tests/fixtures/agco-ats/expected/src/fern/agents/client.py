

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_build_system_shared_dto_agent import ApiPagedResponseBuildSystemSharedDtoAgent
from ..types.build_system_shared_dto_activity_run import BuildSystemSharedDtoActivityRun
from ..types.build_system_shared_dto_activity_run_status import BuildSystemSharedDtoActivityRunStatus
from ..types.build_system_shared_dto_activity_step import BuildSystemSharedDtoActivityStep
from ..types.build_system_shared_dto_agent import BuildSystemSharedDtoAgent
from ..types.build_system_shared_dto_agent_status import BuildSystemSharedDtoAgentStatus
from ..types.build_system_shared_dto_parameter_value import BuildSystemSharedDtoParameterValue
from ..types.build_system_shared_dto_step_configuration import BuildSystemSharedDtoStepConfiguration
from .raw_client import AsyncRawAgentsClient, RawAgentsClient


OMIT = typing.cast(typing.Any, ...)


class AgentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentsClient
        """
        return self._raw_client

    def getagents(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseBuildSystemSharedDtoAgent:
        """
        Gets a collection of Agents. When successful, the response is a PagedResponse of Agents.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseBuildSystemSharedDtoAgent
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.agents.getagents()
        """
        _response = self._raw_client.getagents(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def postagent(
        self,
        *,
        keep_alive_interval: int,
        machine_name: str,
        status: BuildSystemSharedDtoAgentStatus,
        user_id: int,
        agent_id: typing.Optional[int] = OMIT,
        step_configurations: typing.Optional[typing.Sequence[BuildSystemSharedDtoStepConfiguration]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates an Agent.  The body of the POST is the Agent to create.  The AgentID will be assigned
                    on creation of the Agent.  When successful, the response is the AgentID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        keep_alive_interval : int
            The 'Heartbeat Interval' used by the Build Agent.

        machine_name : str
            The machine name of the computer the agent is running on

        status : BuildSystemSharedDtoAgentStatus
            The agent status.

        user_id : int
            The UserID of the Agent

        agent_id : typing.Optional[int]
            The id of the Agent

        step_configurations : typing.Optional[typing.Sequence[BuildSystemSharedDtoStepConfiguration]]
            The agent's step configurations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        from fern import BuildSystemSharedDtoAgentStatus, FernApi

        client = FernApi()
        client.agents.postagent(
            keep_alive_interval=1,
            machine_name="MachineName",
            status=BuildSystemSharedDtoAgentStatus(
                online=True,
            ),
            user_id=1,
        )
        """
        _response = self._raw_client.postagent(
            keep_alive_interval=keep_alive_interval,
            machine_name=machine_name,
            status=status,
            user_id=user_id,
            agent_id=agent_id,
            step_configurations=step_configurations,
            request_options=request_options,
        )
        return _response.data

    def getcurrentagentasync(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BuildSystemSharedDtoAgent:
        """
        Gets the Agent associated with the current user. When successful, the response is the requested Agent.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoAgent
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.agents.getcurrentagentasync()
        """
        _response = self._raw_client.getcurrentagentasync(request_options=request_options)
        return _response.data

    def getcurrentagentactivityrun(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BuildSystemSharedDtoActivityRun:
        """
        Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun
                    assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
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
        client.agents.getcurrentagentactivityrun()
        """
        _response = self._raw_client.getcurrentagentactivityrun(request_options=request_options)
        return _response.data

    def getagentasync(
        self, agent_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BuildSystemSharedDtoAgent:
        """
        Gets an Agent by ID. When successful, the response is the requested Agent.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        agent_id : int
            The id of the Agent to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoAgent
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.agents.getagentasync(
            agent_id=1,
        )
        """
        _response = self._raw_client.getagentasync(agent_id, request_options=request_options)
        return _response.data

    def putagent(
        self,
        agent_id_: int,
        *,
        keep_alive_interval: int,
        machine_name: str,
        status: BuildSystemSharedDtoAgentStatus,
        user_id: int,
        agent_id: typing.Optional[int] = OMIT,
        step_configurations: typing.Optional[typing.Sequence[BuildSystemSharedDtoStepConfiguration]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates an Agent.  The body of the PUT is the updated Agent.  When successful, the response is empty.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        agent_id_ : int
            The id of the Agent to update.

        keep_alive_interval : int
            The 'Heartbeat Interval' used by the Build Agent.

        machine_name : str
            The machine name of the computer the agent is running on

        status : BuildSystemSharedDtoAgentStatus
            The agent status.

        user_id : int
            The UserID of the Agent

        agent_id : typing.Optional[int]
            The id of the Agent

        step_configurations : typing.Optional[typing.Sequence[BuildSystemSharedDtoStepConfiguration]]
            The agent's step configurations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import BuildSystemSharedDtoAgentStatus, FernApi

        client = FernApi()
        client.agents.putagent(
            agent_id_=1,
            keep_alive_interval=1,
            machine_name="MachineName",
            status=BuildSystemSharedDtoAgentStatus(
                online=True,
            ),
            user_id=1,
        )
        """
        _response = self._raw_client.putagent(
            agent_id_,
            keep_alive_interval=keep_alive_interval,
            machine_name=machine_name,
            status=status,
            user_id=user_id,
            agent_id=agent_id,
            step_configurations=step_configurations,
            request_options=request_options,
        )
        return _response.data

    def deleteagent(self, agent_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes an Agent. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        agent_id : int
            The id of the Agent to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.agents.deleteagent(
            agent_id=1,
        )
        """
        _response = self._raw_client.deleteagent(agent_id, request_options=request_options)
        return _response.data

    def getagentactivityrun(
        self, agent_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BuildSystemSharedDtoActivityRun:
        """
        Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun
                    assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        agent_id : int
            The id of the Agent to get.

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
        client.agents.getagentactivityrun(
            agent_id=1,
        )
        """
        _response = self._raw_client.getagentactivityrun(agent_id, request_options=request_options)
        return _response.data

    def putagentactivityrun(
        self,
        agent_id: int,
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
        No Documentation Found.

        Parameters
        ----------
        agent_id : int
            The id of the Agent to update.

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
        client.agents.putagentactivityrun(
            agent_id=1,
            status=BuildSystemSharedDtoActivityRunStatus(),
        )
        """
        _response = self._raw_client.putagentactivityrun(
            agent_id,
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

    def putagentstatus(
        self,
        agent_id: int,
        *,
        online: bool,
        last_status_update: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the status of an Agent.The body of the PUT is the updated Agent status.  When successful,
                    the response is empty.If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        agent_id : int
            The id of the Agent to update.

        online : bool
            Indicates if the agent is online

        last_status_update : typing.Optional[dt.datetime]
            ReadOnly. The UTC date and time of the last status update

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.agents.putagentstatus(
            agent_id=1,
            online=True,
        )
        """
        _response = self._raw_client.putagentstatus(
            agent_id, online=online, last_status_update=last_status_update, request_options=request_options
        )
        return _response.data


class AsyncAgentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentsClient
        """
        return self._raw_client

    async def getagents(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseBuildSystemSharedDtoAgent:
        """
        Gets a collection of Agents. When successful, the response is a PagedResponse of Agents.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit.  If not specified, the default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset.  If not specified, the default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseBuildSystemSharedDtoAgent
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.agents.getagents()


        asyncio.run(main())
        """
        _response = await self._raw_client.getagents(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    async def postagent(
        self,
        *,
        keep_alive_interval: int,
        machine_name: str,
        status: BuildSystemSharedDtoAgentStatus,
        user_id: int,
        agent_id: typing.Optional[int] = OMIT,
        step_configurations: typing.Optional[typing.Sequence[BuildSystemSharedDtoStepConfiguration]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> int:
        """
        Creates an Agent.  The body of the POST is the Agent to create.  The AgentID will be assigned
                    on creation of the Agent.  When successful, the response is the AgentID.  If unsuccessful, an
                    appropriate ApiError is returned.

        Parameters
        ----------
        keep_alive_interval : int
            The 'Heartbeat Interval' used by the Build Agent.

        machine_name : str
            The machine name of the computer the agent is running on

        status : BuildSystemSharedDtoAgentStatus
            The agent status.

        user_id : int
            The UserID of the Agent

        agent_id : typing.Optional[int]
            The id of the Agent

        step_configurations : typing.Optional[typing.Sequence[BuildSystemSharedDtoStepConfiguration]]
            The agent's step configurations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        int
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BuildSystemSharedDtoAgentStatus

        client = AsyncFernApi()


        async def main() -> None:
            await client.agents.postagent(
                keep_alive_interval=1,
                machine_name="MachineName",
                status=BuildSystemSharedDtoAgentStatus(
                    online=True,
                ),
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postagent(
            keep_alive_interval=keep_alive_interval,
            machine_name=machine_name,
            status=status,
            user_id=user_id,
            agent_id=agent_id,
            step_configurations=step_configurations,
            request_options=request_options,
        )
        return _response.data

    async def getcurrentagentasync(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BuildSystemSharedDtoAgent:
        """
        Gets the Agent associated with the current user. When successful, the response is the requested Agent.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoAgent
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.agents.getcurrentagentasync()


        asyncio.run(main())
        """
        _response = await self._raw_client.getcurrentagentasync(request_options=request_options)
        return _response.data

    async def getcurrentagentactivityrun(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BuildSystemSharedDtoActivityRun:
        """
        Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun
                    assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
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
            await client.agents.getcurrentagentactivityrun()


        asyncio.run(main())
        """
        _response = await self._raw_client.getcurrentagentactivityrun(request_options=request_options)
        return _response.data

    async def getagentasync(
        self, agent_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BuildSystemSharedDtoAgent:
        """
        Gets an Agent by ID. When successful, the response is the requested Agent.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        agent_id : int
            The id of the Agent to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BuildSystemSharedDtoAgent
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.agents.getagentasync(
                agent_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getagentasync(agent_id, request_options=request_options)
        return _response.data

    async def putagent(
        self,
        agent_id_: int,
        *,
        keep_alive_interval: int,
        machine_name: str,
        status: BuildSystemSharedDtoAgentStatus,
        user_id: int,
        agent_id: typing.Optional[int] = OMIT,
        step_configurations: typing.Optional[typing.Sequence[BuildSystemSharedDtoStepConfiguration]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates an Agent.  The body of the PUT is the updated Agent.  When successful, the response is empty.
                    If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        agent_id_ : int
            The id of the Agent to update.

        keep_alive_interval : int
            The 'Heartbeat Interval' used by the Build Agent.

        machine_name : str
            The machine name of the computer the agent is running on

        status : BuildSystemSharedDtoAgentStatus
            The agent status.

        user_id : int
            The UserID of the Agent

        agent_id : typing.Optional[int]
            The id of the Agent

        step_configurations : typing.Optional[typing.Sequence[BuildSystemSharedDtoStepConfiguration]]
            The agent's step configurations

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BuildSystemSharedDtoAgentStatus

        client = AsyncFernApi()


        async def main() -> None:
            await client.agents.putagent(
                agent_id_=1,
                keep_alive_interval=1,
                machine_name="MachineName",
                status=BuildSystemSharedDtoAgentStatus(
                    online=True,
                ),
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putagent(
            agent_id_,
            keep_alive_interval=keep_alive_interval,
            machine_name=machine_name,
            status=status,
            user_id=user_id,
            agent_id=agent_id,
            step_configurations=step_configurations,
            request_options=request_options,
        )
        return _response.data

    async def deleteagent(self, agent_id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes an Agent. When successful, the response is empty.  If unsuccessful, an appropriate
                    ApiError is returned.

        Parameters
        ----------
        agent_id : int
            The id of the Agent to delete.

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
            await client.agents.deleteagent(
                agent_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteagent(agent_id, request_options=request_options)
        return _response.data

    async def getagentactivityrun(
        self, agent_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BuildSystemSharedDtoActivityRun:
        """
        Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun
                    assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        agent_id : int
            The id of the Agent to get.

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
            await client.agents.getagentactivityrun(
                agent_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getagentactivityrun(agent_id, request_options=request_options)
        return _response.data

    async def putagentactivityrun(
        self,
        agent_id: int,
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
        No Documentation Found.

        Parameters
        ----------
        agent_id : int
            The id of the Agent to update.

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
            await client.agents.putagentactivityrun(
                agent_id=1,
                status=BuildSystemSharedDtoActivityRunStatus(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putagentactivityrun(
            agent_id,
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

    async def putagentstatus(
        self,
        agent_id: int,
        *,
        online: bool,
        last_status_update: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the status of an Agent.The body of the PUT is the updated Agent status.  When successful,
                    the response is empty.If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        agent_id : int
            The id of the Agent to update.

        online : bool
            Indicates if the agent is online

        last_status_update : typing.Optional[dt.datetime]
            ReadOnly. The UTC date and time of the last status update

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
            await client.agents.putagentstatus(
                agent_id=1,
                online=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putagentstatus(
            agent_id, online=online, last_status_update=last_status_update, request_options=request_options
        )
        return _response.data
