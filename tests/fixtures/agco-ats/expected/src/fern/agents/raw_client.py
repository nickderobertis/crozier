

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.api_paged_response_build_system_shared_dto_agent import ApiPagedResponseBuildSystemSharedDtoAgent
from ..types.build_system_shared_dto_activity_run import BuildSystemSharedDtoActivityRun
from ..types.build_system_shared_dto_activity_run_status import BuildSystemSharedDtoActivityRunStatus
from ..types.build_system_shared_dto_activity_step import BuildSystemSharedDtoActivityStep
from ..types.build_system_shared_dto_agent import BuildSystemSharedDtoAgent
from ..types.build_system_shared_dto_agent_status import BuildSystemSharedDtoAgentStatus
from ..types.build_system_shared_dto_parameter_value import BuildSystemSharedDtoParameterValue
from ..types.build_system_shared_dto_step_configuration import BuildSystemSharedDtoStepConfiguration
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAgentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getagents(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApiPagedResponseBuildSystemSharedDtoAgent]:
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
        HttpResponse[ApiPagedResponseBuildSystemSharedDtoAgent]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/agents",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseBuildSystemSharedDtoAgent,
                    parse_obj_as(
                        type_=ApiPagedResponseBuildSystemSharedDtoAgent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[int]:
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
        HttpResponse[int]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/agents",
            method="POST",
            json={
                "AgentID": agent_id,
                "KeepAliveInterval": keep_alive_interval,
                "MachineName": machine_name,
                "Status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=BuildSystemSharedDtoAgentStatus, direction="write"
                ),
                "StepConfigurations": convert_and_respect_annotation_metadata(
                    object_=step_configurations,
                    annotation=typing.Sequence[BuildSystemSharedDtoStepConfiguration],
                    direction="write",
                ),
                "UserID": user_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getcurrentagentasync(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BuildSystemSharedDtoAgent]:
        """
        Gets the Agent associated with the current user. When successful, the response is the requested Agent.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BuildSystemSharedDtoAgent]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/agents/Current",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoAgent,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoAgent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getcurrentagentactivityrun(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BuildSystemSharedDtoActivityRun]:
        """
        Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun
                    assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BuildSystemSharedDtoActivityRun]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/agents/Current/ActivityRun",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoActivityRun,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoActivityRun,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getagentasync(
        self, agent_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BuildSystemSharedDtoAgent]:
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
        HttpResponse[BuildSystemSharedDtoAgent]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/agents/{encode_path_param(agent_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoAgent,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoAgent,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/agents/{encode_path_param(agent_id_)}",
            method="PUT",
            json={
                "AgentID": agent_id,
                "KeepAliveInterval": keep_alive_interval,
                "MachineName": machine_name,
                "Status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=BuildSystemSharedDtoAgentStatus, direction="write"
                ),
                "StepConfigurations": convert_and_respect_annotation_metadata(
                    object_=step_configurations,
                    annotation=typing.Sequence[BuildSystemSharedDtoStepConfiguration],
                    direction="write",
                ),
                "UserID": user_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deleteagent(
        self, agent_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/agents/{encode_path_param(agent_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getagentactivityrun(
        self, agent_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BuildSystemSharedDtoActivityRun]:
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
        HttpResponse[BuildSystemSharedDtoActivityRun]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/agents/{encode_path_param(agent_id)}/ActivityRun",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoActivityRun,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoActivityRun,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/agents/{encode_path_param(agent_id)}/ActivityRun",
            method="PUT",
            json={
                "ActivityRunID": activity_run_id,
                "EndDate": end_date,
                "JobActivityID": job_activity_id,
                "JobRunID": job_run_id,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Sequence[BuildSystemSharedDtoParameterValue],
                    direction="write",
                ),
                "StartDate": start_date,
                "Status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=BuildSystemSharedDtoActivityRunStatus, direction="write"
                ),
                "Steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[BuildSystemSharedDtoActivityStep], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def putagentstatus(
        self,
        agent_id: int,
        *,
        online: bool,
        last_status_update: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/agents/{encode_path_param(agent_id)}/Status",
            method="PUT",
            json={
                "LastStatusUpdate": last_status_update,
                "Online": online,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAgentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getagents(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApiPagedResponseBuildSystemSharedDtoAgent]:
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
        AsyncHttpResponse[ApiPagedResponseBuildSystemSharedDtoAgent]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/agents",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApiPagedResponseBuildSystemSharedDtoAgent,
                    parse_obj_as(
                        type_=ApiPagedResponseBuildSystemSharedDtoAgent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[int]:
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
        AsyncHttpResponse[int]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/agents",
            method="POST",
            json={
                "AgentID": agent_id,
                "KeepAliveInterval": keep_alive_interval,
                "MachineName": machine_name,
                "Status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=BuildSystemSharedDtoAgentStatus, direction="write"
                ),
                "StepConfigurations": convert_and_respect_annotation_metadata(
                    object_=step_configurations,
                    annotation=typing.Sequence[BuildSystemSharedDtoStepConfiguration],
                    direction="write",
                ),
                "UserID": user_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    int,
                    parse_obj_as(
                        type_=int,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getcurrentagentasync(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BuildSystemSharedDtoAgent]:
        """
        Gets the Agent associated with the current user. When successful, the response is the requested Agent.  If unsuccessful,
                    an appropriate ApiError is returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BuildSystemSharedDtoAgent]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/agents/Current",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoAgent,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoAgent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getcurrentagentactivityrun(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BuildSystemSharedDtoActivityRun]:
        """
        Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun
                    assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BuildSystemSharedDtoActivityRun]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/agents/Current/ActivityRun",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoActivityRun,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoActivityRun,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getagentasync(
        self, agent_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BuildSystemSharedDtoAgent]:
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
        AsyncHttpResponse[BuildSystemSharedDtoAgent]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/agents/{encode_path_param(agent_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoAgent,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoAgent,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/agents/{encode_path_param(agent_id_)}",
            method="PUT",
            json={
                "AgentID": agent_id,
                "KeepAliveInterval": keep_alive_interval,
                "MachineName": machine_name,
                "Status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=BuildSystemSharedDtoAgentStatus, direction="write"
                ),
                "StepConfigurations": convert_and_respect_annotation_metadata(
                    object_=step_configurations,
                    annotation=typing.Sequence[BuildSystemSharedDtoStepConfiguration],
                    direction="write",
                ),
                "UserID": user_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deleteagent(
        self, agent_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/agents/{encode_path_param(agent_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getagentactivityrun(
        self, agent_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BuildSystemSharedDtoActivityRun]:
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
        AsyncHttpResponse[BuildSystemSharedDtoActivityRun]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/agents/{encode_path_param(agent_id)}/ActivityRun",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BuildSystemSharedDtoActivityRun,
                    parse_obj_as(
                        type_=BuildSystemSharedDtoActivityRun,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/agents/{encode_path_param(agent_id)}/ActivityRun",
            method="PUT",
            json={
                "ActivityRunID": activity_run_id,
                "EndDate": end_date,
                "JobActivityID": job_activity_id,
                "JobRunID": job_run_id,
                "Parameters": convert_and_respect_annotation_metadata(
                    object_=parameters,
                    annotation=typing.Sequence[BuildSystemSharedDtoParameterValue],
                    direction="write",
                ),
                "StartDate": start_date,
                "Status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=BuildSystemSharedDtoActivityRunStatus, direction="write"
                ),
                "Steps": convert_and_respect_annotation_metadata(
                    object_=steps, annotation=typing.Sequence[BuildSystemSharedDtoActivityStep], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def putagentstatus(
        self,
        agent_id: int,
        *,
        online: bool,
        last_status_update: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/agents/{encode_path_param(agent_id)}/Status",
            method="PUT",
            json={
                "LastStatusUpdate": last_status_update,
                "Online": online,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
