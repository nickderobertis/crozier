

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.tool_execution_response import ToolExecutionResponse
from .types.remediate_request_max_risk_level import RemediateRequestMaxRiskLevel
from .types.remediate_request_mode import RemediateRequestMode
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTroubleshootingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def execute_remediate_tool(
        self,
        *,
        mode: RemediateRequestMode,
        confidence_threshold: float,
        max_risk_level: RemediateRequestMaxRiskLevel,
        issue: typing.Optional[str] = OMIT,
        evidence: typing.Optional[str] = OMIT,
        execute_choice: typing.Optional[float] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        executed_commands: typing.Optional[typing.Sequence[str]] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ToolExecutionResponse]:
        """
        AI-powered Kubernetes issue analysis that provides root cause identification and actionable remediation steps. Unlike basic kubectl commands, this tool performs multi-step investigation, correlates cluster data, and generates intelligent solutions. Use when users want to understand WHY something is broken, not just see raw status. Ideal for: troubleshooting failures, diagnosing performance issues, analyzing pod problems, investigating networking/storage issues, or any "what's wrong" questions.

        Parameters
        ----------
        mode : RemediateRequestMode
            Execution mode: manual requires user approval, automatic executes based on thresholds

        confidence_threshold : float
            For automatic mode: minimum confidence required for execution (default: 0.8)

        max_risk_level : RemediateRequestMaxRiskLevel
            For automatic mode: maximum risk level allowed for execution (default: low)

        issue : typing.Optional[str]
            What the operator is asking for, in their own words. This is the authoritative instruction for the investigation. Telemetry, logs or manifests quoted from elsewhere belong in `evidence`, not here.

        evidence : typing.Optional[str]
            OPTIONAL. Supporting material quoted from somewhere else — log lines, events, a manifest, an alert payload — that the caller did not write themselves. It is composed into the prompt inside an untrusted-content boundary and analyzed as data; instructions appearing in it are never followed. Callers that cannot tell instruction from quoted evidence at capture time should keep sending `issue` alone, which behaves exactly as it always has.

        execute_choice : typing.Optional[float]
            Execute a previously generated choice (1=Execute via MCP, 2=Execute via agent)

        session_id : typing.Optional[str]
            Session ID from previous remediate call when executing a choice

        executed_commands : typing.Optional[typing.Sequence[str]]
            Commands that were executed to remediate the issue

        interaction_id : typing.Optional[str]
            INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ToolExecutionResponse]
            Tool execution result
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/tools/remediate",
            method="POST",
            json={
                "issue": issue,
                "evidence": evidence,
                "mode": mode,
                "confidenceThreshold": confidence_threshold,
                "maxRiskLevel": max_risk_level,
                "executeChoice": execute_choice,
                "sessionId": session_id,
                "executedCommands": executed_commands,
                "interaction_id": interaction_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolExecutionResponse,
                    parse_obj_as(
                        type_=ToolExecutionResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTroubleshootingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def execute_remediate_tool(
        self,
        *,
        mode: RemediateRequestMode,
        confidence_threshold: float,
        max_risk_level: RemediateRequestMaxRiskLevel,
        issue: typing.Optional[str] = OMIT,
        evidence: typing.Optional[str] = OMIT,
        execute_choice: typing.Optional[float] = OMIT,
        session_id: typing.Optional[str] = OMIT,
        executed_commands: typing.Optional[typing.Sequence[str]] = OMIT,
        interaction_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ToolExecutionResponse]:
        """
        AI-powered Kubernetes issue analysis that provides root cause identification and actionable remediation steps. Unlike basic kubectl commands, this tool performs multi-step investigation, correlates cluster data, and generates intelligent solutions. Use when users want to understand WHY something is broken, not just see raw status. Ideal for: troubleshooting failures, diagnosing performance issues, analyzing pod problems, investigating networking/storage issues, or any "what's wrong" questions.

        Parameters
        ----------
        mode : RemediateRequestMode
            Execution mode: manual requires user approval, automatic executes based on thresholds

        confidence_threshold : float
            For automatic mode: minimum confidence required for execution (default: 0.8)

        max_risk_level : RemediateRequestMaxRiskLevel
            For automatic mode: maximum risk level allowed for execution (default: low)

        issue : typing.Optional[str]
            What the operator is asking for, in their own words. This is the authoritative instruction for the investigation. Telemetry, logs or manifests quoted from elsewhere belong in `evidence`, not here.

        evidence : typing.Optional[str]
            OPTIONAL. Supporting material quoted from somewhere else — log lines, events, a manifest, an alert payload — that the caller did not write themselves. It is composed into the prompt inside an untrusted-content boundary and analyzed as data; instructions appearing in it are never followed. Callers that cannot tell instruction from quoted evidence at capture time should keep sending `issue` alone, which behaves exactly as it always has.

        execute_choice : typing.Optional[float]
            Execute a previously generated choice (1=Execute via MCP, 2=Execute via agent)

        session_id : typing.Optional[str]
            Session ID from previous remediate call when executing a choice

        executed_commands : typing.Optional[typing.Sequence[str]]
            Commands that were executed to remediate the issue

        interaction_id : typing.Optional[str]
            INTERNAL ONLY - Do not populate. Used for evaluation dataset generation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ToolExecutionResponse]
            Tool execution result
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/tools/remediate",
            method="POST",
            json={
                "issue": issue,
                "evidence": evidence,
                "mode": mode,
                "confidenceThreshold": confidence_threshold,
                "maxRiskLevel": max_risk_level,
                "executeChoice": execute_choice,
                "sessionId": session_id,
                "executedCommands": executed_commands,
                "interaction_id": interaction_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ToolExecutionResponse,
                    parse_obj_as(
                        type_=ToolExecutionResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
